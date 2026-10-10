"""Harness for letting a model produce positions.

No LLM API is called from here. The intelligence layer is Claude subagents run inside the project:
Python writes a request batch to a file, the orchestrating session hands it to subagents, and their
answers come back as a response file that Python turns into `weights` for backtest.run.

The timing contract is the same as the backtest: on decision day t the model sees only rows up to
and including the close of t. Requests carry opaque ids in shuffled order; the id -> date key is
written to a separate file that is never shown to a subagent.
Prompts live in prompts/<id>.md and are identified by id + content hash; responses are kept so every
logged run can be replayed without running the subagents again.
"""

from __future__ import annotations

import hashlib
import json
import random
from pathlib import Path
from typing import Callable

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
PROMPTS = ROOT / "prompts"
CACHE = ROOT / "data" / "cache"


def load_prompt(prompt_id: str) -> tuple[str, str]:
    text = (PROMPTS / f"{prompt_id}.md").read_text()
    return text, hashlib.sha256(text.encode()).hexdigest()[:12]


def window(df: pd.DataFrame, t: pd.Timestamp, lookback: int, anonymize: bool = True) -> pd.DataFrame:
    """Rows up to and including t. Anonymized: no dates, prices scaled so the last close is 100.

    Anonymizing reduces, but does not remove, the chance a model recognizes a historical period.
    """
    w = df.loc[:t].tail(lookback)
    if not anonymize:
        return w
    scale = 100 / w["close"].iloc[-1]
    out = w[["open", "high", "low", "close"]] * scale
    out["volume"] = w["volume"] / w["volume"].mean()
    out.index = pd.RangeIndex(-len(w) + 1, 1, name="day")
    return out.round(4)


def cache_key(model: str, prompt_hash: str, payload: str) -> str:
    return hashlib.sha256(f"{model}\n{prompt_hash}\n{payload}".encode()).hexdigest()


class ResponseCache:
    def __init__(self, root: Path = CACHE):
        self.root = root

    def get(self, key: str) -> str | None:
        p = self.root / f"{key}.json"
        return json.loads(p.read_text())["response"] if p.exists() else None

    def put(self, key: str, response: str, meta: dict) -> None:
        self.root.mkdir(parents=True, exist_ok=True)
        (self.root / f"{key}.json").write_text(json.dumps({"response": response, **meta}, indent=1))


def decide_series(df: pd.DataFrame, decide: Callable[[pd.DataFrame], float], lookback: int = 180, freq: str = "W-SUN", anonymize: bool = True) -> pd.Series:
    """Call `decide(window)` on each rebalance day and hold the weight until the next one."""
    rebalance = rebalance_days(df, lookback, freq)
    w = pd.Series({t: float(decide(window(df, t, lookback, anonymize))) for t in rebalance})
    return w.reindex(df.index).ffill().fillna(0.0).clip(0.0, 1.0)


def rebalance_days(df: pd.DataFrame, lookback: int, freq: str = "W-SUN") -> pd.DatetimeIndex:
    days = df.index[lookback - 1 :]
    return days[days.isin(pd.date_range(days[0], days[-1], freq=freq, tz=days.tz))]


def export_requests(df: pd.DataFrame, prompt_id: str, out_dir: Path, lookback: int = 180, freq: str = "W-SUN", seed: int = 0) -> Path:
    """Write requests.json (for subagents) and key.json (id -> date, for Python only)."""
    text, phash = load_prompt(prompt_id)
    days = list(rebalance_days(df, lookback, freq))
    random.Random(seed).shuffle(days)
    ids = [hashlib.sha256(f"{seed}{t}".encode()).hexdigest()[:10] for t in days]
    out_dir.mkdir(parents=True, exist_ok=True)
    requests = [{"id": i, "window": window(df, t, lookback).to_csv()} for i, t in zip(ids, days)]
    (out_dir / "requests.json").write_text(json.dumps({"prompt_id": prompt_id, "prompt_hash": phash, "prompt": text, "requests": requests}, indent=1))
    (out_dir / "key.json").write_text(json.dumps({i: str(t) for i, t in zip(ids, days)}, indent=1))
    return out_dir


def load_responses(df: pd.DataFrame, out_dir: Path) -> pd.Series:
    """Read responses.json ({"model": ..., "responses": {id: weight}}) and map back to dates via key.json."""
    key = json.loads((out_dir / "key.json").read_text())
    resp = json.loads((out_dir / "responses.json").read_text())["responses"]
    missing = set(key) - set(resp)
    if missing:
        raise ValueError(f"{len(missing)} requests have no response")
    w = pd.Series({pd.Timestamp(key[i]): float(v) for i, v in resp.items()}).sort_index()
    return w.reindex(df.index).ffill().fillna(0.0).clip(0.0, 1.0)
