"""Log-Preisgitter: Preis <-> Bucket-Index."""
from __future__ import annotations

import math

import numpy as np


class Grid:
    def __init__(self, p0: float, bucket_bp: float, lo_mult: float = 0.25, hi_mult: float = 4.0):
        self.bucket_bp = bucket_bp
        self.step = math.log1p(bucket_bp / 1e4)
        self.lo = p0 * lo_mult
        self.hi = p0 * hi_mult
        self.n = math.ceil(math.log(self.hi / self.lo) / self.step)
        self.edges = self.lo * np.exp(self.step * np.arange(self.n + 1))

    def index(self, price):
        p = np.asarray(price, dtype=float)
        i = np.floor(np.log(p / self.lo) / self.step).astype(int)
        return np.clip(i, 0, self.n - 1)

    def in_range(self, price):
        p = np.asarray(price, dtype=float)
        return (p >= self.edges[0]) & (p < self.edges[-1])

    def centers(self) -> np.ndarray:
        return np.sqrt(self.edges[:-1] * self.edges[1:])

    def shift_buckets(self, log_shift: float) -> int:
        return int(round(log_shift / self.step))
