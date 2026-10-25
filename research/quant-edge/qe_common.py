"""Shared helpers for the quant-edge study (research/quant-edge/bericht.md).

Holdout rule (forschungsprotokoll §1, §11): rows from 2025-01-01 to 2026-06-30 are dropped
at load time and never reach any test. `post` (2026-07-01+) is dev-only hindsight.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from diamondhamster import backtest  # noqa: E402

HOLD_A = pd.Timestamp("2025-01-01", tz="UTC")
HOLD_B = pd.Timestamp("2026-07-01", tz="UTC")
DEV_END = pd.Timestamp("2024-12-31", tz="UTC")
COST = 0.002
DAYS = 365


def drop_holdout(df: pd.DataFrame) -> pd.DataFrame:
    out = df[(df.index < HOLD_A) | (df.index >= HOLD_B)]
    assert not ((out.index >= HOLD_A) & (out.index < HOLD_B)).any()
    return out


def load_prices(name: str) -> pd.DataFrame:
    """Daily OHLCV from data/raw, holdout removed. Returns dev part only (< 2025)."""
    f = next((ROOT / "data" / "raw").glob(f"{name}_1d_*.csv"))
    df = pd.read_csv(f, parse_dates=["date"]).set_index("date").sort_index()
    df = drop_holdout(df)
    return df[df.index <= DEV_END]


def weekly_to_daily(df: pd.DataFrame, weekly_w: pd.Series) -> pd.Series:
    """Weights decided at a weekly close, held daily until the next decision."""
    return weekly_w.reindex(df.index).ffill().fillna(0.0)


def week_ends(df: pd.DataFrame) -> pd.DatetimeIndex:
    s = pd.Series(df.index, index=df.index)
    key = df.index.tz_localize(None).to_period("W-SUN")
    return pd.DatetimeIndex(s.groupby(key).max().values).tz_localize("UTC") if df.index.tz is not None and pd.DatetimeIndex(s.groupby(key).max().values).tz is None else pd.DatetimeIndex(s.groupby(key).max().values)


def stats(res: pd.DataFrame, weights: pd.Series | None = None) -> dict:
    r = res["ret"]
    eq = (1 + r).cumprod()
    yrs = len(r) / DAYS
    dd = eq / eq.cummax() - 1
    # longest stretch below a previous equity peak, in days
    under = (dd < 0).astype(int)
    longest = int(under.groupby((under == 0).cumsum()).sum().max())
    wk = (1 + r).groupby(r.index.tz_localize(None).to_period("W-SUN")).prod() - 1
    q95, q05 = np.percentile(wk, 95), np.percentile(wk, 5)
    cagr = float(eq.iloc[-1] ** (1 / yrs) - 1)
    mdd = float(dd.min())
    return {
        "cagr": cagr,
        "sharpe": float(r.mean() / r.std() * np.sqrt(DAYS)) if r.std() > 0 else 0.0,
        "max_dd": mdd,
        "calmar": cagr / abs(mdd) if mdd < 0 else float("nan"),
        "longest_dd_days": longest,
        "tail_ratio": float(abs(q95) / abs(q05)) if q05 != 0 else float("nan"),
        "mean_weight": float(res["position"].mean()),
        "turnover_per_year": float(res["turnover"].sum() / yrs),
        "days": len(r),
    }


def run(df: pd.DataFrame, w: pd.Series) -> pd.DataFrame:
    return backtest.run(df, w, cost_per_side=COST)
