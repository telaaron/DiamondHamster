"""Download, version and load daily OHLCV candles.

Raw files are written once to data/raw/ and recorded with their sha256 in data/manifest.json.
`load` cuts off the holdout unless explicitly unlocked; every unlock is appended to
data/holdout_access.log so a burned holdout stays visible in git history.
"""

from __future__ import annotations

import hashlib
import io
import json
import time
import urllib.request
import zipfile
from datetime import date, datetime, timezone
from pathlib import Path

import pandas as pd

from .config import HOLDOUT_START

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "data" / "raw"
MANIFEST = ROOT / "data" / "manifest.json"
HOLDOUT_LOG = ROOT / "data" / "holdout_access.log"

COLUMNS = ["open", "high", "low", "close", "volume"]
BINANCE_VISION = "https://data.binance.vision/data/spot"
COINBASE = "https://api.exchange.coinbase.com/products/{product}/candles"


def _get(url: str) -> bytes | None:
    req = urllib.request.Request(url, headers={"User-Agent": "diamondhamster-research"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.read()
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def parse_binance_klines(raw_csv: bytes) -> pd.DataFrame:
    df = pd.read_csv(io.BytesIO(raw_csv), header=None)
    if not str(df.iloc[0, 0]).isdigit():  # some files carry a header row
        df = df.iloc[1:].astype(float)
    t = df[0].astype("int64")
    # Binance switched spot timestamps from milliseconds to microseconds in 2025.
    unit = t.map(lambda v: "us" if v > 10**14 else "ms")
    ts = [pd.Timestamp(v, unit=u, tz="UTC") for v, u in zip(t, unit)]
    out = pd.DataFrame({c: df[i + 1].astype(float).values for i, c in enumerate(COLUMNS)}, index=pd.DatetimeIndex(ts, name="date"))
    return out


def fetch_binance(symbol: str, start: date = date(2017, 8, 1), end: date | None = None) -> pd.DataFrame:
    """Daily klines from Binance's public bulk archive (monthly zips, daily zips for the open month)."""
    end = end or datetime.now(timezone.utc).date()
    frames = []
    m = date(start.year, start.month, 1)
    while m <= end:
        name = f"{symbol}-1d-{m:%Y-%m}"
        blob = _get(f"{BINANCE_VISION}/monthly/klines/{symbol}/1d/{name}.zip")
        if blob is None and (m.year, m.month) == (end.year, end.month):
            for d in pd.date_range(m, end, freq="D"):
                dn = f"{symbol}-1d-{d:%Y-%m-%d}"
                b = _get(f"{BINANCE_VISION}/daily/klines/{symbol}/1d/{dn}.zip")
                if b is not None:
                    frames.append(_unzip(b, dn))
        elif blob is not None:
            frames.append(_unzip(blob, name))
        m = date(m.year + (m.month == 12), m.month % 12 + 1, 1)
    if not frames:
        raise RuntimeError(f"no Binance data for {symbol}")
    return _clean(pd.concat(frames))


def _unzip(blob: bytes, name: str) -> pd.DataFrame:
    with zipfile.ZipFile(io.BytesIO(blob)) as z:
        return parse_binance_klines(z.read(f"{name}.csv"))


def fetch_coinbase(product: str, start: date = date(2015, 7, 20), end: date | None = None) -> pd.DataFrame:
    """Daily candles from Coinbase Exchange; max 300 per request, newest first."""
    end_ts = pd.Timestamp(end or datetime.now(timezone.utc).date(), tz="UTC")
    cur = pd.Timestamp(start, tz="UTC")
    rows = []
    while cur < end_ts:
        nxt = min(cur + pd.Timedelta(days=299), end_ts)
        url = COINBASE.format(product=product) + f"?granularity=86400&start={cur.isoformat()}&end={nxt.isoformat()}"
        rows += json.loads(_get(url) or b"[]")
        cur = nxt + pd.Timedelta(days=1)
        time.sleep(0.35)  # public rate limit
    df = pd.DataFrame(rows, columns=["t", "low", "high", "open", "close", "volume"])
    df.index = pd.to_datetime(df.pop("t"), unit="s", utc=True).rename("date")
    return _clean(df[COLUMNS].astype(float))


def _clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df[~df.index.duplicated(keep="first")].sort_index()
    df.index = df.index.normalize()
    return df


def save(df: pd.DataFrame, source: str, symbol: str) -> Path:
    """Write a raw file once. Re-downloading writes a new dated file; old files are never overwritten."""
    RAW.mkdir(parents=True, exist_ok=True)
    path = RAW / f"{source}_{symbol}_1d_{datetime.now(timezone.utc):%Y%m%d}.csv"
    if path.exists():
        raise FileExistsError(path)
    df.to_csv(path, float_format="%.8f")
    manifest = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}
    manifest[path.name] = {
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "rows": len(df),
        "first": str(df.index[0].date()),
        "last": str(df.index[-1].date()),
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    return path


def latest_file(source: str, symbol: str) -> Path:
    files = sorted(RAW.glob(f"{source}_{symbol}_1d_*.csv"))
    if not files:
        raise FileNotFoundError(f"no data for {source} {symbol}; run `python -m diamondhamster fetch`")
    return files[-1]


def verify(path: Path) -> None:
    expected = json.loads(MANIFEST.read_text())[path.name]["sha256"]
    if hashlib.sha256(path.read_bytes()).hexdigest() != expected:
        raise ValueError(f"{path.name} does not match its manifest hash")


def read(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, index_col="date", parse_dates=["date"])
    df.index = pd.to_datetime(df.index, utc=True)
    return df


def apply_holdout(df: pd.DataFrame, unlock_holdout: str | None = None) -> pd.DataFrame:
    """Drop holdout rows unless `unlock_holdout` names the reason, which is logged permanently."""
    if unlock_holdout is None:
        return df[df.index < HOLDOUT_START]
    HOLDOUT_LOG.parent.mkdir(parents=True, exist_ok=True)
    with HOLDOUT_LOG.open("a") as f:
        f.write(f"{datetime.now(timezone.utc).isoformat()}\t{unlock_holdout}\n")
    return df


def load(source: str, symbol: str, unlock_holdout: str | None = None) -> pd.DataFrame:
    path = latest_file(source, symbol)
    verify(path)
    return apply_holdout(read(path), unlock_holdout)
