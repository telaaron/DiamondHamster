"""Forward prompt tournament: frozen prompts decide on many coins every Sunday, before the week happens.

Why (research/methodik review-001, B-01 to B-03): for an LLM trader only weeks after the model's
knowledge cutoff are clean, and Jul to Oct 2026 are already used for development. So evidence is
collected forward in time and in breadth:
- A prompt is frozen with id, content hash and date. It only counts on rounds after that date.
- Every round, all active prompts decide on the same coins with the same windows (paired comparison).
- Coin candles are append-only CSVs; a closed bar never changes, a re-ingest that disagrees fails.
  Exception: a volume revision of at most 0.1 % is logged and the stored value is kept.

Scoring, per prompt (weights averaged over repeats first):
- timing value: sum over coins of (w - mean_w_coin) * r - turnover cost, i.e. the prompt minus a
  constant position at its own mean exposure on that coin. Per-coin means keep static coin
  preferences (selection) out of the timing number.
- rank IC: Spearman correlation between weight and next-week return across coins (selection skill).
Both are averaged per week first and the t-statistic uses weeks as the unit, because coins move
together and are not independent observations.

Returns are close(D) -> close(D+7). Under the backtest contract the position starts at open(D+1);
on 24/7 crypto markets that open equals close(D) up to rounding.
"""

from __future__ import annotations

import hashlib
import json
import random
from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd

from . import ai, features, snapshot
from .config import COST_PER_SIDE

ROOT = Path(__file__).resolve().parents[2]
HOME = ROOT / "tournament"
CANDLES = HOME / "candles"
ROUNDS = HOME / "rounds"
REGISTRY = HOME / "prompts.json"
UNIVERSE = HOME / "universe.json"

LOOKBACK = 180
REPEATS = 3
MAX_ACTIVE = 4
OPEN_GAP_TOLERANCE = 0.005  # open(t) vs close(t-1); larger gaps mean a copy error, not the market
PRICE_TOLERANCE = 1e-6
VOLUME_REVISION_TOLERANCE = 1e-3  # TradingView revises Binance volume of closed bars by up to ~0.05 %; prices never
VOLUME_REVISIONS = HOME / "volume_revisions.csv"


# ---------- candles ----------

def parse_tradingview(payload: dict) -> pd.DataFrame:
    """Bars from a TradingView get_ohlcv response, rows or columns layout."""
    bars = payload["bars"]
    if isinstance(bars, dict):
        df = pd.DataFrame({k: bars[k] for k in ("t", "o", "h", "l", "c", "v")})
    else:
        df = pd.DataFrame(bars)[["t", "o", "h", "l", "c", "v"]]
    df.index = pd.DatetimeIndex(pd.to_datetime(df.pop("t"), unit="s", utc=True), name="date").normalize()
    return df.rename(columns={"o": "open", "h": "high", "l": "low", "c": "close", "v": "volume"}).astype(float).sort_index()


def check_bars(df: pd.DataFrame, summary: dict | None = None) -> list[str]:
    """Problems that point to a broken or mis-copied series. Empty list means clean."""
    errors = []
    if df.index.duplicated().any():
        errors.append("duplicate dates")
    gaps = df.index.to_series().diff().dropna()
    if (gaps != pd.Timedelta(days=1)).any():
        errors.append(f"missing days after {list(gaps[gaps != pd.Timedelta(days=1)].index.date)[:3]}")
    if (df["high"] < df[["open", "close"]].max(axis=1) - PRICE_TOLERANCE).any() or (df["low"] > df[["open", "close"]].min(axis=1) + PRICE_TOLERANCE).any():
        errors.append("high/low outside open/close")
    # Feeds round prices to a tick; for coins priced like 0.000001 one tick is about 1 %.
    prices = np.unique(df[["open", "high", "low", "close"]].values.ravel())
    tick = np.diff(prices).min() if len(prices) > 1 else 0.0
    gap = (df["open"] - df["close"].shift(1)).abs().iloc[1:]
    bad = gap > np.maximum(OPEN_GAP_TOLERANCE * df["close"].shift(1).iloc[1:], 1.5 * tick)
    if bad.any():
        errors.append(f"open differs from previous close on {list(gap[bad].index.date)[:3]}")
    if summary:
        expect = {"high": df["high"].max(), "low": df["low"].min(), "last_close": df["close"].iloc[-1], "first_open": df["open"].iloc[0]}
        for k, v in expect.items():
            if k in summary and not np.isclose(summary[k], v, rtol=1e-9):
                errors.append(f"summary {k} {summary[k]} != bars {v}")
        if "total_volume" in summary and not np.isclose(summary["total_volume"], df["volume"].sum(), rtol=1e-6):
            errors.append("summary total_volume != bars")
    return errors


