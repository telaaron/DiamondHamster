"""Data quality report: run before trusting any file."""

import pandas as pd


def report(df: pd.DataFrame, jump_threshold: float = 0.35) -> dict:
    full = pd.date_range(df.index[0], df.index[-1], freq="D", tz="UTC")
    missing = full.difference(df.index)
    ret = df["close"].pct_change().abs()
    bad_ohlc = (df["high"] < df[["open", "close"]].max(axis=1)) | (df["low"] > df[["open", "close"]].min(axis=1))
    return {
        "rows": len(df),
        "first": str(df.index[0].date()),
        "last": str(df.index[-1].date()),
        "missing_days": [str(d.date()) for d in missing],
        "duplicates": int(df.index.duplicated().sum()),
        "non_positive_prices": int((df[["open", "high", "low", "close"]] <= 0).any(axis=1).sum()),
        "inconsistent_ohlc": int(bad_ohlc.sum()),
        "zero_volume_days": int((df["volume"] == 0).sum()),
        "daily_moves_over_threshold": {str(d.date()): round(float(v), 4) for d, v in ret[ret > jump_threshold].items()},
    }


def compare_sources(a: pd.DataFrame, b: pd.DataFrame, tolerance: float = 0.02) -> pd.Series:
    """Days where two sources' closes differ by more than `tolerance` (relative)."""
    j = a[["close"]].join(b[["close"]], how="inner", lsuffix="_a", rsuffix="_b")
    diff = (j["close_a"] / j["close_b"] - 1).abs()
    return diff[diff > tolerance]
