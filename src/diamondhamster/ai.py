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


def compact(w: pd.DataFrame) -> str:
    """One line per day, 'day o h l c v', 1 decimal for prices, 2 for relative volume (keeps batches small)."""
    lines = [f"{d} {r.open:.1f} {r.high:.1f} {r.low:.1f} {r.close:.1f} {r.volume:.2f}" for d, r in w.iterrows()]
    return "day o h l c v\n" + "\n".join(lines)


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


def rebalance_days(df: pd.DataFrame, lookback: int, freq: str = "W-SUN", start: str | None = None) -> pd.DatetimeIndex:
    days = df.index[lookback - 1 :]
    days = days[days.isin(pd.date_range(days[0], days[-1], freq=freq, tz=days.tz))]
    return days[days >= pd.Timestamp(start, tz="UTC")] if start else days


def export_requests(df: pd.DataFrame, prompt_id: str, out_dir: Path, lookback: int = 180, freq: str = "W-SUN", seed: int = 0, start: str | None = None,
                    render: Callable[[pd.DataFrame, pd.Timestamp], str] | None = None) -> Path:
    """Write requests.json (for subagents) and key.json (id -> date, for Python only).

    `render(df, t)` builds the text for one decision day; default is the compact candle window.
    """
    render = render or (lambda d, t: compact(window(d, t, lookback)))
    text, phash = load_prompt(prompt_id)
    days = list(rebalance_days(df, lookback, freq, start))
    random.Random(seed).shuffle(days)
    ids = [hashlib.sha256(f"{seed}{t}".encode()).hexdigest()[:10] for t in days]
    out_dir.mkdir(parents=True, exist_ok=True)
    requests = [{"id": i, "window": render(df, t)} for i, t in zip(ids, days)]
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


def build_prompt(out_dir: Path) -> str:
    r = json.loads((out_dir / "requests.json").read_text())
    return r["prompt"] + "\n\n# Windows\n\n" + "\n\n".join(f"## {q['id']}\n{q['window']}" for q in r["requests"])


def parse_weights(text: str) -> dict[str, float]:
    """Take the JSON object a model answer ends with and return {id: weight}.

    Values may be plain numbers or objects with a "weight" (and e.g. a "flip" price)."""
    dec = json.JSONDecoder()
    for must_end in (True, False):  # prefer the object the answer ends with; else the last one that parses
        start = text.rfind("{")
        while start >= 0:
            try:
                obj, end = dec.raw_decode(text[start:])
                if isinstance(obj, dict) and obj and (not must_end or text[start + end:].strip().strip("`").strip() == ""):
                    return {k: float(v["weight"] if isinstance(v, dict) else v) for k, v in obj.items()}
            except (json.JSONDecodeError, KeyError, TypeError, ValueError):
                pass
            start = text.rfind("{", 0, start)
    raise ValueError("no JSON object with weights found")


def run_claude_cli(out_dir: Path, model: str, workdir: Path) -> Path:
    """Answer a request batch with a fresh headless Claude Code run: no tools, no MCP, no memory, neutral cwd.

    This is the project's own Claude (no separate LLM API key). The full answer is stored next to the
    parsed weights so a run can be audited and replayed.
    """
    import os
    import subprocess

    env = {**os.environ, "CLAUDE_CODE_DISABLE_AUTO_MEMORY": "1"}
    cmd = ["claude", "-p", "--tools", "", "--strict-mcp-config", "--settings", '{"autoMemoryEnabled":false}', "--model", model, "--output-format", "json"]
    proc = subprocess.run(cmd, input=build_prompt(out_dir), capture_output=True, text=True, cwd=workdir, env=env, timeout=1800)
    out = json.loads(proc.stdout)
    if out.get("is_error"):
        raise RuntimeError(out.get("result"))
    weights = parse_weights(out["result"])
    served = [m for m in out.get("modelUsage", {}) if "haiku" not in m] or [model]
    (out_dir / "responses.json").write_text(json.dumps({"model": served[0], "responses": weights, "raw": out["result"], "cost_usd": out.get("total_cost_usd")}, indent=1))
    return out_dir
