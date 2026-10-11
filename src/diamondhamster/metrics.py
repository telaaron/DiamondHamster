"""Performance metrics on a backtest result (daily rows, crypto trades 365 days a year)."""

from __future__ import annotations

import numpy as np
import pandas as pd

from .config import REGIMES

DAYS = 365


def summary(res: pd.DataFrame) -> dict:
    r = res["ret"]
    eq = res["equity"]
    years = len(r) / DAYS
    entries = int(((res["position"] > 0) & (res["position"].shift(1, fill_value=0) == 0)).sum())
    return {
        "cagr": float(eq.iloc[-1] ** (1 / years) - 1) if years > 0 else float("nan"),
        "max_drawdown": float((eq / eq.cummax() - 1).min()),
        "sharpe": float(r.mean() / r.std() * np.sqrt(DAYS)) if r.std() > 0 else 0.0,
        "exposure": float((res["position"] > 0).mean()),
        "entries": entries,
        "total_return": float(eq.iloc[-1] - 1),
        "days": len(r),
    }


def by_regime(res: pd.DataFrame) -> pd.DataFrame:
    rows = {}
    for name, (a, b) in REGIMES.items():
        part = res.loc[a:b]
        if len(part) > 30:
            part = part.assign(equity=(1 + part["ret"]).cumprod())
            rows[name] = summary(part)
    return pd.DataFrame(rows).T
