import sys, time, csv, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *
path = os.path.join(OUT, "spread_live_raw.csv")
with open(path, "w", newline="") as f:
    w = csv.writer(f); w.writerow(["ts", "symbol", "bid", "ask"])
    for k in range(6):
        t0 = time.time()
        r = get("https://api.binance.com/api/v3/ticker/bookTicker")
        ts = int(time.time() * 1000)
        if r is not None and r.status_code == 200:
            for d in r.json():
                if d["symbol"].endswith("USDT"):
                    w.writerow([ts, d["symbol"], d["bidPrice"], d["askPrice"]])
            f.flush()
        print("snap", k, ts, flush=True)
        if k < 5:
            time.sleep(max(0, 600 - (time.time() - t0)))
