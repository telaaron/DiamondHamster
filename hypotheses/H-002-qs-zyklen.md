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

## Result

(only after the test, see below)
