# E-012: was die KI gedacht hat (Set A)

Volle Antwort des Deciders pro Entscheidungswoche, unverändert. Er sah weder Datum noch Coin-Namen; die Namen in Klammern sind erst danach eingesetzt. Gesendeter Prompt und Daten: runs/<set>/<woche>/requests.json.

## Entscheidung 2026-07-05

**Strategy:** All ten windows share the same shape. Each has a six-month downtrend, roughly halving from the start, then a crash around day -150, a range, a second breakdown around day -33, and a rebound into the decision day. My default is therefore a low weight, because the long-term trend and the overhead supply put deep-loss risk above average. I add exposure only where the recent bounce has a higher low and a higher high (an early reversal). I cut further where the bounce came off a lower low, which means the downtrend is still intact.

### 7a33a16ed9 (XRP)
- **Read:** Price fell from 199 to 100. It ranged between 114 and 128, broke down to 90.7 at day -29, and bounced to 111.8. It then made a lower low at 87.5 on day -10 and has rallied back to 100.
- **Structure:** Lower lows and lower highs, with overhead resistance at 102–108 and support at 87.5.
- **Weight: 0.25.** The trend is down and the bounce is not yet confirmed.
- **Change my mind:** A close above 108 means add. A close below 87 means go flat.

### 2ac640639a (ADA)
- **Read:** Price fell from 221 to 100. It crashed from a 125–150 range to 78 at day -29, then made a lower low at 72.9 on day -10. The last four days show a violent rally of about +32% on heavy volume, up to a 105.5 high.
- **Structure:** The reversal thrust is real, but it runs straight into heavy overhead supply from 105 to 125. Pullback risk after a move this extended is high.
- **Weight: 0.3.**
- **Change my mind:** A close above 106 means add. A close below 92 means cut. A close below 84 means flat.

### 8c76be2375 (LTC)
- **Read:** Price fell from 183 to 100. It broke down from a 112–132 range to 88.4 at day -29 and rebounded to 101. The retest low at 85.7 on day -10 was only marginally lower, and price now sits at its 20-day high.
- **Structure:** Roughly a double bottom near 86–88, testing 101 resistance.
- **Weight: 0.3.**
- **Change my mind:** A close above 102 means raise. A close below 89 means cut. A close below 85.5 means flat.

### 1f82221eca (ETH)
- **Read:** Price fell from 184 to 100. It broke down from a 112–135 range to a low of 84.3 at day -29 and bounced to 103.6. It retested the low at 84.7 on day -9, then rallied to 100.
- **Structure:** A clean double bottom at about 84.5, with the neckline at 103.6.
- **Weight: 0.3.** The pattern is not yet confirmed.
- **Change my mind:** A close above 104 means raise. A close below 88 means cut. A close below 84 means flat.

### afb46a7eb7 (LINK)
- **Read:** Price fell from 174 to 100. It broke down from a 108–134 range to 86.8 and bounced to 106.7. It retested the low at 86.9 on day -10 and is now at 100.
- **Structure:** A double bottom near 87, with the neckline at 106.7. Volume on the bounce is light.
- **Weight: 0.3.**
- **Change my mind:** A close above 107 means raise. A close below 87 means flat.

### 2aa0992b2f (DOT)
- **Read:** This is the steepest decline in the set, from 253 to 100. Price made lower highs through the 135–160 area, crashed to 100.3, bounced to 118.8, and then made a lower low at 90.2 on day -7.
- **Structure:** The downtrend is fully intact. Resistance sits at 102 and 119, support at 90.
- **Weight: 0.2.**
- **Change my mind:** A close above 103, and then above 119, means add. A close below 90 means flat.

### c71f05b662 (BTC)
- **Read:** This is a milder decline, from 147 to 100. Price broke down from a 115–128 range to 92.9, bounced to 105.7, and then made a slightly lower low at 90.8 on day -4. It is now at 100 on low volume.
- **Structure:** Lower lows, though volatility is the lowest in the set.
- **Weight: 0.25.**
- **Change my mind:** A close above 106 means raise. A close below 90.5 means flat.

### 59ea2777a3 (AVAX)
- **Read:** Price fell from 211 to 100. It broke down from a 125–150 range to 89.9. A capitulation flush on day -16 reached 82 on 3x volume, followed by higher lows near 86 and a high of 102.8 on day -1, which is above the day -20 bounce high of 102.2.
- **Structure:** An early higher-low/higher-high sequence after a volume climax.
- **Weight: 0.35.**
- **Change my mind:** A close above 103 means raise toward 0.5. A close below 91 means cut. A close below 86 means flat.

### 12b26170cd (SOL)
- **Read:** Price fell from 173 to 100. It broke down from a 100–120 range to 73.7 at day -29 and bounced to 93.3. It then made a higher low at 78.5 on day -10 and has rallied to 100, clearing the 93.3 bounce high.
- **Structure:** This is the only window with a clear higher low and higher high. Price is now retesting the old breakdown level at about 100.
- **Weight: 0.45.**
- **Change my mind:** A close above 103 means raise. A close below 93 means cut. A close below 85 means flat.

### 10d6cc64a8 (DOGE)
- **Read:** Price fell from 193 to 100. It rallied to 152 at day -52, then failed. It broke down to 99.7, bounced to 118.7, and then made a lower low at 89.3 on day -5.
- **Structure:** A failed rally followed by lower lows, with resistance at 102 and 113–119.
- **Weight: 0.2.**
- **Change my mind:** A close above 103 means add. A close below 89 means flat.

{"7a33a16ed9 (XRP)": 0.25, "2ac640639a (ADA)": 0.3, "8c76be2375 (LTC)": 0.3, "1f82221eca (ETH)": 0.3, "afb46a7eb7 (LINK)": 0.3, "2aa0992b2f (DOT)": 0.2, "c71f05b662 (BTC)": 0.25, "59ea2777a3 (AVAX)": 0.35, "12b26170cd (SOL)": 0.45, "10d6cc64a8 (DOGE)": 0.2}

## Entscheidung 2026-07-12

# Analysis

## Strategy
All ten windows share the same shape: a long downtrend from roughly 150–270 down to 100, a range, a capitulation leg about 40 days ago, and a retest of those lows about 2–3 weeks ago. My rule has three parts:
- **Base weight.** Price sits well below its 50- and 180-day structure in every window, so the base weight is low (about 0.15).
- **Higher low.** If the recent retest made a higher low or a clean double bottom, I raise the weight to 0.3–0.35.
- **Failed rally.** If the retest made a clear lower low, or a rally failed and fully reversed, I cut the weight to 0.1.

## e55d3288ad (AVAX)
- **Market read:** Price fell from 230 to 100. It broke down from a 135–160 range at day -40, then capitulated to 88.7 at day -23. It then made a higher low near 93, rallied to 111, and is now back at 100. It remains far below the old range.
- **Weight: 0.2.** The higher low is mildly constructive, but the downtrend is intact.
- **Change my mind:** above 111 I would raise the weight; below 88.7 I would go to 0.

## 089896ac48 (XRP)
- **Market read:** Price fell from 197 to 100 and broke from a 120–140 range. It found a low at 96.7, bounced to 119, then made a lower low at 92.9. It rallied to 109 and has faded to 100.
- **Weight: 0.15.** The lows are still getting lower.
- **Change my mind:** above 109 I would raise; below 92.9 I would go to 0.

## cae45c172b (LTC)
- **Market read:** Price fell from 174 to 100. It found a low at 92.1, bounced to 105, then made a lower low at 89.3. It rallied to 105 and is now at 100.
- **Weight: 0.15.** The trend is down with lower lows.
- **Change my mind:** above 105 I would raise; below 89.3 I would go to 0.

## 1ea5bc02a5 (SOL)
- **Market read:** Price fell from 190 to 100. It capitulated to 78.2, made a higher low at 83.3, then rallied strongly to 109. It is now pulling back to 100.
- **Weight: 0.35.** This is the clearest higher-low recovery of the set.
- **Change my mind:** above 109 I would raise; below 95 I would cut; below 83 I would go to 0.

## e119b6de2c (BTC)
- **Market read:** Price fell from 152 to 100. It found a low at 92.7, then made a marginally lower low at 90.6. It has crept back to 101 on low volatility.
- **Weight: 0.2.** The bottoming attempt is not confirmed.
- **Change my mind:** above 104 I would raise; below 90.6 I would go to 0.

## f3bd0188d0 (DOGE)
- **Market read:** Price fell from 202 to 100. A rally to 163 failed and crashed to 107. It made a lower high at 127 and a lower low at 95.6, rallied to 109, and is now at 100.
- **Weight: 0.15.** The pattern is lower highs and lower lows.
- **Change my mind:** above 109 I would raise; below 95.6 I would go to 0.

