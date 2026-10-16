"""Runde 3: Ereignislisten und Machbarkeits-Tor (03-killkriterien.md).

Rechnet KEINE Ereignis-Renditen. sigma kommt aus Zufallsfenstern derselben Assets
ohne Ereignis (vorab so festgelegt). Aufruf aus dem Runden-Ordner:
    python3 code/r3_events.py
"""
import json
import re
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

R = Path(__file__).resolve().parents[1]
D = R / "daten"
OUT = R / "ergebnisse"
ET = ZoneInfo("America/New_York")
VMIN, VMAX = 0.5e6, 50e6
Z_ALPHA, Z_POWER, MU = 3.39, 0.84, 0.02
RNG = np.random.default_rng(20261016)
HOLDOUT = (pd.Timestamp("2025-01-01"), pd.Timestamp("2026-06-30 23:59:59"))


def n_needed(sigma, mu=MU):
    return int(np.ceil(((Z_ALPHA + Z_POWER) * sigma / mu) ** 2))


# ---------- Kursmatrizen ----------
def crypto_panel(symbols=None):
    uni = pd.read_csv(D / "universe.csv")
    syms = uni[(uni.is_stable == 0)].symbol
    if symbols is not None:
        syms = [s for s in syms if s in symbols]
    o, c, v = {}, {}, {}
    for s in syms:
        f = D / "universe_1d" / f"{s}.csv"
        if not f.exists():
            continue
        x = pd.read_csv(f)
        x["date"] = pd.to_datetime(x.ts, unit="ms").dt.normalize()
        x = x.set_index("date")
        o[s], c[s], v[s] = x.open, x.close, x.quote_volume
    o, c, v = (pd.DataFrame(d).sort_index() for d in (o, c, v))
    assert not ((o.index >= HOLDOUT[0]) & (o.index <= HOLDOUT[1])).any(), "Holdout in Krypto-Kursen"
    return o, c, v


def us_panel():
    o, c, v = {}, {}, {}
    for f in sorted((D / "us_1d").glob("*.csv")):
        x = pd.read_csv(f, parse_dates=["date"]).set_index("date")
        o[f.stem], c[f.stem], v[f.stem] = x.open, x.close, x.close * x.volume
    return tuple(pd.DataFrame(d).sort_index() for d in (o, c, v))


def small_mask(dollar_vol, window, minp):
    """Median-Volumen der Vortage (ohne heute) im Band [VMIN, VMAX]."""
    med = dollar_vol.rolling(window, min_periods=minp).median().shift(1)
    return (med > VMIN) & (med < VMAX), med


def window_abnormal(o, c, member, d0, h, col):
    """Abnormale Rendite open(d0) -> close(d0+h Handelstage) gegen gleichgewichtetes Universum."""
    idx = o.index
    i = idx.get_loc(d0)
    if i + h >= len(idx):
        return np.nan
    d1 = idx[i + h]
    r = c.loc[d1] / o.loc[d0] - 1
    m = member.loc[d0] & r.notna()
    if not m.get(col, False):
        return np.nan
    bench = r[m].drop(col, errors="ignore").mean()
    return r[col] - bench


def sigma_random(o, c, member, cols, h, event_days, n=4000):
    """Streuung abnormaler Renditen in Zufallsfenstern ohne Ereignis (±h+5 Tage)."""
    idx = o.index
    out = []
    tries = 0
    while len(out) < n and tries < n * 20:
        tries += 1
        col = cols[RNG.integers(len(cols))]
        i = int(RNG.integers(0, len(idx) - h - 1))
        d0 = idx[i]
        ev = event_days.get(col, [])
        if any(abs((d0 - e).days) <= h * 1.5 + 5 for e in ev):
            continue
        x = window_abnormal(o, c, member, d0, h, col)
        if np.isfinite(x):
            out.append(x)
    a = np.array(out)
    # robust: MAD-Schätzer, damit einzelne Ausreißer-Token sigma nicht dominieren; Standardabw. daneben
    return float(np.std(a, ddof=1)), float(1.4826 * np.median(np.abs(a - np.median(a)))), len(a)


