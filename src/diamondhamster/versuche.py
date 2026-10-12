"""Experiment playground: one experiment = one change against the current champion on a fixed dev benchmark.

Rules (research/versuche/README.md has the full text):
- Benchmark: fixed coins and Sundays after the model's knowledge cutoff, candles from tournament/candles.
- One request batch per decision week, holding one window per coin. All windows in a batch end on the
  same day, so no window contains another window's future. (Batches of consecutive weeks of one coin
  would: week 5's window shows what happened after week 1.)
- The renderer only ever receives candles up to the decision day's close. Rendered text is checked for
  calendar years and coin names before anything is sent.
- Decisions come from a fresh Claude run with no tools, no MCP, no memory, in an empty directory.
- Scoring is paired: same coins, same weeks as the champion. Timing value per decision is
  (w - mean_w of that coin) * next-week return - turnover cost; the variant minus champion difference is
  averaged over coins per week and tested over weeks.

Experiment folder (one per experiment, written only by its own thread):
  spec.json   {"id", "parent", "axis", "change", "input", "lookback", "thread"}
  prompt.md   the full prompt
  render.py   optional, defines render(df, lookback) -> str for input "custom"; df ends at the decision day
  runs/<set>/ requests, key, responses per week
  result.json written by `score`
  card.md     written by `card`
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import random
import re
from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd

from . import ai, features, snapshot, tournament
from .config import COST_PER_SIDE

HOME = Path("/mnt/project-files/research/versuche")
REPO_COPY = Path(__file__).resolve().parents[2] / "versuche"  # readable copy in the repo, without runs/
PUBLISHED = ("spec.json", "prompt.md", "render.py", "result.json", "card.md", "denken.md", "denken-B.md", "denken-C.md")
MODEL = "claude-opus-5-5"
WEEKS = [d.date() for d in pd.date_range("2026-07-05", "2026-09-27", freq="W-SUN")]
SETS = {
    "A": ["BTC", "ETH", "SOL", "XRP", "DOGE", "ADA", "LINK", "AVAX", "DOT", "LTC"],
    "B": ["BNB", "TRX", "BCH", "SHIB", "UNI", "NEAR", "APT", "SUI", "ARB", "OP"],
    "C": ["ATOM", "ETC", "FIL", "AAVE", "INJ", "HBAR", "XLM", "ICP", "PEPE", "ALGO"],
}
CHECK = ("B", "C")
REPEAT = {"A2": "A"}  # a candidate's one fixed repeat on set A; its timing is averaged with the first run (B-14)  # a candidate from set A is re-run on the other 20 coins
AXES = ("prompt", "daten", "format")
INPUTS = ("candles", "indicators", "custom")
FORBIDDEN = re.compile(r"\b(19|20)\d\d\b|\b(jan(uary)?|feb(ruary)?|mar(ch)?|apr(il)?|may|june?|july?|aug(ust)?|sept?(ember)?|oct(ober)?|nov(ember)?|dec(ember)?)\b", re.I)
# the prompt (and any knowledge block in it) gets the same calendar check, in English and German; plain "may" is a word there,
# and project-only notes (HTML comments, as in research/wissen/*.md line 1) must be stripped before they reach the decider
PROMPT_FORBIDDEN = re.compile(r"\b(19|20)\d\d\b|\b(jan(uary|uar)?|feb(ruary|ruar)?|mar(ch)?|märz|apr(il)?|mai|june?|juni|july?|juli|aug(ust)?|sept?(ember)?|oct(ober)?|okt(ober)?|nov(ember)?|dec(ember)?|dez(ember)?)\b|<!--|\bdev-", re.I)
WIN_T, CHECK_T = 2.0, 1.0
REFERENCE = "E-003M"  # fixed yardstick: a new champion must also beat it, so one lucky champion can't move the bar (B-12)


def folder(exp_id: str, home: Path = HOME) -> Path:
    return home / exp_id


def spec(exp_id: str, home: Path = HOME) -> dict:
    return json.loads((folder(exp_id, home) / "spec.json").read_text())


def champion(home: Path = HOME) -> str:
    return json.loads((home / "champion.json").read_text())["id"]


def renderer(exp_dir: Path, s: dict):
    """render(df_up_to_t, t) -> text. The candle frame never extends past t."""
    lookback = int(s.get("lookback", 180))
    kind = s.get("input", "candles")
    if kind == "candles":
        return lambda df, t: ai.compact(ai.window(df, t, lookback))
    if kind == "indicators":
        return lambda df, t: snapshot.snapshot(features.compute(df), t) + "\n" + ai.compact(ai.window(df, t, lookback))
    if kind == "custom":
        mod_spec = importlib.util.spec_from_file_location(f"render_{s['id']}", exp_dir / "render.py")
        mod = importlib.util.module_from_spec(mod_spec)
        mod_spec.loader.exec_module(mod)
        return lambda df, t: mod.render(df, lookback)
    raise ValueError(f"input must be one of {INPUTS}")


def leak_check(text: str, coins: list[str]) -> list[str]:
    problems = []
    if m := FORBIDDEN.search(text):
        problems.append(f"calendar text {m.group(0)!r}")
    for c in coins:
        if re.search(rf"\b{re.escape(c)}\b", text):
            problems.append(f"coin name {c}")
    return problems


def export(exp_id: str, which: str = "A", home: Path = HOME, candles: Path | None = None) -> list[Path]:
    """One batch per decision week with one window per coin of the set."""
    candles = candles or tournament.CANDLES
    d = folder(exp_id, home)
    s = spec(exp_id, home)
    if s.get("axis") not in AXES:
        raise ValueError(f"axis must be one of {AXES}")
    text = (d / "prompt.md").read_text()
    phash = hashlib.sha256(text.encode()).hexdigest()[:12]
    if m := PROMPT_FORBIDDEN.search(text):
        raise ValueError(f"{exp_id} prompt.md: calendar text or project note {m.group(0)!r}")
    render = renderer(d, s)
    universe = tournament.universe()
    coins_of = SETS.get(which) or SETS[REPEAT[which]]
    frames = {c: tournament.read_candles(c, candles) for c in coins_of}
    out = []
    k = int(s.get("ensemble", 1))  # ensemble: k independent batches per week, the decision is their mean weight
    memory = bool(s.get("memory"))  # the decider sees its own weight and flip price of the week before
    if memory and k > 1:
        raise ValueError("memory and ensemble together are not supported")
    every = int(s.get("every", 1))  # decide only every n-th week; the weight stands in between (see weights)
    if memory and every > 1:
        raise ValueError("memory and every together are not supported")
    for week, e in ((w, e) for w in WEEKS[::every] for e in range(1, k + 1)):
        t = pd.Timestamp(week, tz="UTC")
        last = {}
        if memory and week != WEEKS[0]:
            prev = d / "runs" / which / WEEKS[WEEKS.index(week) - 1].isoformat()
            if not (prev / "responses.json").exists():
                break  # weeks are decided one after another
            last = previous_decision(prev, frames, t)
        run = d / "runs" / which / (week.isoformat() + (f"-e{e}" if k > 1 else ""))
        if (run / "requests.json").exists():
            out.append(run)
            continue
        seed = f"{exp_id}{which}{week}" + (f"e{e}" if k > 1 else "")
        coins = list(coins_of)
        random.Random(seed).shuffle(coins)
        ids = {c: hashlib.sha256(f"{seed}{c}".encode()).hexdigest()[:10] for c in coins}
        reqs = []
        for c in coins:
            window = render(frames[c].loc[:t], t)
            if memory:
                w, f = last.get(c, (None, None))
                window = (f"last week: weight {w:.2f}, flip price {f:.1f} on today's scale" if w is not None and f is not None
                          else f"last week: weight {w:.2f}, no flip price" if w is not None else "last week: no decision") + "\n" + window
            problems = leak_check(window, universe)
            if problems:
                raise ValueError(f"{exp_id} {c} {week}: {problems}")
            reqs.append({"id": ids[c], "window": window})
        run.mkdir(parents=True, exist_ok=True)
        (run / "requests.json").write_text(json.dumps({"prompt_id": exp_id, "prompt_hash": phash, "prompt": text, "requests": reqs}, indent=1))
        (run / "key.json").write_text(json.dumps({ids[c]: c for c in coins}, indent=1))
        out.append(run)
    return out


def last_json(text: str) -> dict:
    """The JSON object an answer ends with (nested values allowed); trailing code fences are ignored."""
    dec = json.JSONDecoder()
    start = text.rfind("{")
    while start >= 0:
        try:
            obj, end = dec.raw_decode(text[start:])
            if isinstance(obj, dict) and text[start + end:].strip().strip("`").strip() == "":
                return obj
        except json.JSONDecodeError:
            pass
        start = text.rfind("{", 0, start)
    return {}


def parse_flips(text: str) -> dict[str, float]:
    """Flip prices from answers whose JSON values look like {"weight": .., "flip": ..}."""
    out = {}
    for k, v in last_json(text).items():
        if isinstance(v, dict) and isinstance(v.get("flip"), (int, float)):
            out[k] = float(v["flip"])
    return out


def previous_decision(prev: Path, frames: dict[str, pd.DataFrame], t: pd.Timestamp) -> dict[str, tuple[float, float | None]]:
    """Per coin: last week's weight and flip price, the flip rescaled from last week's 100 to today's 100."""
    key = json.loads((prev / "key.json").read_text())
    resp = json.loads((prev / "responses.json").read_text())
    flips = parse_flips(resp.get("raw", ""))
    t_prev = pd.Timestamp(prev.name[:10], tz="UTC")
    out = {}
    for i, c in key.items():
        if c not in frames or i not in resp["responses"]:
            continue
        f = flips.get(i)
        scale = frames[c].loc[t_prev, "close"] / frames[c].loc[t, "close"]
        out[c] = (float(resp["responses"][i]), f * scale if f is not None else None)
    return out


