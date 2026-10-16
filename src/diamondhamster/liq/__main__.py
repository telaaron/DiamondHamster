"""CLI: python -m diamondhamster.liq simulate|run|score (Spec 3.7)."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

from .baseline import baseline_params
from .engine import Engine
from .events import load_events
from .params import load_params
from .score import score_snapshots
from .sim import simulate, write_sim
from .snapshot import Snapshot


def _iso_to_ms(s: str) -> int:
    t = pd.Timestamp(s)
    t = t.tz_localize("UTC") if t.tzinfo is None else t.tz_convert("UTC")
    return int(t.value // 1_000_000)


def _load_snapshots(directory: Path) -> list[Snapshot]:
    out = []
    for js in sorted(directory.glob("*.json")):
        z = np.load(js.with_suffix(".npz"))
        out.append(Snapshot(data=json.loads(js.read_text()), dist={"long": z["long"], "short": z["short"]},
                            edges=z["edges"]))
    return out


def _hl_collect(data: Path, coins: tuple[str, ...]) -> int:
    try:
        import websockets
    except ImportError:
        websockets = None
    if websockets is None:
        print("hl-collect braucht das Paket websockets: pip install -e '.[collector]'", file=sys.stderr)
        return 2
    import asyncio
    import logging
    import signal

    from .hl.api import WS_URL, HttpInfo
    from .hl.collector import Collector
    from .hl.store import Store

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    collector = Collector(Store(Path(data) / "hl"), HttpInfo(),
                          lambda: websockets.connect(WS_URL, ping_interval=20, ping_timeout=20, max_size=2**24), coins=coins)

    async def run() -> None:
        stop = asyncio.Event()
        loop = asyncio.get_running_loop()
        for sig in (signal.SIGINT, signal.SIGTERM):
            loop.add_signal_handler(sig, stop.set)
        await collector.run(stop)

    asyncio.run(run())
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m diamondhamster.liq", description="Liquidations-Engine")
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("simulate", help="synthetischer Markt mit bekannter Wahrheit")
    s.add_argument("--seed", type=int, required=True)
    s.add_argument("--days", type=int, required=True)
    s.add_argument("--out", type=Path, required=True)
    r = sub.add_parser("run", help="Snapshots aus einem Event-Satz")
    r.add_argument("--events", type=Path, required=True)
    r.add_argument("--params", type=Path)
    r.add_argument("--model", choices=("engine", "baseline"), default="engine")
    r.add_argument("--at", action="append", default=[])
    r.add_argument("--out", type=Path, required=True)
    c = sub.add_parser("score", help="Snapshots gegen ein wahres Buch bewerten")
    c.add_argument("--events", type=Path, required=True)
    c.add_argument("--snapshots", type=Path, required=True)
    c.add_argument("--include-warmup", action="store_true")
    h = sub.add_parser("hl-collect", help="Hyperliquid-Sammler im Vordergrund (läuft dauerhaft)")
    h.add_argument("--data", type=Path, required=True)
    h.add_argument("--coins", default="BTC,ETH")
    hs = sub.add_parser("hl-service", help="Sammler als macOS-Dienst: install, uninstall, status")
    hs.add_argument("action", choices=("install", "uninstall", "status"))
    hs.add_argument("--data", type=Path, required=True)
    hs.add_argument("--python", help="Python des Dienstes (Standard: dieses)")
    he = sub.add_parser("hl-events", help="Hyperliquid-Rohdaten in Event-Satz + truth.csv umwandeln")
    he.add_argument("--data", type=Path, required=True, help="Ordner <data>/hl des Sammlers")
    he.add_argument("--coin", default="BTC")
    he.add_argument("--out", type=Path, required=True)
    bd = sub.add_parser("bn-download", help="Binance-Archiv laden (fortsetzbar)")
    bd.add_argument("--symbol", default="BTCUSDT")
    bd.add_argument("--start", default="2025-01-01")
    bd.add_argument("--end", help="Standard: gestern (UTC)")
    bd.add_argument("--data", type=Path, required=True)
    be = sub.add_parser("bn-events", help="Binance-Archiv in Event-Satz umwandeln")
    be.add_argument("--symbol", default="BTCUSDT")
    be.add_argument("--data", type=Path, required=True)
    be.add_argument("--out", type=Path, required=True)
    a = ap.parse_args(argv)

    if a.cmd == "hl-collect":
        return _hl_collect(a.data, tuple(a.coins.split(",")))
    if a.cmd == "bn-download":
        from datetime import date, datetime, timedelta, timezone

        from .bn import download as dl
        end = date.fromisoformat(a.end) if a.end else datetime.now(timezone.utc).date() - timedelta(days=1)
        rep = dl.download(a.symbol, date.fromisoformat(a.start), end, a.data, fetch=dl.urllib_fetch)
        print(json.dumps(rep, indent=2))
        return 0
    if a.cmd == "bn-events":
        from .bn.adapter import build_events as bn_build
        print(json.dumps(bn_build(a.data, a.symbol, a.out), indent=2))
        return 0
    if a.cmd == "hl-events":
        from .hl.adapter import build_events
        print(json.dumps(build_events(a.data, a.coin, a.out), indent=2))
        return 0
    if a.cmd == "hl-service":
        from .hl import service
        return service.main(a.action, a.data, a.python)

    if a.cmd == "simulate":
        write_sim(a.out, *simulate(a.seed, a.days))
        return 0
    if a.cmd == "run":
        params = load_params(a.params)
        if a.model == "baseline":
            params = baseline_params(params)
        if a.at:
            ats = [_iso_to_ms(x) for x in a.at]
        elif (a.events / "ats.json").exists():
            ats = json.loads((a.events / "ats.json").read_text())
        else:
            print("run braucht --at oder ats.json im Events-Ordner", file=sys.stderr)
            return 2
        for snap in Engine(params).run(load_events(a.events), ats):
            snap.save(a.out)
        return 0
    truth_path = a.events / "truth.csv"
    if not truth_path.exists():
        print("score braucht ein wahres Buch (truth.csv)", file=sys.stderr)
        return 2
    res = score_snapshots(_load_snapshots(a.snapshots), pd.read_csv(truth_path), load_events(a.events),
                          include_warmup=a.include_warmup)
    print(json.dumps(res, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
