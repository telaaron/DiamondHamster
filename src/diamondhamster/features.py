"""Group A features: everything computable from daily OHLCV, plus lunar phase.

Every column at row t uses only rows up to and including t (tests/test_features.py checks this by
recomputing on truncated data). Chart patterns and Elliott waves are left to the model's reading of
the price window; they have no single mechanical definition.

Before features go to a model: exact moon_age together with dow and month can pin down the calendar
date, which undoes anonymization. Pass the moon phase coarsely (e.g. 8 buckets) or drop the calendar columns.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

SYNODIC_MONTH = 29.530588853
NEW_MOON_REF = pd.Timestamp("2000-01-06 18:14", tz="UTC")


def ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False).mean()


def rma(s: pd.Series, n: int) -> pd.Series:
    """Wilder smoothing, as used by RSI/ATR/ADX."""
    return s.ewm(alpha=1 / n, adjust=False).mean()


def rsi(close: pd.Series, n: int = 14) -> pd.Series:
    d = close.diff()
    up, down = rma(d.clip(lower=0), n), rma(-d.clip(upper=0), n)
    return 100 * up / (up + down).replace(0, np.nan)


def atr(df: pd.DataFrame, n: int = 14) -> pd.Series:
    prev = df["close"].shift(1)
    tr = pd.concat([df["high"] - df["low"], (df["high"] - prev).abs(), (df["low"] - prev).abs()], axis=1).max(axis=1)
    return rma(tr, n)


def adx(df: pd.DataFrame, n: int = 14) -> pd.Series:
    up, down = df["high"].diff(), -df["low"].diff()
    plus = pd.Series(np.where((up > down) & (up > 0), up, 0.0), index=df.index)
    minus = pd.Series(np.where((down > up) & (down > 0), down, 0.0), index=df.index)
    a = atr(df, n)
    pdi, mdi = 100 * rma(plus, n) / a, 100 * rma(minus, n) / a
    return rma(100 * (pdi - mdi).abs() / (pdi + mdi).replace(0, np.nan), n)


def rci(close: pd.Series, n: int) -> pd.Series:
    """Rank Correlation Index: Spearman correlation of price ranks vs time over n bars, scaled to ±100."""
    t = np.arange(n)

    def f(w):
        r = pd.Series(w).rank().values
        return (1 - 6 * ((t + 1 - r) ** 2).sum() / (n * (n**2 - 1))) * 100

    return close.rolling(n).apply(f, raw=True)


def gaussian_filter(s: pd.Series, period: int = 144, poles: int = 4) -> pd.Series:
    """Ehlers' recursive Gaussian filter (basis of the 'Gaussian Channel'); causal by construction."""
    beta = (1 - np.cos(2 * np.pi / period)) / (2 ** (1 / poles) - 1)
    alpha = -beta + np.sqrt(beta**2 + 2 * beta)
    x = s.to_numpy(float)
    out = x.copy()
    for _ in range(poles):
        y = np.empty_like(out)
        y[0] = out[0]
        for i in range(1, len(out)):
            y[i] = alpha * out[i] + (1 - alpha) * y[i - 1]
        out = y
    return pd.Series(out, index=s.index)


def moon_age(index: pd.DatetimeIndex) -> pd.Series:
    """Days since new moon (0..29.5), from the mean synodic month; accurate to well under a day."""
    days = (index - NEW_MOON_REF).total_seconds() / 86400
    return pd.Series(np.mod(days, SYNODIC_MONTH), index=index)


def divergence(price: pd.Series, osc: pd.Series, n: int = 30) -> pd.Series:
    """+1 bullish (price at n-day low, oscillator above its low), -1 bearish (mirror), else 0."""
    bull = (price <= price.rolling(n).min()) & (osc > osc.rolling(n).min())
    bear = (price >= price.rolling(n).max()) & (osc < osc.rolling(n).max())
    return bull.astype(int) - bear.astype(int)


def candles(df: pd.DataFrame) -> pd.DataFrame:
    o, h, l, c = df["open"], df["high"], df["low"], df["close"]
    body, rng = (c - o).abs(), (h - l).replace(0, np.nan)
    po, pc = o.shift(1), c.shift(1)
    return pd.DataFrame({
        "doji": (body / rng < 0.1).astype(int),
        "hammer": ((np.minimum(o, c) - l) > 2 * body).astype(int) & ((h - np.maximum(o, c)) < body).astype(int),
        "engulf": np.where((c > o) & (pc < po) & (c >= po) & (o <= pc), 1, np.where((c < o) & (pc > po) & (o >= pc) & (c <= po), -1, 0)),
    }, index=df.index)


def compute(df: pd.DataFrame) -> pd.DataFrame:
    c, v = df["close"], df["volume"]
    f = pd.DataFrame(index=df.index)
    f["ret_1d"] = c.pct_change()
    f["ret_7d"] = c.pct_change(7)
    f["ret_30d"] = c.pct_change(30)
    for n in (20, 50, 200):
        f[f"ema{n}_dist"] = c / ema(c, n) - 1
    f["rsi14"] = rsi(c)
    macd = ema(c, 12) - ema(c, 26)
    f["macd"] = macd / c
    f["macd_hist"] = (macd - ema(macd, 9)) / c
    r = f["rsi14"]
    f["stoch_rsi"] = (r - r.rolling(14).min()) / (r.rolling(14).max() - r.rolling(14).min()).replace(0, np.nan)
    mid, sd = c.rolling(20).mean(), c.rolling(20).std()
    f["bb_pos"] = (c - mid) / (2 * sd)
    f["bb_width"] = 4 * sd / mid
    a = atr(df)
    f["atr_pct"] = a / c
    f["kc_pos"] = (c - ema(c, 20)) / (2 * a)
    f["adx14"] = adx(df)
    vwap30 = (c * v).rolling(30).sum() / v.rolling(30).sum()
    f["vwap30_dist"] = c / vwap30 - 1
    f["vol_z30"] = (v - v.rolling(30).mean()) / v.rolling(30).std()
    # Last completed week (Mon..Sun); on a Sunday that week ends with today's close.
    wk = df.resample("W-SUN").agg({"high": "max", "low": "min", "close": "last"})
    pivot = ((wk["high"] + wk["low"] + wk["close"]) / 3).reindex(df.index, method="ffill")
    f["pivot_w_dist"] = c / pivot - 1
    hi, lo = df["high"].rolling(180).max(), df["low"].rolling(180).min()
    f["fib_pos180"] = (c - lo) / (hi - lo)  # 0.382 / 0.5 / 0.618 retracements read off this
    g = gaussian_filter(c)
    f["gauss_dist"] = c / g - 1
    f["gauss_slope"] = g.pct_change(5)
    f["rci9"] = rci(c, 9)
    f["rci26"] = rci(c, 26)
    f["div_rsi"] = divergence(c, r)
    f["sr_dist_hi90"] = c / df["high"].rolling(90).max() - 1
    f["sr_dist_lo90"] = c / df["low"].rolling(90).min() - 1
    f = f.join(candles(df))
    f["moon_age"] = moon_age(df.index)
    f["dow"] = df.index.dayofweek
    f["month"] = df.index.month
    return f
