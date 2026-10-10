"""CLI: `python -m diamondhamster fetch` then `python -m diamondhamster baselines`."""

import argparse
import json

import pandas as pd

from . import baselines, data, metrics, quality
from .config import IN_SAMPLE_END

SOURCES = {
    ("binance", "BTCUSDT"): lambda: data.fetch_binance("BTCUSDT"),
    ("binance", "ETHUSDT"): lambda: data.fetch_binance("ETHUSDT"),
    ("coinbase", "BTC-USD"): lambda: data.fetch_coinbase("BTC-USD"),
    ("coinbase", "ETH-USD"): lambda: data.fetch_coinbase("ETH-USD", start=pd.Timestamp("2016-05-18").date()),
}


def fetch() -> None:
    for (src, sym), fn in SOURCES.items():
        df = fn()
        path = data.save(df, src, sym)
        rep = quality.report(df.loc[: data.HOLDOUT_START - pd.Timedelta(days=1)])
        print(path.name, json.dumps({k: v for k, v in rep.items() if k != "missing_days"} | {"missing_days": len(rep["missing_days"])}))


def run_baselines() -> None:
    pd.set_option("display.width", 160)
    for src, sym in [("binance", "BTCUSDT"), ("binance", "ETHUSDT"), ("coinbase", "BTC-USD")]:
        df = data.load(src, sym).loc[:IN_SAMPLE_END]
        bh = baselines.buy_and_hold(df)
        print(f"\n== {src} {sym} in-sample {df.index[0].date()} .. {df.index[-1].date()}")
        print("buy&hold:", {k: round(v, 3) for k, v in metrics.summary(bh).items()})
        print("dca:", {k: round(v, 3) for k, v in baselines.dca(df).items()})
        rnd = baselines.random_timing(df, n=500)
        print("random 50% exposure, 30d holds (5/50/95 pct):")
        print(rnd[["cagr", "max_drawdown", "sharpe"]].quantile([0.05, 0.5, 0.95]).round(3).to_string())
        print("buy&hold by regime:")
        print(metrics.by_regime(bh)[["cagr", "max_drawdown", "sharpe"]].round(3).to_string())


if __name__ == "__main__":
    p = argparse.ArgumentParser(prog="diamondhamster")
    p.add_argument("command", choices=["fetch", "baselines"])
    {"fetch": fetch, "baselines": run_baselines}[p.parse_args().command]()
