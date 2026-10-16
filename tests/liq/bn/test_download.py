import json
from datetime import date

import pandas as pd

from diamondhamster.liq.bn.download import download, url_for

from .conftest import SYM

D1, D2, D3 = date(2025, 1, 1), date(2025, 1, 2), date(2025, 1, 3)


def test_url_for():
    base = "https://data.binance.vision/data/futures/um/"
    assert url_for("aggTrades", SYM, D1) == base + "daily/aggTrades/BTCUSDT/BTCUSDT-aggTrades-2025-01-01.zip"
    assert url_for("metrics", SYM, D1) == base + "daily/metrics/BTCUSDT/BTCUSDT-metrics-2025-01-01.zip"
    assert url_for("markPriceKlines", SYM, D1) == base + "daily/markPriceKlines/BTCUSDT/1m/BTCUSDT-1m-2025-01-01.zip"
    assert url_for("fundingRate", SYM, D1) == base + "monthly/fundingRate/BTCUSDT/BTCUSDT-fundingRate-2025-01.zip"


def test_download_writes_normalized_csv(archive, tmp_path):
    archive.add_day(D1)
    archive.add_funding(2025, 1, [0.0001, -0.0002])
    rep = download(SYM, D1, D1, tmp_path, fetch=archive)
    d = tmp_path / "bn" / SYM
    agg = pd.read_csv(d / "aggTrades/2025-01-01.csv")
    assert list(agg.columns) == ["ts", "price", "qty", "taker_buy", "notional"] and agg.qty.sum() > 0
    assert list(pd.read_csv(d / "metrics/2025-01-01.csv").columns) == ["ts", "oi"]
    mk = pd.read_csv(d / "markPriceKlines/2025-01-01.csv")
    assert list(mk.columns) == ["ts", "high", "low", "close"] and mk.ts.iloc[0] % 60_000 == 0
    assert list(pd.read_csv(d / "fundingRate/2025-01.csv").rate) == [0.0001, -0.0002]
    assert rep["done"] == 4 and rep["missing"] == 0


def test_header_and_no_header_same_result(archive, tmp_path):
    archive.add_day(D1, header=True)
    archive.add_day(D2, header=False)
    download(SYM, D1, D2, tmp_path, fetch=archive)
    d = tmp_path / "bn" / SYM / "aggTrades"
    a, b = pd.read_csv(d / "2025-01-01.csv"), pd.read_csv(d / "2025-01-02.csv")
    assert len(a) == len(b) and (a.qty.to_numpy() == b.qty.to_numpy()).all()


def test_resume_skips_done(archive, tmp_path):
    archive.add_day(D1)
    download(SYM, D1, D1, tmp_path, fetch=archive)
    n = len(archive.calls)
    download(SYM, D1, D1, tmp_path, fetch=archive)
    assert [c for c in archive.calls[n:] if "fundingRate" not in c] == []


def test_404_recorded_and_continues(archive, tmp_path):
    archive.add_day(D1)
    archive.add_day(D3, skip=("metrics",))
    rep = download(SYM, D1, D3, tmp_path, fetch=archive)
    missing = [json.loads(l) for l in (tmp_path / "bn" / SYM / "missing.jsonl").read_text().splitlines()]
    keys = {(m["kind"], m["tag"]) for m in missing}
    assert ("metrics", "2025-01-03") in keys and ("aggTrades", "2025-01-02") in keys
    assert (tmp_path / "bn" / SYM / "aggTrades/2025-01-03.csv").exists()
    assert rep["missing"] >= 4


def test_bad_checksum_not_marked_done(archive, tmp_path):
    archive.add_day(D1)
    url = next(u for u in archive.files if "metrics" in u and not u.endswith("CHECKSUM"))
    archive.add(url, archive.files[url], bad_checksum=True)
    rep = download(SYM, D1, D1, tmp_path, fetch=archive)
    assert not (tmp_path / "bn" / SYM / "done/metrics/2025-01-01").exists()
    assert rep["errors"] == 1


def test_metrics_ts_in_ms(archive, tmp_path):
    from .conftest import ms
    archive.add_day(D1)
    download(SYM, D1, D1, tmp_path, fetch=archive)
    oi = pd.read_csv(tmp_path / "bn" / SYM / "metrics/2025-01-01.csv")
    assert oi.ts.iloc[1] == ms(D1, 5)


def test_holdout_fetches_logged(archive, tmp_path):
    late = date(2026, 7, 1)
    for d in (date(2026, 6, 30), late):
        archive.add_day(d)
    archive.add_funding(2026, 6, [0.0001])
    archive.add_funding(2026, 7, [0.0001])
    rep = download(SYM, date(2026, 6, 30), late, tmp_path, fetch=archive)
    lines = (tmp_path / "bn" / SYM / "holdout_access.log").read_text().splitlines()
    tags = sorted(l.split("\t")[1].split()[3] for l in lines)
    assert tags == ["2026-06", "2026-06-30", "2026-06-30", "2026-06-30"]
    assert all("binance.vision" in l for l in lines)
    assert rep["holdout"] == 4
    download(SYM, date(2026, 6, 30), late, tmp_path, fetch=archive)  # bereits fertig: kein neuer Abruf, kein Eintrag
    assert len((tmp_path / "bn" / SYM / "holdout_access.log").read_text().splitlines()) == 4