def decide(exp_id: str, which: str = "A", home: Path = HOME, workers: int = 5) -> list[Path]:
    import tempfile
    from concurrent.futures import ThreadPoolExecutor

    work = Path(tempfile.mkdtemp(prefix="decider-"))  # empty cwd: no repo, no CLAUDE.md
    if spec(exp_id, home).get("memory"):  # one week after another: each week's input holds the week before
        done = []
        while True:
            pending = [r for r in export(exp_id, which, home) if not (r / "responses.json").exists()]
            if not pending:
                return done
            done.append(ai.run_claude_cli(pending[0], MODEL, work))
    runs = sorted(r for r in (folder(exp_id, home) / "runs" / which).iterdir() if not (r / "responses.json").exists())
    with ThreadPoolExecutor(max_workers=workers) as ex:
        return list(ex.map(lambda r: ai.run_claude_cli(r, MODEL, work), runs))


def weights(exp_id: str, which: str, home: Path = HOME) -> pd.DataFrame:
    rows = []
    for run in sorted((folder(exp_id, home) / "runs" / which).glob("*")):
        if not (run / "responses.json").exists():
            continue
        key = json.loads((run / "key.json").read_text())
        resp = json.loads((run / "responses.json").read_text())["responses"]
        if missing := set(key) - set(resp):
            raise ValueError(f"{run}: answer has no weight for {len(missing)} of {len(key)} windows")
        for i, coin in key.items():
            rows.append({"decision": pd.Timestamp(run.name[:10], tz="UTC"), "coin": coin, "weight": min(max(float(resp.get(i, np.nan)), 0.0), 1.0)})
    if not rows:
        return pd.DataFrame(columns=["decision", "coin", "weight"])
    # ensemble members of the same week (<week>-e1, -e2, ...) collapse to their mean weight
    w = pd.DataFrame(rows).groupby(["decision", "coin"], as_index=False)["weight"].mean()
    if int(spec(exp_id, home).get("every", 1)) > 1:  # weeks without a decision keep the last decided weight
        grid = pd.MultiIndex.from_product([[pd.Timestamp(x, tz="UTC") for x in WEEKS], sorted(w["coin"].unique())], names=["decision", "coin"])
        w = w.set_index(["decision", "coin"]).reindex(grid).groupby(level="coin")["weight"].ffill().dropna().reset_index()
    return w


