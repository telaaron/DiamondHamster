"""T-002 (T-001 plus indicators) on the T-001 window, scored with the tournament's timing value.

Jul to Oct 2026 is development data since T-001 was scored there (protocol section 11): this run
shows direction, it does not prove anything. The proof comes from the tournament once T-002 is frozen.

Usage:
  python experiments/t002_indicators.py export
  python experiments/t002_indicators.py decide
  python experiments/t002_indicators.py score
"""

import json
import sys
from pathlib import Path

import pandas as pd

from diamondhamster import ai, data, experiment, snapshot, tournament

START = "2026-07-01"
ASSETS = {"BTC": ("binance", "BTCUSDT"), "ETH": ("binance", "ETHUSDT")}
REPEATS = 3
RUNS = Path(__file__).parent / "runs"
REASON = "T-002 dev comparison on the T-001 post-cutoff window (dev data since T-001 was scored there)"


def run_dir(prompt: str, asset: str, k: int) -> Path:
    return RUNS / f"{prompt}_{asset}_r{k}"


def export() -> None:
    for asset, (src, sym) in ASSETS.items():
        df = data.load(src, sym, unlock_holdout=f"{REASON} ({asset})")
        render = snapshot.renderer(df)
        for k in range(1, REPEATS + 1):
            ai.export_requests(df, "T-002", run_dir("T-002", asset, k), lookback=180, seed=k, start=START, render=render)


def decide(model: str = "claude-opus-5-5") -> None:
    import tempfile
    from concurrent.futures import ThreadPoolExecutor

    work = Path(tempfile.mkdtemp(prefix="decider-"))
    dirs = [run_dir("T-002", a, k) for a in ASSETS for k in range(1, REPEATS + 1) if not (run_dir("T-002", a, k) / "responses.json").exists()]
    with ThreadPoolExecutor(max_workers=6) as ex:
        for d in ex.map(lambda d: ai.run_claude_cli(d, model, work), dirs):
            print("done", d.name)


def weights() -> pd.DataFrame:
    rows = []
    for prompt in ("T-001", "T-002"):
        for asset in ASSETS:
            for d in sorted(RUNS.glob(f"{prompt}_{asset}_r*")):
                if not (d / "responses.json").exists():
                    continue
                key = json.loads((d / "key.json").read_text())
                resp = json.loads((d / "responses.json").read_text())["responses"]
                rows += [{"decision": pd.Timestamp(key[i]).normalize(), "prompt": prompt, "coin": asset, "weight": min(max(float(w), 0.0), 1.0), "repeat": d.name} for i, w in resp.items()]
    df = pd.DataFrame(rows)
    df["decision"] = pd.to_datetime(df["decision"], utc=True)
    return df


def score() -> None:
    w = weights()
    closes = {a: tournament.read_candles(a)["close"] for a in ASSETS}
    avg = w.groupby(["decision", "prompt", "coin"], as_index=False)["weight"].mean()
    weekly, summary = tournament.score(avg, closes)
    pd.set_option("display.width", 160)
    print(summary.round(4).to_string())
    # per asset and per repeat, to see whether the difference holds in every repeat
    for (prompt, rep), g in w.groupby(["prompt", "repeat"]):
        _, s = tournament.score(g.drop(columns="repeat").assign(prompt=prompt), closes)
        print(rep, s[["weeks", "exposure", "timing_mean", "vs_hold_mean"]].round(4).to_dict("records"))
    for asset in ASSETS:
        _, s = tournament.score(avg[avg.coin == asset], closes)
        print(asset, s[["exposure", "timing_mean", "timing_t", "vs_hold_mean"]].round(4).to_dict("index"))
    for p, r in summary.iterrows():
        experiment.log_run(p, "binance:BTCUSDT+ETHUSDT", f"{START}..2026-10-10", {"prompt": p, "prompt_hash": ai.load_prompt(p)[1], "metric": "timing value (tournament.score)", "repeats_avg": True},
                           r.round(6).to_dict(), {"constant_at_mean_weight": 0.0}, note="dev comparison T-001 vs T-002 on Jul-Oct 2026; not evidence (dev data)", allow_dirty=True)


if __name__ == "__main__":
    {"export": export, "decide": decide, "score": score}[sys.argv[1]]()
