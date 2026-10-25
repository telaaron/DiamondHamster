# E-018: was die KI gedacht hat (Set A)

Volle Antwort des Deciders pro Entscheidungswoche, unverändert. Er sah weder Datum noch Coin-Namen; die Namen in Klammern sind erst danach eingesetzt. Gesendeter Prompt und Daten: runs/<set>/<woche>/requests.json.

## Entscheidung 2026-07-05

# Weekly position decision: 10 windows

## Strategy
The only rule I treat as reliable is time-series momentum over 1 to 4 weeks, long-only. Volatility sets position size, not direction. All ten windows are in a long downtrend that dropped hard around day −33 to −30. Each then made a second low around day −10 and rallied about 8–15 % in the last week. One strong week alone is not momentum, so I only add weight above the low default (about 0.15–0.2) when the 2–4-week picture agrees: higher lows, or a weekly close above the post-crash range high. High volatility caps the size.

## 3c6630209f (DOT)
- **Read:** Downtrend from about 250 to 100, with a clear sequence of lower highs: 163 (−53), 118.8 (−20), now 100.
- **Momentum:** One week is up (+9 % from 91.9), but 2–4 weeks are negative (106.8 / 113.3 / 110.6). The low was 90.2 at day −7.
- **Weight:** 0.15. The bounce is still inside the downtrend.
- **Change my mind:** A weekly close above 115 would make me raise the weight. A break below 90 would take it to 0.

## f3f65489d9 (AVAX)
- **Read:** Low of 82 at day −16, followed by higher lows at 86 (−10) and 90.6 (−7). The 2-week return is positive (88.3 → 100), and 3–4 weeks are flat (about 98).
- **Resistance:** About 102.
- **Weight:** 0.3. The structure is improving, but the longer trend is still down from 147.
- **Change my mind:** Above 103 on a weekly close I would go to about 0.5. Below 90 I would go to 0.1.

## 86d6fb8ba4 (ADA)
- **Read:** A low of 72.9 at day −10, then a vertical rally of +32 % in 4 days on 2× volume (76 → 105.5 high). The 4-week return is +15 %, and the price broke above the 100 range high.
- **Weight:** 0.3. This is a single extreme week with very high volatility, and the breakout has not yet held for even one weekly close. That points more to a pullback than to confirmed momentum.
- **Change my mind:** If price holds above 100 for 2 weekly closes, I would go to about 0.5. Below 90 (the gap zone) I would go to 0.1.

## da84649330 (DOGE)
- **Read:** Lower highs at 152 (−52) and 118.7 (−23). The low was 89.3 at day −5. The 4-week return is negative (110.8 → 100), and only the last week is up.
- **Weight:** 0.15.
- **Change my mind:** Above 114 I would raise the weight. Below 89 I would go to 0.

## 6bc07a03ce (BTC)
- **Read:** Calmer asset. The lows were 92.9 (−30) and 90.8 (−4), roughly flat, so this looks sideways in the 91–105 range. The 4-week return is about 0.
- **Weight:** 0.2. Neutral; this is the range rule.
- **Change my mind:** Above 105 I would raise to about 0.4. Below 90 I would go to 0.05.

## fa51453693 (SOL)
- **Read:** The cleanest base of the ten. The lows rise from 73.7 (−29) to 78.5 (−10) to 85.5 (−7). The price broke above the −20 range high of 93.3 and has closed above it for 4 days, now at about 100.
- **Momentum:** The 4-week return is +23 % (81.5 → 100), and both 1-week and 2-week are positive.
- **Weight:** 0.45. Several weeks agree on direction. The longer trend from 120 is still down, so the weight is not maximal.
- **Change my mind:** Above 106 I would go to about 0.6. A close below 92 would take it back to 0.2.

## 46b1c79d06 (XRP)
- **Read:** Lower highs at 133.9 (−52) and 111.8 (−20). The low was 87.2 at day −10. The 4-week return is about 0, and the 3-week return is negative (102.5).
- **Weight:** 0.2.
- **Change my mind:** Above 108 I would raise the weight. Below 88 I would go to 0.05.

## 35a3a3f47b (LTC)
- **Read:** Lows at 88.4 (−29) and 85.7 (−10), which is a slightly lower low. Today closed at 100, near the −20 high of 101. The 4-week return is +7 %, and the 2–3-week return is flat.
- **Weight:** 0.2. The breakout is not confirmed.
- **Change my mind:** A weekly close above 102 would take me to about 0.4. Below 89 I would go to 0.05.

## c606b09710 (ETH)
- **Read:** A double bottom at 84.3 (−29) and 84.7 (−9). The 4-week return is +5 %. Resistance is the −20 high at 103.6.
- **Weight:** 0.25.
- **Change my mind:** Above 104 on a weekly close I would go to about 0.45. Below 86 I would go to 0.05.

## 50a1cea1fd (LINK)
- **Read:** Lower highs at 134.8 (−56) and 106.7 (−20). The low was 86.8 at day −29 and 86.9 at day −10. The 4-week return is +2 %, and the 3-week return is negative (101.5).
- **Weight:** 0.2.
- **Change my mind:** Above 107 I would raise the weight. Below 87 I would go to 0.05.

{"3c6630209f (DOT)": 0.15, "f3f65489d9 (AVAX)": 0.3, "86d6fb8ba4 (ADA)": 0.3, "da84649330 (DOGE)": 0.15, "6bc07a03ce (BTC)": 0.2, "fa51453693 (SOL)": 0.45, "46b1c79d06 (XRP)": 0.2, "35a3a3f47b (LTC)": 0.2, "c606b09710 (ETH)": 0.25, "50a1cea1fd (LINK)": 0.2}

## Entscheidung 2026-07-12

**Strategy:** I use 1 to 4 week time-series momentum, long-only, and treat the 6-month trend as the regime filter. In a confirmed downtrend the weight stays low, about 0.05 to 0.15. A window earns more weight only if its 2 to 4 week momentum is positive and it shows a confirmed higher-low structure. Position within the range and single-day spikes don't count, and elevated volatility after the crash at days −40 to −37 caps the size everywhere.

All ten windows share one shape: a 6-month decline from about 150–260 to 100, a crash at days −40 to −37, a retest low around day −17, a rally peaking near day −8, and a fade back to 100 at falling volume. The windows differ only in degree.

## 69fbb9e5b9 (ADA)
- **Trend:** Strong downtrend, from 260 to 100.
- **Momentum:** 4 weeks −11%, 2 weeks +13%.
- **Structure:** A spike to 123 (day −8) was fully given back. Lows sit at 85–86. Volatility is very high (2-day +20%, then −15%).
- **Weight 0.10.** The bounce failed and volatility argues for a small size.
- **Change my mind:** Weekly closes above 112 would mean adding. A break below 85 would mean going flat.

## e477659dd7 (DOGE)
- **Trend:** Steady decline. The lower-high sequence from 160 → 127 → 109 → 104 is intact.
- **Momentum:** 4 weeks −18%, 2 weeks flat.
- **Volume:** Drying up, about 0.3.
- **Weight 0.05.** There is no momentum at all.
- **Change my mind:** Above 109 with a second weekly close up there. Otherwise I stay out, especially if it loses 95.

## e209667a16 (BTC)
- **Trend:** Downtrend from 150, though the decline has been flatter since day −37 (low 92.7).
- **Momentum:** 4 weeks −3%, 2 weeks +7%.
- **Structure:** Lows at 91 and 92.7 roughly held. Price is at the top of the 91–101 range.
- **Weight 0.20.** It has mild positive short-term momentum and low volatility.
- **Change my mind:** Weekly closes above 105 would mean raising to about 0.4. Below 91 would mean going to 0.

## f0ed437d62 (AVAX)
- **Trend:** Downtrend. The low was 88.7 at day −23.
- **Momentum:** 4 weeks −6%, 2 weeks flat.
- **Structure:** A peak at 111 was followed by a fade. Day 0 closed at the low of the day.
- **Weight 0.10.**
- **Change my mind:** Above 111 on a weekly close would mean adding. Below 92 would mean flat.