def timing(w: pd.DataFrame, closes: dict[str, pd.Series], cost: float = COST_PER_SIDE) -> pd.DataFrame:
    """Per (decision, coin): timing contribution against a constant position at the coin's mean weight."""
    w = w.copy()
    w["ret"] = tournament.forward_returns(w, closes)
    w = w.dropna(subset=["ret", "weight"]).sort_values(["coin", "decision"])
    w["mean_w"] = w.groupby("coin")["weight"].transform("mean")
    w["turnover"] = w.groupby("coin")["weight"].diff().abs().fillna(0.0)
    w["timing"] = (w["weight"] - w["mean_w"]) * w["ret"] - w["turnover"] * cost
    return w


def clean(x):
    """NaN is not valid JSON: write null instead."""
    if isinstance(x, dict):
        return {k: clean(v) for k, v in x.items()}
    return None if isinstance(x, float) and np.isnan(x) else x


def timed(exp_id: str, sets: tuple[str, ...], closes: dict[str, pd.Series], home: Path = HOME) -> pd.DataFrame:
    """Timing frame of one experiment, or of a composite reference: the mean over its runs per decision and coin.

    Averaging the timing value (not the weights) keeps the comparison fair: smoothed weights would turn over less
    and look better than any single run could."""
    runs = spec(exp_id, home).get("composite") or [exp_id]
    frames = []
    for r in runs:
        have = [k for k in sets if (folder(r, home) / "runs" / k).exists()]
        if have:
            frames.append(timing(pd.concat([weights(r, k, home) for k in have], ignore_index=True), closes))
        for rep_set, orig in REPEAT.items():  # the repeat counts as one more run of the same coins
            if orig in sets and (folder(r, home) / "runs" / rep_set).exists():
                frames.append(timing(weights(r, rep_set, home), closes))
    if not frames:
        raise ValueError(f"{exp_id}: no runs on {sets}")
    if len(frames) == 1:
        return frames[0]
    return pd.concat(frames).groupby(["decision", "coin"], as_index=False)[["weight", "ret", "timing"]].mean()


