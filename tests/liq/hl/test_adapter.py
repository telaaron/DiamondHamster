import gzip
import json

import numpy as np
import pandas as pd
import pytest

from diamondhamster.liq import __main__ as cli
from diamondhamster.liq.events import load_events
from diamondhamster.liq.hl.adapter import build_events
from diamondhamster.liq.hl.store import Store

M = 60_000
T0 = 1_790_000_000_000 // M * M
DAYS = 3


def make_raw(root, skip_ctx=()):
    rng = np.random.default_rng(0)
    s = Store(root)
    n = DAYS * 1440
    mark = 100_000 * np.exp(np.cumsum(rng.normal(0, 5e-4, n)))
    oi = 1000 + np.cumsum(rng.normal(0, 2, n))
    tid = 0
    for i in range(n):
        t = T0 + i * M
        if i in skip_ctx:
            continue
        s.append("ctx", {"t": t, "coins": {"BTC": {"oi": oi[i], "mark": mark[i], "funding": 1e-5, "max_lev": 40}}}, t)
        s.append("candles", {"ts": t - M, "high": mark[i] * 1.002, "low": mark[i] * 0.998}, t - M, coin="BTC")
        for _ in range(3):
            tid += 1
            rec = {"coin": "BTC", "ts": t - int(rng.integers(1, M)), "price": mark[i], "qty": float(rng.lognormal(-3, 1)),
                   "taker_buy": int(rng.integers(0, 2)), "buyer": "a", "seller": "b", "tid": tid, "rt": t}
            s.append("trades", rec, rec["ts"], coin="BTC")
            if tid % 50 == 0:  # Wiederholung nach Reconnect
                s.append("trades", rec, rec["ts"], coin="BTC")
        if i % 60 == 0:
            s.append("funding", {"ts": t, "rate": 1e-5}, t, coin="BTC")
        if i % 15 == 0 and i > 0:
            book = pd.DataFrame({"user": ["a", "b", "c"], "side": ["long", "short", "long"],
                                 "mode": ["cross", "isolated", "cross"], "leverage": [10, 20, 2],
                                 "entry_px": [mark[i]] * 3, "liq_px": [mark[i] * 0.9, mark[i] * 1.05, None],
                                 "qty": [5.0, 3.0, 1.0], "polled_at": [t] * 3})
            s.write_book("BTC", t, book)
    s.gap(T0 + 100 * M, T0 + 103 * M, "ws")
    s.close()
    return root


@pytest.fixture
def raw(tmp_path):
    return make_raw(tmp_path / "hl")


def test_ctx_hole_becomes_gap(tmp_path):
    root = make_raw(tmp_path / "hl", skip_ctx=range(500, 520))
    build_events(root, "BTC", tmp_path / "ev")
    es = load_events(tmp_path / "ev")
    holes = es.gaps[es.gaps.reason == "ctx"]
    assert list(zip(holes.start, holes.end)) == [(T0 + 499 * M, T0 + 520 * M)]


def test_snapshots_in_or_right_after_gap_dropped(raw, tmp_path):
    build_events(raw, "BTC", tmp_path / "ev")
    ats = set(json.loads((tmp_path / "ev" / "ats.json").read_text()))
    assert T0 + 90 * M in ats
    assert T0 + 105 * M not in ats and T0 + 120 * M not in ats  # Lücke endet bei 103 min, 30 min Schonfrist
    assert T0 + 135 * M in ats


def test_build_events_end_to_end(raw, tmp_path):
    out = tmp_path / "ev"
    rep = build_events(raw, "BTC", out)
    es = load_events(out)
    assert es.exchange == "hyperliquid" and es.symbol == "BTC"
    assert len(es.oi) == DAYS * 1440 and rep["broken_lines"] == 0
    assert rep["duplicate_trades"] > 0
    assert (es.mark.high >= es.mark.close).all() and (es.mark.low <= es.mark.close).all()
    assert "notional" in es.trades.columns and es.trades.ts.is_monotonic_increasing
    truth = pd.read_csv(out / "truth.csv")
    assert set(truth.side) == {"long", "short"} and truth.liq_price.notna().all()
    assert list(es.gaps.reason) == ["ws"]
    ats = json.loads((out / "ats.json").read_text())
    assert ats and min(ats) >= es.oi.ts.iloc[0] and set(ats) == set(truth.ts)
    assert "max_leverage = 40" in (out / "tiers.toml").read_text()
    assert 'tiers = "tiers.toml"' in (out / "params.toml").read_text()


def test_mark_takes_candle_extremes(raw, tmp_path):
    out = tmp_path / "ev"
    build_events(raw, "BTC", out)
    es = load_events(out)
    r = es.mark.iloc[10]
    assert r.high == pytest.approx(r.close * 1.002) and r.low == pytest.approx(r.close * 0.998)


def test_run_and_score_on_adapter_output(raw, tmp_path, capsys):
    out = tmp_path / "ev"
    build_events(raw, "BTC", out)
    for model in ("engine", "baseline"):
        assert cli.main(["run", "--events", str(out), "--params", str(out / "params.toml"), "--model", model,
                         "--out", str(tmp_path / model)]) == 0
        capsys.readouterr()
        assert cli.main(["score", "--events", str(out), "--snapshots", str(tmp_path / model),
                         "--include-warmup"]) == 0
        res = json.loads(capsys.readouterr().out)
        assert 0 <= res["overlap"] <= 1 and res["n"] > 0


def test_truncated_gzip_line_counted(raw, tmp_path):
    f = sorted((raw / "raw/ctx").glob("*.gz"))[-1]
    data = gzip.compress(b'{"t": 1, "coins"')
    f.write_bytes(f.read_bytes() + data[:-4])
    rep = build_events(raw, "BTC", tmp_path / "ev")
    assert rep["broken_lines"] >= 1


def test_cli_hl_events(raw, tmp_path):
    assert cli.main(["hl-events", "--data", str(raw), "--coin", "BTC", "--out", str(tmp_path / "ev")]) == 0
    assert (tmp_path / "ev" / "truth.csv").exists()
