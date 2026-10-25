"""Mechanical version of Stefan Kassing's "SK-System" (hypothesis H-004).

Terms from the source document: a "sequence" is three alternating swing points 0, A, B with a target
("Sequenzziel") at the 161.8 % trend-based Fibonacci extension B + 1.618 * (A - 0). The sequence dies
when price crosses the 0 point. A "Korrekturlevel" is the 50 % to 66.7 % retracement of the last
higher-timeframe swing; sequences only count when they start there ("Wendebereich").

Lookahead contract: a swing at bar i is known from bar i + k on, never earlier. Everything a sequence
uses is known at its `confirmed` bar; the trade enters at the next bar's open.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

TARGET_RATIO = 1.618
MIN_RETRACE = 0.382
KL_ZONE = (0.5, 0.667)


@dataclass(frozen=True)
class Pivot:
    i: int
    confirmed: int
    kind: str  # "H" or "L"
    price: float


@dataclass(frozen=True)
class Sequence:
    direction: int  # 1 bullish, -1 bearish
    i0: int
    ia: int
    ib: int
    confirmed: int
    p0: float
    pa: float
    pb: float
    ratio: float = TARGET_RATIO

    @property
    def target(self) -> float:
        return self.pb + self.direction * self.ratio * abs(self.pa - self.p0)

    @property
    def stop(self) -> float:
        return self.p0


@dataclass(frozen=True)
class Trade:
    seq: Sequence
    entry_i: int
    exit_i: int
    entry: float
    exit: float
    outcome: str  # "target", "stop", "open"
    r: float
    ret: float


def _raw_pivots(df: pd.DataFrame, k: int) -> list[Pivot]:
    h, lo = df["high"].to_numpy(), df["low"].to_numpy()
    out = []
    for i in range(k, len(df) - k):
        win = slice(i - k, i + k + 1)
        # first bar of a flat top/bottom wins, so equal neighbours do not create twin pivots
        if h[i] == h[win].max() and np.argmax(h[win]) == k:
            out.append(Pivot(i, i + k, "H", float(h[i])))
        if lo[i] == lo[win].min() and np.argmin(lo[win]) == k:
            out.append(Pivot(i, i + k, "L", float(lo[i])))
    return sorted(out, key=lambda p: (p.confirmed, p.i))


def _merge(zz: list[Pivot], p: Pivot) -> bool:
    """Append p to the zigzag in place. Returns True if the zigzag changed."""
    if zz and zz[-1].kind == p.kind:
        more_extreme = p.price > zz[-1].price if p.kind == "H" else p.price < zz[-1].price
        if not more_extreme:
            return False
        zz[-1] = p
        return True
    zz.append(p)
    return True


def pivots(df: pd.DataFrame, k: int) -> list[Pivot]:
    zz: list[Pivot] = []
    for p in _raw_pivots(df, k):
        _merge(zz, p)
    return zz


def sequences(df: pd.DataFrame, k: int, ratio: float = TARGET_RATIO, min_retrace: float = MIN_RETRACE) -> list[Sequence]:
    zz: list[Pivot] = []
    out = []
    for p in _raw_pivots(df, k):
        if not _merge(zz, p) or len(zz) < 3:
            continue
        z0, za, zb = zz[-3], zz[-2], zz[-1]
        d = 1 if zb.kind == "L" else -1
        leg = abs(za.price - z0.price)
        if leg == 0 or d * (zb.price - z0.price) <= 0:
            continue  # B beyond the 0 point: invalid
        if abs(za.price - zb.price) / leg < min_retrace:
            continue
        out.append(Sequence(d, z0.i, za.i, zb.i, p.confirmed, z0.price, za.price, zb.price, ratio))
    return out


def simulate(df: pd.DataFrame, s: Sequence, cost_per_side: float) -> Trade | None:
    o, h, lo, c = (df[x].to_numpy() for x in ("open", "high", "low", "close"))
    d, n = s.direction, len(df)
    if s.confirmed + 1 >= n:
        return None
    last_close = c[s.confirmed]
    if not (d * (last_close - s.stop) > 0 and d * (s.pa - last_close) > 0):
        return None  # already through A or the 0 point: entry missed
    ei = s.confirmed + 1
    entry = o[ei]
    if d * (entry - s.stop) <= 0 or d * (s.target - entry) <= 0:
        return None  # gapped through a level at the open
    exit_i, exit_p, outcome = n - 1, c[n - 1], "open"
    for j in range(ei, n):
        stop_hit = lo[j] <= s.stop if d == 1 else h[j] >= s.stop
        tgt_hit = h[j] >= s.target if d == 1 else lo[j] <= s.target
        if stop_hit:  # conservative: stop first if both in the same bar
            gap = d * (o[j] - s.stop) < 0 and j > ei
            exit_i, exit_p, outcome = j, (o[j] if gap else s.stop), "stop"
            break
        if tgt_hit:
            gap = d * (o[j] - s.target) > 0 and j > ei
            exit_i, exit_p, outcome = j, (o[j] if gap else s.target), "target"
            break
    ret = d * (exit_p / entry - 1) - cost_per_side * (1 + exit_p / entry)
    risk = abs(entry - s.stop) / entry
    return Trade(s, ei, exit_i, float(entry), float(exit_p), outcome, float(ret / risk), float(ret))


def weekly(df: pd.DataFrame) -> pd.DataFrame:
    w = df.resample("W-SUN").agg({"open": "first", "high": "max", "low": "min", "close": "last"})
    return w.dropna()


def kl_zones(df: pd.DataFrame, k: int = 3) -> list[tuple[pd.Timestamp, int, float, float]]:
    """Weekly Korrekturlevel zones as (known_from, direction, lo, hi), in order of becoming known.

    direction 1: bullish zone, 50-66.7 % pullback of the last weekly up-swing (low -> high).
    direction -1: bearish zone, 50-66.7 % bounce of the last weekly down-swing (high -> low).
    known_from is the close of the week that confirmed the swing's second point.
    """
    w = weekly(df)
    zz: list[Pivot] = []
    out = []
    for p in _raw_pivots(w, k):
        if not _merge(zz, p) or len(zz) < 2:
            continue
        a, b = zz[-2], zz[-1]
        known = w.index[p.confirmed]
        lo_p, hi_p = (a.price, b.price) if b.kind == "H" else (b.price, a.price)
        rng = hi_p - lo_p
        if b.kind == "H":  # up-swing finished -> bullish KL below
            out.append((known, 1, hi_p - KL_ZONE[1] * rng, hi_p - KL_ZONE[0] * rng))
        else:
            out.append((known, -1, lo_p + KL_ZONE[0] * rng, lo_p + KL_ZONE[1] * rng))
    return out


def in_kl(s: Sequence, zones, index: pd.DatetimeIndex) -> bool:
    now = index[s.confirmed]
    known = [z for z in zones if z[1] == s.direction and z[0] <= now]
    if not known:
        return False
    _, _, lo, hi = known[-1]
    return lo <= s.p0 <= hi


def blash(s: Sequence, df: pd.DataFrame) -> bool:
    """Close at confirmation in the lower (bullish) or upper (bearish) half of the 52-week range."""
    j = s.confirmed
    win = df.iloc[max(0, j - 364): j + 1]
    mid = (win["high"].max() + win["low"].min()) / 2
    c = df["close"].iloc[j]
    return c < mid if s.direction == 1 else c > mid
