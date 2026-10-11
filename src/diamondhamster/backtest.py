"""Minimal long/flat backtest core.

Timing contract (the only place lookahead can hide, so it is fixed here):
- `weights[t]` may use information up to and including the close of day t.
- The position is changed at the open of day t+1, paying `cost_per_side` on the traded fraction.
- Returns are open-to-open, so day t+1's position earns open[t+1] -> open[t+2].
"""

from __future__ import annotations

import pandas as pd

from .config import COST_PER_SIDE


def run(df: pd.DataFrame, weights: pd.Series, cost_per_side: float = COST_PER_SIDE) -> pd.DataFrame:
    w = weights.reindex(df.index).fillna(0.0).clip(0.0, 1.0)
    held = w.shift(1).fillna(0.0)  # position during [open_t, open_t+1)
    ret = df["open"].shift(-1) / df["open"] - 1
    turnover = held.diff().abs().fillna(held.abs())
    strat = held * ret - turnover * cost_per_side
    out = pd.DataFrame({"position": held, "asset_ret": ret, "turnover": turnover, "ret": strat}).dropna()
    out["equity"] = (1 + out["ret"]).cumprod()
    return out
