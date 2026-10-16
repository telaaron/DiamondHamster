"""K4 control arm: trend filter times volatility targeting, walk-forward 2017-2024.

Lookahead audit (each reference, in order):
- sma[t], vol[t], target[t] use closes up to and including day t (rolling/expanding windows).
- Decision only at week-end closes; backtest.run shifts weights by one day and trades at open t+1.
- L for calendar year Y is picked from Sharpe on rows strictly before Y-01-01.
"""

from __future__ import annotations

import json
import sys

import numpy as np
import pandas as pd

from qe_common import COST, DAYS, load_prices, run, stats, week_ends, weekly_to_daily

sys.path.insert(0, "../../src")
from diamondhamster import baselines  # noqa: E402

GRID = [50, 100, 150, 200]
START, END = "2017-01-01", "2024-12-31"


def raw_weights(df: pd.DataFrame, L: int) -> pd.Series:
    c = df["close"]
    trend = (c > c.rolling(L).mean()).astype(float)
    vol = np.log(c).diff().rolling(30).std() * np.sqrt(DAYS)
    target = vol.expanding(min_periods=90).median()
    scale = (target / vol).clip(upper=1.0)
    w = (trend * scale).fillna(0.0)
    we = week_ends(df)
    return weekly_to_daily(df, w.loc[we])


def sharpe(res: pd.DataFrame) -> float:
    r = res["ret"]
    return float(r.mean() / r.std() * np.sqrt(DAYS)) if r.std() > 0 else -9.0


def walk_forward(df: pd.DataFrame) -> tuple[pd.Series, dict]:
    parts, picks = [], {}
    for y in range(int(START[:4]), int(END[:4]) + 1):
        past = df[df.index < pd.Timestamp(f"{y}-01-01", tz="UTC")]
        scores = {L: sharpe(run(past, raw_weights(past, L))) for L in GRID if len(past) > L + 120}
        L = max(scores, key=scores.get) if scores else GRID[0]
        picks[y] = L
        # weights for year y computed on data up to each day (rolling windows only look back)
        w = raw_weights(df[df.index <= pd.Timestamp(f"{y}-12-31", tz="UTC")], L)
        parts.append(w[str(y)])
    return pd.concat(parts), picks


def random_perm(df: pd.DataFrame, w: pd.Series, n: int = 1000, seed: int = 1) -> pd.DataFrame:
    """Random timing with the same weights, same persistence and same turnover:
    shuffle 13-week blocks of the strategy's own weekly weights, then rotate by a random offset."""
    rng = np.random.default_rng(seed)
    we = week_ends(df)
    ww = w.loc[we].values
    blocks = [ww[i : i + 13] for i in range(0, len(ww), 13)]
    rows = []
    for _ in range(n):
        order = rng.permutation(len(blocks))
        p = np.roll(np.concatenate([blocks[i] for i in order]), rng.integers(len(ww)))
        rows.append(stats(run(df, weekly_to_daily(df, pd.Series(p, index=we)))))
    return pd.DataFrame(rows)


def main(name: str) -> dict:
    full = load_prices(name)
    w, picks = walk_forward(full)
    df = full.loc[START:END]
    w = w.reindex(df.index).fillna(0.0)
    strat = stats(run(df, w))
    bh = stats(run(df, pd.Series(1.0, index=df.index)))
    const = stats(run(df, pd.Series(float(w.mean()), index=df.index)))
    rnd = random_perm(df, w)
    dca = baselines.dca(df, cost_per_side=COST)
    res = run(df, w)
    yearly = {str(y): float((1 + g["ret"]).prod() - 1) for y, g in res.groupby(res.index.year)}
    yearly_bh = {str(y): float(g["close"].iloc[-1] / g["open"].iloc[0] - 1) for y, g in df.groupby(df.index.year)}
    out = {
        "asset": name,
        "picks": picks,
        "strategy": strat,
        "buy_hold": bh,
        "constant_same_mean_weight": const,
        "dca": dca,
        "random_perm_pct_rank": {
            "sharpe": float((rnd["sharpe"] < strat["sharpe"]).mean()),
            "cagr": float((rnd["cagr"] < strat["cagr"]).mean()),
            "max_dd": float((rnd["max_dd"] < strat["max_dd"]).mean()),
        },
        "random_perm_median": rnd.median().to_dict(),
        "yearly": yearly,
        "yearly_bh": yearly_bh,
    }
    return out


if __name__ == "__main__":
    allres = {n: main(n) for n in ["coinbase_BTC-USD", "coinbase_ETH-USD"]}
    print(json.dumps(allres, indent=1, default=float))
    json.dump(allres, open("out/k4.json", "w"), indent=1, default=float)
