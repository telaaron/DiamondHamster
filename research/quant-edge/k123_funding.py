"""K1 carry, K2 forced-seller reversal, K3 overheating filter. Pre-registered in 00-killkriterien.md.

Lookahead audit:
- funding_daily[t] sums payments at 00/08/16 UTC of day t; all are known at the close of day t.
- Trailing percentiles use rows t-364..t (inclusive of t, known at close t) via rolling(365).
- K2 entries at open t+1 after a signal at close t; returns open-to-open.
- K3 weights decided at week-end close, applied from next open by backtest.run.
- K1 is always on, so it uses no signal at all; P&L uses realised funding and closes only.
"""

from __future__ import annotations

import json

import numpy as np
import pandas as pd

from qe_binance import COINS, candles, funding_daily
from qe_common import COST, DAYS, run, stats, week_ends, weekly_to_daily

RNG = np.random.default_rng(7)


# ---------- K1 ----------
def carry(coin: str, capital: float = 1.5, cond: bool = False) -> tuple[pd.Series, dict]:
    spot, perp, f = candles("spot", coin), candles("perp", coin), funding_daily(coin)
    idx = perp.index.intersection(spot.index).intersection(f.index)
    spot, perp, f = spot.loc[idx], perp.loc[idx], f.loc[idx]
    rs, rp = spot["close"].pct_change(), perp["close"].pct_change()
    on = pd.Series(1.0, index=idx)
    if cond:  # post-hoc variant: only on while last 7 days paid more than ~10 % p.a.
        on = (f.rolling(7).mean() * DAYS > 0.10).astype(float).shift(1).fillna(0.0)
    gross = on * (f + rs - rp)  # short perp earns funding, hedge P&L is spot minus perp move
    # hedge upkeep: keep perp margin at 0.5 x notional -> move half of each daily price change, both legs
    upkeep = on * rs.abs() * 0.5 * COST * 2
    switches = on.diff().abs().fillna(on.iloc[0])
    entry_exit = switches * 2 * COST  # two legs per switch
    entry_exit.iloc[-1] += on.iloc[-1] * 2 * COST  # close out at the end
    net = (gross - upkeep - entry_exit) / capital
    net = net.dropna()
    eq = (1 + net).cumprod()
    yrs = len(net) / DAYS
    r30 = (1 + net).rolling(30).apply(np.prod, raw=True) - 1
    mdd = float((eq / eq.cummax() - 1).min())
    by_year = {str(y): float((1 + g).prod() - 1) for y, g in net.groupby(net.index.year)}
    funding_ann = {str(y): float(g.mean() * DAYS) for y, g in f.groupby(f.index.year)}
    neg_days = float((f < 0).mean())
    # one exchange failure: half the capital lost once, at the worst moment for a compounding path
    cagr = float(eq.iloc[-1] ** (1 / yrs) - 1)
    cagr_default = float((eq.iloc[-1] * 0.5) ** (1 / yrs) - 1)
    out = {
        "coin": coin, "start": str(idx[0].date()), "end": str(idx[-1].date()), "years": yrs,
        "cagr_on_capital": cagr, "sharpe": float(net.mean() / net.std() * np.sqrt(DAYS)),
        "max_dd": mdd, "share_neg_30d": float((r30.dropna() < 0).mean()),
        "worst_30d": float(r30.min()), "share_days_funding_negative": neg_days,
        "time_on": float(on.mean()), "cagr_with_one_50pct_exchange_loss": cagr_default,
        "by_year": by_year, "funding_annualised_by_year": funding_ann,
        "max_7d_perp_rally": float((perp["close"] / perp["close"].shift(7) - 1).max()),
    }
    return net, out


# ---------- K2 ----------
def events(signal: pd.Series, hold: int) -> list[pd.Timestamp]:
    out, block = [], None
    for t, v in signal.items():
        if v and (block is None or t > block):
            out.append(t)
            block = t + pd.Timedelta(days=hold)
    return out


def fwd(spot: pd.DataFrame, hold: int) -> pd.Series:
    o = spot["open"]
    return o.shift(-1 - hold) / o.shift(-1) - 1  # buy open t+1, sell open t+1+hold


