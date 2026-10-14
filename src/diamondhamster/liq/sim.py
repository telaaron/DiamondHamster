"""Synthetischer Markt mit bekannter Wahrheit (Spec 3.5).

Der Simulator folgt den Annahmen des Modells. Ein Sieg der Engine hier zeigt, dass sie richtig rechnet,
nicht dass sie die Realität trifft.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
import pandas as pd

from .attribution import _weights
from .events import COLUMNS, EventSet, save_events
from .margin import liq_price_cross, liq_price_isolated, load_tiers, tier_for
from .params import DEFAULT_PARAMS_PATH, LEVERAGES, SIZE_CLASSES, Params, size_class, with_overrides

STEP_MS = 300_000
STEPS_PER_DAY = 288
ORIGIN_MS = 1_767_225_600_000  # 2026-01-01T00:00:00Z
FUNDING_EVERY = 96  # 8 h


def _norm(w) -> np.ndarray:
    a = np.asarray(w, dtype=float)
    return a / a.sum()


@dataclass(frozen=True)
class SimTruth:
    leverage_weights: dict = field(default_factory=lambda: {
        "small": _norm([1, 2, 5, 15, 25, 15, 20, 7, 8, 2]),
        "mid": _norm([3, 5, 12, 35, 25, 10, 7, 2, 1, 0]),
        "large": _norm([20, 20, 25, 25, 7, 3, 0, 0, 0, 0]),
    })
    cross_share: float = 0.25
    cross_kappa: float = 2.5
    beta: float = 0.05
    transfer_share: float = 0.5
    open_rate: float = 10.0
    close_rate: float = 8.0
    p_start: float = 60_000.0
    daily_vol: float = 0.03
    jump_per_day: float = 1.0
    jump_size: float = 0.05
    qty_mu: float = -1.0
    qty_sigma: float = 1.5
    funding_abs: float = 0.0001


DEFAULT_TRUTH = SimTruth()


def truth_params(base: Params, truth: SimTruth) -> Params:
    # alpha = transfer_share ist eine Näherung: im 5-min-Intervall netten auch Opens und Closes gegeneinander.
    return with_overrides(base, leverage_weights={c: _norm(truth.leverage_weights[c]) for c in SIZE_CLASSES},
                          cross_share=truth.cross_share, cross_kappa=truth.cross_kappa, beta=truth.beta,
                          alpha=truth.transfer_share)


def _reduce(qty: np.ndarray, weight: np.ndarray, amount: float) -> np.ndarray:
    """Zieht `amount` gewichtet ab, je Position höchstens ihre Menge (Wasserfüllung). Gibt neue Mengen zurück."""
    qty = qty.copy()
    amount = min(amount, qty.sum())
    w = np.where(qty > 0, weight, 0.0)
    while amount > 1e-12 and w.sum() > 0:
        alloc = amount * w / w.sum()
        take = np.minimum(alloc, qty)
        qty -= take
        amount -= take.sum()
        w = np.where(qty > 1e-15, w, 0.0)
        qty[qty <= 1e-15] = 0.0
    return qty


class _Side:
    def __init__(self):
        self.qty = np.zeros(0)
        self.liq = np.zeros(0)
        self.iso = np.zeros(0, dtype=bool)
        self.day = np.zeros(0)

    def add(self, qty, liq, iso, day):
        self.qty = np.concatenate([self.qty, qty])
        self.liq = np.concatenate([self.liq, liq])
        self.iso = np.concatenate([self.iso, iso])
        self.day = np.concatenate([self.day, np.full(len(qty), day, dtype=float)])

    def compact(self):
        keep = self.qty > 0
        self.qty, self.liq, self.iso, self.day = self.qty[keep], self.liq[keep], self.iso[keep], self.day[keep]

    def hazard(self, today: float, beta: float) -> np.ndarray:
        return self.qty * np.exp(beta * (today - self.day))


def simulate(seed: int, days: int, truth: SimTruth = DEFAULT_TRUTH, pre_days: int = 14, snapshot_every_h: int = 24,
             tiers_path: Path | None = None) -> tuple[EventSet, pd.DataFrame, list[int]]:
    rng = np.random.default_rng(seed)
    tiers = load_tiers(tiers_path or (DEFAULT_PARAMS_PATH.parent.parent / "tiers" / "illustrativ.toml"))
    sides = {"long": _Side(), "short": _Side()}
    sigma = truth.daily_vol / np.sqrt(STEPS_PER_DAY * 5)
    price = truth.p_start
    t_start = ORIGIN_MS + pre_days * 86_400_000
    snap_every = snapshot_every_h * 3_600_000
    ats = [t_start + k * snap_every for k in range(1, days * 24 // snapshot_every_h + 1)]
    trades, oi_rows, mark_rows, fund_rows, liq_rows, truth_rows = [], [], [], [], [], []

    def open_positions(side: str, qty: np.ndarray, entry: float, today: float) -> None:
        notional = qty * entry
        max_lev, mmr, k = tier_for(tiers, notional)
        w = _weights(size_class(notional), max_lev, truth.leverage_weights)
        lev = np.array([rng.choice(LEVERAGES, p=row) for row in w], dtype=float)
        iso_price = liq_price_isolated(side, entry, lev, mmr, k, qty)
        is_iso = rng.random(len(qty)) >= truth.cross_share
        liq = np.where(is_iso, iso_price, liq_price_cross(side, entry, iso_price, truth.cross_kappa))
        sides[side].add(qty, liq, is_iso, today)

    total_steps = (pre_days + days) * STEPS_PER_DAY
    for step in range(total_steps):
        t_end = ORIGIN_MS + (step + 1) * STEP_MS
        today = (t_end - 1) / 86_400_000
        emit = t_end > t_start
        # 1. Preis- und Mark-Pfad
        path = []
        for _ in range(5):
            price *= np.exp(rng.normal(0, sigma))
            if rng.random() < truth.jump_per_day / (STEPS_PER_DAY * 5):
                price *= 1 + truth.jump_size * rng.choice([-1, 1])
            path.append(price * (1 + rng.normal(0, 1e-4)))
        lo, hi, close = min(path), max(path), path[-1]
        step_trades = []
        # 2. Liquidationen
        liquidated = {}
        for side, s in sides.items():
            hit = (s.liq >= lo) if side == "long" else (s.liq <= hi)
            hit &= s.qty > 0
            q, px = s.qty[hit], np.clip(s.liq[hit], lo, hi)
            liquidated[side] = q.sum()
            if emit:
                ts = t_end - STEP_MS + rng.integers(1, STEP_MS, size=len(q))
                liq_rows += [(int(a), side, float(b), float(c)) for a, b, c in zip(ts, px, q)]
                step_trades += [(float(b), float(c)) for b, c in zip(px, q)]
            s.qty[hit] = 0.0
        for side, other in (("long", "short"), ("short", "long")):
            o = sides[other]
            o.qty = _reduce(o.qty, o.hazard(today, truth.beta), liquidated[side])
        # 3. Opens (Paare)
        n_open = rng.poisson(truth.open_rate)
        if n_open:
            q = rng.lognormal(truth.qty_mu, truth.qty_sigma, n_open)
            entry = close * (1 + rng.normal(0, 2e-4))
            open_positions("long", q, entry, today)
            open_positions("short", q, entry, today)
            step_trades += [(entry, float(x)) for x in q]
        # 4. Closes je Seite: Übergabe (gleiche Seite eröffnet neu) oder Gegenseite schließt
        for side, other in (("long", "short"), ("short", "long")):
            s = sides[side]
            k = rng.poisson(truth.close_rate)
            haz = s.hazard(today, truth.beta)
            if k == 0 or haz.sum() <= 0:
                continue
            idx = np.unique(rng.choice(len(s.qty), size=k, p=haz / haz.sum()))
            q = s.qty[idx].copy()
            s.qty[idx] = 0.0
            transfer = rng.random(len(q)) < truth.transfer_share
            if transfer.any():
                open_positions(side, q[transfer], close, today)
            o = sides[other]
            o.qty = _reduce(o.qty, o.hazard(today, truth.beta), q[~transfer].sum())
            step_trades += [(close, float(x)) for x in q]
        # Gleichstand erzwingen (nur bei extremen Schritten mit Liquidationen auf beiden Seiten nötig)
        tl, ts_ = sides["long"].qty.sum(), sides["short"].qty.sum()
        if abs(tl - ts_) > 1e-9 * max(tl, 1.0):
            big = "long" if tl > ts_ else "short"
            b = sides[big]
            b.qty = _reduce(b.qty, b.hazard(today, truth.beta), abs(tl - ts_))
        # 5. Funding
        if (step + 1) % FUNDING_EVERY == 0:
            rate = truth.funding_abs * rng.choice([-1.0, 1.0])
            for s in sides.values():
                s.liq = np.where(s.iso, s.liq * np.exp(rate), s.liq)
            if emit:
                fund_rows.append((t_end, rate))
        if step % STEPS_PER_DAY == 0:
            for s in sides.values():
                s.compact()
        if emit:
            ts = np.sort(t_end - STEP_MS + rng.integers(1, STEP_MS, size=len(step_trades)))
            trades += [(int(a), p_, q_, bool(rng.integers(0, 2))) for a, (p_, q_) in zip(ts, step_trades)]
            mark_rows.append((t_end, hi, lo, close))
            oi_rows.append((t_end, float(sides["long"].qty.sum())))
            if t_end in ats:
                for side, s in sides.items():
                    live = s.qty > 0
                    truth_rows.append(pd.DataFrame({"ts": t_end, "side": side,
                                                    "mode": np.where(s.iso[live], "isolated", "cross"),
                                                    "liq_price": s.liq[live], "qty": s.qty[live]}))

    trades_df = pd.DataFrame(trades, columns=COLUMNS["trades"]).sort_values("ts", kind="stable").reset_index(drop=True)
    events = EventSet(
        exchange="sim", symbol="SIMUSDT", trades=trades_df,
        oi=pd.DataFrame(oi_rows, columns=COLUMNS["oi"]),
        mark=pd.DataFrame(mark_rows, columns=COLUMNS["mark"]),
        funding=pd.DataFrame(fund_rows, columns=COLUMNS["funding"]),
        liquidations=pd.DataFrame(liq_rows, columns=COLUMNS["liquidations"]).sort_values("ts", kind="stable")
        .reset_index(drop=True),
        gaps=pd.DataFrame(columns=COLUMNS["gaps"]),
    )
    return events, pd.concat(truth_rows, ignore_index=True), ats


def write_sim(directory: Path, events: EventSet, truth: pd.DataFrame, ats: list[int]) -> None:
    directory = Path(directory)
    save_events(events, directory)
    truth.to_csv(directory / "truth.csv", index=False)
    (directory / "ats.json").write_text(json.dumps(ats))
