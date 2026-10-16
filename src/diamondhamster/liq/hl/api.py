"""Hyperliquid-API: Antworten parsen und /info aufrufen. Nur öffentliche Endpunkte, kein Schlüssel."""
from __future__ import annotations

import json
import urllib.error
import urllib.request

INFO_URL = "https://api.hyperliquid.xyz/info"
WS_URL = "wss://api.hyperliquid.xyz/ws"
WEIGHTS = {"clearinghouseState": 2, "metaAndAssetCtxs": 20, "candleSnapshot": 20, "fundingHistory": 20}


class RateLimited(RuntimeError):
    pass


def parse_trades(msg: dict) -> list[dict]:
    if msg.get("channel") != "trades":
        return []
    return [{"coin": t["coin"], "ts": int(t["time"]), "price": float(t["px"]), "qty": float(t["sz"]),
             "taker_buy": 1 if t["side"] == "B" else 0, "buyer": t["users"][0], "seller": t["users"][1],
             "tid": t["tid"]} for t in msg.get("data", [])]


def parse_ctx(resp: list, coins: tuple[str, ...]) -> dict[str, dict]:
    meta, ctxs = resp
    out = {}
    for asset, ctx in zip(meta["universe"], ctxs):
        if asset["name"] in coins:
            out[asset["name"]] = {"oi": float(ctx["openInterest"]), "mark": float(ctx["markPx"]),
                                  "funding": float(ctx["funding"]), "max_lev": int(asset["maxLeverage"])}
    return out


def parse_positions(resp: dict, coins: tuple[str, ...]) -> list[dict]:
    out = []
    for ap in resp.get("assetPositions", []):
        p = ap["position"]
        szi = float(p["szi"])
        if p["coin"] not in coins or szi == 0:
            continue
        entry = float(p["entryPx"])
        liq = p.get("liquidationPx")
        out.append({"coin": p["coin"], "side": "long" if szi > 0 else "short", "mode": p["leverage"]["type"],
                    "leverage": p["leverage"]["value"], "entry_px": entry,
                    "liq_px": float(liq) if liq is not None else None, "qty": abs(szi),
                    "notional": abs(szi) * entry})
    return out


def parse_funding(resp: list) -> list[dict]:
    return [{"ts": int(r["time"]), "rate": float(r["fundingRate"])} for r in resp]


def parse_candles(resp: list) -> list[dict]:
    return [{"ts": int(c["t"]), "high": float(c["h"]), "low": float(c["l"])} for c in resp]


class HttpInfo:
    def __init__(self, url: str = INFO_URL, timeout: float = 15.0):
        self.url, self.timeout = url, timeout

    def post(self, body: dict) -> object:
        req = urllib.request.Request(self.url, data=json.dumps(body).encode(),
                                     headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code == 429:
                raise RateLimited(f"429 für {body.get('type')}") from e
            raise