def tstat(x: pd.Series) -> float:
    x = x.dropna()
    return float(x.mean() / (x.std(ddof=1) / np.sqrt(len(x)))) if len(x) > 1 and x.std(ddof=1) > 0 else float("nan")


def compare(exp_id: str, base_id: str, sets: str | tuple[str, ...], home: Path = HOME, candles: Path | None = None) -> dict:
    """Paired comparison on the given sets, pooled: per week the mean over all coins of those sets."""
    candles = candles or tournament.CANDLES
    sets = (sets,) if isinstance(sets, str) else tuple(sets)
    coins = [c for k in sets for c in SETS[k]]
    closes = {c: tournament.read_candles(c, candles)["close"] for c in coins}
    v, b = timed(exp_id, sets, closes, home), timed(base_id, sets, closes, home)
    m = v.merge(b, on=["decision", "coin"], suffixes=("", "_base"))
    if m.empty:
        raise ValueError(f"no paired decisions for {exp_id} vs {base_id} on {sets}")
    weekly = m.groupby("decision")[["timing", "timing_base"]].mean()
    diff = weekly["timing"] - weekly["timing_base"]
    ex_best = diff.drop(diff.idxmax()) if len(diff) > 1 else diff
    ic = m.groupby("decision").apply(lambda g: g["weight"].rank().corr(g["ret"].rank()), include_groups=False)
    return {
        "sets": "+".join(sets), "coins": int(m["coin"].nunique()), "weeks": int(len(weekly)), "decisions": int(len(m)),
        "timing_week_pct": round(100 * weekly["timing"].mean(), 3), "timing_t": round(tstat(weekly["timing"]), 2),
        "base_timing_week_pct": round(100 * weekly["timing_base"].mean(), 3),
        "diff_week_pct": round(100 * diff.mean(), 3), "diff_t": round(tstat(diff), 2),
        "diff_ex_best_week_pct": round(100 * ex_best.mean(), 3), "best_week": diff.idxmax().date().isoformat(),
        "exposure": round(float(m["weight"].mean()), 3), "base_exposure": round(float(m["weight_base"].mean()), 3),
        "rank_ic": round(float(ic.mean()), 3),
        "weeks_better": int((diff > 0).sum()),
    }


