"""X-Collector fuer H-X1 (siehe PREREGISTRIERUNG.md).

Ein Lauf = ein Durchgang ueber alle Accounts aus accounts-v1.csv:
  1. Timeline jedes Accounts (neueste ~20 Posts) roh speichern.
  2. Fuer jeden eigenen Post, der 3-24 h alt ist und noch keine Replies hat:
     einmal Replies holen (max. 40, Reihenfolge wie X sie zeigt), roh speichern.
Gedacht fuer launchd alle 30 min auf dem Mac (siehe README).

    python research/x-daten/collector.py --dry-run     # prueft Setup, kein Netz
    python research/x-daten/collector.py               # ein Durchgang

Rohdaten: <data>/raw/YYYY-MM-DD/HHMMSS_<endpoint>_<id>_pN.json.gz + .request.json,
Tages-Manifest <data>/raw/YYYY-MM-DD/sha256.txt (append-only).
Zustand: <data>/state.sqlite (gesehene Posts, Reply-Abrufe).
"""
from __future__ import annotations

import argparse
import asyncio
import csv
import gzip
import hashlib
import json
import os
import random
import re
import sqlite3
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
PREREG = HERE / "PREREGISTRIERUNG.md"
ACCOUNTS = HERE / "accounts-v1.csv"
DEFAULT_DATA = Path(os.path.expanduser("~/.diamondhamster/x-daten"))
DEFAULT_DB = Path(os.path.expanduser("~/.diamondhamster/x-accounts.db"))

POSTS_PER_FETCH = 20
REPLIES_PER_POST = 40
REPLY_MIN_AGE = timedelta(hours=3)
REPLY_MAX_AGE = timedelta(hours=24)


# ---------- Vorbedingungen ----------

def prereg_frozen(text: str) -> bool:
    """Eingefroren = Zeile 'Eingefroren am: <Datum>' mit echtem Datum."""
    return re.search(r"Eingefroren am:\s*\d{4}-\d{2}-\d{2}", text) is not None


def load_accounts(path: Path) -> list[dict]:
    with path.open(newline="") as f:
        rows = [r for r in csv.DictReader(f) if (r.get("user_id") or "").strip()]
    for r in rows:
        r["user_id"] = int(r["user_id"])
    return rows


# ---------- Rohdaten ----------

def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def store_raw(data_dir: Path, now: datetime, endpoint: str, obj_id: int | str, page: int,
              payload: dict, request: dict) -> Path:
    """Schreibt Payload (gz) + request.json, haengt beide Hashes ans Tagesmanifest.
    Ueberschreibt nie: existiert der Name, wird ein Suffix angehaengt."""
    day = data_dir / "raw" / now.strftime("%Y-%m-%d")
    day.mkdir(parents=True, exist_ok=True)
    base = f"{now.strftime('%H%M%S')}_{endpoint}_{obj_id}_p{page}"
    n = 0
    while (day / f"{base}.json.gz").exists():
        n += 1
        base = f"{now.strftime('%H%M%S')}_{endpoint}_{obj_id}_p{page}_{n}"
    body = gzip.compress(json.dumps(payload, ensure_ascii=False).encode(), mtime=0)
    req = json.dumps({**request, "fetched_utc": now.isoformat()}, indent=2).encode()
    (day / f"{base}.json.gz").write_bytes(body)
    (day / f"{base}.request.json").write_bytes(req)
    with (day / "sha256.txt").open("a") as m:
        m.write(f"{sha256_bytes(body)}  {base}.json.gz\n")
        m.write(f"{sha256_bytes(req)}  {base}.request.json\n")
    return day / f"{base}.json.gz"


# ---------- Zustand ----------

def open_state(data_dir: Path) -> sqlite3.Connection:
    data_dir.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(data_dir / "state.sqlite")
    con.execute("""create table if not exists posts(
        tweet_id integer primary key, user_id integer, created_utc text,
        first_seen_utc text, replies_fetched_utc text)""")
    con.execute("""create table if not exists runs(
        started_utc text, finished_utc text, accounts_ok integer, accounts_err integer,
        reply_fetches integer, error text)""")
    return con


def due_for_replies(con: sqlite3.Connection, now: datetime) -> list[tuple[int, int]]:
    lo = (now - REPLY_MAX_AGE).isoformat()
    hi = (now - REPLY_MIN_AGE).isoformat()
    return con.execute(
        "select tweet_id, user_id from posts where replies_fetched_utc is null "
        "and created_utc between ? and ? order by created_utc", (lo, hi)).fetchall()


