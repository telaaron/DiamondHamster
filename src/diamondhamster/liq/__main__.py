"""CLI: python -m diamondhamster.liq simulate|run|score (Spec 3.7)."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

from .baseline import baseline_params
from .engine import Engine
from .events import load_events
from .params import load_params
from .score import score_snapshots
from .sim import simulate, write_sim
from .snapshot import Snapshot


def _iso_to_ms(s: str) -> int:
    t = pd.Timestamp(s)
    t = t.tz_localize("UTC") if t.tzinfo is None else t.tz_convert("UTC")
    return int(t.value // 1_000_000)


def _load_snapshots(directory: Path) -> list[Snapshot]:
    out = []
    for js in sorted(directory.glob("*.json")):
        z = np.load(js.with_suffix(".npz"))
        out.append(Snapshot(data=json.loads(js.read_text()), dist={"long": z["long"], "short": z["short"]},
                            edges=z["edges"]))
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m diamondhamster.liq", description="Liquidations-Engine")
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("simulate", help="synthetischer Markt mit bekannter Wahrheit")
    s.add_argument("--seed", type=int, required=True)
    s.add_argument("--days", type=int, required=True)
    s.add_argument("--out", type=Path, required=True)
    r = sub.add_parser("run", help="Snapshots aus einem Event-Satz")
    r.add_argument("--events", type=Path, required=True)
    r.add_argument("--params", type=Path)
    r.add_argument("--model", choices=("engine", "baseline"), default="engine")
    r.add_argument("--at", action="append", default=[])
    r.add_argument("--out", type=Path, required=True)
    c = sub.add_parser("score", help="Snapshots gegen ein wahres Buch bewerten")
    c.add_argument("--events", type=Path, required=True)
    c.add_argument("--snapshots", type=Path, required=True)
    c.add_argument("--include-warmup", action="store_true")
    a = ap.parse_args(argv)

    if a.cmd == "simulate":
        write_sim(a.out, *simulate(a.seed, a.days))
        return 0
    if a.cmd == "run":
        params = load_params(a.params)
        if a.model == "baseline":
            params = baseline_params(params)
        if a.at:
            ats = [_iso_to_ms(x) for x in a.at]
        elif (a.events / "ats.json").exists():
            ats = json.loads((a.events / "ats.json").read_text())
        else:
            print("run braucht --at oder ats.json im Events-Ordner", file=sys.stderr)
            return 2
        for snap in Engine(params).run(load_events(a.events), ats):
            snap.save(a.out)
        return 0
    truth_path = a.events / "truth.csv"
    if not truth_path.exists():
        print("score braucht ein wahres Buch (truth.csv)", file=sys.stderr)
        return 2
    res = score_snapshots(_load_snapshots(a.snapshots), pd.read_csv(truth_path), load_events(a.events),
                          include_warmup=a.include_warmup)
    print(json.dumps(res, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
