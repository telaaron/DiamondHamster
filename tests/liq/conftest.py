import numpy as np
import pandas as pd

from diamondhamster.liq.events import COLUMNS, EventSet

STEP = 300_000  # 5 min
T0 = 1_788_220_800_000


def make_events(n: int = 50, seed: int = 0, p0: float = 100.0) -> EventSet:
    """Kleiner Zufallsmarkt: n+1 OI-Punkte im 5-min-Takt, Mark je Punkt, ein paar Trades je Intervall."""
    rng = np.random.default_rng(seed)
    ts = T0 + STEP * np.arange(n + 1)
    close = p0 * np.exp(np.cumsum(np.r_[0, rng.normal(0, 0.002, n)]))
    mark = pd.DataFrame({"ts": ts, "high": close * 1.001, "low": close * 0.999, "close": close})
    oi = pd.DataFrame({"ts": ts, "oi": 1000 + np.cumsum(np.r_[0, rng.normal(0, 5, n)])})
    rows = []
    for i in range(1, n + 1):
        for _ in range(rng.integers(1, 5)):
            rows.append((int(ts[i - 1] + rng.integers(1, STEP)), close[i] * (1 + rng.normal(0, 5e-4)),
                         float(rng.lognormal(0, 1)), bool(rng.integers(0, 2))))
    trades = pd.DataFrame(rows, columns=COLUMNS["trades"]).sort_values("ts").reset_index(drop=True)
    empty = {k: pd.DataFrame(columns=COLUMNS[k]) for k in ("funding", "liquidations", "gaps")}
    return EventSet(exchange="sim", symbol="TEST", trades=trades, oi=oi, mark=mark, **empty)
