"""Q1 post-hoc robustness (Nachtrag N2): empirical null for the 2026-H2 residual, for Q1b and Q1c.

Leave-one-year-out within dev: fit on all dev years except Y, compute rolling n-day mean residuals inside Y
(n = length of the 2026-H2 prediction window). Share of those windows at or below the observed residual =
empirical p, robust to the heavy autocorrelation that makes the Newey-West t overconfident on ~80 days.
"""
import json

import numpy as np
import pandas as pd

from q1_regime import OUT, features
from r2_common import DEV_END

obs = json.load(open(OUT / "r2_q1.json"))
res = {}
for key, cols, oi in (("Q1b", ["ret30", "vol30"], False), ("Q1c", ["ret30", "vol30", "oi30"], True)):
    for c in ("BTC", "ETH"):
        d = features(c, with_oi=oi)
        dev = d[d.index <= DEV_END]
        n = obs[key][c]["n_pred"]
        wins = []
        for y in sorted(set(dev.index.year)):
            tr, te = dev[dev.index.year != y], dev[dev.index.year == y]
            if len(te) < n:
                continue
            X = np.column_stack([np.ones(len(tr))] + [tr[k] for k in cols])
            b, *_ = np.linalg.lstsq(X, tr["y"].values, rcond=None)
            r = te["y"].values - np.column_stack([np.ones(len(te))] + [te[k] for k in cols]) @ b
            wins += list(pd.Series(r).rolling(n).mean().dropna().values)
        wins = np.array(wins)
        o = obs[key][c]["resid_mean_pp"]
        res[f"{key}_{c}"] = {"observed_resid_pp": o, "n_windows": len(wins), "empirical_p_low": float((wins <= o).mean()),
                             "q05": float(np.percentile(wins, 5)), "min": float(wins.min())}
        print(key, c, res[f"{key}_{c}"])
json.dump(res, open(OUT / "r2_q1_empirical_null.json", "w"), indent=1)
