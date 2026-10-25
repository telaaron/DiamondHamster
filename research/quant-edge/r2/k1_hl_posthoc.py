"""Post-hoc (Nachtrag N4, 2 variants, never confirmation): K1 carry with the short leg on Hyperliquid.

Funding = Hyperliquid hourly payments summed per UTC day. HL perp prices were not fetched, so the Binance perp
close stands in for the HL perp (S): cross-venue basis risk is NOT modelled, result is an upper bound.
Same mechanics as round-1 carry (capital 1.5, upkeep, 0.2 % per side per leg)."""
import json
import pandas as pd
from q2_dispersion import other_daily
from r2_common import COST, DAYS, DEV_END, HOLD_B, candles, perf

out = {}
for c in ("BTC", "ETH"):
    spot, perp = candles("spot", c, dev_only=False), candles("perp", c, dev_only=False)
    f = other_daily("hl", c, dev_only=False)
    for name, sel in (("dev_2023_05_2024", lambda i: i <= DEV_END), ("post_2026_07", lambda i: i >= HOLD_B)):
        s, p, ff = spot[sel(spot.index)], perp[sel(perp.index)], f[sel(f.index)]
        idx = s.index.intersection(p.index).intersection(ff.index)
        s, p, ff = s.loc[idx], p.loc[idx], ff.loc[idx]
        rs, rp = s["close"].pct_change(), p["close"].pct_change()
        net = ((ff + rs - rp) - rs.abs() * 0.5 * COST * 2) / 1.5
        run = perf((((ff + rs - rp) - rs.abs() * 0.5 * COST * 2) / 1.5).dropna())
        net.iloc[1] -= 2 * COST / 1.5
        net.iloc[-1] -= 2 * COST / 1.5
        o = perf(net.dropna())
        o["cagr_run_rate_ex_entry_exit"] = run["cagr"]
        o["funding_gross_ann"] = float(ff.mean() * DAYS)
        o["share_days_neg_funding"] = float((ff < 0).mean())
        out[f"{c}_{name}"] = o
        print(c, name, o["start"], o["end"], "fund", round(o["funding_gross_ann"] * 100, 1), "cagr", round(o["cagr"] * 100, 2), "run", round(o["cagr_run_rate_ex_entry_exit"] * 100, 2), "dd", round(o["max_dd"] * 100, 2), "neg30", round(o["share_neg_30d"], 3))
json.dump(out, open("../out/r2_k1_hl_posthoc.json", "w"), indent=1)
