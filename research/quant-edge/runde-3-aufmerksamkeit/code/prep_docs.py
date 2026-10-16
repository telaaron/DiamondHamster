"""Runde 3: Dokumente pseudonymisieren und in Lese-Batches aufteilen.

Der Leser sieht nur eine zufällige ID und den pseudonymisierten Text, keine Kurse,
kein Datum, keinen Namen. Die Zuordnung ID -> Ereignis bleibt in lesen/<kand>/key.csv.

    python3 code/prep_docs.py a2k
    python3 code/prep_docs.py a2s
"""
import gzip
import hashlib
import json
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).parent))
from pseudo import pseudonymize  # noqa: E402

R = Path(__file__).resolve().parents[1]
D, E, L = R / "daten", R / "ergebnisse", R / "lesen"
INJECT = re.compile(r"onerror\s*=|<script|atob\(", re.I)
MAX_WORDS = 4000  # sehr lange Dokumente werden gekürzt (Tokenbudget), vermerkt in key.csv
MAX_CHARS = 40000  # je Batch-Datei; größere Dateien schneidet das Read-Werkzeug ab

_SUFFIX = re.compile(r"[,.]?\s+(inc|corp|corporation|co|company|ltd|limited|plc|llc|lp|l\.p|holdings?|group|n\.v|s\.a|ag|se|trust|bancorp|technologies|therapeutics|pharmaceuticals)\.?$", re.I)
_EXTRA = [
    ("PHONE", re.compile(r"\(?\b\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}\b")),
    ("FILENO", re.compile(r"\b0\d{2}-\d{5}\b")),
    ("EIN", re.compile(r"\b\d{2}-\d{7}\b")),
    ("ZIP", re.compile(r"\b[A-Z]{2}\s+\d{5}(?:-\d{4})?\b")),
]


def name_variants(name: str) -> list[str]:
    out = {name.strip()}
    n = name.strip()
    for _ in range(3):
        n2 = _SUFFIX.sub("", n).strip(" ,.")
        if n2 and n2 != n:
            out.add(n2)
            n = n2
    return sorted((v for v in out if len(v) >= 3), key=len, reverse=True)


def cut_8k(text: str) -> str:
    """Deckblatt (Adresse, Registernummern) und Unterschriftenblock entfernen."""
    m = re.search(r"\bItem\s+\d{1,2}\.\d{2}\b", text, re.I)
    if m:
        text = text[m.start():]
    s = re.search(r"\bSIGNATURES?\b", text)
    if s and s.start() > 200:
        text = text[: s.start()]
    return text


def finish(text, ents):
    t, _ = pseudonymize(text, ents)
    for label, pat in _EXTRA:
        t = pat.sub(f"[{label}]", t)
    words = t.split()
    cut = len(words) > MAX_WORDS
    if cut:
        t = " ".join(words[:MAX_WORDS]) + " [GEKÜRZT]"
    return t, cut


def write_batches(kand, docs):
    out = L / kand
    out.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(20261016)
    order = rng.permutation(len(docs))
    key = []
    batches = []
    for j, i in enumerate(order):
        d = docs[i]
        did = hashlib.sha256(f"{kand}-{d['event']}-r3".encode()).hexdigest()[:10]
        key.append(dict(id=did, event=d["event"], words=len(d["text"].split()), gekuerzt=d["cut"]))
        size = sum(len(x["text"]) for x in batches[-1]) if batches else None
        if not batches or size + len(d["text"]) > MAX_CHARS:
            batches.append([])
        batches[-1].append(dict(id=did, text=d["text"]))
    for k, b in enumerate(batches):
        (out / f"batch_{k:03d}.json").write_text(json.dumps(b, ensure_ascii=False, indent=0))
    pd.DataFrame(key).to_csv(out / "key.csv", index=False)
    # Stil-Kontrolle (Gegenhypothese 4): nur die ersten 50 Wörter, gleiche IDs, 100 Dokumente je Datei
    w50 = out / "w50"
    w50.mkdir(exist_ok=True)
    flat = [x for b in batches for x in b]
    for k in range(0, len(flat), 100):
        part = [dict(id=x["id"], text=" ".join(x["text"].split()[:50])) for x in flat[k:k + 100]]
        (w50 / f"batch_{k // 100:03d}.json").write_text(json.dumps(part, ensure_ascii=False, indent=0))
    print(kand, len(docs), "Dokumente,", len(batches), "Batches")


def a2k():
    ev = pd.read_csv(E / "events_a2k.csv")
    ev = ev[ev.selected]
    props = {json.loads(x)["id"]: json.loads(x) for x in open(D / "snapshot_proposals.jsonl")}
    docs, spam = [], 0
    for r in ev.itertuples():
        p = props[r.id]
        if INJECT.search(p.get("body") or ""):  # Nachtrag N2: Phishing/Code-Injektion, kein echter Vorschlag
            spam += 1
            continue
        sp = p["space"]
        base = sym = r.symbol.removesuffix("USDT")
        nm = sp.get("name") or ""
        core = re.sub(r"\b(governance|signal|dao|foundation|snapshot|non-technical|technical|vote|voting)\b", "", nm, flags=re.I).strip(" -")
        names = {nm, core, sp["id"].split(".")[0], sp["id"]}
        ents = {"TOKEN": [sym, sp.get("symbol") or sym], "PROJECT": [n for n in names if len(n) >= 3]}
        text = f"Titel: {p['title']}\n\n{p['body']}\n\nAuswahl: {' / '.join(p.get('choices') or [])}"
        t, cut = finish(text, ents)
        docs.append(dict(event=r.id, text=t, cut=cut))
        _ = base
    print("A2-K: Spam/Injektion verworfen:", spam)
    write_batches("a2k", docs)


def a2s():
    ev = pd.read_csv(E / "events_a2s.csv")
    names = pd.read_csv(D / "sec_names.csv").set_index("cik")
    tick = json.loads((D / "company_tickers_exchange.json").read_text())
    alltick = {}
    for row in tick["data"]:
        alltick.setdefault(row[0], set()).add(row[2])
    texts = {}
    with gzip.open(D / "sec_8k_text.jsonl.gz", "rt") as f:
        for line in f:
            x = json.loads(line)
            texts[x["accession"]] = x["text"]
    docs, dropped = [], 0
    for r in ev.itertuples():
        if r.accession not in texts:
            dropped += 1
            continue
        body = cut_8k(texts[r.accession])
        if len(re.findall(r"\w+", body)) < 300:  # Vorab-Regel: Haupttext >= 300 Wörter
            dropped += 1
            continue
        nm = [names.at[r.cik, "name"]] if r.cik in names.index else []
        if r.cik in names.index and isinstance(names.at[r.cik, "former_names"], str):
            nm += names.at[r.cik, "former_names"].split(";")
        variants = sorted({v for n in nm for v in name_variants(n)}, key=len, reverse=True)
        ents = {"COMPANY": variants, "TICKER": sorted(alltick.get(int(r.cik), {r.ticker}) | {r.ticker})}
        t, cut = finish(body, ents)
        docs.append(dict(event=r.accession, text=t, cut=cut))
    print("A2-S: verworfen (fehlend oder < 300 Wörter):", dropped)
    write_batches("a2s", docs)


if __name__ == "__main__":
    {"a2k": a2k, "a2s": a2s}[sys.argv[1]]()
