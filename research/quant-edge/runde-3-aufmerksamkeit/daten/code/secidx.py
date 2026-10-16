import sys, os, json, csv, datetime, re
sys.path.insert(0, os.path.dirname(__file__))
from common import *
H = {"User-Agent": "DiamondHamster research admin@must-seen.com"}
lim = RateLimiter(7)
rows = []; missing = []
d = datetime.date(2026, 7, 1)
while d <= datetime.date(2026, 9, 18):
    if d.weekday() < 5:
        q = (d.month - 1) // 3 + 1
        url = f"https://www.sec.gov/Archives/edgar/daily-index/{d.year}/QTR{q}/form.{d:%Y%m%d}.idx"
        r = get(url, headers=H, limiter=lim)
        if r is None or r.status_code != 200:
            missing.append((str(d), getattr(r, "status_code", "ERR")))
        else:
            started = False
            for line in r.text.splitlines():
                if line.startswith("-----"): started = True; continue
                if not started or not line.strip(): continue
                m = re.match(r"^(\S+(?: \S+)*?)\s{2,}(.+?)\s{2,}(\d+)\s+(\d{8})\s+(\S+)\s*$", line)
                if not m: continue
                form, company, cik, date, path = m.groups()
                if form == "8-K":
                    rows.append([cik, company.strip(), f"{date[:4]}-{date[4:6]}-{date[6:]}", path])
    d += datetime.timedelta(days=1)
with open(os.path.join(OUT, "sec_8k_index.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(["cik", "company", "date", "path"]); w.writerows(rows)
r = get("https://www.sec.gov/files/company_tickers_exchange.json", headers=H, limiter=lim)
open(os.path.join(OUT, "company_tickers_exchange.json"), "wb").write(r.content)
print(len(rows), "missing days:", missing)
