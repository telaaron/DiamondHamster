"""Q4: K1 expected value after exchange-failure risk (pre-registered, 2 calculations).

Hazard p and loss-given-failure LGD come from daten-r2/q4/events.csv (literature list, notes.md).
E[r] = carry return - p * LGD * share_on_exchange (share = 1: both legs or all capital at risk somewhere;
splitting across venues lowers variance, not the mean, unless failures are correlated).

K1 post window (2026-07+) is computed with the same mechanics as round-1 `carry()` (dev-hindsight only).
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

from r2_common import COST, DAYS, DEV_END, HOLD_B, R2, candles, funding_daily, perf

OUT = Path(__file__).resolve().parents[1] / "out"
P = {"low": 0.010, "central": 0.023, "high": 0.050}
LGD = {"fiat_claim": {"low": 0.0, "central": 0.3, "high": 0.7}, "in_kind": {"low": 0.5, "central": 0.75, "high": 0.95}}


def carry_net(coin: str, post: bool, entry_exit: bool = True) -> pd.Series:
    spot, perp, f = candles("spot", coin, dev_only=False), candles("perp", coin, dev_only=False), funding_daily(coin, dev_only=False)
    sel = (lambda i: i >= HOLD_B) if post else (lambda i: i <= DEV_END)
    spot, perp, f = spot[sel(spot.index)], perp[sel(perp.index)], f[sel(f.index)]
    idx = perp.index.intersection(spot.index).intersection(f.index)
    spot, perp, f = spot.loc[idx], perp.loc[idx], f.loc[idx]
    rs, rp = spot["close"].pct_change(), perp["close"].pct_change()
    gross = f + rs - rp
    upkeep = rs.abs() * 0.5 * COST * 2
    net = (gross - upkeep) / 1.5
    if entry_exit:
        net.iloc[1] -= 2 * COST / 1.5  # entry, two legs
        net.iloc[-1] -= 2 * COST / 1.5  # exit
    return net.dropna()


def tbill_mean(start: pd.Timestamp, end: pd.Timestamp) -> float | None:
    p = R2 / "tbill_dtb3.csv"
    if not p.exists():
        return None
    t = pd.read_csv(p)
    t.columns = ["date", "rate"]
    t["rate"] = pd.to_numeric(t["rate"], errors="coerce")
    t.index = pd.DatetimeIndex(pd.to_datetime(t["date"], utc=True))
    s = t["rate"].dropna()
    s = s[(s.index >= start) & (s.index <= end)]
    return float(s.mean() / 100) if len(s) else None


if __name__ == "__main__":
    out = {"p": P, "lgd": LGD, "coins": {}}
    for c in ("BTC", "ETH"):
        row = {}
        for name, post in (("dev_2019_2024", False), ("post_2026_07", True)):
            net = carry_net(c, post)
            o = perf(net)
            tb = tbill_mean(net.index[0], net.index[-1])
            o["tbill_mean"] = tb
            o["cagr_run_rate_ex_entry_exit"] = perf(carry_net(c, post, entry_exit=False))["cagr"]
            o["funding_gross_ann"] = float(funding_daily(c, dev_only=False).loc[net.index].mean() * DAYS)
            ev = {}
            for basis, lg in LGD.items():
                ev[basis] = {k: o["cagr"] - P[k] * lg[k] for k in P}
                ev[basis]["central_minus_tbill"] = None if tb is None else ev[basis]["central"] - tb
            o["expected_return_after_failure_risk"] = ev
            o["breakeven_p_fiat_central"] = (o["cagr"] - (tb or 0.04)) / LGD["fiat_claim"]["central"] if LGD["fiat_claim"]["central"] else None
            o["breakeven_p_inkind_central"] = (o["cagr"] - (tb or 0.04)) / LGD["in_kind"]["central"]
            row[name] = o
        dead_today = all(row["post_2026_07"]["expected_return_after_failure_risk"][b]["central_minus_tbill"] is not None
                         and row["post_2026_07"]["expected_return_after_failure_risk"][b]["central_minus_tbill"] < 0 for b in LGD)
        dead_always = all(row["dev_2019_2024"]["expected_return_after_failure_risk"][b]["central_minus_tbill"] is not None
                          and row["dev_2019_2024"]["expected_return_after_failure_risk"][b]["central_minus_tbill"] < 0 for b in LGD)
        row["verdict"] = {"oekonomisch_tot_heute": dead_today, "tot_in_jeder_funding_lage": dead_always}
        out["coins"][c] = row
        for name in ("dev_2019_2024", "post_2026_07"):
            o = row[name]
            print(c, name, "cagr", round(o["cagr"] * 100, 2), "fund", round(o["funding_gross_ann"] * 100, 2), "tbill", o["tbill_mean"], "run", round(o["cagr_run_rate_ex_entry_exit"] * 100, 2),
                  {b: round(v["central"] * 100, 2) for b, v in o["expected_return_after_failure_risk"].items()},
                  "be_p fiat/inkind", round(o["breakeven_p_fiat_central"] or 0, 3), round(o["breakeven_p_inkind_central"], 3))
        print(c, row["verdict"])
    OUT.mkdir(exist_ok=True)
    json.dump(out, open(OUT / "r2_q4.json", "w"), indent=1, default=float)
