"""Provider-agnostic harness for letting a model produce positions.

The model is just another source of `weights` for backtest.run, so the timing contract is the same:
on decision day t it sees only rows up to and including the close of t.
Prompts live in prompts/<id>.md and are identified by id + content hash; responses are cached
by (model, prompt hash, input) so every logged run can be replayed without new API calls.
"""

from __future__ import annotations

import hashlib
import json
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
    days = df.index[lookback - 1 :]
    rebalance = days[days.isin(pd.date_range(days[0], days[-1], freq=freq, tz=days.tz))]
    w = pd.Series({t: float(decide(window(df, t, lookback, anonymize))) for t in rebalance})
    return w.reindex(df.index).ffill().fillna(0.0).clip(0.0, 1.0)
