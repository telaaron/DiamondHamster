"""Downloader für das öffentliche Binance-Archiv (Spec 4.1). Fortsetzbar, prüft sha256, verdichtet aggTrades."""
from __future__ import annotations

import hashlib
import io
import json
import time
import urllib.error
import urllib.request
import zipfile
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import pandas as pd

from ..trades import compress

BASE = "https://data.binance.vision/data/futures/um/"
DAILY = ("metrics", "markPriceKlines", "aggTrades")
RAW_COLUMNS = {
    "aggTrades": ["agg_trade_id", "price", "quantity", "first_trade_id", "last_trade_id", "transact_time",
                  "is_buyer_maker"],
    "markPriceKlines": ["open_time", "open", "high", "low", "close", "volume", "close_time", "quote_volume",
                        "count", "taker_buy_volume", "taker_buy_quote_volume", "ignore"],
    "metrics": ["create_time", "symbol", "sum_open_interest", "sum_open_interest_value"],
    "fundingRate": ["calc_time", "funding_interval_hours", "last_funding_rate"],
}


class NotFound(RuntimeError):
    pass


class ChecksumError(RuntimeError):
    pass


def url_for(kind: str, symbol: str, day: date) -> str:
    if kind == "fundingRate":
        return f"{BASE}monthly/fundingRate/{symbol}/{symbol}-fundingRate-{day:%Y-%m}.zip"
    if kind == "markPriceKlines":
        return f"{BASE}daily/markPriceKlines/{symbol}/1m/{symbol}-1m-{day:%Y-%m-%d}.zip"
    return f"{BASE}daily/{kind}/{symbol}/{symbol}-{kind}-{day:%Y-%m-%d}.zip"


def urllib_fetch(url: str, tries: int = 4) -> bytes:
    for i in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=120) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                raise NotFound(url) from e
            if i == tries - 1:
                raise
        except OSError:
            if i == tries - 1:
                raise
        time.sleep(2 ** (i + 1))
    raise AssertionError("unreachable")


def _read_csv(payload: bytes, kind: str) -> pd.DataFrame:
    with zipfile.ZipFile(io.BytesIO(payload)) as z:
        text = z.read(z.namelist()[0])
    first = text.split(b",", 1)[0].strip()
    has_header = not first.replace(b".", b"").isdigit()
    df = pd.read_csv(io.BytesIO(text), header=0 if has_header else None)
    if not has_header:
        df.columns = RAW_COLUMNS[kind][: df.shape[1]]
    return df


def _ms(s: pd.Series) -> pd.Series:
    """Binance-Zeitstempel in ms; Mikrosekunden (neuere Dateien) werden erkannt."""
    s = s.astype("int64")
    return s.where(s < 10**14, s // 1000)


def normalize(kind: str, df: pd.DataFrame) -> pd.DataFrame:
    if kind == "aggTrades":
        maker = df.is_buyer_maker.astype(str).str.lower() == "true"
        trades = pd.DataFrame({"ts": _ms(df.transact_time), "price": df.price.astype(float),
                               "qty": df.quantity.astype(float), "taker_buy": (~maker).astype(int)})
        return compress(trades.sort_values("ts", kind="stable"))
    if kind == "markPriceKlines":  # Kerze [open, open+1min) ist erst an ihrem Ende bekannt
        return pd.DataFrame({"ts": _ms(df.open_time) + 60_000, "high": df.high.astype(float),
                             "low": df.low.astype(float), "close": df.close.astype(float)})
    if kind == "metrics":
        ts = pd.to_datetime(df.create_time, utc=True).astype("int64") // 1_000_000
        return pd.DataFrame({"ts": ts, "oi": df.sum_open_interest.astype(float)})
    if kind == "fundingRate":
        return pd.DataFrame({"ts": _ms(df.calc_time), "rate": df.last_funding_rate.astype(float)})
    raise ValueError(kind)


def _verify(payload: bytes, checksum: bytes) -> None:
    want = checksum.decode().split()[0].lower()
    if hashlib.sha256(payload).hexdigest() != want:
        raise ChecksumError("sha256 stimmt nicht")


def _months(start: date, end: date):
    d = start.replace(day=1)
    while d <= end:
        yield d
        d = (d + timedelta(days=32)).replace(day=1)


def download(symbol: str, start: date, end: date, root: Path, fetch=urllib_fetch, log=print) -> dict:
    base = Path(root) / "bn" / symbol
    rep = {"done": 0, "skipped": 0, "missing": 0, "errors": 0}
    jobs = [(kind, d, f"{d:%Y-%m-%d}") for d in (start + timedelta(n) for n in range((end - start).days + 1))
            for kind in DAILY]
    jobs += [("fundingRate", m, f"{m:%Y-%m}") for m in _months(start, end)]
    for kind, day, tag in jobs:
        marker = base / "done" / kind / tag
        if marker.exists():
            rep["skipped"] += 1
            continue
        url = url_for(kind, symbol, day)
        try:
            payload = fetch(url)
            _verify(payload, fetch(url + ".CHECKSUM"))
            out = normalize(kind, _read_csv(payload, kind))
        except NotFound:
            rep["missing"] += 1
            _note(base, kind, tag, "404")
            continue
        except Exception as e:  # Prüfsumme, Netz, kaputte Datei: beim nächsten Lauf neu versuchen
            rep["errors"] += 1
            _note(base, kind, tag, f"Fehler: {e}")
            log(f"{kind} {tag}: {e}")
            continue
        (base / kind).mkdir(parents=True, exist_ok=True)
        out.to_csv(base / kind / f"{tag}.csv", index=False)
        marker.parent.mkdir(parents=True, exist_ok=True)
        marker.touch()
        rep["done"] += 1
        if kind == "aggTrades":
            log(f"{tag} fertig")
    return rep


def _note(base: Path, kind: str, tag: str, reason: str) -> None:
    base.mkdir(parents=True, exist_ok=True)
    with open(base / "missing.jsonl", "a") as f:
        f.write(json.dumps({"kind": kind, "tag": tag, "reason": reason,
                            "at": datetime.now(timezone.utc).isoformat(timespec="seconds")}) + "\n")
