"""Append-only experiment log. Every run is recorded, including the ones that fail."""

from __future__ import annotations

import csv
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LOG = ROOT / "experiments" / "log.csv"
FIELDS = ["timestamp", "hypothesis", "commit", "dataset", "period", "params", "metrics", "baseline", "note"]


def _commit(allow_dirty: bool) -> str:
    sha = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    dirty = subprocess.run(["git", "status", "--porcelain", "--", "src"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    if dirty and not allow_dirty:
        raise RuntimeError("uncommitted changes in src/: commit first so the run is reproducible")
    return sha + ("-dirty" if dirty else "")


def log_run(hypothesis: str, dataset: str, period: str, params: dict, metrics: dict, baseline: dict, note: str = "", allow_dirty: bool = False) -> None:
    new = not LOG.exists()
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        if new:
            w.writeheader()
        w.writerow({
            "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "hypothesis": hypothesis,
            "commit": _commit(allow_dirty),
            "dataset": dataset,
            "period": period,
            "params": json.dumps(params, sort_keys=True),
            "metrics": json.dumps({k: round(v, 4) if isinstance(v, float) else v for k, v in metrics.items()}),
            "baseline": json.dumps({k: round(v, 4) if isinstance(v, float) else v for k, v in baseline.items()}),
            "note": note,
        })


def count(hypothesis: str | None = None) -> int:
    """Number of logged trials; needed for multiple-testing corrections."""
    if not LOG.exists():
        return 0
    with LOG.open() as f:
        return sum(1 for r in csv.DictReader(f) if hypothesis is None or r["hypothesis"] == hypothesis)
