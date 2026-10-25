"""Q5: intraday forced flow. Does buying into a liquidation cascade (price crash + open-interest drop in a
15-minute bar) earn a premium within 1 h to 24 h after realistic costs and latency? Pre-registered, 30 tests.

Lookahead audit:
- Bar t = kline with open_time t, covering [t, t+15m). Its return is close_t / close_{t-1} - 1.
- OI change of bar t = OI snapshot at t+15m / OI snapshot at t - 1; the t+15m snapshot exists at the bar's end.
- Thresholds are quantiles of the previous 2880 bars (30 days), shifted by one bar: the current bar is excluded.
- Entry at open of bar t+1+L (L latency bars), exit at open of bar t+1+L+H. Nothing after t enters the decision.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

from r2_common import ALPHA, COST, DEV_END, R2, dropped, ms_index

OUT = Path(__file__).resolve().parents[1] / "out"
RNG = np.random.default_rng(5)
START = pd.Timestamp("2022-01-01", tz="UTC")
WIN = 2880


def load(coin: str) -> pd.DataFrame:
    k = pd.read_csv(R2 / f"perp15m_{coin}.csv")
    k.index = ms_index(k["ts"])
    k = dropped(k[~k.index.duplicated()].sort_index())
    m = pd.read_csv(R2 / f"metrics_15m_{coin}.csv")
    m.index = ms_index(m["ts"]).floor("15min")
    m = dropped(m[~m.index.duplicated()].sort_index())
    k = k[(k.index >= START - pd.Timedelta(days=31)) & (k.index <= DEV_END + pd.Timedelta(hours=23, minutes=45))]
    full = pd.date_range(k.index[0], k.index[-1], freq="15min")
    k = k.reindex(full)
    oi = m["sum_open_interest"].astype(float).where(lambda x: x > 0).reindex(full)
    k["ret"] = k["close"] / k["close"].shift(1) - 1
    k["doi"] = oi.shift(-1) / oi - 1
    k["q_lo"] = k["ret"].shift(1).rolling(WIN, min_periods=WIN // 2).quantile(0.002)
    k["q_hi"] = k["ret"].shift(1).rolling(WIN, min_periods=WIN // 2).quantile(0.998)
    k["q_oi"] = k["doi"].shift(1).rolling(WIN, min_periods=WIN // 2).quantile(0.05)
    return k


def run(k: pd.DataFrame, side: str, H: int, L: int, use_oi: bool, cost: float = COST) -> dict:
    o = k["open"].values
    n = len(k)
    ent = np.arange(n) + 1 + L
    ext = ent + H
    ok = ext < n
    fwd = np.full(n, np.nan)
    fwd[ok] = o[ext[ok]] / o[ent[ok]] - 1
    if side == "short":
        fwd = -fwd
    if side == "long":
        cond = k["ret"] < k["q_lo"]
    else:
        cond = k["ret"] > k["q_hi"]
    if use_oi:
        cond &= k["doi"] < k["q_oi"]
    valid = (k.index >= START) & ~np.isnan(fwd) & k["q_lo"].notna().values
    cond = cond.values & valid
    gap = max(H, 16)
    ev, block = [], -1
    for i in np.flatnonzero(cond):
        if i > block:
            ev.append(i)
            block = i + L + gap
    ev = np.array(ev, int)
    base_pool = fwd[valid]
    base = float(np.nanmean(base_pool))
    res = {"side": side, "H_bars": H, "L_bars": L, "use_oi": use_oi, "n_events": int(len(ev))}
    if len(ev) < 10:
        res["note"] = "fewer than 10 events"
        return res
    e = fwd[ev]
    draws = RNG.integers(0, len(base_pool), (10000, len(ev)))
    boot = base_pool[draws].mean(axis=1)
    p = float((boot >= e.mean()).mean())
    yrs = k.index[ev].year
    h1, h2 = e[yrs <= 2023], e[yrs == 2024]
    res.update({
        "gross_mean": float(e.mean()), "base_mean": base, "excess_gross": float(e.mean() - base),
        "excess_net": float(e.mean() - base - 2 * cost), "net_mean_trade": float(e.mean() - 2 * cost),
        "net_mean_trade_005": float(e.mean() - 2 * 0.0005), "hit_rate_net": float((e - 2 * cost > 0).mean()),
        "p_one_sided": p, "median": float(np.median(e)), "worst": float(e.min()), "best": float(e.max()),
        "excess_gross_2022_23": float(h1.mean() - base) if len(h1) else None, "n_2022_23": int(len(h1)),
        "excess_gross_2024": float(h2.mean() - base) if len(h2) else None, "n_2024": int(len(h2)),
        "first_events": [str(t) for t in k.index[ev][:5]],
    })
    return res


def verdict(rows: list[dict]) -> str:
    good = all(r.get("excess_net", -1) > 0 and r.get("p_one_sided", 1) < ALPHA
               and (r.get("excess_gross_2022_23") or -1) > 0 and (r.get("excess_gross_2024") or -1) > 0 for r in rows)
    if good:
        return "lebt"
    pre = all(r.get("excess_gross", -1) > 0 and r.get("p_one_sided", 1) < 0.05 for r in rows)
    if pre:
        return "Prämie existiert, für uns nicht erntbar" if all(r.get("excess_net", -1) <= 0 for r in rows) else "Hinweis"
    return "tot"


if __name__ == "__main__":
    out = {"alpha": ALPHA, "tests": [], "verdicts": {}}
    data = {c: load(c) for c in ("BTC", "ETH")}
    grid = []
    for H in (4, 16, 96):
        grid.append(("main", "long", H, 0, True))
        grid.append(("squeeze", "short", H, 0, True))
        grid.append(("latency", "long", H, 1, True))
        grid.append(("latency", "long", H, 4, True))
        grid.append(("price_only", "long", H, 0, False))
    for fam, side, H, L, use_oi in grid:
        rows = []
        for c, k in data.items():
            r = run(k, side, H, L, use_oi)
            r.update({"family": fam, "coin": c})
            out["tests"].append(r)
            rows.append(r)
            print(fam, c, side, "H", H, "L", L, "n", r["n_events"], "exG", round(r.get("excess_gross", np.nan) * 100, 3),
                  "exN", round(r.get("excess_net", np.nan) * 100, 3), "p", r.get("p_one_sided"),
                  "h1", None if r.get("excess_gross_2022_23") is None else round(r["excess_gross_2022_23"] * 100, 3),
                  "h2", None if r.get("excess_gross_2024") is None else round(r["excess_gross_2024"] * 100, 3))
        out["verdicts"][f"{fam}_{side}_H{H}_L{L}"] = verdict(rows)
    out["bars"] = {c: {"n": int(k.index.size), "missing_close": int(k["close"].isna().sum()), "missing_doi": int(k["doi"].isna().sum())} for c, k in data.items()}
    OUT.mkdir(exist_ok=True)
    json.dump(out, open(OUT / "r2_q5.json", "w"), indent=1, default=float)
    print(json.dumps(out["verdicts"], indent=1))
