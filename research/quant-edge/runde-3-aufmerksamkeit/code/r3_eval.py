"""Runde 3: Auswertung nach 03-killkriterien.md (inkl. Nachträge).

    python3 code/r3_eval.py a2s   # Test (A2-S-5) plus deskriptiv A2-S-20
    python3 code/r3_eval.py a2k   # deskriptiv
    python3 code/r3_eval.py a1    # deskriptiv
"""
import json
import sys
import tarfile
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).parent))
import r3_events as ev  # noqa: E402

R = Path(__file__).resolve().parents[1]
D, E, L = R / "daten", R / "ergebnisse", R / "lesen"
FEE = 0.002
ALPHA = 0.05 / 143
BORROW = 0.05 / 252  # Leihkosten Short je Handelstag (Aktien)
RNG = np.random.default_rng(20261016)


def corwin_schultz(h, l):
    """Halber Spread (Anteil) je Tag aus Hoch/Tief zweier Tage (Corwin/Schultz 2012), negativ -> 0."""
    lh = np.log(h / l) ** 2
    beta = lh + lh.shift(-1)
    gamma = np.log(np.maximum(h, h.shift(-1)) / np.minimum(l, l.shift(-1))) ** 2
    k = 3 - 2 * np.sqrt(2)
    alpha = (np.sqrt(2 * beta) - np.sqrt(beta)) / k - np.sqrt(gamma / k)
    s = 2 * (np.exp(alpha) - 1) / (1 + np.exp(alpha))
    return (s.clip(lower=0) / 2)


def week_bootstrap(x, weeks, n=10000):
    """Einseitiges p für Mittel > 0, Block-Bootstrap über Kalenderwochen (unter H0 zentriert)."""
    df = pd.DataFrame({"x": x, "w": weeks})
    groups = [g.x.values for _, g in df.groupby("w")]
    m = df.x.mean()
    cen = [g - m for g in groups]
    k = len(cen)
    sims = np.empty(n)
    for i in range(n):
        pick = RNG.integers(0, k, k)
        v = np.concatenate([cen[j] for j in pick])
        sims[i] = v.mean()
    return float((sims >= m).mean())


def summarize(df, col="net"):
    if len(df) == 0:
        return dict(n=0)
    d = df.sort_values("entry_day")
    half = len(d) // 2
    p = week_bootstrap(d[col].values, pd.to_datetime(d.entry_day).dt.isocalendar().week.values)
    t = d[col].mean() / (d[col].std(ddof=1) / np.sqrt(len(d))) if len(d) > 2 else np.nan
    return dict(n=int(len(d)), mean=float(d[col].mean()), median=float(d[col].median()), t=float(t), p_week_boot=p,
                first_half=float(d[col].iloc[:half].mean()), second_half=float(d[col].iloc[half:].mean()),
                hit=float((d[col] > 0).mean()))


def verdict(gross, net):
    if net["n"] == 0:
        return "keine Ereignisse"
    same = np.sign(net["first_half"]) == np.sign(net["second_half"])
    if net["mean"] > 0 and net["p_week_boot"] < ALPHA and same:
        return "lebt"
    if gross["mean"] <= 0:
        return "tot (brutto ≤ 0)"
    if gross["p_week_boot"] < 0.05 and net["mean"] <= 0:
        return "Prämie da, nicht erntbar"
    if net["mean"] > 0 and net["p_week_boot"] < 0.05:
        return "Hinweis"
    return "tot (netto ≤ 0 oder nicht signifikant)"


def load_answers(kand):
    key = pd.read_csv(L / kand / "key.csv")
    a = pd.DataFrame(json.loads((L / kand / "antworten.json").read_text()))
    k = pd.DataFrame(json.loads((L / kand / "leck.json").read_text())) if (L / kand / "leck.json").exists() else None
    out = key.merge(a, on="id", how="left")
    if k is not None:
        out = out.merge(k.rename(columns={"name": "leck_name", "jahr": "leck_jahr", "sicher": "leck_sicher"}), on="id", how="left")
    s50 = L / kand / "antworten_50w.json"
    if s50.exists():
        b = pd.DataFrame(json.loads(s50.read_text()))[["id", "richtung"]].rename(columns={"richtung": "richtung_50w"})
        out = out.merge(b, on="id", how="left")
    return out


def recognized(row, truth):
    """Leck: Name erraten (Teilstring, ohne Groß/Klein) oder Jahr 2026 mit Sicherheit 3."""
    n = str(row.get("leck_name", "")).lower()
    if not n or n == "unbekannt" or n == "nan":
        return False
    return any(t and (t.lower() in n or n in t.lower()) for t in truth if len(t) >= 3)


