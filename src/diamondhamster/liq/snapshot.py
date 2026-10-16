"""Point-in-time Snapshot als JSON für KI und Prüfstand (Spec 3.4)."""
from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

import numpy as np

from . import MODEL_VERSION
from .book import Book
from .grid import Grid
from .params import Params

SCHEMA = "liq-snapshot/1"
WITHIN = {"5": 0.05, "10": 0.10, "20": 0.20}


def _iso(ms: int) -> str:
    return datetime.fromtimestamp(ms / 1000, UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


@dataclass
class Snapshot:
    data: dict
    dist: dict[str, np.ndarray]
    edges: np.ndarray

    def to_json(self) -> str:
        return json.dumps(self.data, sort_keys=True, indent=2)

    def stem(self) -> str:
        return datetime.strptime(self.data["at"], "%Y-%m-%dT%H:%M:%SZ").strftime("%Y%m%dT%H%MZ")

    def save(self, directory: Path) -> None:
        directory = Path(directory)
        directory.mkdir(parents=True, exist_ok=True)
        (directory / f"{self.stem()}.json").write_text(self.to_json())
        np.savez(directory / f"{self.stem()}.npz", long=self.dist["long"], short=self.dist["short"], edges=self.edges)


def find_clusters(dist, amb, ages, grid: Grid, mark: float, side: str, min_share: float, top_n: int) -> list[dict]:
    total = dist.sum()
    if total <= 0:
        return []
    on = dist >= min_share * total
    centers = grid.centers()
    out = []
    i = 0
    while i < len(dist):
        if not on[i]:
            i += 1
            continue
        j = i
        while j + 1 < len(dist) and on[j + 1]:
            j += 1
        m = dist[i:j + 1]
        lo, hi = grid.edges[i], grid.edges[j + 1]
        out.append({
            "from": float(lo), "to": float(hi),
            "dist_pct": float((np.sqrt(lo * hi) / mark - 1) * 100),
            "notional_usd": float((m * centers[i:j + 1]).sum()),
            "share_ambiguous": float(amb[i:j + 1].sum() / m.sum()),
            "median_age_days": float((ages[i:j + 1] * m).sum() / m.sum()),
        })
        i = j + 1
    out.sort(key=lambda c: c["notional_usd"], reverse=True)
    return out[:top_n]


def _within(dist, centers, lo: float, hi: float) -> float:
    sel = (centers >= lo) & (centers <= hi)
    return float((dist[sel] * centers[sel]).sum())


def build_snapshot(book: Book, params: Params, *, exchange: str, symbol: str, at_ms: int, mark: float, oi: float,
                   quality: dict, sources: list[str], events_until_ms: int) -> Snapshot:
    grid, today = book.grid, at_ms // 86_400_000
    centers = grid.centers()
    dist = {s: book.distribution(s) for s in ("long", "short")}
    levels = {s: find_clusters(dist[s], book.ambiguous_distribution(s), book.age_distribution(s, today), grid, mark, s,
                               params.cluster_min_share, params.top_n) for s in dist}
    long_w = {k: _within(dist["long"], centers, mark * (1 - x), mark) for k, x in WITHIN.items()}
    short_w = {k: _within(dist["short"], centers, mark, mark * (1 + x)) for k, x in WITHIN.items()}
    l10, s10 = long_w["10"], short_w["10"]
    data = {
        "schema": SCHEMA, "exchange": exchange, "symbol": symbol, "at": _iso(at_ms),
        "price": {"mark": float(mark)}, "oi": float(oi), "levels": levels,
        "summary": {"long_usd_within": long_w, "short_usd_within": short_w,
                    "asymmetry_10": float((s10 - l10) / (s10 + l10)) if s10 + l10 > 0 else 0.0},
        "quality": {**quality, "seed_share": book.seed_share(), "out_of_range_share": book.out_of_range_share()},
        "provenance": {"model_version": MODEL_VERSION, "params_hash": params.params_hash,
                       "events_until": _iso(events_until_ms), "sources": list(sources)},
    }
    return Snapshot(data=data, dist=dist, edges=grid.edges.copy())


_REQUIRED = {"schema": str, "exchange": str, "symbol": str, "at": str, "price": dict, "oi": float, "levels": dict,
             "summary": dict, "quality": dict, "provenance": dict}
_LEVEL_KEYS = {"from", "to", "dist_pct", "notional_usd", "share_ambiguous", "median_age_days"}


def validate_snapshot(d: dict) -> None:
    for key, typ in _REQUIRED.items():
        assert key in d, f"Schlüssel fehlt: {key}"
        assert isinstance(d[key], typ), f"{key} hat Typ {type(d[key]).__name__}, erwartet {typ.__name__}"
    assert d["schema"] == SCHEMA
    assert set(d["levels"]) == {"long", "short"}
    for side in ("long", "short"):
        for lv in d["levels"][side]:
            assert set(lv) == _LEVEL_KEYS, f"Level-Felder: {sorted(lv)}"
    for k in ("long_usd_within", "short_usd_within"):
        assert set(d["summary"][k]) == set(WITHIN)
    assert "asymmetry_10" in d["summary"]
    for k in ("warmup", "seed_share", "out_of_range_share", "gaps", "max_drift"):
        assert k in d["quality"], f"quality.{k} fehlt"
    for k in ("model_version", "params_hash", "events_until", "sources"):
        assert k in d["provenance"], f"provenance.{k} fehlt"
