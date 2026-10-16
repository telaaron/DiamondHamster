# Runde 3, Rohdaten (Phase 3/4), Stand 2026-10-16

Only downloaded and counted here. No returns were computed or looked at.

Holdout (hard): no price/volume data point from 2025-01-01 00:00 UTC to 2026-06-30 23:59:59 UTC. Windows: W1 = 2023-01-01..2024-12-31, W2 = 2026-07-01..2026-10-15 (last complete day). Check: `holdout_check.txt`.

## Files
| File | Content |
|---|---|
| universe.csv | all 766 Binance spot pairs with quote USDT (from data.binance.vision monthly+daily listing, incl. delisted). first_date/last_date = first/last archive file (file-name metadata, may lie in the holdout), is_stable, rows_w1w2. PAXG/XAUT is_stable=0, note gold_token. FRAXUSDT is_stable=0 (since 2026 the renamed governance token, formerly FXS). |
| universe_1d/SYM.csv | 1d candles W1+W2 (ts ms UTC, open, high, low, close, volume, quote_volume). 682 symbols have data in W1/W2; 84 traded only outside them. µs timestamps (from 2025) converted to ms. |
| spread_live.csv | /api/v3/ticker/bookTicker, 6 snapshots 10 min apart (2026-10-16 ~17:05–17:55 UTC), all 766 universe symbols. Non-trading symbols show bid/ask 0 (raw API value). |
| snapshot_proposals.jsonl | hub.snapshot.org, all proposals created 2026-07-01..2026-09-26 23:59:59 UTC (971). The hub shows no proposals flagged as spam. |
| mapping_snapshot_binance.csv | space_id → binance_symbol only for an exact symbol match `<symbol>USDT` in the universe. status: matched / ambiguous_shared_symbol (>1 space with the same symbol, e.g. SNX) / ambiguous_short_symbol (1 character: A, T) / ambiguous_stable / none. candidate_symbol always filled. |
| snapshot_counts.json | counts (see below) |
| kl_1h/SYM.csv (tar.gz) | 1h candles W2 for the 30 matched symbols; 25 with data (BADGER, BAL, BIFI, DF, GHST delisted/no W2 data). |
| sec_8k_index.csv | daily-index form.*.idx 2026-07-01..2026-09-18, form exactly "8-K" (13,747). Jul 3 + Sep 7 = holidays (no file, 403). |
| company_tickers_exchange.json | SEC, unchanged. There is no "NYSE American" label (it is part of NYSE); kept: Nasdaq + NYSE. For multiple tickers per CIK, ticker = the first one, all in all_tickers. |
| sec_8k_meta.csv | 8-Ks with a ticker. **acceptance_utc comes from the filing index page ("Accepted", ET → UTC)**, because the JSON field acceptanceDateTime (column acceptance_json_raw) differs in 6,085 of 11,056 cases (often +4 h, e.g. AAPL 0000320193-26-000018: index 16:30:28 ET, JSON 00:30:28Z the next day). |
| sec_8k_docs/ (tar.gz) | 3,000 primary documents (random.seed(20261016), random.sample from the 9,596 8-Ks with a ticker and items not only ⊆ {5.07, 7.01, 9.01}, sorted by accession). 2,995 files, because co-registrants share an accession number. List: sec_8k_docs_sample.txt |
| us_1d/TICKER.csv | Yahoo chart v8, 1d, 2026-07-01..2026-10-15 (date in ET, open, high, low, close, volume; unadjusted close as delivered by Yahoo "close"). 4,247 tickers, all with data; us_short_or_delisted_tickers.txt = 73 with <80 % of the median row count. |
| us_1h/TICKER.csv (tar.gz) | Yahoo 60m, same period, ts ms UTC (bar start). |
| unlocks_cdx_tokens.csv | Wayback CDX token.unlocks.app, 171 token slugs, all daily snapshots 2023–2024. |
| unlocks_token_map.csv | slug → symbol from the page title → Binance pair (122 mapped). |
| unlocks_wayback/ (tar.gz) | 1 snapshot per month 2023-03..2024-12 per mapped token where one exists: 560 HTML files (gzip decompressed). |
| unlocks_pit.csv | extracted: token, snapshot_ts, unlock_date, amount, pct_circ, category, vesting_type, source. 822 rows, 79 tokens. |
| request.log, request_log_notes.txt, sha256.txt, holdout_check.txt, code/ | log of every request (time, HTTP, URL), checksums, holdout check, scripts |

## Unlock HTML: what is in it
- Up to about 2023-10 (Next.js pages router): `__NEXT_DATA__` with `info.nextEventData` (next cliff: date, amount, per group), `chartData` (full cumulative unlock curve per allocation, daily, as of the snapshot), allocations, circulatingSupply. unlocks_pit takes only nextEventData; chartData is still in the HTML (not exported because of size).
- About 2023-11 to early 2024 (app router RSC `self.__next_f`): `fiveUnlocks` (2 past + 3 upcoming events with instances, beginDate/endDate, cliff/linear, totalCliffToCirculatingSupply → pct_circ).
- From about 2024-Q1/Q2: no schedule in the HTML any more; fields are obfuscated (hashes). 299 of 560 files have no schedule. → A1 point-in-time is essentially usable for 2023 only.
- pct_circ: for next_data = amount / circulatingSupply at the snapshot; for RSC = the page's own totalCliffToCirculatingSupply (cliff only).
- Duplicate slug `apecoin%20` = same pages as `apecoin`.

## US price source
Yahoo first returned 429 (with a Chrome user-agent string); with UA "Mozilla/5.0" all 8,494 requests returned 200. stooq requires a JavaScript proof-of-work bot check → not used, not bypassed. Nasdaq API was a temporary fallback, not delivered.

## Not in the repo (size rule: kl_1h + us_1h > 80 MB)
sec_8k_docs/, unlocks_wayback/, kl_1h/, us_1h/ stay only as tar.gz on Aaron's MacBook in `DiamondHamster/r3-daten/` (sha256 in sha256.txt there and here):
    8fe321f11e034fa8e7e463dde5430238dc0044caf63af67946361ea7f5050397  kl_1h.tar.gz
    4c960e06bf7905146a87f4d0c9f3671377f0a6326939abc28cd6933db582749f  sec_8k_docs.tar.gz
    81c33b249f357512cd0faa86ff3bd56baed75736d2e5bd60e8fcf9a1b255942b  unlocks_wayback.tar.gz
    68d6b9005db9b67f940b45f15405b0ccdef0160f44385bf6ec23a9813b6e7f66  us_1h.tar.gz
