"""Runde 4, Arm B2: Dealer-Gamma-Proxy aus Deribit-Optionstrades und Regime-Tests.

Eingaben (daten/): deribit/daily_flow_{CUR}.csv, binance_1h/{CUR}USDT.csv
Ausgabe: ergebnisse/b2_gex_{CUR}.csv, ergebnisse/b2_result.json

Proxy A-1: Kunden = Taker. Kundenposition je Kontrakt = kumulierte Taker-Käufe - Taker-Verkäufe.
Dealer = -Kunde. GEX(t) = sum Dealer-Pos * Gamma_BS * S^2 * 0.01  (USD je 1 % Bewegung), 00:00 UTC.
Proxy A-2: Dealer long Calls, short Puts, Gewicht |Netto| je Kontrakt.
"""
import json, math, sys
from pathlib import Path
import numpy as np
import pandas as pd

R = Path(__file__).resolve().parents[1]
D = R / "daten"
OUT = R / "ergebnisse"
TEST_START, TEST_END = "2023-01-01", "2024-12-31"
WARM_START = "2022-07-01"   # ab hier GEX-Verteilung für Terzile (Flüsse ab 2022-01)
NPERM = 10_000
COST_SIDE = 0.002 + 0.0001  # 0,2 % + halber Spread BTC/ETH pauschal 0,01 %
MON = {m: i + 1 for i, m in enumerate("JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC".split())}


def parse_inst(name):
    # BTC-29MAR24-60000-C ; Strike kann Dezimalpunkt als 'd' haben (z. B. ETH-...-1d5-C) -> selten
    cur, exp, k, cp = name.split("-")
    day, mon, yr = int(exp[:-5]), MON[exp[-5:-2]], 2000 + int(exp[-2:])
    expiry = pd.Timestamp(year=yr, month=mon, day=day, hour=8, tz="UTC")
    return expiry, float(k.replace("d", ".")), cp


def bs_gamma(S, K, T, sig):
    if T <= 0 or sig <= 0 or S <= 0:
        return 0.0
    d1 = (math.log(S / K) + 0.5 * sig * sig * T) / (sig * math.sqrt(T))
    return math.exp(-0.5 * d1 * d1) / math.sqrt(2 * math.pi) / (S * sig * math.sqrt(T))


def load_spot(cur):
    k = pd.read_csv(D / "binance_1h" / f"{cur}USDT.csv")
    k["ts"] = pd.to_datetime(k["open_time"], unit="ms", utc=True)
    k = k.set_index("ts").sort_index()
    return k


def build_gex(cur):
    f = pd.read_csv(D / "deribit" / f"daily_flow_{cur}.csv")
    f["date"] = pd.to_datetime(f["date"]).dt.tz_localize("UTC")
    meta = {n: parse_inst(n) for n in f["instrument_name"].unique()}
    f["net"] = f["taker_buy_amount"] - f["taker_sell_amount"]
    spot = load_spot(cur)
    days = pd.date_range(f["date"].min() + pd.Timedelta(days=1), TEST_END, freq="D", tz="UTC")
    pos, iv = {}, {}
    by_day = {d: g for d, g in f.groupby("date")}
    rows = []
    for d in days:
        g = by_day.get(d - pd.Timedelta(days=1))
        if g is not None:   # Flüsse bis Ende Vortag
            for n, net, v in zip(g["instrument_name"], g["net"], g["mean_iv"]):
                pos[n] = pos.get(n, 0.0) + net
                if v == v and v > 0:
                    iv[n] = v / 100.0
        if d not in spot.index:
            continue
        S = float(spot.loc[d, "open"])
        g1 = g2 = 0.0
        ncon = 0
        for n, p in pos.items():
            expiry, K, cp = meta[n]
            T = (expiry - d).total_seconds() / (365.25 * 86400)
            if T <= 0 or n not in iv:
                continue
            gam = bs_gamma(S, K, T, iv[n]) * S * S * 0.01
            g1 += -p * gam
            g2 += (abs(p) if cp == "C" else -abs(p)) * gam
            ncon += 1
        rows.append((d, S, g1, g2, ncon))
    return pd.DataFrame(rows, columns=["date", "spot", "gex_a1", "gex_a2", "n_contracts"]).set_index("date")


def next24(spot, d):
    w = spot.loc[d: d + pd.Timedelta(hours=24)]["open"].values  # 25 Opens -> 24 Renditen
    if len(w) < 25:
        return None
    return np.diff(np.log(w))


def expanding_rank(x, start):
    """Perzentil von x[t] in x[start..t-1] (nur Vergangenheit)."""
    vals = x.values
    idx = x.index
    out = np.full(len(x), np.nan)
    s = idx.searchsorted(pd.Timestamp(start, tz="UTC"))
    for i in range(len(x)):
        if i - s < 60 or i < s:
            continue
        past = vals[s:i]
        out[i] = (past < vals[i]).mean()
    return pd.Series(out, index=idx)


