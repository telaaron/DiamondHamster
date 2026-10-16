"""Loader for the Binance pull in /mnt/project-files/research/quant-edge/daten (holdout never downloaded)."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from qe_common import DEV_END, drop_holdout

DATA = Path("/mnt/project-files/research/quant-edge/daten")
COINS = ["BTC", "ETH", "SOL", "XRP", "BNB", "DOGE", "ADA", "LTC", "LINK", "AVAX", "TRX", "DOT"]


def candles(kind: str, coin: str, dev_only: bool = True) -> pd.DataFrame:
    df = pd.read_csv(DATA / f"{kind}_{coin}_1d.csv")
    df.index = pd.DatetimeIndex(pd.to_datetime(df.pop("open_time"), unit="ms", utc=True), name="date")
    df = drop_holdout(df.sort_index())
    return df[df.index <= DEV_END] if dev_only else df


def funding_daily(coin: str, dev_only: bool = True) -> pd.Series:
    """Sum of the funding payments within each UTC day (positive = longs pay shorts)."""
    f = pd.read_csv(DATA / f"funding_{coin}.csv")
    t = pd.to_datetime(f["fundingTime"], unit="ms", utc=True)
    s = pd.Series(f["fundingRate"].astype(float).values, index=t).sort_index()
    s = drop_holdout(s.to_frame("r"))["r"]
    d = s.groupby(s.index.floor("D")).sum()
    return d[d.index <= DEV_END] if dev_only else d
