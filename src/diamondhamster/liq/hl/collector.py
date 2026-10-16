"""Sammler: Trades, Marktzustand und Positionen aller bekannten Konten mitschneiden (Spec 3.1–3.3).

Netzwerk steckt hinter `http` (post(body) -> json) und `ws_connect` (async Kontextmanager mit send/recv),
damit alles ohne Netz testbar ist.
"""
from __future__ import annotations

import asyncio
import json
import logging
import time

from . import api
from .known import KnownBook
from .scheduler import Scheduler
from .store import Store

log = logging.getLogger("hl-collector")
MIN = 60_000
QUARTER = 15 * MIN
PAUSE_MS = 90_000
SLOWDOWN_MS = 5 * MIN


class Collector:
    MARKET_WEIGHT = 30  # ctx 20/min + Kerzen 2×20 alle 5 min + Funding 2×20 stündlich, aufgerundet

    def __init__(self, store: Store, http, ws_connect, coins: tuple[str, ...] = ("BTC", "ETH"),
                 clock=time.time, budget_per_min: int = 600):
        self.store, self.http, self.ws_connect, self.coins = store, http, ws_connect, tuple(coins)
        self.clock, self.budget = clock, budget_per_min
        state = store.load_state() or {}
        self.sched = Scheduler.from_state(state["scheduler"]) if "scheduler" in state else Scheduler(self.now())
        self.last_funding: dict[str, int] = dict(state.get("last_funding", {}))
        self.known = KnownBook()
        self.ctx: dict[str, dict] = {}
        self.slow_until = 0
        self.last_tick: int | None = None
        self.last_candles = self.last_funding_fetch = -10**15
        self.polls: list[int] = []
        self.errors = 0
        self.ws_up = False

    def now(self) -> int:
        return int(self.clock() * 1000)

    # --- Trades ---------------------------------------------------------------------------------
    def on_message(self, raw: str, now: int) -> None:
        for t in api.parse_trades(json.loads(raw)):
            self.store.append("trades", {**t, "rt": now}, t["ts"], coin=t["coin"])
            self.sched.seen_in_trade(t["buyer"], now)
            self.sched.seen_in_trade(t["seller"], now)

    async def ws_loop(self, stop: asyncio.Event, backoff_start: float = 1.0) -> None:
        backoff, down_since = backoff_start, None
        while not stop.is_set():
            try:
                async with self.ws_connect() as conn:
                    for coin in self.coins:
                        await conn.send(json.dumps({"method": "subscribe",
                                                    "subscription": {"type": "trades", "coin": coin}}))
                    if down_since is not None:
                        self.store.gap(down_since, self.now(), "ws")
                        down_since = None
                    backoff, self.ws_up = backoff_start, True
                    while not stop.is_set():
                        try:
                            msg = await asyncio.wait_for(conn.recv(), 30)
                        except asyncio.TimeoutError:
                            await conn.send(json.dumps({"method": "ping"}))
                            continue
                        self.on_message(msg, self.now())
            except asyncio.CancelledError:
                raise
            except Exception as e:  # Netz weg, Server schließt: neu verbinden
                self.ws_up = False
                log.warning("WebSocket getrennt: %s", e)
                if down_since is None:
                    down_since = self.now()
                await asyncio.sleep(backoff)
                backoff = min(backoff * 2, 60.0)

    # --- Marktdaten -----------------------------------------------------------------------------
    def step_market(self, now: int) -> None:
        self.ctx = api.parse_ctx(self.http.post({"type": "metaAndAssetCtxs"}), self.coins)
        self.store.append("ctx", {"t": now, "coins": self.ctx}, now)
        if now - self.last_candles >= 5 * MIN:
            self.last_candles = now
            for coin in self.coins:
                req = {"coin": coin, "interval": "1m", "startTime": now - 10 * MIN, "endTime": now}
                for c in api.parse_candles(self.http.post({"type": "candleSnapshot", "req": req})):
                    self.store.append("candles", c, c["ts"], coin=coin)
        if now - self.last_funding_fetch >= 60 * MIN:
            self.last_funding_fetch = now
            for coin in self.coins:
                start = self.last_funding.get(coin, now - 2 * 60 * MIN) + 1
                for f in api.parse_funding(self.http.post({"type": "fundingHistory", "coin": coin,
                                                           "startTime": start})):
                    if f["ts"] > self.last_funding.get(coin, -1):
                        self.store.append("funding", f, f["ts"], coin=coin)
                        self.last_funding[coin] = f["ts"]

    # --- Positionen -----------------------------------------------------------------------------
    def poll_rate(self, now: int) -> float:
        rate = (self.budget - self.MARKET_WEIGHT) / api.WEIGHTS["clearinghouseState"]
        return rate / 2 if now < self.slow_until else rate

    def fetch_positions(self, users: list[str]) -> list[tuple[str, object]]:
        out: list[tuple[str, object]] = []
        for i, user in enumerate(users):
            try:
                out.append((user, self.http.post({"type": "clearinghouseState", "user": user})))
            except api.RateLimited as e:
                out.extend((u, e) for u in users[i:])
                break
            except Exception as e:
                out.append((user, e))
        return out

    def apply_positions(self, results: list[tuple[str, object]], now: int) -> int:
        ok = 0
        for user, resp in results:
            if isinstance(resp, Exception):
                self.sched.failed(user, now)
                self.errors += 1
                if isinstance(resp, api.RateLimited):
                    self.slow_until = now + SLOWDOWN_MS
                continue
            pos = api.parse_positions(resp, self.coins)
            self.store.append("positions", {"t": now, "user": user, "positions": pos}, now)
            self.known.update(user, pos, now)
            self.sched.polled(user, self.known.notional(user), bool(pos), now)
            self.polls.append(now)
            ok += 1
        return ok

    def step_poll(self, now: int, n: int) -> int:
        return self.apply_positions(self.fetch_positions(self.sched.take(n, now)), now)

    # --- Zustand --------------------------------------------------------------------------------
    def tick(self, now: int) -> None:
        if self.last_tick is not None and now - self.last_tick > PAUSE_MS:
            self.store.gap(self.last_tick, now, "pause")  # Mac schlief oder Prozess hing
        self.last_tick = now

    def status(self, now: int) -> dict:
        self.polls = [t for t in self.polls if t > now - MIN]
        return {"t": now, "users": len(self.sched), "users_with_pos": len(self.known),
                "coverage": {c: self.known.coverage(c, self.ctx.get(c, {}).get("oi", 0.0), now)
                             for c in self.coins},
                "polls_last_min": len(self.polls), "lateness_s": self.sched.lateness_ms(now) / 1000,
                "errors": self.errors, "ws_connected": self.ws_up, "slowed": now < self.slow_until}

    def save(self, now: int) -> None:
        self.store.flush()
        self.store.write_status(self.status(now))
        self.store.save_state({"scheduler": self.sched.to_state(), "last_funding": self.last_funding})

    def step_snapshot(self, now: int) -> None:
        for coin in self.coins:
            self.store.write_book(coin, now, self.known.rows(coin, now))
        self.save(now)

    # --- Schleifen ------------------------------------------------------------------------------
    async def market_loop(self, stop: asyncio.Event) -> None:
        while not stop.is_set():
            try:
                await asyncio.to_thread(self.step_market, self.now())
            except Exception as e:
                self.errors += 1
                log.warning("Marktdaten fehlgeschlagen: %s", e)
            await _sleep_until_next(stop, MIN, self.now())

    async def poll_loop(self, stop: asyncio.Event) -> None:
        acc = 0.0
        while not stop.is_set():
            now = self.now()
            self.tick(now)
            acc = min(acc + self.poll_rate(now) / 60, self.poll_rate(now))
            n = int(acc)
            acc -= n
            users = self.sched.take(n, now)
            if users:
                results = await asyncio.to_thread(self.fetch_positions, users)
                self.apply_positions(results, self.now())
            await _sleep_until_next(stop, 1000, self.now())

    async def snapshot_loop(self, stop: asyncio.Event) -> None:
        last_q = self.now() // QUARTER
        while not stop.is_set():
            await _sleep_until_next(stop, MIN, self.now())
            now = self.now()
            if now // QUARTER != last_q:
                last_q = now // QUARTER
                self.step_snapshot(now)
                self.sched.drop_stale(now)
            else:
                self.save(now)

    async def run(self, stop: asyncio.Event) -> None:
        tasks = [asyncio.create_task(f(stop)) for f in (self.ws_loop, self.market_loop, self.poll_loop,
                                                        self.snapshot_loop)]
        try:
            await stop.wait()
        finally:
            for t in tasks:
                t.cancel()
            await asyncio.gather(*tasks, return_exceptions=True)
            self.save(self.now())
            self.store.close()


async def _sleep_until_next(stop: asyncio.Event, period_ms: int, now: int) -> None:
    delay = (period_ms - now % period_ms) / 1000
    try:
        await asyncio.wait_for(stop.wait(), timeout=delay)
    except asyncio.TimeoutError:
        pass
