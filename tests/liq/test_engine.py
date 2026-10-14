import numpy as np
import pandas as pd
import pytest

from diamondhamster.liq.baseline import baseline_params
from diamondhamster.liq.engine import Engine
from diamondhamster.liq.events import EventSet
from diamondhamster.liq.params import LEVERAGES, load_params

from .conftest import STEP, T0, make_events


def run(es, ats, p=None):
    return Engine(p or load_params()).run(es, ats)


def test_mass_equals_oi_after_every_interval():
    es = make_events(50)
    ats = list(es.oi.ts)
    for s, oi in zip(run(es, ats), es.oi.oi):
        assert s.dist["long"].sum() == pytest.approx(oi, rel=1e-9)
        assert s.dist["short"].sum() == pytest.approx(oi, rel=1e-9)


def test_no_lookahead():
    es = make_events(60, seed=1)
    at = int(T0 + 30 * STEP + 1234)
    full = run(es, [at])[0]
    cut = run(es.until(at), [at])[0]
    assert full.to_json() == cut.to_json()
    assert full.data["provenance"]["events_until"] <= full.data["at"]


def test_at_before_first_oi_raises():
    es = make_events(5)
    with pytest.raises(ValueError, match="no data at or before at"):
        run(es, [int(es.oi.ts.min()) - 1])


def test_gap_recorded_and_book_frozen():
    es = make_events(10)
    es.mark = es.mark[es.mark.ts != T0 + 5 * STEP].reset_index(drop=True)
    a, b = run(es, [T0 + 4 * STEP, T0 + 5 * STEP])
    assert b.data["quality"]["gaps"] and not a.data["quality"]["gaps"]
    # Masse wird auf OI skaliert, Form bleibt: normierte Verteilung unverändert
    assert np.allclose(a.dist["long"] / a.dist["long"].sum(), b.dist["long"] / b.dist["long"].sum())


def test_no_trades_uses_mark_close():
    es = make_events(1)
    es.trades = es.trades.iloc[0:0]
    es.mark.loc[1, ["low", "close", "high"]] = [119.0, 120.0, 121.0]
    es.oi.loc[1, "oi"] = es.oi.oi[0] + 500
    s = run(es, [T0 + STEP])[0]
    c = np.sqrt(s.edges[:-1] * s.edges[1:])
    assert s.dist["long"][(c > 100) & (c < 120)].sum() > 0


def test_price_crash_out_of_range():
    es = make_events(1)
    es.mark.loc[1, ["low", "close", "high"]] = [19.0, 20.0, 21.0]
    s = run(es, [T0 + STEP])[0]
    assert s.data["quality"]["out_of_range_share"] > 0
    assert s.dist["long"].sum() == pytest.approx(es.oi.oi[1])


def test_full_sweep_reseeds():
    es = make_events(1)
    es.mark.loc[1, ["low", "close", "high"]] = [1.0, 100.0, 10_000.0]
    s = run(es, [T0 + STEP])[0]
    assert s.data["quality"]["reseeds"] >= 1
    assert s.dist["short"].sum() == pytest.approx(es.oi.oi[1])


def test_funding_applies_in_gap():
    es = make_events(2)
    es.mark = es.mark[es.mark.ts != T0 + 2 * STEP].reset_index(drop=True)
    es.funding = pd.DataFrame({"ts": [T0 + 2 * STEP - 1], "rate": [0.01]})
    a, b = run(es, [T0 + STEP, T0 + 2 * STEP])
    ca = (a.dist["long"] * np.arange(len(a.edges) - 1)).sum() / a.dist["long"].sum()
    cb = (b.dist["long"] * np.arange(len(b.edges) - 1)).sum() / b.dist["long"].sum()
    assert cb > ca


def test_warmup_flag():
    es = make_events(3)
    assert run(es, [T0])[0].data["quality"]["warmup"] is True


def test_baseline_only_four_leverages():
    p = baseline_params(load_params())
    for w in p.leverage_weights.values():
        nz = {LEVERAGES[i] for i in np.flatnonzero(w)}
        assert nz == {10, 25, 50, 100}
    assert p.cross_share == 0 and p.alpha == 0
