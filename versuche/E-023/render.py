"""E-023: the champion's 180-day daily table plus one line with the perp basis (backlog #36).

basis_frozen.csv (daten/) holds daily closes of BINANCE:<COIN>USDT.P from the TradingView connector
(raw tool results in daten/raw/, unchanged) next to the spot closes from tournament/candles.
Only rows up to and including the decision day are used (README §3 rule 5).

- B = close_perp / close_spot - 1, per day.
- B7 = mean of B over the last 7 days.
- Shown: percentile of today's B7 among the B7 values of the last 180 days (0 to 100), the
  scale-free form backlog #36 asks for. Fewer than 180 values or no series: "not available".

render(df, lookback) does not receive the coin. The coin is found by matching the spot closes of the
last 30 days in df against basis_frozen.csv; this needs exactly one match, else it raises.
"""

from pathlib import Path

import pandas as pd

from diamondhamster import ai

DATA = pd.read_csv(Path(__file__).parent / "daten" / "basis_frozen.csv", parse_dates=["date"])
DATA["date"] = DATA["date"].dt.tz_localize("UTC")
WINDOW, AVG = 180, 7


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


def percentile(df: pd.DataFrame) -> int | None:
    c = coin_of(df)
    if c is None:
        return None
    g = DATA[(DATA.coin == c) & (DATA.date <= df.index[-1])].set_index("date").sort_index()
    if g.empty or g.index[-1] != df.index[-1]:
        return None
    b7 = (g.close_perp / g.close_spot - 1).rolling(AVG).mean().dropna().tail(WINDOW)
    if len(b7) < WINDOW:
        return None
    return int(round(100 * (b7 <= b7.iloc[-1]).mean()))


def line(df: pd.DataFrame) -> str:
    p = percentile(df)
    return "basis pct not available" if p is None else f"basis pct {p}"


def render(df: pd.DataFrame, lookback: int) -> str:
    return line(df) + "\n" + ai.compact(ai.window(df, df.index[-1], lookback))
