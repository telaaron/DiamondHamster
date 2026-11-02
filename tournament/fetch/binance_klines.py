"""Fetch Binance spot daily klines for the tournament universe (replacement for TradingView get_ohlcv).

Runs on a machine that can reach api.binance.com (Aaron's Mac). Standard library only.
Writes, per coin, into <out>/<COIN>/:
  raw.json      the exact Binance response
  request.json  URL and fetch time
  payload.json  the same bars in the TradingView get_ohlcv layout that `tournament ingest` reads
and <out>/sha256.txt over all files.

    python3 tournament/fetch/binance_klines.py --out tournament/fetch/2026-11-02
"""
import argparse
import hashlib
import json
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

URL = "https://api.binance.com/api/v3/klines?symbol={sym}&interval=1d&limit=1000"
HERE = Path(__file__).resolve().parent


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    out = Path(args.out)
    coins = json.loads((HERE.parent / "universe.json").read_text())["coins"]
    for coin in coins:
        url = URL.format(sym=f"{coin}USDT")
        for attempt in range(4):
            try:
                with urllib.request.urlopen(url, timeout=30) as r:
                    body = r.read()
                break
            except Exception as e:  # network hiccup or 429
                if attempt == 3:
                    raise SystemExit(f"{coin}: {e}")
                time.sleep(2 ** (attempt + 1))
        rows = json.loads(body)
        d = out / coin
        d.mkdir(parents=True, exist_ok=True)
        (d / "raw.json").write_bytes(body)
        (d / "request.json").write_text(json.dumps({"url": url, "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                                                    "source": "Binance spot REST /api/v3/klines"}, indent=1))
        bars = [{"t": int(k[0]) // 1000, "o": float(k[1]), "h": float(k[2]), "l": float(k[3]), "c": float(k[4]), "v": float(k[5])} for k in rows]
        (d / "payload.json").write_text(json.dumps({"symbol": f"BINANCE:{coin}USDT", "source": "binance", "bars": bars}))
        print(coin, len(bars), datetime.fromtimestamp(bars[-1]["t"], timezone.utc).date())
        time.sleep(0.3)
    lines = [f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(out)}" for p in sorted(out.rglob("*.json"))]
    (out / "sha256.txt").write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