## 408fba6095 (ETH)
- **Trend:** Downtrend from 185.
- **Structure:** A double bottom formed at 83.3 and 83.7. The range is 84–102.
- **Momentum:** 4 weeks +5%, 2 weeks +15%.
- **Weight 0.25.** This is one of the better momentum profiles, but there is no breakout yet.
- **Change my mind:** Weekly closes above 102 would mean raising to 0.4 or more. Below 90 would mean cutting to 0.05.

## aa91b66836 (DOT)
- **Trend:** Downtrend from 270.
- **Momentum:** 4 weeks −15%, 2 weeks +4%.
- **Structure:** Lower highs at 124, 107 and 106. A spike at day −2 was rejected.
- **Weight 0.10.**
- **Change my mind:** Above 107 on a weekly close. Below 94 would mean flat.

## 5d1dcc50d1 (LINK)
- **Trend:** Downtrend from 176.
- **Structure:** Lows held at 87.5 and 87.7.
- **Momentum:** 4 weeks −2%, 2 weeks +10%.
- **Volume:** Fading.
- **Weight 0.20.**
- **Change my mind:** Weekly closes above 103 would mean adding. Below 88 would mean flat.

## e4c6bee232 (SOL)
- **Trend:** Downtrend from 190, but this is the only window with clear higher lows and higher highs since the crash.
  - Lows: 78.2 → 83.3
  - Highs: 98.9 → 109.2
- **Momentum:** 4 weeks +8%, 2 weeks +8%.
- **Weight 0.30.** It is the best-confirmed turn, but the 6-month regime is still down.
- **Change my mind:** Weekly closes above 109 would mean raising to 0.5. Below 88 would invalidate the higher low and mean cutting to 0.05.

## 356eca7950 (XRP)
- **Trend:** Downtrend from 200, with lower highs at 119 and 109.
- **Momentum:** 4 weeks −8%, 2 weeks +4%.
- **Weight 0.10.**
- **Change my mind:** Above 110 on a weekly close. Below 93 would mean flat.

## 4599b66d2b (LTC)
- **Trend:** Downtrend from 178.
- **Structure:** Lows at 89.3 and 89.3. The range is 89–105, with lower highs at 105 and 104.9.
- **Momentum:** 4 weeks −3%, 2 weeks +4%.
- **Volatility:** Relatively low.
- **Weight 0.15.**
- **Change my mind:** Weekly closes above 105 would mean adding. Below 89 would mean flat.

{"69fbb9e5b9 (ADA)": 0.1, "e477659dd7 (DOGE)": 0.05, "e209667a16 (BTC)": 0.2, "f0ed437d62 (AVAX)": 0.1, "408fba6095 (ETH)": 0.25, "aa91b66836 (DOT)": 0.1, "5d1dcc50d1 (LINK)": 0.2, "e4c6bee232 (SOL)": 0.3, "356eca7950 (XRP)": 0.1, "4599b66d2b (LTC)": 0.15}

## Entscheidung 2026-07-19

**Strategy:** I stay long-only, with a base weight of about 0.25 to 0.3. I lower it when the 1–3 month trend is down and price sits below its broken ranges. I raise it modestly only when 2–3 weekly closes point the same way, up from a higher low. Range position and oscillator-type readings don't change the weight. High volatility after crash legs caps the size.

All ten windows share a similar shape: a crash around day -164, a sideways-to-down range, a second drop at days -47 to -44, and then a partial recovery to 100. The differences are in the last 3–6 weeks.

## 84f72cbb30 (XRP)
- **Read:** Long downtrend from about 175 to 100. The old 120–130 range broke at day -47.
- **Recent action:** Range of 92–108 over the last 6 weeks. Close went from 96.5 three weeks ago to 100, which is weak upward momentum. Volume is very low, a quiet compression that says nothing about direction.
- **Weight:** 0.2. The trend is down and there's no confirmed turn.
- **Change my mind:** Weekly closes above 106 would raise the weight. A break below 92 would take it to 0.05.

## 93bdb8c1cc (BTC)
- **Read:** Downtrend. The 110–120 range broke at day -47 and the low was 89.8 at day -24.
- **Recent action:** Three weeks of 92 → 100, a modest higher-low structure. Resistance sits at about 102–104.
- **Weight:** 0.25.
- **Change my mind:** Weekly closes above 104 would raise the weight. Below 90 would lower it.

## 01158e1441 (DOGE)
- **Read:** Rallied to 159 at day -66, then fell steadily to 100, about -37% in 2 months. That is a clear downtrend with lower highs at 125 and then 108.
- **Recent action:** Flat at about 100 for 3 weeks with no reversal.
- **Weight:** 0.1.
- **Change my mind:** Above 109 on a weekly close would raise it. Below 96 would confirm the downtrend.

## d2cd58fb95 (DOT)
- **Read:** Fell from the 150–160 range to 100. The bounce stalled at 107–110, and day 0 is a down day (-2.3%).
- **Recent action:** Lower highs. Support is at 97–98.
- **Weight:** 0.1.
- **Change my mind:** Weekly closes above 110 would raise it. Below 97 would take it to 0.

## cd3851505c (LTC)
- **Read:** The low was 83.5 at day -25, and there have been 3 weeks of 87 → 100 with higher lows (83.5, 87.4, 91.2).
- **Recent action:** The last day pushed the close to 100, the top of the 92–98 range. Momentum is short but in place. The pre-drop range at 110 is still well above.
- **Weight:** 0.35.
- **Change my mind:** Holding above 102–105 for several weekly closes would take it to about 0.5. Below 91 would take it to 0.1.

## d1bd7023a7 (LINK)
- **Read:** The low was 83.4 to 83.6 at days -43 and -24, a double bottom. Three weeks have gone 86 → 100, and price briefly reached 103.
- **Recent action:** Moderate upward momentum, but still below the 108–115 range.
- **Weight:** 0.35.
- **Change my mind:** Above 104 on a weekly close would raise it. Below 92 would lower it.

## d79c572c47 (SOL)
- **Read:** The low was 78.7 at day -43, followed by a recovery to 107.8 at day -16. Since then price has drifted to 96–102.
- **Recent action:** Sideways for 3 weeks after a reversal leg. Mixed signals.
- **Weight:** 0.25.
- **Change my mind:** Above 108 would raise it. Below 95 would lower it.

## f2fb4cf300 (ADA)
- **Read:** A crash to 89 at day -43 and a lower low of 83 at day -24. A spike to 120 at day -15 was fully reversed.
- **Recent action:** Price is at 100 with high volatility and no confirmed direction.
- **Weight:** 0.2. Volatility keeps the size small.
- **Change my mind:** Weekly closes above 108 would raise it. Below 93 would lower it.

## 712aeb5843 (AVAX)
- **Read:** The low was 87.9 at day -30. Price recovered to 108 and has since moved sideways at 98–104 for 3 weeks.
- **Recent action:** The trend is unclear, and price is still below the 135–145 range.
- **Weight:** 0.2.
- **Change my mind:** Above 108 on a weekly close would raise it. Below 97 would lower it.

## aa019c8e5b (ETH)
- **Read:** Lows of 80.4 at day -43 and 80.8 at day -24 form a double bottom. Three weeks have gone 84 → 100, and the high was 104.
- **Recent action:** Upward momentum is the clearest of the windows, though price is still below the 107–113 range.
- **Weight:** 0.35.
- **Change my mind:** Above 104 to 107 on a weekly close would take it to about 0.5. Below 93 would lower it.

{"84f72cbb30 (XRP)": 0.2, "93bdb8c1cc (BTC)": 0.25, "01158e1441 (DOGE)": 0.1, "d2cd58fb95 (DOT)": 0.1, "cd3851505c (LTC)": 0.35, "d1bd7023a7 (LINK)": 0.35, "d79c572c47 (SOL)": 0.25, "f2fb4cf300 (ADA)": 0.2, "712aeb5843 (AVAX)": 0.2, "aa019c8e5b (ETH)": 0.35}

## Entscheidung 2026-07-26

