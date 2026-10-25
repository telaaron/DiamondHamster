import json, csv, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from common import OUT
SP = os.path.join(os.path.dirname(__file__), "..")
STABLE = {"USDC","FDUSD","TUSD","BUSD","DAI","USDP","PAX","EUR","EURI","AEUR","GBP","AUD","USDS","USDSB","UST","SUSD","USD1","PYUSD","USDE","RLUSD","BFUSD","XUSD","BRL","TRY","RWUSD","EURC","USDSOLD","USDF"}
m = json.load(open(os.path.join(SP, "universe_meta_1d.json")))
def norm(x, last=False):
    if len(x) == 7:
        if not last: return x + "-01"
        import calendar; y, mo = map(int, x.split("-")); return f"{x}-{calendar.monthrange(y, mo)[1]:02d}"
    return x
with open(os.path.join(OUT, "universe.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(["symbol", "first_date", "last_date", "is_stable", "rows_w1w2", "note"])
    for x in m:
        b = x["symbol"][:-4]
        st = b in STABLE
        note = "gold_token" if b in ("XAUT", "PAXG") else ""
        w.writerow([x["symbol"], norm(x.get("first_file", "")), norm(x.get("last_file", ""), True), int(st), x["rows"], note])
print(sum(1 for x in m if x["symbol"][:-4] in STABLE), [x["symbol"] for x in m if x["symbol"][:-4] in STABLE])
