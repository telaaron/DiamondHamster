import time

import numpy as np
import pandas as pd
import pytest

from diamondhamster.liq.events import validate
from diamondhamster.liq.params import load_params
from diamondhamster.liq.sim import DEFAULT_TRUTH, simulate, truth_params


@pytest.fixture(scope="module")
def sim3():
    t = time.perf_counter()
    out = simulate(1, 3)
    out_time = time.perf_counter() - t
    return out, out_time


def test_sim_is_fast_enough(sim3):
    assert sim3[1] < 5


def test_sim_is_deterministic(sim3):
    (ev, truth, ats), _ = sim3
    ev2, truth2, ats2 = simulate(1, 3)
    pd.testing.assert_frame_equal(ev.trades, ev2.trades)
    pd.testing.assert_frame_equal(truth, truth2)
    assert ats == ats2


def test_sim_events_validate(sim3):
    (ev, _, ats), _ = sim3
    validate(ev)
    assert len(ats) == 3 and ev.oi.ts.min() < ats[0] and not ev.funding.empty and not ev.liquidations.empty


def test_sim_oi_equals_truth_both_sides(sim3):
    (ev, truth, ats), _ = sim3
    for at in ats:
        oi = ev.oi.oi[ev.oi.ts == at].iloc[0]
        t = truth[truth.ts == at]
        assert t[t.side == "long"].qty.sum() == pytest.approx(oi, rel=1e-9)
        assert t[t.side == "short"].qty.sum() == pytest.approx(oi, rel=1e-9)


def test_sim_liquidations_inside_mark_range(sim3):
    (ev, _, _), _ = sim3
    step_end = ev.mark.ts.to_numpy()
    j = np.searchsorted(step_end, ev.liquidations.ts.to_numpy(), side="left")
    lo, hi = ev.mark.low.to_numpy()[j], ev.mark.high.to_numpy()[j]
    p = ev.liquidations.price.to_numpy()
    assert ((p >= lo - 1e-9) & (p <= hi + 1e-9)).all()


def test_truth_params_overrides():
    p = truth_params(load_params(), DEFAULT_TRUTH)
    assert p.cross_share == DEFAULT_TRUTH.cross_share and p.beta == DEFAULT_TRUTH.beta
    assert p.alpha == DEFAULT_TRUTH.transfer_share
    assert np.allclose(p.leverage_weights["small"].sum(), 1)
