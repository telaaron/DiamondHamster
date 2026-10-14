"""Zustand der Engine: Masse je Seite × Margin-Modus × Kohorte × Preis-Bucket (Spec 3.3)."""
from __future__ import annotations

import numpy as np

from .attribution import Deposit
from .grid import Grid

SIDES = ("long", "short")
MODES = ("isolated", "cross")
ISO = 0


def _shift(arr: np.ndarray, k: int) -> np.ndarray:
    """Verschiebt entlang der letzten Achse um k Buckets; was herausfällt, landet im Randbucket."""
    if k == 0:
        return arr
    out = np.zeros_like(arr)
    if k > 0:
        out[..., k:] = arr[..., :-k]
        out[..., -1] += arr[..., -k:].sum(axis=-1)
    else:
        out[..., :k] = arr[..., -k:]
        out[..., 0] += arr[..., :-k].sum(axis=-1)
    return out


class Book:
    SEED = -1

    def __init__(self, grid: Grid, max_cohorts: int, start_day: int = 0):
        self.grid = grid
        self.max_cohorts = max_cohorts
        self.start_day = start_day
        self._mass: dict[int, np.ndarray] = {}   # cohort -> (side, mode, bucket)
        self._amb: dict[int, np.ndarray] = {}
        self._shift: dict[int, float] = {}        # cohort -> log-Preis-Verschiebung (nur isolated)

    def cohorts(self) -> list[int]:
        return sorted(self._mass)

    def _ensure(self, cohort: int) -> None:
        if cohort not in self._mass:
            shape = (len(SIDES), len(MODES), self.grid.n)
            self._mass[cohort], self._amb[cohort], self._shift[cohort] = np.zeros(shape), np.zeros(shape), 0.0

    def _day(self, cohort: int) -> int:
        return self.start_day if cohort == self.SEED else cohort

    def add(self, deposit: Deposit, cohort: int, ambiguous_frac: float) -> None:
        self._ensure(cohort)
        s, m = SIDES.index(deposit.side), MODES.index(deposit.mode)
        idx = self.grid.index(deposit.liq_price)
        if m == ISO:  # gespeichert wird unverschoben; der Kohorten-Shift gilt beim Lesen
            idx = np.clip(idx - self.grid.shift_buckets(self._shift[cohort]), 0, self.grid.n - 1)
        np.add.at(self._mass[cohort][s, m], idx, deposit.qty)
        np.add.at(self._amb[cohort][s, m], idx, deposit.qty * ambiguous_frac)

    def _effective(self, store: dict, cohort: int, s: int) -> np.ndarray:
        """(mode, bucket) der Seite s mit angewandtem Funding-Shift für isolated."""
        a = store[cohort][s].copy()
        a[ISO] = _shift(a[ISO], self.grid.shift_buckets(self._shift[cohort]))
        return a

    def sweep(self, mark_low: float, mark_high: float) -> dict[str, float]:
        centers = self.grid.centers()
        lo = int(np.searchsorted(centers, mark_low, side="left"))       # Long: center >= mark_low
        hi = int(np.searchsorted(centers, mark_high, side="right")) - 1  # Short: center <= mark_high
        removed = {"long": 0.0, "short": 0.0}
        for c in self._mass:
            for m in range(len(MODES)):
                k = self.grid.shift_buckets(self._shift[c]) if m == ISO else 0
                lo_raw, hi_raw = max(lo - k, 0), min(hi - k, self.grid.n - 1)
                for store in (self._mass, self._amb):
                    if store is self._mass:
                        removed["long"] += store[c][0, m, lo_raw:].sum()
                        removed["short"] += store[c][1, m, : hi_raw + 1].sum() if hi_raw >= 0 else 0.0
                    store[c][0, m, lo_raw:] = 0.0
                    if hi_raw >= 0:
                        store[c][1, m, : hi_raw + 1] = 0.0
        return removed

    def close(self, side: str, qty: float, today: int, beta: float) -> None:
        s = SIDES.index(side)
        cs = list(self._mass)
        mass = np.array([self._mass[c][s].sum() for c in cs])
        qty = min(qty, mass.sum())
        if qty <= 0:
            return
        weight = mass * np.exp(beta * np.array([today - self._day(c) for c in cs], dtype=float))
        take = np.zeros(len(cs))
        open_ = mass > 0
        remaining = qty
        while remaining > 1e-15 * max(qty, 1.0) and open_.any():  # Wasserfüllung mit Deckel je Kohorte
            alloc = remaining * np.where(open_, weight, 0) / weight[open_].sum()
            room = mass - take
            capped = open_ & (alloc >= room)
            if not capped.any():
                take += alloc
                break
            take[capped] = mass[capped]
            open_ &= ~capped
            remaining = qty - take.sum()
        for c, m, t in zip(cs, mass, take):
            if m > 0 and t > 0:
                f = max(1.0 - t / m, 0.0)
                self._mass[c][s] *= f
                self._amb[c][s] *= f

    def apply_funding(self, rate: float) -> None:
        # rate > 0: Longs zahlen → Long-Liq (unter dem Preis) steigt = rückt hin; Shorts erhalten →
        # Short-Liq (über dem Preis) steigt = rückt weg. rate < 0 spiegelbildlich. Beides ist +rate in log-Preis.
        for c in self._shift:
            self._shift[c] += rate

    def total(self, side: str) -> float:
        s = SIDES.index(side)
        return float(sum(a[s].sum() for a in self._mass.values()))

    def scale(self, side: str, factor: float) -> None:
        s = SIDES.index(side)
        for c in self._mass:
            self._mass[c][s] *= factor
            self._amb[c][s] *= factor

    def merge_old(self, today: int) -> None:
        cs = sorted(self._mass, key=self._day)
        if len(cs) <= self.max_cohorts:
            return
        old, keep = cs[: len(cs) - self.max_cohorts + 1], cs[0]
        weights = np.array([self._mass[c].sum() for c in old])
        rest = float(np.average([self._shift[c] for c in old], weights=weights)) if weights.sum() > 0 else 0.0
        k_rest = self.grid.shift_buckets(rest)
        merged_m, merged_a = np.zeros_like(self._mass[keep]), np.zeros_like(self._amb[keep])
        for c in old:  # Shift-Unterschied zum gemeinsamen Shift in die Buckets einrechnen
            k = self.grid.shift_buckets(self._shift[c]) - k_rest
            for src, dst in ((self._mass, merged_m), (self._amb, merged_a)):
                a = src[c].copy()
                a[:, ISO] = _shift(a[:, ISO], k)
                dst += a
            del self._mass[c], self._amb[c], self._shift[c]
        self._mass[keep], self._amb[keep], self._shift[keep] = merged_m, merged_a, rest

    def _sum_effective(self, store: dict, side: str) -> np.ndarray:
        s = SIDES.index(side)
        out = np.zeros(self.grid.n)
        for c in store:
            out += self._effective(store, c, s).sum(axis=0)
        return out

    def distribution(self, side: str) -> np.ndarray:
        return self._sum_effective(self._mass, side)

    def ambiguous_distribution(self, side: str) -> np.ndarray:
        return self._sum_effective(self._amb, side)

    def age_distribution(self, side: str, today: int) -> np.ndarray:
        s = SIDES.index(side)
        num, den = np.zeros(self.grid.n), np.zeros(self.grid.n)
        for c in self._mass:
            m = self._effective(self._mass, c, s).sum(axis=0)
            num += m * (today - self._day(c))
            den += m
        return np.divide(num, den, out=np.zeros_like(num), where=den > 0)

    def seed_share(self) -> float:
        total = sum(a.sum() for a in self._mass.values())
        return float(self._mass[self.SEED].sum() / total) if total > 0 and self.SEED in self._mass else 0.0

    def out_of_range_share(self) -> float:
        total = self.total("long") + self.total("short")
        if total <= 0:
            return 0.0
        edge = sum(self.distribution(s)[[0, -1]].sum() for s in SIDES)
        return float(edge / total)
