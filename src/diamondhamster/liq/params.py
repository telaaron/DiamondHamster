"""Parametersatz der Engine: aus TOML laden, Hash für die Herkunft."""
from __future__ import annotations

import dataclasses
import hashlib
import json
import tomllib
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from .margin import Tier, load_tiers

LEVERAGES: tuple[int, ...] = (2, 3, 5, 10, 20, 25, 50, 75, 100, 125)
SIZE_CLASSES = ("small", "mid", "large")
DEFAULT_PARAMS_PATH = Path(__file__).parent / "presets" / "v001.toml"


def size_class(notional_usd) -> np.ndarray:
    n = np.asarray(notional_usd, dtype=float)
    return np.where(n < 10_000, "small", np.where(n < 1_000_000, "mid", "large"))


@dataclass(frozen=True)
class Params:
    bucket_bp: float
    max_cohorts: int
    alpha: float
    cross_share: float
    cross_kappa: float
    beta: float
    warmup_days: float
    drift_warn: float
    cluster_min_share: float
    top_n: int
    leverage_weights: dict
    tiers: tuple[Tier, ...]
    params_hash: str


def load_params(path: Path | None = None) -> Params:
    path = Path(path) if path else DEFAULT_PARAMS_PATH
    raw_bytes = path.read_bytes()
    raw = tomllib.loads(raw_bytes.decode())
    tiers_path = (path.parent / raw["tiers"]).resolve()
    weights = {}
    for cls in SIZE_CLASSES:
        w = np.asarray(raw["leverage_weights"][cls], dtype=float)
        if len(w) != len(LEVERAGES) or (w < 0).any() or w.sum() <= 0:
            raise ValueError(f"leverage_weights.{cls}: need {len(LEVERAGES)} non-negative weights")
        weights[cls] = w / w.sum()
    digest = hashlib.sha256(raw_bytes + tiers_path.read_bytes()).hexdigest()[:16]
    return Params(
        bucket_bp=float(raw["bucket_bp"]), max_cohorts=int(raw["max_cohorts"]), alpha=float(raw["alpha"]),
        cross_share=float(raw["cross_share"]), cross_kappa=float(raw["cross_kappa"]), beta=float(raw["beta"]),
        warmup_days=float(raw["warmup_days"]), drift_warn=float(raw["drift_warn"]),
        cluster_min_share=float(raw["cluster_min_share"]), top_n=int(raw["top_n"]),
        leverage_weights=weights, tiers=load_tiers(tiers_path), params_hash=digest,
    )


def _canon(v):
    if isinstance(v, np.ndarray):
        return [round(float(x), 12) for x in v]
    if isinstance(v, dict):
        return {k: _canon(v[k]) for k in sorted(v)}
    if isinstance(v, (tuple, list)):
        return [_canon(x) for x in v]
    if dataclasses.is_dataclass(v):
        return _canon(dataclasses.asdict(v))
    return v


def with_overrides(p: Params, **kw) -> Params:
    """Überschreibt Felder; der Hash bekommt die überschriebenen Werte mit, damit Varianten unterscheidbar bleiben."""
    base = p.params_hash.removesuffix("+override")
    payload = json.dumps({"base": base, **{k: _canon(v) for k, v in sorted(kw.items())}}, sort_keys=True)
    h = hashlib.sha256(payload.encode()).hexdigest()[:16] + "+override"
    return dataclasses.replace(p, params_hash=h, **kw)
