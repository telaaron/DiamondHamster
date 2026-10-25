"""E-019: the champion's 180-day daily table plus one line with the quantities the knowledge block relies on.

All values come from candles up to and including the decision day (df ends there, README §3 rule 5).
Definitions follow research/wissen/bausteine (zeitreihen-momentum, regime, positionsgroesse,
gleitende-durchschnitte):
- z_2W, z_4W, z_8W: r_N / (sigma_day * sqrt(N)), r_N = close / close N days ago - 1 (N = 14, 28, 56),
  sigma_day = std of daily log returns over the last 60 days.
- ER(30) = |C_t - C_t-30| / sum |C_i - C_i-1| over 30 days.
- sigma20/sigma90: std of daily log returns over 20 vs 90 days.
- SMA100: close vs the 100-day simple average in %, and the average's change over 20 days in %
  (rising if > 0, else falling).
- crossings: sign changes of close - SMA100 over the last 90 days.
"""

import numpy as np
import pandas as pd

from diamondhamster import ai


def stats(df: pd.DataFrame) -> dict:
    c = df["close"].astype(float)
    lr = np.log(c).diff()
    sd = lr.tail(60).std()
    z = {n: (c.iloc[-1] / c.iloc[-1 - n] - 1) / (sd * np.sqrt(n)) for n in (14, 28, 56)}
    er = abs(c.iloc[-1] - c.iloc[-31]) / c.diff().abs().tail(30).sum()
    vr = lr.tail(20).std() / lr.tail(90).std()
    sma = c.rolling(100).mean()
    dist = (c.iloc[-1] / sma.iloc[-1] - 1) * 100
    slope = (sma.iloc[-1] / sma.iloc[-21] - 1) * 100
    side = np.sign(c - sma).tail(90)
    side = side[side != 0]
    cross = int((side != side.shift()).iloc[1:].sum())
    return {"z": z, "er": er, "vr": vr, "dist": dist, "slope": slope, "cross": cross}


def line(df: pd.DataFrame) -> str:
    s = stats(df)
    z = s["z"]
    trend = "rising" if s["slope"] > 0 else "falling"
    pos = "above" if s["dist"] > 0 else "below"
    return (f"stats: z_2W {z[14]:+.1f}, z_4W {z[28]:+.1f}, z_8W {z[56]:+.1f} | ER(30) {s['er']:.2f}"
            f" | sigma20/sigma90 {s['vr']:.2f} | close {abs(s['dist']):.1f}% {pos} SMA100,"
            f" SMA100 {trend} ({s['slope']:+.1f}% in 20 days) | close/SMA100 crossings in 90 days: {s['cross']}")


def render(df: pd.DataFrame, lookback: int) -> str:
    return line(df) + "\n" + ai.compact(ai.window(df, df.index[-1], lookback))
