"""Quant-Edge Runde 2: Rohdaten laden (stdlib only). Holdout 2025-01-01..2026-06-30 wird nie angefragt."""
import csv, io, json, os, sys, time, zipfile, urllib.request, urllib.error, datetime as dt, re
from concurrent.futures import ThreadPoolExecutor

OUT = sys.argv[1]
STEP = sys.argv[2]
os.makedirs(OUT, exist_ok=True)
LOG = os.path.join(OUT, "request_log.jsonl")

def ms(y, m, d):
    return int(dt.datetime(y, m, d, tzinfo=dt.timezone.utc).timestamp() * 1000)

H0 = ms(2025, 1, 1)               # holdout start (inclusive)
W2S = ms(2026, 7, 1)              # holdout end (exclusive) = W2 start
W1E = H0 - 1
NOW = int(time.time() * 1000)
COINS = "BTC ETH SOL XRP BNB DOGE ADA LTC LINK AVAX TRX DOT".split()
UA = {"User-Agent": "Mozilla/5.0 qe-r2"}

def log(**kw):
    kw["at"] = dt.datetime.now(dt.timezone.utc).isoformat()
    with open(LOG, "a") as f:
        f.write(json.dumps(kw) + "\n")

def get(url, body=None, tries=5, quiet=False):
    data = json.dumps(body).encode() if body is not None else None
    hdr = dict(UA)
    if data: hdr["Content-Type"] = "application/json"
    err = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, data=data, headers=hdr)
            with urllib.request.urlopen(req, timeout=60) as r:
                raw = r.read()
            if not quiet: log(url=url, body=body, status=200, bytes=len(raw))
            return raw
        except urllib.error.HTTPError as e:
            err = f"HTTP {e.code}"
            if e.code in (404, 400, 403, 451):
                break
            time.sleep(2 ** i)
        except Exception as e:
            err = repr(e)
            time.sleep(2 ** i)
    log(url=url, body=body, error=err)
    return None

def inhold(t):
    return H0 <= t < W2S

def write(name, header, rows):
    p = os.path.join(OUT, name)
    with open(p, "w", newline="") as f:
        w = csv.writer(f); w.writerow(header); w.writerows(rows)
    print(name, len(rows), flush=True)

# 1 Bybit funding
def bybit():
    base = "https://api.bybit.com/v5/market/funding/history?category=linear&symbol={s}&limit=200"
    for c in COINS:
        s = c + "USDT"; rows = {}
        for (start, end) in [(None, W1E), (W2S, NOW)]:
            e = end
            while True:
                u = base.format(s=s) + (f"&startTime={start}" if start else "") + f"&endTime={e}"
                r = get(u)
                if r is None: break
                j = json.loads(r)
                if j.get("retCode") != 0:
                    log(url=u, error=f"retCode {j.get('retCode')} {j.get('retMsg')}"); break
                lst = j["result"]["list"]
                if not lst: break
                for x in lst:
                    t = int(x["fundingRateTimestamp"]); rows[t] = x["fundingRate"]
                mn = min(int(x["fundingRateTimestamp"]) for x in lst)
                if len(lst) < 200 or (start and mn <= start): break
                e = mn - 1
                time.sleep(0.12)
        write(f"bybit_funding_{c}.csv", ["ts", "fundingRate"], sorted(rows.items()))

# 2 Hyperliquid funding
def hl():
    for c in COINS:
        rows = {}
        for (start, end) in [(ms(2022, 1, 1), W1E), (W2S, NOW)]:
            s = start
            while s < end:
                b = {"type": "fundingHistory", "coin": c, "startTime": s, "endTime": end}
                r = get("https://api.hyperliquid.xyz/info", body=b)
                if r is None: break
                lst = json.loads(r)
                if not lst: break
                for x in lst:
                    rows[int(x["time"])] = (x["fundingRate"], x["premium"])
                mx = max(int(x["time"]) for x in lst)
                if len(lst) < 500: break
                s = mx + 1
                time.sleep(1.0)
        write(f"hl_funding_{c}.csv", ["ts", "fundingRate", "premium"], [(t, a, b) for t, (a, b) in sorted(rows.items())])

