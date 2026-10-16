import asyncio
import json

import pytest

from diamondhamster.liq.hl import api
from diamondhamster.liq.hl.collector import Collector
from diamondhamster.liq.hl.store import Store, read_jsonl_gz

T0 = 1_790_000_000_000
CTX = [{"universe": [{"name": "BTC", "maxLeverage": 40}, {"name": "ETH", "maxLeverage": 25}]},
       [{"funding": "0.00001", "openInterest": "10", "markPx": "100000"},
        {"funding": "0.00001", "openInterest": "100", "markPx": "3000"}]]


def chs(qty="1.0"):
    return {"assetPositions": [{"position": {"coin": "BTC", "entryPx": "100000", "szi": qty,
            "leverage": {"type": "cross", "value": 10}, "liquidationPx": "91000"}}]}


class FakeHttp:
    def __init__(self, rate_limit_after=None):
        self.calls, self.rate_limit_after = [], rate_limit_after

    def post(self, body):
        self.calls.append(body)
        t = body["type"]
        if t == "clearinghouseState":
            n = sum(c["type"] == t for c in self.calls)
            if self.rate_limit_after is not None and n > self.rate_limit_after:
                raise api.RateLimited("429")
            return chs()
        if t == "metaAndAssetCtxs":
            return CTX
        if t == "candleSnapshot":
            return [{"t": T0 - 60_000, "h": "100100", "l": "99900"}]
        if t == "fundingHistory":
            return [{"coin": body["coin"], "fundingRate": "0.00001", "premium": "0", "time": T0}]
        raise AssertionError(t)


class Clock:
    def __init__(self, t):
        self.t = t

    def __call__(self):
        return self.t / 1000


_made = []


@pytest.fixture(autouse=True)
def _close_stores():
    yield
    while _made:
        _made.pop().store.close()


def make(tmp_path, http=None, ws=None, budget=600):
    clock = Clock(T0)
    c = Collector(Store(tmp_path), http or FakeHttp(), ws, clock=clock, budget_per_min=budget)
    _made.append(c)
    return c, clock


def trade_msg(buyer="0xb", seller="0xs"):
    return json.dumps({"channel": "trades", "data": [{"coin": "BTC", "side": "B", "px": "100000", "sz": "0.1",
                       "hash": "0x", "time": T0, "tid": 1, "users": [buyer, seller]}]})


def test_trade_message_queues_both_users_and_stores_trade(tmp_path):
    c, _ = make(tmp_path)
    c.on_message(trade_msg(), T0)
    c.store.flush()
    assert sorted(c.sched.take(10, T0)) == ["0xb", "0xs"]
    recs, _ = read_jsonl_gz(tmp_path / "raw/trades/BTC/2026-09-21.jsonl.gz")
    assert recs[0]["buyer"] == "0xb" and recs[0]["rt"] == T0


def test_poll_respects_budget_and_updates_book(tmp_path):
    c, _ = make(tmp_path)
    for i in range(50):
        c.sched.seen_in_trade(f"u{i}", T0)
    done = c.step_poll(T0, 10)
    assert done == 10 and len(c.known) == 10
    assert c.poll_rate(T0) == pytest.approx((600 - c.MARKET_WEIGHT) / 2)


def test_rate_limit_halves_tempo_for_5_minutes(tmp_path):
    c, _ = make(tmp_path, http=FakeHttp(rate_limit_after=2))
    for i in range(10):
        c.sched.seen_in_trade(f"u{i}", T0)
    full = c.poll_rate(T0)
    c.step_poll(T0, 10)
    assert c.poll_rate(T0 + 1000) == pytest.approx(full / 2)
    assert c.poll_rate(T0 + 300_001) == pytest.approx(full)
    assert len(c.sched.take(100, T0 + 60_000)) == 8  # gescheiterte Abfragen kommen nach 1 min wieder