def tercile(rank):
    return np.where(rank < 1 / 3, 0, np.where(rank < 2 / 3, 1, 2))


def block_perm_idx(n, rng, block=30):
    blocks = [np.arange(i, min(i + block, n)) for i in range(0, n, block)]
    order = rng.permutation(len(blocks))
    return np.concatenate([blocks[j] for j in order])


def stats(df):
    """d (HAR-Koeffizient GEX-Rang), AC-Differenz oben-unten."""
    X = np.column_stack([np.ones(len(df)), df["rv_lag"], df["rv_w"], df["rank"]])
    beta = np.linalg.lstsq(X, df["rv"].values, rcond=None)[0]
    t = df["terc"].values
    ac = {}
    for k in (0, 2):
        m = t == k
        num = df["xy"].values[m].sum()
        den = df["xx"].values[m].sum()
        ac[k] = num / den if den > 0 else np.nan
    return beta[3], ac[2] - ac[0], ac


def analyse(cur, gex, col, rng):
    spot = load_spot(cur)
    rank = expanding_rank(gex[col], WARM_START)
    rec = []
    for d in gex.index:
        r = next24(spot, d)
        if r is None:
            continue
        rec.append((d, (r ** 2).sum(), (r[1:] * r[:-1]).sum(), (r[:-1] ** 2).sum(), r.sum()))
    y = pd.DataFrame(rec, columns=["date", "rv", "xy", "xx", "ret24"]).set_index("date")
    df = y.join(rank.rename("rank"))
    df["rv_lag"] = df["rv"].shift(1)
    df["rv_w"] = df["rv"].shift(1).rolling(7).mean()
    df["ret_prev"] = df["ret24"].shift(1)
    df = df.loc[TEST_START:TEST_END].dropna()
    df["terc"] = tercile(df["rank"].values)
    d, acdiff, ac = stats(df)
    nd = np.empty(NPERM)
    nac = np.empty(NPERM)
    base = df.copy()
    for i in range(NPERM):
        pi = block_perm_idx(len(df), rng)
        base["rank"] = df["rank"].values[pi]
        base["terc"] = df["terc"].values[pi]
        nd[i], nac[i], _ = stats(base)
    res = {
        "n_days": int(len(df)),
        "har_d": float(d), "p_d_less0": float((nd <= d).mean()),
        "ac1_top": float(ac[2]), "ac1_bottom": float(ac[0]), "ac_diff_top_minus_bottom": float(acdiff),
        "p_acdiff_less0": float((nac <= acdiff).mean()),
        "rv_mean_by_tercile": {int(k): float(v) for k, v in df.groupby("terc")["rv"].mean().items()},
        "days_by_tercile": {int(k): int(v) for k, v in df["terc"].value_counts().items()},
    }
    return res, df


def trade_rule(df):
    pos = np.where(df["terc"] == 0, np.sign(df["ret_prev"]), np.where(df["terc"] == 2, -np.sign(df["ret_prev"]), 0.0))
    gross = pos * (np.exp(df["ret24"].values) - 1)
    turn = np.abs(np.diff(np.concatenate([[0.0], pos])))
    net = gross - turn * COST_SIDE
    def summ(x):
        x = pd.Series(x, index=df.index)
        ann = x.mean() * 365
        sd = x.std() * math.sqrt(365)
        h = len(x) // 2
        return {"mean_daily": float(x.mean()), "ann": float(ann), "sharpe": float(ann / sd) if sd > 0 else None,
                "half1": float(x.iloc[:h].mean()), "half2": float(x.iloc[h:].mean()), "n_trades": int((turn > 0).sum())}
    return {"gross": summ(gross), "net": summ(net), "net_cost_0.05": summ(gross - turn * 0.0006)}


def main():
    rng = np.random.default_rng(20261016)
    out = {}
    for cur in sys.argv[1:] or ["BTC", "ETH"]:
        gex = build_gex(cur)
        gex.to_csv(OUT / f"b2_gex_{cur}.csv")
        res1, df1 = analyse(cur, gex, "gex_a1", rng)
        out[f"{cur}_A1"] = res1
        out[f"{cur}_A1"]["trade_rule"] = trade_rule(df1)
        if cur == "BTC":
            res2, df2 = analyse(cur, gex, "gex_a2", rng)
            out["BTC_A2"] = res2
        out[f"{cur}_gex_share_positive"] = float((gex.loc[TEST_START:TEST_END, "gex_a1"] > 0).mean())
    (OUT / "b2_result.json").write_text(json.dumps(out, indent=2))
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
