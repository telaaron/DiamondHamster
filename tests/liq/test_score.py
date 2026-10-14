import os
from concurrent.futures import ProcessPoolExecutor

import numpy as np
import pandas as pd
import pytest

from diamondhamster.liq.baseline import baseline_params
from diamondhamster.liq.engine import Engine
from diamondhamster.liq.params import load_params
from diamondhamster.liq.score import liq_corr, overlap, score_snapshots, truth_dist
from diamondhamster.liq.sim import DEFAULT_TRUTH, simulate, truth_params


def test_overlap_bounds():
    assert overlap(np.array([1, 0]), np.array([1, 0])) == 1
    assert overlap(np.array([1, 0]), np.array([0, 1])) == 0
    assert overlap(np.array([2, 2]), np.array([1, 3])) == pytest.approx(0.75)
    assert overlap(np.array([0, 0]), np.array([1, 0])) == 0


def test_truth_dist_bins_and_clips():
    edges = np.array([1.0, 2.0, 3.0, 4.0])
    t = pd.DataFrame({"ts": 5, "side": "long", "mode": "isolated", "liq_price": [0.5, 1.5, 2.5, 9.0], "qty": 1.0})
    assert list(truth_dist(t, 5, edges, "long")) == [2.0, 1.0, 1.0]
    assert truth_dist(t, 5, edges, "short").sum() == 0


def test_score_snapshots_on_short_sim():
    ev, truth, ats = simulate(2, 3, pre_days=14)
    snaps = Engine(truth_params(load_params(), DEFAULT_TRUTH)).run(ev, ats)
    res = score_snapshots(snaps, truth, ev, include_warmup=True)
    assert res["n"] == len(ats)
    with pytest.raises(ValueError, match="keine Snapshots nach dem Warmup"):
        score_snapshots(snaps, truth, ev)
    assert set(res) >= {"overlap_long", "overlap_short", "overlap", "liq_corr", "n"}
    assert 0 <= res["overlap"] <= 1


def test_liq_corr_nan_when_few_buckets():
    ev, truth, ats = simulate(2, 1, pre_days=1)
    snap = Engine(load_params()).run(ev, ats)[-1]  # letzter Snapshot: keine Folge-Events
    assert np.isnan(liq_corr(snap, ev))


def _score_seed(seed: int) -> dict:
    base = load_params()
    ev, truth, ats = simulate(seed, days=20)
    return {name: score_snapshots(Engine(p).run(ev, ats), truth, ev)["overlap"]
            for name, p in (("true", truth_params(base, DEFAULT_TRUTH)), ("default", base),
                            ("baseline", baseline_params(base)))}


@pytest.mark.slow
def test_engine_beats_fixed_leverage_on_sim(capsys):
    # Seeds sind unabhängig: parallel rechnen, damit der Test im Standardlauf bleiben kann
    with ProcessPoolExecutor(max_workers=min(5, os.cpu_count() or 1)) as pool:
        per_seed = list(pool.map(_score_seed, range(1, 6)))
    res = {k: [r[k] for r in per_seed] for k in ("true", "default", "baseline")}
    with capsys.disabled():
        print("\noverlap je Seed:", {k: [round(x, 3) for x in v] for k, v in res.items()})
    assert all(t > b for t, b in zip(res["true"], res["baseline"]))
    assert np.mean(res["default"]) > np.mean(res["baseline"])
