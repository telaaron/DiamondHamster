"""E-024: the champion's 180-day daily table plus one line with open interest (backlog #37).

oi_frozen.csv (daten/) holds the daily close of BINANCE:<COIN>USDT.P_OI from the TradingView connector
(raw tool results in daten/raw/, unchanged; values are open contracts in coins, not USD) next to the
spot closes from tournament/candles.
Cut-off: only OI values up to and including the day BEFORE the decision day are used
(research/wissen/bausteine/open-interest.md par. 7; stricter than README par. 3 rule 5).

- chg = OI(day -1) / OI(day -29) - 1, in percent, rounded to whole percent (4-week change).
- pct = percentile of OI(day -1) among the 180 daily OI values ending at day -1 (0 to 100).
- Fewer than 180 values, a missing day or no series: "oi not available" (never 0).

render(df, lookback) does not receive the coin. The coin is found by matching the spot closes of the
last 30 days in df against oi_frozen.csv (same method as E-023); exactly one match, else it raises.
"""

from pathlib import Path

import pandas as pd

from diamondhamster import ai

DATA = pd.read_csv(Path(__file__).parent / "daten" / "oi_frozen.csv", parse_dates=["date"])
DATA["date"] = DATA["date"].dt.tz_localize("UTC")
WINDOW, WEEKS4 = 180, 28


def coin_of(df: pd.DataFrame) -> str | None:
    tail = df["close"].astype(float).tail(30)
    hits = []
    for c, g in DATA.groupby("coin"):
        s = g.set_index("date")["close_spot"].reindex(tail.index)
        if s.notna().all() and ((s - tail).abs() <= 1e-9 * tail.abs()).all():
            hits.append(c)
    if len(hits) > 1:
        raise ValueError(f"window matches several coins: {hits}")
    return hits[0] if hits else None


def oi_stats(df: pd.DataFrame) -> tuple[int, int] | None:
    c = coin_of(df)
    if c is None:
        return None
    cutoff = df.index[-1] - pd.Timedelta(days=1)
    oi = DATA[(DATA.coin == c) & (DATA.date <= cutoff)].set_index("date")["oi"].sort_index().dropna()
    if oi.empty or oi.index[-1] != cutoff:
        return None
    win = oi.tail(WINDOW)
    if len(win) < WINDOW or (win.index[-1] - win.index[0]).days != WINDOW - 1:
        return None
    base = oi.get(cutoff - pd.Timedelta(days=WEEKS4))
    if base is None or base <= 0:
        return None
    chg = int(round(100 * (oi.iloc[-1] / base - 1)))
    pct = int(round(100 * (win <= win.iloc[-1]).mean()))
    return chg, pct


def line(df: pd.DataFrame) -> str:
    s = oi_stats(df)
    return "oi not available" if s is None else f"oi 4w {s[0]:+d}%, oi pct {s[1]}"


def render(df: pd.DataFrame, lookback: int) -> str:
    return line(df) + "\n" + ai.compact(ai.window(df, df.index[-1], lookback))
