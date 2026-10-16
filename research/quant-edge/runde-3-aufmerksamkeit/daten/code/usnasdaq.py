import sys, os, json, csv, datetime
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from concurrent.futures import ThreadPoolExecutor
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36", "Accept": "application/json"}
lim = RateLimiter(4)
outdir = os.path.join(OUT, "us_1d"); os.makedirs(outdir, exist_ok=True)
j = json.load(open(os.path.join(OUT, "company_tickers_exchange.json")))
tick = {}
for cik, name, t, e in j["data"]:
    if e in ("Nasdaq", "NYSE", "NYSE American"): tick.setdefault(cik, []).append(t)
ciks = {int(r["cik"]) for r in csv.DictReader(open(os.path.join(OUT, "sec_8k_index.csv")))}
tickers = sorted({tick[c][0] for c in ciks if c in tick})
num = lambda s: s.replace("$", "").replace(",", "").strip()
def work(t):
    for sym in dict.fromkeys([t, t.replace("-", ".")]):
        for ac in ("stocks", "etf"):
            r = get(f"https://api.nasdaq.com/api/quote/{sym}/historical", headers=UA, limiter=lim,
                    params={"assetclass": ac, "fromdate": "2026-07-01", "todate": "2026-10-16", "limit": 500})
            try:
                rows = r.json()["data"]["tradesTable"]["rows"]
            except Exception:
                rows = None
            if rows:
                out = []
                for x in rows:
                    m, d, y = x["date"].split("/"); date = f"{y}-{m}-{d}"
                    if date < "2026-07-01": continue
                    out.append([date, num(x["open"]), num(x["high"]), num(x["low"]), num(x["close"]), num(x["volume"])])
                out.sort()
                with open(os.path.join(outdir, f"{t}.csv"), "w", newline="") as f:
                    w = csv.writer(f); w.writerow(["date", "open", "high", "low", "close", "volume"]); w.writerows(out)
                return t, len(out)
    return t, 0
with ThreadPoolExecutor(6) as ex:
    res = list(ex.map(work, tickers))
miss = [t for t, n in res if n == 0]
open(os.path.join(OUT, "us_missing_tickers.txt"), "w").write("\n".join(miss) + "\n")
print("tickers", len(res), "ok", len(res) - len(miss), "missing", len(miss))