## 7a41d5234f (ETH)
- **Market read:** Price fell from 185 to 100. It formed a double bottom at about 83.3 and 83.7, rallied to the 101.5 neckline, and is now testing it at 100.
- **Weight: 0.3.** The base is constructive, but the breakout is not yet confirmed.
- **Change my mind:** above 102 I would raise; below 93 I would cut; below 83 I would go to 0.

## 002e35eb26 (LINK)
- **Market read:** Price fell from 176 to 100. It formed a double bottom at about 87.5 and 87.7, rallied to 102, and is now at 100.
- **Weight: 0.3.** The base is constructive, but the breakout is not yet confirmed.
- **Change my mind:** above 102.5 I would raise; below 94 I would cut; below 87.5 I would go to 0.

## 87f88d2ae9 (ADA)
- **Market read:** Price fell from 260 to 100. It found a low at 91.7, then made a lower low at 85.3. It spiked on high volume to 123, and that spike fully retraced back to 100.
- **Weight: 0.1.** A failed breakout is bearish.
- **Change my mind:** above 108 I would raise; below 85 I would go to 0.

## 2682eee075 (DOT)
- **Market read:** Price fell from 270 to 100. It found a low at 104.7, then made a lower low at 94.2. It rallied to 107.6 and is now at 100.
- **Weight: 0.15.** The lows are still getting lower.
- **Change my mind:** above 108 I would raise; below 94 I would go to 0.

{"e55d3288ad (AVAX)": 0.2, "089896ac48 (XRP)": 0.15, "cae45c172b (LTC)": 0.15, "1ea5bc02a5 (SOL)": 0.35, "e119b6de2c (BTC)": 0.2, "f3bd0188d0 (DOGE)": 0.15, "7a41d5234f (ETH)": 0.3, "002e35eb26 (LINK)": 0.3, "87f88d2ae9 (ADA)": 0.1, "2682eee075 (DOT)": 0.15}

## Entscheidung 2026-07-19

## Strategy
Every window is in a long-term downtrend: price is 30–60% below where it was 180 days ago, with a crash near day −164, a second leg down near day −45, and lower highs since. In that kind of regime I cap exposure at about 0.55 and never go fully long. Within the cap, I add weight when the last 4–6 weeks show a base: higher swing lows, price above the post-crash range midpoint, and recent swing highs reclaimed. I cut weight when price sits at the bottom of its range and is still making lower highs.

## 36653c82ee (DOGE)
- **Read:** A steady bleed from 140 (day −48) to 100. The low of the last 20 days is 96.0. Highs keep getting lower: 108.4, then 104.1, then 102.9. Price sits near the bottom of a 96–108 box, and the very low volume shows no buying interest.
- **Weight: 0.2.** The structure is still pointing down and there is no confirmed base.
- **Change my mind:** above 108.5 I would raise the weight. A close below 96 takes it to 0.

## 2d66f8c2ef (XRP)
- **Read:** The low was 91.9 (day −23), followed by a bounce to 107.9 that has faded back to 100. Highs are lower in sequence: 117.8, 107.9, 103.0. The lows are only marginally higher, from 92 to 96.
- **Weight: 0.3.**
- **Change my mind:** above 108 I would raise. Below 96 I would cut.

## 735bd2efe0 (BTC)
- **Read:** A smoother decline, with the low at 89.3 (day −18) and a steady climb since. Recent lows are rising (95.5, then 96.6), and price is pressing the 100–101.4 ceiling.
- **Weight: 0.45.** The base is constructive, but the bigger trend is still down.
- **Change my mind:** a close above 101.7 (then 104) would raise it. Below 95.5 I would cut.

## 04b61827df (LTC)
- **Read:** The double low is 83.5 (days −25 and −24). Lows have risen since: 87.4, then 91.2, then 93.7. On day −1 price broke out to 101.7 on above-average volume, clearing the prior highs at 98.0–98.3. This is the best structure of the set.
- **Weight: 0.55.**
- **Change my mind:** holding above 102 would raise the weight. Below 93 I would cut.

## 7fd7fecb23 (DOT)
- **Read:** The deepest long-term damage of the set, down from 238. The low is 97.0 (day −21), and the range is 97–110.7 with lower highs: 110.7, 109.1, 106.6. On day 0 price slid to 98.3 and is sitting near the range floor.
- **Weight: 0.25.**
- **Change my mind:** a close below 97 takes it to 0. Above 107 I would raise.

## 0efb55c976 (ETH)
- **Read:** A double bottom at 80.4 and 80.8, then a rally to 104.0 that cleared the day −34 high of 98.8. The pullback lows are holding higher, at 93.5 and then 96.3.
- **Weight: 0.45.**
- **Change my mind:** above 104 I would raise. Below 93 I would cut.

## 85fc9efb72 (AVAX)
- **Read:** The low was 87.9 on a volume spike (day −30), followed by chop between 97 and 110. Highs are lower (110.1, 105.7, 104.8), and day 0 printed a low of 98.9.
- **Weight: 0.3.**
- **Change my mind:** above 105 I would raise. Below 97 I would cut.

## 619b7ead0c (ADA)
- **Read:** The low was 83.1 (day −24), followed by a violent spike to 120.3 that fully retraced to 100. That is a failed breakout. The recent lows of 93.4 and 94.9 are holding, but volatility is high.
- **Weight: 0.3.**
- **Change my mind:** above 102 I would raise. Below 93 the weight goes to 0.

## 0ab9bf284f (LINK)
- **Read:** A double low at 83.4 and 83.6, then a rally to 103.0 above the day −34 high of 102.6. Lows are higher at 93.0 and then 95.5, and volume during the pullback is light.
- **Weight: 0.45.**
- **Change my mind:** above 103 I would raise. Below 93 I would cut.

## fac11c0043 (SOL)
- **Read:** The low was 78.7 (day −43), with a higher low at 83.8 (day −24). Price then rallied to 110.0 and has pulled back to 96–100. It is still above the earlier swing high of 99.6, so the pattern of higher lows is intact.
- **Weight: 0.45.**
- **Change my mind:** above 104 I would raise. Below 96 I would cut.

{"36653c82ee (DOGE)": 0.2, "2d66f8c2ef (XRP)": 0.3, "735bd2efe0 (BTC)": 0.45, "04b61827df (LTC)": 0.55, "7fd7fecb23 (DOT)": 0.25, "0efb55c976 (ETH)": 0.45, "85fc9efb72 (AVAX)": 0.3, "619b7ead0c (ADA)": 0.3, "0ab9bf284f (LINK)": 0.45, "fac11c0043 (SOL)": 0.45}

## Entscheidung 2026-07-26

## Strategy

Every window shows the same general pattern: a crash early in the window, a choppy range, a second sharp drop around day −54 to −51, and then a recovery to 100. Two things set the weight. The first is the shape of the recovery: higher lows above the crash low push the weight up, while lower lows or lower highs push it down. The second is where price sits inside its last 30-day range. All windows are still well below their levels from before the second crash, so no window gets full weight. If price closes below the most recent swing low, the recovery has failed and the weight goes to 0.

## 067ee05663 (LTC)
- **Trend:** The crash low was 84.7 at day −50, followed by a marginal lower low of 82.1 at −31.
- **Structure:** Since then there is a clean series of higher lows: 86.0, 89.7, 95.6.
- **Day 0:** Closed at 100, a 50-day closing high, and broke out of the 94–99 shelf. The pre-crash range was about 108–110.
- **Weight:** 0.7. The recovery is constructive and volatility has calmed.
- **Change of mind:** A close below 95.6 cuts the weight to about 0.2. A move above 105 raises it.

## 1570d90c86 (ETH)
- **Trend:** Double bottom at 77.0 and 77.4 (days −50 and −30).
- **Structure:** Higher lows at 87.7 and 94.5. The climb from 77 to 100 is about 30%.
- **Day 0:** Closed at 100, just under the 100.1–100.6 highs. The pre-crash level was about 103.
- **Weight:** 0.7.
- **Change of mind:** A close below 94.5 cuts the weight. A clean move above 101 confirms it.

## db5a87e166 (LINK)
- **Trend:** Double bottom at 79.3 and 79.4.
- **Structure:** Higher lows at 85.2 and 93.7.
- **Day 0:** Closed at 100, above the prior high of 99.3. The pre-crash level was about 103.
- **Weight:** 0.7.
- **Change of mind:** A close below 93.7 cuts the weight.

