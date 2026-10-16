import gzip
import json

import pandas as pd

from diamondhamster.liq.hl.scheduler import Scheduler
from diamondhamster.liq.hl.store import Store, read_jsonl_gz

DAY = 86_400_000
T = 1_790_000_000_000  # 2026-09-21


def test_append_splits_by_utc_day_and_coin(tmp_path):
    s = Store(tmp_path, run_id="r")
    s.append("trades", {"a": 1}, T, coin="BTC")
    s.append("trades", {"a": 2}, T + DAY, coin="BTC")
    s.close()
    files = sorted(p.relative_to(tmp_path).as_posix() for p in (tmp_path / "raw").rglob("*.gz"))
    assert files == ["raw/trades/BTC/2026-09-21.r.jsonl.gz", "raw/trades/BTC/2026-09-22.r.jsonl.gz"]


def test_flushed_data_readable_while_open_and_new_part_after_restart(tmp_path):
    s = Store(tmp_path, run_id="a")
    s.append("ctx", {"i": 1}, T)
    s.flush()
    path = tmp_path / "raw/ctx/2026-09-21.a.jsonl.gz"
    recs, broken = read_jsonl_gz(path)
    assert recs == [{"i": 1}]
    s.close()
    s2 = Store(tmp_path, run_id="b")  # Neustart: eigene Teildatei
    s2.append("ctx", {"i": 2}, T)
    s2.close()
    assert read_jsonl_gz(path) == ([{"i": 1}], 0)
    assert read_jsonl_gz(tmp_path / "raw/ctx/2026-09-21.b.jsonl.gz") == ([{"i": 2}], 0)


def test_truncated_tail_counted_not_fatal(tmp_path):
    path = tmp_path / "x.jsonl.gz"
    with gzip.open(path, "wt") as f:
        f.write(json.dumps({"ok": 1}) + "\n")
    data = gzip.compress(b'{"ok": 2}\n{"half": ')
    path.write_bytes(path.read_bytes() + data[: len(data) - 5])
    recs, broken = read_jsonl_gz(path)
    assert recs[0] == {"ok": 1} and broken >= 1


def test_book_gap_status(tmp_path):
    s = Store(tmp_path)
    s.write_book("BTC", T, pd.DataFrame({"user": ["a"], "qty": [1.0]}))
    s.gap(T, T + 5000, "ws")
    s.write_status({"n": 3})
    assert pd.read_csv(tmp_path / "book/BTC/20260921T1413Z.csv.gz").qty.tolist() == [1.0]
    assert json.loads((tmp_path / "gaps.jsonl").read_text()) == {"start": T, "end": T + 5000, "reason": "ws"}
    assert json.loads((tmp_path / "status.json").read_text()) == {"n": 3}


def test_state_roundtrip_restores_scheduler(tmp_path):
    s = Store(tmp_path)
    assert s.load_state() is None
    sch = Scheduler(0)
    sch.polled("a", 2e6, True, 0)
    s.save_state({"scheduler": sch.to_state()})
    assert not list(tmp_path.glob("*.tmp"))
    back = Scheduler.from_state(Store(tmp_path).load_state()["scheduler"])
    assert len(back) == 1


def test_restart_after_crash_keeps_all_lines(tmp_path):
    a = Store(tmp_path, run_id="1")
    for i in range(1000):
        a.append("ctx", {"i": i}, T)
    a.flush()  # Absturz: a wird nie geschlossen, letztes gzip-Glied ohne Abschluss
    b = Store(tmp_path, run_id="2")
    for i in range(1000, 2000):
        b.append("ctx", {"i": i}, T)
    b.close()
    recs = []
    for p in sorted((tmp_path / "raw/ctx").glob("*.jsonl.gz")):
        recs += read_jsonl_gz(p)[0]
    assert sorted(r["i"] for r in recs) == list(range(2000))
    a._open.clear()  # Testende: a nicht nachträglich sauber schließen lassen
