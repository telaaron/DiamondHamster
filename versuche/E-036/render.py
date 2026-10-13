"""E-036: the champion's 180-day daily table plus one volatility line per window (backlog #13).

Computed only from the window's own candles up to and including the decision day (no external data):
- daily log returns of the close, ln(c_t / c_{t-1});
- vol_N = standard deviation (ddof 1) of the last N returns, annualized with sqrt(365) (crypto trades 7 days),
  in percent, rounded to whole percent; N = 7, 30, 90.
- Missing history (fewer than N + 1 closes): "volatility not available".
Scale-free, so it reveals no price level, date or coin.
"""

import numpy as np
import pandas as pd

from diamondhamster import ai

PERIODS = (7, 30, 90)


def line(df: pd.DataFrame) -> str:
    c = df["close"].astype(float)
    if len(c) < max(PERIODS) + 1:
        return "volatility not available"
    r = np.log(c / c.shift(1)).dropna()
    parts = [f"{n}d {round(100 * r.tail(n).std(ddof=1) * np.sqrt(365))}%" for n in PERIODS]
    return "volatility (annualized) " + ", ".join(parts)


def render(df: pd.DataFrame, lookback: int) -> str:
    return line(df) + "\n" + ai.compact(ai.window(df, df.index[-1], lookback))