# ---------- A2-S ----------
def a2s(o, c, v):
    meta = pd.read_csv(D / "sec_8k_meta.csv")
    sample = set(Path(D / "sec_8k_docs_sample.txt").read_text().split())
    meta = meta[meta.accession.isin(sample)].copy()
    only = {"5.07", "7.01", "9.01"}
    meta["items_set"] = meta["items"].fillna("").astype(str).map(lambda s: {i.strip() for i in s.split(",") if i.strip()})
    meta = meta[~meta.items_set.map(lambda s: s <= only)]
    meta["acc_utc"] = pd.to_datetime(meta.acceptance_utc, utc=True)
    member, med = small_mask(v, 21, 5)
    days = o.index
    rows = []
    for r in meta.itertuples():
        t = r.acc_utc + pd.Timedelta(minutes=60)
        te = t.tz_convert(ET)
        # erste volle Stunde (Yahoo-60m-Bars starten 9:30, 10:30, ... 15:30 ET), die >= t beginnt
        entry = None
        for d in days[days >= pd.Timestamp(te.date())]:
            for k in range(7):
                bar = pd.Timestamp(d.date()).tz_localize(ET) + pd.Timedelta(hours=9, minutes=30) + pd.Timedelta(hours=k)
                if bar >= te:
                    entry = bar
                    break
            if entry is not None:
                break
        if entry is None or r.ticker not in o.columns:
            continue
        d0 = pd.Timestamp(entry.date())
        is_small = bool(member.at[d0, r.ticker]) if d0 in member.index else False
        rows.append(dict(accession=r.accession, cik=r.cik, ticker=r.ticker, items=r.items,
                         acceptance_utc=r.acceptance_utc, entry_bar_et=entry.isoformat(),
                         entry_day=d0.date().isoformat(), med_dollar_vol=med.at[d0, r.ticker], small=is_small))
    ev = pd.DataFrame(rows)
    ev = ev[ev.small].sort_values("entry_bar_et")
    keep, last = [], {}
    for r in ev.itertuples():  # ein Ereignis je Firma und 20 Tage
        d = pd.Timestamp(r.entry_day)
        if r.ticker in last and (d - last[r.ticker]).days < 28:
            continue
        last[r.ticker] = d
        keep.append(r.Index)
    return ev.loc[keep], member


# ---------- A2-K ----------
def a2k():
    mp = pd.read_csv(D / "mapping_snapshot_binance.csv")
    mp = mp[mp.status == "matched"].set_index("space_id").binance_symbol
    props = [json.loads(x) for x in open(D / "snapshot_proposals.jsonl")]
    rows = []
    for p in props:
        sid = p["space"]["id"]
        if sid not in mp.index:
            continue
        words = len(re.findall(r"\w+", p.get("body") or ""))
        t = pd.Timestamp(p["created"], unit="s", tz="UTC") + pd.Timedelta(minutes=60)
        entry = t.ceil("h")
        rows.append(dict(id=p["id"], space=sid, symbol=mp[sid], created=p["created"], words=words,
                         entry_utc=entry.isoformat(), entry_day=entry.tz_localize(None).normalize().date().isoformat()))
    return pd.DataFrame(rows)


# ---------- A1 ----------
INSIDER = re.compile(r"team|investor|\bvc\b|advisor|contributor|founder|seed|private|strategic|backer|series|yuga|employee|partner", re.I)
EXCLUDE = re.compile(r"ecosystem|community|treasury|foundation|airdrop|staking|reward|liquidity|dao|grant|public|reserve", re.I)


def a1(o, c, v):
    u = pd.read_csv(D / "unlocks_pit.csv")
    tm = pd.read_csv(D / "unlocks_token_map.csv").dropna(subset=["binance_symbol"]).set_index("token").binance_symbol
    u = u[u.token.isin(tm.index)].copy()
    u["symbol"] = u.token.map(tm)
    u["snap"] = pd.to_datetime(u.snapshot_ts.astype(str), format="%Y%m%d%H%M%S")
    u["day"] = pd.to_datetime(u.unlock_date, utc=True).dt.tz_localize(None).dt.normalize()
    u["insider"] = u.category.astype(str).map(lambda s: bool(INSIDER.search(s)) and not EXCLUDE.search(s))
    u = u[(u.vesting_type == "cliff") & u.insider & (u.pct_circ >= 1.0) & ((u.day - u.snap).dt.days >= 35)]
    u = u.sort_values(["symbol", "day", "snap"]).drop_duplicates(["symbol", "day"])
    member, med = small_mask(v, 30, 7)
    idx = o.index
    rows, last = [], {}
    for r in u.itertuples():
        if r.symbol not in o.columns:
            continue
        pre, post = r.day - pd.Timedelta(days=30), r.day + pd.Timedelta(days=15)
        if pre not in idx or post not in idx or pre < pd.Timestamp("2023-01-01") or post > pd.Timestamp("2024-12-31"):
            continue
        if r.symbol in last and (r.day - last[r.symbol]).days < 60:
            continue
        sm = bool(member.at[pre, r.symbol])
        rows.append(dict(symbol=r.symbol, token=r.token, unlock_day=r.day.date().isoformat(),
                         snapshot=r.snap.isoformat(), pct_circ=r.pct_circ, category=r.category,
                         med_vol=med.at[pre, r.symbol], small=sm))
        if sm:
            last[r.symbol] = r.day
    return pd.DataFrame(rows), member


