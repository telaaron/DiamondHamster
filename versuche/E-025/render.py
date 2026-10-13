"""E-025: the champion's 180-day daily table plus one market line with stablecoin growth (backlog #38).

stable_frozen.csv (daten/) holds the daily close of CRYPTOCAP:USDT and CRYPTOCAP:USDC from the TradingView
connector (raw tool results in daten/raw/, unchanged; market capitalisation, about the circulating supply)
and their sum. The series is market-wide: every window of a batch gets the identical line.
Cut-off: only values up to and including the day BEFORE the decision day are used (as E-024).

- g4  = S(day -1) / S(day -29) - 1, in percent with one decimal (4-week growth of USDT plus USDC).
- g13 = S(day -1) / S(day -92) - 1, in percent with one decimal (13-week growth).
- p4, p13 = percentile of today's g4 / g13 among its own 180 daily values ending at day -1 (0 to 100).
- Any value missing or too short a history: "stablecoins not available" (never 0).
Never shows dollar levels.
"""

from pathlib import Path

import pandas as pd

from diamondhamster import ai

DATA = pd.read_csv(Path(__file__).parent / "daten" / "stable_frozen.csv", parse_dates=["date"])
S = DATA.set_index(DATA["date"].dt.tz_localize("UTC"))["total"].astype(float).sort_index()
WINDOW, W4, W13 = 180, 28, 91


def growth(s: pd.Series, lag: int) -> pd.Series:
    prev = s.reindex(s.index - pd.Timedelta(days=lag))
    return pd.Series(100 * (s.values / prev.values - 1), index=s.index)


def stats(cutoff: pd.Timestamp) -> tuple[float, int, float, int] | None:
    s = S[S.index <= cutoff]
    if s.empty or s.index[-1] != cutoff:
        return None
    out = []
    for lag in (W4, W13):
        g = growth(s, lag).tail(WINDOW)
        if len(g) < WINDOW or g.isna().any() or (g.index[-1] - g.index[0]).days != WINDOW - 1:
            return None
        out += [round(float(g.iloc[-1]), 1), int(round(100 * (g <= g.iloc[-1]).mean()))]
    return tuple(out)


def line(df: pd.DataFrame) -> str:
    st = stats(df.index[-1] - pd.Timedelta(days=1))
    if st is None:
        return "stablecoins not available"
    return f"stablecoins 4w {st[0]:+.1f}% pct {st[1]}, 13w {st[2]:+.1f}% pct {st[3]}"


def render(df: pd.DataFrame, lookback: int) -> str:
    return line(df) + "\n" + ai.compact(ai.window(df, df.index[-1], lookback))