## 42ea69bb24 (DOGE)
- **Trend:** Down from a peak of 157 at day −73. The lows keep getting lower: 105.8, then 97.4, 94.7, and 92.9 at day −2.
- **Structure:** The highs are also falling: 108, then 103, then 101. Price is still in a downtrend and is now at the top of a 93–101 range.
- **Weight:** 0.4. The trend is down, but price has been compressing.
- **Change of mind:** A close below 92.9 sends the weight to 0. A close above 103 raises it to about 0.6.

## 7b62891dae (ADA)
- **Trend:** Crash to 89.5, then a lower low of 83.3 at day −31.
- **Structure:** A spike to 120.5 at day −22 fully faded back to 93.6. Since then price has been chopping between 97 and 109.
- **Risk:** Volatility is very high, and the pre-crash level was about 140, so the overhead supply is heavy.
- **Weight:** 0.4.
- **Change of mind:** A close below 93.6 sends the weight to 0. A close above 109 raises it.

## a82e89f0be (AVAX)
- **Trend:** Crash low of 92.3, then a lower low of 84.2 at day −37.
- **Structure:** Higher lows since then at 88.3, 91.0 and 93.1. Range of 91 to 105.5.
- **Day 0:** Followed a large up-day on volume from 92.9.
- **Weight:** 0.5.
- **Change of mind:** A close below 91 sends the weight to 0. A close above 105.5 raises it to 0.7.

## a8780e6420 (DOT)
- **Trend:** The weakest window. A steady decline from 200 to 106.8 at the crash, then lower lows of 96.0 and 95.0.
- **Structure:** Lower highs: 109.7, 108.1, 105.6, 105.0.
- **Day 0:** Closed at 100, mid-range.
- **Weight:** 0.3.
- **Change of mind:** A close below 95 sends the weight to 0. A close above 108 raises it to 0.5.

## 99313fbdef (SOL)
- **Trend:** Crash low of 78.3, then a higher low of 83.4.
- **Structure:** A strong rally to 109.4, then a pullback that held at 95.6 and 95.7, forming a double support.
- **Day 0:** Closed at 100.
- **Weight:** 0.6.
- **Change of mind:** A close below 95.6 cuts the weight to about 0.1. A close above 103 raises it.

## 62441ba289 (XRP)
- **Trend:** Crash low of 94.3, then a lower low of 90.7.
- **Structure:** A rally to 106.4, then pullback lows of 94.6 and 97.5. Range of 94.6 to 106.
- **Day 0:** Closed at 100, on very light volume.
- **Weight:** 0.5.
- **Change of mind:** A close below 94.6 sends the weight to 0. A close above 105 raises it.

## 4254ee64c3 (BTC)
- **Trend:** Crash low of 90.4, then a slight lower low of 88.4 at day −25.
- **Structure:** A steady low-volatility staircase of higher lows: 93.7, 94.5, 95.6, 96.5, 97.5.
- **Day 0:** Closed at 100, near the high of 102.4. The pre-crash level was about 112.
- **Weight:** 0.6.
- **Change of mind:** A close below 96.5 cuts the weight. A close above 102.5 raises it to 0.8.

{"067ee05663 (LTC)": 0.7, "1570d90c86 (ETH)": 0.7, "db5a87e166 (LINK)": 0.7, "42ea69bb24 (DOGE)": 0.4, "7b62891dae (ADA)": 0.4, "a82e89f0be (AVAX)": 0.5, "a8780e6420 (DOT)": 0.3, "99313fbdef (SOL)": 0.6, "62441ba289 (XRP)": 0.5, "4254ee64c3 (BTC)": 0.6}

## Entscheidung 2026-08-02

## Strategy

All ten windows share the same shape: a sharp crash about 58 to 61 days ago, then some kind of recovery. My rule is to judge the recovery's structure since the crash low and over the last 30 days.

- **Higher lows and higher highs** (a basing recovery that holds support): stay mostly long, 0.55–0.65.
- **Lower highs pressing on flat support** (a descending pattern inside a long downtrend): cut to 0.15–0.3.
- **Choppy ranges**: sit in between.

Each weight comes with a support level that cuts it and a resistance level that raises it.

## 2fbb91204e (ETH)
- **Read:** The fall from 128 (day -107) ended in a crash low of about 80 at day -57, and a retest at 80.2 (day -37) held as a double bottom. The rally reached 103.6 at day -12. For the last 20 days price has held a 97–105 range with rising lows (92.5, 95.6, 98, 96.6). Price is at 100, mid-range, after a firm close.
- **Weight: 0.6.** The recovery structure is intact, but price is still well below the 110–125 levels from before the crash.
- **Change mind:** below 96.5 cut to 0.2; a close above 105 raises to 0.8.

## 7695b320b2 (XRP)
- **Read:** The peak was 142.6 (day -80) and the crash low 96.6 (day -57). A second low at 92.9 came at day -37. Since the 109 high at day -29 the highs keep falling: 107.1, 102.7, 100.6. Support sits at 96–96.5, so this is a descending triangle inside a long downtrend.
- **Weight: 0.3.**
- **Change mind:** below 96 go to 0.0; above 105 raise to 0.6.

## 3f8e3e3c24 (DOGE)
- **Read:** The fall runs from 167.5 (day -80) to 98.2 (day -33). Lower highs since the 112 high at day -29: 106.5, 104.6, 100.9. Support is at 96.3–97, and the move lacks volume. The persistent downtrend has not been repaired.
- **Weight: 0.2.**
- **Change mind:** below 96 go to 0.0; above 106.5 raise to 0.5.

## d96a5059ce (SOL)
- **Read:** A strong V-recovery ran from 81.7 (day -57) to 114 (day -29). Since then it has been fading with lower highs (107.3, 105.3, 102.3) and slightly lower lows: 98.2, then 95.9 at day -1. Price is at 100, about where its 50-day average sits.
- **Weight: 0.4.** The recovery is real, but the short-term trend is rolling over.
- **Change mind:** below 95.9 cut to 0.1; above 105.5 raise to 0.7.

## 1cefae7f1b (DOT)
- **Read:** This is a long decline from 180–219 down to a crash low of 110.6, followed by a lower low at 99.5 (day -35). After the 113.6 high at day -27 the highs kept falling (112, 109.4, 104). A high-volume breakdown to 93.6 at day -6 set a new low. Price has bounced back to 100, but the trend is still down.
- **Weight: 0.15.**
- **Change mind:** below 93 go to 0.0; a close above 104 raises to 0.5.

## 8f90c2db33 (BTC)
- **Read:** This one had a milder crash, from 130 to 93, and a base at 90.9–91.4 (days -38 to -32). It rallied to 105.3 at day -12. The last 20 days form a tight 97–105 range with steady lows at 97.3, 98.4, 98.7 and 98.0, and volume is calm.
- **Weight: 0.6.**
- **Change mind:** below 97.3 cut to 0.25; above 105.3 raise to 0.85.

## 043cf80b2e (LINK)
- **Read:** A double bottom formed at 83.4 and 83.6 (days -57 and -38). Price broke the 102.6 neckline to reach 106.3 at day -6, then pulled back to 94.1 at day -1. Day 0 was a strong reclaim to 100, which makes this a retest of the breakout zone.
- **Weight: 0.55.**
- **Change mind:** below 94 cut to 0.15; above 106.3 raise to 0.85.

## 40ce88c0e7 (AVAX)
- **Read:** A two-stage crash went from 160 to 95, then to 86.7 at day -44. The rally reached 108.6 at day -29. Since then price has chopped between 92 and 105, and the lows have been slipping: 96.4, 95.9, 93.7, 92.2. Day 0 was a strong reversal candle from 94.5 to 100 on above-average volume.
- **Weight: 0.4.**
- **Change mind:** below 92 go to 0.0; above 105 raise to 0.7.

## 85f930ba3a (ADA)
- **Read:** The deepest crash in the set ran from 152 to 78.4, then to a lower low of 72.9 at day -38. A high-volume spike to 105.5 at day -29 faded fully, back to 82. Since then the lows have been higher (80.9–82). Day 0 broke out from 92 to 100 on the highest volume in weeks, clearing the 95.4 swing high. Momentum is up, but volatility is high and the last spike failed. Resistance is at 105.5.
- **Weight: 0.5.**
- **Change mind:** below 88 cut to 0.15; a close above 105.5 raises to 0.8.

## 7a84fab078 (LTC)
- **Read:** The crash here was milder, from 135.6 to 90.7, with a low of 87.9 at day -38. Since then the trend is clean: higher lows (96.6, 96.0, 97.6) and higher highs (103.3, 107.7, 108). Price is now pulling back to 100 on light volume, which looks like a normal retracement inside an uptrend.
- **Weight: 0.65.**
- **Change mind:** below 96 cut to 0.25; above 108 raise to 0.9.

