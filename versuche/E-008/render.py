"""E-008: last 30 days as daily candles, days 31 to 177 before that as weekly candles.

Same 180-day horizon as the champion, condensed: 21 full weeks (days -176 to -30, the 3 oldest days that do not
fill a week are dropped) plus 30 daily rows instead of 180 daily rows. Weekly candles are built from the daily
bars in 7-day blocks counted back from the decision day: open of the first day, max high, min low, close of the
last day. Prices scaled so the last close is 100. Volume is the average daily volume of the row's days relative
to the average daily volume of the whole window, so weekly and daily v are on the same scale.
"""

import pandas as pd

DAILY = 30
WEEKS = 21


def render(df: pd.DataFrame, lookback: int) -> str:
    w = df.tail(DAILY + 7 * WEEKS).copy()
    w.index = pd.RangeIndex(-len(w) + 1, 1)
    scale = 100 / w["close"].iloc[-1]
    w[["open", "high", "low", "close"]] *= scale
    w["volume"] = w["volume"] / w["volume"].mean()
    old, recent = w.iloc[:-DAILY], w.iloc[-DAILY:]
    weekly = [old.iloc[i:i + 7] for i in range(0, len(old), 7)]
    fmt = "{} {:.1f} {:.1f} {:.1f} {:.1f} {:.2f}"
    lines = ["weekly: day o h l c v (day = last day of the week)"]
    lines += [fmt.format(b.index[-1], b["open"].iloc[0], b["high"].max(), b["low"].min(), b["close"].iloc[-1], b["volume"].mean()) for b in weekly]
    lines += ["daily: day o h l c v"]
    lines += [fmt.format(d, r.open, r.high, r.low, r.close, r.volume) for d, r in recent.iterrows()]
    return "\n".join(lines)