**Strategy:** I hold a baseline weight of about 0.35 when the weekly structure is sideways. I raise it to 0.5–0.6 only when 2–4 weeks of momentum point the same way, confirmed by a series of higher lows and a test of the range high. A lower-high structure or fading momentum pulls the weight down to about 0.3. Volatility only scales the size. Weights move in steps of at least 0.15 from the mean, otherwise they stay near it.

## e29000de7e (XRP)
- **Read:** Long decline from about 130 (day −60) to a low of 90.7 (day −30). Since then it has moved sideways between 94 and 106. Lows are rising (90.7 → 94.6 → 96.1 → 97.3) and the range is compressing below 104.6. The 4-week return is about +6% and the 2-week return about +2%, which is not a confirmed state change.
- **Weight:** 0.35, sideways baseline.
- **Change my mind:** Weekly closes above 105 would raise the weight. A close below 96 would cut it.

## 19f0c11f22 (DOT)
- **Read:** Downtrend from about 160 to 100, followed by 4 weeks of sideways trading between 95 and 109. Highs are falling slightly (109.7 → 108.1 → 105.0) and the lows hold around 95–97. There is no momentum.
- **Weight:** 0.3.
- **Change my mind:** Above 106 I would raise the weight. Below 95 I would go to about 0.15.

## 7b04fef380 (AVAX)
- **Read:** Capitulation low at 84.2 (day −37), then a recovery to a 99–105 band. The last few days were volatile: a drop to 91 followed by a reclaim to 100.5 on high volume. Structure is mixed and volatility is elevated.
- **Weight:** 0.3.
- **Change my mind:** A held weekly close above 105 would raise the weight. A close below 91 would cut it.

## c83ebfd558 (SOL)
- **Read:** Low at 78.3 (day −50), recovery to 109 (day −22), then a slight drift down to 96–102. Lows are higher (83.4 → 95.7), but highs have flattened. This is a sideways phase after a rebound.
- **Weight:** 0.35.
- **Change my mind:** Above 108 I would raise the weight. Below 95.5 I would cut it.

## e4359f40e6 (LINK)
- **Read:** Double bottom at about 79.5 (days −50 and −31). Since then there is a clean series of higher lows: 80.2 → 85.2 → 90.7 → 94.0. The 4-week return is about +21%. Day 0 closes at 100 above the previous range high of 97.8–99.3, but only on a daily basis, not yet as a weekly close.
- **Weight:** 0.55, for the momentum over several weeks. I am not going higher because the breakout is not yet confirmed on the weekly level.
- **Change my mind:** Falling back below 94 would mean returning to 0.35. Weekly closes above 103 would justify up to 0.7.

## 9ba1ea84af (ETH)
- **Read:** Low at 77 (day −50). Higher lows since then: 77.4 → 79.3 → 87.7 → 92.2 → 94.5. The 4-week return is about +24%. Price is testing the 100–100.6 resistance for the third time.
- **Weight:** 0.6, for momentum confirmed over 3–4 weeks.
- **Change my mind:** Below 94 I would go to 0.35. Weekly closes above 101 would justify 0.7.

## e04c6e2014 (BTC)
- **Read:** Low at 88.4 (day −25). Since then there are steadily higher lows (93.7, 94.5, 96.5, 97.5) with comparatively low volatility. The 4-week return is about +10%. The range high is 102.4.
- **Weight:** 0.5, for moderate, consistent momentum.
- **Change my mind:** Below 96 I would go to 0.35. Above 102.5 I would go to 0.65.

## a0dbca77b5 (DOGE)
- **Read:** Downtrend from 157 (day −73) to 100, then sideways between 94 and 108. Highs are falling (108.2 → 103 → 100.9). There was a shakeout to 93.2 three days ago. Momentum is negative or flat.
- **Weight:** 0.3.
- **Change my mind:** Weekly closes above 106 would raise the weight. A close below 93 would take it to about 0.15.

## db4a7a69d3 (LTC)
- **Read:** Low at about 82 (days −31 and −32). Higher lows since then: 86.0 → 90.2 → 92.2 → 95.6. The 4-week return is about +12%, with low volatility. Price is testing the 100–101 range high. Volume is slightly elevated.
- **Weight:** 0.5.
- **Change my mind:** Below 95.5 I would go to 0.35. Weekly closes above 101 would justify 0.65.

## cee4ef231c (ADA)
- **Read:** Extreme spike week to 120.5 (day −22), followed by a complete fade back to 97–105. A single extreme week is not momentum. The current structure is sideways with highs falling from 108.9.
- **Weight:** 0.35.
- **Change my mind:** Weekly closes above 106 would raise the weight. Below 96 I would go to 0.2.

{"e29000de7e (XRP)": 0.35, "19f0c11f22 (DOT)": 0.3, "7b04fef380 (AVAX)": 0.3, "c83ebfd558 (SOL)": 0.35, "e4359f40e6 (LINK)": 0.55, "9ba1ea84af (ETH)": 0.6, "e04c6e2014 (BTC)": 0.5, "a0dbca77b5 (DOGE)": 0.3, "db4a7a69d3 (LTC)": 0.5, "cee4ef231c (ADA)": 0.35}

## Entscheidung 2026-08-02

**Strategy:** I go long only when 2 to 4 weeks of closes confirm upward momentum, such as higher lows or a held breakout. When the trend is falling I stay near flat. When the market is moving sideways I stay at a moderate weight of about 0.25 to 0.3, and I don't trade position in the range. High volatility and one-off spike weeks shrink the weight rather than raise it.

## 9f1f0f5ad0 (DOT)
- **Read:** A persistent downtrend, from about 190 down to 100. Lower highs at 131, 112 and 108.8. The day −6 drop broke below the 100–108 shelf, and price has only just reclaimed 100. The 4-week return is negative.
- **Weight:** 0.1. The trend is still down, and spending 0.2% on a range-low bounce isn't worth it.
- **Change my mind:** Weekly closes above about 109 (above the last high), or below 93 to confirm staying flat.

## 04c9decb10 (DOGE)
- **Read:** Down from 167 (day −80) to about 100. For 5 weeks price has drifted sideways to lower between 96 and 106 on fading volume. There is no confirmed reversal.
- **Weight:** 0.15. Downtrend regime with sideways drift.
- **Change my mind:** A held weekly close above 106 to 107.

## eaaf161dbb (ADA)
- **Read:** A crash to about 73 (day −38), then a spike to 105, then a pullback to 81 to 83. Today's close of 100 came on 1.7× volume. Lows are rising (73, 81, 85), and the 4-week return is about +20%. Price is now at the 101 to 105 resistance zone, and volatility is high.
- **Weight:** 0.4. Momentum is turning positive, but this is one extreme week at resistance, and the volatility argues for a smaller size.
- **Change my mind:** Two weekly closes above 105 would let me raise it. Falling back below 88 would cut it.

## 953a104b35 (BTC)
- **Read:** Down from 130 to 91 (day −38), then a slow recovery into a tight range of 98 to 105 for about 4 weeks. Volatility is low. Momentum is flat to slightly positive.
- **Weight:** 0.3. Sideways, so I hold near the mean.
- **Change my mind:** A held breakout above 105.5, or a break below 97.

## 5846df7852 (AVAX)
- **Read:** A collapse from 156 to 87 (day −44). Since then it has been a 6-week range between 92 and 108 with many crossings. Today's bounce from 94 is a single day.
- **Weight:** 0.25. Sideways regime, and the bounce is noise.
- **Change my mind:** Weekly closes above 108, or below 92.

## bd1d6ec88c (ETH)
- **Read:** A low of 80 (day −37), then higher lows at 91, 92.5 and 96.6. Highs sit at 103 to 105. The 8-week return is about +19% and the 4-week return about +6%, so recovery momentum is confirmed over several weeks.
- **Weight:** 0.45. Moderate positive momentum, still below the higher breakout level.
- **Change my mind:** Weekly closes above 105 would lift me toward 0.6. A close below 96 would drop me to 0.25.

