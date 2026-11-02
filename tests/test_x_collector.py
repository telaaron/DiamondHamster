import gzip
import hashlib
import importlib.util
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "x_collector", Path(__file__).resolve().parents[1] / "research/x-daten/collector.py")
col = importlib.util.module_from_spec(spec)
spec.loader.exec_module(col)


def test_prereg_frozen():
    assert not col.prereg_frozen("Eingefroren am: ____ · Commit: ____")
    assert col.prereg_frozen("Eingefroren am: 2026-11-05 · Commit: abc")


def test_store_raw_never_overwrites_and_hashes(tmp_path):
    now = datetime(2026, 11, 2, 10, 0, 0, tzinfo=timezone.utc)
    a = col.store_raw(tmp_path, now, "UserTweets", 1, 0, {"x": 1}, {"endpoint": "UserTweets"})
    b = col.store_raw(tmp_path, now, "UserTweets", 1, 0, {"x": 2}, {"endpoint": "UserTweets"})
    assert a != b and a.exists() and b.exists()
    assert json.loads(gzip.decompress(a.read_bytes())) == {"x": 1}
    manifest = (tmp_path / "raw/2026-11-02/sha256.txt").read_text().splitlines()
    assert len(manifest) == 4
    h, name = manifest[0].split("  ")
    assert hashlib.sha256((a.parent / name).read_bytes()).hexdigest() == h


def test_due_for_replies_window(tmp_path):
    con = col.open_state(tmp_path)
    now = datetime(2026, 11, 2, 12, tzinfo=timezone.utc)
    for tid, age_h in [(1, 1), (2, 5), (3, 30)]:
        con.execute("insert into posts(tweet_id,user_id,created_utc) values(?,?,?)",
                    (tid, 9, (now - timedelta(hours=age_h)).isoformat()))
    assert col.due_for_replies(con, now) == [(2, 9)]


def test_main_refuses_without_setup(tmp_path, capsys):
    rc = col.main(["--data", str(tmp_path), "--db", str(tmp_path / "none.db"),
                   "--accounts", str(tmp_path / "none.csv"), "--dry-run"])
    assert rc == 2
    assert "NICHT GESTARTET" in capsys.readouterr().out
