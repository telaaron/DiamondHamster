"""Binance-Archiv -> EventSet (Spec 4.2). Ohne Wahrheit: keine truth.csv, keine Liquidationen."""
from __future__ import annotations

import json
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import pandas as pd

from ..events import COLUMNS, EventSet, save_events
from .download import DAILY

DAY_MS = 86_400_000


def _concat(d: Path, cols: list[str]) -> pd.DataFrame:
    files = sorted(d.glob("*.csv")) if d.exists() else []
    if not files:
        return pd.DataFrame(columns=cols)
    return pd.concat([pd.read_csv(f) for f in files], ignore_index=True)


def _day_ms(tag: str) -> int:
    return int(datetime.strptime(tag, "%Y-%m-%d").replace(tzinfo=timezone.utc).timestamp() * 1000)


def build_events(root: Path, symbol: str, out: Path) -> dict:
    base = Path(root) / "bn" / symbol
    days = {k: {f.stem for f in (base / k).glob("*.csv")} for k in DAILY}
    have = sorted(set.union(*days.values())) if any(days.values()) else []
    if not have:
        raise ValueError(f"keine Binance-Daten unter {base}")
    first, last = date.fromisoformat(have[0]), date.fromisoformat(have[-1])
    all_days = [f"{first + timedelta(n):%Y-%m-%d}" for n in range((last - first).days + 1)]
    missing = [d for d in all_days if any(d not in days[k] for k in DAILY)]

    oi = _concat(base / "metrics", COLUMNS["oi"]).drop_duplicates("ts").sort_values("ts")
    mark = _concat(base / "markPriceKlines", COLUMNS["mark"]).drop_duplicates("ts").sort_values("ts")
    if len(mark):  # Engine braucht einen Startpreis <= erstem OI-Zeitpunkt (kein Blick in die Zukunft)
        oi = oi[oi.ts >= mark.ts.iloc[0]]
    trades = _concat(base / "aggTrades", COLUMNS["trades"] + ["notional"]).sort_values("ts", kind="stable")
    funding = _concat(base / "fundingRate", COLUMNS["funding"]).drop_duplicates("ts").sort_values("ts")
    funding = funding[(funding.ts >= _day_ms(have[0])) & (funding.ts < _day_ms(have[-1]) + DAY_MS)]
    gaps = pd.DataFrame([{"start": _day_ms(d), "end": _day_ms(d) + DAY_MS, "reason": "Archiv fehlt"}
                         for d in missing], columns=COLUMNS["gaps"])

    es = EventSet(exchange="binance", symbol=symbol, trades=trades.reset_index(drop=True),
                  oi=oi.reset_index(drop=True), mark=mark.reset_index(drop=True),
                  funding=funding.reset_index(drop=True),
                  liquidations=pd.DataFrame(columns=COLUMNS["liquidations"]), gaps=gaps)
    save_events(es, out)
    ats = [_day_ms(d) for d in all_days[1:]]
    Path(out, "ats.json").write_text(json.dumps(ats))
    return {"from": have[0], "to": have[-1], "oi_rows": len(oi), "mark_rows": len(mark),
            "trade_rows": len(trades), "funding_rows": len(funding), "missing_days": missing, "snapshots": len(ats)}