## 5e4e34fce7 (XRP)
- **Read:** Down from 140 to 93. Then a rebound to 109 (day −29) that faded. Price has ranged between 96 and 107 for 4 weeks, and the 4-week return is flat.
- **Weight:** 0.3. Sideways.
- **Change my mind:** Above 107, or below 96.

## cae267e396 (LINK)
- **Read:** A low of 83 (day −38), then higher lows at 89.7, 94 and 94.1. Highs come in at 103 to 105.5. The 4-week return is about +6% and the 8-week return about +14%.
- **Weight:** 0.4. Higher-low structure with modest momentum.
- **Change my mind:** A close above 106 would raise it. A close below 94 would cut it to about 0.2.

## b5573def37 (SOL)
- **Read:** A low of 82 (day −57), then a strong rally to 114 (day −30). Since then a drift lower with lower highs at 107 and 105, down to 100. The 4-week return is flat to negative, so the momentum has faded.
- **Weight:** 0.25.
- **Change my mind:** Above 107 would raise it. Below 95.5 would take me toward flat.

## 6dd31f2eb4 (LTC)
- **Read:** A low of 88 (day −39), then a recovery to 108 (day −7). Price has since pulled back to 99 to 100, and the 4-week return is about +2.5%. The range is 97 to 108, with a mixed sequence of highs and lows.
- **Weight:** 0.3.
- **Change my mind:** Above 108 would raise it. Below 97 would cut it.

{"9f1f0f5ad0 (DOT)": 0.1, "04c9decb10 (DOGE)": 0.15, "eaaf161dbb (ADA)": 0.4, "953a104b35 (BTC)": 0.3, "5846df7852 (AVAX)": 0.25, "bd1d6ec88c (ETH)": 0.45, "5e4e34fce7 (XRP)": 0.3, "cae267e396 (LINK)": 0.4, "b5573def37 (SOL)": 0.25, "6dd31f2eb4 (LTC)": 0.3}

## Entscheidung 2026-08-09

**Strategy:** Long-only momentum over 1–4 weeks. The base weight is about 0.25. I raise it only when two or more weekly closes confirm upward momentum, and I cut it toward 0.1 when there is a clear series of lower highs. All ten windows share a crash around day -65 followed by a base, so the large drop from the old level does not change the weight by itself. Only the structure since the crash matters. High volatility caps the size.

## 2100de012b (AVAX)
- **Read:** Fell from 140–150 to about 100, then moved sideways between 92 and 110 for nine weeks. Weekly closes were 102.5, 99.8, 102.4 and 100: flat, with low volume and narrowing ranges. This is a sideways market, so position in the range means nothing.
- **Weight: 0.2.** No signal, so I stay a little below the base weight.
- **Change my mind:** A weekly close above 109 → 0.4. A close below 94 → 0.05.

## 2433c161c7 (LINK)
- **Read:** Double bottom at 85.5 and 85.6, then a recovery to 106. Since then it has drifted sideways to slightly lower between 98 and 106; weekly closes were 105, 102.4, 100 and 100. Momentum over six weeks is positive, but over three weeks it is neutral to slightly negative.
- **Weight: 0.25**
- **Change my mind:** A weekly close above 106 → 0.4. A close below 96 → 0.1.

## 71c2d28511 (BTC)
- **Read:** Fell from 113–126 to a low of 89.5, then recovered to about 100. Since then it has been very narrow and sideways between 96 and 103, with low volatility. Compressed volatility points to a larger move, but not its direction.
- **Weight: 0.25**
- **Change my mind:** A weekly close above 103.5 → 0.4. A close below 95 → 0.1.

## f17914abaf (DOGE)
- **Read:** Fell from 170 to 113, then kept falling. The highs step down: 133, 114.5, 106.8, 103. The price is now at the lower edge of the 98–106 range. The downtrend is gentle but intact.
- **Weight: 0.1**
- **Change my mind:** A weekly close above 107 → 0.3. Below 97 the weight stays at 0.05–0.1.

## 85add7edff (ETH)
- **Read:** Double bottom at 79, then higher lows at 89.7, 94.4 and 95.4. The price climbed from 82 to about 100 over six weeks, and the last three weeks have been flat between 96 and 102. This is the cleanest higher-low structure of the set.
- **Weight: 0.35**
- **Change my mind:** A weekly close above 103 → 0.5. A close below 95 → 0.15.

## 4641a4bf0d (ADA)
- **Read:** After the crash it hit a low of 71. A spike to 102.8 was sold back down to 80. Since then it has rallied sharply: weekly closes went from 85.3 to 97.4 to 100, about 25% in two weeks. It probed 108.8 but only closed at 103.4, and it is back at 100. Two up weeks give confirmed momentum, but volatility is high.
- **Weight: 0.4.** The momentum is confirmed, but the size is limited because volatility is high.
- **Change my mind:** A weekly close above 104 that holds → 0.55. A close below 92 → 0.15.

## 079da006b8 (SOL)
- **Read:** Low of 78.8, then a rally to 110. Since then the highs have stepped down: 110, 103.4, 101.6, 102. The range is 92.5–104. The last week was up, from 96.4 to 100, but there is no trend.
- **Weight: 0.25**
- **Change my mind:** A weekly close above 104 → 0.4. A close below 93 → 0.1.

## 8a1cecdd8b (LTC)
- **Read:** Low of 86.4, then a recovery to 105. Weekly closes were 103.5, 105.2, 98.3 and 100: sideways with a slight downward lean. The range is 96–106.
- **Weight: 0.25**
- **Change my mind:** A weekly close above 106 → 0.4. A close below 96 → 0.1.

## 05838cd95c (XRP)
- **Read:** The bounces after the crash keep making lower highs: 125.6, 115, 113, 108. The price is now testing support at 98–100 for the third time. The downtrend is intact.
- **Weight: 0.1**
- **Change my mind:** A weekly close above 109 → 0.3. A close below 97 → 0.0.

## d17dd20f02 (DOT)
- **Read:** A persistent decline from about 200. Lower highs were 131, 112.6 and 108.9, and the lows were 93 recently. The last bounce, from 95 to 107, was immediately given back. The downtrend is intact.
- **Weight: 0.1**
- **Change my mind:** A weekly close above 109 → 0.3. A close below 93 → 0.0.

```json
{"2100de012b (AVAX)": 0.2, "2433c161c7 (LINK)": 0.25, "71c2d28511 (BTC)": 0.25, "f17914abaf (DOGE)": 0.1, "85add7edff (ETH)": 0.35, "4641a4bf0d (ADA)": 0.4, "079da006b8 (SOL)": 0.25, "8a1cecdd8b (LTC)": 0.25, "05838cd95c (XRP)": 0.1, "d17dd20f02 (DOT)": 0.1}
```

## Entscheidung 2026-08-16

## Strategy

I go long only when trend and 1–4 week momentum agree across several weekly closes. I size down when volatility is high. In sideways or falling markets I stay near a low base weight of about 0.2–0.3, and I go lower when there are lower highs and negative weekly momentum. Range position and single daily candles do not change the weight; a confirmed change of state does.

---

## 76a2b03d59 (AVAX)
- **Read:** Long-term downtrend, from about 150 down to 100. There was a crash around day −72 to about 105, and price has ranged between 95 and 112 since.
  - Weekly closes: 102 → 107 → 104 → 101 → 100, so flat with a slight downward drift.
  - Day −1 spiked to 108.6 and failed back to 100.
  - Support is 96–97; resistance is 108–110.
- **Weight: 0.2.** This is a range under a falling trend with no momentum signal.
- **Change my mind:** Two weekly closes above 110 would raise the weight. A close below 95 would take it to 0.

## a4d0ad81bd (DOGE)
- **Read:** Downtrend from 165 (day −103) to 100. Since day −45 it has ranged 98–114 with falling highs.
  - Volume and range have compressed sharply. That signals a larger move coming, but not its direction.
  - Weekly closes: 104 → 105 → 102 → 100 → 100.
- **Weight: 0.2.**
- **Change my mind:** A held breakout above 106 would raise the weight. Below 97, go flat.

## 0bba290ae9 (SOL)
- **Read:** Crash low at 80.6 (day −71), recovery to 110 (day −44), then drift back to about 100.
  - Weekly closes: 102 → 103 → 99 → 102 → 100, so sideways.
  - The range is 95–105.
