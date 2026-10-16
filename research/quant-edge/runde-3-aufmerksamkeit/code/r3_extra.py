"""Runde 3: Gegenhypothesen und Zusatzzahlen zu A2-S/A2-K (nach r3_eval.py).

    python3 code/r3_extra.py   ->  ergebnisse/extra.json
"""
import glob
import json
import re
from pathlib import Path

import numpy as np
import pandas as pd

R = Path(__file__).resolve().parents[1]
D, E, L = R / "daten", R / "ergebnisse", R / "lesen"


def stats(x):
    x = np.asarray(x, float)
    if len(x) < 2:
        return dict(n=int(len(x)), mean=float(x.mean()) if len(x) else None)
    return dict(n=int(len(x)), mean=float(x.mean()), median=float(np.median(x)), t=float(x.mean() / (x.std(ddof=1) / np.sqrt(len(x)))))


def main():
    out = {}
    t = pd.read_csv(E / "a2s_trades.csv")
    t5 = t[t.h == 5]
    # Stil-Kontrolle: Übereinstimmung Volltext vs. erste 50 Wörter
    for kand in ("a2s", "a2k"):
        a = pd.DataFrame(json.loads((L / kand / "antworten.json").read_text()))[["id", "richtung"]]
        b = pd.DataFrame(json.loads((L / kand / "antworten_50w.json").read_text()))[["id", "richtung"]]
        m = a.merge(b, on="id", suffixes=("", "_50"))
        d = m[m.richtung != 0]
        out[f"{kand}_stil"] = dict(n=len(m), gleich_alle=float((m.richtung == m.richtung_50).mean()), n_richtung=len(d),
                                   gleich_bei_richtung=float((d.richtung == d.richtung_50).mean()),
                                   gegenteil_bei_richtung=float((d.richtung == -d.richtung_50).mean()))
    out["a2s_5_nach_50w"] = dict(gleiche_richtung_wie_50w=stats(t5[t5.richtung == t5.richtung_50w].net),
                                 nur_volltext=stats(t5[t5.richtung_50w == 0].net))
    out["a2s_5_nach_zuversicht"] = {int(z): stats(g.net) for z, g in t5.groupby("zuversicht")}
    # Rest-Leck in Texten (Jahr/CIK aus XBRL-Kopf, der vor dem ersten "Item" stand)
    docs = [d for f in sorted(glob.glob(str(L / "a2s" / "batch_*.json"))) for d in json.load(open(f))]
    leak_ids = {d["id"] for d in docs if re.search(r"202[56]|000\d{7}", d["text"])}
    out["a2s_resttext_leck"] = dict(dokumente=len(leak_ids), von=len(docs), trades_h5=int(t5.id.isin(leak_ids).sum()),
                                    ohne_diese=stats(t5[~t5.id.isin(leak_ids)].net))
    # Leck-Erkennung, zweite (lockerere) Regel: erstes Namenswort >= 4 Zeichen im Rate-Namen
    names = pd.read_csv(D / "sec_names.csv").set_index("cik")
    lk = pd.DataFrame(json.loads((L / "a2s" / "leck.json").read_text())).set_index("id")
    ev = pd.read_csv(E / "events_a2s.csv").drop_duplicates("accession").set_index("accession")

    def loose(r):
        g = str(lk.at[r.id, "name"]).lower() if r.id in lk.index else ""
        if not g.strip() or g.startswith("unbekannt"):
            return False
        cik = ev.at[r.accession, "cik"]
        nm = str(names.at[cik, "name"]).lower() if cik in names.index else ""
        w = [x for x in re.findall(r"[a-z0-9&]+", nm) if len(x) >= 4 and x not in ("corp", "holdings", "group", "company", "the")]
        return bool(w) and w[0] in g
    t5 = t5.assign(leck_locker=[loose(r) for r in t5.itertuples()])
    out["a2s_5_leck"] = dict(streng_anteil=float(t5.leck.mean()), locker_anteil=float((t5.leck | t5.leck_locker).mean()),
                             erkannt=stats(t5[t5.leck | t5.leck_locker].net), nicht_erkannt=stats(t5[~(t5.leck | t5.leck_locker)].net),
                             leser_sicher3_anteil=float((lk.sicher == 3).mean()), leser_name_genannt=float((~lk.name.str.lower().str.startswith("unbekannt")).mean()))
    # Survivorship: 8-K-Zeilen ohne Ticker in der heutigen SEC-Liste (privat, Schulden-Emittenten oder delistet)
    ix = pd.read_csv(D / "sec_8k_index.csv")
    tk = json.loads((D / "company_tickers_exchange.json").read_text())
    ciks = {r[0] for r in tk["data"]}
    mapped = ix.cik.astype(int).isin(ciks)
    dl = set((D / "us_short_or_delisted_tickers.txt").read_text().split())
    out["survivorship"] = dict(achtk_zeilen=len(ix), ohne_ticker_anteil=float(1 - mapped.mean()), ohne_ticker_ciks=int(ix.loc[~mapped, "cik"].nunique()),
                               trades_mit_kurzer_historie=int(t5.ticker.isin(dl).sum()))
    # Kosten-Aufschlüsselung
    out["a2s_5_kosten"] = dict(mittel=float(t5.cost.mean()), median_halber_spread=float(t5.half_spread.median()),
                               mittel_halber_spread=float(t5.half_spread.mean()), gebuehr_rundreise=0.004)
    (E / "extra.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
    print(json.dumps(out, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
