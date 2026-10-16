"""Hyperliquid-Rohdaten -> EventSet + truth.csv für run/score aus TP1 (Spec 3.5)."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from ..events import COLUMNS, EventSet, save_events
from ..params import DEFAULT_PARAMS_PATH
from ..trades import compress
from .store import read_jsonl_gz

MINUTE = 60_000


def _read(files) -> tuple[list[dict], int]:
    recs, broken = [], 0
    for f in sorted(files):
        r, b = read_jsonl_gz(f)
        recs += r
        broken += b
    return recs, broken


def _book_ts(path: Path) -> int:
    stem = path.name.split(".")[0]
    return int(datetime.strptime(stem, "%Y%m%dT%H%MZ").replace(tzinfo=timezone.utc).timestamp() * 1000)


def build_events(root: Path, coin: str, out: Path) -> dict:
    root, out = Path(root), Path(out)
    broken = 0

    ctx, b = _read((root / "raw" / "ctx").glob("*.jsonl.gz"))
    broken += b
    ctx = pd.DataFrame([{"ts": r["t"], **r["coins"][coin]} for r in ctx if coin in r.get("coins", {})])
    if ctx.empty:
        raise ValueError(f"keine Marktdaten für {coin} unter {root}/raw/ctx")
    ctx = ctx.drop_duplicates("ts", keep="last").sort_values("ts").reset_index(drop=True)

    candles, b = _read((root / "raw" / "candles" / coin).glob("*.jsonl.gz"))
    broken += b
    mark = ctx[["ts"]].assign(close=ctx["mark"], high=ctx["mark"], low=ctx["mark"])
    if candles:
        # Kerze [s, s+1min) gehört zum Mark-Zeitpunkt am Ende des Intervalls, also s = Minute vor ts
        c = pd.DataFrame(candles).drop_duplicates("ts", keep="last").set_index("ts")
        key = (mark.ts // MINUTE - 1) * MINUTE
        mark["high"] = pd.concat([mark.high, key.map(c.high)], axis=1).max(axis=1)
        mark["low"] = pd.concat([mark.low, key.map(c.low)], axis=1).min(axis=1)

    trades, b = _read((root / "raw" / "trades" / coin).glob("*.jsonl.gz"))
    broken += b
    tr = pd.DataFrame(trades, columns=["ts", "price", "qty", "taker_buy", "tid"])
    n_raw = len(tr)
    tr = tr.drop_duplicates(["tid", "ts"]).sort_values("ts", kind="stable")
    trades_c = compress(tr[["ts", "price", "qty", "taker_buy"]])

    funding, b = _read((root / "raw" / "funding" / coin).glob("*.jsonl.gz"))
    broken += b
    fu = pd.DataFrame(funding, columns=["ts", "rate"]).drop_duplicates("ts").sort_values("ts")

    gaps_path = root / "gaps.jsonl"
    gaps = pd.DataFrame([json.loads(l) for l in gaps_path.read_text().splitlines() if l.strip()]
                        if gaps_path.exists() else [], columns=COLUMNS["gaps"])

    es = EventSet(exchange="hyperliquid", symbol=coin, trades=trades_c, oi=ctx[["ts", "oi"]],
                  mark=mark[["ts", "high", "low", "close"]], funding=fu.reset_index(drop=True),
                  liquidations=pd.DataFrame(columns=COLUMNS["liquidations"]), gaps=gaps)
    save_events(es, out)

    first = int(ctx.ts.iloc[0])
    truth, ats = [], []
    for f in sorted((root / "book" / coin).glob("*.csv.gz")):
        ts = _book_ts(f)
        if ts < first:
            continue
        book = pd.read_csv(f)
        book = book[book.liq_px.notna()]
        truth.append(pd.DataFrame({"ts": ts, "side": book.side, "mode": book["mode"], "liq_price": book.liq_px,
                                   "qty": book.qty}))
        ats.append(ts)
    pd.concat(truth or [pd.DataFrame(columns=["ts", "side", "mode", "liq_price", "qty"])]).to_csv(
        out / "truth.csv", index=False)
    (out / "ats.json").write_text(json.dumps(ats))

    max_lev = int(ctx["max_lev"].iloc[-1])
    (out / "tiers.toml").write_text(
        f'source = "Hyperliquid metaAndAssetCtxs, maxLeverage {coin}; Wartungssatz 1/(2*maxLeverage)"\n\n'
        f"[[tier]]\nmax_notional = 1e15\nmax_leverage = {max_lev}\nmmr = {1 / (2 * max_lev)}\nmaint_amount = 0\n")
    params = DEFAULT_PARAMS_PATH.read_text()
    (out / "params.toml").write_text(
        "\n".join('tiers = "tiers.toml"' if l.startswith("tiers") else l for l in params.splitlines()) + "\n")
    return {"oi_rows": len(es.oi), "trade_rows": len(trades_c), "raw_trades": n_raw,
            "duplicate_trades": n_raw - len(tr), "funding_rows": len(fu), "snapshots": len(ats),
            "broken_lines": broken, "from": first, "to": int(ctx.ts.iloc[-1])}
