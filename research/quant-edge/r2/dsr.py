"""Deflated Sharpe Ratio for the round-2 survivors (K1, D3, R5), N = cumulative variant count.
Variance of Sharpe across trials: per-period Sharpe of all daily-return strategy trials computed this round."""
import json
import numpy as np
import pandas as pd
import r2_common  # noqa: F401  (puts round-1 code on sys.path)
from k123_funding import carry
import q2_dispersion as q2
from q3_dated import dated_carry
from r2_common import COINS, DEV_END, N_CUM, deflated_sharpe

N = N_CUM + 2 + 2 + 6 + 4  # + Nachträge N2 (Q1 empirical null x4 -> 2 counted beyond N1), Q2 no-cost diagnostics 6, Q5 post-hoc 4
series = {}
for c in ("BTC", "ETH"):
    series[f"K1_{c}"] = carry(c)[0]
    for key, kind, mode in (("D1", "um", "always"), ("D2", "cm", "always"), ("D3", "um", "cond")):
        series[f"{key}_{c}"] = dated_carry(kind, c, mode)[0]
nets = pd.DataFrame({c: carry(c)[0] for c in COINS}).sort_index()
nets = nets[nets.index <= DEV_END]
series["bench12"] = q2.portfolio(nets, pd.DataFrame(True, index=nets.index, columns=COINS))
for k, m in q2.rule_masks(nets).items():
    series[k] = q2.portfolio(nets, m)
for k, ex in (("X1", "bybit"), ("X2", "hl")):
    series[k] = q2.spread_carry(ex)[0]
srs = np.array([s.mean() / s.std() for s in series.values()])
var = float(srs.var(ddof=1))
out = {"N": N, "sr_var_per_day": var, "n_series": len(srs), "dsr": {}}
for k in ("K1_BTC", "K1_ETH", "D3_BTC", "D3_ETH", "R5", "bench12"):
    out["dsr"][k] = deflated_sharpe(series[k], N, var)
    print(k, {a: round(b, 3) if isinstance(b, float) else b for a, b in out["dsr"][k].items()})
json.dump(out, open("../out/r2_dsr.json", "w"), indent=1)