{"2fbb91204e (ETH)": 0.6, "7695b320b2 (XRP)": 0.3, "3f8e3e3c24 (DOGE)": 0.2, "d96a5059ce (SOL)": 0.4, "1cefae7f1b (DOT)": 0.15, "8f90c2db33 (BTC)": 0.6, "043cf80b2e (LINK)": 0.55, "40ce88c0e7 (AVAX)": 0.4, "85f930ba3a (ADA)": 0.5, "7a84fab078 (LTC)": 0.65}

## Entscheidung 2026-08-09

**Strategy:** I hold more when the market has recovered from its crash low with higher lows and is trading above its recent range support. I cut exposure when it is still making lower highs and sits near or below support. A close beyond the window's key level, the recent swing low or the range top, is what changes the weight.

---

### 74df12051a (DOT)
- **Read:** A long downtrend from about 208 (day -165). It crashed to about 110 (day -64), slid further to 99.5 (day -42), and has ranged 93.6–110 since. The highs keep getting lower: 110.8, 107.5, 107.3. It closed at 100, below the middle of the range, after failing at 108.9.
- **Weight:** 0.2. The trend is still down, and support at 93.6 is only 6% away.
- **Change my mind:** a close above 109 would make me add; a close below 93.5 would take me flat.

### a3bd01713f (DOGE)
- **Read:** It fell from 171 (day -87), crashed, and kept making lower lows down to 100 (day -40). After a bounce to 114.5, the highs fell to 108.7, 106.8, then 103.2. For the last 20 days it has been a tight 98.4–103 coil on fading volume, with no sign of buyers.
- **Weight:** 0.25.
- **Change my mind:** a close below 98 would take me to 0; a close above 107 would take me to about 0.6.

### fef9aa9ccd (LINK)
- **Read:** It peaked at 132.8 (day -91), crashed to 85.5, and retested 85.6 (day -45). Since then the recovery has made higher lows (91.9, then 96.3) and highs of 105–108.9. It closed at 100, mid-range, above the rising base.
- **Weight:** 0.5. The structure is improving but it is still range-bound.
- **Change my mind:** a close below 96 would cut me to 0.2; a close above 109 would take me to 0.8.

### 98cd081901 (ETH)
- **Read:** It fell from 129 to a crash low of 78.8, then retested 79.1 (day -44). The recovery is clean: higher lows at 89.7, 94.4 and 95.4, and higher highs at 101.9 then 103.7. It is consolidating at 100, near the top of the recovery.
- **Weight:** 0.6. This is the strongest structure of the set.
- **Change my mind:** a close below 95 would cut me to 0.2; a close above 104 would take me to 0.8.

### d40a1db1a6 (ADA)
- **Read:** A very volatile chart. It crashed to 71 (day -45), spiked to 102.8, fell back to 79–80 twice, then broke out of the 80–93 base on volume to a high of 108.8 (day -3). It has pulled back to 100. The momentum is real, but daily ranges of 4–8% mean a deep-loss risk.
- **Weight:** 0.45.
- **Change my mind:** a close below 93, back into the old base, would cut me to 0.1; a close above 105 would take me to 0.7.

### 89f4ae042c (XRP)
- **Read:** It fell from 146 (day -91) to 102, then to 98 (day -45). After a bounce to 115, the highs fell to 113, 108.8, 106.2. Price has slipped to 98.3–100, its lowest closes since day -40, and is testing range support.
- **Weight:** 0.2.
- **Change my mind:** a close below 98 would take me to 0; a close above 108 would take me to 0.5.

### 123173d2a2 (LTC)
- **Read:** It fell from 133 to 89 and retested 86.4 (day -45). It recovered to 105.9, then made a higher low at 96.0 (day -8), and is now 100 and rising off that low. It is ranging 96–106 with modest volatility.
- **Weight:** 0.5.
- **Change my mind:** a close below 96 would cut me to 0.2; a close above 106 would take me to 0.8.

### 1ddae477a1 (BTC)
- **Read:** It fell from 127.7 to 91, retested 89.5 (day -45), recovered to 103.2, and made a higher low at 96.0 (day -9). It is the quietest tape of the set, at 100 inside a 96–103 range.
- **Weight:** 0.5.
- **Change my mind:** a close below 96 would cut me to 0.2; a close above 103.5 would take me to 0.8.

### 3707b005e2 (AVAX)
- **Read:** It fell from 163 to 97, then had a second flush to 88.5 (day -51). Since then it has made higher lows (92.7, 94.1) but flat highs (110.8, 106.6, 108.8), with wide, whippy candles. It is sideways at 100, mid-range.
- **Weight:** 0.4.
- **Change my mind:** a close below 94 would cut me to 0.1; a close above 109 would take me to 0.7.

### 00ec7e21b0 (SOL)
- **Read:** It fell from 129 to 78.8, and the rally from the 84 retest peaked at 110.1 (day -36). Since then it has drifted lower, with highs at 104.5, 103.4 and 101.6, down to 92.5 (day -8). The last two days popped to 102.1, but that has not yet broken the drift.
- **Weight:** 0.35.
- **Change my mind:** a close above 104 would take me to 0.6; a close below 92.5 would take me to 0.

---

```json
{"74df12051a (DOT)": 0.2, "a3bd01713f (DOGE)": 0.25, "fef9aa9ccd (LINK)": 0.5, "98cd081901 (ETH)": 0.6, "d40a1db1a6 (ADA)": 0.45, "89f4ae042c (XRP)": 0.2, "123173d2a2 (LTC)": 0.5, "1ddae477a1 (BTC)": 0.5, "3707b005e2 (AVAX)": 0.4, "00ec7e21b0 (SOL)": 0.35}
```

## Entscheidung 2026-08-16

## Strategy

I hold full exposure only when price is above its rising ~50-day mean and the swing structure is intact (higher lows, with breakouts that hold). When price is ranging under a series of lower highs I hold a partial weight. I go flat or near-flat when the swing structure prints lower highs and lower lows, or the window is in a steady decline. High recent volatility, such as big spikes followed by give-backs, also trims the weight.

## f4f181d79c (LINK)
- **Read:** The peak was ~115 (day -98). It crashed to ~75–78 (days -72 to -47) and then built a clean sequence of higher lows: 75 → 80 → 85 → 87. Day -1 broke out to 103.8 on 1.66× volume. Price now sits at 100, well above the ~88 50-day mean. Resistance is 104–106; support is 92–93 and then 87.
- **Weight:** 0.8. The trend is up with confirmed structure. I keep a little back because of the extended move off 87.
- **Change mind:** a close below 92 cuts the weight to ≤0.3.

## 04a8966966 (ETH)
- **Read:** The peak was ~131. It crashed to 80 and recovered to 100–105. It has spent 3 weeks in a very tight 99–103 coil on drying volume, holding above the ~97 50-day mean. The prior breakdown zone at 107–113 is overhead resistance.
- **Weight:** 0.7. The base is constructive and the risk is defined.
- **Change mind:** below 97 → 0.2. Above 105 → 1.0.

## 79b106d906 (AVAX)
- **Read:** The peak was 166. It crashed to 104 and then made a lower low at 89.7 (day -58). Since then it has ranged 96–111 for about 50 days. On day -1 a spike to 108.6 was fully rejected. Price is at 100, at the lower-middle of the range.
- **Weight:** 0.4. The range is neutral, with a bearish rejection candle.
- **Change mind:** below 96 → 0. Above 110 → 0.8.

## b82984d20e (XRP)
- **Read:** The peak was 161. Since the crash it has made persistent lower highs (124.6 → 119 → 117 → 112 → 110) and lower lows (101.9 → 99.3). Price now sits at 100, at the bottom of the trend.
- **Weight:** 0.1. This is an orderly downtrend testing new lows.
- **Change mind:** a reclaim above 106 → 0.5.

## 36ea17fec4 (SOL)
- **Read:** The peak was 131. It crashed to 80.6 and recovered to 111 (day -44). Since then it has drifted lower with highs at 105.7 / 104.3 / 104 and a low of 94.6 (day -15). Price is at 100, mid-range, on low volume.
- **Weight:** 0.4. The structure is sideways-to-soft.
- **Change mind:** below 96.5 → 0. Above 105 → 0.8.

## d19cc6cc0f (DOT)
- **Read:** A long decline from 230 to 100, with lower highs at 137.9 → 119.6 → 114.6. Price is back near the 98.6 low from day -20. There is no base.
- **Weight:** 0.0. This is a persistent downtrend.
- **Change mind:** above 115 → 0.5.