def verdict(a: dict, check: dict | None, repeated: bool = True) -> str:
    """Set A filters, the other 20 coins confirm. Robust means: still ahead without its single best week."""
    t = np.nan_to_num(a["diff_t"] if a["diff_t"] is not None else np.nan)
    if t <= -WIN_T:
        return "schlechter"
    if t < WIN_T or a["diff_ex_best_week_pct"] <= 0:
        return "kein messbarer Unterschied"
    if not repeated:
        return "Kandidat: einmal auf A wiederholen (--set A2); zählt nur, wenn das Mittel beider Läufe t ≥ 2 hält"
    if check is None:
        return "Kandidat, Check-Sets B+C laufen lassen"
    if check["diff_week_pct"] > 0 and np.nan_to_num(check["diff_t"]) >= CHECK_T and check["diff_ex_best_week_pct"] > 0:
        return "neuer Dev-Champion"
    return "verworfen: hält auf B+C nicht"


def tool_version() -> str:
    """Repo commit plus the hash of this file, so a result names the exact scoring code (B-14)."""
    import subprocess
    root = Path(__file__).resolve().parents[2]
    try:
        head = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=root, capture_output=True, text=True).stdout.strip()
        blob = subprocess.run(["git", "hash-object", __file__], cwd=root, capture_output=True, text=True).stdout.strip()[:10]
        return f"{head or '?'} versuche.py@{blob or '?'}"
    except OSError:
        return "unbekannt"


def usage(exp_id: str, home: Path = HOME) -> dict:
    """What the experiment cost: Claude calls, characters sent, list-price USD as reported by the CLI."""
    calls, chars, usd = 0, 0, 0.0
    for r in (folder(exp_id, home) / "runs").glob("*/*/responses.json"):
        calls += 1
        usd += json.loads(r.read_text()).get("cost_usd") or 0.0
        chars += len((r.parent / "requests.json").read_text())
    return {"calls": calls, "chars": chars, "cost_usd_list": round(usd, 2)}


def score(exp_id: str, home: Path = HOME) -> dict:
    s = spec(exp_id, home)
    base = s.get("parent") or champion(home)
    a = compare(exp_id, base, "A", home)
    if base == exp_id:  # the reference itself: absolute numbers only
        result = {"id": exp_id, "vs": base, "A": a, "check": compare(exp_id, base, CHECK, home) if (folder(exp_id, home) / "runs" / "B").exists() else None,
                  "verdict": "Referenz", "model": MODEL, "usage": usage(exp_id, home), "tool": tool_version()}
        (folder(exp_id, home) / "result.json").write_text(json.dumps(clean(result), indent=1, ensure_ascii=False))
        return result
    ran = all((folder(x, home) / "runs" / k).exists() for x in (exp_id, base) for k in CHECK)
    check = compare(exp_id, base, CHECK, home) if ran else None
    repeated = (folder(exp_id, home) / "runs" / "A2").exists()
    result = {"id": exp_id, "vs": base, "A": a, "check": check, "verdict": verdict(a, check, repeated), "repeated_A": repeated,
              "model": MODEL, "usage": usage(exp_id, home), "tool": tool_version()}
    if result["verdict"] == "neuer Dev-Champion" and base != REFERENCE and (folder(REFERENCE, home) / "spec.json").exists():
        ref = {"A": compare(exp_id, REFERENCE, "A", home), "check": compare(exp_id, REFERENCE, CHECK, home)}
        result["vs_reference"] = ref
        if not (ref["A"]["diff_week_pct"] > 0 and ref["A"]["diff_ex_best_week_pct"] > 0 and ref["check"]["diff_week_pct"] > 0):
            result["verdict"] = f"verworfen: schlägt die feste Referenz {REFERENCE} nicht"
    (folder(exp_id, home) / "result.json").write_text(json.dumps(clean(result), indent=1, ensure_ascii=False))
    return result


def transcript(exp_id: str, which: str = "A", home: Path = HOME) -> str:
    """denken.md: the decider's full answer per week, window ids resolved to coins after the fact."""
    d = folder(exp_id, home)
    lines = [f"# {exp_id}: was die KI gedacht hat (Set {which})", "",
             "Volle Antwort des Deciders pro Entscheidungswoche, unverändert. Er sah weder Datum noch Coin-Namen; "
             "die Namen in Klammern sind erst danach eingesetzt. Gesendeter Prompt und Daten: runs/<set>/<woche>/requests.json."]
    for run in sorted((d / "runs" / which).glob("*")):
        if not (run / "responses.json").exists():
            continue
        key = json.loads((run / "key.json").read_text())
        raw = json.loads((run / "responses.json").read_text()).get("raw", "")
        for i, coin in key.items():
            raw = raw.replace(i, f"{i} ({coin})")
        lines += ["", f"## Entscheidung {run.name}", "", raw.strip()]
    text = "\n".join(lines) + "\n"
    (d / f"denken{'' if which == 'A' else '-' + which}.md").write_text(text)
    return text