def eval_a2s():
    a = load_answers("a2s")
    evs = pd.read_csv(E / "events_a2s.csv")
    evs = evs[~evs.accession.duplicated(keep=False)]  # Nachtrag N3: Sammelmeldungen mehrerer Fonds raus
    a = a.drop_duplicates("id").merge(evs, left_on="event", right_on="accession")
    ent = pd.read_csv(D / "a2s_entry.csv")[["accession", "open", "matched"]].rename(columns={"open": "entry_open"})
    a = a.merge(ent, on="accession", how="left")
    names = pd.read_csv(D / "sec_names.csv").set_index("cik")
    uo, uc, uv = ev.us_panel()
    hi, lo = {}, {}
    for f in sorted((D / "us_1d").glob("*.csv")):
        x = pd.read_csv(f, parse_dates=["date"]).set_index("date")
        hi[f.stem], lo[f.stem] = x.high, x.low
    hi, lo = pd.DataFrame(hi).sort_index(), pd.DataFrame(lo).sort_index()
    member, _ = ev.small_mask(uv, 21, 5)
    meta = pd.read_csv(D / "sec_8k_meta.csv")
    meta["d"] = pd.to_datetime(meta.acceptance_utc).dt.tz_localize(None).dt.normalize()
    res = {}
    rows = []
    for h in (5, 20):
        for r in a.itertuples():
            if r.richtung not in (-1, 1) or pd.isna(r.entry_open) or r.matched == "none":
                continue
            d0 = pd.Timestamp(r.entry_day)
            idx = uo.index
            if d0 not in idx:
                continue
            i = idx.get_loc(d0)
            if i + h >= len(idx):
                continue
            d1 = idx[i + h]
            px1 = uc.at[d1, r.ticker]
            if not np.isfinite(px1):
                continue
            ret = px1 / r.entry_open - 1
            rr = uc.loc[d1] / uo.loc[d0] - 1
            m = member.loc[d0] & rr.notna()
            bench = rr[m].drop(r.ticker, errors="ignore").mean()
            hs = corwin_schultz(hi[r.ticker], lo[r.ticker]).loc[:d0].iloc[-21:-1].mean()
            hs = 0.0 if not np.isfinite(hs) else hs
            gross = r.richtung * (ret - bench)
            cost = 2 * (FEE + hs) + (BORROW * h if r.richtung < 0 else 0)
            truth = [r.ticker] + ([names.at[r.cik, "name"]] if r.cik in names.index else [])
            near = meta[(meta.cik == r.cik) & (meta.accession != r.accession) & ((meta.d - d0).abs().dt.days <= 3)]
            rows.append(dict(h=h, id=r.id, accession=r.accession, ticker=r.ticker, entry_day=r.entry_day,
                             richtung=r.richtung, zuversicht=r.zuversicht, gross=gross, half_spread=hs, cost=cost,
                             net=gross - cost, leck=recognized(r._asdict(), truth), other_8k_pm3=len(near) > 0,
                             richtung_50w=getattr(r, "richtung_50w", np.nan)))
    t = pd.DataFrame(rows)
    t.to_csv(E / "a2s_trades.csv", index=False)
    for h in (5, 20):
        x = t[t.h == h]
        g, n = summarize(x, "gross"), summarize(x, "net")
        res[f"A2-S-{h}"] = dict(
            gross=g, net=n, verdict=verdict(g, n) if h == 5 else "deskriptiv (Tor: nicht messbar); " + verdict(g, n),
            ohne_leck=summarize(x[~x.leck], "net"), nur_leck=summarize(x[x.leck], "net"),
            ohne_andere_8k=summarize(x[~x.other_8k_pm3], "net"),
            long=summarize(x[x.richtung > 0], "net"), short=summarize(x[x.richtung < 0], "net"),
            mean_cost=float(x.cost.mean()) if len(x) else None, median_half_spread=float(x.half_spread.median()) if len(x) else None)
    res["leser"] = dict(n_docs=int(len(a)), richtung=a.richtung.value_counts().to_dict(),
                        leck_quote=float(np.mean([recognized(r._asdict(), [r.ticker]) for r in a.itertuples()])) if "leck_name" in a else None,
                        einstieg_matched=a.matched.value_counts().to_dict())
    (E / "a2s_result.json").write_text(json.dumps(res, indent=1, default=str))
    print(json.dumps(res, indent=1, default=str))


