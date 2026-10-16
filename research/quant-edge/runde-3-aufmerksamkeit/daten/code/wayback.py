import sys, os, json, csv, re, gzip, urllib.parse, html as H
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from concurrent.futures import ThreadPoolExecutor
SP = os.path.join(os.path.dirname(__file__), "..")
lim = RateLimiter(0.8)
NON = {"pricing","allocation-screener","ethereum-shanghai","claimed","terms","privacy","events","dashboard","login","signup","404","sitemap.xml","robots.txt","favicon.ico","launchpad","categories","supply","api","auth","static","_next","get-started","cdn-cgi","unlocks","calendar","vesting","fundraising","sitemap"}
d = json.load(open(os.path.join(SP, "cdx_unlocks.json")))[1:]
slugs = set()
for ts, o in d:
    p = urllib.parse.urlparse(o).path.strip("/").lower()
    if not p or "/" in p or re.fullmatch(r"[0-9a-f]{16,}", p) or p in NON or "." in p: continue
    slugs.add(p)
slugs = sorted(slugs)
def cdx(slug):
    r = get("https://web.archive.org/cdx/search/cdx", limiter=lim, timeout=180, params={"url": f"token.unlocks.app/{slug}", "output": "json", "from": "2023", "to": "2024", "filter": "statuscode:200", "collapse": "timestamp:8", "fl": "timestamp,original"})
    try: return slug, [x for x in r.json()[1:]]
    except Exception: return slug, None
with ThreadPoolExecutor(3) as ex: cd = dict(ex.map(cdx, slugs))
with open(os.path.join(OUT, "unlocks_cdx_tokens.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(["token", "timestamp", "original"])
    for s in slugs:
        for ts, o in (cd[s] or []): w.writerow([s, ts, o])
print("slugs", len(slugs), "cdx_fail", [s for s in slugs if cd[s] is None], flush=True)
def fetch(ts, orig):
    r = get(f"https://web.archive.org/web/{ts}id_/{orig}", limiter=lim, timeout=180)
    if r is None or r.status_code != 200: return None
    b = r.content
    if b[:2] == b"\x1f\x8b":
        try: b = gzip.decompress(b)
        except Exception: pass
    return b
syms = set(s for g in json.load(open(os.path.join(SP, "symbols_all.json"))).values() for s in g if s.endswith("USDT"))
def title_sym(b):
    m = re.search(rb"<title>\s*([A-Za-z0-9$.]+)\s+[|-]", b or b"")
    return H.unescape(m.group(1).decode("utf-8", "replace")).strip() if m else ""
def mapone(slug):
    snaps = cd.get(slug) or []
    if not snaps: return slug, "", ""
    ts, o = snaps[-1]
    b = fetch(ts, o); t = title_sym(b)
    return slug, t, (t + "USDT") if (t and t.upper() == t and (t + "USDT") in syms) else ""
with ThreadPoolExecutor(3) as ex: mp = list(ex.map(mapone, slugs))
with open(os.path.join(OUT, "unlocks_token_map.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(["token", "page_symbol", "binance_symbol"]); w.writerows(mp)
mapped = [m for m in mp if m[2]]
print("mapped", len(mapped), flush=True)
jobs = []
for slug, t, bs in mapped:
    seen = set()
    for ts, o in cd[slug]:
        ym = ts[:6]
        if "202303" <= ym <= "202412" and ym not in seen:
            seen.add(ym); jobs.append((slug, ts, o))
def dl(j):
    slug, ts, o = j
    p = os.path.join(OUT, "unlocks_wayback", slug); os.makedirs(p, exist_ok=True)
    fp = os.path.join(p, f"{ts}.html")
    if os.path.exists(fp): return 1
    b = fetch(ts, o)
    if b: open(fp, "wb").write(b); return 1
    return 0
with ThreadPoolExecutor(3) as ex: ok = sum(ex.map(dl, jobs))
print("snapshots", len(jobs), "ok", ok, flush=True)
