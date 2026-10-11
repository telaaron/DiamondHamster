"""Indicator snapshot for a decision day, as text for a trader prompt (T-002 onward).

Only scale-free values, so the snapshot does not reveal price level, asset or date. Calendar columns
(moon age, weekday, month) are left out because together they can pin down the date.
"""

from __future__ import annotations

import pandas as pd

from . import ai, features

# name in the prompt -> (column, multiplier, decimals)
FIELDS = {
    "ret_7d_%": ("ret_7d", 100, 1),
    "ret_30d_%": ("ret_30d", 100, 1),
    "dist_ema20_%": ("ema20_dist", 100, 1),
    "dist_ema50_%": ("ema50_dist", 100, 1),
    "dist_ema200_%": ("ema200_dist", 100, 1),
    "rsi14": ("rsi14", 1, 1),
    "stoch_rsi": ("stoch_rsi", 1, 2),
    "macd_hist_%": ("macd_hist", 100, 2),
    "bollinger_pos": ("bb_pos", 1, 2),
    "bollinger_width_%": ("bb_width", 100, 1),
    "atr14_%": ("atr_pct", 100, 2),
    "adx14": ("adx14", 1, 1),
    "dist_vwap30_%": ("vwap30_dist", 100, 1),
    "pos_in_180d_range": ("fib_pos180", 1, 2),
    "dist_gauss144_%": ("gauss_dist", 100, 1),
    "gauss144_slope5d_%": ("gauss_slope", 100, 2),
    "rsi_divergence": ("div_rsi", 1, 0),
    "dist_90d_high_%": ("sr_dist_hi90", 100, 1),
    "dist_90d_low_%": ("sr_dist_lo90", 100, 1),
}


def snapshot(feats: pd.DataFrame, t: pd.Timestamp) -> str:
    row = feats.loc[t]
    parts = []
    for name, (col, mult, dec) in FIELDS.items():
        v = row[col]
        parts.append(f"{name}={'na' if pd.isna(v) else f'{v * mult:.{dec}f}'}")
    return "indicators " + " ".join(parts)


def renderer(df: pd.DataFrame, lookback: int = 180):
    """render(df, t) for ai.export_requests: indicator line, then the candle window."""
    feats = features.compute(df)
    return lambda d, t: snapshot(feats, t) + "\n" + ai.compact(ai.window(d, t, lookback))