def eval_a2k():
    a = load_answers("a2k")
    evs = pd.read_csv(E / "events_a2k.csv")
    a = a.merge(evs, left_on="event", right_on="id", suffixes=("", "_ev"))
    co, cc, cv = ev.crypto_panel()
    w2 = co.index >= pd.Timestamp("2026-07-01")
    co, cc, cv = co[w2], cc[w2], cv[w2]
    member, _ = ev.small_mask(cv, 30, 7)
    kl = {}
    with tarfile.open(D / "kl_1h.tar.gz") as tf:
        for m in tf.getmembers():
            if m.name.endswith(".csv"):
                kl[Path(m.name).stem] = pd.read_csv(tf.extractfile(m))
    sp = pd.read_csv(D / "spread_live.csv")
    sp = sp[(sp.bid > 0) & (sp.ask > 0)]
    sp["hs"] = (sp.ask - sp.bid) / (sp.ask + sp.bid)
    hs = sp.groupby("symbol").hs.median()
    rows = []
    for h in (5, 20):
        for r in a.itertuples():
            if r.richtung not in (-1, 1) or r.symbol not in kl:
                continue
            k = kl[r.symbol]
            te = int(pd.Timestamp(r.entry_utc).timestamp() * 1000)
            bar = k[k.ts >= te].head(1)
            if bar.empty:
                continue
            d0 = pd.Timestamp(r.entry_day)
            i = co.index.get_loc(d0)
            if i + h >= len(co.index):
                continue
            d1 = co.index[i + h]
            ret = cc.at[d1, r.symbol] / bar.open.iloc[0] - 1
            rr = cc.loc[d1] / co.loc[d0] - 1
            m = member.loc[d0] & rr.notna()
            bench = rr[m].drop(r.symbol, errors="ignore").mean()
            gross = r.richtung * (ret - bench)
            cost = 2 * (FEE + hs.get(r.symbol, 0.0))
            rows.append(dict(h=h, id=r.id, symbol=r.symbol, entry_day=r.entry_day, richtung=r.richtung,
                             gross=gross, cost=cost, net=gross - cost,
                             leck=str(getattr(r, "leck_name", "unbekannt")).lower() not in ("unbekannt", "nan", "")))
    t = pd.DataFrame(rows)
    t.to_csv(E / "a2k_trades.csv", index=False)
    res = {f"A2-K-{h}": dict(gross=summarize(t[t.h == h], "gross"), net=summarize(t[t.h == h], "net"),
                             verdict="deskriptiv (Tor: nicht messbar)") for h in (5, 20)}
    res["leser"] = dict(n_docs=int(len(a)), richtung=a.richtung.value_counts().to_dict(),
                        leck_name_genannt=int(t.drop_duplicates("id").leck.sum()) if len(t) else 0)
    (E / "a2k_result.json").write_text(json.dumps(res, indent=1, default=str))
    print(json.dumps(res, indent=1, default=str))


def eval_a1():
    e = pd.read_csv(E / "events_a1.csv")
    e = e[e.small]
    co, cc, cv = ev.crypto_panel()
    w1 = co.index <= pd.Timestamp("2024-12-31")
    co, cc, cv = co[w1], cc[w1], cv[w1]
    member, _ = ev.small_mask(cv, 30, 7)
    rows = []
    for r in e.itertuples():
        day = pd.Timestamp(r.unlock_day)
        pre0, pre1 = day - pd.Timedelta(days=30), day - pd.Timedelta(days=1)
        post0, post1 = day + pd.Timedelta(days=1), day + pd.Timedelta(days=14)
        for leg, d0, d1, sgn in (("A1-a", pre0, pre1, -1), ("A1-b", post0, post1, 1)):
            rr = cc.loc[d1] / co.loc[d0] - 1
            m = member.loc[d0] & rr.notna()
            ab = rr[r.symbol] - rr[m].drop(r.symbol, errors="ignore").mean()
            # Kontrolle: gleicher Token, Zufallsfenster gleicher Länge ohne Unlock in ±45 Tagen
            ctl = []
            days = co.index
            for _ in range(200):
                s = days[RNG.integers(0, len(days) - (d1 - d0).days - 1)]
                if abs((s - day).days) <= 45:
                    continue
                e1 = s + (d1 - d0)
                if e1 not in days or not np.isfinite(cc.at[e1, r.symbol]) or not np.isfinite(co.at[s, r.symbol]):
                    continue
                q = cc.loc[e1] / co.loc[s] - 1
                mm = member.loc[s] & q.notna()
                ctl.append(q[r.symbol] - q[mm].drop(r.symbol, errors="ignore").mean())
            rows.append(dict(leg=leg, symbol=r.symbol, unlock_day=r.unlock_day, entry_day=d0.date().isoformat(),
                             abnormal=ab, control_mean=float(np.nanmean(ctl)) if ctl else np.nan,
                             gross=sgn * (ab - (np.nanmean(ctl) if ctl else 0)), net=sgn * (ab - (np.nanmean(ctl) if ctl else 0)) - 2 * FEE))
    t = pd.DataFrame(rows)
    t.to_csv(E / "a1_trades.csv", index=False)
    res = {leg: dict(gross=summarize(t[t.leg == leg], "gross"), net=summarize(t[t.leg == leg], "net"),
                     verdict="deskriptiv (Tor: nicht messbar, < 30 Ereignisse)") for leg in ("A1-a", "A1-b")}
    (E / "a1_result.json").write_text(json.dumps(res, indent=1, default=str))
    print(json.dumps(res, indent=1, default=str))


if __name__ == "__main__":
    {"a2s": eval_a2s, "a2k": eval_a2k, "a1": eval_a1}[sys.argv[1]]()
