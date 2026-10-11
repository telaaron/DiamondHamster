"""H-002: do price turns cluster on QS hit days? Test design fixed in hypotheses/H-002-qs-zyklen.md.

Run: python experiments/h002_qs_backtest.py [--log]
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from diamondhamster import backtest, baselines, data, experiment, metrics, qs  # noqa: E402

START = pd.Timestamp("2011-11-17", tz="UTC")
END = pd.Timestamp("2024-12-31", tz="UTC")  # holdout starts 2025-01-01 and stays closed
VALIDATION_START = pd.Timestamp("2023-01-01", tz="UTC")
DATASET = "tradingview:INDEX-BTCUSD"
N_RANDOM_FILTERS = 2000


def rsi(close: pd.Series, n: int = 14) -> pd.Series:
    d = close.diff()
    up = d.clip(lower=0).ewm(alpha=1 / n, adjust=False).mean()
    dn = (-d.clip(upper=0)).ewm(alpha=1 / n, adjust=False).mean()
    return 100 - 100 / (1 + up / dn)


def swings(s: pd.Series, k: int, kind: str) -> pd.Series:
    """Centered swing points: the extreme of [t-k, t+k]. Uses future bars on purpose (event study, not a signal)."""
    roll = s.rolling(2 * k + 1, center=True)
    ext = roll.max() if kind == "high" else roll.min()
    full = roll.count() == 2 * k + 1
    return (s == ext) & full


def events(df: pd.DataFrame) -> dict[str, pd.Series]:
    r = rsi(df["close"])
    hi = lambda k: swings(df["high"], k, "high")
    lo = lambda k: swings(df["low"], k, "low")
    return {
        "E1_swing14": hi(14) | lo(14),
        "E2_swing7": hi(7) | lo(7),
        "E3_swing30": hi(30) | lo(30),
        "E4_low14": lo(14),
        "E5_high14": hi(14),
        "E6_rsi14": swings(r, 14, "high") | swings(r, 14, "low"),
    }


def per_qs_counts(ev: pd.Series, cal: pd.DataFrame) -> dict[int, np.ndarray]:
    """counts[cycle][q] = number of events in that cycle with QS q (anchor day excluded)."""
    out = {}
    for c in qs.CLASSES:
        m = (cal["cycle"] == c) & (cal["days"] > 0) & ev
        out[c] = np.bincount(cal.loc[m, "qs"].astype(int).to_numpy(), minlength=10)
    return out


def class_pair_null(counts: dict[int, np.ndarray]) -> np.ndarray:
    """Exact distribution of total hits over all 36^4 class-pair combinations (one pair per cycle)."""
    dist = np.array([1.0])
    for c in sorted(counts):
        vals = np.array([counts[c][a] + counts[c][b] for a, b in qs.PAIRS])
        pmf = np.bincount(vals) / len(vals)
        dist = np.convolve(dist, pmf)
    return dist


def event_study(name: str, ev: pd.Series, cal: pd.DataFrame, hit: pd.Series) -> dict:
    valid = (cal["cycle"] > 0) & (cal["days"] > 0)
    ev = ev & valid
    counts = per_qs_counts(ev, cal)
    obs = int((ev & hit).sum())
    n = int(ev.sum())
    dist = class_pair_null(counts)
    p = float(dist[obs:].sum())
    base = float(hit[valid].mean())
    ranks = {}
    for c, (a, b) in qs.CLASSES.items():
        vals = sorted((counts[c][x] + counts[c][y] for x, y in qs.PAIRS), reverse=True)
        mine = counts[c][a] + counts[c][b]
        ranks[c] = 1 + sum(v > mine for v in vals)  # 1 = best of 36 (ties share the better rank)
    return {
        "events": n, "on_hit_days": obs, "hit_share": obs / n if n else float("nan"), "base_rate": base,
        "lift": (obs / n) / base if n else float("nan"), "p_class_pairs": p,
        "null_mean": float((np.arange(len(dist)) * dist).sum()), "rank_of_36": ranks,
    }


def signal_weights(sig: pd.Series, hold: int = 30) -> pd.Series:
    """1.0 for `hold` days after each signal day (signal at close t; backtest enters at open t+1)."""
    w = sig.astype(float).rolling(hold, min_periods=1).max()
    return w.fillna(0.0)


def trading_check(df: pd.DataFrame, cal: pd.DataFrame, hit: pd.Series, rng: np.random.Generator) -> dict:
    sig = (df["close"] == df["close"].rolling(14).min()) & (cal["cycle"] > 0)
    res_plain = metrics.summary(backtest.run(df, signal_weights(sig)))
    res_qs = metrics.summary(backtest.run(df, signal_weights(sig & hit)))
    rand = []
    for _ in range(N_RANDOM_FILTERS):
        classes = {c: qs.PAIRS[rng.integers(36)] for c in qs.CLASSES}
        rand.append(metrics.summary(backtest.run(df, signal_weights(sig & qs.hits(cal, classes))))["sharpe"])
    rand = np.array(rand)
    bh = metrics.summary(baselines.buy_and_hold(df))
    return {
        "qs_filtered": res_qs, "unfiltered": res_plain, "buy_and_hold": bh, "dca": baselines.dca(df),
        "random_filter_sharpe_p95": float(np.percentile(rand, 95)),
        "random_filter_sharpe_median": float(np.median(rand)),
        "qs_sharpe_percentile": float((rand < res_qs["sharpe"]).mean()),
    }


def main(log: bool) -> dict:
    df = data.load("tradingview", "INDEX-BTCUSD")  # holdout cut off by the loader
    df = df.loc[START - pd.Timedelta(days=60) : END]
    cal = qs.calendar(df.index)
    hit = qs.hits(cal)
    evs = events(df)
    keep = df.index >= START
    out = {"study": {}, "validation_2023_24": {}}
    for name, ev in evs.items():
        out["study"][name] = event_study(name, ev[keep], cal[keep], hit[keep])
    val = df.index >= VALIDATION_START
    e1 = evs["E1_swing14"]
    out["validation_2023_24"] = {
        "events": int(e1[val].sum()), "on_hit_days": int((e1 & hit)[val].sum()),
        "base_rate": float(hit[val].mean()),
    }
    out["trading"] = trading_check(df[keep], cal[keep], hit[keep], np.random.default_rng(2))
    if log:
        period = f"{START.date()}..{END.date()}"
        for name, r in out["study"].items():
            experiment.log_run("H-002", DATASET, period, {"event": name, "test": "class_pair_null_36^4"},
                               {k: v for k, v in r.items() if k != "rank_of_36"},
                               {"null_mean": r["null_mean"]}, note=f"ranks {r['rank_of_36']}")
        t = out["trading"]
        experiment.log_run("H-002", DATASET, period, {"rule": "close=14d low, hold 30d, QS filter", "cost_per_side": 0.002},
                           t["qs_filtered"], t["unfiltered"],
                           note=f"random filter p95 sharpe {t['random_filter_sharpe_p95']:.3f}; qs percentile {t['qs_sharpe_percentile']:.3f}")
    return out


if __name__ == "__main__":
    print(json.dumps(main("--log" in sys.argv), indent=1, default=float))