- **Weight: 0.25.** Neutral range, low volatility.
- **Change my mind:** Two weekly closes above 105 would raise it. Below 95, cut it.

## 1aecc2e8da (DOT)
- **Read:** Persistent downtrend from about 220 to 100. Highs keep falling: 138 (day −62), 120 (day −41), 115 (day −12).
  - Weekly closes: 108 → 109 → 105 → 105 → 100. Negative momentum.
- **Weight: 0.1.**
- **Change my mind:** A weekly close above 115 would break the lower-high sequence.

## f99a931be4 (ETH)
- **Read:** Low at 80.6 (day −51), then higher lows and a recovery to a 98–104 plateau.
  - Weekly closes: 100 → 104 → 100.5 → 102 → 100.
  - The base-building is constructive, but recent weekly momentum is flat.
- **Weight: 0.3.**
- **Change my mind:** Holding above 105 would raise it to about 0.5. A close below 96 would cut it to 0.1.

## 5b37a653f1 (LINK)
- **Read:** Low at 74.7 (day −52), followed by a series of higher lows: 80, 84, 85, 87.
  - Last week's close went from 87 to 100 (+15%), clearing the 94–95 range ceiling with volume.
  - Weekly closes: 89 → 94 → 89 → 87 → 100.
  - This is a breakout, but so far only one strong week. A single extreme week argues for caution until it is confirmed.
- **Weight: 0.45.**
- **Change my mind:** Two more weekly closes above 100 would raise it to about 0.7. A fall back below 92 would mean the breakout failed, and I would cut to 0.15.

## e0be27d407 (BTC)
- **Read:** Low at 92.4 (day −52), then recovery into a tight 99–106 range with low volatility.
  - Weekly closes: 103 → 104 → 101 → 103 → 100. Sideways.
- **Weight: 0.3.**
- **Change my mind:** A close above 106 would raise it; a close below 98 would lower it.

## 66ef76ccf2 (XRP)
- **Read:** Clear lower highs: 130 (day −62), 119 (day −43), 117 (day −26), 110 (day −14).
  - Weekly closes: 110.5 → 112 → 109 → 104 → 100. A steady decline.
- **Weight: 0.1.**
- **Change my mind:** A weekly close back above 110.

## b250ec785e (ADA)
- **Read:** Very volatile.
  - Spike to 114 (day −43) that failed; spike to 121 (day −10) that also failed.
  - Six straight down days from 115 to 100.
  - Weekly closes: 95 → 95 → 108 → 111 → 100.
  - The rally was not held, and volatility is high, so position size should be small.
- **Weight: 0.15.**
- **Change my mind:** Reclaiming 110 on a weekly close would raise it. Below 93, go to 0.

## 8241404d4c (LTC)
- **Read:** Low at 88.9 (day −53), recovery to 108 (day −28), then drift down to 100.
  - Weekly closes: 106.6 → 108 → 101 → 103 → 100. Mildly negative.
  - Support is 98–99.
- **Weight: 0.25.**
- **Change my mind:** A close below 98 would cut to 0.1. Above 105, raise it.

---

{"76a2b03d59 (AVAX)": 0.2, "a4d0ad81bd (DOGE)": 0.2, "0bba290ae9 (SOL)": 0.25, "1aecc2e8da (DOT)": 0.1, "f99a931be4 (ETH)": 0.3, "5b37a653f1 (LINK)": 0.45, "e0be27d407 (BTC)": 0.3, "66ef76ccf2 (XRP)": 0.1, "b250ec785e (ADA)": 0.15, "8241404d4c (LTC)": 0.25}

## Entscheidung 2026-08-23

## Strategy

Every window shows the same setup. A multi-week sideways or downtrend phase is followed by a sharp 4-day rally of +20 to +50 % into day 0, with a volume spike and often a long upper wick on day -1.

The rule I apply:
- A single extreme week is not confirmed momentum. It points more toward consolidation or a pullback, and the volatility jump argues for a smaller position.
- I hold a moderate weight below the mean (0.2–0.4) and only go slightly higher where a weekly uptrend already existed before the spike.
- The weight rises only if the breakout holds over 2–3 weekly closes. It falls if price drops back into the old range.

## 1d39ee78ae (ETH)
**Read:** Sideways at 75–78 for about 6 weeks, then a jump to 103 (high) on day -2. Closing at 100 sits above the gap level from the crash (~82) and at the old 95–100 resistance zone. This is one week of momentum only, with volatility clearly higher.

**Weight:** 0.35. Hold, don't add.

**Change my mind:** A weekly close above 104 → raise. Below 90 → reduce.

## 71ae485bd4 (BTC)
**Read:** Range at 80–84, rally to 102, and day -1 has no strong rejection. The rally is the most moderate in relative terms (+20 %). Old highs sit at 104–106.

**Weight:** 0.4.

**Change my mind:** Above 106 → raise. Below 92 → reduce.

## c88b3d054e (ADA)
**Read:** Long-term downtrend from 130. Two earlier spikes (-50 to 88, -17 to 93) were fully given back. Now there is a spike with a wick to 113.8 and a close at 100, which is a blow-off profile with very high volatility.

**Weight:** 0.25.

**Change my mind:** Holding above 105 for 2 weeks → raise. Below 88 → go toward 0.1.

## 1b19cef591 (XRP)
**Read:** From 66 to 100 in 4 days (+52 %), with volume up to 6×. Day -1 shows a wick to 111.8 and a close at 96. This is the most extreme blow-off of the set, and before it there was a steady downtrend.

**Weight:** 0.2.

**Change my mind:** Above 112 held → raise. Below 85 → reduce further.

## a9a31c5272 (AVAX)
**Read:** Range at 82–90 after the crash, long-term trend down from 135. Spike with a wick to 109.3 and a close at 100. The old breakdown level is around 117.

**Weight:** 0.3.

**Change my mind:** Above 110 → raise. Below 90 → reduce.

## 4db6f65b19 (SOL)
**Read:** Range at 76–82, spike with a wick to 107.7, close at 100. The prior highs at 100–103 (day -105) are being tested.

**Weight:** 0.3.

**Change my mind:** A weekly close above 104 → raise. Below 88 → reduce.

## 8dc1e50ef3 (LINK)
**Read:** The only window with a rise before the spike: from 70 (day -13) to 83 (day -5). That means 2–3 weeks pointing in the same direction. Then a rally with a wick to 109.3, close at 100. Old highs are at 92–94.

**Weight:** 0.4.

**Change my mind:** Holding above 104 → raise. Below 90 → reduce.

## 57e22787f3 (LTC)
**Read:** Downtrend from 115 with a range at 84–90. Spike with a wick to 106, close at 100. The old 110–116 zone is overhead.

**Weight:** 0.3.

**Change my mind:** Above 107 → raise. Below 90 → reduce.

## 7d55302e10 (DOT)
**Read:** Persistent downtrend from 179 to 81 with lower highs. Spike with a wick to 111.2, close at 100. Volatility is structurally high. This looks more like a bear-market rally than a regime change.

**Weight:** 0.25.

**Change my mind:** Above 112 held → raise. Below 88 → reduce.

## 5ad235527e (DOGE)
**Read:** Very tight range at 74–77 (compressed volatility), then an explosive rally with a wick to 107.9 and a close at 100. Direction is unconfirmed, and the old 105–108 zone acts as resistance.

**Weight:** 0.25.

**Change my mind:** Above 108 held → raise. Below 88 → reduce.

{"1d39ee78ae (ETH)": 0.35, "71ae485bd4 (BTC)": 0.4, "c88b3d054e (ADA)": 0.25, "1b19cef591 (XRP)": 0.2, "a9a31c5272 (AVAX)": 0.3, "4db6f65b19 (SOL)": 0.3, "8dc1e50ef3 (LINK)": 0.4, "57e22787f3 (LTC)": 0.3, "7d55302e10 (DOT)": 0.25, "5ad235527e (DOGE)": 0.25}

## Entscheidung 2026-08-30

