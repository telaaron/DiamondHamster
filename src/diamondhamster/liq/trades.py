"""Trades verdichten: eine Zeile je Minute und Größenklasse (Spec TP2/TP3, Abschnitt 2)."""
from __future__ import annotations

import numpy as np
import pandas as pd

from .params import SIZE_CLASSES, size_class

MINUTE_MS = 60_000
OUT_COLUMNS = ["ts", "price", "qty", "taker_buy", "notional"]


def compress(df: pd.DataFrame) -> pd.DataFrame:
    """`ts` = Ende der Minute (ein Bucket ist erst danach bekannt), `price` = VWAP, `notional` =
    mengengewichtetes Mittel des Einzel-Trade-Notionals, `taker_buy` = Mehrheit der Menge."""
    if df.empty:
        return pd.DataFrame(columns=OUT_COLUMNS)
    price, qty = df.price.to_numpy(float), df.qty.to_numpy(float)
    notional = price * qty
    g = pd.DataFrame({
        "ts": (df.ts.to_numpy(np.int64) // MINUTE_MS + 1) * MINUTE_MS,
        "cls": pd.Categorical(size_class(notional), categories=SIZE_CLASSES, ordered=True),
        "pq": notional, "qty": qty, "buy": qty * (df.taker_buy.to_numpy(float) > 0), "nq": notional * qty,
    }).groupby(["ts", "cls"], observed=True, sort=True).sum()
    out = pd.DataFrame({"ts": g.index.get_level_values("ts"), "price": (g.pq / g.qty).to_numpy(),
                        "qty": g.qty.to_numpy(), "taker_buy": (g.buy > g.qty / 2).astype(int).to_numpy(),
                        "notional": (g.nq / g.qty).to_numpy()})
    return out.reset_index(drop=True)