def main():
    OUT.mkdir(exist_ok=True)
    gate = {}

    uo, uc, uv = us_panel()
    ev_s, mem_s = a2s(uo, uc, uv)
    ev_s.to_csv(OUT / "events_a2s.csv", index=False)
    evd = {t: [pd.Timestamp(d) for d in g.entry_day] for t, g in pd.read_csv(D / "sec_8k_meta.csv").assign(
        entry_day=lambda x: pd.to_datetime(x.acceptance_utc).dt.tz_localize(None).dt.normalize()).groupby("ticker")}
    cols = sorted(set(ev_s.ticker))
    for h in (5, 20):
        sd, mad, k = sigma_random(uo, uc, mem_s, cols, h, evd)
        last_ok = uo.index[-1 - h]
        n_av = int((pd.to_datetime(ev_s.entry_day) <= last_ok).sum())
        gate[f"A2-S-{h}"] = dict(sigma_sd=sd, sigma_mad=mad, n_random=k, n_available=n_av,
                                 n_needed_sd=n_needed(sd), n_needed_mad=n_needed(mad))

    co, cc, cv = crypto_panel()
    w2 = co.index >= pd.Timestamp("2026-07-01")
    co2, cc2, cv2 = co[w2], cc[w2], cv[w2]
    mem_k, medk = small_mask(cv2, 30, 7)
    ev_k = a2k()
    ev_k["small"] = [bool(mem_k.at[pd.Timestamp(d), s]) if pd.Timestamp(d) in mem_k.index and s in mem_k.columns else False
                     for d, s in zip(ev_k.entry_day, ev_k.symbol)]
    ev_k["med_vol"] = [medk.at[pd.Timestamp(d), s] if pd.Timestamp(d) in medk.index and s in medk.columns else np.nan
                       for d, s in zip(ev_k.entry_day, ev_k.symbol)]
    ev_k = ev_k.sort_values("created")
    keep, last = [], {}
    for r in ev_k.itertuples():
        if not (r.small and r.words >= 300):
            continue
        if r.symbol in last and r.created - last[r.symbol] < 5 * 86400:
            continue
        last[r.symbol] = r.created
        keep.append(r.Index)
    ev_k["selected"] = ev_k.index.isin(keep)
    ev_k.to_csv(OUT / "events_a2k.csv", index=False)
    evd = {s: [pd.Timestamp(d) for d in g.entry_day] for s, g in ev_k.groupby("symbol")}
    cols = sorted(set(ev_k[ev_k.selected].symbol)) or sorted(set(ev_k.symbol))
    for h in (5, 20):
        sd, mad, k = sigma_random(co2, cc2, mem_k, cols, h, evd)
        last_ok = co2.index[-1 - h]
        n_av = int((ev_k.selected & (pd.to_datetime(ev_k.entry_day) <= last_ok)).sum())
        gate[f"A2-K-{h}"] = dict(sigma_sd=sd, sigma_mad=mad, n_random=k, n_available=n_av,
                                 n_needed_sd=n_needed(sd), n_needed_mad=n_needed(mad))

    w1 = co.index <= pd.Timestamp("2024-12-31")
    ev_a, mem_a = a1(co[w1], cc[w1], cv[w1])
    ev_a.to_csv(OUT / "events_a1.csv", index=False)
    sel = ev_a[ev_a.small] if len(ev_a) else ev_a
    evd = {s: [pd.Timestamp(d) for d in g.unlock_day] for s, g in sel.groupby("symbol")} if len(sel) else {}
    cols = sorted(set(sel.symbol)) if len(sel) else []
    for name, h in (("A1-a", 29), ("A1-b", 14)):
        if cols:
            sd, mad, k = sigma_random(co[w1], cc[w1], mem_a, cols, h, evd)
        else:
            sd = mad = float("nan"); k = 0
        gate[name] = dict(sigma_sd=sd, sigma_mad=mad, n_random=k, n_available=int(len(sel)),
                          n_needed_sd=n_needed(sd) if cols else None, n_needed_mad=n_needed(mad) if cols else None)

    for g in gate.values():
        g["gate"] = "messbar" if g["n_needed_sd"] and g["n_available"] >= g["n_needed_sd"] else "nicht messbar"
    (OUT / "gate.json").write_text(json.dumps(gate, indent=1))
    print(json.dumps(gate, indent=1))
    print("A2-S Ereignisse:", len(ev_s), "A2-K gewählt:", int(ev_k.selected.sum()), "von", len(ev_k),
          "A1 klein:", int(ev_a.small.sum()) if len(ev_a) else 0, "von", len(ev_a))


if __name__ == "__main__":
    main()
