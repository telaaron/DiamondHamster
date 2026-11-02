"""X-Daten-Probe: testet kostenlose Routen an X-Posts und Replies.

Laeuft auf Aarons Mac (aus der Cloud blockt X mit 403). Nur stdlib fuer die
login-freien Routen; twscrape optional fuer die Burner-Route.

    python3 research/x-daten/x_probe.py                       # alle login-freien Routen
    python3 research/x-daten/x_probe.py --twscrape            # zusaetzlich Burner-Route
    python3 research/x-daten/x_probe.py --users a,b,c --out /tmp/x

Ausgabe: <out>/<route>.jsonl (ein Post pro Zeile) + <out>/summary.json.
Langsam mit Absicht: 3-6 s Pause zwischen Requests, kein Parallelismus.
"""
from __future__ import annotations

import argparse
import asyncio
import html
import json
import os
import random
import re
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

DEFAULT_USERS = ["APompliano", "woonomic", "CryptoHayes"]
NITTER = [
    "xcancel.com",
    "nitter.poast.org",
    "nitter.privacyredirect.com",
    "nitter.tiekoetter.com",
    "nuku.trabun.org",
    "nitter.catsarch.com",
    "nitter.kareem.one",
]
UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/129.0 Safari/537.36"
)


def get(url: str, timeout: int = 20) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception as e:  # DNS, TLS, timeout
        return -1, f"{type(e).__name__}: {e}"


def pause() -> None:
    time.sleep(random.uniform(3, 6))


# ---------- Route 1: Nitter / xcancel RSS + Reply-Seite ----------

def nitter_rss(inst: str, user: str) -> tuple[int, list[dict]]:
    code, body = get(f"https://{inst}/{user}/rss")
    if code != 200 or not body.lstrip().startswith("<"):
        return code, []
    try:
        root = ET.fromstring(body)
    except ET.ParseError:
        return -2, []  # z.B. Bot-Challenge-HTML statt RSS
    posts = []
    for it in root.iter("item"):
        link = it.findtext("link") or ""
        m = re.search(r"/status/(\d+)", link)
        posts.append({
            "route": "nitter_rss", "instance": inst, "user": user,
            "id": m.group(1) if m else None,
            "date": it.findtext("pubDate"),
            "text": html.unescape(re.sub(r"<[^>]+>", " ", it.findtext("description") or "")).strip(),
        })
    return code, posts


def nitter_replies(inst: str, user: str, tweet_id: str) -> tuple[int, list[dict]]:
    """Erste Seite Replies aus der Nitter-Statusseite (HTML)."""
    code, body = get(f"https://{inst}/{user}/status/{tweet_id}")
    if code != 200:
        return code, []
    replies = []
    # Nitter-Markup: <div class="reply thread thread-line"> ... <a class="username" ...>@x</a> ... <div class="tweet-content media-body" dir="auto">TEXT</div>
    section = body.split('id="r"', 1)[-1] if 'id="r"' in body else body.split("replies", 1)[-1]
    for m in re.finditer(
        r'class="username"[^>]*>@?([^<]+)</a>.*?class="tweet-content[^"]*"[^>]*>(.*?)</div>',
        section, re.S,
    ):
        author, txt = m.group(1).strip(), html.unescape(re.sub(r"<[^>]+>", "", m.group(2))).strip()
        if author.lower() == user.lower():
            continue
        replies.append({"route": "nitter_replies", "instance": inst, "parent": tweet_id,
                        "user": author, "text": txt})
    return code, replies


# ---------- Route 2: Syndication (Embed-Widget, kein Login) ----------

def syndication_timeline(user: str) -> tuple[int, list[dict]]:
    code, body = get(f"https://syndication.twitter.com/srv/timeline-profile/screen-name/{user}")
    if code != 200:
        return code, []
    m = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', body, re.S)
    if not m:
        return -2, []
    data = json.loads(m.group(1))
    entries = (data.get("props", {}).get("pageProps", {}).get("timeline", {}) or {}).get("entries", [])
    posts = []
    for e in entries:
        t = (e.get("content") or {}).get("tweet") or {}
        if t:
            posts.append({"route": "syndication", "user": user, "id": t.get("id_str"),
                          "date": t.get("created_at"), "text": t.get("full_text") or t.get("text"),
                          "replies": t.get("reply_count")})
    return code, posts


def syndication_tweet(tweet_id: str) -> tuple[int, dict | None]:
    token = random.randint(1, 10**8)
    code, body = get(f"https://cdn.syndication.twimg.com/tweet-result?id={tweet_id}&token={token}")
    if code != 200 or not body:
        return code, None
    try:
        t = json.loads(body)
    except json.JSONDecodeError:
        return -2, None
    return code, {"route": "syndication_tweet", "id": tweet_id, "text": t.get("text"),
                  "replies": t.get("conversation_count")}


