# H-002: QS-Klassen je Zyklus ("Harms BTC")

- Date: 2026-10-11 (written before any test was run)
- Author: Fynn (indicator from a third party), test design by Claude for Aaron
- Observation: A Pine script (`indicators/qs_zyklen.pine`) marks calendar days whose "iterated digit sum" (QS) of
  the day count since a bear-market low falls in one of two classes per cycle (2011: 4/6, 2015: 6/3,
  2018: 3/5, 2022: 5/9). Its author claims high success rates. The script itself gives no direction and no
  buy or sell signal, and "success" is not defined.
- Hypothesis: price turns (swing highs and lows) fall on QS hit days clearly more often than on other days,
  i.e. hit days are about 2/9 of all days but carry clearly more than 2/9 of the turns.
- Mechanism: none known. QS of a day count mod 9 is pure calendar arithmetic. The only plausible routes are
  (a) self-fulfilling attention by people who use it, (b) chance, (c) selection: the class pair per cycle
  was chosen by looking at the chart. (c) is the main risk and is tested explicitly.
- Data: TradingView `INDEX:BTCUSD` daily (the feed the anchors match: all four anchors are the lowest low
  within +-60 days on this feed), 2011-11-17 to 2024-12-31. Holdout 2025-01-01..2026-06-30 is not touched.
  Validation slice 2023-01-01..2024-12-31 reported separately.

## Test (fixed before running)

Calendar: exact port of the Pine logic (`src/diamondhamster/qs.py`), UTC calendar days, anchor = day 0
(never a hit), QS(n) = 1 + (n-1) mod 9. Default 2015 anchor 2015-08-18.

Turn events, defined without looking at QS days:
- E1 (primary): swing high or swing low with k = 14: high[t] is the max of high over [t-14, t+14], or
  low[t] is the min of low over [t-14, t+14]. Anchor days excluded. Days whose window is cut by the data
  edge are excluded.
- E2..E6 (secondary, reported, counted as tested variants): k = 7, k = 30, k = 14 lows only,
  k = 14 highs only, RSI(14, Wilder on close) swing with k = 14.

Statistic: H = number of events that land on a hit day. Null distribution: replace the four class pairs by
every one of the 36 possible pairs per cycle, independently, i.e. all 36^4 = 1,679,616 combinations
(exact, by convolution). This also covers shifted anchors, since shifting an anchor by s days equals
shifting both classes by s. p = share of combinations with H >= observed H. Lift = observed hit share of
events / hit share of all days.

Selection check: rank of the chosen pair among the 36 pairs in each cycle on E1. A chosen pair that ranks
at or near the top in every cycle while the pooled lift is high is what selection by eye looks like, and
then the in-sample result proves nothing.

Trading check (secondary): signal S = close is the lowest close of the last 14 days. Rule: hold 1.0 for 30
days after a signal (signal at close t, entry at open t+1, re-signals extend the hold), else flat, costs
0.2 % per side. Compare QS-filtered (S on a hit day) vs unfiltered S, vs 2,000 random class-pair
combinations used as filter, vs buy and hold and monthly DCA.

## Refuted if (fixed before testing)

- Primary: E1 p >= 0.05 against the class-pair null, or E1 lift < 1.2. Either one refutes.
- Secondary variants count as 5 more tests; one of them alone under p < 0.05 is not evidence (Bonferroni
  threshold 0.05 / 6 = 0.0083).
- Trading: QS-filtered Sharpe after costs not above the unfiltered rule, or below the 95th percentile of
  random-pair filters. Either one means the time model adds nothing to the signal.
- Even if not refuted in-sample: if the chosen pair ranks top 3 of 36 in at least 3 of 4 cycles, the
  result is marked "consistent with selection" and only data after the pair was fixed counts.

## Result (2026-10-11, commit eaf5453, `python experiments/h002_qs_backtest.py`)

Period 2011-11-17..2024-12-31, holdout not opened. Hit days are 22.2 % of all days.

| Events | n | on hit days | share | lift | p (36^4 class pairs) | rank of chosen pair 2011/2015/2018/2022 |
|---|---|---|---|---|---|---|
| E1 swing k=14 (primary) | 195 | 51 | 26.2 % | 1.18 | 0.078 | 26 / 4 / 2 / 9 |
| E2 swing k=7 | 397 | 100 | 25.2 % | 1.13 | 0.070 | 28 / 2 / 8 / 1 |
| E3 swing k=30 | 92 | 25 | 27.2 % | 1.22 | 0.175 | 19 / 1 / 18 / 5 |
| E4 lows k=14 | 95 | 26 | 27.4 % | 1.23 | 0.147 | 15 / 3 / 2 / 19 |
| E5 highs k=14 | 100 | 25 | 25.0 % | 1.12 | 0.262 | 31 / 9 / 7 / 6 |
| E6 RSI swing k=14 | 249 | 68 | 27.3 % | 1.23 | 0.068 | 12 / 14 / 2 / 5 |

E1 per cycle (lift): 2011 0.87, 2015 1.30, 2018 1.40, 2022-2024 1.06.
Validation 2023-01..2024-12: 7 of 32 turns on hit days = 21.9 % against a 22.3 % base rate (lift 0.98).

Trading check (close = 14-day low, hold 30 days, 0.2 % per side, 2011-11-17..2024-12-31):

| Rule | CAGR | Sharpe | Max DD | Exposure |
|---|---|---|---|---|
| with QS filter | 19 % | 0.60 | -62 % | 42 % |
| without filter | 41 % | 0.86 | -80 % | 72 % |
| buy and hold | 125 % | 1.41 | -85 % | 100 % |

QS-filtered Sharpe sits at the 78th percentile of 2,000 random class-pair filters (95th percentile = 0.75).
Monthly DCA: IRR 108 %.

- Primary criterion: p = 0.078 >= 0.05 and lift 1.18 < 1.2. **Refuted.**
- Trading: the QS filter lowers Sharpe against the same signal without it and does not reach the 95th
  percentile of random filters. **Refuted.**
- Selection check: chosen pair in the top 3 in only 1 of 4 cycles on E1, so the weak in-sample lift does not
  even look like a strong fit; 2011 is below chance, and the 2023-24 slice shows no effect at all.
- Variants tested: 7 rows in experiments/log.csv (E1..E6, trading rule).
- Decision: **drop.** Holdout stays closed; spending it on a hypothesis that fails in-sample would waste it.
  If Fynn wants it kept alive, the only fair test left is paper-forward from today with the 2022 pair 5/9,
  scored with the same E1 statistic.
