"""H-004: mechanical SK-System on BTC/ETH. Test design fixed in hypotheses/H-004-sk-system.md.

Run: python experiments/h004_sk_backtest.py [--log]
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from diamondhamster import backtest, baselines, data, experiment, metrics, sk  # noqa: E402
from diamondhamster.config import COST_PER_SIDE, IN_SAMPLE_END, VALIDATION_END, VALIDATION_START  # noqa: E402

COINS = ["BTCUSDT", "ETHUSDT"]
RATIOS = [1.0, 1.2, 1.4, 1.618, 1.8, 2.0, 2.2, 2.6, 3.0]
N_BOOT = 10_000
N_RANDOM = 1000


def trades(df, k, filt, ratio=sk.TARGET_RATIO, weekly=False):
    zones = sk.kl_zones(df, k=3) if filt == "F1" else None
    out = []
    for s in sk.sequences(df, k=k, ratio=ratio):
        if filt == "F1" and not sk.in_kl(s, zones, df.index):
            continue
        if filt == "F2" and not sk.blash(s, df):
            continue
        t = sk.simulate(df, s, COST_PER_SIDE)
        if t is not None:
            out.append(t)
    return out


def boot_ci(r, rng):
    r = np.asarray(r)
    if len(r) < 2:
        return (float("nan"), float("nan"))
    means = rng.choice(r, size=(N_BOOT, len(r)), replace=True).mean(axis=1)
    return (float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5)))


def stats(ts, rng):
    r = [t.r for t in ts]
    done = [t for t in ts if t.outcome != "open"]
    hits = sum(t.outcome == "target" for t in done)
    # break-even hit rate per trade: 1 / (1 + CRV), CRV = reward / risk at entry
    be = [abs(t.seq.stop - t.entry) / (abs(t.seq.target - t.entry) + abs(t.seq.stop - t.entry)) for t in done]
    lo, hi = boot_ci(r, rng)
    return {
        "n": len(ts),
        "long": sum(t.seq.direction == 1 for t in ts),
        "mean_r": float(np.mean(r)) if r else float("nan"),
        "ci_lo": lo,
        "ci_hi": hi,
        "hit_rate": hits / len(done) if done else float("nan"),
        "breakeven_hit_rate": float(np.mean(be)) if be else float("nan"),
        "median_hold_days": float(np.median([t.exit_i - t.entry_i + 1 for t in ts])) if ts else float("nan"),
    }


def portfolio(df, ts):
    w = pd.Series(0.0, index=df.index)
    for t in ts:
        if t.seq.direction == 1:
            # weights[t] are acted on at the next open: hold from entry bar open until the exit bar
            w.iloc[t.entry_i - 1 : t.exit_i] = 1.0
    return w


def main(log: bool):
    rng = np.random.default_rng(0)
    full = {c: data.load("binance", c) for c in COINS}  # holdout cut off by the loader
    ins = {c: df[df.index <= IN_SAMPLE_END] for c, df in full.items()}
    val = {c: df[df.index <= VALIDATION_END] for c, df in full.items()}
    rows, report = [], {}

    def run(name, frames, k, filt, ratio=sk.TARGET_RATIO, weekly=False, since=None):
        ts = []
        for c, df in frames.items():
            d = sk.weekly(df) if weekly else df
            got = trades(d, k, filt, ratio)
            if since is not None:
                got = [t for t in got if d.index[t.entry_i] >= since]
            ts += [(c, t) for t in got]
        st = stats([t for _, t in ts], rng)
        rows.append({"variant": name, "k": k, "filter": filt, "ratio": ratio, "weekly": weekly, **st})
        return ts, st

    # primary
    prim, report["primary"] = run("primary", ins, 10, "F1")
    # side variants (count as tests)
    for k in (5, 20):
        run(f"k{k}", ins, k, "F1")
    for f in ("F0", "F2"):
        run(f"{f}", ins, 10, f)
    for c in COINS:
        run(f"only_{c}", {c: ins[c]}, 10, "F1")
    run("weekly_k3_F0", ins, 3, "F0", weekly=True)
    # fibonacci placebo: same rules, other target ratios
    placebo = {}
    for rho in RATIOS:
        _, st = run(f"ratio_{rho}", ins, 10, "F1", ratio=rho)
        placebo[rho] = st["mean_r"]
    others = [v for r, v in placebo.items() if r != sk.TARGET_RATIO]
    report["placebo"] = placebo
    report["placebo_median_others"] = float(np.median(others))
    # F0 placebo too (larger n)
    placebo0 = {rho: run(f"F0_ratio_{rho}", ins, 10, "F0", ratio=rho)[1]["mean_r"] for rho in RATIOS}
    report["placebo_F0"] = placebo0

    # portfolio, per coin, long only, primary rules
    port = {}
    for c in COINS:
        df = ins[c]
        ts = [t for cc, t in prim if cc == c]
        res = backtest.run(df, portfolio(df, ts))
        m = metrics.summary(res)
        bh = metrics.summary(baselines.buy_and_hold(df))
        exposure = max(m["exposure"], 0.01)
        holds = [t.exit_i - t.entry_i + 1 for t in ts if t.seq.direction == 1] or [30]
        rnd = baselines.random_timing(df, exposure=exposure, mean_hold_days=float(np.mean(holds)), n=N_RANDOM)
        port[c] = {"strategy": m, "buy_and_hold": bh, "random_sharpe_p95": float(rnd["sharpe"].quantile(0.95)),
                   "sharpe_percentile": float((rnd["sharpe"] < m["sharpe"]).mean())}
        if log:
            experiment.log_run("H-004", f"binance:{c}", f"{df.index[0].date()}..{df.index[-1].date()}",
                               {"k": 10, "filter": "F1", "ratio": 1.618, "variant": "primary-portfolio"}, m, bh,
                               note=f"random timing p95 sharpe {port[c]['random_sharpe_p95']:.3f}")
    report["portfolio"] = port

    # validation 2023-24, primary rules, history before 2023 used only for swing context
    _, report["validation"] = run("validation_2023_24", val, 10, "F1", since=VALIDATION_START)
    _, report["validation_F0"] = run("validation_2023_24_F0", val, 10, "F0", since=VALIDATION_START)

    table = pd.DataFrame(rows)
    if log:
        for r in rows:
            experiment.log_run("H-004", "binance:BTCUSDT+ETHUSDT", "2017-08-17..2022-12-31" if "validation" not in r["variant"] else "2023-01-01..2024-12-31",
                               {k: r[k] for k in ("variant", "k", "filter", "ratio", "weekly")},
                               {k: r[k] for k in ("n", "mean_r", "ci_lo", "ci_hi", "hit_rate", "breakeven_hit_rate")}, {},
                               note="trade-level stats in R after costs")
    pd.set_option("display.width", 200)
    print(table.round(3).to_string(index=False))
    print(json.dumps(report, indent=2, default=float))
    out = Path(__file__).resolve().parent / "runs" / "h004"
    out.mkdir(parents=True, exist_ok=True)
    table.to_csv(out / "variants.csv", index=False)
    (out / "report.json").write_text(json.dumps(report, indent=2, default=float) + "\n")
    pd.DataFrame([{"coin": c, "dir": t.seq.direction, "date_0": ins[c].index[t.seq.i0].date(), "date_b": ins[c].index[t.seq.ib].date(),
                   "entry_date": ins[c].index[t.entry_i].date(), "exit_date": ins[c].index[t.exit_i].date(),
                   "p0": t.seq.p0, "pa": t.seq.pa, "pb": t.seq.pb, "target": t.seq.target, "entry": t.entry,
                   "exit": t.exit, "outcome": t.outcome, "r": round(t.r, 3)} for c, t in prim]).to_csv(out / "primary_trades.csv", index=False)


if __name__ == "__main__":
    main("--log" in sys.argv)
