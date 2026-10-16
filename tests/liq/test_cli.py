import json

from diamondhamster.liq.__main__ import main


def test_cli_end_to_end(tmp_path, capsys):
    ev, snap = tmp_path / "ev", tmp_path / "snap"
    assert main(["simulate", "--seed", "1", "--days", "3", "--out", str(ev)]) == 0
    assert main(["run", "--events", str(ev), "--out", str(snap)]) == 0
    assert len(list(snap.glob("*.json"))) == 3
    capsys.readouterr()
    assert main(["score", "--events", str(ev), "--snapshots", str(snap), "--include-warmup"]) == 0
    assert "overlap" in json.loads(capsys.readouterr().out)


def test_cli_run_explicit_at_and_baseline(tmp_path):
    ev, snap = tmp_path / "ev", tmp_path / "snap"
    main(["simulate", "--seed", "2", "--days", "1", "--out", str(ev)])
    assert main(["run", "--events", str(ev), "--model", "baseline", "--at", "2026-01-15T12:00:00Z",
                 "--out", str(snap)]) == 0
    d = json.loads((snap / "20260115T1200Z.json").read_text())
    assert d["provenance"]["params_hash"].endswith("+override")


def test_cli_score_without_truth(tmp_path, capsys):
    ev, snap = tmp_path / "ev", tmp_path / "snap"
    main(["simulate", "--seed", "1", "--days", "1", "--out", str(ev)])
    main(["run", "--events", str(ev), "--out", str(snap)])
    (ev / "truth.csv").unlink()
    assert main(["score", "--events", str(ev), "--snapshots", str(snap)]) == 2
    assert "truth.csv" in capsys.readouterr().err
