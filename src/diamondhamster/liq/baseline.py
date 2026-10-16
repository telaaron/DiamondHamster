"""Fixe-Hebel-Baseline im Coinglass-Stil: dieselbe Engine, nur 10/25/50/100x, kein Cross, keine Übergaben."""
from __future__ import annotations

import numpy as np

from .params import LEVERAGES, SIZE_CLASSES, Params, with_overrides


def baseline_params(p: Params) -> Params:
    w = np.array([0.25 if lev in (10, 25, 50, 100) else 0.0 for lev in LEVERAGES])
    return with_overrides(p, leverage_weights={c: w.copy() for c in SIZE_CLASSES}, cross_share=0.0, alpha=0.0)
