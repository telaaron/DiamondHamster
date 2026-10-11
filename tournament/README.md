# Forward prompt tournament

Evidence for "which prompt is best" is collected only from weeks that had not happened when the prompt was frozen.
Background: research/methodik/review-001 (B-01 to B-03). Code: `src/diamondhamster/tournament.py`.

## Files
- `universe.json`: the 30 coins, fixed before the first round.
- `candles/<COIN>.csv`: daily Binance candles from TradingView, append-only. A closed bar never changes; a re-ingest that disagrees fails.
- `prompts.json`: frozen prompts with content hash and freeze date. A prompt counts only on rounds after its freeze date. At most 4 active.
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