def ingest(coin: str, payload: dict, today: date, root: Path = CANDLES, last: int | None = None) -> int:
    """Append closed bars for a coin. Bars dated today or later are still forming and are dropped.

    Fails if the payload is inconsistent or disagrees with bars already stored. Returns new bar count.
    """
    new = parse_tradingview(payload)
    if last is not None and len(new) > last:  # old history can have exchange outages; only recent bars are needed
        new = new.iloc[-last:]
        payload = {k: v for k, v in payload.items() if k != "summary"}
    errors = check_bars(new, payload.get("summary"))
    if errors:
        raise ValueError(f"{coin}: {'; '.join(errors)}")
    new = new[new.index < pd.Timestamp(today, tz="UTC")]
    path = root / f"{coin}.csv"
    old = read_candles(coin, root) if path.exists() else new.iloc[:0]
    both = old.index.intersection(new.index)
    prices = ["open", "high", "low", "close"]
    changed = ~np.isclose(old.loc[both, prices].values, new.loc[both, prices].values, rtol=1e-9).all(axis=1)
    if changed.any():
        raise ValueError(f"{coin}: stored prices changed on {list(both[changed].date)[:3]}")
    vol_old, vol_new = old.loc[both, "volume"], new.loc[both, "volume"]
    rel = ((vol_new - vol_old) / vol_old.where(vol_old != 0)).fillna(0.0)
    revised = ~np.isclose(vol_old.values, vol_new.values, rtol=1e-9)
    if (abs(rel[revised]) > VOLUME_REVISION_TOLERANCE).any():
        big = rel[revised][abs(rel[revised]) > VOLUME_REVISION_TOLERANCE]
        raise ValueError(f"{coin}: stored volume changed by more than {VOLUME_REVISION_TOLERANCE:.1%} on {list(big.index.date)[:3]}")
    if revised.any():  # stored bars are kept; the revision is only logged
        log = root.parent / VOLUME_REVISIONS.name
        rows = pd.DataFrame({"ingested": today.isoformat(), "coin": coin, "date": [d.date().isoformat() for d in both[revised]],
                             "stored": vol_old[revised].values, "new": vol_new[revised].values, "rel": rel[revised].values})
        rows.to_csv(log, mode="a", header=not log.exists(), index=False, float_format="%.10g")
    merged = pd.concat([old, new[~new.index.isin(old.index)]]).sort_index()
    errors = check_bars(merged)
    if errors:
        raise ValueError(f"{coin} after merge: {'; '.join(errors)}")
    root.mkdir(parents=True, exist_ok=True)
    merged.to_csv(path, float_format="%.10g")
    return len(merged) - len(old)


def read_candles(coin: str, root: Path = CANDLES) -> pd.DataFrame:
    df = pd.read_csv(root / f"{coin}.csv", index_col="date", parse_dates=["date"])
    df.index = pd.to_datetime(df.index, utc=True)
    return df


# ---------- prompts ----------

def registry(path: Path = REGISTRY) -> dict:
    return json.loads(path.read_text()) if path.exists() else {}


def freeze(prompt_id: str, on: date, path: Path = REGISTRY, input: str = "candles") -> dict:
    """Enter a prompt into the tournament. Its text may never change afterwards.

    input: "candles" (window only) or "indicators" (snapshot.snapshot line, then the window).
    """
    if input not in ("candles", "indicators"):
        raise ValueError(input)
    reg = registry(path)
    _, phash = ai.load_prompt(prompt_id)
    if prompt_id in reg:
        raise ValueError(f"{prompt_id} is already frozen ({reg[prompt_id]['frozen_at']})")
    active = [p for p, e in reg.items() if not e.get("retired_at")]
    if len(active) >= MAX_ACTIVE:
        raise ValueError(f"already {len(active)} active prompts ({', '.join(active)}); retire one first")
    reg[prompt_id] = {"hash": phash, "frozen_at": on.isoformat(), "input": input}
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(reg, indent=1, sort_keys=True) + "\n")
    return reg[prompt_id]


def active_prompts(decision: date, path: Path = REGISTRY) -> list[str]:
    """Prompts frozen on or before the decision day, not retired, with unchanged text."""
    out = []
    for p, e in sorted(registry(path).items()):
        if date.fromisoformat(e["frozen_at"]) > decision or (e.get("retired_at") and date.fromisoformat(e["retired_at"]) <= decision):
            continue
        if ai.load_prompt(p)[1] != e["hash"]:
            raise ValueError(f"{p} changed after freezing; give the new text a new id")
        out.append(p)
    return out


