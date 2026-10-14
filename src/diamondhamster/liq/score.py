"""Bewertung: Modell-Buch gegen wahres Buch (Simulator, später Hyperliquid), Spec 3.5."""
from __future__ import annotations

import numpy as np
import pandas as pd

from .events import EventSet
from .snapshot import Snapshot

SIDES = ("long", "short")


def overlap(p: np.ndarray, q: np.ndarray) -> float:
    p, q = np.asarray(p, dtype=float), np.asarray(q, dtype=float)
    if p.sum() <= 0 or q.sum() <= 0:
        return 0.0
    return float(np.minimum(p / p.sum(), q / q.sum()).sum())


def truth_dist(truth: pd.DataFrame, ts: int, edges: np.ndarray, side: str) -> np.ndarray:
    t = truth[(truth.ts == ts) & (truth.side == side)]
    n = len(edges) - 1
    idx = np.clip(np.searchsorted(edges, t.liq_price.to_numpy(), side="right") - 1, 0, n - 1)
    return np.bincount(idx, weights=t.qty.to_numpy(), minlength=n).astype(float)


def _at_ms(snap: Snapshot) -> int:
    return int(pd.Timestamp(snap.data["at"]).value // 1_000_000)


def liq_corr(snap: Snapshot, events: EventSet, horizon_ms: int = 86_400_000) -> float:
    at = _at_ms(snap)
    m = events.mark[(events.mark.ts > at) & (events.mark.ts <= at + horizon_ms)]
    if m.empty:
        return float("nan")
    edges = snap.edges
    centers = np.sqrt(edges[:-1] * edges[1:])
    reached = (centers >= m.low.min()) & (centers <= m.high.max())
    if reached.sum() < 5:
        return float("nan")
    liq = events.liquidations[(events.liquidations.ts > at) & (events.liquidations.ts <= at + horizon_ms)]
    idx = np.clip(np.searchsorted(edges, liq.price.to_numpy(), side="right") - 1, 0, len(centers) - 1)
    actual = np.bincount(idx, weights=liq.qty.to_numpy(), minlength=len(centers))[reached]
    pred = (snap.dist["long"] + snap.dist["short"])[reached]
    # Spearman = Pearson auf Rängen (ohne scipy)
    return float(pd.Series(pred).rank().corr(pd.Series(actual).rank()))


def score_snapshots(snaps: list[Snapshot], truth: pd.DataFrame, events: EventSet,
                    include_warmup: bool = False) -> dict:
    use = [s for s in snaps if include_warmup or not s.data["quality"]["warmup"]]
    if not use:
        raise ValueError("keine Snapshots nach dem Warmup")
    ov = {side: [overlap(s.dist[side], truth_dist(truth, _at_ms(s), s.edges, side)) for s in use] for side in SIDES}
    corr = [liq_corr(s, events) for s in use]
    finite = [c for c in corr if np.isfinite(c)]
    return {"overlap_long": float(np.mean(ov["long"])), "overlap_short": float(np.mean(ov["short"])),
            "overlap": float(np.mean(ov["long"] + ov["short"])),
            "liq_corr": float(np.mean(finite)) if finite else float("nan"), "n": len(use)}
