"""E-014: the champion's 180-day daily table plus one line with a fixed rule and its signal today.

Rule: invested (1) when the decision-day close is above the simple average of the last 50 daily closes
(decision day included), otherwise 0. The average is computed from the full candle history up to the decision
day, so it exists from the first window day on; it is shown on the window's 100 scale.
"""

import pandas as pd

from diamondhamster import ai

SMA = 50


def signal(df: pd.DataFrame) -> tuple[float, int]:
    sma = df["close"].tail(SMA).mean()
    return sma, int(df["close"].iloc[-1] > sma)


def render(df: pd.DataFrame, lookback: int) -> str:
    sma, sig = signal(df)
    sma100 = sma * 100 / df["close"].iloc[-1]
    state = "1 (invested)" if sig else "0 (flat)"
    rule = f"rule: close {100:.1f} vs 50-day average {sma100:.1f} -> signal {state}"
    return rule + "\n" + ai.compact(ai.window(df, df.index[-1], lookback))
