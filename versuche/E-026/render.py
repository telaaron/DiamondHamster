"""E-026: the champion's 180-day daily table plus a second table with the overall market (backlog #7).

The market is BTC (tournament/candles/BTC.csv, frozen TradingView Binance spot candles, the same file the
bench scores with; no new fetch). It is shown anonymously as daily closes over exactly the same days as the
coin window, cut off at the same decision day, scaled so its last close is 100. Never a ticker, date or level.
For BTC's own window the second table is identical to the first table's closes, which can reveal that window.
If any day of the window has no market close: "market not available".
"""

import pandas as pd

from diamondhamster import ai, tournament

BTC = tournament.read_candles("BTC", tournament.CANDLES)["close"]


def market(days: pd.DatetimeIndex) -> str:
    c = BTC.reindex(days)
    if c.isna().any() or len(c) == 0:
        return "market not available"
    c = c * (100 / c.iloc[-1])
    lines = [f"{d} {v:.1f}" for d, v in zip(range(-len(c) + 1, 1), c)]
    return "market: day c\n" + "\n".join(lines)


def render(df: pd.DataFrame, lookback: int) -> str:
    w = df.loc[: df.index[-1]].tail(lookback)
    return ai.compact(ai.window(df, df.index[-1], lookback)) + "\n" + market(w.index)
