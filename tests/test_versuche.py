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
    assert r["verdict"].startswith("Kandidat: einmal auf A wiederholen") and r["usage"]["calls"] == len(vs.WEEKS)
    answer(home, "E-001", "A2", candles, lambda r: 1.0 if r > 0 else 0.0)
    r = vs.score("E-001", home)
    assert r["repeated_A"] and r["verdict"] == "Kandidat, Check-Sets B+C laufen lassen" and r["tool"]
    for k in vs.CHECK:
        answer(home, "E-001", k, candles, lambda r: 1.0 if r > 0 else 0.0)
    r = vs.score("E-001", home)
    assert r["check"]["coins"] == 4 and r["verdict"] == "neuer Dev-Champion"
    assert r["usage"]["cost_usd_list"] == 0.5 * 4 * len(vs.WEEKS)
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


def test_a_champion_must_also_beat_the_fixed_reference(lab, monkeypatch):
    home, candles = lab
    monkeypatch.setattr(vs, "REFERENCE", "E-000")
    for e, parent in (("E-000", None), ("E-001", "E-000"), ("E-002", "E-001")):
        make(home, e, parent=parent)
    oracle = lambda r: 1.0 if r > 0 else 0.0
    for k in vs.SETS:
        answer(home, "E-000", k, candles, oracle)  # the reference is strong
        answer(home, "E-001", k, candles, lambda r: 0.5)  # a weak champion
        answer(home, "E-002", k, candles, lambda r: 0.75 if r > 0 else 0.25)  # beats E-001, not E-000
    answer(home, "E-002", "A2", candles, lambda r: 0.75 if r > 0 else 0.25)
    r = vs.score("E-002", home)
    assert r["A"]["diff_week_pct"] > 0 and r["verdict"].startswith("verworfen: schlägt die feste Referenz")


def test_composite_reference_averages_timing_of_its_runs(lab):
    home, candles = lab
    for e in ("E-000", "E-001"):
        make(home, e)
        answer(home, e, "A", candles, lambda r: 0.5)
    ref = home / "E-00M"
    ref.mkdir()
    (ref / "spec.json").write_text(json.dumps({"id": "E-00M", "composite": ["E-000", "E-001"], "axis": "prompt", "change": "mean"}))
    make(home, "E-002", parent="E-00M")
    answer(home, "E-002", "A", candles, lambda r: 1.0 if r > 0 else 0.0)
    r = vs.compare("E-002", "E-00M", "A", home)
    assert r["base_timing_week_pct"] == 0 and r["diff_week_pct"] > 0


def test_repeat_on_a_is_averaged_and_can_sink_a_lucky_candidate(lab):
    home, candles = lab
    make(home, "E-000")
    make(home, "E-001", parent="E-000")
    answer(home, "E-000", "A", candles, lambda r: 0.5)
    answer(home, "E-001", "A", candles, lambda r: 1.0 if r > 0 else 0.0)  # lucky first run
    assert vs.score("E-001", home)["verdict"].startswith("Kandidat: einmal")
    answer(home, "E-001", "A2", candles, lambda r: 0.0 if r > 0 else 1.0)  # the repeat is the opposite
    r = vs.score("E-001", home)
    assert r["repeated_A"] and r["verdict"] in ("kein messbarer Unterschied", "schlechter")


def test_ensemble_decides_by_the_mean_of_k_batches(lab):
    home, candles = lab
    make(home, "E-000")
    spec = json.loads((home / "E-000" / "spec.json").read_text())
    spec["ensemble"] = 3
    (home / "E-000" / "spec.json").write_text(json.dumps(spec))
    runs = vs.export("E-000", "A", home, candles)
    assert len(runs) == 3 * len(vs.WEEKS) and runs[0].name.endswith("-e1")
    for n, run in enumerate(runs):
        key = json.loads((run / "key.json").read_text())
        (run / "responses.json").write_text(json.dumps({"responses": {i: [0.0, 0.5, 1.0][n % 3] for i in key}}))
    w = vs.weights("E-000", "A", home)
    assert len(w) == 3 * len(vs.WEEKS) and (w["weight"] == 0.5).all()


def test_memory_feeds_last_weeks_weight_and_rescaled_flip(lab):
    home, candles = lab
    make(home, "E-000")
    spec = json.loads((home / "E-000" / "spec.json").read_text())
    spec["memory"] = True
    (home / "E-000" / "spec.json").write_text(json.dumps(spec))
    runs = vs.export("E-000", "A", home, candles)
    assert len(runs) == 1  # the second week needs the first week's answer
    first = json.loads((runs[0] / "requests.json").read_text())["requests"]
    assert all(r["window"].startswith("last week: no decision") for r in first)
    key = json.loads((runs[0] / "key.json").read_text())
    raw = "analysis\n```json\n" + json.dumps({i: {"weight": 0.6, "flip": 95.0} for i in key}) + "\n```"
    (runs[0] / "responses.json").write_text(json.dumps({"responses": vs.ai.parse_weights(raw), "raw": raw}))
    runs = vs.export("E-000", "A", home, candles)
    assert len(runs) == 2
    second = json.loads((runs[1] / "requests.json").read_text())
    k2 = json.loads((runs[1] / "key.json").read_text())
    t0, t1 = (pd.Timestamp(w, tz="UTC") for w in vs.WEEKS[:2])
    for r in second["requests"]:
        coin = k2[r["id"]]
        close = vs.tournament.read_candles(coin, candles)["close"]
        assert r["window"].startswith(f"last week: weight 0.60, flip price {95.0 * close[t0] / close[t1]:.1f}")
