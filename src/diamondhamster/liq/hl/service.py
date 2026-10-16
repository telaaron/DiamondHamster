"""Sammler als macOS-Hintergrunddienst (launchd), Spec 3.6."""
from __future__ import annotations

import json
import os
import plistlib
import subprocess
import sys
from pathlib import Path

LABEL = "com.diamondhamster.hl-collector"


def plist_path() -> Path:
    return Path.home() / "Library" / "LaunchAgents" / f"{LABEL}.plist"


def plist_xml(python: str, data: Path) -> str:
    data = Path(data)
    logs = data / "hl" / "logs"
    d = {"Label": LABEL, "RunAtLoad": True, "KeepAlive": True, "ThrottleInterval": 30,
         # caffeinate -i: Mac schläft im Leerlauf nicht ein, solange der Sammler läuft
         "ProgramArguments": ["/usr/bin/caffeinate", "-i", python, "-m", "diamondhamster.liq", "hl-collect",
                              "--data", str(data)],
         "WorkingDirectory": str(data), "StandardOutPath": str(logs / "out.log"),
         "StandardErrorPath": str(logs / "err.log")}
    return plistlib.dumps(d).decode()


def _launchctl(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["launchctl", *args], capture_output=True, text=True)


def main(action: str, data: Path, python: str | None = None) -> int:
    if action == "status":
        p = Path(data) / "hl" / "status.json"
        if not p.exists():
            print(f"kein Status unter {p} (läuft der Sammler?)", file=sys.stderr)
            return 1
        print(json.dumps(json.loads(p.read_text()), indent=2))
        return 0
    if sys.platform != "darwin":
        print("hl-service gibt es nur auf macOS; sonst hl-collect direkt starten", file=sys.stderr)
        return 2
    domain = f"gui/{os.getuid()}"
    _launchctl("bootout", f"{domain}/{LABEL}")  # alte Version stoppen, Fehler egal
    if action == "uninstall":
        plist_path().unlink(missing_ok=True)
        print("Sammler-Dienst entfernt")
        return 0
    (Path(data) / "hl" / "logs").mkdir(parents=True, exist_ok=True)
    plist_path().parent.mkdir(parents=True, exist_ok=True)
    plist_path().write_text(plist_xml(python or sys.executable, Path(data).resolve()))
    r = _launchctl("bootstrap", domain, str(plist_path()))
    if r.returncode != 0:
        print(f"launchctl bootstrap fehlgeschlagen: {r.stderr.strip()}", file=sys.stderr)
        return 1
    print(f"Sammler-Dienst läuft ({LABEL}); Status: python -m diamondhamster.liq hl-service status --data {data}")
    return 0
