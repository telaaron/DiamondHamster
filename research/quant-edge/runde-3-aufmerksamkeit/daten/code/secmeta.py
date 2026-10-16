import sys, os, json, csv
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from concurrent.futures import ThreadPoolExecutor
H = {"User-Agent": "DiamondHamster research admin@must-seen.com"}
lim = RateLimiter(7)
j = json.load(open(os.path.join(OUT, "company_tickers_exchange.json")))
tick = {}
for cik, name, t, e in j["data"]:
    if e in ("Nasdaq", "NYSE", "NYSE American"): tick.setdefault(cik, []).append(t)
rows = [r for r in csv.DictReader(open(os.path.join(OUT, "sec_8k_index.csv"))) if int(r["cik"]) in tick]
bycik = {}
for r in rows:
    acc = r["path"].split("/")[-1].replace(".txt", "")
    bycik.setdefault(int(r["cik"]), set()).add(acc)
def tab(rec):
    keys = ["accessionNumber", "acceptanceDateTime", "form", "items", "primaryDocument"]
    return {a: dict(zip(keys[1:], v)) for a, *v in zip(*[rec[k] for k in keys])} if rec else {}
def work(cik):
    url = f"https://data.sec.gov/submissions/CIK{cik:010d}.json"
    r = get(url, headers=H, limiter=lim)
    out = []
    if r is None or r.status_code != 200: return cik, out, "fail"
    js = r.json(); t = tab(js["filings"]["recent"])
    need = bycik[cik] - set(t)
    for fobj in js["filings"].get("files", []):
        if not need: break
        if fobj.get("filingTo", "") >= "2026-07-01":
            r2 = get("https://data.sec.gov/submissions/" + fobj["name"], headers=H, limiter=lim)
            if r2 is not None and r2.status_code == 200:
                t.update(tab(r2.json())); need = bycik[cik] - set(t)
    for acc in sorted(bycik[cik]):
        m = t.get(acc)
        if not m: out.append([cik, tick[cik][0], acc, "", "", ""]); continue
        doc = f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-', '')}/{m['primaryDocument']}"
        out.append([cik, tick[cik][0], acc, m["acceptanceDateTime"], m["items"], doc])
    return cik, out, "ok"
with ThreadPoolExecutor(6) as ex:
    res = list(ex.map(work, sorted(bycik)))
with open(os.path.join(OUT, "sec_8k_meta.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(["cik", "ticker", "accession", "acceptance_utc", "items", "primary_doc_url", "all_tickers"])
    for cik, out, st in res:
        for o in out: w.writerow(o + ["|".join(tick[cik])])
print("ciks", len(res), "fail", sum(1 for r in res if r[2] != "ok"), "missing_meta", sum(1 for r in res for o in r[1] if not o[3]))
