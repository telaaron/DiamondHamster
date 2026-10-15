"""E-027: the champion's 180-day daily table plus one market line with US M2 money supply (backlog #16).

m2_frozen.csv (daten/) holds monthly ECONOMICS:USM2 from the TradingView connector (raw tool result in
daten/raw/, unchanged), dated by the month it covers. TradingView has no vintages: the history is the
revised one, not what was known at the time (bias noted on the card).
The series is market-wide: every window of a batch gets the identical line.
Point in time: a month counts as known only from its datestamp + 56 days (8 weeks, hinweise-forschung.md),
judged on the day BEFORE the decision day.

- yoy  = M(m) / M(m-12) - 1 for the latest known month m, in whole percent.
- g3   = annualised 3-month growth rate M(m) / M(m-3); its direction vs the month before (rising/falling)
         and for how many consecutive months it has moved that way (capped: "12 or more").
- Any value missing or too short a history: "US money supply not available" (never 0).
Never shows levels or dates.
"""

from pathlib import Path

import pandas as pd

from diamondhamster import ai

DATA = pd.read_csv(Path(__file__).parent / "daten" / "m2_frozen.csv", parse_dates=["month"])
M = DATA.set_index(DATA["month"].dt.tz_localize("UTC"))["value"].astype(float).sort_index()
LAG, CAP = pd.Timedelta(days=56), 12


def stats(cutoff: pd.Timestamp) -> tuple[int, str, int] | None:
    s = M[M.index + LAG <= cutoff]
    if s.empty:
        return None
    m = s.index[-1]
    want = pd.date_range(end=m, periods=len(s), freq="MS")
    if not (s.index == want).all():
        return None
    if len(s) < 13:
        return None
    yoy = 100 * (s.iloc[-1] / s.iloc[-13] - 1)
    g3 = (s / s.shift(3)) ** 4 - 1
    step = g3.diff().dropna()
    if step.empty or step.iloc[-1] == 0:
        return None
    up = step.iloc[-1] > 0
    n = 0
    for v in step.iloc[::-1]:
        if (v > 0) != up or v == 0:
            break
        n += 1
    full = n == len(step)
    if full and n < CAP:
        return None
    return int(round(yoy)), "rising" if up else "falling", min(n, CAP)


def line(df: pd.DataFrame) -> str:
    st = stats(df.index[-1] - pd.Timedelta(days=1))
    if st is None:
        return "US money supply not available"
    months = "12 or more months" if st[2] >= CAP else f"{st[2]} month" + ("s" if st[2] > 1 else "")
    return f"US money supply M2: year-on-year {st[0]:+d}%, 3-month growth rate {st[1]} for {months}"


def render(df: pd.DataFrame, lookback: int) -> str:
    return line(df) + "\n" + ai.compact(ai.window(df, df.index[-1], lookback))
