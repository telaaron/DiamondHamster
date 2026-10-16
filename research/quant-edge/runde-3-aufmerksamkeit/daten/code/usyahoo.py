import sys, os, json, csv, datetime, time
from zoneinfo import ZoneInfo
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from concurrent.futures import ThreadPoolExecutor
UA = {"User-Agent": "Mozilla/5.0"}
lim = RateLimiter(2.5)
ET = ZoneInfo("America/New_York")
SP = os.path.join(os.path.dirname(__file__), "..")
d1 = os.path.join(SP, "us_1d_yahoo"); h1 = os.path.join(OUT, "us_1h"); os.makedirs(d1, exist_ok=True); os.makedirs(h1, exist_ok=True)
j = json.load(open(os.path.join(OUT, "company_tickers_exchange.json")))
tick = {}
for cik, name, t, e in j["data"]:
    if e in ("Nasdaq", "NYSE", "NYSE American"): tick.setdefault(cik, []).append(t)
ciks = {int(r["cik"]) for r in csv.DictReader(open(os.path.join(OUT, "sec_8k_index.csv")))}
tickers = sorted({tick[c][0] for c in ciks if c in tick})
P1, P2 = 1782864000, int(time.time())
def one(t, iv):
    r = get(f"https://query1.finance.yahoo.com/v8/finance/chart/{t}", headers=UA, limiter=lim, params={"interval": iv, "period1": P1, "period2": P2}, retries=5)
    try:
        res = r.json()["chart"]["result"][0]; q = res["indicators"]["quote"][0]; ts = res.get("timestamp") or []
    except Exception:
        return None
    out = []
    for i, s in enumerate(ts):
        if s < P1: continue
        vals = [q[k][i] for k in ("open", "high", "low", "close", "volume")]
        if vals[3] is None: continue
        if iv == "1d": out.append([datetime.datetime.fromtimestamp(s, ET).strftime("%Y-%m-%d")] + vals)
        else: out.append([s * 1000] + vals)
    return out
def work(t):
    st = {}
    for iv, dd, hdr in (("1d", d1, "date"), ("60m", h1, "ts")):
        out = one(t, iv)
        st[iv] = len(out) if out else 0
        if out:
            with open(os.path.join(dd, f"{t}.csv"), "w", newline="") as f:
                w = csv.writer(f); w.writerow([hdr, "open", "high", "low", "close", "volume"]); w.writerows(out)
    return t, st
with ThreadPoolExecutor(4) as ex: res = list(ex.map(work, tickers))
json.dump(res, open(os.path.join(SP, "usyahoo_res.json"), "w"))
print("tickers", len(res), "1d_ok", sum(1 for t, s in res if s["1d"]), "60m_ok", sum(1 for t, s in res if s["60m"]))