## ab9c558885 (LTC)
- **Read:** The peak was 137. It crashed to 89 and recovered to 109 (days -29 and -21). Since then it has made lower highs at 109.3 → 105.3 → 104.4, and day -2 dipped to 98.3. Price is at 100. The range is 98–109.
- **Weight:** 0.4. The range has a downward tilt.
- **Change mind:** below 98 → 0.1. Above 105.5 → 0.8.

## b0f97511ff (ADA)
- **Read:** The peak was 168. It crashed to 79 and has been extremely volatile since. There were spikes to 114 (day -43) and 121 (day -10), and both were given back. Price has slid steadily for 10 days from 115 to 100. The lows are rising (79 → 88), and the 50-day mean is about 97.
- **Weight:** 0.3. Higher lows are a positive, but realized volatility is high and momentum is fading.
- **Change mind:** below 96 → 0. A hold above 104 → 0.6.

## 5d92077e4e (DOGE)
- **Read:** The peak was 170. It crashed to 111 and then made a lower low at ~100 (day -47). The rebound reached 114 (day -43). Since then highs have stepped down from 114 → 108 → 106 → 105, and price is coiling at 98–103 on very low volume. Price is at 100.
- **Weight:** 0.3. The compression sits under declining highs.
- **Change mind:** below 98 → 0. Above 106 → 0.7.

## 3c26728cc1 (BTC)
- **Read:** The peak was 131.7. It crashed to 94 and made a low of 91.9 (day -46). It recovered to 106.4, and since then has ranged 99–106 with mild lower highs. Volatility is low and price is at 100, at the lower part of the range.
- **Weight:** 0.4. The range is neutral.
- **Change mind:** below 99 → 0.1. Above 106.5 → 0.8.

{"f4f181d79c (LINK)": 0.8, "04a8966966 (ETH)": 0.7, "79b106d906 (AVAX)": 0.4, "b82984d20e (XRP)": 0.1, "36ea17fec4 (SOL)": 0.4, "d19cc6cc0f (DOT)": 0.0, "ab9c558885 (LTC)": 0.4, "b0f97511ff (ADA)": 0.3, "5d92077e4e (DOGE)": 0.3, "3c26728cc1 (BTC)": 0.4}

## Entscheidung 2026-08-23

**Strategy:** All ten windows show the same setup. Each had a crash around day -82 to -79, then a months-long base or drift lower, then a near-vertical 18–52% spike on heavy volume over days -4 to -1. A move that steep usually gives back a large share within weeks, so the deep-loss risk is high and I keep exposure low. I allow somewhat more weight where the spike held calmly (no long blow-off wick, volume fading, tight day -1/0 candles) or grew out of a base with rising lows. I give less where day -1 is a wide climax bar on extreme volume.

## 14e066424b (DOGE)
- **Read:** The trend has been down since the 127 high, with a crash to 84 and then a flat base at 74–76. The last four days ran from 75 to a 107.9 high, about +33%. Day -1 was a climax bar: range 88.8–107.9 on 3.46× volume. The pre-crash range near 108 sits directly overhead as resistance.
- **Weight:** 0.2. Blow-off structure into resistance.
- **Change my mind:** A close above 108 would raise the weight; a close below 89 would take it to 0.

## 4c9d8dbbaf (BTC)
- **Read:** The base ran 80–84 for about 40 days, then the spike reached a 102.3 high, about +21%. Days -1 and 0 are tight consolidation bars (98.4–101.4 and 97.2–100.4) with volume falling from 1.05 to 0.87, so there is no exhaustion wick. The pre-crash range was 95–105.
- **Weight:** 0.4. The most orderly hold of the gains in this set.
- **Change my mind:** A break below 93.9 (the day -2 gap level) cuts it; a close above 102.3 adds.

## 03f75b0f16 (XRP)
- **Read:** The base at 65–67 was making lower lows. Price then went to 111.8 in four days, about +52%, with volume of 3.9, 4.5 and 6.0×. Day -1 was a 90.6–111.8 climax bar. This is the textbook blow-off.
- **Weight:** 0.1.
- **Change my mind:** Below 90.6 goes to 0; a hold above 100 for several days would allow 0.3.

## 3bdf67a898 (LTC)
- **Read:** After the crash, lows rose from 75 to 83 and then to 84–85. The spike was a modest +18%, to a 106.1 high. Day -1 had a wick down to 96.3 on 3.2× volume. The pre-crash shelf was 100–104.
- **Weight:** 0.35.
- **Change my mind:** A close below 96.3 cuts it.

## 049f5d0f81 (ADA)
- **Read:** This is a repeated pattern of failed spikes. The move to 88 at day -50 faded back to 68, and the move to 93 at day -17 faded to 77. The current spike reached a 113.8 high, with a day -1 bar of 92–113.8. History says these moves fade.
- **Weight:** 0.15.
- **Change my mind:** Below 92 goes to 0.

## 886c4c1216 (AVAX)
- **Read:** A choppy base at 81–90, then a spike to 109.3. Day -1 closed weak at 98.5 after a 92.0 low. The pre-crash level of 117 is well above.
- **Weight:** 0.2.
- **Change my mind:** Below 92 goes to 0; a close above 109.3 adds.

## 6d1490b9aa (LINK)
- **Read:** This one has a real rising structure: lows of 61, then 68, then 70, then 76–82 from day -12 onward. The spike started from that uptrend rather than a dead base. Price is now above both the pre-crash range (78–84) and the day -105 high of 94. Day -1 had a wick down to 94.7.
- **Weight:** 0.35.
- **Change my mind:** A close below 94.7 cuts it.

## 4e9640c9e5 (SOL)
- **Read:** The base sat at 75–81, then price spiked to 107.7. Day -1 was a 91.9–107.7 climax bar on 2.8× volume. The prior high near 102 (day -104) is being tested.
- **Weight:** 0.25.
- **Change my mind:** Below 92 cuts it; a hold above 102 adds.

## bdb1902e17 (DOT)
- **Read:** The macro downtrend runs from 179 to 82, with lower highs throughout. The spike reached a 111.2 high, with day -1 at 96.9–111.2. Price is still far below the pre-crash range of about 128.
- **Weight:** 0.15.
- **Change my mind:** Below 96.9 goes to 0.

## f8b56ab95e (ETH)
- **Read:** The base at 75–78 was very tight. A gap-up on day -4 started the move, which peaked at 103.4 on day -2. Days -1 and 0 drifted at 96.8–102.7 with volume fading, and there is no climax wick. Price is above the old range of 81–96.
- **Weight:** 0.35.
- **Change my mind:** Below 94.4 cuts it.

{"14e066424b (DOGE)": 0.2, "4c9d8dbbaf (BTC)": 0.4, "03f75b0f16 (XRP)": 0.1, "3bdf67a898 (LTC)": 0.35, "049f5d0f81 (ADA)": 0.15, "886c4c1216 (AVAX)": 0.2, "6d1490b9aa (LINK)": 0.35, "4e9640c9e5 (SOL)": 0.25, "bdb1902e17 (DOT)": 0.15, "f8b56ab95e (ETH)": 0.35}

## Entscheidung 2026-08-30

**Strategy:** Stay long only when the structure has repaired. That means price above the pre-crash range, a breakout that holds, and no long-wick blow-off that is fading. Cut exposure where the long-term trend is still down and the latest spike is being rejected back toward the base.

## 8ad019a88e (DOT)
- **Read:** A persistent decline from about 188 to a 92–95 base. The spike topped at 126 intraday on day -8 and has round-tripped to 100. Lower highs persist throughout.
- **Weight: 0.15.** The downtrend is intact and the blow-off was rejected, so a revisit of 92–94 is likely.
- **Change my mind:** a close above 110.

## da969945dd (DOGE)
- **Read:** A peak near 140, then a crash and a dead 84–86 base on very low volume. The spike reached 122.9, and price has given back most of it.
- **Weight: 0.3.** The base is real, but the wick is huge and the fade continues. Support is at 98.5, then 86.
- **Change my mind:** a close above 110.

## 48ee4860b5 (ETH)
- **Read:** Higher lows since the crash low of 62 (64 → 72 → 76). The gap up from 79 to 96–105 has held for 9 sessions. Price of 100 is at the top of the 180-day range (prior high about 102).
- **Weight: 0.8.** This is a genuine breakout that is holding, with intact trend structure.
- **Change my mind:** a close below 95.

## f6dbcf742f (LTC)
- **Read:** A peak at 126, a crash to 82, and a recovery with higher lows (82 → 86 → 90.5). The spike reached 115.7 and has faded to 100, sitting on the prior 98–100 resistance.
- **Weight: 0.5.** The structure is constructive, but the spike rejection is unresolved.
- **Change my mind:** below 96 (cut) or above 106 (add).

