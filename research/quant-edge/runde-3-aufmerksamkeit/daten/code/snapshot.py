import sys, os, json, time
sys.path.insert(0, os.path.dirname(__file__))
from common import *
lim = RateLimiter(1.2)
START, END = 1782864000, 1790467199
Q = """query($skip:Int!,$gte:Int!){ proposals(first: 1000, skip: $skip, where:{created_gte:$gte, created_lte:%d}, orderBy:"created", orderDirection:asc){ id created start end title body choices space{id name symbol} state author network } }""" % END
seen = {}; gte = START; skip = 0
while True:
    r = get("https://hub.snapshot.org/graphql", method="POST", json={"query": Q, "variables": {"skip": skip, "gte": gte}}, limiter=lim, timeout=120, ok_statuses=(200,))
    j = r.json()
    if "errors" in j: print(j["errors"]); break
    ps = j["data"]["proposals"]
    new = 0
    for p in ps:
        if p["id"] not in seen: seen[p["id"]] = p; new += 1
    print(gte, skip, len(ps), new, len(seen), flush=True)
    if len(ps) < 1000: break
    last = ps[-1]["created"]
    if last == gte: skip += 1000
    else: gte = last; skip = 0
with open(os.path.join(OUT, "snapshot_proposals.jsonl"), "w") as f:
    for p in sorted(seen.values(), key=lambda p: (p["created"], p["id"])):
        f.write(json.dumps(p, ensure_ascii=False) + "\n")
print("total", len(seen))
