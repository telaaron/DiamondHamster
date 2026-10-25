import sys, os, re, json, csv, glob, datetime, collections
sys.path.insert(0, os.path.dirname(__file__))
from common import OUT
if len(sys.argv) > 1: OUT = sys.argv[1]
def rsc(s):
    chunks = re.findall(r'self\.__next_f\.push\(\[1,"(.*?)"\]\)</script>', s, re.S)
    out = []
    for c in chunks:
        try: out.append(json.loads('"' + c + '"'))
        except Exception: pass
    return "".join(out)
def obj_at(txt, i):
    j = txt.index("{", i); d = 0; q = False; esc = False
    for k in range(j, len(txt)):
        ch = txt[k]
        if q:
            if esc: esc = False
            elif ch == "\\": esc = True
            elif ch == '"': q = False
            continue
        if ch == '"': q = True
        elif ch == "{": d += 1
        elif ch == "}":
            d -= 1
            if d == 0: return json.loads(txt[j:k + 1])
rows = []; fmt = collections.Counter()
for fp in sorted(glob.glob(os.path.join(OUT, "unlocks_wayback", "*", "*.html"))):
    tok = fp.split(os.sep)[-2]; ts = os.path.basename(fp)[:-5]
    s = open(fp, encoding="utf-8", errors="replace").read()
    m = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', s, re.S)
    got = False
    if m:
        try:
            info = json.loads(m.group(1))["props"]["pageProps"]["info"]
            circ = float(info["token"].get("circulatingSupply") or 0)
            ne = info.get("nextEventData") or {}
            for g in ne.get("data") or []:
                a = float(g.get("amount") or 0)
                rows.append([tok, ts, ne.get("beginDate", ""), a, (a / circ * 100) if circ else "", g.get("group", ""), (ne.get("type") or "").lower(), "next_data.nextEventData"])
                got = True
            fmt["next_data"] += 1
        except Exception as e:
            fmt["next_data_err"] += 1
    else:
        txt = rsc(s); i = txt.find('"fiveUnlocks"')
        if i >= 0:
            fmt["rsc_fiveUnlocks"] += 1
            try:
                fu = obj_at(txt, i + len('"fiveUnlocks"'))
                for slot, v in fu.items():
                    for al in ((v or {}).get("data") or {}).get("allocations") or []:
                        for ins in al.get("instances") or []:
                            a = float(ins.get("amount") or 0)
                            tc = float(al.get("totalCliffUnlockAmount") or 0); pc = al.get("totalCliffToCirculatingSupply")
                            pct = (pc * a / tc) if (tc and pc is not None and ins.get("typeOfVesting") == "cliff") else ""
                            rows.append([tok, ts, ins.get("beginDate", ""), a, pct, ins.get("group", al.get("group", "")), ins.get("typeOfVesting", ""), f"rsc.fiveUnlocks.{slot}|end={ins.get('endDate','')}|perDay={ins.get('amountPerDay','')}"])
                            got = True
            except Exception:
                fmt["rsc_err"] += 1
        else:
            fmt["no_schedule"] += 1
    fmt["files_with_rows" if got else "files_without_rows"] += 1
with open(os.path.join(OUT, "unlocks_pit.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(["token", "snapshot_ts", "unlock_date", "amount", "pct_circ", "category", "vesting_type", "source"]); w.writerows(rows)
print(dict(fmt), "rows", len(rows))