# ---------- Route 3: twscrape mit Burner-Account (Cookies) ----------

async def twscrape_route(users: list[str], db: str, n_posts: int, n_replies: int) -> dict:
    try:
        from twscrape import API, gather
    except ImportError:
        return {"status": "nicht installiert (pip install twscrape)"}
    os.environ.setdefault("TWS_TELEMETRY", "0")
    api = API(db, raise_when_no_account=True)
    accs = await api.pool.accounts_info()
    if not accs:
        return {"status": f"kein Account in {db}; siehe README Schritt Burner"}
    out: dict = {"status": "ok", "posts": [], "replies": []}
    for u in users:
        user = await api.user_by_login(u)
        if not user:
            out.setdefault("errors", []).append(f"user {u} nicht gefunden")
            continue
        tweets = await gather(api.user_tweets(user.id, limit=n_posts))
        tweets = [t for t in tweets if t.user.username.lower() == u.lower()][:n_posts]
        for t in tweets:
            out["posts"].append({"route": "twscrape", "user": u, "id": str(t.id),
                                 "date": t.date.isoformat(), "text": t.rawContent,
                                 "replies": t.replyCount, "likes": t.likeCount})
        for t in tweets[:2]:  # Replies fuer die 2 neuesten Posts
            await asyncio.sleep(random.uniform(3, 6))
            reps = await gather(api.tweet_replies(t.id, limit=n_replies))
            for r in reps:
                out["replies"].append({"route": "twscrape_replies", "parent": str(t.id),
                                       "user": r.user.username, "date": r.date.isoformat(),
                                       "text": r.rawContent, "likes": r.likeCount})
        await asyncio.sleep(random.uniform(3, 6))
    return out


def dump(path: Path, rows: list[dict]) -> None:
    with path.open("w") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--users", default=",".join(DEFAULT_USERS))
    ap.add_argument("--out", default="research/x-daten/probe-out")
    ap.add_argument("--twscrape", action="store_true")
    ap.add_argument("--db", default=os.path.expanduser("~/.diamondhamster/x-accounts.db"))
    ap.add_argument("--skip-nitter", action="store_true")
    args = ap.parse_args()
    users = [u.strip().lstrip("@") for u in args.users.split(",") if u.strip()]
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    summary: dict = {"time": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "users": users, "routes": {}}

    nitter_rows: list[dict] = []
    # Nitter: jede Instanz mit dem 1. User testen, erste funktionierende fuer alle nutzen
    if not args.skip_nitter:
        inst_status, working = {}, None
        for inst in NITTER:
            code, posts = nitter_rss(inst, users[0])
            inst_status[inst] = {"http": code, "posts": len(posts)}
            print(f"nitter {inst:32s} http={code} posts={len(posts)}", flush=True)
            if posts and not working:
                working = inst
            pause()
        rows, reps = [], []
        if working:
            for u in users:
                code, posts = nitter_rss(working, u)
                rows += posts
                pause()
                if posts and posts[0]["id"]:
                    rc, r = nitter_replies(working, u, posts[0]["id"])
                    reps += r
                    print(f"nitter replies {u}: http={rc} n={len(r)}", flush=True)
                    pause()
        nitter_rows = rows
        dump(out / "nitter_posts.jsonl", rows)
        dump(out / "nitter_replies.jsonl", reps)
        summary["routes"]["nitter"] = {"instances": inst_status, "used": working,
                                       "posts": len(rows), "replies": len(reps)}

    # Syndication
    rows, st = [], {}
    for u in users:
        code, posts = syndication_timeline(u)
        st[u] = {"http": code, "posts": len(posts)}
        print(f"syndication {u}: http={code} posts={len(posts)}", flush=True)
        rows += posts
        pause()
    probe_id = next((r["id"] for r in rows + nitter_rows if r.get("id")), None)
    single = None
    if probe_id:
        code, single = syndication_tweet(probe_id)
        print(f"syndication tweet-result {probe_id}: http={code} ok={bool(single)}", flush=True)
    dump(out / "syndication_posts.jsonl", rows)
    summary["routes"]["syndication"] = {"timeline": st, "tweet_result": bool(single)}

    if args.twscrape:
        res = asyncio.run(twscrape_route(users, args.db, n_posts=5, n_replies=40))
        dump(out / "twscrape_posts.jsonl", res.get("posts", []))
        dump(out / "twscrape_replies.jsonl", res.get("replies", []))
        summary["routes"]["twscrape"] = {k: (len(v) if isinstance(v, list) else v) for k, v in res.items()}
        print(f"twscrape: {summary['routes']['twscrape']}", flush=True)

    (out / "summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False))
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
