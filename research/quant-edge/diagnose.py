"""Post-hoc diagnostics (not pre-registered, not counted as tests): carry under stress events,
and at which horizon the forced-seller premium after funding extremes actually shows up."""

from __future__ import annotations

import json

import numpy as np
import pandas as pd

from k123_funding import carry, events
from qe_binance import COINS, candles, funding_daily
from qe_common import COST

STRESS = {
    "Covid 2020-03-12": ("2020-03-09", "2020-03-20"),
    "Mai-Crash 2021-05-19": ("2021-05-12", "2021-05-26"),
    "LUNA 2022-05": ("2022-05-05", "2022-05-20"),
    "Juni 2022 (Celsius/3AC)": ("2022-06-10", "2022-06-25"),
    "FTX 2022-11": ("2022-11-05", "2022-11-20"),
    "Yen-Carry 2024-08-05": ("2024-08-01", "2024-08-10"),
}

out = {"carry_stress": {}, "short_horizon": {}, "funding_streaks": {}}
for c in ("BTC", "ETH", "SOL"):
    net, _ = carry(c)
    out["carry_stress"][c] = {k: float((1 + net.loc[a:b]).prod() - 1) for k, (a, b) in STRESS.items() if len(net.loc[a:b])}
    f = funding_daily(c)
    neg = (f < 0).astype(int)
    runs = neg.groupby((neg == 0).cumsum()).sum()
    out["funding_streaks"][c] = {"longest_negative_days": int(runs.max()),
                                 "worst_30d_funding_sum": float(f.rolling(30).sum().min())}

# pooled over 12 coins: forward returns after the K2 funding trigger, by horizon
rows = []
for c in COINS:
    spot = candles("spot", c)
    f7 = funding_daily(c).rolling(7).mean()
    sig = (f7 < f7.rolling(365).quantile(0.05)).reindex(spot.index).fillna(False)
    o = spot["open"]
    for h in (1, 3, 7, 14, 28, 56):
        fr = (o.shift(-1 - h) / o.shift(-1) - 1).dropna()
        s = sig.loc[fr.index]
        first = f7.rolling(365).quantile(0.05).dropna().index[0]
        fr, s = fr[fr.index >= first], s[s.index >= first]
        ev = events(s, max(h, 7))
        if ev:
            rows.append({"coin": c, "h": h, "n": len(ev), "excess": float(fr.loc[ev].mean() - fr.mean())})
df = pd.DataFrame(rows)
for h, g in df.groupby("h"):
    w = g["n"] / g["n"].sum()
    out["short_horizon"][int(h)] = {"events": int(g["n"].sum()), "excess_weighted": float((g["excess"] * w).sum()),
                                    "coins_positive": int((g["excess"] > 0).sum()), "coins": len(g),
                                    "round_trip_cost": 2 * COST}
json.dump(out, open("out/diagnose.json", "w"), indent=1)
print(json.dumps(out, indent=1))
