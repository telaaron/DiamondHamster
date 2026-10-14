"""Event-Format (Spec 3.2): eine CSV je Typ plus meta.json, Validierung, point-in-time Schnitt."""
from __future__ import annotations

import json
from dataclasses import dataclass, replace
from pathlib import Path

import pandas as pd

COLUMNS: dict[str, list[str]] = {
    "trades": ["ts", "price", "qty", "taker_buy"],
    "oi": ["ts", "oi"],
    "mark": ["ts", "high", "low", "close"],
    "funding": ["ts", "rate"],
    "liquidations": ["ts", "side", "price", "qty"],
    "gaps": ["start", "end", "reason"],
}
REQUIRED = ("trades", "oi", "mark")
STRICT_TS = ("oi", "mark")
POSITIVE = {"trades": ["price", "qty"], "oi": ["oi"], "mark": ["high", "low", "close"],
            "liquidations": ["price", "qty"]}


class EventError(ValueError):
    pass


@dataclass
class EventSet:
    exchange: str
    symbol: str
    trades: pd.DataFrame
    oi: pd.DataFrame
    mark: pd.DataFrame
    funding: pd.DataFrame
    liquidations: pd.DataFrame
    gaps: pd.DataFrame

    def until(self, ts_ms: int) -> "EventSet":
        cut = {name: getattr(self, name) for name in COLUMNS if name != "gaps"}
        cut = {name: df[df.ts <= ts_ms].reset_index(drop=True) for name, df in cut.items()}
        return replace(self, **cut, gaps=self.gaps[self.gaps.start <= ts_ms].reset_index(drop=True))


def _fail(name: str, row: int, msg: str):
    raise EventError(f"{name}.csv, Zeile {row + 1}: {msg}")


def _check(name: str, df: pd.DataFrame) -> None:
    missing = [c for c in COLUMNS[name] if c not in df.columns]
    if missing:
        raise EventError(f"{name}.csv: Spalten fehlen: {missing}")
    if df.empty:
        return
    key = "start" if name == "gaps" else "ts"
    d = df[key].diff().iloc[1:]
    bad = d[(d <= 0) if name in STRICT_TS else (d < 0)]
    if len(bad):
        _fail(name, int(bad.index[0]), f"{key} nicht {'streng ' if name in STRICT_TS else ''}steigend")
    for col in POSITIVE.get(name, []):
        bad = df.index[~(df[col] > 0)]
        if len(bad):
            _fail(name, int(bad[0]), f"{col} muss > 0 sein")
    if name == "mark":
        bad = df.index[~((df.low <= df.close) & (df.close <= df.high))]
        if len(bad):
            _fail(name, int(bad[0]), "low <= close <= high verletzt")
    if name == "liquidations":
        bad = df.index[~df.side.isin(["long", "short"])]
        if len(bad):
            _fail(name, int(bad[0]), "side muss long oder short sein")


def validate(es: EventSet) -> None:
    for name in COLUMNS:
        _check(name, getattr(es, name))


def load_events(directory: Path) -> EventSet:
    directory = Path(directory)
    meta = json.loads((directory / "meta.json").read_text())
    frames = {}
    for name, cols in COLUMNS.items():
        path = directory / f"{name}.csv"
        if not path.exists():
            if name in REQUIRED:
                raise EventError(f"{name}.csv fehlt in {directory}")
            frames[name] = pd.DataFrame(columns=cols)
            continue
        frames[name] = pd.read_csv(path)
    es = EventSet(exchange=meta["exchange"], symbol=meta["symbol"], **frames)
    validate(es)
    return es


def save_events(es: EventSet, directory: Path) -> None:
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "meta.json").write_text(json.dumps({"exchange": es.exchange, "symbol": es.symbol}))
    for name, cols in COLUMNS.items():
        getattr(es, name)[cols].to_csv(directory / f"{name}.csv", index=False)