def test_market_step_stores_ctx_candles_funding(tmp_path):
    c, _ = make(tmp_path)
    c.step_market(T0)
    c.store.flush()
    ctx, _ = read_jsonl_gz(tmp_path / "raw/ctx/2026-09-21.jsonl.gz")
    assert ctx[0]["coins"]["BTC"]["oi"] == 10.0 and ctx[0]["t"] == T0
    assert (tmp_path / "raw/candles/ETH/2026-09-21.jsonl.gz").exists()
    assert (tmp_path / "raw/funding/BTC/2026-09-21.jsonl.gz").exists()
    calls = len(c.http.calls)
    c.step_market(T0 + 60_000)  # eine Minute später: nur ctx
    assert [x["type"] for x in c.http.calls[calls:]] == ["metaAndAssetCtxs"]


def test_funding_not_stored_twice(tmp_path):
    c, _ = make(tmp_path)
    c.step_market(T0)
    c.step_market(T0 + 3_600_000)
    c.store.flush()
    recs, _ = read_jsonl_gz(tmp_path / "raw/funding/BTC/2026-09-21.jsonl.gz")
    assert len(recs) == 1


def test_snapshot_writes_book_status_state(tmp_path):
    c, _ = make(tmp_path)
    c.sched.seen_in_trade("a", T0)
    c.step_market(T0)
    c.step_poll(T0, 5)
    c.step_snapshot(T0)
    status = json.loads((tmp_path / "status.json").read_text())
    assert status["coverage"]["BTC"]["long"] == pytest.approx(0.1)
    assert status["users"] == 1 and status["users_with_pos"] == 1
    assert list((tmp_path / "book/BTC").glob("*.csv.gz"))
    assert json.loads((tmp_path / "state.json").read_text())["scheduler"]["users"]["a"]


def test_restart_restores_users(tmp_path):
    c, _ = make(tmp_path)
    c.sched.seen_in_trade("a", T0)
    c.step_snapshot(T0)
    c2, _ = make(tmp_path)
    assert len(c2.sched) == 1


def test_clock_jump_records_gap(tmp_path):
    c, _ = make(tmp_path)
    c.tick(T0)
    c.tick(T0 + 10 * 60_000)
    gaps = [json.loads(l) for l in (tmp_path / "gaps.jsonl").read_text().splitlines()]
    assert gaps == [{"start": T0, "end": T0 + 600_000, "reason": "pause"}]


class FakeConn:
    def __init__(self, msgs, fail=True):
        self.msgs, self.sent, self.fail = list(msgs), [], fail

    async def send(self, s):
        self.sent.append(json.loads(s))

    async def recv(self):
        if self.msgs:
            return self.msgs.pop(0)
        if self.fail:
            raise ConnectionError("weg")
        await asyncio.sleep(3600)


def test_ws_reconnects_and_records_gap(tmp_path):
    conns = [FakeConn([trade_msg("0x1", "0x2")]), FakeConn([trade_msg("0x3", "0x4")], fail=False)]

    class Ctx:
        def __init__(self, conn):
            self.conn = conn

        async def __aenter__(self):
            return self.conn

        async def __aexit__(self, *a):
            return False

    made = []

    def connect():
        made.append(1)
        return Ctx(conns[len(made) - 1])

    c, _ = make(tmp_path, ws=connect)

    async def main():
        stop = asyncio.Event()
        task = asyncio.create_task(c.ws_loop(stop, backoff_start=0.01))
        for _ in range(200):
            await asyncio.sleep(0.01)
            if len(c.sched) == 4:
                break
        stop.set()
        task.cancel()

    asyncio.run(main())
    assert len(made) == 2 and len(c.sched) == 4
    subs = [m["subscription"]["coin"] for m in conns[0].sent if m["method"] == "subscribe"]
    assert subs == ["BTC", "ETH"]
    gaps = [json.loads(l) for l in (tmp_path / "gaps.jsonl").read_text().splitlines()]
    assert gaps[0]["reason"] == "ws"
