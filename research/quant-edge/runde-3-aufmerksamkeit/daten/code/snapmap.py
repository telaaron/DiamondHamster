import sys, os, json, csv, collections
sys.path.insert(0, os.path.dirname(__file__))
from common import OUT
SP = os.path.join(os.path.dirname(__file__), "..")
STABLE = {"USDC","FDUSD","TUSD","BUSD","DAI","USDP","PAX","EUR","EURI","AEUR","GBP","AUD","USDS","USDSB","UST","SUSD","USD1","PYUSD","USDE","RLUSD","BFUSD","XUSD","FRAX","TRY","BRL","U","USDF","RWUSD","EURC"}
syms = set(s for g in json.load(open(os.path.join(SP, "symbols_all.json"))).values() for s in g if s.endswith("USDT"))
ps = [json.loads(l) for l in open(os.path.join(OUT, "snapshot_proposals.jsonl"))]
spaces = {}
for p in ps:
    sp = p["space"] or {}
    spaces[sp.get("id")] = (sp.get("symbol") or "").strip()
bysym = collections.defaultdict(set)
for sid, sym in spaces.items(): bysym[sym].add(sid)
rows = []; m = {}
for sid, sym in sorted(spaces.items()):
    cand = sym + "USDT" if sym and (sym + "USDT") in syms else ""
    if not cand: st = "none"
    elif sym in STABLE: st = "ambiguous_stable"
    elif len(sym) <= 1: st = "ambiguous_short_symbol"
    elif len(bysym[sym]) > 1: st = "ambiguous_shared_symbol"
    else: st = "matched"; m[sid] = cand
    rows.append([sid, sym, cand if st == "matched" else "", st, cand, len(bysym[sym])])
with open(os.path.join(OUT, "mapping_snapshot_binance.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(["space_id", "space_symbol", "binance_symbol", "status", "candidate_symbol", "n_spaces_with_symbol"]); w.writerows(rows)
wc = lambda p: len((p.get("body") or "").split())
mp = [p for p in ps if p["space"] and p["space"]["id"] in m]
def dedup(lst):
    last = {}; keep = []
    for p in sorted(lst, key=lambda p: p["created"]):
        t = m[p["space"]["id"]]
        if t not in last or p["created"] - last[t] >= 5 * 86400:
            keep.append(p); last[t] = p["created"]
    return keep
c = {"proposals_total": len(ps), "spaces_total": len(spaces), "spaces_matched": len(m),
     "spaces_ambiguous": sum(1 for r in rows if r[3].startswith("ambiguous")),
     "proposals_mapped": len(mp), "proposals_body_ge300_all": sum(1 for p in ps if wc(p) >= 300),
     "proposals_mapped_body_ge300": sum(1 for p in mp if wc(p) >= 300),
     "mapped_after_5d_dedup": len(dedup(mp)), "mapped_body_ge300_after_5d_dedup": len(dedup([p for p in mp if wc(p) >= 300])),
     "binance_symbols_mapped": sorted(set(m.values()))}
json.dump(c, open(os.path.join(OUT, "snapshot_counts.json"), "w"), indent=1)
open(os.path.join(SP, "kl1h_syms.txt"), "w").write("\n".join(sorted(set(m.values()))) + "\n")
print(json.dumps(c, indent=1))
print([r for r in rows if r[3] != "none"])
