"""Bekanntes Positionsbuch: letzter Stand je Adresse, Schnappschuss und Abdeckung (Spec 3.4)."""
from __future__ import annotations

import pandas as pd

ROW_COLUMNS = ["user", "side", "mode", "leverage", "entry_px", "liq_px", "qty", "polled_at"]
MAX_AGE_MS = 3_600_000


class KnownBook:
    def __init__(self):
        self._pos: dict[str, tuple[int, list[dict]]] = {}

    def update(self, user: str, positions: list[dict], polled_at: int) -> None:
        if positions:
            self._pos[user] = (polled_at, positions)
        else:
            self._pos.pop(user, None)

    def notional(self, user: str) -> float:
        return float(sum(p["notional"] for p in self._pos.get(user, (0, []))[1]))

    def _fresh(self, coin: str, now: int, max_age_ms: int):
        for user, (t, ps) in self._pos.items():
            if now - t > max_age_ms:
                continue
            for p in ps:
                if p["coin"] == coin:
                    yield user, t, p

    def rows(self, coin: str, now: int, max_age_ms: int = MAX_AGE_MS) -> pd.DataFrame:
        recs = [{"user": u, "side": p["side"], "mode": p["mode"], "leverage": p["leverage"],
                 "entry_px": p["entry_px"], "liq_px": p["liq_px"], "qty": p["qty"], "polled_at": t}
                for u, t, p in self._fresh(coin, now, max_age_ms)]
        return pd.DataFrame(recs, columns=ROW_COLUMNS)

    def coverage(self, coin: str, oi: float, now: int, max_age_ms: int = MAX_AGE_MS) -> dict:
        if oi <= 0:
            return {"long": 0.0, "short": 0.0, "no_liq_share": 0.0}
        qty = {"long": 0.0, "short": 0.0}
        no_liq = 0.0
        for _, _, p in self._fresh(coin, now, max_age_ms):
            qty[p["side"]] += p["qty"]
            if p["liq_px"] is None:
                no_liq += p["qty"]
        total = qty["long"] + qty["short"]
        return {"long": qty["long"] / oi, "short": qty["short"] / oi,
                "no_liq_share": no_liq / total if total else 0.0}

    def to_state(self) -> dict:
        return {u: [t, ps] for u, (t, ps) in self._pos.items()}

    @classmethod
    def from_state(cls, d: dict) -> "KnownBook":
        b = cls()
        b._pos = {u: (int(t), ps) for u, (t, ps) in d.items()}
        return b

    def __len__(self) -> int:
        return len(self._pos)