## 737322973f (ADA)
- **Read:** A crash from about 150 to 77, followed by a series of failed spikes (103, 110, now 134 intraday). Each spike faded, and this one is down from 118 to 100. Volatility is extreme.
- **Weight: 0.15.** The pattern is repeated blow-offs that retrace, so the downside toward 85–90 is open.
- **Change my mind:** a close above 112.

## 774b48611c (BTC)
- **Read:** A peak at 106, a crash to 76, and a quiet 77–85 base. The modest spike to 102 has held in a tight 99–104 range. Volatility is low.
- **Weight: 0.7.** The breakout held without a blow-off wick.
- **Change my mind:** a close below 97.

## 93fd40a457 (XRP)
- **Read:** Lower lows after the crash, with the base at 72.6 undercutting the crash low of 77. Then came a 6x-volume blow-off to 125 that has faded to 100. The long-term trend is down.
- **Weight: 0.15.** This looks like a climax; the risk is a retrace to 80–85.
- **Change my mind:** a close above 110.

## 178da88980 (AVAX)
- **Read:** A decline from 147, two crashes (87.5, then 80), and an 87–95 base. The spike reached 117 and has faded to 100.
- **Weight: 0.3.** The trend is down, and the spike's gains are mostly gone. Support is at 95, then 88.
- **Change my mind:** a close above 108.

## b14f8264df (SOL)
- **Read:** A crash to 59 and a recovery to a 71–76 base, then a staircase advance to 108.7 on day -3. Price of 100 is above the old 96 high, so this is a new 180-day high zone.
- **Weight: 0.7.** The trend is up and the pullback looks normal.
- **Change my mind:** a close below 93.

## 78dbd46d65 (LINK)
- **Read:** A peak at 97.5, a crash to 63, and then higher lows into the spike (rising from 74 to 85 beforehand). The spike to 113 is holding at 100–107, above the prior high of about 97.
- **Weight: 0.6.** The breakout is constructive but carries a wick.
- **Change my mind:** a close below 97.

{"8ad019a88e (DOT)": 0.15, "da969945dd (DOGE)": 0.3, "48ee4860b5 (ETH)": 0.8, "f6dbcf742f (LTC)": 0.5, "737322973f (ADA)": 0.15, "774b48611c (BTC)": 0.7, "93fd40a457 (XRP)": 0.15, "178da88980 (AVAX)": 0.3, "b14f8264df (SOL)": 0.7, "78dbd46d65 (LINK)": 0.6}

## Entscheidung 2026-09-06

## Strategy

Every window has the same skeleton: a crash around day −96 to −93, a base, then a high-volume breakout around day −18 to −16, a pullback, and price now at 100. The rule is to stay long when the breakout has held with higher lows and there is little overhead supply. I scale down when price is still inside a longer downtrend, when heavy pre-crash supply sits above 100, or when the breakout left long upper-wick rejections. If price closes below the post-breakout pullback low, the breakout has failed and I cut to flat.

## 32e448fa11 (LTC)
- **Read:** Before the crash the range was 95–110, with a peak at 109.9. The crash went to 75, then a base formed between 77 and 87. The breakout reached 100.9, pulled back to 86.2, and has since made higher lows at 88.2 and 90.0. Day −1 was a 2.3× volume push to 99.5, and price now sits at the 100.9 breakout high.
- **Supply:** There is overhead supply at 100–110 from the old range.
- **Weight: 0.6.** The structure is constructive, but price is testing resistance under the old range.
- **Change my mind:** A close below 90 cuts the position. Holding above 101 would raise it.

## 26119be63b (ETH)
- **Read:** The crash took price to 60 and the base sat at 62–77. Then came a vertical breakout from 76 to 100. Since then price has held a tight 93.7–102 range for 15 days on fading volume, which is clean digestion.
- **Supply:** Little supply remains overhead; the old highs are 96–98.
- **Weight: 0.8.**
- **Change my mind:** A close below 93.7.

## 908513f860 (BTC)
- **Read:** The old peak was 103.1. The crash went to 73.6 and the base sat at 77–83. The breakout reached 97.5, and price has consolidated at 94.9–101.4 with shallow pullbacks and quiet volume.
- **Weight: 0.8.**
- **Change my mind:** A close below 94.9.

## 1836e847bb (DOT)
- **Read:** This is a long-term downtrend from about 155, with lower highs at 142, 107, 92.7 and 88.9. The breakout cleared 88.9 and spiked to 105.4, then fell back to 82.5. Price has now rallied to 100, with today a 1.7× volume push.
- **Supply:** Volatility is high and there is heavy supply at 120–140.
- **Weight: 0.5.** This is a trend-change attempt, but it is volatile and unproven.
- **Change my mind:** A close below 85.6. The deeper line is 82.5.

## 614528b5ba (SOL)
- **Read:** The old range was 77–92. The crash went to 56 and the base sat at 66–78. The breakout reached 103.8, and price has consolidated at 91.4–103.8 with higher lows.
- **Supply:** Price is above all the pre-crash structure, so supply is minimal.
- **Weight: 0.8.**
- **Change my mind:** A close below 91.4.

## beca5ffe67 (AVAX)
- **Read:** This is a longer downtrend from 120–130. There were two capitulations, at 78.7 and 71.8, and the base sat at 76–88. The breakout spiked to 105.2, pulled back to 88.7, and has now worked back up to 100 with higher lows.
- **Supply:** There is supply at 110–130.
- **Weight: 0.6.**
- **Change my mind:** A close below 88.7.

## c2ffa0009e (DOGE)
- **Read:** There was a peak at 130, then a steady decline to a base at 75–78. The breakout spiked to 110.9 and fell back to 88.1. Day −1 spiked to 104.7 but was rejected to close at 98.6. Two upper-wick rejections in 15 days make this choppy.
- **Supply:** There is supply at 100–130.
- **Weight: 0.5.**
- **Change my mind:** A close below 88.
- **Upgrade trigger:** Holding above 105 would raise the weight.

## 5b90d88b3d (XRP)
- **Read:** The base was drifting lower into 70. Then price exploded from 70 to 102 in three days. The 6× volume spike to 119.4 looks like a blow-off wick. Since then the highs have been lower, at 108.9, 104.2 and 100.6, and price is holding 92–104.
- **Weight: 0.5.** The blow-off rejection and the declining highs warrant caution.
- **Change my mind:** A close below 92 cuts the position. A close above 105 would raise it.

## 0e45ed534b (LINK)
- **Read:** The old peak was 82. After the crash the base made higher lows from 53. The breakout reached 93.7, consolidated at 82.4–91, and today broke out again to new window highs at 100, a +9.8% day on 1.7× volume.
- **Supply:** There is no overhead supply. The main risk is short-term overextension after a 10% day.
- **Weight: 0.7.**
- **Change my mind:** A close below 87.

## 593645e47e (ADA)
- **Read:** This is a downtrend from 130. The crash went to 66.5, and the base has been volatile with repeated failed spikes, at 89.5 and 94.8. The breakout spiked to 115.7 and was rejected, falling back to 84.8. Day −3 spiked to 100.9, day −2 faded to 94.6, and price is now 100.
- **Supply:** This window has a pattern of failed rallies, with supply at 105–125.
- **Weight: 0.4.**
- **Change my mind:** A close below 85 takes the position to flat. A close above 102 would raise it.

{"32e448fa11 (LTC)": 0.6, "26119be63b (ETH)": 0.8, "908513f860 (BTC)": 0.8, "1836e847bb (DOT)": 0.5, "614528b5ba (SOL)": 0.8, "beca5ffe67 (AVAX)": 0.6, "c2ffa0009e (DOGE)": 0.5, "5b90d88b3d (XRP)": 0.5, "0e45ed534b (LINK)": 0.7, "593645e47e (ADA)": 0.4}

## Entscheidung 2026-09-13

## Strategy

I stay long while the price holds above the support built after its most recent breakout, and I size the position down as volatility and blow-off behaviour rise. Blow-off behaviour means spikes with long upper wicks, very high volume, and lower highs. I cut toward flat when the recent action is a climax followed by a fast reversal, or when the price sits inside a longer-term downtrend. A clean, low-volatility consolidation above a breakout gets the largest weight.

All ten windows share a similar shape: an early decline, a crash around day -100, a base, a gap-up breakout around days -25 to -23, a consolidation, and a pullback in the last week to 100. The main differences are how orderly the consolidation is and how violent the latest spike was.

---

### 0fa8bdb6bb (LINK)
- **Read:**
  - The base held at 72–75 until day -34, and the breakout carried the price to 107 by day -23.
  - It then consolidated between 98 and 107 with an uptrend still intact.
  - On day -6 a spike to 122 failed, and the price gave back all of it to 100.
  - Support is the 97.4–98.3 cluster (lows on days -14, -11 and -10). Resistance is 107–109.
