import sys, os, json, io, zipfile, csv, re
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from s3list import s3list
from concurrent.futures import ThreadPoolExecutor
DL = "https://data.binance.vision/"
interval = sys.argv[1] if len(sys.argv) > 1 else "1d"
symfile = sys.argv[2] if len(sys.argv) > 2 else None
outdir = os.path.join(OUT, "universe_1d" if interval == "1d" else "kl_1h")
os.makedirs(outdir, exist_ok=True)
d = json.load(open(os.path.join(os.path.dirname(__file__), "..", "symbols_all.json")))
syms = sorted(set(s for s in d["monthly"] + d["daily"] if s.endswith("USDT")))
if symfile:
    syms = [l.strip() for l in open(symfile) if l.strip()]
W1 = [f"{y}-{m:02d}" for y in (2023, 2024) for m in range(1, 13)]
W2 = ["2026-07", "2026-08", "2026-09"]
months_wanted = (W1 if interval == "1d" else []) + W2
def parse(content):
    rows = []
    z = zipfile.ZipFile(io.BytesIO(content))
    for n in z.namelist():
        for line in z.read(n).decode().splitlines():
            p = line.split(",")
            if not p or not p[0].strip().isdigit():
                continue
            ts = int(p[0])
            if ts > 10**14: ts //= 1000
            rows.append([ts, p[1], p[2], p[3], p[4], p[5], p[7]])
    return rows
def work(sym):
    meta = {"symbol": sym}
    mkeys, _ = s3list(f"data/spot/monthly/klines/{sym}/{interval}/")
    mfiles = sorted(k for k in mkeys if k.endswith(".zip"))
    months = [re.search(r"(\d{4}-\d{2})\.zip$", k).group(1) for k in mfiles]
    dkeys, _ = s3list(f"data/spot/daily/klines/{sym}/{interval}/{sym}-{interval}-2026-10")
    dfiles = sorted(k for k in dkeys if k.endswith(".zip"))
    if interval == "1d":
        if months:
            meta["first_file"] = months[0]; meta["last_file"] = months[-1]
        else:
            alld, _ = s3list(f"data/spot/daily/klines/{sym}/{interval}/")
            dd = sorted(re.search(r"(\d{4}-\d{2}-\d{2})\.zip$", k).group(1) for k in alld if k.endswith(".zip"))
            meta["first_file"] = dd[0] if dd else ""; meta["last_file"] = dd[-1] if dd else ""
        if dfiles:
            meta["last_file"] = re.search(r"(\d{4}-\d{2}-\d{2})\.zip$", dfiles[-1]).group(1)
    rows = []
    for k, m in zip(mfiles, months):
        if m in months_wanted:
            r = get(DL + k)
            if r is not None and r.status_code == 200: rows += parse(r.content)
            else: meta.setdefault("errors", []).append(k)
    for k in dfiles:
        r = get(DL + k)
        if r is not None and r.status_code == 200: rows += parse(r.content)
        else: meta.setdefault("errors", []).append(k)
    # hard holdout filter
    w1s, w1e = 1672531200000, 1735689599999
    w2s = 1782864000000
    rows = sorted({r[0]: r for r in rows if (w1s <= r[0] <= w1e) or r[0] >= w2s}.values())
    if rows:
        with open(os.path.join(outdir, f"{sym}.csv"), "w", newline="") as f:
            w = csv.writer(f); w.writerow(["ts", "open", "high", "low", "close", "volume", "quote_volume"]); w.writerows(rows)
    meta["rows"] = len(rows)
    return meta
with ThreadPoolExecutor(12) as ex:
    res = list(ex.map(work, syms))
json.dump(res, open(os.path.join(os.path.dirname(__file__), "..", f"universe_meta_{interval}.json"), "w"))
print(len(res), sum(1 for r in res if r["rows"]), sum(len(r.get("errors", [])) for r in res))
