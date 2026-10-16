import json

import numpy as np
import pytest

from diamondhamster.liq.attribution import Deposit
from diamondhamster.liq.book import Book
from diamondhamster.liq.grid import Grid
from diamondhamster.liq.params import load_params
from diamondhamster.liq.snapshot import build_snapshot, find_clusters, validate_snapshot

AT = 1_788_220_800_000  # 2026-09-01T00:00:00Z
DAY = AT // 86_400_000


def make_book():
    b = Book(Grid(100, 10), max_cohorts=10, start_day=DAY)
    b.add(Deposit("long", "isolated", np.array([97.0]), np.array([1.0])), cohort=DAY, ambiguous_frac=0.5)
    b.add(Deposit("short", "isolated", np.array([115.0]), np.array([2.0])), cohort=DAY, ambiguous_frac=0.0)
    return b


def snap(b=None):
    return build_snapshot(b or make_book(), load_params(), exchange="sim", symbol="BTCUSDT", at_ms=AT, mark=100.0,
                          oi=3.0, quality={"warmup": False, "max_drift": 0.0, "drift_warning": False, "gaps": [],
                                           "reseeds": 0},
                          sources=["sim:BTCUSDT"], events_until_ms=AT)


def test_schema_valid_and_deterministic():
    a, b = snap(), snap()
    validate_snapshot(a.data)
    assert a.to_json() == b.to_json()
    d = a.data
    assert d["schema"] == "liq-snapshot/1" and d["at"] == "2026-09-01T00:00:00Z"
    assert d["provenance"]["model_version"] == "liq/0.1.0" and d["quality"]["seed_share"] == 0


def test_clusters_threshold_and_order():
    g = Grid(100, 10)
    dist = np.zeros(g.n)
    i = g.index(90)
    dist[i:i + 3] = 1.0
    j = g.index(80)
    dist[j] = 1.0
    out = find_clusters(dist, dist * 0, dist * 0, g, 100.0, "long", 0.002, 10)
    assert len(out) == 2 and out[0]["notional_usd"] > out[1]["notional_usd"]
    assert out[0]["from"] == pytest.approx(g.edges[i]) and out[0]["to"] == pytest.approx(g.edges[i + 3])
    assert out[0]["dist_pct"] < 0


def test_summary_within_and_asymmetry():
    s = snap().data["summary"]
    assert s["long_usd_within"]["5"] == pytest.approx(97.0, rel=2e-3)
    assert s["short_usd_within"]["10"] == 0
    assert s["short_usd_within"]["20"] == pytest.approx(230.0, rel=2e-3)
    assert s["asymmetry_10"] == pytest.approx(-1.0)
    lv = snap().data["levels"]["long"][0]
    assert lv["share_ambiguous"] == pytest.approx(0.5)


def test_save_writes_json_and_npz(tmp_path):
    snap().save(tmp_path)
    assert json.loads((tmp_path / "20260901T0000Z.json").read_text())["symbol"] == "BTCUSDT"
    z = np.load(tmp_path / "20260901T0000Z.npz")
    assert set(z.files) == {"long", "short", "edges"} and z["long"].sum() == pytest.approx(1.0)


def test_validate_rejects_missing_key():
    d = snap().data
    del d["quality"]
    with pytest.raises(AssertionError):
        validate_snapshot(d)
