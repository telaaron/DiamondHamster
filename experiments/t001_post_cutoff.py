"""T-001 on the post-cutoff window (2026-07 onward): export request batches, later score the responses.

Usage:
  python experiments/t001_post_cutoff.py export   # writes experiments/runs/T-001_<asset>_r<k>/requests.json + key.json
  python experiments/t001_post_cutoff.py decide   # answers every batch with a tool-less headless Claude run (parallel)
  python experiments/t001_post_cutoff.py score    # reads responses.json in each run dir, prints and logs results
"""

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

from diamondhamster import ai, backtest, baselines, data, experiment, metrics

START = "2026-07-01"
ASSETS = {"BTC": ("binance", "BTCUSDT"), "ETH": ("binance", "ETHUSDT")}
REPEATS = 5
RUNS = Path(__file__).parent / "runs"
REASON = "T-001 post-cutoff evaluation: model knowledge ends ~2026-06, so 2026-07+ is the only clean window for an LLM trader"


def run_dir(asset: str, k: int) -> Path:
    return RUNS / f"T-001_{asset}_r{k}"


def export() -> None:
    for asset, (src, sym) in ASSETS.items():
        df = data.load(src, sym, unlock_holdout=f"{REASON} ({asset})")
        for k in range(1, REPEATS + 1):
            ai.export_requests(df, "T-001", run_dir(asset, k), lookback=180, seed=k, start=START)
            n = len(json.loads((run_dir(asset, k) / "key.json").read_text()))
            print(asset, k, n, "requests")


def decide(model: str = "claude-opus-5-5") -> None:
    from concurrent.futures import ThreadPoolExecutor
    import tempfile

    work = Path(tempfile.mkdtemp(prefix="decider-"))  # neutral cwd: no repo, no CLAUDE.md
    dirs = [run_dir(a, k) for a in ASSETS for k in range(1, REPEATS + 1) if not (run_dir(a, k) / "responses.json").exists()]
    with ThreadPoolExecutor(max_workers=5) as ex:
        for d in ex.map(lambda d: ai.run_claude_cli(d, model, work), dirs):
            print("done", d.name)


def score() -> None:
    for asset, (src, sym) in ASSETS.items():
        df = data.load(src, sym, unlock_holdout=f"{REASON} ({asset}, scoring)")
        period = df.loc[START:]
        bh = metrics.summary(backtest.run(period, pd.Series(1.0, index=period.index)))
        rows = []
        for k in range(1, REPEATS + 1):
            d = run_dir(asset, k)
            if not (d / "responses.json").exists():
                continue
            w = ai.load_responses(df, d).loc[START:]
            res = backtest.run(period, w)
            m = metrics.summary(res)
            m["mean_weight"] = float(w.mean())
            rows.append(m)
            model = json.loads((d / "responses.json").read_text()).get("model", "unknown")
            experiment.log_run("T-001", f"{src}:{sym}", f"{START}..{period.index[-1].date()}",
                               {"prompt": "T-001", "prompt_hash": ai.load_prompt("T-001")[1], "model": model, "repeat": k, "lookback": 180, "freq": "W-SUN"},
                               m, bh, note="first end-to-end trader run; post-cutoff window", allow_dirty=True)
        if not rows:
            continue
        runs = pd.DataFrame(rows)
        exp = float(runs["mean_weight"].mean())
        rnd = baselines.random_timing(period, exposure=max(min(exp, 0.95), 0.05), mean_hold_days=14, n=1000)
        print(f"\n== {asset} {START} .. {period.index[-1].date()} ({len(period)} days)")
        print("buy&hold:", {k: round(v, 4) for k, v in bh.items() if k in ("total_return", "max_drawdown", "sharpe")})
        print("T-001 runs:")
        print(runs[["total_return", "max_drawdown", "sharpe", "mean_weight", "entries"]].round(4).to_string())
        pct = float((rnd["total_return"] < runs["total_return"].mean()).mean())
        print(f"random timing at same exposure ({exp:.2f}): median total_return {rnd['total_return'].median():.4f}; T-001 mean beats {pct:.0%} of random runs")


if __name__ == "__main__":
    {"export": export, "decide": decide, "score": score}[sys.argv[1]]()
