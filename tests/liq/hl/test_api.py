import io
import urllib.error

import pytest

from diamondhamster.liq.hl import api

POS_DOC = {"assetPositions": [{"position": {"coin": "ETH", "entryPx": "2986.3",
           "leverage": {"rawUsd": "-95.059824", "type": "isolated", "value": 20},
           "liquidationPx": "2866.26936529", "szi": "0.0335", "positionValue": "100.0"}, "type": "oneWay"}],
           "time": 1}


def test_parse_positions_doc_example():
    (p,) = api.parse_positions(POS_DOC, ("BTC", "ETH"))
    assert p == {"coin": "ETH", "side": "long", "mode": "isolated", "leverage": 20, "entry_px": 2986.3,
                 "liq_px": 2866.26936529, "qty": 0.0335, "notional": pytest.approx(0.0335 * 2986.3)}


def test_parse_positions_short_null_liq_and_filters():
    doc = {"assetPositions": [
        {"position": {"coin": "BTC", "entryPx": "100000", "leverage": {"type": "cross", "value": 3},
                      "liquidationPx": None, "szi": "-0.5"}},
        {"position": {"coin": "SOL", "entryPx": "1", "leverage": {"type": "cross", "value": 3},
                      "liquidationPx": "0.5", "szi": "1"}},
        {"position": {"coin": "ETH", "entryPx": "1", "leverage": {"type": "cross", "value": 3},
                      "liquidationPx": "0.5", "szi": "0.0"}}]}
    (p,) = api.parse_positions(doc, ("BTC", "ETH"))
    assert (p["side"], p["mode"], p["liq_px"], p["qty"]) == ("short", "cross", None, 0.5)


def test_parse_ctx_doc_example():
    resp = [{"universe": [{"name": "BTC", "maxLeverage": 40}, {"name": "XYZ", "maxLeverage": 3},
                          {"name": "ETH", "maxLeverage": 25}]},
            [{"funding": "0.0000125", "openInterest": "688.11", "markPx": "14.3161"},
             {"funding": "0", "openInterest": "1", "markPx": "1"},
             {"funding": "-0.0001", "openInterest": "50", "markPx": "3000"}]]
    out = api.parse_ctx(resp, ("BTC", "ETH"))
    assert out["BTC"] == {"oi": 688.11, "mark": 14.3161, "funding": 0.0000125, "max_lev": 40}
    assert out["ETH"]["max_lev"] == 25 and set(out) == {"BTC", "ETH"}


def test_parse_trades_users_and_side():
    msg = {"channel": "trades", "data": [{"coin": "BTC", "side": "B", "px": "100000.5", "sz": "0.01",
           "hash": "0x0", "time": 1700000000000, "tid": 7, "users": ["0xbuyer", "0xseller"]}]}
    (t,) = api.parse_trades(msg)
    assert t == {"coin": "BTC", "ts": 1700000000000, "price": 100000.5, "qty": 0.01, "taker_buy": 1,
                 "buyer": "0xbuyer", "seller": "0xseller", "tid": 7}
    msg["data"][0]["side"] = "A"
    assert api.parse_trades(msg)[0]["taker_buy"] == 0
    assert api.parse_trades({"channel": "pong"}) == []


def test_parse_funding_and_candles():
    assert api.parse_funding([{"coin": "ETH", "fundingRate": "-0.00022196", "premium": "0", "time": 5}]) == \
        [{"ts": 5, "rate": -0.00022196}]
    assert api.parse_candles([{"t": 60000, "T": 119999, "h": "2", "l": "1", "o": "1", "c": "2"}]) == \
        [{"ts": 60000, "high": 2.0, "low": 1.0}]


def test_weights():
    assert api.WEIGHTS["clearinghouseState"] == 2 and api.WEIGHTS["metaAndAssetCtxs"] == 20


def test_http_raises_rate_limited(monkeypatch):
    def boom(req, timeout):
        raise urllib.error.HTTPError(req.full_url, 429, "too many", {}, io.BytesIO(b""))
    monkeypatch.setattr(api.urllib.request, "urlopen", boom)
    with pytest.raises(api.RateLimited):
        api.HttpInfo().post({"type": "metaAndAssetCtxs"})
