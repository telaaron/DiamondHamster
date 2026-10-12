"""E-005: daily rows as returns and range instead of prices.

Same days and volume as the candle window, but no price level: per day the close-to-close change and the
high-low range, both in % of the previous close. One extra candle (day -lookback) is read only to get the
first day's previous close.
"""

import pandas as pd


def render(df: pd.DataFrame, lookback: int) -> str:
    w = df.tail(lookback + 1)
    prev = w["close"].shift(1)
    ret = 100 * (w["close"] / prev - 1)
    rng = 100 * (w["high"] - w["low"]) / prev
    vol = w["volume"] / w["volume"].iloc[1:].mean()
    rows = pd.DataFrame({"ret": ret, "range": rng, "v": vol}).iloc[1:]
    rows.index = pd.RangeIndex(-len(rows) + 1, 1)
    lines = [f"{d} {r.ret:+.1f} {r.range:.1f} {r.v:.2f}" for d, r in rows.iterrows()]
    return "day ret range v\n" + "\n".join(lines)
