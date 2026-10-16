"""Q3: carry with dated (quarterly) futures instead of perps, against the T-bill hurdle. Pre-registered D1-D3.

Mechanics (always on, D1/D2): long spot, short the quarterly future. At the close of the day before an expiry
(X-1) close the expiring contract (CURRENT_QUARTER close X-1) and short the next one (NEXT_QUARTER close X-1);
from close X onward that contract is CURRENT_QUARTER. P&L per unit notional = spot move - future move, divided
by entry spot; capital 1.5 per unit; upkeep as K1. Costs 0.2 % per side per leg.

Lookahead audit:
- Expiry dates are contract terms (last Friday of Mar/Jun/Sep/Dec, 08:00 UTC), known in advance.
- D3 decides at close X-1 from the basis observable at close X-1 and the latest T-bill print on or before X-1.
- T-bill accrual uses the print of day t-1 (FRED dates are the observation day).
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

from r2_common import COST, DAYS, DEV_END, R2, candles, dropped, ms_index, perf

OUT = Path(__file__).resolve().parents[1] / "out"
CAP = 1.5


def last_friday(y: int, m: int) -> pd.Timestamp:
    d = pd.Timestamp(y, m, 1) + pd.offsets.MonthEnd(0)
    while d.weekday() != 4:
        d -= pd.Timedelta(days=1)
    return d.tz_localize("UTC")


EXPIRIES = [last_friday(y, m) for y in range(2019, 2027) for m in (3, 6, 9, 12)]


def load_dated(kind: str, coin: str, which: str) -> pd.Series:
    df = pd.read_csv(R2 / f"dated_{kind}_{coin}_{which}.csv")
    s = pd.Series(df["close"].astype(float).values, index=ms_index(df["ts"]).floor("D")).sort_index()
    s = s[~s.index.duplicated()]
    return dropped(s[s.index <= DEV_END])


def tbill_daily(idx: pd.DatetimeIndex) -> pd.Series:
    t = pd.read_csv(R2 / "tbill_dtb3.csv")
    t.columns = ["date", "rate"]
    t["rate"] = pd.to_numeric(t["rate"], errors="coerce")
    s = pd.Series(t["rate"].values, index=pd.DatetimeIndex(pd.to_datetime(t["date"], utc=True))).dropna().sort_index()
    s = dropped(s)
    s = s.reindex(s.index.union(idx)).ffill().reindex(idx)
    return (s / 100 / 360).shift(1)  # simple daily accrual on discount yield, print of t-1


def dated_carry(kind: str, coin: str, mode: str = "always") -> tuple[pd.Series, dict]:
    spot = candles("spot", coin)["close"]
    cur, nxt = load_dated(kind, coin, "current"), load_dated(kind, coin, "next")
    idx = spot.index.intersection(cur.index).intersection(nxt.index)
    spot, cur, nxt = spot.loc[idx], cur.loc[idx], nxt.loc[idx]
    tb = tbill_daily(idx)
    rolls = [x - pd.Timedelta(days=1) for x in EXPIRIES if idx[0] < x - pd.Timedelta(days=1) < idx[-1]]
    rolls = [r for r in rolls if r in idx]
    start = rolls[0]
    days = idx[idx >= start]
    net = pd.Series(0.0, index=days)
    held_on = pd.Series(False, index=days)
    log = []
    for i, r in enumerate(rolls):
        end = rolls[i + 1] if i + 1 < len(rolls) else days[-1]
        seg = days[(days > r) & (days <= end)]
        if len(seg) == 0:
            continue
        expiry = r + pd.Timedelta(days=1)
        nxt_exp = next(x for x in EXPIRIES if x > expiry)
        dte = (nxt_exp - r).days
        basis_ann = (nxt.loc[r] / spot.loc[r] - 1) * DAYS / dte
        on = True
        if mode == "cond":
            on = basis_ann > float(tb.loc[r] * 360) + 0.02 if not np.isnan(tb.loc[r]) else False
        log.append({"roll": str(r.date()), "dte": dte, "basis_ann": float(basis_ann), "tbill": float(tb.loc[r] * 360) if not np.isnan(tb.loc[r]) else None, "on": bool(on)})
        if not on:
            net.loc[seg] = tb.loc[seg].fillna(0).values  # capital in T-bills for the quarter
            continue
        s0 = spot.loc[r]
        fut = pd.concat([pd.Series([nxt.loc[r]], index=[r]), cur.loc[seg]])
        sp = spot.loc[[r] + list(seg)]
        pnl = (sp.diff() - fut.diff()).iloc[1:] / s0
        upkeep = sp.pct_change().abs().iloc[1:] * 0.5 * COST * 2
        net.loc[seg] = ((pnl - upkeep) / CAP).values
        held_on.loc[seg] = True
    # trading costs: entering/exiting a held quarter costs the future leg 2 sides; spot leg in/out when state flips
    state = [l["on"] for l in log]
    for i, l in enumerate(log):
        r = pd.Timestamp(l["roll"], tz="UTC")
        first = days[days > r][0] if (days > r).any() else None
        if first is None or not l["on"]:
            continue
        c = 2 * COST  # open new future now + close it at the next roll
        prev_on = state[i - 1] if i > 0 else False
        if not prev_on:
            c += COST  # buy spot
        nxt_on = state[i + 1] if i + 1 < len(state) else False
        if not nxt_on:
            c += COST  # sell spot at the end of this quarter
        net.loc[first] -= c / CAP
    excess = net - tb.reindex(net.index).fillna(0)
    out = perf(net)
    ex_eq = (1 + excess).cumprod()
    out.update({
        "kind": kind, "coin": coin, "mode": mode, "quarters": len(log), "quarters_on": int(sum(state)),
        "mean_basis_ann_at_roll": float(np.mean([l["basis_ann"] for l in log])),
        "tbill_mean_ann": float(tb.reindex(net.index).mean() * 360),
        "excess_cagr_over_tbill": float(ex_eq.iloc[-1] ** (DAYS / len(excess)) - 1),
        "rolls": log,
    })
    return net, out


def verdict(o: dict) -> str:
    dead = o["excess_cagr_over_tbill"] <= 0 or o["max_dd"] < -0.10 or o["share_neg_30d"] > 0.25
    return "tot" if dead else "lebt (Dev)"


if __name__ == "__main__":
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from k123_funding import carry

    res = {"D1": {}, "D2": {}, "D3": {}, "K1_same_window": {}, "data_check": {}}
    for coin in ("BTC", "ETH"):
        for key, kind, mode in (("D1", "um", "always"), ("D2", "cm", "always"), ("D3", "um", "cond")):
            try:
                net, o = dated_carry(kind, coin, mode)
            except FileNotFoundError as e:
                res[key][coin] = {"error": str(e)}
                continue
            o["verdict"] = verdict(o)
            res[key][coin] = o
            if key == "D1":
                k1net, _ = carry(coin)
                k1 = k1net.loc[net.index[0]:net.index[-1]]
                res["K1_same_window"][coin] = perf(k1)
                # roll-continuity check: NEXT close at X-1 vs CURRENT close at X (same contract) vs CURRENT X-1
                cur, nxt = load_dated(kind, coin, "current"), load_dated(kind, coin, "next")
                chk = []
                for x in EXPIRIES:
                    a, b = x - pd.Timedelta(days=1), x
                    if a in nxt.index and b in cur.index and a in cur.index:
                        chk.append({"expiry": str(x.date()), "next_xm1": float(nxt[a]), "cur_x": float(cur[b]), "cur_xm1": float(cur[a])})
                res["data_check"][coin] = chk
            print(key, coin, o["start"], o["end"], "cagr", round(o["cagr"] * 100, 2), "excess", round(o["excess_cagr_over_tbill"] * 100, 2),
                  "dd", round(o["max_dd"] * 100, 2), "neg30", round(o["share_neg_30d"], 3), "basis", round(o["mean_basis_ann_at_roll"] * 100, 2), o["verdict"])
    OUT.mkdir(exist_ok=True)
    json.dump(res, open(OUT / "r2_q3.json", "w"), indent=1, default=float)
