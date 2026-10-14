"""Opens/Closes je Seite aus Volumen und ΔOI, und Ablage der Opens als Liquidationspreis-Verteilung."""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .margin import liq_price_cross, liq_price_isolated, tier_for
from .params import LEVERAGES, Params, size_class


def opens_closes(volume: float, d_oi: float, alpha: float) -> tuple[float, float, float]:
    """Je Seite gleich: in jedem Trade eröffnen bzw. schließen Käufer und Verkäufer zum selben Preis.

    A = max(V − |ΔOI|, 0) ist mehrdeutiges Volumen (Übergaben); davon gilt der Anteil α als Übergabe,
    je zur Hälfte auf Long und Short.
    """
    ambiguous = alpha * max(volume - abs(d_oi), 0.0) / 2
    return max(d_oi, 0.0) + ambiguous, max(-d_oi, 0.0) + ambiguous, ambiguous


@dataclass
class Deposit:
    side: str
    mode: str
    liq_price: np.ndarray
    qty: np.ndarray


def _weights(classes: np.ndarray, max_lev: np.ndarray, params: Params) -> np.ndarray:
    lev = np.asarray(LEVERAGES)
    w = np.stack([params.leverage_weights[c] for c in classes])
    w = np.where(lev[None, :] <= max_lev[:, None], w, 0.0)
    total = w.sum(axis=1)
    for i in np.flatnonzero(total == 0):  # nichts erlaubt: alles auf den größten erlaubten Hebel
        allowed = np.flatnonzero(lev <= max_lev[i])
        w[i, allowed[-1] if len(allowed) else 0] = 1.0
    return w / w.sum(axis=1, keepdims=True)


def deposits(prices: np.ndarray, qtys: np.ndarray, open_qty: float, params: Params,
             force_class: str | None = None) -> list[Deposit]:
    prices, qtys = np.asarray(prices, dtype=float), np.asarray(qtys, dtype=float)
    entry_qty = open_qty * qtys / qtys.sum()
    notional = prices * qtys
    classes = np.full(len(prices), force_class) if force_class else size_class(notional)
    max_lev, mmr, k = tier_for(params.tiers, notional)
    w = _weights(classes, max_lev, params)
    lev = np.asarray(LEVERAGES, dtype=float)[None, :]
    E, Q = prices[:, None], qtys[:, None]
    base = entry_qty[:, None] * w
    out = []
    for side in ("long", "short"):
        iso = liq_price_isolated(side, E, lev, mmr[:, None], k[:, None], Q)
        iso = np.broadcast_to(iso, base.shape)
        cross = liq_price_cross(side, np.broadcast_to(E, base.shape), iso, params.cross_kappa)
        out.append(Deposit(side, "isolated", iso.ravel(), (base * (1 - params.cross_share)).ravel()))
        out.append(Deposit(side, "cross", cross.ravel(), (base * params.cross_share).ravel()))
    return out
