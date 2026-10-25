"""Shared helpers for Quant-Edge round 2 (research/quant-edge/01-killkriterien-runde2.md).

Holdout rule: rows 2025-01-01..2026-06-30 are dropped at load time (assert), never used.
Data: round-1 pull in daten/, round-2 pull in daten-r2/ (both fetched on Aaron's Mac, holdout never downloaded).
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats as sps

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from qe_common import COST, DAYS, DEV_END, HOLD_A, HOLD_B, drop_holdout  # noqa: E402,F401
from qe_binance import COINS, candles, funding_daily  # noqa: E402,F401

SHARED = Path("/mnt/project-files/research/quant-edge")
R2 = SHARED / "daten-r2"
N_CUM = 121  # cumulative variant count incl. this round's pre-registered tests (WB §4)
ALPHA = 0.05 / N_CUM


def dropped(df: pd.DataFrame | pd.Series) -> pd.DataFrame | pd.Series:
    out = df[(df.index < HOLD_A) | (df.index >= HOLD_B)]
    assert not ((out.index >= HOLD_A) & (out.index < HOLD_B)).any()
    return out


def ms_index(s: pd.Series) -> pd.DatetimeIndex:
    return pd.DatetimeIndex(pd.to_datetime(s.astype("int64"), unit="ms", utc=True))


def newey_west_t(x: np.ndarray, lag: int) -> tuple[float, float]:
    """t-stat of the mean of x with Newey-West (Bartlett) standard error; two-sided normal p."""
    x = np.asarray(x, float)
    x = x[~np.isnan(x)]
    n = len(x)
    e = x - x.mean()
    v = e @ e / n
    for k in range(1, min(lag, n - 1) + 1):
        v += 2 * (1 - k / (lag + 1)) * (e[k:] @ e[:-k]) / n
    se = np.sqrt(v / n)
    t = x.mean() / se if se > 0 else float("nan")
    return float(t), float(2 * (1 - sps.norm.cdf(abs(t))))


def deflated_sharpe(r: pd.Series, n_trials: int, sr_var_trials: float, periods: int = DAYS) -> dict:
    """Deflated Sharpe Ratio (Bailey & Lopez de Prado 2014). r = per-period returns.

    sr_var_trials: variance of the per-period Sharpe estimates across the trials.
    """
    r = r.dropna()
    t = len(r)
    sr = r.mean() / r.std()
    g3 = float(sps.skew(r))
    g4 = float(sps.kurtosis(r, fisher=False))
    em = 0.5772156649
    z = sps.norm.ppf
    sr0 = np.sqrt(sr_var_trials) * ((1 - em) * z(1 - 1 / n_trials) + em * z(1 - 1 / (n_trials * np.e)))
    denom = np.sqrt(max(1 - g3 * sr + (g4 - 1) / 4 * sr**2, 1e-12))
    dsr = sps.norm.cdf((sr - sr0) * np.sqrt(t - 1) / denom)
    return {"sr_annual": float(sr * np.sqrt(periods)), "sr0_annual": float(sr0 * np.sqrt(periods)),
            "skew": g3, "kurt": g4, "dsr": float(dsr), "n_trials": n_trials}


def perf(net: pd.Series, capital_note: str = "") -> dict:
    net = net.dropna()
    eq = (1 + net).cumprod()
    yrs = len(net) / DAYS
    r30 = (1 + net).rolling(30).apply(np.prod, raw=True) - 1
    return {
        "start": str(net.index[0].date()), "end": str(net.index[-1].date()), "years": yrs,
        "cagr": float(eq.iloc[-1] ** (1 / yrs) - 1),
        "sharpe": float(net.mean() / net.std() * np.sqrt(DAYS)) if net.std() > 0 else float("nan"),
        "max_dd": float((eq / eq.cummax() - 1).min()),
        "share_neg_30d": float((r30.dropna() < 0).mean()),
        "worst_30d": float(r30.min()),
        "by_year": {str(y): float((1 + g).prod() - 1) for y, g in net.groupby(net.index.year)},
    }


def block_bootstrap_p(diff: pd.Series, block: int = 30, n: int = 5000, seed: int = 11) -> float:
    """One-sided p that mean(diff) <= 0, circular block bootstrap of the centred series."""
    rng = np.random.default_rng(seed)
    x = diff.dropna().values
    m = len(x)
    obs = x.mean()
    c = x - obs
    nb = int(np.ceil(m / block))
    cnt = 0
    for _ in range(n):
        starts = rng.integers(0, m, nb)
        idx = (starts[:, None] + np.arange(block)[None, :]).ravel()[:m] % m
        if c[idx].mean() >= obs:
            cnt += 1
    return cnt / n