def card(exp_id: str, home: Path = HOME) -> str:
    """Markdown card: what changed, the exact prompt, the data, the score and the verdict."""
    d, s = folder(exp_id, home), spec(exp_id, home)
    r = json.loads((d / "result.json").read_text()) if (d / "result.json").exists() else None
    prompt = (d / "prompt.md").read_text()
    parent = s.get("parent")
    lines = [f"# {exp_id}: {s['change']}", "", f"- Achse: {s['axis']}", f"- Basis: {parent or '(keine)'}",
             f"- Daten: {s.get('input', 'candles')}, {s.get('lookback', 180)} Tage", f"- Modell: {MODEL}"]
    if int(s.get("ensemble", 1)) > 1:
        lines.append(f"- Ensemble: {s['ensemble']} unabhängige Läufe pro Woche, entschieden wird mit ihrem mittleren Gewicht")
    if r and r.get("tool"):
        lines.append(f"- Werkzeug: {r['tool']}")
    if r and r.get("repeated_A"):
        lines.append("- Set A zweimal gelaufen (A und A2), bewertet wird das Mittel")
    if s.get("thread"):
        lines.append(f"- Thread: {s['thread']}")
    if parent and (folder(parent, home) / "prompt.md").exists():
        import difflib
        diff = difflib.unified_diff((folder(parent, home) / "prompt.md").read_text().splitlines(), prompt.splitlines(), parent, exp_id, lineterm="")
        lines += ["", "## Änderung zum Prompt der Basis", "```diff", *diff, "```"]
    lines += ["", "## Prompt", "```", prompt.strip(), "```"]
    if s.get("input") == "custom" and (d / "render.py").exists():
        lines += ["", "## Datenaufbereitung (render.py)", "```python", (d / "render.py").read_text().strip(), "```"]
    if r:
        lines += ["", f"## Bewertung gegen {r['vs']}", "", "| Coins | Wochen | Entscheidungen | Timing-Wert/Woche | Basis | Differenz | t | ohne beste Woche | Wochen besser | Exposure | Rank-IC |", "|---|---|---|---|---|---|---|---|---|---|---|"]
        for x in (r.get("A"), r.get("check")):
            if x:
                lines.append(f"| {x['sets']} ({x['coins']}) | {x['weeks']} | {x['decisions']} | {x['timing_week_pct']} % | {x['base_timing_week_pct']} % | {x['diff_week_pct']} % | {x['diff_t']} | {x['diff_ex_best_week_pct']} % (ohne {x['best_week']}) | {x['weeks_better']}/{x['weeks']} | {x['exposure']} (Basis {x['base_exposure']}) | {x['rank_ic']} |")
        u = r.get("usage", {})
        lines += ["", f"**Urteil: {r['verdict']}**", "", f"Verbrauch: {u.get('calls')} Claude-Aufrufe, {u.get('chars', 0) // 1000}k Zeichen, Listenpreis {u.get('cost_usd_list')} USD (zählt gegen Aarons Limit, keine Rechnung)"]
    first = sorted((d / "runs" / "A").glob("*/responses.json"))
    if first:
        transcript(exp_id, "A", home)
        key = json.loads((first[0].parent / "key.json").read_text())
        raw = json.loads(first[0].read_text()).get("raw", "")
        for i, coin in key.items():
            raw = raw.replace(i, f"{i} ({coin})")
        lines += ["", f"## Was die KI gedacht hat (Beispiel: Entscheidung {first[0].parent.name})", "",
                  "Alle Wochen: [denken.md](denken.md)", "", "````", raw.strip(), "````"]
    if s.get("notes"):
        lines += ["", "## Notizen", s["notes"]]
    text = "\n".join(lines) + "\n"
    (d / "card.md").write_text(text)
    return text