# ---------- rounds ----------

def round_dir(decision: date, prompt_id: str, k: int, root: Path = ROUNDS) -> Path:
    return root / decision.isoformat() / f"{prompt_id}_r{k}"


def export_round(decision: date, coins: list[str], repeats: int = REPEATS, candles: Path = CANDLES, rounds: Path = ROUNDS, registry_path: Path = REGISTRY) -> list[Path]:
    """Write one request batch per active prompt and repeat. Windows end at the decision day's close."""
    if decision.weekday() != 6:
        raise ValueError("decisions are taken at the Sunday close")
    t = pd.Timestamp(decision, tz="UTC")
    windows, snapshots, skipped = {}, {}, {}
    for c in coins:
        df = read_candles(c, candles)
        if t not in df.index:
            skipped[c] = f"no bar for {decision} (last {df.index[-1].date()})"
        elif len(df.loc[:t]) < LOOKBACK:
            skipped[c] = f"only {len(df.loc[:t])} bars"
        else:
            windows[c] = ai.compact(ai.window(df, t, LOOKBACK))
            snapshots[c] = snapshot.snapshot(features.compute(df.loc[:t]), t)
    if not windows:
        raise ValueError(f"no coin has data for {decision}: {skipped}")
    out = []
    reg = registry(registry_path)
    for p in active_prompts(decision, registry_path):
        text, phash = ai.load_prompt(p)
        with_indicators = reg[p].get("input", "candles") == "indicators"
        for k in range(1, repeats + 1):
            d = round_dir(decision, p, k, rounds)
            if (d / "requests.json").exists():
                out.append(d)
                continue
            seed = f"{decision}{p}{k}"
            order = sorted(windows)
            random.Random(seed).shuffle(order)
            ids = {c: hashlib.sha256(f"{seed}{c}".encode()).hexdigest()[:10] for c in order}
            d.mkdir(parents=True, exist_ok=True)
            reqs = [{"id": ids[c], "window": (snapshots[c] + "\n" if with_indicators else "") + windows[c]} for c in order]
            (d / "requests.json").write_text(json.dumps({"prompt_id": p, "prompt_hash": phash, "prompt": text, "requests": reqs}, indent=1))
            (d / "key.json").write_text(json.dumps({ids[c]: c for c in order}, indent=1))
            out.append(d)
    (rounds / decision.isoformat()).mkdir(parents=True, exist_ok=True)
    (rounds / decision.isoformat() / "round.json").write_text(json.dumps({"decision": decision.isoformat(), "coins": sorted(windows), "skipped": skipped, "lookback": LOOKBACK}, indent=1))
    return out


def decide_round(decision: date, model: str, rounds: Path = ROUNDS, workers: int = 4) -> list[Path]:
    """Answer every unanswered batch of a round with a fresh tool-less Claude run (see ai.run_claude_cli)."""
    import tempfile
    from concurrent.futures import ThreadPoolExecutor

    work = Path(tempfile.mkdtemp(prefix="decider-"))
    dirs = sorted(d for d in (rounds / decision.isoformat()).iterdir() if d.is_dir() and not (d / "responses.json").exists())
    with ThreadPoolExecutor(max_workers=workers) as ex:
        return list(ex.map(lambda d: ai.run_claude_cli(d, model, work), dirs))


def round_weights(rounds: Path = ROUNDS) -> pd.DataFrame:
    """All answered decisions: one row per (decision, prompt, coin), weight averaged over repeats."""
    rows = []
    for d in sorted(rounds.glob("*/*_r*")):
        if not (d / "responses.json").exists():
            continue
        key = json.loads((d / "key.json").read_text())
        resp = json.loads((d / "responses.json").read_text())["responses"]
        prompt = d.name.rsplit("_r", 1)[0]
        for i, coin in key.items():
            if i in resp:
                rows.append({"decision": pd.Timestamp(d.parent.name, tz="UTC"), "prompt": prompt, "coin": coin, "weight": min(max(float(resp[i]), 0.0), 1.0)})
    if not rows:
        return pd.DataFrame(columns=["decision", "prompt", "coin", "weight"])
    return pd.DataFrame(rows).groupby(["decision", "prompt", "coin"], as_index=False)["weight"].mean()


def forward_returns(decisions: pd.DataFrame, closes: dict[str, pd.Series], horizon: int = 7) -> pd.Series:
    """close(D+horizon)/close(D) - 1 per row; NaN while the week is not over."""
    def r(row):
        s = closes.get(row.coin)
        end = row.decision + pd.Timedelta(days=horizon)
        if s is None or row.decision not in s.index or end not in s.index:
            return np.nan
        return s[end] / s[row.decision] - 1
    return decisions.apply(r, axis=1) if len(decisions) else pd.Series(dtype=float)