**Strategy:** I stay long-only and follow 1–4 week momentum on weekly closes. A breakout counts only if price holds above its prior range for more than a week. Elevated volatility after a spike cuts the size, and a lower-high downtrend caps it. Every window shows a sharp breakout 9–11 days ago that has since pulled back to 100, so the deciding questions are whether 100 still sits above the prior range and how big the longer-term damage is.

## 1c84a500f1 (LINK)
- **Read:** The market based at 73–75 for about six weeks, then broke out in stages from day −19. It peaked at a 113 high and a 107.6 close. For eight days it has held 100–107, above the old 4-month high near 96. Four-week momentum is strongly positive (+35%). The last week is slightly negative, and volatility is high.
- **Weight: 0.6.** The breakout is holding, but the high volatility keeps the size moderate.
- **Change my mind:** A weekly close below 95 means the breakout failed.

## ce02e9c518 (SOL)
- **Read:** The base at 71–75 broke out at day −11. Price has held 92–107 and is now 100, above the prior high near 96. The structure has higher lows (93 → 98.6).
- **Weight: 0.6.**
- **Change my mind:** A close below 92.

## 893ed2bb20 (ADA)
- **Read:** Price fell from 150 to a crash low near 80. The rally to 104 (day −24) faded to 90. The spike to a 134 high left a long wick and has now retraced almost entirely to 100, below the earlier 104 high. The four-week change is flat, and the spike looks like an extreme week rather than momentum.
- **Weight: 0.3.**
- **Change my mind:** A weekly close above 111 would raise the weight; a close below 90 would take it to 0.

## 7de918f5eb (AVAX)
- **Read:** The pre-crash level was 125–140. After the crash, price ranged 85–98 for two months, then broke out to 110 and is now 100, just above the range top at 98. The bigger picture is still well below pre-crash levels.
- **Weight: 0.45.**
- **Change my mind:** A close back below 95, inside the range, would cut it toward 0.2.

## 9e15046fdb (XRP)
- **Read:** This window had the slow bleed from 105 to 73 and then the most extreme spike: a 125 high on six times average volume. Price has given back most of it, falling from 112 to 100. That extreme week argues for a counter-move, even though four-week momentum is large.
- **Weight: 0.45.**
- **Change my mind:** Below 92 the weight goes to 0; a weekly close above 110 would raise it.

## 03811dc3db (BTC)
- **Read:** This is the calmest window. The base at 81–84 broke out to 100–104 and has held a tight 99–104 band for nine days. Price is back inside its pre-crash range of 95–105, and the low volatility supports a larger size.
- **Weight: 0.65.**
- **Change my mind:** A close below 97.

## fad5f00c2e (LTC)
- **Read:** Since the crash low at 86 there is a higher-low sequence: 82 → 90 → 92. The breakout reached 111 and has pulled back to 100. Trend structure is the best of the set, although price is still below the old 108–126 range.
- **Weight: 0.6.**
- **Change my mind:** A close below 96.

## 486e7e5da0 (DOGE)
- **Read:** The longer-term downtrend runs from 140 (day −108) to a flat 84–90 base. The spike reached 123 and has retraced to 100. The trend is weaker and more of the gain has been given back.
- **Weight: 0.45.**
- **Change my mind:** A close below 93 would take it to 0.

## 0b9c0f6e0b (ETH)
- **Read:** The base at 77–80 broke out on day −11 to 104. Price has held 99–104 for nine days, cleanly above the base.
- **Weight: 0.6.**
- **Change my mind:** A close below 95.

## 283b967cbe (DOT)
- **Read:** A six-month downtrend from 190 to 92 is still intact as a lower-high sequence (110 → 106 → spike 126). The spike has faded back to 100, so this is a counter-rally inside the downtrend.
- **Weight: 0.3.**
- **Change my mind:** A weekly close above 108 would raise the weight; a close below 92 would take it to 0.

{"1c84a500f1 (LINK)": 0.6, "ce02e9c518 (SOL)": 0.6, "893ed2bb20 (ADA)": 0.3, "7de918f5eb (AVAX)": 0.45, "9e15046fdb (XRP)": 0.45, "03811dc3db (BTC)": 0.65, "fad5f00c2e (LTC)": 0.6, "486e7e5da0 (DOGE)": 0.45, "0b9c0f6e0b (ETH)": 0.6, "283b967cbe (DOT)": 0.3}

## Entscheidung 2026-09-06

**Strategy:** I hold a long position only when 2–4 weekly closes confirm upward momentum and price holds above the breakout base. I scale the size down when volatility is elevated or the move came from one extreme week, which raises the risk of a reversal. Without a confirmed change of state, the weight stays near 0.5. Range position and oscillator levels are not used as signals.

All ten windows share the same broad shape: a crash around day −95, a base or downtrend in the 55–80 zone, and a high-volume breakout at days −18 to −16. Since then price has consolidated and now closes at 100. Volatility is elevated in all of them, so no weight goes above 0.75.

## c1e067dd63 (BTC)
- **Market read:**
  - Weekly closes are about 81 (−28), 78 (−21), 97 (−14), 97 (−7) and 100 (now).
  - The breakout from the 78–81 base has held for more than two weekly closes.
  - Price has consolidated in a tight 94–102 band and is retesting the 180-day high around 101–103.
- **Weight: 0.70.** Momentum is confirmed and the consolidation is orderly.
- **Change my mind:** a weekly close below 94.

## e5d1126018 (LTC)
- **Market read:**
  - The spike to 101 at day −15 faded to 87 by day −7.
  - Price then recovered with higher lows, closing at 87 (−7) and 100 (now), with a strong volume day at −1.
  - The four-week trend is up, from a base near 80. Pre-crash highs were around 105–110.
- **Weight: 0.65.** The retest held, but the path was choppier than in the leaders.
- **Change my mind:** a close below 90.

## 86bfc1e29c (SOL)
- **Market read:**
  - Weekly closes have risen four times in a row: 72 → 70 → 90 → 96 → 100.
  - Price is above the old 92 high from day −118 and near the 180-day high of 104.
  - The base was 67–73, and the breakout was clean.
- **Weight: 0.75.** This is the cleanest multi-week momentum in the set.
- **Change my mind:** a close below 92.

## 4d08426b71 (AVAX)
- **Market read:**
  - The larger trend is still down: price was 120–130 before the crash and is 100 now.
  - Price broke out of an 78–86 base. Weekly closes are 81 → 80 → 96 → 90 → 100.
  - The pullback held at 89, and price now closes at the top of the 89–100 range.
- **Weight: 0.60.** Momentum is positive, but there is overhead supply at 105–115.
- **Change my mind:** a close below 89.

## 35bb534a8a (ETH)
- **Market read:**
  - Weekly closes are 76 → 75 → 98 → 96 → 100.
  - The breakout from the 73–77 base has held.
  - Price is consolidating in a 94–101 range at the 180-day high, with the earlier peak near 98.
- **Weight: 0.70.**
- **Change my mind:** a close below 94.

## 2309fd2c19 (XRP)
- **Market read:**
  - Day −15 was a blow-off: the high reached 119.4 on six times average volume.
  - Since then the trend has been sideways to down: 107 → 95 → 100, within a 92–104 range.
  - That single extreme week argues for mean reversion rather than momentum.
- **Weight: 0.50.** The breakout is real, but there has been no follow-through above the spike.
- **Change my mind:**
  - A close below 92 would lower the weight.
  - A weekly close above 105 would raise it.

## 4e4ccb0d97 (DOT)
- **Market read:**
  - The six-month downtrend ran from 165 to 77.
  - Weekly closes are 82 → 78 → 95 → 84 → 100.
  - The last week alone gained about 19%, which is an extreme single week.
  - Price is below the 110–135 levels from before the crash.
- **Weight: 0.50.** The trend reversal is not yet confirmed by higher weekly closes.
- **Change my mind:** a close below 88. A hold above 100 for another week would raise the weight.