# 3 dated futures continuous klines
def dated():
    for p in ["BTC", "ETH"]:
        for ct, tag in [("CURRENT_QUARTER", "current"), ("NEXT_QUARTER", "next")]:
            for venue, host, pair, win in [("um", "https://fapi.binance.com/fapi/v1", p + "USDT", 1000), ("cm", "https://dapi.binance.com/dapi/v1", p + "USD", 199)]:
                rows = {}
                for (start, end) in [(ms(2019, 1, 1), W1E), (W2S, NOW)]:
                    s = start
                    while s <= end:
                        e = min(end, s + win * 86400000 - 1)
                        u = f"{host}/continuousKlines?pair={pair}&contractType={ct}&interval=1d&startTime={s}&endTime={e}&limit=1500"
                        r = get(u)
                        if r is not None:
                            j = json.loads(r)
                            if isinstance(j, list):
                                for k in j:
                                    rows[int(k[0])] = k[1:6]
                            else:
                                log(url=u, error=str(j))
                        s = e + 1
                        time.sleep(0.3)
                write(f"dated_{venue}_{p}_{tag}.csv", ["ts", "open", "high", "low", "close", "volume"], [[t] + v for t, v in sorted(rows.items())])

# 4 FRED
def fred():
    today = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")
    rows = []
    for a, b in [("2018-01-01", "2024-12-31"), ("2026-07-01", today)]:
        r = get(f"https://fred.stlouisfed.org/graph/fredgraph.csv?id=DTB3&cosd={a}&coed={b}")
        if r is None: continue
        rd = csv.reader(io.StringIO(r.decode()))
        next(rd)
        for d, v in rd:
            rows.append((d, "" if v == "." else v))
    write("tbill_dtb3.csv", ["date", "rate"], rows)

# S3 listing of data.binance.vision
def s3list(prefix):
    keys, marker = [], ""
    while True:
        u = f"https://s3-ap-northeast-1.amazonaws.com/data.binance.vision?delimiter=/&prefix={prefix}" + (f"&marker={marker}" if marker else "")
        r = get(u)
        if r is None: break
        t = r.decode()
        ks = re.findall(r"<Key>([^<]+)</Key>", t)
        keys += ks
        if "<IsTruncated>true</IsTruncated>" in t and ks:
            marker = ks[-1]
        else:
            break
    return keys

def keydate(k):
    m = re.search(r"(\d{4}-\d{2}-\d{2})\.zip$", k)
    return m.group(1) if m else None

def allowed_date(d):
    return d <= "2024-12-31" or d >= "2026-07-01"

def zipcsv(url):
    r = get(url)
    if r is None: return url, None
    with zipfile.ZipFile(io.BytesIO(r)) as z:
        return url, z.read(z.namelist()[0]).decode()

def fl(x):
    try: return float(x)
    except: return None

# 5 metrics
def metrics():
    coins = sys.argv[3].split(",") if len(sys.argv) > 3 else COINS
    for c in coins:
        s = c + "USDT"
        keys = [k for k in s3list(f"data/futures/um/daily/metrics/{s}/") if k.endswith(".zip") and keydate(k) and allowed_date(keydate(k))]
        urls = ["https://data.binance.vision/" + k for k in keys]
        log(step="metrics", symbol=s, files=len(urls), first=keydate(keys[0]) if keys else None, last=keydate(keys[-1]) if keys else None, note="url pattern https://data.binance.vision/data/futures/um/daily/metrics/{S}/{S}-metrics-YYYY-MM-DD.zip, one GET per listed file")
        daily, m15, fails = [], [], []
        with ThreadPoolExecutor(12) as ex:
            res = list(ex.map(zipcsv, urls))
        for url, txt in res:
            if txt is None: fails.append(url); continue
            d = keydate(url)
            rd = [r for r in csv.reader(io.StringIO(txt)) if r]
            if rd and not re.match(r"\d{4}-", rd[0][0]): rd = rd[1:]
            # create_time,symbol,sum_open_interest,sum_open_interest_value,count_toptrader_long_short_ratio,sum_toptrader_long_short_ratio,count_long_short_ratio,sum_taker_long_short_vol_ratio
            rd = sorted(rd, key=lambda r: r[0])
            def mean(i):
                v = [fl(r[i]) for r in rd if len(r) > i and fl(r[i]) is not None]
                return sum(v) / len(v) if v else ""
            oiv = [fl(r[3]) for r in rd if fl(r[3]) is not None]
            daily.append((d, oiv[-1] if oiv else "", mean(3), mean(6), mean(7), len(rd)))
            if c in ("BTC", "ETH"):
                for r in rd:
                    t = dt.datetime.strptime(r[0], "%Y-%m-%d %H:%M:%S").replace(tzinfo=dt.timezone.utc)
                    if t.minute % 15 == 0 and t.second == 0:
                        m15.append((int(t.timestamp() * 1000), r[2], r[3], r[4], r[7]))
        if fails: log(step="metrics", symbol=s, failed=fails)
        daily.sort()
        write(f"metrics_daily_{c}.csv", ["date", "oi_value_last", "oi_value_mean", "count_long_short_ratio_mean", "taker_ls_vol_ratio_mean", "n_rows"], daily)
        if c in ("BTC", "ETH"):
            m15 = sorted(set(m15))
            write(f"metrics_15m_{c}.csv", ["ts", "sum_open_interest", "sum_open_interest_value", "count_toptrader_long_short_ratio", "sum_taker_long_short_vol_ratio"], m15)