def k2(coin: str, trigger: str, hold: int, n_boot: int = 10000) -> dict:
    spot = candles("spot", coin)
    if trigger == "funding":
        f = funding_daily(coin).rolling(7).mean()
        thr = f.rolling(365).quantile(0.05)
        sig = (f < thr).reindex(spot.index).fillna(False)
    else:
        r7 = spot["close"].pct_change(7)
        thr = r7.rolling(365).quantile(0.05)
        sig = (r7 < thr).fillna(False)
    fr = fwd(spot, hold) - 2 * COST
    valid = fr.dropna()
    sig = sig.loc[valid.index]
    first_valid = thr.dropna().index[0] if trigger == "price" else funding_daily(coin).rolling(7).mean().rolling(365).quantile(0.05).dropna().index[0]
    valid = valid[valid.index >= first_valid]
    sig = sig.loc[valid.index]
    ev = events(sig, hold)
    if len(ev) == 0:
        return {"coin": coin, "trigger": trigger, "hold": hold, "n": 0}
    er = valid.loc[ev]
    base = float(valid.mean())
    boot = np.array([valid.iloc[RNG.integers(0, len(valid), len(ev))].mean() for _ in range(n_boot)])
    mid = valid.index[0] + (valid.index[-1] - valid.index[0]) / 2
    h1, h2 = er[er.index < mid], er[er.index >= mid]
    # Monte Carlo over trade order: compounding the events one after another in random order
    seq_dd = []
    for _ in range(2000):
        e = (1 + RNG.permutation(er.values)).cumprod()
        seq_dd.append(float((e / np.maximum.accumulate(e) - 1).min()))
    return {
        "coin": coin, "trigger": trigger, "hold": hold, "n": len(ev),
        "window": f"{valid.index[0].date()}..{valid.index[-1].date()}",
        "event_mean": float(er.mean()), "event_median": float(er.median()), "hit_rate": float((er > 0).mean()),
        "base_mean": base, "excess": float(er.mean() - base),
        "p_one_sided": float((boot >= er.mean()).mean()),
        "excess_half1": float(h1.mean() - base) if len(h1) else None, "n_half1": len(h1),
        "excess_half2": float(h2.mean() - base) if len(h2) else None, "n_half2": len(h2),
        "worst_event": float(er.min()), "best_event": float(er.max()),
        "mc_order_maxdd_median": float(np.median(seq_dd)), "mc_order_maxdd_p95": float(np.percentile(seq_dd, 5)),
        "dates": [str(d.date()) for d in ev],
    }


# ---------- K3 ----------
def k3_weights(spot: pd.DataFrame, f: pd.Series, delay: int = 0) -> pd.Series:
    f7 = f.rolling(7).mean()
    hot = f7 > f7.rolling(365).quantile(0.90)
    w = pd.Series(np.where(hot, 0.5, 1.0), index=f7.index)
    w[f7.rolling(365).quantile(0.90).isna()] = np.nan
    w = w.shift(delay)
    w = w.reindex(spot.index)
    we = week_ends(spot)
    return weekly_to_daily(spot, w.loc[we].dropna())


def k3(coin: str, delay: int = 0, drop_frac: float = 0.0) -> dict:
    spot, f = candles("spot", coin), funding_daily(coin)
    if drop_frac:
        keep = RNG.random(len(f)) >= drop_frac
        f = f[keep].reindex(f.index).ffill()
    w = k3_weights(spot, f, delay)
    start = w[w > 0].index[0]
    spot, w = spot.loc[start:], w.loc[start:]
    res = run(spot, w)
    const = run(spot, pd.Series(float(w.mean()), index=spot.index))
    d = res["ret"] - const["ret"]
    wk = d.groupby(d.index.tz_localize(None).to_period("W-SUN")).sum()
    yr = {str(y): float(g.sum()) for y, g in d.groupby(d.index.year)}
    return {
        "coin": coin, "delay_days": delay, "drop_frac": drop_frac, "start": str(start.date()),
        "mean_weight": float(w.mean()), "share_weeks_hot": float((w < 1).mean()),
        "timing_value_pct_per_week": float(wk.mean() * 100), "t_weekly": float(wk.mean() / wk.std() * np.sqrt(len(wk))),
        "timing_value_by_year": yr, "strategy": stats(res), "constant": stats(const),
    }


if __name__ == "__main__":
    out = {"K1": {}, "K1_cond_posthoc": {}, "K2": [], "K3": {}, "K3_ablation": [], "K1_all": {}, "K2_all": [], "K3_all": {}}
    nets = {}
    for c in COINS:
        net, o = carry(c)
        nets[c] = net
        (out["K1"] if c in ("BTC", "ETH") else out["K1_all"])[c] = o
    for c in ("BTC", "ETH"):
        out["K1_cond_posthoc"][c] = carry(c, cond=True)[1]
    pf = pd.DataFrame(nets).dropna(how="all").mean(axis=1)
    eq = (1 + pf).cumprod()
    out["K1_portfolio_12"] = {"cagr": float(eq.iloc[-1] ** (DAYS / len(pf)) - 1), "sharpe": float(pf.mean() / pf.std() * np.sqrt(DAYS)),
                              "max_dd": float((eq / eq.cummax() - 1).min()), "start": str(pf.index[0].date())}
    for c in ("BTC", "ETH"):
        for trig in ("funding", "price"):
            for h in (28, 56):
                out["K2"].append(k2(c, trig, h))
        out["K3"][c] = k3(c)
        out["K3_ablation"] += [k3(c, delay=3), k3(c, drop_frac=0.10)]
    for c in COINS[2:]:
        for h in (28, 56):
            out["K2_all"].append(k2(c, "funding", h, n_boot=2000))
        out["K3_all"][c] = k3(c)
    json.dump(out, open("out/k123.json", "w"), indent=1, default=float)
    print("ok")
