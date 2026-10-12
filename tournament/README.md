# Forward prompt tournament

Evidence for "which prompt is best" is collected only from weeks that had not happened when the prompt was frozen.
Background: research/methodik/review-001 (B-01 to B-03). Code: `src/diamondhamster/tournament.py`.

## Files
- `universe.json`: the 30 coins, fixed before the first round.
- `candles/<COIN>.csv`: daily Binance candles from TradingView, append-only. A closed bar never changes; a re-ingest that disagrees fails.
- `prompts.json`: frozen prompts with content hash, freeze date and input (`candles`, or `indicators` = indicator line from `snapshot.py` before the window). A prompt counts only on rounds after its freeze date. At most 4 active.
- `rounds/<sunday>/`: one request batch per prompt and repeat (`requests.json`, `key.json` id -> coin, `responses.json`), plus `round.json` with the coins used.
- `scores_weekly.csv`: one row per prompt and finished week.

## Metrics
- **Timing value** (primary): prompt weights minus a constant position at the prompt's own mean weight on that coin, minus turnover cost, averaged over coins per week. t-statistic over weeks, because coins move together.
- **Rank IC**: Spearman correlation between weight and next-week return across coins (selection, not timing).
- **vs hold**: weights minus always fully invested (secondary).

## Weekly run (Monday shortly after 00:00 UTC, decision = the Sunday close before)
1. For every coin in `universe.json`: TradingView `get_ohlcv` with `symbol=BINANCE:<COIN>USDT`, `interval=1D`, `count=1000`. The response is large, so the harness saves it to a file; pass that file on unchanged. Never retype bars by hand.
2. `python -m diamondhamster.tournament ingest --today <monday> --last 1000 <files>`: drops Monday's still-forming bar and checks every bar.
3. `python -m diamondhamster.tournament score`: scores every round whose week is now over.
4. `python -m diamondhamster.tournament export <sunday>` then `decide <sunday>`: fresh tool-less Claude runs, 3 repeats per active prompt.
5. Commit candles, round and scores; push.

The decider never sees dates, coin names or anything after the Sunday close.

## Blocker on a round day: every one has a default (Wächter B-15, 2026-10-12)
A round must never wait on an answer. The first round sat blocked for 6 hours on a question nobody answered. So every blocker below has a default that applies on its own. A card may still go to Aaron, but it names the default and says that it applies after **2 hours** without an answer; the round thread then carries on and logs what it did in `round.json` (`notes`).

| Blocker | Default |
|---|---|
| Re-ingest shows changed **volume** on closed bars (≤ 0.1 %) | accept, keep the stored history, log every difference (built into `ingest`) |
| Re-ingest shows changed **prices** on closed bars, or volume > 0.1 % | keep the stored history unchanged, use it for the round, log the difference; the research thread looks at it afterwards |
| A coin has no data or fails the bar checks | leave that coin out of this round (`skipped` in `round.json`), run the rest |
| The Sunday bar is not closed or not available yet | wait and retry; the round may run any time before the next Sunday, since the windows end at the Sunday close anyway |
| A decider batch fails (API error, refusal, no JSON) | retry that batch once; if it fails again, archive it and count that prompt and repeat as "no decision" for the week; the other prompts and repeats still count |
| Usage limit reached | stop, resume when the limit resets, same rules as above |
| Anything not listed | the option the round thread recommends on its card, after 2 hours |

Rules never change during a round: no edits to frozen prompts, the universe, or scoring to get a round through.