# 6 perp 15m
def perp():
    months = []
    y, m = 2021, 12
    while (y, m) <= (2024, 12):
        months.append(f"{y}-{m:02d}"); m += 1
        if m == 13: y, m = y + 1, 1
    for c in ["BTC", "ETH"]:
        s = c + "USDT"; rows = {}
        urls = [f"https://data.binance.vision/data/futures/um/monthly/klines/{s}/15m/{s}-15m-{mo}.zip" for mo in months]
        with ThreadPoolExecutor(8) as ex:
            res = list(ex.map(zipcsv, urls))
        for url, txt in res:
            log(url=url, status="ok" if txt else "fail")
            if txt is None: continue
            for r in csv.reader(io.StringIO(txt)):
                if not r or not r[0].isdigit(): continue
                rows[int(r[0])] = [r[1], r[2], r[3], r[4], r[5], r[7], r[8], r[10]]
        st = W2S
        while st < NOW:
            u = f"https://fapi.binance.com/fapi/v1/klines?symbol={s}&interval=15m&startTime={st}&endTime={NOW}&limit=1500"
            r = get(u)
            if r is None: break
            j = json.loads(r)
            if not j: break
            for k in j:
                rows[int(k[0])] = [k[1], k[2], k[3], k[4], k[5], k[7], k[8], k[10]]
            st = int(j[-1][0]) + 1
            if len(j) < 1500: break
            time.sleep(0.3)
        write(f"perp15m_{c}.csv", ["ts", "open", "high", "low", "close", "volume", "quote_volume", "trades", "taker_buy_quote_volume"], [[t] + v for t, v in sorted(rows.items())])

# 7 liquidation snapshots
def liq():
    info = {}
    for c in ["BTC", "ETH"]:
        s = c + "USDT"
        keys = [k for k in s3list(f"data/futures/um/daily/liquidationSnapshot/{s}/") if k.endswith(".zip")]
        ds = sorted(filter(None, map(keydate, keys)))
        pre = [k for k in keys if keydate(k) and keydate(k) <= "2024-12-31"]
        info[s] = {"n_files_total": len(ds), "first": ds[0] if ds else None, "last": ds[-1] if ds else None, "n_files_W1": len(pre)}
        if pre:
            with ThreadPoolExecutor(8) as ex:
                res = list(ex.map(zipcsv, ["https://data.binance.vision/" + k for k in pre]))
            hdr, rows = None, []
            for url, txt in res:
                if txt is None: continue
                rd = [r for r in csv.reader(io.StringIO(txt)) if r]
                if rd and not rd[0][0].isdigit():
                    hdr = hdr or rd[0]; rd = rd[1:]
                rows += rd
            rows.sort(key=lambda r: int(r[0]))
            write(f"liq_{c}.csv", hdr or [f"c{i}" for i in range(len(rows[0]))], rows)
    log(step="liq_listing", info=info)
    print(json.dumps(info))

# 8 USDe
def usde():
    r = get("https://stablecoins.llama.fi/stablecoins")
    j = json.loads(r)
    cand = [a for a in j["peggedAssets"] if a.get("symbol") == "USDe" or "Ethena" in (a.get("name") or "")]
    a = [x for x in cand if x.get("symbol") == "USDe"][0]
    sid = a["id"]
    r = get(f"https://stablecoins.llama.fi/stablecoin/{sid}")
    j = json.loads(r)
    rows, dropped = [], 0
    for x in j["tokens"]:
        t = int(x["date"]) * 1000
        if inhold(t): dropped += 1; continue
        v = (x.get("circulating") or {}).get("peggedUSD")
        rows.append((dt.datetime.fromtimestamp(t / 1000, dt.timezone.utc).strftime("%Y-%m-%d"), v))
    log(step="usde", id=sid, name=a.get("name"), holdout_transit={"source": f"https://stablecoins.llama.fi/stablecoin/{sid}", "rows_received_in_holdout_dropped_before_save": dropped, "reason": "endpoint has no time-window parameter"})
    write("usde_supply.csv", ["date", "circulating_usd"], rows)

globals()[STEP]()
