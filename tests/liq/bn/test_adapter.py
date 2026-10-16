import json
from datetime import date

import pandas as pd

from diamondhamster.liq import __main__ as cli
from diamondhamster.liq.bn.adapter import build_events
from diamondhamster.liq.bn.download import download
from diamondhamster.liq.events import load_events

from .conftest import SYM, ms

D1, D2, D3 = date(2025, 1, 1), date(2025, 1, 2), date(2025, 1, 3)


def test_build_events_end_to_end(archive, tmp_path):
    for d in (D1, D3):
        archive.add_day(d)
    archive.add_funding(2025, 1, [0.0001, 0.0002, -0.0001])
    download(SYM, D1, D3, tmp_path, fetch=archive)
    out = tmp_path / "ev"
    rep = build_events(tmp_path, SYM, out)
    es = load_events(out)
    assert es.exchange == "binance" and es.symbol == SYM
    assert len(es.oi) == 11 and es.oi.ts.iloc[0] >= es.mark.ts.iloc[0] and "notional" in es.trades.columns
    assert list(es.funding.rate) == [0.0001, 0.0002, -0.0001]
    assert len(es.gaps) == 1 and es.gaps.start.iloc[0] == ms(D2) and es.gaps.end.iloc[0] == ms(D3)
    assert json.loads((out / "ats.json").read_text()) == [ms(D2), ms(D3)]
    assert rep["missing_days"] == ["2025-01-02"]


def test_run_on_binance_events(archive, tmp_path):
    archive.add_day(D1)
    download(SYM, D1, D1, tmp_path, fetch=archive)
    out = tmp_path / "ev"
    build_events(tmp_path, SYM, out)
    (out / "ats.json").write_text(json.dumps([ms(D1, 25)]))
    assert cli.main(["run", "--events", str(out), "--out", str(tmp_path / "snap")]) == 0
    assert len(list((tmp_path / "snap").glob("*.json"))) == 1


def test_cli_bn_download_and_events(archive, tmp_path, monkeypatch):
    from diamondhamster.liq.bn import download as dl
    archive.add_day(D1)
    monkeypatch.setattr(dl, "urllib_fetch", archive)
    assert cli.main(["bn-download", "--symbol", SYM, "--start", "2025-01-01", "--end", "2025-01-01",
                     "--data", str(tmp_path)]) == 0
    assert cli.main(["bn-events", "--symbol", SYM, "--data", str(tmp_path), "--out", str(tmp_path / "ev")]) == 0
    assert pd.read_csv(tmp_path / "ev" / "oi.csv").shape[0] == 5
