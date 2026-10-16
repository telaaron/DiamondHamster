"""Q2: funding dispersion across coins and exchanges. Exclusion rules R1-R5 on the 12-coin carry, and
exchange-spread carry X1 (Binance vs Bybit), X2 (Binance vs Hyperliquid). Pre-registered.

Lookahead audit:
- Rules are evaluated at the Sunday close s from data up to close s; weights apply to day returns from s+1 on
  (weekly decision forward-filled, then shift(1) so the decision day itself still earns the old weight).
- Per-coin carry nets come from round-1 `carry()` (close-to-close, funding of day t known at close t).
- Exchange funding is summed per UTC day; a day's payments are all known at its close.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from k123_funding import carry  # noqa: E402

from r2_common import ALPHA, COINS, COST, DAYS, DEV_END, HOLD_B, R2, SHARED, dropped, funding_daily, ms_index, perf  # noqa: E402

OUT = Path(__file__).resolve().parents[1] / "out"
CAP = 1.5


def payments_binance(coin: str) -> pd.Series:
    f = pd.read_csv(SHARED / "daten" / f"funding_{coin}.csv")
    return dropped(pd.Series(f["fundingRate"].astype(float).values, index=ms_index(f["fundingTime"])).sort_index())


def other_daily(ex: str, coin: str, dev_only: bool = True) -> pd.Series | None:
    p = R2 / f"{ex}_funding_{coin}.csv"
    if not p.exists():
        return None
    f = pd.read_csv(p)
    if f.empty:
        return None
    s = dropped(pd.Series(f["fundingRate"].astype(float).values, index=ms_index(f["ts"])).sort_index())
    s = s[~s.index.duplicated()]
    d = s.groupby(s.index.floor("D")).sum()
    return d[d.index <= DEV_END] if dev_only else d


def oi_daily(coin: str) -> pd.Series | None:
    p = R2 / f"metrics_daily_{coin}.csv"
    if not p.exists():
        return None
    df = pd.read_csv(p)
    s = pd.Series(df["oi_value_last"].astype(float).where(lambda x: x > 0).values, index=pd.DatetimeIndex(pd.to_datetime(df["date"], utc=True)))
    return dropped(s.sort_index())


def weekly(mask: pd.DataFrame) -> pd.DataFrame:
    """Decision at Sunday close, held for the following week, effective the next day."""
    sundays = mask.index[mask.index.dayofweek == 6]
    w = mask.loc[sundays].reindex(mask.index).ffill()
    return w.shift(1)


def portfolio(nets: pd.DataFrame, include: pd.DataFrame) -> pd.Series:
    avail = nets.notna()
    inc = include.reindex(nets.index).fillna(True).astype(bool) & avail
    n = inc.sum(axis=1).replace(0, np.nan)
    w = inc.div(n, axis=0).fillna(0.0)
    gross = (w * nets.fillna(0.0)).sum(axis=1)
    cost = w.diff().abs().sum(axis=1).fillna(0.0) * 2 * COST / CAP  # two legs per unit of weight moved
    return (gross - cost)[n.notna()]


def sharpe_diff_p(a: pd.Series, b: pd.Series, block: int = 30, n: int = 3000, seed: int = 3) -> float:
    """One-sided p that Sharpe(a) <= Sharpe(b): share of paired circular-block resamples with diff <= 0."""
    rng = np.random.default_rng(seed)
    x = pd.concat([a, b], axis=1).dropna().values
    m = len(x)
    nb = int(np.ceil(m / block))
    cnt = 0
    for _ in range(n):
        idx = ((rng.integers(0, m, nb)[:, None] + np.arange(block)[None, :]).ravel()[:m]) % m
        y = x[idx]
        sa, sb = y[:, 0].mean() / y[:, 0].std(), y[:, 1].mean() / y[:, 1].std()
        cnt += sa - sb <= 0
    return cnt / n


def rule_masks(nets: pd.DataFrame) -> dict[str, pd.DataFrame]:
    idx = nets.index
    fd = pd.DataFrame({c: funding_daily(c) for c in COINS}).reindex(idx)
    negshare = {}
    for c in COINS:
        p = payments_binance(c)
        p = p[p.index <= DEV_END + pd.Timedelta(days=1)]
        neg = (p < 0).groupby(p.index.floor("D")).sum().reindex(idx).fillna(0)
        cnt = p.groupby(p.index.floor("D")).size().reindex(idx).fillna(0)
        negshare[c] = neg.rolling(30).sum() / cnt.rolling(30).sum()
    negshare = pd.DataFrame(negshare)
    f7 = fd.rolling(7).mean()
    f30 = fd.rolling(30).mean()
    m = {}
    m["R1"] = ~(negshare > 1 / 3)
    m["R2"] = ~(f7 < 0)
    oi = pd.DataFrame({c: oi_daily(c) for c in COINS if oi_daily(c) is not None}).reindex(idx)
    if not oi.empty:
        oi7 = oi / oi.shift(7) - 1
        m["R3"] = ~((oi7.reindex(columns=COINS) > 0.30) & (f7 < 0))
    by = pd.DataFrame({c: other_daily("bybit", c) for c in COINS if other_daily("bybit", c) is not None}).reindex(idx)
    if not by.empty:
        gap = (f7 - by.reindex(columns=COINS).rolling(7).mean()).abs() * DAYS
        m["R4"] = ~(gap > 0.10)
    rank = f30.rank(axis=1, ascending=False)
    m["R5"] = rank <= 4
    return {k: weekly(v.astype(float)).fillna(1.0).astype(bool) for k, v in m.items()}


def spread_carry(other: str) -> tuple[pd.Series | None, dict]:
    legs = {}
    for c in COINS:
        b = funding_daily(c)
        o = other_daily(other, c)
        if o is None:
            continue
        j = pd.concat([b.rename("b"), o.rename("o")], axis=1).dropna()
        if len(j) < 60:
            continue
        s7 = (j["b"] - j["o"]).rolling(7).mean()
        hurdle = 4 * COST / 30  # four legs per round trip, amortised over a month, per day
        sig = np.sign(s7).where(s7.abs() > hurdle, 0.0)
        sundays = j.index[j.index.dayofweek == 6]
        pos = sig.loc[sundays].reindex(j.index).ffill().shift(1).fillna(0.0)
        inc = pos * (j["b"] - j["o"])  # short the higher-funding leg, long the lower
        cost = pos.diff().abs().fillna(pos.abs()) * 2 * COST  # two legs each switch (a flip moves 2 units)
        legs[c] = (inc - cost) / 1.0
    if not legs:
        return None, {"error": f"no {other} data"}
    df = pd.DataFrame(legs)
    pf = df.fillna(0.0).sum(axis=1) / len(COINS)  # each coin owns 1/12 of capital, idle capital earns 0
    pf = pf[df.notna().any(axis=1)]
    o = perf(pf)
    o["coins"] = list(df.columns)
    o["time_active_share"] = float((df.fillna(0) != 0).mean().mean())
    o["note"] = "upper bound: cross-exchange price basis not modelled (no second-venue prices)"
    return pf, o


def exchange_levels() -> dict:
    out = {}
    for c in COINS:
        row = {}
        for ex in ("binance", "bybit", "hl"):
            d = funding_daily(c, dev_only=False) if ex == "binance" else other_daily(ex, c, dev_only=False)
            if d is None:
                continue
            yy = {}
            for y, g in d.groupby(d.index.year):
                yy[str(y)] = float(g.mean() * DAYS)
            post = d[d.index >= HOLD_B]
            yy["2026H2"] = float(post.mean() * DAYS) if len(post) else None
            row[ex] = yy
        out[c] = row
    return out


if __name__ == "__main__":
    nets = pd.DataFrame({c: carry(c)[0] for c in COINS}).sort_index()
    nets = nets[nets.index <= DEV_END]
    bench = portfolio(nets, pd.DataFrame(True, index=nets.index, columns=COINS))
    res = {"alpha": ALPHA, "benchmark": perf(bench), "rules": {}, "X": {}, "levels": exchange_levels()}
    masks = rule_masks(nets)
    for k, inc in masks.items():
        pf = portfolio(nets, inc)
        if k == "R3":
            pf = pf[pf.index >= pd.Timestamp("2022-01-01", tz="UTC")]
        b = bench.loc[pf.index[0]:pf.index[-1]]
        pb, pr = perf(b), perf(pf)
        diff = (pf - b.reindex(pf.index)).dropna()
        excl = ~inc.reindex(pf.index)
        sol = excl.loc["2022-11-01":"2022-11-09", "SOL"].any() if "SOL" in excl else None
        episodes = {c: int(((excl[c].astype(int).diff() == 1)).sum()) for c in COINS}
        yrs = len(pf) / DAYS
        dd_better = pr["max_dd"] > pb["max_dd"] * 0.7
        cagr_ok = pr["cagr"] >= pb["cagr"] - 0.01
        p = sharpe_diff_p(pf, b.reindex(pf.index))
        verdict = "lebt" if dd_better and cagr_ok and p < ALPHA and pr["sharpe"] > pb["sharpe"] else ("Hinweis" if dd_better and cagr_ok else "tot")
        res["rules"][k] = {"rule": pr, "bench_same_window": pb, "p_block_bootstrap_sharpediff": p, "dd_30pct_better": bool(dd_better),
                            "cagr_within_1pp": bool(cagr_ok), "sol_excluded_2022_11_01_to_09": None if sol is None else bool(sol),
                            "exclusion_episodes_per_year": float(sum(episodes.values()) / yrs), "share_coin_days_excluded": float(excl.mean().mean()),
                            "verdict": verdict}
        print(k, "cagr", round(pr["cagr"] * 100, 2), "vs", round(pb["cagr"] * 100, 2), "dd", round(pr["max_dd"] * 100, 2), "vs", round(pb["max_dd"] * 100, 2),
              "sh", round(pr["sharpe"], 2), "vs", round(pb["sharpe"], 2), "p", p, "SOL", sol, verdict)
    for key, ex in (("X1", "bybit"), ("X2", "hl")):
        pf, o = spread_carry(ex)
        if pf is not None:
            o["verdict"] = "lebt (Obergrenze)" if o["cagr"] > 0.04 and o["share_neg_30d"] < 0.25 and o["max_dd"] > -0.10 else "tot"
            print(key, "cagr", round(o["cagr"] * 100, 2), "dd", round(o["max_dd"] * 100, 2), "neg30", round(o["share_neg_30d"], 3), o["start"], o["verdict"])
        res["X"][key] = o
    OUT.mkdir(exist_ok=True)
    json.dump(res, open(OUT / "r2_q2.json", "w"), indent=1, default=float)