## 66de816a1b (DOGE)
- **Market read:**
  - Price spiked to 111 at day −15 and has since moved sideways in an 88–103 range.
  - Weekly closes are 76 → 77 → 103 → 90 → 100.
  - Heavy resistance sits at 110–125 from the pre-crash period.
- **Weight: 0.55.**
- **Change my mind:** a close below 88.

## 0ac78f130d (ADA)
- **Market read:**
  - Breakout attempts at days −65 and −35 both failed.
  - Weekly closes are 87 → 78 → 102 → 86 → 100, a choppy sequence.
  - The current range is 85–102, and the pre-crash level was around 105–125.
- **Weight: 0.45.** Repeated failed spikes make this the least reliable momentum in the set.
- **Change my mind:**
  - A close below 86 would lower the weight.
  - A weekly close above 103 would raise it.

## 7fc2c74bd6 (LINK)
- **Market read:**
  - A persistent uptrend has run since day −36, from 61.
  - Weekly closes are 62 → 71 → 87 → 84 → 100.
  - Price is at the 180-day high, clearly above the old 82 high.
  - The last day gained 10%, so a short-term pullback is possible.
- **Weight: 0.75.** The momentum spans four weeks.
- **Change my mind:** a close below 88.

{"c1e067dd63 (BTC)": 0.7, "e5d1126018 (LTC)": 0.65, "86bfc1e29c (SOL)": 0.75, "4d08426b71 (AVAX)": 0.6, "35bb534a8a (ETH)": 0.7, "2309fd2c19 (XRP)": 0.5, "4e4ccb0d97 (DOT)": 0.5, "66de816a1b (DOGE)": 0.55, "0ac78f130d (ADA)": 0.45, "7fc2c74bd6 (LINK)": 0.75}

## Entscheidung 2026-09-13

**Strategy:** I start from a neutral 0.5. I add weight only when a confirmed state is in place: positive 1–4 week momentum and a breakout that has held over several weekly closes. I cut weight for high or rising volatility, or for a single blow-off week, which tends to reverse. Where a level is within a few percent of 100, I treat it as range noise rather than a signal.

All ten windows share the same broad structure. Each had a crash around day -100, a base from about day -80 to -26, a sharp breakout over days -25 to -23, and three weeks of consolidation. The differences are in how cleanly each breakout held and how volatile it was.

## 93d0cb0d8a (BTC)
- **Read:** The base sat at 82–85. The breakout ran to about 102 and has held 99–106 for three weekly closes, with relatively low volatility. Four-week momentum is about +19%. Support is 99, the breakout shelf. Resistance is 106–108, the old high from day -130.
- **Weight:** 0.65. The breakout is confirmed over several weeks with calm volatility.
- **Change my mind:** a weekly close below 97.

## 598b52f5b0 (ADA)
- **Read:** The long-term trend is down from 142. The spike to 127 was immediately rejected. Price has since chopped between 94 and 114, and the earlier rally to 94 at day -71 fully reversed. Volatility is high.
- **Weight:** 0.45. Momentum is positive, but large swings and a history of failed rallies argue for a smaller position.
- **Change my mind:** a weekly close below 93 (cut), or a hold above 110 (add).

## 2ba1d6d3ae (LINK)
- **Read:** The base sat at 65–75, with the breakout reaching 107. A second push to 118 at day -7 failed, and price is now back at the breakout zone around 100. Lows of 98–100 are still holding.
- **Weight:** 0.5. Momentum is positive, but the failed extension is a warning.
- **Change my mind:** a weekly close below 97.

## 4098bf11b3 (LTC)
- **Read:** The base sat at 82–85. The breakout to 99 faded to 89, then recovered to 100–103 with a wick to 110. Volatility is moderate and the lows are rising (89, 92, 96).
- **Weight:** 0.55.
- **Change my mind:** a weekly close below 95.

## fc27240a3b (AVAX)
- **Read:** The longer-term trend is down from 140. The base sat at 86–92, and the breakout went to 107 and then 110. Price is back at 100, with support at 97–98.
- **Weight:** 0.5. Momentum is positive but the larger downtrend has not turned.
- **Change my mind:** a weekly close below 97.

## e3a3316b1d (DOGE)
- **Read:** The base sat at 84–88, followed by a spike to 122 on heavy volume. Weekly highs have been lower each time (113, 110, 109, now 100), so the breakout is fading.
- **Weight:** 0.45.
- **Change my mind:** a weekly close below 97 (cut), or a reclaim of 110 (add).

## 0c2376a359 (XRP)
- **Read:** The base sat at 74–75. The blow-off spike reached 126.7 on 6× volume. Weekly closes since then are 113, 101, 106, 100, which is a declining sequence. Momentum is strongest of all windows in percentage terms, but it is fading.
- **Weight:** 0.45.
- **Change my mind:** a weekly close below 97.

## 7d36fc1602 (SOL)
- **Read:** The base sat at 74–77, and the breakout extended to 110. Weekly closes are 96, 102.5, 107, 100. Four-week momentum is about +30% with moderate volatility.
- **Weight:** 0.55.
- **Change my mind:** a weekly close below 98.

## 5e4fbcf576 (ETH)
- **Read:** Price gapped from a 75–77 base to about 101. It has since held a tight 96–102 range for three weeks, which shows a clean acceptance above the breakout level.
- **Weight:** 0.6.
- **Change my mind:** a weekly close below 95.

## 508848ad28 (DOT)
- **Read:** This is a long downtrend from 162. The first spike to 103 faded to 82. Then came a single extreme week (day -6 and -5), running to 128.5 on 4× volume, which fully reversed to 100. Volatility is extreme, and an extreme week like this points to a counter-move rather than momentum.
- **Weight:** 0.3.
- **Change my mind:** a weekly close above 112 (add), or below 90 (cut to flat).

{"93d0cb0d8a (BTC)": 0.65, "598b52f5b0 (ADA)": 0.45, "2ba1d6d3ae (LINK)": 0.5, "4098bf11b3 (LTC)": 0.55, "fc27240a3b (AVAX)": 0.5, "e3a3316b1d (DOGE)": 0.45, "0c2376a359 (XRP)": 0.45, "7d36fc1602 (SOL)": 0.55, "5e4fbcf576 (ETH)": 0.6, "508848ad28 (DOT)": 0.3}

## Entscheidung 2026-09-20

**Strategy:** I start from a neutral weight of about 0.45. I raise it only when two things agree: 2–4 weeks of momentum, and a confirmed state change, meaning a breakout that has held over several weekly closes with higher lows. I scale the weight down when volatility is high or the last few days were extreme, because a single extreme week argues against chasing. Sideways ranges with high volatility stay near neutral.

## e615362136 (AVAX)
- **Read:** Long decline from 85 to a 55–60 base. It broke out to about 69 and consolidated at 63–71.
- **Recent move:** The last three days jumped from 67 to 100 on 4–6× volume. Four-week momentum is very strong (about 64 → 100), but almost all of it came in one blow-off week with extreme volatility. A counter-move is likely, and 89 (the day -1 close) is the first gap level.
- **Weight:** 0.40. The trend is up, but I size down for the volatility and don't chase.
- **Change my mind:**
  - A weekly close below 85 would cut the weight to about 0.2.
  - Holding above 95 for two weekly closes would raise it to 0.6.

## 35ba2b9b22 (ADA)
- **Read:** Crash to 69, then a low at 61 (day -88). Since then the lows have been rising: 68, 76, 84. The spike to 113 was rejected, but price has recovered to 100 at the top of the 84–101 range.
- **Momentum:** Four-week momentum is about +15%. Volatility is elevated.
- **Weight:** 0.60.
- **Change my mind:** A close below 84 breaks the higher-low structure and would cut the weight to about 0.3.

## 33b0546954 (ETH)
- **Read:** A clean step breakout at day -32, from 72 to 85+. It has held 89–96 for four weekly closes, and today's 100 is a new closing high. Pullbacks have been shallow and volatility is moderate.
- **Weight:** 0.70. This is a confirmed state change with momentum behind it.
- **Change my mind:** A weekly close below 89 would take the weight back toward 0.4.

