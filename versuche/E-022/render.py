"""E-022: the champion's 180-day daily table plus one line with a fixed rule and its signal today.

Rule: invested (1) when the decision-day close is above the 20-week average, otherwise 0. The 20-week average is
the mean of the last 20 weekly closes, taken every 7th daily close counting back from the decision day (decision
days are Sundays, so these are the weekly closes; the decision day is included). It is computed from the full
candle history up to the decision day and shown on the window's 100 scale. Only change against E-014: the
signal's average (50 daily closes -> 20 weekly closes).
"""

import pandas as pd

from diamondhamster import ai

WEEKS = 20


def signal(df: pd.DataFrame) -> tuple[float, int]:
    weekly = df["close"].iloc[::-7].head(WEEKS)
    sma = weekly.mean()
    return sma, int(df["close"].iloc[-1] > sma)


def render(df: pd.DataFrame, lookback: int) -> str:
    sma, sig = signal(df)
    sma100 = sma * 100 / df["close"].iloc[-1]
    state = "1 (invested)" if sig else "0 (flat)"
    rule = f"rule: close {100:.1f} vs 20-week average {sma100:.1f} -> signal {state}"
    return rule + "\n" + ai.compact(ai.window(df, df.index[-1], lookback))