def score(weights: pd.DataFrame, closes: dict[str, pd.Series], cost_per_side: float = COST_PER_SIDE) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Per (prompt, week) contributions and per-prompt summary. Only finished weeks are scored."""
    w = weights.copy()
    w["ret"] = forward_returns(w, closes)
    w = w.dropna(subset=["ret"]).sort_values(["prompt", "coin", "decision"])
    if w.empty:
        return pd.DataFrame(), pd.DataFrame()
    w["mean_w"] = w.groupby(["prompt", "coin"])["weight"].transform("mean")
    w["turnover"] = w.groupby(["prompt", "coin"])["weight"].diff().abs().fillna(0.0)
    w["timing"] = (w["weight"] - w["mean_w"]) * w["ret"] - w["turnover"] * cost_per_side
    w["vs_hold"] = (w["weight"] - 1.0) * w["ret"] - w["turnover"] * cost_per_side

    def week(g):
        ic = g["weight"].rank().corr(g["ret"].rank()) if g["weight"].nunique() > 1 and len(g) > 2 else np.nan
        return pd.Series({"coins": len(g), "exposure": g["weight"].mean(), "timing": g["timing"].mean(), "vs_hold": g["vs_hold"].mean(), "rank_ic": ic})

    weekly = w.groupby(["prompt", "decision"]).apply(week, include_groups=False).reset_index()

    def tstat(x):
        x = x.dropna()
        return x.mean() / (x.std(ddof=1) / np.sqrt(len(x))) if len(x) > 1 and x.std(ddof=1) > 0 else np.nan

    summary = weekly.groupby("prompt").agg(
        weeks=("decision", "nunique"), decisions=("coins", "sum"), exposure=("exposure", "mean"),
        timing_mean=("timing", "mean"), timing_t=("timing", tstat),
        rank_ic_mean=("rank_ic", "mean"), rank_ic_t=("rank_ic", tstat), vs_hold_mean=("vs_hold", "mean"),
    )
    return weekly, summary


def score_all(rounds: Path = ROUNDS, candles: Path = CANDLES) -> tuple[pd.DataFrame, pd.DataFrame]:
    weights = round_weights(rounds)
    closes = {c: read_candles(c, candles)["close"] for c in weights["coin"].unique()} if len(weights) else {}
    return score(weights, closes)


def coin_of(symbol: str) -> str:
    """'BINANCE:SOLUSDT' -> 'SOL'."""
    return symbol.split(":")[-1].removesuffix("USDT")


def universe(path: Path = UNIVERSE) -> list[str]:
    return json.loads(path.read_text())["coins"]


if __name__ == "__main__":
    import argparse

    p = argparse.ArgumentParser(prog="python -m diamondhamster.tournament")
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("ingest", help="append TradingView get_ohlcv JSON responses (saved tool results); coin from the symbol field, else the file name")
    s.add_argument("files", nargs="+", type=Path)
    s.add_argument("--today", type=date.fromisoformat, default=date.today())
    s.add_argument("--last", type=int, default=None, help="keep only the newest N bars of each response")
    s = sub.add_parser("freeze")
    s.add_argument("prompt_id")
    s.add_argument("--on", type=date.fromisoformat, default=date.today())
    s.add_argument("--input", choices=["candles", "indicators"], default="candles")
    for name in ("export", "decide"):
        s = sub.add_parser(name)
        s.add_argument("decision", type=date.fromisoformat)
        s.add_argument("--model", default="claude-opus-5-5")
    sub.add_parser("score")
    a = p.parse_args()
    if a.cmd == "ingest":
        for f in a.files:
            payload = json.loads(f.read_text())
            coin = coin_of(payload.get("symbol", "")) or f.stem
            print(coin, ingest(coin, payload, a.today, last=a.last), "new bars")
    elif a.cmd == "freeze":
        print(a.prompt_id, freeze(a.prompt_id, a.on, input=a.input))
    elif a.cmd == "export":
        for d in export_round(a.decision, universe()):
            print(d)
    elif a.cmd == "decide":
        for d in decide_round(a.decision, a.model):
            print("done", d.name)
    else:
        weekly, summary = score_all()
        pd.set_option("display.width", 160)
        print(summary.round(4).to_string() if len(summary) else "no finished week yet")
        if len(weekly):
            HOME.mkdir(exist_ok=True)
            weekly.to_csv(HOME / "scores_weekly.csv", index=False, float_format="%.6f")
