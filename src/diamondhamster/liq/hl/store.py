"""Ablage der Rohdaten auf dem Mac (Spec 3.2): gzip-JSONL je Tag, Buch-Schnappschüsse, Lücken, Zustand."""
from __future__ import annotations

import gzip
import json
import os
import zlib
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd


def _utc(ts_ms: int) -> datetime:
    return datetime.fromtimestamp(ts_ms / 1000, tz=timezone.utc)


def read_jsonl_gz(path: Path) -> tuple[list[dict], int]:
    """Liest alle vollständigen Zeilen; ein abgeschnittenes Ende (Absturz) zählt als kaputt statt abzubrechen."""
    recs, broken = [], 0
    try:
        with gzip.open(path, "rt") as f:
            for line in f:
                try:
                    recs.append(json.loads(line))
                except json.JSONDecodeError:
                    broken += 1
    except (EOFError, gzip.BadGzipFile, zlib.error):
        broken += 1
    return recs, broken


class Store:
    def __init__(self, root: Path):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)
        self._open: dict[Path, gzip.GzipFile] = {}

    def _path(self, kind: str, ts_ms: int, coin: str | None) -> Path:
        d = self.root / "raw" / kind
        if coin:
            d = d / coin
        return d / f"{_utc(ts_ms):%Y-%m-%d}.jsonl.gz"

    def append(self, kind: str, rec: dict, ts_ms: int, coin: str | None = None) -> None:
        path = self._path(kind, ts_ms, coin)
        f = self._open.get(path)
        if f is None:
            self._close_older(path)
            path.parent.mkdir(parents=True, exist_ok=True)
            f = self._open[path] = gzip.open(path, "ab")
        f.write((json.dumps(rec, separators=(",", ":")) + "\n").encode())

    def _close_older(self, path: Path) -> None:
        for p in [p for p in self._open if p.parent == path.parent]:
            self._open.pop(p).close()

    def flush(self) -> None:
        for f in self._open.values():
            f.flush()

    def close(self) -> None:
        for f in self._open.values():
            f.close()
        self._open.clear()

    def write_book(self, coin: str, ts_ms: int, df: pd.DataFrame) -> Path:
        path = self.root / "book" / coin / f"{_utc(ts_ms):%Y%m%dT%H%MZ}.csv.gz"
        path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(path, index=False)
        return path

    def gap(self, start_ms: int, end_ms: int, reason: str) -> None:
        with open(self.root / "gaps.jsonl", "a") as f:
            f.write(json.dumps({"start": int(start_ms), "end": int(end_ms), "reason": reason}) + "\n")

    def _atomic(self, name: str, d: dict) -> None:
        tmp = self.root / f"{name}.tmp"
        tmp.write_text(json.dumps(d))
        os.replace(tmp, self.root / name)

    def save_state(self, d: dict) -> None:
        self._atomic("state.json", d)

    def load_state(self) -> dict | None:
        p = self.root / "state.json"
        return json.loads(p.read_text()) if p.exists() else None

    def write_status(self, d: dict) -> None:
        self._atomic("status.json", d)