## c4549b4f90 (DOGE)
- **Read:** Earlier highs were 130+. Price crashed to 80 and based at 79–85, then broke out to 105. Since then it has ranged between 91 and 105, and 100 sits mid-range. Four-week momentum is modest (95 → 100).
- **Weight:** 0.50. The trend is up from the base, but the last month is sideways.
- **Change my mind:**
  - A close below 90 would lower the weight to 0.3.
  - A weekly close above 106 would raise it to 0.65.

## cc1807216e (SOL)
- **Read:** Broke out of a 65–70 base at day -32, then made higher lows at 87–88. Today's 100 is near new highs above the earlier 180-day high of 88. The breakout has held for four weeks.
- **Weight:** 0.65.
- **Change my mind:** A weekly close below 87 would lower the weight to about 0.4.

## d2884de3fb (LINK)
- **Read:** Rising lows at 56, 63 and 66, then a breakout to 85–96. It spiked to 106 and pulled back to 87, and has now recovered to 100. It is well above the earlier 180-day highs around 87. Four-week momentum is +10%.
- **Weight:** 0.60.
- **Change my mind:** A close below 86 would lower the weight to 0.35.

## 07527fb6b2 (LTC)
- **Read:** The 74–81 range broke at day -30. Price then made a higher low at 81.6, a high at 94, a higher low at 86.4, and is now at 100. That is a constructive staircase, with the earlier peak at 103 overhead. Four-week momentum is about +20%.
- **Weight:** 0.65.
- **Change my mind:** A close below 86 would lower the weight to 0.4.

## f79e1dfb1e (XRP)
- **Read:** The decline into 70 ended in a violent spike: a wick to 120 and a close at 103. Since then it has chopped between 89 and 108 on heavy volume, with wide daily swings (101 → 91 → 100). Four-week momentum is flat (98 → 100). This is sideways with high volatility.
- **Weight:** 0.40.
- **Change my mind:**
  - A close below 89 would lower the weight to 0.2.
  - A weekly close above 108 would raise it to 0.6.

## 8bbec28bc5 (BTC)
- **Read:** Crash to 72, then a recovery and a breakout to 96. It has held a tight 93–100 range for four weeks with low volatility. Today's 100 is at the range top and near the earlier highs around 101. The trend is up and orderly.
- **Weight:** 0.65. Low volatility supports a larger size.
- **Change my mind:** A weekly close below 93 would lower the weight to 0.4.

## 6bd5c4ae71 (DOT)
- **Read:** Downtrend from 123 to 66. A first breakout to 83 failed back to 72. A second surge spiked to 110, crashed to 83, and has rebounded to 100. That makes a higher low (83 vs 72), and four-week momentum is +35%. Volatility is very high, with 10%+ daily ranges.
- **Weight:** 0.45. The direction is up, but the size is cut for volatility.
- **Change my mind:**
  - A close below 88 would lower the weight to 0.25.
  - A weekly close above 110 would raise it to 0.6.

{"e615362136 (AVAX)": 0.4, "35ba2b9b22 (ADA)": 0.6, "33b0546954 (ETH)": 0.7, "c4549b4f90 (DOGE)": 0.5, "cc1807216e (SOL)": 0.65, "d2884de3fb (LINK)": 0.6, "07527fb6b2 (LTC)": 0.65, "f79e1dfb1e (XRP)": 0.4, "8bbec28bc5 (BTC)": 0.65, "6bd5c4ae71 (DOT)": 0.45}

## Entscheidung 2026-09-27

**Strategy:** Every window applies the same rule. Go long when 2 to 4 weeks of weekly closes point the same way and a breakout has held over several weekly closes. Cut size when volatility is high, or when the move comes mainly from one extreme week with heavy volume. Position in the range alone changes nothing; with no confirmed state, stay near 0.5.

All ten windows share a pattern: a crash around day −115, a base near 55–70, a breakout at day −39, and a rally into the 100 close. They differ in how clean the trend is and how volatile.

## 9ca53b2d31 (DOT)
- **Market:** Uptrend out of a 59–68 base. Weekly closes ran 64.6 → 68.8 → 80.4 → 89.5 → 100. The spike at day −19 to 101 failed down to 74.5, but price has now recovered to the 100–103 zone. The prior range top from day −140 is 105–113. Daily ranges are wide, at 5–10 %.
- **Weight:** 0.6. Momentum is confirmed, but high volatility keeps the size down.
- **Change my mind:** a close below 86 (the low at day −4).

## 3e1a23fe5f (ETH)
- **Market:** Breakout at day −39 from 71 to about 90, which held between 88 and 95 for 5 weeks. Then it stepped to 100–104 at day −6 and is holding there with falling volatility. Prior highs were near 91.
- **Weight:** 0.8. This is a clean breakout held over several weekly closes.
- **Change my mind:** a close below 89.

## 35edaa6685 (DOGE)
- **Market:** Choppy recovery. The spike at day −36 reached 104, followed by a range of 83–98. The spike at day −6 to 109 fell back to 95.7, and price now sits at 100. Older resistance is at 113–122. Volume and volatility are high.
- **Weight:** 0.55. Momentum is positive but noisy, with no held breakout.
- **Change my mind:** a close below 94.

## e059397518 (XRP)
- **Market:** The blow-off at day −36 to 112 was followed by a range of 84–104 for 5 weeks. Price is at 100, near the top of that range. Four-week momentum is only about +5 %, volatility is high, and the bars show wide wicks on both sides.
- **Weight:** 0.5. This reads as sideways, so the weight stays near its mean.
- **Change my mind:** a weekly close above 106 (raise the weight) or below 84 (cut it).

## 75e2abfa93 (LINK)
- **Market:** Steady higher highs and higher lows: 75 → 85 → 94 → 103. The lows rose from 77.6 to 86. Price is at the window high, with a prior peak of 77.5.
- **Weight:** 0.8. The trend is clean and confirmed over several weeks.
- **Change my mind:** a close below 86.

## f451f7d5e6 (ADA)
- **Market:** Higher lows at 75.5, 76.6 and 91.5, and a series of weekly highs at 89 → 92 → 101 → 104. Price at 100 sits just under the day −140 range of 106–113. Volatility is high.
- **Weight:** 0.65.
- **Change my mind:** a close below 91.

## e36c2053b3 (LTC)
- **Market:** Uptrend from 69 to 87 over 3 weeks, then an extreme bar at day −3 to 105 on 6.7× volume. Price has held 100–102 for three days. The prior high was 85.
- **Weight:** 0.6. Momentum is confirmed, but the latest week is extreme, so the size stays moderate.
- **Change my mind:** a close below 87.

## aaa985b852 (BTC)
- **Market:** Breakout at day −39, which held between 90 and 96 for 5 weeks. A step to 102.5 at day −6 is holding near 100 on low volatility. The prior high was 98.
- **Weight:** 0.8. This is a held breakout in a quiet regime.
- **Change my mind:** a close below 90.

## a54acd6c1b (SOL)
- **Market:** Higher highs and higher lows: 89.5 → 93.7 → 98.4 → 102.4, with lows rising from 79.4 to 92.6. Price is at the window high, and volatility is moderate.
- **Weight:** 0.75.
- **Change my mind:** a close below 92.

## 4a343e75ec (AVAX)
- **Market:** A long base at 57–62. A modest move to about 74 was followed by a single explosive week at days −8 and −7, from 70 to 105 on 5.7× volume. Price has consolidated between 92 and 105 for one week.
- **Weight:** 0.45. This is one extreme week with only one week of follow-through, so a pullback is more likely and volatility is very high.
- **Change my mind:** a weekly close above 106 (raise the weight) or below 91 (cut it).

```json
{"9ca53b2d31 (DOT)": 0.6, "3e1a23fe5f (ETH)": 0.8, "35edaa6685 (DOGE)": 0.55, "e059397518 (XRP)": 0.5, "75e2abfa93 (LINK)": 0.8, "f451f7d5e6 (ADA)": 0.65, "e36c2053b3 (LTC)": 0.6, "aaa985b852 (BTC)": 0.8, "a54acd6c1b (SOL)": 0.75, "4a343e75ec (AVAX)": 0.45}
```
