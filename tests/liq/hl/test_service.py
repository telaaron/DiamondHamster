import plistlib
import sys
from pathlib import Path

from diamondhamster.liq import __main__ as cli
from diamondhamster.liq.hl import service


def test_plist_contents():
    xml = service.plist_xml("/Users/a/.dh-venv/bin/python", Path("/Users/a/dh data"))
    d = plistlib.loads(xml.encode())
    assert d["Label"] == "com.diamondhamster.hl-collector"
    assert d["KeepAlive"] is True and d["RunAtLoad"] is True
    assert d["ProgramArguments"][:2] == ["/usr/bin/caffeinate", "-i"]
    assert d["ProgramArguments"][2:] == ["/Users/a/.dh-venv/bin/python", "-m", "diamondhamster.liq", "hl-collect",
                                          "--data", "/Users/a/dh data"]
    assert d["StandardOutPath"] == "/Users/a/dh data/hl/logs/out.log"
    assert d["StandardErrorPath"] == "/Users/a/dh data/hl/logs/err.log"


def test_hl_collect_without_websockets_explains(monkeypatch, tmp_path, capsys):
    monkeypatch.setitem(sys.modules, "websockets", None)
    assert cli.main(["hl-collect", "--data", str(tmp_path)]) == 2
    assert "pip install -e '.[collector]'" in capsys.readouterr().err


def test_hl_service_refuses_off_macos(monkeypatch, tmp_path, capsys):
    monkeypatch.setattr(service.sys, "platform", "linux")
    assert cli.main(["hl-service", "install", "--data", str(tmp_path)]) == 2
    assert "macOS" in capsys.readouterr().err


def test_hl_service_status_prints_status(tmp_path, capsys):
    (tmp_path / "hl").mkdir()
    (tmp_path / "hl" / "status.json").write_text('{"users": 5}')
    assert cli.main(["hl-service", "status", "--data", str(tmp_path)]) == 0
    assert '"users": 5' in capsys.readouterr().out
