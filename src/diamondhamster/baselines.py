"""The bar every method has to clear: buy & hold, DCA, and random timing at equal exposure."""

from __future__ import annotations

import numpy as np
import pandas as pd

from . import backtest, metrics
from .config import COST_PER_SIDE


def buy_and_hold(df: pd.DataFrame) -> pd.DataFrame:
    return backtest.run(df, pd.Series(1.0, index=df.index))


def dca(df: pd.DataFrame, amount: float = 100.0, cost_per_side: float = COST_PER_SIDE) -> dict:
    """Buy `amount` at the open of the first day of each month. Reports money-weighted return (IRR)."""
    first = df.groupby([df.index.year, df.index.month]).head(1)
    units = (amount * (1 - cost_per_side) / first["open"]).cumsum().reindex(df.index).ffill().fillna(0.0)
    invested = pd.Series(amount, index=first.index).cumsum().reindex(df.index).ffill().fillna(0.0)
    value = units * df["close"]
    held = value[invested > 0]
    dd = float((held / invested[invested > 0] / (held / invested[invested > 0]).cummax() - 1).min())
    flows = [(d, -amount) for d in first.index] + [(df.index[-1], float(value.iloc[-1]))]
    return {
        "invested": float(invested.iloc[-1]),
        "final_value": float(value.iloc[-1]),
        "multiple": float(value.iloc[-1] / invested.iloc[-1]),
        "irr": _irr(flows),
        "max_drawdown_vs_invested": dd,
    }


def _irr(flows: list[tuple[pd.Timestamp, float]]) -> float:
    t0 = flows[0][0]
    yrs = np.array([(d - t0).days / 365 for d, _ in flows])
    cf = np.array([c for _, c in flows])
    npv = lambda r: float((cf / (1 + r) ** yrs).sum())
    lo, hi = -0.99, 10.0
    if npv(lo) * npv(hi) > 0:
        return float("nan")
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if npv(lo) * npv(mid) > 0 else (lo, mid)
    return (lo + hi) / 2


def random_weights(index: pd.DatetimeIndex, exposure: float, mean_hold_days: float, rng: np.random.Generator) -> pd.Series:
    """Random long/flat path with a target exposure and mean holding period (geometric durations)."""
    mean_flat = mean_hold_days * (1 - exposure) / exposure
    out = np.zeros(len(index))
    i, on = 0, rng.random() < exposure
    while i < len(index):
        n = int(rng.geometric(1 / (mean_hold_days if on else mean_flat)))
        out[i : i + n] = 1.0 if on else 0.0
        i, on = i + n, not on
    return pd.Series(out, index=index)


def random_timing(df: pd.DataFrame, exposure: float = 0.5, mean_hold_days: float = 30, n: int = 1000, seed: int = 0) -> pd.DataFrame:
    """Distribution of metrics for random strategies. Compare a method against the same exposure and holding period."""
    rng = np.random.default_rng(seed)
    rows = [metrics.summary(backtest.run(df, random_weights(df.index, exposure, mean_hold_days, rng))) for _ in range(n)]
    return pd.DataFrame(rows)
