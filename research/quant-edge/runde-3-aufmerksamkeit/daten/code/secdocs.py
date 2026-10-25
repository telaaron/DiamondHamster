import sys, os, csv, re, random, datetime, json
from zoneinfo import ZoneInfo
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from concurrent.futures import ThreadPoolExecutor
H = {"User-Agent": "DiamondHamster research admin@must-seen.com"}
lim = RateLimiter(7)
P = os.path.join(OUT, "sec_8k_meta.csv")
rows = list(csv.DictReader(open(P)))
ET = ZoneInfo("America/New_York")
def acc(r):
    if not r["accession"]: return r
    cik = r["cik"]; a = r["accession"]
    url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{a.replace('-', '')}/{a}-index.htm"
    x = get(url, headers=H, limiter=lim)
    r["accepted_et_index"] = ""; r["acceptance_utc"] = ""
    if x is not None and x.status_code == 200:
        m = re.search(r'Accepted</div>\s*<div class="info">([0-9-]+ [0-9:]+)</div>', x.text)
        if m:
            et = datetime.datetime.strptime(m.group(1), "%Y-%m-%d %H:%M:%S").replace(tzinfo=ET)
            r["accepted_et_index"] = m.group(1)
            r["acceptance_utc"] = et.astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return r
for r in rows: r["acceptance_json_raw"] = r.pop("acceptance_utc")
with ThreadPoolExecutor(6) as ex: rows = list(ex.map(acc, rows))
cols = ["cik", "ticker", "accession", "acceptance_utc", "items", "primary_doc_url", "acceptance_json_raw", "accepted_et_index", "all_tickers"]
with open(P, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore"); w.writeheader(); w.writerows(rows)
SKIP = {"5.07", "7.01", "9.01"}
elig = sorted([r for r in rows if r["primary_doc_url"] and r["items"] and not set(i.strip() for i in r["items"].split(",") if i.strip()) <= SKIP], key=lambda r: r["accession"])
random.seed(20261016)
pick = random.sample(elig, 3000) if len(elig) > 3000 else elig
dd = os.path.join(OUT, "sec_8k_docs"); os.makedirs(dd, exist_ok=True)
def doc(r):
    x = get(r["primary_doc_url"], headers=H, limiter=lim)
    if x is not None and x.status_code == 200:
        open(os.path.join(dd, r["accession"] + ".html"), "wb").write(x.content); return 1
    return 0
with ThreadPoolExecutor(6) as ex: ok = sum(ex.map(doc, pick))
open(os.path.join(OUT, "sec_8k_docs_sample.txt"), "w").write("\n".join(r["accession"] for r in pick) + "\n")
c = {"8k_total_index": sum(1 for _ in open(os.path.join(OUT, "sec_8k_index.csv"))) - 1, "8k_with_ticker": len(rows),
     "8k_with_ticker_meta_found": sum(1 for r in rows if r["primary_doc_url"]),
     "8k_with_ticker_not_only_507_701_901": len(elig), "acceptance_from_index": sum(1 for r in rows if r["acceptance_utc"]),
     "json_vs_index_mismatch": sum(1 for r in rows if r["acceptance_utc"] and r["acceptance_json_raw"] and r["acceptance_json_raw"][:19] != r["acceptance_utc"][:19]),
     "docs_sampled": len(pick), "docs_ok": ok}
json.dump(c, open(os.path.join(OUT, "sec_counts.json"), "w"), indent=1); print(c)
