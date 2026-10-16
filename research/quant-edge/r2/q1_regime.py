"""Q1: is low funding a regime (structural) or the market state (cyclical)? Pre-registered in 01-killkriterien-runde2.md.

Lookahead audit:
- y[t] = mean of daily funding t-29..t (annualised), regressors ret30[t] = close t / close t-30 - 1 and
  vol30[t] = std of daily returns t-29..t; all known at close t. The model is fitted on dev data only.
- Post window (2026-07+) has no history before 2026-07-01 (holdout gap); rolling windows start fresh there,
  so the first 30 days are NaN and dropped (Nachtrag N1).
- sup-F break search is in-sample by design (Q1-a), p from AR(1) bootstrap under H0.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

from r2_common import ALPHA, DAYS, DEV_END, HOLD_B, R2, candles, dropped, funding_daily, ms_index, newey_west_t

OUT = Path(__file__).resolve().parents[1] / "out"
RNG = np.random.default_rng(23)


def sup_f(y: np.ndarray, trim: float = 0.15) -> tuple[float, int]:
    n = len(y)
    ssr0 = ((y - y.mean()) ** 2).sum()
    best, kbest = -1.0, -1
    for k in range(int(trim * n), int((1 - trim) * n)):
        a, b = y[:k], y[k:]
        ssr1 = ((a - a.mean()) ** 2).sum() + ((b - b.mean()) ** 2).sum()
        f = (ssr0 - ssr1) / (ssr1 / (n - 2))
        if f > best:
            best, kbest = f, k
    return best, kbest


def q1a(coin: str, nsim: int = 5000) -> dict:
    f = funding_daily(coin)  # dev only
    m = f.groupby(f.index.tz_localize(None).to_period("M")).agg(["mean", "count"])
    m = m[m["count"] >= 25]["mean"] * DAYS * 100  # % p.a., full months only
    y = m.values
    stat, k = sup_f(y)
    e = y - y.mean()
    phi = float(np.corrcoef(e[:-1], e[1:])[0, 1])
    sd = float(np.std(e[1:] - phi * e[:-1]))
    sims = np.empty(nsim)
    for i in range(nsim):
        z = np.empty(len(y))
        z[0] = RNG.normal(0, sd / np.sqrt(max(1 - phi**2, 1e-6)))
        for j in range(1, len(y)):
            z[j] = phi * z[j - 1] + RNG.normal(0, sd)
        sims[i] = sup_f(z)[0]
    cus = np.cumsum(e) / (np.std(e, ddof=1) * np.sqrt(len(e)))
    return {
        "coin": coin, "months": len(y), "first": str(m.index[0]), "last": str(m.index[-1]),
        "supF": float(stat), "break_month": str(m.index[k]), "mean_before": float(y[:k].mean()), "mean_after": float(y[k:].mean()),
        "ar1_phi": phi, "p_ar1_bootstrap": float((sims >= stat).mean()),
        "cusum_max_abs": float(np.abs(cus).max()), "cusum_crit_5pct": 1.36,
        "monthly": {str(i): float(v) for i, v in m.items()},
    }


def features(coin: str, with_oi: bool = False) -> pd.DataFrame:
    spot = candles("spot", coin, dev_only=False)
    f = funding_daily(coin, dev_only=False)
    out = []
    for seg in (spot.index < HOLD_B, spot.index >= HOLD_B):  # rolling windows never bridge the holdout gap
        s = spot[seg]
        if s.empty:
            continue
        ff = f.reindex(s.index)
        r = s["close"].pct_change()
        d = pd.DataFrame({
            "y": ff.rolling(30).mean() * DAYS * 100,
            "ret30": s["close"] / s["close"].shift(30) - 1,
            "vol30": r.rolling(30).std() * np.sqrt(DAYS),
        })
        if with_oi:
            oi = oi_daily(coin).reindex(s.index)
            d["oi30"] = np.log(oi / oi.shift(30))
        out.append(d)
    return dropped(pd.concat(out)).replace([np.inf, -np.inf], np.nan).dropna()


def oi_daily(coin: str) -> pd.Series:
    df = pd.read_csv(R2 / f"metrics_daily_{coin}.csv", parse_dates=["date"])
    s = df.set_index(pd.DatetimeIndex(pd.to_datetime(df["date"], utc=True)))["oi_value_last"].astype(float).where(lambda x: x > 0)
    return dropped(s.sort_index())


def fit_predict(d: pd.DataFrame, cols: list[str], fit_end: pd.Timestamp, pred_start: pd.Timestamp, pred_end: pd.Timestamp | None = None) -> dict:
    tr = d[d.index <= fit_end]
    te = d[d.index >= pred_start] if pred_end is None else d[(d.index >= pred_start) & (d.index <= pred_end)]
    X = np.column_stack([np.ones(len(tr))] + [tr[c].values for c in cols])
    beta, *_ = np.linalg.lstsq(X, tr["y"].values, rcond=None)
    Xt = np.column_stack([np.ones(len(te))] + [te[c].values for c in cols])
    pred = Xt @ beta
    res = te["y"].values - pred
    t, p = newey_west_t(res, lag=30)
    r2 = 1 - ((tr["y"].values - X @ beta) ** 2).sum() / ((tr["y"] - tr["y"].mean()) ** 2).sum()
    return {
        "cols": cols, "fit": f"{tr.index[0].date()}..{tr.index[-1].date()}", "n_fit": len(tr), "r2_in": float(r2),
        "beta": dict(zip(["const"] + cols, map(float, beta))),
        "pred": f"{te.index[0].date()}..{te.index[-1].date()}", "n_pred": len(te),
        "actual_mean": float(te["y"].mean()), "pred_mean": float(pred.mean()),
        "resid_mean_pp": float(res.mean()), "nw_t": t, "p_two_sided": p, "p_one_sided_low": p / 2 if t < 0 else 1 - p / 2,
        "state_post": {c: float(te[c].mean()) for c in cols},
        "state_fit_mean": {c: float(tr[c].mean()) for c in cols},
    }


def verdict(r: dict) -> str:
    if r["resid_mean_pp"] < -3 and r["p_one_sided_low"] < ALPHA:
        return "strukturell niedriger bestätigt"
    if r["resid_mean_pp"] < -3 and r["p_one_sided_low"] < 0.05:
        return "Hinweis auf Regime"
    return "durch Marktlage erklärt / nicht unterscheidbar"


def baseline_share(coin: str) -> dict:
    df = pd.read_csv(Path("/mnt/project-files/research/quant-edge/daten") / f"funding_{coin}.csv")
    s = dropped(pd.Series(df["fundingRate"].astype(float).values, index=ms_index(df["fundingTime"])).sort_index())
    out = {}
    for y, g in s.groupby(s.index.year):
        out[str(y)] = {"at_base": float((g.round(8) == 0.0001).mean()), "below": float((g.round(8) < 0.0001).mean()),
                       "above": float((g.round(8) > 0.0001).mean()), "n": len(g)}
    return out


def usde(coin: str, d: pd.DataFrame, fitres: dict) -> dict | None:
    p = R2 / "usde_supply.csv"
    if not p.exists():
        return None
    u = pd.read_csv(p, parse_dates=["date"])
    u = dropped(u.set_index(pd.DatetimeIndex(pd.to_datetime(u["date"], utc=True)))["circulating_usd"].astype(float).sort_index())
    beta = fitres["beta"]
    pred = beta["const"] + sum(beta[c] * d[c] for c in fitres["cols"])
    res = (d["y"] - pred).rename("res")
    parts = []
    for seg in (u.index < HOLD_B, u.index >= HOLD_B):
        uu = u[seg]
        parts.append(np.log(uu / uu.shift(30)))
    g = pd.concat(parts).rename("usde30")
    j = pd.concat([res, g], axis=1).dropna()
    if len(j) < 60:
        return {"n": len(j)}
    x = (j["usde30"] - j["usde30"].mean()) / j["usde30"].std()
    yv = (j["res"] - j["res"].mean()) / j["res"].std()
    t, pval = newey_west_t((x * yv).values, lag=30)
    months = len(pd.Index(j.index.tz_localize(None).to_period("M")).unique())
    return {"n_days": len(j), "months": months, "corr": float((x * yv).mean()), "nw_t": t, "p": pval,
            "window": f"{j.index[0].date()}..{j.index[-1].date()}",
            "usde_bn_first": float(u.iloc[0] / 1e9), "usde_bn_last_dev": float(u[u.index <= DEV_END].iloc[-1] / 1e9) if (u.index <= DEV_END).any() else None,
            "usde_bn_last": float(u.iloc[-1] / 1e9), "never_confirmed_reason": "< 12 independent months" if months < 12 else None}


if __name__ == "__main__":
    out = {"alpha": ALPHA, "Q1a": {}, "Q1b": {}, "Q1b_check_2023_24": {}, "Q1c": {}, "Q1d": {}, "baseline_share": {}}
    for c in ("BTC", "ETH"):
        out["Q1a"][c] = q1a(c)
        d = features(c)
        b = fit_predict(d, ["ret30", "vol30"], DEV_END, pd.Timestamp("2026-07-31", tz="UTC"))
        b["verdict"] = verdict(b)
        out["Q1b"][c] = b
        chk = fit_predict(d, ["ret30", "vol30"], pd.Timestamp("2022-12-31", tz="UTC"), pd.Timestamp("2023-01-01", tz="UTC"), DEV_END)
        chk["verdict_if_this_were_the_test"] = verdict(chk)
        out["Q1b_check_2023_24"][c] = chk
        out["baseline_share"][c] = baseline_share(c)
        if (R2 / f"metrics_daily_{c}.csv").exists():
            doi = features(c, with_oi=True)
            cc = fit_predict(doi, ["ret30", "vol30", "oi30"], DEV_END, pd.Timestamp("2026-07-31", tz="UTC"))
            cc["verdict"] = verdict(cc)
            out["Q1c"][c] = cc
        out["Q1d"][c] = usde(c, d, b)
    OUT.mkdir(exist_ok=True)
    json.dump(out, open(OUT / "r2_q1.json", "w"), indent=1, default=float)
    for c in ("BTC", "ETH"):
        a, b, k = out["Q1a"][c], out["Q1b"][c], out["Q1b_check_2023_24"][c]
        print(c, "supF", round(a["supF"], 2), a["break_month"], round(a["mean_before"], 1), "->", round(a["mean_after"], 1), "p", a["p_ar1_bootstrap"], "phi", round(a["ar1_phi"], 2))
        print("  Q1b actual", round(b["actual_mean"], 2), "pred", round(b["pred_mean"], 2), "res", round(b["resid_mean_pp"], 2), "t", round(b["nw_t"], 2), b["verdict"], b["state_post"])
        print("  check 23-24 res", round(k["resid_mean_pp"], 2), "t", round(k["nw_t"], 2), "r2", round(k["r2_in"], 2))