- **Weight: 0.5.** The trend is still up and the price sits just above support. The failed spike and wide daily ranges argue against a full position.
- **Change of mind:**
  - A close below 97 → cut to 0.
  - A close above 108 → raise to 0.8.

### 5371d96e4e (SOL)
- **Read:**
  - The base held at 74–77, and the breakout ran to 111 on day -17.
  - Since then the highs have stepped down (111, 108, 106.5) while the lows held at 98–99.
  - That makes a mild descending triangle, with the price now at its lower edge.
- **Weight: 0.45.** The trend is intact, but the series of lower highs is a warning.
- **Change of mind:**
  - Below 98 → 0.
  - Above 108 → 0.8.

### cd417e9432 (LTC)
- **Read:**
  - Before the crash the price traded at 100–110. It crashed to 77, recovered to 88, then faded to 82.
  - The breakout reached 103, pulled back to 88–89, and climbed again to a 110.6 high on day -6.
  - That high had a large upper wick, and the price has since slipped back to 97–100.
  - Support sits at 96 and then 88. The price is now back at its old pre-crash range.
- **Weight: 0.5.** The higher lows (88 → 96) are constructive. The volatility near the top and the rejection at the old range keep the position moderate.
- **Change of mind:**
  - Below 96 → 0.15.
  - Above 104 → 0.8.

### b60826a570 (DOGE)
- **Read:**
  - The bigger picture is a downtrend: the price peaked at 140 around day -122, crashed to 96, and drifted down to a base at 84–88.
  - The spike to 122 came on 3.7× volume and was fully retraced to 98.
  - The bounce to 115.5 also failed, so the highs keep falling (122 → 115 → 111).
  - Support is 98–100. Below that there is little structure until about 85.
- **Weight: 0.3.** Lower highs inside a longer downtrend, high volatility, and a large air pocket beneath the price.
- **Change of mind:**
  - Below 98 → 0.
  - Above 111 → 0.6.

### 6895d20337 (ETH)
- **Read:**
  - The base held at 75–77, and the gap-up came on day -25 at 2.8× volume.
  - Since then the price has held a tight 95–103 range for three weeks, with modest volatility.
  - The day -2 wick to 107.6 was rejected, but no damage was done to the range.
  - Support is 95–96. Resistance is 103, then 107.6.
- **Weight: 0.7.** This is the most orderly post-breakout consolidation of the set, and the risk to support is limited at about 4–5%.
- **Change of mind:**
  - Below 95 → 0.2.
  - Above 104 → 0.9.

### bebb054837 (DOT)
- **Read:**
  - This is a long downtrend: the price fell from 162 to 76.
  - A first spike to 103 faded back to 82.
  - Then came a parabolic climax: the price ran to 128.5 on about 4× volume over days -6 and -5.
  - It gave all of that back within four sessions (124.7 → 100), which is a classic blow-off reversal.
  - Support is weak, around 99.6, then 92 and 85.
- **Weight: 0.15.** Climax-and-collapse inside a long downtrend makes a deep drawdown the most likely risk.
- **Change of mind:**
  - Back above 113 → 0.5.
  - Below 96 → 0.

### f37eafd63a (XRP)
- **Read:**
  - The price had been in a slow decline from 113 to 74 before the event.
  - The breakout spike reached 126.7 on 6× volume and was immediately rejected.
  - Since then the price has consolidated between 98 and 110, with support at 97.7–99.
  - Over the last week the price has been fading from 106 to 100.
- **Weight: 0.4.** The new support is holding, but the price is pressing on it, volatility is high, and the climax volume suggests distribution.
- **Change of mind:**
  - Below 97.5 → 0.
  - Above 108 → 0.7.

### aef5d1378b (BTC)
- **Read:**
  - The base held at 82–84, and an orderly step up took the price to 100–106.
  - Daily ranges in the consolidation are small and volume is subdued.
  - The price sits at the bottom of the range, with lows of 99.0–99.5 on days -12, -3 and -2.
- **Weight: 0.6.** Volatility is low and the step-up came without a climax. Being at the edge of the range is the main risk.
- **Change of mind:**
  - Below 98.5 → 0.2.
  - Above 104 → 0.85.

### 219faa8590 (ADA)
- **Read:**
  - The market crashed to 73.
  - Three separate spikes have all failed: 98 → 77, 104 → 85, and 127 → 94.
  - The latest bounce reached 114 and has been fading. Ranges are very wide, roughly 5–10% a day.
  - Support is 94–98, and it is weak.
- **Weight: 0.25.** Repeated failed spikes and very high volatility give a poor drawdown profile.
- **Change of mind:**
  - Below 94 → 0.
  - Above 110 → 0.55.

### f3504dab4b (AVAX)
- **Read:**
  - The longer trend is down: the price fell from 140 and crashed to 78–85.
  - The breakout reached 114 and then consolidated between 96 and 104.
  - A retest to 112.5 on day -6 was rejected, and the price is back at 100.
  - Support is 96–97. Resistance is 108–112.
- **Weight: 0.4.** The lows are holding, but the highs keep falling inside the longer downtrend, and volatility is moderate to high.
- **Change of mind:**
  - Below 96 → 0.
  - Above 109 → 0.7.

{"0fa8bdb6bb (LINK)": 0.5, "5371d96e4e (SOL)": 0.45, "cd417e9432 (LTC)": 0.5, "b60826a570 (DOGE)": 0.3, "6895d20337 (ETH)": 0.7, "bebb054837 (DOT)": 0.15, "f37eafd63a (XRP)": 0.4, "aef5d1378b (BTC)": 0.6, "219faa8590 (ADA)": 0.25, "f3504dab4b (AVAX)": 0.4}

## Entscheidung 2026-09-20

**Strategy:** Stay long when price holds a rising structure of higher lows near the top of its 180-day range and volatility is contained. Cut exposure when price sits in a wide, choppy range below earlier highs, or after a vertical move on extreme volume, because those are the setups that tend to produce deep giveback. The size of the weight follows how close the invalidation level is and how stable the trend is.

## 818b45bc5d (DOGE)
- **Trend:** The 180-day peak was ~135 (day -129). Price crashed to ~89 (day -107), then ground down to a ~78–80 base.
- **Recent action:** A violent breakout (days -32 to -29) spiked to 115.5 and failed. Since then price has chopped between 89.7 and ~105. It is now at 100, mid-range.
- **Structure:** The range is wide and volatile, and price is still well below the old highs. There is no clean trend.
- **Weight:** 0.5. The range floor is holding, but the risk of a deep move is moderate.
- **Change of mind:** A close above 105 raises the weight. A break below 89.5 cuts it.

## 471a2d0fbc (LINK)
- **Trend:** Price ran from a ~56 low (day -87) through a breakout to 100. It has made higher lows: 84.8 on day -4, after 87–88 earlier.
- **Levels:** The 180-day high is 109.3 (day -13). Price is near the top of the full window and has recovered quickly from the day -5 dip.
- **Weight:** 0.7. The trend is intact, and the higher-low structure supports holding.
- **Change of mind:** Below 84.5 the structure breaks. Above 109.5 I would add.

## 0262d8f2e8 (DOT)
- **Trend:** This is a long downtrend from 123 to ~64 (day -33).
- **Recent action:** Price had a two-stage spike to 113 (day -12) on 4x volume, then a sharp reversal to 82.3. It has now rebounded to 100, on very large daily ranges with elevated volume.
- **Structure:** Highly unstable, and still below the levels where the window started.
- **Weight:** 0.45. The volatility makes a deep drawdown likely in either direction.
- **Change of mind:** A hold above 103.5 and then 113 would raise the weight. A loss of 88 cuts it toward 0.2.

## b0f1cfef19 (BTC)
- **Trend:** The prior high was 102.1 (day -137). Price crashed to 72.8, built a calm base at 77–80, then broke out cleanly to ~97–101.
- **Structure:** A tight consolidation between 92.4 and 101.4 with low volatility. Price is now 100, pressing the top of the range and near its 180-day high.
- **Weight:** 0.85. This is the cleanest setup in the set: a low-volatility trend with a nearby stop.
- **Change of mind:** A break below 92.3 cuts the weight.

## a79597e270 (ADA)
- **Trend:** The high was 126.7 (day -133). Price crashed hard to 65 and then traded in a choppy recovery.
- **Recent action:** A spike to 113.4 (day -29) failed. Since then price has ranged between 83.5 and 103 with wide bars, and it is now 100.
- **Structure:** Still below the old highs, volatile, and repeated spike-and-fail behaviour.
- **Weight:** 0.5.
- **Change of mind:** Above 104 I would add. Below 83.5 I would cut.

