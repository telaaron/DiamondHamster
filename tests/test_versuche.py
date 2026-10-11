import json

import pandas as pd
import pytest

from diamondhamster import versuche as vs
from test_core import synthetic


@pytest.fixture
def lab(tmp_path, monkeypatch):
    candles = tmp_path / "candles"
    candles.mkdir()
    sets = {"A": ["AAA", "BBB", "CCC"], "B": ["DDD", "EEE"], "C": ["FFF", "GGG"]}
    for i, c in enumerate(c for cs in sets.values() for c in cs):
        synthetic(500, start="2025-06-01", seed=i).to_csv(candles / f"{c}.csv")
    monkeypatch.setattr(vs, "SETS", sets)
    monkeypatch.setattr(vs, "WEEKS", [d.date() for d in pd.date_range("2026-07-05", "2026-09-06", freq="W-SUN")])
    monkeypatch.setattr(vs.tournament, "CANDLES", candles)
    monkeypatch.setattr(vs.tournament, "universe", lambda: [c for cs in sets.values() for c in cs])
    home = tmp_path / "versuche"
    return home, candles


def make(home, exp_id, parent=None, prompt="decide", input="candles"):
    d = home / exp_id
    d.mkdir(parents=True)
    (d / "spec.json").write_text(json.dumps({"id": exp_id, "parent": parent, "axis": "prompt", "change": f"change {exp_id}", "input": input, "lookback": 60}))
    (d / "prompt.md").write_text(prompt)


def answer(home, exp_id, which, candles, rule):
    """Fill responses with weights from rule(future_return) so scoring has a known answer."""
    for run in vs.export(exp_id, which, home, candles):
        key = json.loads((run / "key.json").read_text())
        t = pd.Timestamp(run.name, tz="UTC")
        resp = {}
        for i, c in key.items():
            close = vs.tournament.read_candles(c, candles)["close"]
            resp[i] = rule(close[t + pd.Timedelta(days=7)] / close[t] - 1)
        (run / "responses.json").write_text(json.dumps({"responses": resp, "cost_usd": 0.5}))


def test_batches_hold_one_week_across_coins_and_hide_names(lab):
    home, candles = lab
    make(home, "E-000")
    runs = vs.export("E-000", "A", home, candles)
    assert [r.name for r in runs] == [w.isoformat() for w in vs.WEEKS]
    req = json.loads((runs[0] / "requests.json").read_text())
    assert len(req["requests"]) == 3
    text = json.dumps(req["requests"])
    assert all(c not in text for c in ["AAA", "BBB", "CCC", "2026", "2025"])
    # every window in a batch ends on the decision day: the last row is day 0 at price 100
    assert all(r["window"].splitlines()[-1].startswith("0 ") for r in req["requests"])


def test_custom_renderer_only_gets_the_past_and_leaks_are_refused(lab):
    home, candles = lab
    make(home, "E-001", input="custom")
    (home / "E-001" / "render.py").write_text("def render(df, lookback):\n    return f'last {df.index[-1].day} n {len(df)}'\n")
    run = vs.export("E-001", "A", home, candles)[0]
    w = json.loads((run / "requests.json").read_text())["requests"][0]["window"]
    assert w.startswith(f"last {vs.WEEKS[0].day} ")
    make(home, "E-002", input="custom")
    (home / "E-002" / "render.py").write_text("def render(df, lookback):\n    return str(df.index[-1])\n")
    with pytest.raises(ValueError, match="calendar"):
        vs.export("E-002", "A", home, candles)


def test_scoring_finds_foresight_and_needs_the_check_sets(lab):
    home, candles = lab
    make(home, "E-000")
    make(home, "E-001", parent="E-000", prompt="better")
    (home / "champion.json").write_text(json.dumps({"id": "E-000"}))
    for k in vs.SETS:
        answer(home, "E-000", k, candles, lambda r: 0.5)
    answer(home, "E-001", "A", candles, lambda r: 1.0 if r > 0 else 0.0)
    ref = vs.score("E-000", home)
    assert ref["verdict"] == "Referenz" and ref["A"]["timing_week_pct"] == 0
    r = vs.score("E-001", home)
    assert r["A"]["diff_week_pct"] > 0 and r["A"]["diff_t"] > 2 and r["A"]["diff_ex_best_week_pct"] > 0
    assert r["verdict"].startswith("Kandidat") and r["usage"]["calls"] == len(vs.WEEKS)
    for k in vs.CHECK:
        answer(home, "E-001", k, candles, lambda r: 1.0 if r > 0 else 0.0)
    r = vs.score("E-001", home)
    assert r["check"]["coins"] == 4 and r["verdict"] == "neuer Dev-Champion"
    assert r["usage"]["cost_usd_list"] == 0.5 * 3 * len(vs.WEEKS)
    vs.card("E-001", home)
    card = (home / "E-001" / "card.md").read_text()
    assert "-decide" in card and "+better" in card and "neuer Dev-Champion" in card
    ov = vs.overview(home)
    assert "Varianten bisher getestet: **1**" in ov and "E-001" in ov


def test_a_lucky_single_week_is_not_a_win(lab):
    home, candles = lab
    make(home, "E-000")
    make(home, "E-003", parent="E-000")
    answer(home, "E-000", "A", candles, lambda r: 0.5)
    answer(home, "E-003", "A", candles, lambda r: 0.5)
    first = home / "E-003" / "runs" / "A" / vs.WEEKS[0].isoformat()
    resp = json.loads((first / "responses.json").read_text())
    key = json.loads((first / "key.json").read_text())
    t = pd.Timestamp(vs.WEEKS[0], tz="UTC")
    for i, c in key.items():
        close = vs.tournament.read_candles(c, candles)["close"]
        resp["responses"][i] = 1.0 if close[t + pd.Timedelta(days=7)] > close[t] else 0.0
    (first / "responses.json").write_text(json.dumps(resp))
    r = vs.score("E-003", home)
    assert r["A"]["diff_week_pct"] > 0 and r["verdict"] == "kein messbarer Unterschied"


def test_reasoning_before_the_weights_is_kept_and_shown(lab):
    home, candles = lab
    make(home, "E-000")
    runs = vs.export("E-000", "A", home, candles)
    for run in runs:
        key = json.loads((run / "key.json").read_text())
        raw = "Lage: seitwärts, ich bleibe halb drin.\n" + json.dumps({i: 0.5 for i in key})
        (run / "responses.json").write_text(json.dumps({"responses": vs.ai.parse_weights(raw), "raw": raw, "cost_usd": 0.1}))
    assert len(vs.weights("E-000", "A", home)) == 3 * len(vs.WEEKS)
    vs.card("E-000", home)
    card = (home / "E-000" / "card.md").read_text()
    assert "Lage: seitwärts" in card and "(AAA)" in (home / "E-000" / "denken.md").read_text()
    broken = runs[0] / "responses.json"
    r = json.loads(broken.read_text())
    r["responses"].popitem()
    broken.write_text(json.dumps(r))
    with pytest.raises(ValueError, match="no weight"):
        vs.weights("E-000", "A", home)


def test_publish_copies_cards_but_not_runs(lab, tmp_path):
    home, candles = lab
    make(home, "E-000")
    vs.export("E-000", "A", home, candles)
    (home / "UEBERSICHT.md").write_text("x")
    dest = tmp_path / "repo" / "versuche"
    vs.publish(home, dest)
    assert (dest / "E-000" / "prompt.md").exists() and (dest / "UEBERSICHT.md").exists()
    assert not (dest / "E-000" / "runs").exists()
