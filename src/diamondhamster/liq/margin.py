"""Liquidationspreise (isoliert, cross) und Tier-Tabellen.

Herleitung isoliert, Long: Marge q·E/L plus PnL q·(P−E) erreicht die Wartungsmarge m·q·P − k
⇒ P = (E·(1 − 1/L) − k/q) / (1 − m). Short analog: P = (E·(1 + 1/L) + k/q) / (1 + m).
Gebühren sind vernachlässigt.
"""
from __future__ import annotations

import tomllib
from dataclasses import dataclass
from pathlib import Path

import numpy as np


@dataclass(frozen=True)
class Tier:
    max_notional: float
    max_leverage: int
    mmr: float
    maint_amount: float


def load_tiers(path: Path) -> tuple[Tier, ...]:
    with open(path, "rb") as f:
        raw = tomllib.load(f)
    tiers = [Tier(float(t["max_notional"]), int(t["max_leverage"]), float(t["mmr"]), float(t["maint_amount"]))
             for t in raw["tier"]]
    return tuple(sorted(tiers, key=lambda t: t.max_notional))


def tier_for(tiers, notional_usd):
    caps = np.array([t.max_notional for t in tiers])
    i = np.minimum(np.searchsorted(caps, np.asarray(notional_usd, dtype=float), side="left"), len(tiers) - 1)
    lev = np.array([t.max_leverage for t in tiers])[i]
    mmr = np.array([t.mmr for t in tiers])[i]
    k = np.array([t.maint_amount for t in tiers])[i]
    return lev, mmr, k


def liq_price_isolated(side: str, entry, leverage, mmr, maint_amount, qty):
    entry, leverage, mmr, k, q = (np.asarray(x, dtype=float) for x in (entry, leverage, mmr, maint_amount, qty))
    if side == "long":
        return (entry * (1 - 1 / leverage) - k / q) / (1 - mmr)
    if side == "short":
        return (entry * (1 + 1 / leverage) + k / q) / (1 + mmr)
    raise ValueError(f"side must be long or short, got {side!r}")


def liq_price_cross(side: str, entry, iso_price, kappa: float):
    entry, iso = np.asarray(entry, dtype=float), np.asarray(iso_price, dtype=float)
    if side == "long":
        return np.maximum(entry - kappa * (entry - iso), entry * 1e-6)
    if side == "short":
        return entry + kappa * (iso - entry)
    raise ValueError(f"side must be long or short, got {side!r}")