## 5242b38031 (AVAX)
- **Trend:** Price based between 50 and 60 for months.
- **Recent action:** It then went near-vertical, from 67 to 100 in two days: +23% then +12%, on 3.9x and 6.1x volume. Day 0 alone ranged from 83.4 to 101.4.
- **Structure:** This is a climactic move far above all support. The nearest structure is ~72, so a retrace to it would be about -28%.
- **Weight:** 0.3. The trend is strong, but the drawdown risk is extreme.
- **Change of mind:** A calm hold above 90 for several days would raise the weight. A break below 83 means flat.

## d0a8c1d302 (XRP)
- **Trend:** Price started the window at ~100, fell to ~70, then broke out to a 120.5 spike (day -29).
- **Structure:** Since then it has traded in a wide 88–110 range with violent bars. The day -6 to -5 reversal went from 106 to 89.7. Price is now 100, mid-range, with volume still elevated.
- **Weight:** 0.45.
- **Change of mind:** Above 106 I would add. Below 88.4 I would cut.

## eef68a53a2 (ETH)
- **Trend:** Price broke out of a long, quiet ~71–72 base on day -32. It has since held a steady 89–100 range, now at 100, which is its 180-day high.
- **Structure:** Volatility is low and the lows are firm (89.2, 89.1).
- **Weight:** 0.8.
- **Change of mind:** Below 89 I would cut. A confirmed close above 101 keeps the weight full.

## 051fa3f95c (LTC)
- **Trend:** The prior high was 103.2 (day -133). Price crashed to 66.9, recovered steadily, and broke out to 94.
- **Structure:** Higher lows at 81.7 and then 85.5. The recent high is 101.2, with price now at 100, near the top of the window.
- **Weight:** 0.7.
- **Change of mind:** Below 85.5 I would cut. Above 103.5 I would add.

## 7a90c321bb (SOL)
- **Trend:** Price rose steadily from a 55 low through a breakout. The highs run 99.5 (day -24) to 102.8 (day -2), and price is now 100, at its 180-day high.
- **Structure:** Higher lows at 86.2 and 87.6. The trend is orderly, with moderate volatility.
- **Weight:** 0.75.
- **Change of mind:** Below 86 I would cut. Above 103 I would add.

{"818b45bc5d (DOGE)": 0.5, "471a2d0fbc (LINK)": 0.7, "0262d8f2e8 (DOT)": 0.45, "b0f1cfef19 (BTC)": 0.85, "a79597e270 (ADA)": 0.5, "5242b38031 (AVAX)": 0.3, "d0a8c1d302 (XRP)": 0.45, "eef68a53a2 (ETH)": 0.8, "051fa3f95c (LTC)": 0.7, "7a90c321bb (SOL)": 0.75}

## Entscheidung 2026-09-27

**Strategy:** I hold more exposure when price is at or above its prior 180-day highs, is building higher lows, and the recent daily ranges are calm. I cut exposure when the rally is a recent near-vertical spike, price sits below an old supply zone, or wide daily swings mean a quick 15–25% retrace is plausible. Each weight scales with how far below today's price the nearest solid support sits and how volatile the approach to it has been.

---

### e4fb7660aa (DOT)
- **Read:** Price topped around 109 (day -140), crashed to 72, then bled to about 57 (day -40). Since then it has rallied roughly 70% in 40 days. The swings have been violent: up to 98.3 on day -19, down to 74.5 on day -12, and back to 100 on heavy volume. Higher lows sit at 74.5 and 86.
- **Price vs. old supply:** It is just reaching the 100–109 supply zone, with daily ranges of 5–8%.
- **Weight:** 0.45. The trend is up, but volatility and overhead supply make a deep pullback quite possible.
- **Change my mind:** A close below 86 means cut to 0. A close above 105 means add.

### 0a31cdef07 (DOGE)
- **Read:** Price peaked at 122 (day -136), crashed to 80, and based near 72 for about two months. It then rallied to 100.
- **Recent action:** The spike on day -6 to 105 was rejected down to 94, then partly recovered. Higher lows sit at 81, 84 and 94.
- **Price vs. old supply:** It is still below the old 105–122 supply zone.
- **Weight:** 0.5. The structure is improving but the price is capped overhead and volatile.
- **Change my mind:** Below 94 means cut. A close above 106 means add.

### 602abc152f (LTC)
- **Read:** The prior high was 85 (day -140), followed by a crash to 57 and a base near 62. The rally from day -39 broke above 85.
- **Breakout:** On day -3 it gapped from 87 to 101 on 6.7x volume, and it has held 99–102 for three days.
- **Weight:** 0.7. It is clearly at new highs with an intact trend. The gap is extended, so the lower edge of the gap (about 87) is a real risk.
- **Change my mind:** A close below 96 means reduce. Below 86 means go flat.

### 5570536059 (BTC)
- **Read:** The prior high was 98 (day -144), followed by a crash to 70 and a base near 75. It then rallied to 93 and consolidated between 89 and 96 for a month.
- **Breakout:** On day -6 it broke out to 102, and it is now holding 99.6–100.8 on low volume with tight ranges.
- **Weight:** 0.85. It is a clean breakout above the 98 prior high, with low volatility and nearby support.
- **Change my mind:** A close below 97 means reduce. Below 89 means go flat.

### 218dac44cb (LINK)
- **Read:** The prior high was 77 (day -140), followed by a crash to 50 and a base at 52–62. It has been in a steady staircase higher since day -47.
- **New highs:** Price is well above 77. Higher lows sit at 75.7, 86 and 99.
- **Weight:** 0.75. The trend structure is strong, though the move is extended.
- **Change my mind:** Below 94 means reduce. Below 86 means go flat.

### a3cea178bf (SOL)
- **Read:** The prior high was 80.7 (day -139), followed by a crash to 49 and a base near 60. It has rallied since day -39 to new highs, with a pattern of higher lows at 78.5 and 92.2.
- **Volatility:** Moderate, with daily ranges of 3–4%.
- **Weight:** 0.75.
- **Change my mind:** Below 92 means cut sharply. Above 103 means add.

### 28e448e27b (ETH)
- **Read:** The prior high was 91.7, followed by a crash to 56 and a recovery to 71. A big gap on day -39 lifted it to 84–94, and it then spent about 30 days building a base between 88 and 95.
- **Breakout:** On day -6 it broke out to 103.
- **Holding:** It is now quietly holding at 100, with very low volume (0.30 on day -1) and tight ranges.
- **Weight:** 0.8. This is a mature base breakout above the old high, and volatility is calm.
- **Change my mind:** Below 96.7 means reduce. Below 88 means go flat.

### f0607f1258 (ADA)
- **Read:** The prior high was 113 (day -140), followed by a crash to 54. Since then it has been very choppy: spikes to 78, 83 and 101 have each faded 20–30%.
- **Price vs. old supply:** It is at 100, under the 104–113 supply zone, with wide daily ranges of 5–10%.
- **Weight:** 0.45. A history of failed spikes and high volatility means high drawdown risk.
- **Change my mind:** Below 91.5 means go flat. A close above 105 means add.

### b905d84a53 (XRP)
- **Read:** The prior high was about 102 (day -136), followed by a crash to 65 and a base near 66.
- **Recent action:** A parabolic move on days -38 to -36 reached a 112 wick, followed by a month-long range between 83 and 100. It has now spiked again to 103–109, but each push leaves long upper wicks on 3x volume.
- **Weight:** 0.45. Price is at the top of a volatile range with repeated rejection near 104–112.
- **Change my mind:** Below 95.7 means cut toward 0. A close above 109 means add.

### d00be39141 (AVAX)
- **Read:** The prior high was 96 (day -140), followed by a crash to 52 and a long base at 56–62. The first rally faded back to 66.
- **Spike:** On days -8 and -7 the price exploded from 70 to 104, a 48% gain in two days on 5.7x volume.
- **Since the spike:** It has chopped between 91 and 104. The nearest structural support is around 70, roughly 30% below.
- **Weight:** 0.3. Gap and spike risk is high, and there is no base under the current price.
- **Change my mind:** Holding above 92 for another week, or breaking above 105, would justify adding. Below 91 means go flat.

---

{"e4fb7660aa (DOT)": 0.45, "0a31cdef07 (DOGE)": 0.5, "602abc152f (LTC)": 0.7, "5570536059 (BTC)": 0.85, "218dac44cb (LINK)": 0.75, "a3cea178bf (SOL)": 0.75, "28e448e27b (ETH)": 0.8, "f0607f1258 (ADA)": 0.45, "b905d84a53 (XRP)": 0.45, "d00be39141 (AVAX)": 0.3}