def overview(home: Path = HOME) -> str:
    """UEBERSICHT.md: one line per experiment, rebuilt from the folders, plus the multiple-testing counter."""
    champ = champion(home) if (home / "champion.json").exists() else None
    exps = sorted(p for p in home.glob("E-*") if (p / "spec.json").exists())
    results = {d.name: json.loads((d / "result.json").read_text()) for d in exps if (d / "result.json").exists()}
    tested = sum(1 for r in results.values() if r.get("vs") != r.get("id"))
    usd = sum((r.get("usage") or {}).get("cost_usd_list") or 0 for r in results.values())
    rows = ["# Versuche: Übersicht", "", f"Dev-Champion: **{champ}**" if champ else "Dev-Champion: (noch keiner)",
            f"Varianten bisher getestet: **{tested}**. Je mehr Varianten, desto sicherer ist die beste davon auch Glück: "
            "ein Dev-Sieg ist nur ein Filter, zählen tut das Turnier.",
            f"Verbrauch gesamt: {usd:.0f} USD Listenpreis (gegen Aarons Claude-Limit)", "",
            "| ID | Achse | Änderung | Basis | Diff/Woche A | t | ohne beste Woche | B+C | Urteil | Thread |", "|---|---|---|---|---|---|---|---|---|---|"]
    for d in exps:
        s = json.loads((d / "spec.json").read_text())
        r = results.get(d.name, {})
        a, c = r.get("A") or {}, r.get("check") or {}
        thread = f"[Thread]({s['thread']})" if s.get("thread") else ""
        if r.get("verdict") == "Referenz":  # no difference to show: its own timing value instead
            rows.append(f"| [{s['id']}]({d.name}/card.md) | {s['axis']} | {s['change']} | - | eigener Wert {a.get('timing_week_pct')} | {a.get('timing_t')} | | eigener Wert {c.get('timing_week_pct', '')} | Referenz | {thread} |")
            continue
        rows.append(f"| [{s['id']}]({d.name}/card.md) | {s['axis']} | {s['change']} | {s.get('parent') or '-'} | {a.get('diff_week_pct', '')} | {a.get('diff_t', '')} | {a.get('diff_ex_best_week_pct', '')} | {c.get('diff_week_pct', '')} | {r.get('verdict', 'läuft')} | {thread} |")
    text = "\n".join(rows) + "\n"
    (home / "UEBERSICHT.md").write_text(text)
    return text


def publish(home: Path = HOME, dest: Path = REPO_COPY) -> list[Path]:
    """Copy the readable part of every experiment into the repo: specs, prompts, results, cards, reasoning. Not runs/."""
    written = []
    for name in ("README.md", "UEBERSICHT.md", "backlog.md", "champion.json"):
        if (home / name).exists():
            written.append(dest / name)
            written[-1].parent.mkdir(parents=True, exist_ok=True)
            written[-1].write_text((home / name).read_text())
    for d in sorted(p for p in home.glob("E-*") if (p / "spec.json").exists()):
        for name in PUBLISHED:
            if (d / name).exists():
                out = dest / d.name / name
                out.parent.mkdir(parents=True, exist_ok=True)
                out.write_text((d / name).read_text())
                written.append(out)
    return written


if __name__ == "__main__":
    import argparse

    p = argparse.ArgumentParser(prog="python -m diamondhamster.versuche")
    p.add_argument("cmd", choices=["export", "decide", "run", "score", "card", "overview", "publish"])
    p.add_argument("exp_id", nargs="?")
    p.add_argument("--set", default="A", choices=[*SETS, *REPEAT])
    p.add_argument("--home", type=Path, default=HOME)
    a = p.parse_args()
    if a.cmd == "overview":
        print(overview(a.home))
    elif a.cmd == "publish":
        print(len(publish(a.home)), "files copied to", REPO_COPY)
    elif a.cmd == "export":
        print(len(export(a.exp_id, a.set, a.home)), "batches")
    elif a.cmd == "decide":
        print(len(decide(a.exp_id, a.set, a.home)), "batches answered")
    elif a.cmd == "run":
        export(a.exp_id, a.set, a.home)
        decide(a.exp_id, a.set, a.home)
        print(json.dumps(score(a.exp_id, a.home), indent=1, ensure_ascii=False))
    elif a.cmd == "score":
        print(json.dumps(score(a.exp_id, a.home), indent=1, ensure_ascii=False))
    else:
        print(card(a.exp_id, a.home))
