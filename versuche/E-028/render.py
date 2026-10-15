"""E-028: the champion's 180-day daily table plus one market line with the US dollar index (backlog #39).

dxy_frozen.csv (daten/) holds the daily close of TVC:DXY from the TradingView connector (raw tool result in
daten/raw/, unchanged). Bars are stamped at the session open of the evening before (21:00 to 00:00 UTC); the
CSV carries the trading day (stamp + 3 hours). Weekdays only. The series is market-wide: every window of a
batch gets the identical line. Cut-off: only closes up to and including the day BEFORE the decision day.

- v   = last close on or before the cut-off.
- c4  = v / (last close on or before cut-off - 28 days) - 1, in percent rounded to 0.5.
- c13 = v / (last close on or before cut-off - 91 days) - 1, in percent rounded to 0.5.
- pct = percentile of v among all closes of the 180 calendar days ending at the cut-off (0 to 100).
- Missing data (no close within 5 days of a reference day, or history shorter than the window):
  "dollar index not available" (never 0).
Never shows index levels.
"""

from pathlib import Path

import pandas as pd

from diamondhamster import ai

DATA = pd.read_csv(Path(__file__).parent / "daten" / "dxy_frozen.csv", parse_dates=["date"])
S = DATA.set_index(DATA["date"].dt.tz_localize("UTC"))["close"].astype(float).sort_index()
WINDOW, W4, W13, MAXGAP = 180, 28, 91, 5


def last_close(day: pd.Timestamp) -> float | None:
    s = S[S.index <= day]
    if s.empty or (day - s.index[-1]).days > MAXGAP:
        return None
    return float(s.iloc[-1])


def half(x: float) -> str:
    r = round(2 * x) / 2
    return "0.0%" if r == 0 else f"{r:+.1f}%"


def stats(cutoff: pd.Timestamp) -> tuple[str, str, int] | None:
    start = cutoff - pd.Timedelta(days=WINDOW - 1)
    if S.empty or S.index[0] > start:
        return None
    v, b4, b13 = last_close(cutoff), last_close(cutoff - pd.Timedelta(days=W4)), last_close(cutoff - pd.Timedelta(days=W13))
    if None in (v, b4, b13):
        return None
    win = S[(S.index >= start) & (S.index <= cutoff)]
    pct = int(round(100 * (win <= v).mean()))
    return half(100 * (v / b4 - 1)), half(100 * (v / b13 - 1)), pct


def line(df: pd.DataFrame) -> str:
    st = stats(df.index[-1].normalize() - pd.Timedelta(days=1))
    if st is None:
        return "dollar index not available"
    return f"dollar index 4w {st[0]}, 13w {st[1]}, pct {st[2]}"


def render(df: pd.DataFrame, lookback: int) -> str:
    return line(df) + "\n" + ai.compact(ai.window(df, df.index[-1], lookback))