# ---------- Netz (twscrape) ----------

async def run_once(data_dir: Path, db: Path, accounts: list[dict]) -> dict:
    os.environ.setdefault("TWS_TELEMETRY", "0")
    from importlib.metadata import version

    from twscrape import API
    from twscrape.models import parse_tweets

    api = API(str(db), raise_when_no_account=True)
    con = open_state(data_dir)
    started = datetime.now(timezone.utc)
    stats = {"accounts_ok": 0, "accounts_err": 0, "reply_fetches": 0, "errors": []}
    meta = {"route": "twscrape", "twscrape": version("twscrape")}

    for acc in accounts:
        uid = acc["user_id"]
        try:
            page = 0
            async for rep in api.user_tweets_raw(uid, limit=POSTS_PER_FETCH):
                now = datetime.now(timezone.utc)
                payload = rep.json()
                store_raw(data_dir, now, "UserTweets", uid, page, payload,
                          {**meta, "endpoint": "UserTweets", "user_id": uid,
                           "handle": acc.get("handle"), "limit": POSTS_PER_FETCH})
                for t in parse_tweets(payload):
                    if t.user.id != uid or t.retweetedTweet is not None:
                        continue
                    con.execute("insert or ignore into posts(tweet_id,user_id,created_utc,first_seen_utc) "
                                "values(?,?,?,?)", (t.id, uid, t.date.astimezone(timezone.utc).isoformat(),
                                                    now.isoformat()))
                page += 1
            con.commit()
            stats["accounts_ok"] += 1
        except Exception as e:  # ein kaputter Account stoppt den Lauf nicht
            stats["accounts_err"] += 1
            stats["errors"].append(f"{uid}: {type(e).__name__}: {e}"[:300])
        await asyncio.sleep(random.uniform(3, 6))

    for tweet_id, uid in due_for_replies(con, datetime.now(timezone.utc)):
        try:
            page = 0
            async for rep in api.tweet_replies_raw(tweet_id, limit=REPLIES_PER_POST):
                store_raw(data_dir, datetime.now(timezone.utc), "TweetDetail", tweet_id, page, rep.json(),
                          {**meta, "endpoint": "TweetDetail", "tweet_id": tweet_id, "user_id": uid,
                           "limit": REPLIES_PER_POST})
                page += 1
            con.execute("update posts set replies_fetched_utc=? where tweet_id=?",
                        (datetime.now(timezone.utc).isoformat(), tweet_id))
            con.commit()
            stats["reply_fetches"] += 1
        except Exception as e:
            stats["errors"].append(f"replies {tweet_id}: {type(e).__name__}: {e}"[:300])
        await asyncio.sleep(random.uniform(3, 6))

    con.execute("insert into runs values(?,?,?,?,?,?)",
                (started.isoformat(), datetime.now(timezone.utc).isoformat(), stats["accounts_ok"],
                 stats["accounts_err"], stats["reply_fetches"], json.dumps(stats["errors"])[:2000]))
    con.commit()
    return stats


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", type=Path, default=DEFAULT_DATA)
    ap.add_argument("--db", type=Path, default=DEFAULT_DB)
    ap.add_argument("--accounts", type=Path, default=ACCOUNTS)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--allow-unfrozen", action="store_true",
                    help="nur fuer Technik-Tests; Daten landen in <data>/TEST-unfrozen, zaehlen nie fuer H-X1")
    args = ap.parse_args(argv)

    problems = []
    frozen = PREREG.exists() and prereg_frozen(PREREG.read_text())
    if not frozen and not args.allow_unfrozen:
        problems.append("PREREGISTRIERUNG.md ist nicht eingefroren (B-24)")
    if not args.accounts.exists():
        problems.append(f"{args.accounts.name} fehlt")
        accounts = []
    else:
        accounts = load_accounts(args.accounts)
        if not accounts:
            problems.append(f"{args.accounts.name} ohne user_id-Zeilen")
    if not args.db.exists():
        problems.append(f"twscrape-DB {args.db} fehlt (Burner, README)")
    if problems:
        print("NICHT GESTARTET:\n- " + "\n- ".join(problems))
        return 2
    data = args.data if frozen else args.data / "TEST-unfrozen"
    if args.dry_run:
        print(f"OK: {len(accounts)} Accounts, Daten nach {data}")
        return 0
    stats = asyncio.run(run_once(data, args.db, accounts))
    print(json.dumps(stats, ensure_ascii=False))
    return 0 if stats["accounts_ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
