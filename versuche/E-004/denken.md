# E-004: was die KI gedacht hat (Set A)

Volle Antwort des Deciders pro Entscheidungswoche, unverändert. Er sah weder Datum noch Coin-Namen; die Namen in Klammern sind erst danach eingesetzt. Gesendeter Prompt und Daten: runs/<set>/<woche>/requests.json.

## Entscheidung 2026-07-05

**1. Strategy**

All ten markets share one path: a sell-off into a crash low around day -150, a recovery into highs around day -60 to -50, a second break from day -33 to -30, a retest low between day -16 and day -5, and a 3–4 day bounce back to 100. I rank them by the quality of the retest. That means higher lows after day -30, whether price has reclaimed the day -20 swing high, and volume on the bounce. Markets that held their retest and broke above the post-crash range get the most weight. Markets that made clean lower lows and lower highs get the least.

**2. Windows**

**2ae1674212 (BTC)**
- **Read:** Recovered from 98.8 to 129 (day -56), then broke down. The day -30 low of 92.9 was undercut at 90.8 (day -4), a marginal lower low.
- **Now:** The bounce to 100 came on fading volume (0.46). Resistance is 104–105.7, the day -20 high.
- **Weight:** 0.3. The trend is still down and the bounce has no thrust.
- **Change my mind:** above 106 raises it; below 90.8 cuts it to zero.

**2225508141 (DOGE)**
- **Read:** The deepest giveback: from 152 (day -52) down to 89.3 (day -5), a clear lower low under the day -30 low of 101.5.
- **Now:** The bounce to 101.9 is on below-average volume. Overhead resistance sits at 110–114.
- **Weight:** 0.2. This is the weakest structure.
- **Change my mind:** above 114 raises it; below 89 exits.

**d9ae2edc29 (LTC)**
- **Read:** Bottomed at 85.7 (day -10), made a higher low at 89.8 (day -4), and is now pressing the 101 ceiling (day -20 and day -14 highs). Volume is steady at about 0.8.
- **Weight:** 0.45. The structure is improving but has not broken out yet.
- **Change my mind:** a close above 101.5 raises it; below 89.8 cuts it.

**b1a691bee1 (ADA)**
- **Read:** Had the worst crash, from 152 to 78.4 and then a 72.9 low (day -10). Then came a violent four-day reversal from 76 to 105.5 on 1.8–2.2x volume, clearing the 100.3 range top (day -20).
- **Now:** Day 0 held 97.7.
- **Weight:** 0.5. This is the strongest short-term momentum, discounted because it is a potential squeeze inside a long-term downtrend with heavy overhead at 110–125.
- **Change my mind:** a hold above 97 confirms it; a close below 92 means the breakout failed.

**0b7037d84a (SOL)**
- **Read:** The cleanest base. Lows ran 73.7 (day -29), then 78.5 (day -10), then 88.1 (day -5), a sequence of higher lows.
- **Now:** Price broke the 93.3 day -20 high and has held 98–103 for three days. It now sits at its old day -150 to day -90 range of 95–105.
- **Weight:** 0.6. This is the strongest structure.
- **Change my mind:** below 94 cuts it; above 103 adds to it.

**3b8255ec36 (ETH)**
- **Read:** Double bottom at 84.3 (day -29) and 84.7 (day -9). It rallied to 101.3, but the neckline at 103.6 (day -20) is not yet cleared. Volume picked up on day 0 (0.99).
- **Weight:** 0.4.
- **Change my mind:** above 103.6 raises it; below 94 cuts it.

**5b55cd059b (AVAX)**
- **Read:** Held up best through day -50 to day -34, in the 130s. A capitulation low of 82.0 came on day -16 with 3x volume. Since then the lows have risen: 86.0, 90.6, 92.2, 98.0.
- **Now:** The day -1 high of 102.8 marginally clears the 102.2 day -20 high.
- **Weight:** 0.5.
- **Change my mind:** below 92 cuts it; above 103 confirms it.

**ebc38d3ac0 (LINK)**
- **Read:** Double bottom at 86.8 and 86.9, and price has bounced to 101.4. The neckline is 106.7 (day -20), and the bounce volume is very thin (0.34–0.38).
- **Weight:** 0.35. The volume does not confirm the move.
- **Change my mind:** above 107 raises it; below 88 cuts it.

**4ea4bffb88 (XRP)**
- **Read:** A marginal lower low at 87.2 (day -10) versus 90.7 (day -29), then a bounce to 102.3. Resistance is 107 and 111.8 (the day -20 spike).
- **Weight:** 0.35.
- **Change my mind:** above 107 raises it; below 88 cuts it.

**0f92a5bf9c (DOT)**
- **Read:** A persistent pattern of lower highs: 163 (day -53), then 118.8 (day -20), then 111 (day -13). There is also a lower low at 90.2 (day -7) versus 100.3 (day -29).
- **Now:** It is bouncing into 101–102, which is overhead supply.
- **Weight:** 0.25.
- **Change my mind:** above 112 raises it; below 90 exits.

**3. Weights**

{"2ae1674212 (BTC)": 0.3, "2225508141 (DOGE)": 0.2, "d9ae2edc29 (LTC)": 0.45, "b1a691bee1 (ADA)": 0.5, "0b7037d84a (SOL)": 0.6, "3b8255ec36 (ETH)": 0.4, "5b55cd059b (AVAX)": 0.5, "ebc38d3ac0 (LINK)": 0.35, "4ea4bffb88 (XRP)": 0.35, "0f92a5bf9c (DOT)": 0.25}

## Entscheidung 2026-07-12

**Strategy:** Every window shows the same bear market: two crash legs (around -162/-157 and -40/-37) and a weak rebound to about 100. I treat the regime as hostile and keep all weights modest. Within that, I favour markets with the smallest drawdown from their day -60 to -63 highs and with higher or equal lows since the -37 crash. I cut markets that made lower lows or failed rallies.

## d25be26213 (ETH)
- **Read:** The day -63 high was 131.2, then the market crashed to 83.3 (day -36). Price re-tested 83.7 at day -17, a double bottom.
- **Recovery:** It has climbed back to 100, but the band from 101 to 102 keeps capping it.
- **Drawdown:** About 24% from the day -63 high, which ranks among the milder ones.
- **Weight 0.3:** The base is intact, but price is still stuck under resistance.
- **Change my mind:** Below 94.5 I go to 0. A close above 102.5 would raise the weight.

## 368f8c4a53 (SOL)
- **Read:** The market fell from 127.9 to 78.2 at day -36. The day -17 low of 83.3 was a clear higher low.
- **Recovery:** It had the strongest rebound in the set, reaching 109.2 at day -8. It is now pulling back to 100 on light volume.
- **Drawdown:** About 22%, the best structure in the group.
- **Weight 0.45.**
- **Change my mind:** Below 98 I cut. Below 90 I go to 0.

## 5c003eb513 (DOT)
- **Read:** A persistent downtrend: about 170 at day -60, 104.7 at day -36, then a lower low of 94.2 at day -14.
- **Recovery:** The bounce is capped around 106.
- **Drawdown:** About 41%, with lower lows.
- **Weight 0.05:** It is among the weakest.
- **Change my mind:** Below 96 I go to 0. Only a close above 107 would justify more.

## 3cd150bc63 (XRP)
- **Read:** The market fell from 142.7 at day -59 to 96.7, then made a lower low at 92.9 on day -16.
- **Recovery:** It bounced to 109.1 and has faded back to 100.
- **Drawdown:** About 30%.
- **Weight 0.15:** The structure is weak.
- **Change my mind:** Below 98.5 I go to 0. Above 109 I would add.

## 6661f4ed29 (LINK)
- **Read:** The market fell from 135.9 to 87.5 at day -36, then re-tested 87.7, a double bottom.
- **Recovery:** Price sits at 100, just under the 102.2 cap.
- **Drawdown:** About 26%.
- **Weight 0.3.**
- **Change my mind:** Below 94 I go to 0. Above 102.5 I would add.

## f05a852c8f (LTC)
- **Read:** The market fell from 137.7 to 92.1 at day -36, then made a marginally lower low at 89.3.
- **Recovery:** It reached 104.9 at day -7 and is holding around 99 to 100 with steady closes.
- **Drawdown:** About 27%.
- **Weight 0.25.**
- **Change my mind:** Below 98 I cut. Below 95 I go to 0.

## b3be6bed8d (DOGE)
- **Read:** The market had a late rally to 163 at day -59, then crashed to 106.8. After that it made lower lows at 98.3 and 95.6.
- **Recovery:** It bounced to 109.2 and has faded back to 100.
- **Drawdown:** About 39%, a heavy reversal.
- **Weight 0.1.**
- **Change my mind:** Below 97.5 I go to 0. Above 109 I would add.

## 309d6607b2 (AVAX)
- **Read:** The market fell from 163.7 to 97.1, then made a lower low on a capitulation at 88.7 (day -23).
- **Recovery:** It rebounded to 111.1, but day 0 dropped from 102 to a 98 intraday low on rising volume.
- **Drawdown:** About 39%.
- **Weight 0.1.**
- **Change my mind:** Below 98 I go to 0. Above 111 I would add.

## a3e99866f0 (ADA)
- **Read:** This had the largest drawdown, from 178 to 85.3. A blow-off spike reached 123.4 at day -8, and price has since fully retraced to 100.
- **Drawdown:** About 44%, and the spike was a failed breakout.
- **Weight 0.05.**
- **Change my mind:** Below 99 I go to 0. A recovery above 108 would change the picture.

## 3436b92453 (BTC)
- **Read:** This is the least damaged market over the whole window (152 to 100). It is the least volatile.
- **Recovery:** It made a double bottom at 92.7 and 91.1, and price is consolidating tightly at about 100. The ceiling is 101.4.
- **Drawdown:** About 23% from 129.3.
- **Weight 0.4.**
- **Change my mind:** Below 96.5 I cut. Below 91 I go to 0. Above 101.5 I would add.

{"d25be26213 (ETH)": 0.3, "368f8c4a53 (SOL)": 0.45, "5c003eb513 (DOT)": 0.05, "3cd150bc63 (XRP)": 0.15, "6661f4ed29 (LINK)": 0.3, "f05a852c8f (LTC)": 0.25, "b3be6bed8d (DOGE)": 0.1, "309d6607b2 (AVAX)": 0.1, "a3e99866f0 (ADA)": 0.05, "3436b92453 (BTC)": 0.4}

## Entscheidung 2026-07-19

**1. Strategy**

Every window shares the same two crashes, one around day -164 and one around day -44. So the comparison is relative strength through the second one. I rank by four things: how much of the drop from the day -48 level each market has recovered, whether its lows are rising, whether it is breaking above its post-crash resistance, and its momentum over the last 20 days. Weight goes to markets that have nearly repaired the crash and are making higher highs. Markets with persistent lower highs, still far below where they were before the crash, get close to zero.

**2. Windows**

### fb1009b284 (LTC)
- **Read:** This is the strongest window. Before the crash it closed at 107.9 (day -48), so the gap is only about 7%. The lows are 83.5 on days -25/-24, and price has climbed steadily since.
- **Breakout:** Yesterday it closed through the 98 resistance (highs of 98.3 on day -34 and 98.0 on day -14), reaching 101.7 on rising volume. That is the highest close since the crash.
- **Weight:** 1.0. It is the clear relative-strength leader with a fresh breakout.
- **Invalidation:** a close below 92.

### e4f8f89261 (ETH)
- **Read:** A double bottom at about 80.5 (days -43 and -23), with the neckline at 98.8 broken on day -4 (high 104.0). It is about 7% below the day -48 close of 107.2. Higher lows since: 93.5, then 96.3.
- **Weight:** 0.8. Clean base and breakout, slightly less momentum than fb10.
- **Invalidation:** below 93.

### 5908285004 (SOL)
- **Read:** Rising lows at 78.7, 83.8 and 96.1. The rally reached 110 on day -15 and has pulled back to 100. It is about 6% below the day -48 close of 106.4, the best of the group on that measure. The pullback is orderly, on low volume.
- **Weight:** 0.7.
- **Invalidation:** below 96.

### 66ce2ed9ac (LINK)
- **Read:** Lows of about 83.5 on days -43 and -24. The day -4 high of 103.0 is above the day -34 high of 102.6. It is about 7% below the day -48 close of 108.0. Volume is very thin.
- **Weight:** 0.7. The structure is similar to e4f8 but with less conviction.
- **Invalidation:** below 95.

### 1c8b23f419 (BTC)
- **Read:** A shallower drop: the low was 89.8 and the gap to the day -48 close of 110.3 is about 9%. Price is stuck under 101.4–101.7, the double top from days -35 and -4. The range is 96–101.
- **Weight:** 0.5. Resilient, but not yet breaking out.
- **Invalidation:** below 95.5. A close above 102 would raise the weight.

### 43b31c5edf (XRP)
- **Read:** Lower highs at 117.8, 107.9 and 103.0. It is about 15% below the day -48 close of 118.2. The low was 92.2.
- **Weight:** 0.3. It sits mid-pack with a deteriorating series of highs.
- **Invalidation:** below 96. A close above 104 would raise the weight.

### 95d869a083 (ADA)
- **Read:** A spike to 120 on day -15 faded completely back to 100. It is about 28% below the day -48 close of 139. The lows are rising (83, 93.4, 94.9), but the failed rally caps it.
- **Weight:** 0.2.
- **Invalidation:** below 94. A move above 105 would raise the weight.

### bf92963846 (AVAX)
- **Read:** It made a lower low of 87.9 on day -30, below the first post-crash low. It is about 28% below the day -48 close of 138, and has gone sideways between 97 and 110 with a lower high.
- **Weight:** 0.1.
- **Invalidation:** above 108 would turn me constructive. Below 97 confirms weakness.

### 5a337aaf38 (DOGE)
- **Read:** A steady cascade of lower highs: 163.8, 127.7, 109.6, 104.1. It is about 28% below the day -48 close of 139.6. Volume is drying up near the lows.
- **Weight:** 0.1.
- **Invalidation:** above 105 would turn me constructive.

### ea8849b3db (DOT)
- **Read:** The weakest window. It is about 29% below the day -48 close of 141.3, and the highs keep falling: 127.7, 110.7, 109.1. Today it slipped from 102.3 to 100 on above-average volume.
- **Weight:** 0.0.
- **Invalidation:** above 109 would turn me constructive.

{"fb1009b284 (LTC)": 1.0, "e4f8f89261 (ETH)": 0.8, "5908285004 (SOL)": 0.7, "66ce2ed9ac (LINK)": 0.7, "1c8b23f419 (BTC)": 0.5, "43b31c5edf (XRP)": 0.3, "95d869a083 (ADA)": 0.2, "bf92963846 (AVAX)": 0.1, "5a337aaf38 (DOGE)": 0.1, "ea8849b3db (DOT)": 0.0}

## Entscheidung 2026-07-26

**1. Strategy**

All ten markets move together: a crash near day -171, a second leg down at day -51, a retest near day -30, and now a rebound to 100. Because the common factor dominates, I rank them by relative strength. I favour markets that are making higher lows since the day -30 retest and are pushing through their recent range highs, and that fell less from their day -77 peaks. Markets with lower highs, deep drawdowns, or failed spikes get small weights. Each window has an invalidation level just under its most recent higher low.

**2. Per-window analysis**

**8469f93de8 (SOL)**
- **Read:** The day -77 peak was 126.8. Price crashed to 78.3 at day -50, rebounded to 109.4 at day -22, then made lower highs (107.3, then 102.8). It is now chopping between 95.6 and 103. It closed at 100, the top of the range, on low volume.
- **Structure:** Neutral to soft. Resistance is 103 and then 109. Support is 95.6.
- **Weight:** 0.4. It sits mid-pack, with no higher-low sequence.
- **Change my mind:** A close below 95.5 means cut. A close above 103.5 means add.

**a811fdf28c (LINK)**
- **Read:** The day -77 peak was 123. It made a double bottom at 79.3 (day -50) and 79.4 (day -31). Since then it has made clean higher lows: 80.2, then 85.2, 88.3, 90.7 and 94.0. Day 0 closed at the high (100.0, high 100.2), clearing the 99.3 resistance.
- **Structure:** Constructive base and breakout. Support is 94 and then 90.7.
- **Weight:** 0.8. It has one of the best higher-low structures in the group.
- **Change my mind:** A close below 93.5.

**7dd32144fc (ETH)**
- **Read:** The peak was 126 at day -100. It double-bottomed at 77.0 and 77.4. Higher lows followed at 79.3, 87.7, 92.2 and 94.5. Day 0 was a strong close at 100 after a 100.6 high, testing the 100.1 swing high.
- **Structure:** This is the cleanest uptrend off the lows. Support is 94.5.
- **Weight:** 0.8.
- **Change my mind:** A close below 94.

**f6c1127bfe (XRP)**
- **Read:** The peak was 139 at day -73. It made a lower low at 90.7 (day -30) than at day -50 (94.3). It rallied to 106.4, then made lower highs (104.6). It has ranged between 94.6 and 104.6 for three weeks and closed at 100 on very low volume.
- **Structure:** Sideways with a downward tilt.
- **Weight:** 0.4.
- **Change my mind:** A close below 96 means cut. A close above 104.7 means add.

**f0eaa51279 (AVAX)**
- **Read:** The peak was 155.5 at day -77, so it has fallen about 45%. The low was 84.2 at day -37. It has stayed in a 91–105 range since then. A spike day at day -1 (92.4 to 101.5 on 1.53 volume) came right after a fresh dip to 91.0.
- **Structure:** A volatile range with no trend, and resistance between 103 and 105.
- **Weight:** 0.25.
- **Change my mind:** A close below 92 means go flat. A close above 105.5 means add.

**adda73ec39 (BTC)**
- **Read:** It had the shallowest drawdown: from 126.7 at day -81 to 88.4 at day -25. Since then it has made steady higher lows at 93.7, 94.1, 94.5, 95.6, 96.5 and 97.5. The swing high is 102.4 at day -5, and it closed at 100.
- **Structure:** A tight, orderly uptrend with low volatility.
- **Weight:** 0.6. It is solid, but has not yet cleared 102.4.
- **Change my mind:** A close below 97 means cut. A close above 102.5 means add.

**a415f1f0d1 (DOGE)**
- **Read:** The peak was 161.6 at day -73, a roughly 40% drawdown. The low was 94.7 at day -26. Highs have been lower (108.2, then 103, then 102.7). There was a sharp dip to 92.9 at day -2 before a recovery to 100.
- **Structure:** A weak range with a downward bias.
- **Weight:** 0.2.
- **Change my mind:** A close below 93 means go flat. A close above 103 means re-evaluate upward.

**5ecdb61e89 (ADA)**
- **Read:** The peak was 173.9 at day -77. It crashed to 83.3 at day -31. A blow-off spike to 120.5 at day -22 fully failed. Highs have been lower since (108.9 at day -4), and it closed at 100 on very low volume.
- **Structure:** A failed breakout and distribution.
- **Weight:** 0.25.
- **Change my mind:** A close below 97 means go flat. A close above 109 means add.

**78399f1bd3 (LTC)**
- **Read:** The peak was 126.7 at day -77, and the low was 82.1 at day -31. It has made a persistent series of higher lows: 86.0, 90.2, 89.7, 92.2 and 95.6. Day 0 broke out to a 100.9 high on above-average relative volume (0.82), clearing the 100.1 swing highs.
- **Structure:** A trend resuming, supported by volume.
- **Weight:** 0.75.
- **Change my mind:** A close below 95.5.

**19a367a248 (DOT)**
- **Read:** This is the longest downtrend in the group. It went from 200 at days -132/-151, to 171 at day -77, to a 96.0 low at day -28. It has made lower highs since (109.7, 108.1, 105.6, 105.0) and ranged between 95 and 106 for three weeks.
- **Structure:** A persistent downtrend that is only pausing.
- **Weight:** 0.15. It is the weakest in the group.
- **Change my mind:** A close below 95 means go flat. A close above 108.5 means add.

**3. Weights**

{"8469f93de8 (SOL)": 0.4, "a811fdf28c (LINK)": 0.8, "7dd32144fc (ETH)": 0.8, "f6c1127bfe (XRP)": 0.4, "f0eaa51279 (AVAX)": 0.25, "adda73ec39 (BTC)": 0.6, "a415f1f0d1 (DOGE)": 0.2, "5ecdb61e89 (ADA)": 0.25, "78399f1bd3 (LTC)": 0.75, "19a367a248 (DOT)": 0.15}

## Entscheidung 2026-08-02

**Strategy:** Every window shows the same shock at day −61 to −58, so I rank each one by how it has behaved since that low. I look at whether its lows are rising, how much of the pre-crash level it has recovered, and where day 0 sits inside the last month's range. Rising lows with closes in the upper half of the range get the most weight. Lower highs, or new lows made after the crash, get the least.

## a25140bab9 (DOGE)
- **Read:** Pre-crash the market was around 142. It fell to 111.6 at the crash and kept bleeding to 98.2 at day −33. For the last month it has drifted sideways at 96–106 on very low volume. There is no recovery at all, and it sits about 30% below its pre-shock level. Support is 95.6; resistance is 106.5–110.
- **Weight: 0.10.** It is the weakest of the group, with a base but no demand behind it.
- **Change my mind:** a close above 107 would raise the weight; a close below 95 would take it to flat.

## 9164092420 (ETH)
- **Read:** Pre-crash it was around 107. It bottomed at 79.9 twice (days −57 and −37). Since then the lows have stepped up: 82.2, then 92.8, then 96.6. Highs have reached 103.2 and 105.1, so it has recovered almost all of the shock. The structure is a clean uptrend. Support is 96.6; resistance is 105.
- **Weight: 0.65.** It shows the strongest relative recovery.
- **Change my mind:** a close below 96 would cut the weight; a close above 105 would add to it.

## ec0cb70df5 (BTC)
- **Read:** Pre-crash it was around 116. It made a low of 93 at the crash and 90.9 at day −32. Since then lows have risen to 97.3 and 98.0, while the market has held a tight 98–105 range. It has recovered only partially, but the range is orderly. Support is 98; resistance is 105.3.
- **Weight: 0.45.**
- **Change my mind:** a close below 97 would cut the weight.

## d2c3dc339a (AVAX)
- **Read:** Pre-crash it was around 136. It hit 95 at the crash, then made a lower low of 86.7 at day −44. Since then it has chopped between 92 and 108. On day 0 it reversed from 92.2 to 100 on firm volume. It has recovered little of the shock and its swing highs are lower: 108.6, then 104.5. Support is 92.2; resistance is 104.5.
- **Weight: 0.30.** The day-0 reversal helps, but the overall structure is weak.
- **Change my mind:** a close above 105 would raise the weight; a close below 92 would take it to flat.

## f964e74018 (DOT)
- **Read:** Pre-crash it was around 148. It fell to 110.6 at the crash and kept falling to 99.5. It then made a series of lower highs (131, 113.6, 108.8, 104.1) and broke to 93 at day −6. It has bounced to 100, but the trend is still down. Support is 93; resistance is 104.
- **Weight: 0.10.**
- **Change my mind:** a close above 105 would raise the weight; a close below 93 would take it to flat.

## 66ade06dfc (SOL)
- **Read:** Pre-crash it was around 112. It bottomed at 81.7 at the crash, then rallied to 114 at day −29, fully recovering the shock. It has since pulled back to 100, and its low of 95.9 sits well above the earlier 87. This looks like a corrective pullback inside a recovery. Support is 96; resistance is 107–114.
- **Weight: 0.50.**
- **Change my mind:** a close below 95.5 would cut the weight.

## 5fb36862cd (LINK)
- **Read:** Pre-crash it was around 108. Lows went from 83.4 (crash) to 83.6, 89.7, 93.0 and then 94.1. Highs reached 103 and then 106.3, so this is a steady uptrend with lows rising and most of the shock recovered. Support is 94; resistance is 106.3.
- **Weight: 0.55.**
- **Change my mind:** a close below 94 would cut the weight; a close above 106.5 would add to it.

## 9f9b1ccd58 (LTC)
- **Read:** Pre-crash it was around 116. It made a low of 90.7 at the crash and 87.9 at day −38. Since then lows have risen to 96.0 and 97.6. It broke out to 107–108 on rising volume around days −15 to −13 and is now pulling back to 100. Support is 97.6; resistance is 108.
- **Weight: 0.55.**
- **Change my mind:** a close below 97 would cut the weight.

## bdcbc5387a (XRP)
- **Read:** Pre-crash it was around 122. It made a low of 96.6 at the crash and 92.9 at day −37. It spiked to 109 and since then has ranged between 96 and 107 with lower highs. Day 0 recovered to the middle of that range. Support is 96.1; resistance is 107.
- **Weight: 0.35.**
- **Change my mind:** a close below 96 would take it to near flat.

## d44df14b42 (ADA)
- **Read:** Pre-crash it was around 124. This was the deepest fall: 78.4 at the crash, then a new low of 72.9 at day −38. It spiked to 105.5, faded back to 81, and has now rallied 22% in six days. Day 0 closed at 100, near its high, on 1.73× volume and above the 95 range top. The short-term momentum is strong, but the market is volatile and still far below its pre-crash level. Support is 92 and then 85; resistance is 105.5.
- **Weight: 0.40.**
- **Change my mind:** a close back below 92 would cut the weight; a close above 105.5 would add to it.

{"a25140bab9 (DOGE)": 0.10, "9164092420 (ETH)": 0.65, "ec0cb70df5 (BTC)": 0.45, "d2c3dc339a (AVAX)": 0.30, "f964e74018 (DOT)": 0.10, "66ade06dfc (SOL)": 0.50, "5fb36862cd (LINK)": 0.55, "9f9b1ccd58 (LTC)": 0.55, "bdcbc5387a (XRP)": 0.35, "d44df14b42 (ADA)": 0.40}

## Entscheidung 2026-08-09

## Strategy
All ten markets fell together in the same sell-off around day -68 to -65. I rank them by how well they have recovered since then. I look at three things: the distance from the post-crash low, whether the lows are getting higher, and where price sits within the recent range. Markets that keep making lower highs and are sitting near their lows get close to 0. Markets that have climbed back with clearly higher lows get the most weight.

## cc4520af4e (XRP)
- **Read:** Before the crash it traded around 128–140. It fell to 102 and bounced to 120. It then made a low at 98 on day -45. Since then each rally has topped lower than the last: 115, 113, 108, 106. It has now drifted back to 100, near the support zone at 98–100.
- **Weight:** 0.1. This is a persistent downtrend that is pressing on its lows.
- **Change mind:** a close above 108.

## 4bb27fded0 (DOGE)
- **Read:** It ran up to 171 and then lost about 40%. The lower highs continue (131, 114.5, 109, 106), and price is grinding along 98–103. Support is at 97.6.
- **Weight:** 0.1. This is one of the weakest structures.
- **Change mind:** a close above 107.

## b76fa82f45 (BTC)
- **Read:** It peaked at about 127, crashed to 91, and printed a low of 89.5 on day -45. Since then the lows have stepped up: 89.5, then 95.3, then 96. Price is consolidating between 96 and 103.
- **Weight:** 0.4. This is a modest base with higher lows, but it has not broken out.
- **Change mind:** a close below 95.5 gets cut; a close above 103.5 gets added.

## 86f3254376 (DOT)
- **Read:** It has round-tripped from 219 down to 100. It made a lower low at 93 on day -13. The bounce to 108.9 failed, and it is back at 100.
- **Weight:** 0.1. The big-picture downtrend is still intact.
- **Change mind:** a close above 109.

## efa8eb8714 (SOL)
- **Read:** It crashed to 78.8, then recovered sharply to 110. From there it bled down to 92.5 on day -8. It then popped back to 100 on a single day.
- **Weight:** 0.3. The recovery from the low is strong, but the last month has been a pullback.
- **Change mind:** a close below 94 cuts it; a close above 104 adds.

## 997a76211c (ADA)
- **Read:** It had the deepest crash, to 71. It has also had the strongest recovery, about +40%. The lows are rising: 71, 80, 79, 95.6. On day -7 it broke above 90 on heavy volume, reaching a high of 108.8. Price is now holding just under that at about 100.
- **Weight:** 0.8. This has the strongest momentum and structure of the set.
- **Change mind:** a close below 95.

## 40570cb1df (LTC)
- **Read:** It crashed to 86.4, then made higher lows at 94.4 and 96. Its high after the crash was 106. Price is now consolidating between 97 and 102.
- **Weight:** 0.5. The base is constructive.
- **Change mind:** a close below 96.

## ecbbc470d5 (LINK)
- **Read:** It fell to 85.5, then recovered to 108.9 on day -13. The lows are rising: 85.6, 91.9, then 96.3. Price sits mid-range at 100.
- **Weight:** 0.45. It is improving, but rallies keep fading near 105–108.
- **Change mind:** a close below 96.

## e6ecd84895 (AVAX)
- **Read:** It was cut from 164 down to 88.5 on day -51. Since then it has been choppy between 94 and 108. The lows have risen only slightly, to 94.1, and the trend is flat.
- **Weight:** 0.3. This is directionless.
- **Change mind:** a close below 94 or above 106.

## df414002de (ETH)
- **Read:** It crashed to 79 and has climbed steadily since. The lows step up cleanly: 79, 89.7, 91.6, 95.4. Price is now near the top of its post-crash range at 100, with resistance at 102–104.
- **Weight:** 0.55. The structure is a clean, steady uptrend.
- **Change mind:** a close below 95.

{"cc4520af4e (XRP)": 0.1, "4bb27fded0 (DOGE)": 0.1, "b76fa82f45 (BTC)": 0.4, "86f3254376 (DOT)": 0.1, "efa8eb8714 (SOL)": 0.3, "997a76211c (ADA)": 0.8, "40570cb1df (LTC)": 0.5, "ecbbc470d5 (LINK)": 0.45, "e6ecd84895 (AVAX)": 0.3, "df414002de (ETH)": 0.55}

## Entscheidung 2026-08-16

**Strategy:** I use trend and relative strength over weeks. The most weight goes to markets making higher lows and breaking out of their post-crash ranges (the crash was around day -72) on rising volume. Less weight goes to markets stuck in a range, and close to none to markets still making lower highs and lower lows from their peaks around days -100 to -95. Each market's thesis fails if price closes below the nearest higher low or the breakout level.

### 815569e322 (LINK)
- **Read:** Peaked at 115.8 (day -98), crashed to 74.5 and double-bottomed at about 74.7 (day -52). It then built higher lows (75.4, then 80.1, then 84.0). Last week it broke out of the 85–95 range with an impulse from 87 to 103.8 on 1.66 volume, its strongest volume in two months. Close is 100, the highest since about day -85. Resistance is 103.8, then 106–107. Support is 93–94.
- **Weight:** 0.8. This is the only window with a clean, volume-confirmed breakout and clear relative strength against the rest.
- **Change my mind:** a close below 92.

### 4baccb82bb (ETH)
- **Read:** Fell from 128 to a crash low of 80.3, then made higher lows: 80.6 (day -51), 91.3, 97.1, and about 99.3 recently. Price has coiled in a tight 98–104 range on falling volume. Resistance is 104–105.6. Support is 97–98.
- **Weight:** 0.4. The structure is constructive but there is no breakout yet.
- **Change my mind:** a close below 97.

### 8893a6d921 (LTC)
- **Read:** Fell from 137 to lows of 91.8 and then 88.9. It recovered to 109 (day -29) and has pulled back to 98.3–100. Lows are rising: 88.9, 97.8, 98.8, 98.3. It is now testing the 98–99 support. Resistance is 104–109.
- **Weight:** 0.35. The trend is up but price is testing support.
- **Change my mind:** a close below 97.

### 2edba87a70 (ADA)
- **Read:** Fell from 165 to a crash low of 85, then 79.0 (day -52). Since then it has made higher highs (114.4, then 121.0) and higher lows (79, then 87.7). It has faded steadily from 121 to 100 on light volume. Support is 98–100, with the 87.7 low further below. Resistance is 110–115.
- **Weight:** 0.35. The structure is the strongest of the volatile names, but the current pullback is sharp.
- **Change my mind:** a close below 95.

### dfcd3050e4 (SOL)
- **Read:** Fell from 131.9 to a crash low of 80.6. It rebounded to 112.6 (day -43), drifted down to 94.6 (day -15), and is now at 100–102 with a small higher low. The range is 95–105.
- **Weight:** 0.3. This is a neutral range.
- **Change my mind:** a close below 94.5. A close above 105 would raise the weight.

### d875fe196a (BTC)
- **Read:** Fell from 131.7 to a crash low of 94, and later to 91.9. Since then it has ranged flat between 99 and 106, with slightly lower highs (107, then 106.4, 104.5, 104). Support is 99–99.4.
- **Weight:** 0.3. The range is flat and drifting lower.
- **Change my mind:** a close below 98.5.

### 0fbb37dc22 (AVAX)
- **Read:** Fell from 165 to a crash low of 98, then 89.7 (day -58). It recovered to about 112 (day -43) and has chopped between 96 and 110 since. Yesterday it spiked to 108.6 and was fully rejected back to 100. The range is wide and volatile.
- **Weight:** 0.25. There is no clear trend, and the latest move was a failed breakout.
- **Change my mind:** a close below 96. A close above 110 would turn me constructive.

### 4a9e57704d (DOGE)
- **Read:** Peaked at 170 (day -94) and has made persistent lower highs since: 132.9, 114, 108, 106, 105. Price is flattening around 99–102 on very low volume. Resistance is 105–106.
- **Weight:** 0.1. The trend is down and there is no base yet.
- **Change my mind:** a close above 106. A close below 97 would cut the weight to 0.

### cdcc0f2968 (DOT)
- **Read:** Has trended down steadily from about 180–230 to 100. It made a low of 98.6 (day -20), bounced to 114.6, and faded again. The highs keep falling.
- **Weight:** 0.1. This is a clear downtrend.
- **Change my mind:** a close above 110. A close below 98.5 would cut the weight to 0.

### 462701077f (XRP)
- **Read:** Peaked at 156 and crashed to 107.6. It bounced to 130, then fell back to 101.6 (day -51), bounced to 119, and has slid to 99.3 recently. It has broken below all of its post-crash support, making lower highs and lower lows. It is the weakest window relative to its own range.
- **Weight:** 0.05.
- **Change my mind:** a close above 110.

```json
{"4baccb82bb (ETH)": 0.4, "815569e322 (LINK)": 0.8, "d875fe196a (BTC)": 0.3, "4a9e57704d (DOGE)": 0.1, "462701077f (XRP)": 0.05, "8893a6d921 (LTC)": 0.35, "0fbb37dc22 (AVAX)": 0.25, "cdcc0f2968 (DOT)": 0.1, "dfcd3050e4 (SOL)": 0.3, "2edba87a70 (ADA)": 0.35}
```

## Entscheidung 2026-08-23

**Strategy.** Every window has the same shape: a sharp crash around day -80, a basing period, then a 4-day high-volume breakout to 100. I rank them by how much prior structure sits above 100. A breakout that clears the old pre-crash range, ideally after a base with rising lows, gets the most weight. One that runs straight into heavy overhead supply, comes out of a long downtrend, or looks like a blow-off gets the least. Each window's change-my-mind level is a close back inside its breakout zone, usually below the day -1 / day 0 lows.

## bb8cd13c70 (LINK)
- **Trend:** Pre-crash range was 73–93, with a peak close of 92.9 at day -105. The crash bottomed at 61. Lows then rose steadily (62 → 67 → 70), and the rally was already underway before the gap: 71 → 82 between days -13 and -5.
- **Breakout:** It reached 103.9 and is holding 100. That is above every close in the window, so there is no overhead supply. The day -1 wick (109 high, 94.7 low) came on heavy volume but closed firm.
- **Weight: 0.8.** Best structure in the set: a true range breakout with momentum that built before the gap.
- **Change my mind:** a close below 94.

## 0ddd40bd30 (ETH)
- **Trend:** Pre-crash highs were 96–98, peaking at 98.2 at day -128. The crash low was 61.1. Since then the lows have risen in steps: 61 → 63 → 70 → 74 → 75.
- **Breakout:** It gapped from 78 to 102 and is now consolidating at 98–100 on falling volume, which is a constructive flag. Price sits at the old range top.
- **Weight: 0.75.** A clean higher-low base and an orderly pullback after the breakout.
- **Change my mind:** a close below 95.5.

## 5d40875649 (SOL)
- **Trend:** Pre-crash highs were 100.8 and 102.0. The crash low was 63. A recovery to 86 at day -51 was followed by a tight 76–81 base.
- **Breakout:** It reached 98–100 and is now testing the prior highs at 101–103. The day -1 wick to 107.7 shows some selling, but the closes have held.
- **Weight: 0.7.** At the old range highs after a sound base. It needs to clear 103.
- **Change my mind:** a close below 92.

## e3e69b618c (BTC)
- **Trend:** The pre-crash peak was about 104–106, between days -110 and -104. The crash low was 76. The base ran 80–85 for about 50 days.
- **Breakout:** It went from 83 to 100.8, then held 99–100 for two days on low volume (1.05, then 0.87). That is the quietest consolidation in the group.
- **Weight: 0.65.** Healthy digestion, though there is some supply at 104–106.
- **Change my mind:** a close below 96.

## 251dd529f7 (LTC)
- **Trend:** The pre-crash range was 100–115. The crash low was 77. A recovery to 91 at day -36 faded back to 84.
- **Breakout:** It reached 101.7 and is now at 100. That is only the floor of the old range, with supply between 104 and 115.
- **Weight: 0.45.**
- **Change my mind:** a close below 95.

## 57f3503a78 (XRP)
- **Trend:** The pre-crash range was 86–97. A steady decline then took price down to 65 by day -5.
- **Breakout:** It ran 65 → 96 in three sessions on 4.5–6x volume. Day -1 printed a 111.8 high and closed at 96.2, which looks like a classic blow-off wick. Price is above the old range, but the move is parabolic straight out of a downtrend.
- **Weight: 0.4.** Strong momentum, but exhaustion risk is high.
- **Change my mind:** a close below 94. A close above 112 would raise the weight.

## c1c88a3194 (AVAX)
- **Trend:** The pre-crash range was 115–137, and the breakdown level is about 117. The base ran 81–91.
- **Breakout:** It reached 103, with a day -1 wick to 109 that closed at 98.5. There is large overhead supply between 105 and 125.
- **Weight: 0.35.**
- **Change my mind:** a close below 94.

## c0e57afb88 (DOGE)
- **Trend:** The pre-crash range was 95–125. After the crash there was a persistent decline from 95 to 74, then a flat base at 74–75.
- **Breakout:** It went to 98–100, with a day -1 high of 107.9 that was rejected. Supply sits between 105 and 120.
- **Weight: 0.3.**
- **Change my mind:** a close below 93.

## 642afefda9 (ADA)
- **Trend:** The pre-crash range was 105–130. Since the crash there have been two failed spikes: 63 → 88 around day -50, and 74 → 93 around day -17. Both fully retraced.
- **Breakout:** This is the third spike, with a 113.8 wick that closed at 99.6. The pattern is a pump-and-fade.
- **Weight: 0.3.**
- **Change my mind:** a close below 92. A close above 106 would raise the weight.

## 10e9a23014 (DOT)
- **Trend:** A 180-day downtrend from 179 to 81, with lower highs all the way down: 150, 145, 112, 97, 94.
- **Breakout:** The move to 100 does break the last lower high (about 94–96). Still, the larger structure is bearish, with supply at 105–112 and 128–150.
- **Weight: 0.2.** The weakest structure in the set.
- **Change my mind:** a close below 94. A close above 112 would raise the weight.

{"bb8cd13c70 (LINK)": 0.8, "0ddd40bd30 (ETH)": 0.75, "5d40875649 (SOL)": 0.7, "e3e69b618c (BTC)": 0.65, "251dd529f7 (LTC)": 0.45, "57f3503a78 (XRP)": 0.4, "c1c88a3194 (AVAX)": 0.35, "c0e57afb88 (DOGE)": 0.3, "642afefda9 (ADA)": 0.3, "10e9a23014 (DOT)": 0.2}

## Entscheidung 2026-08-30

**Strategy:** All ten markets share the same shape: a sharp crash around day -86, a basing period, then a broad surge from day -11 to day -8 that has since pulled back to 100. I rank each one by where it now sits within its own 180-day range, how much of the surge it has held, and whether it is above or below its pre-crash highs (overhead supply). Markets breaking to new range highs with shallow pullbacks get the most weight. Markets still deep under prior highs, or with repeated failed spikes, get the least.

## 9c36b22947 (ETH)
- **Read:** Started near 88 and peaked around 100 at day -135. It crashed to about 65, then built a slow base at 77–80. The surge ran from 79 to 104 and has eased only modestly to 100.
- **Structure:** It now trades at the top of its 180-day range, and the old ~100 high is acting as a pivot. Support is at 98.8 (today's low), then the 93–96 gap area.
- **Weight:** 0.7. It holds near its range highs with little overhead supply.
- **Change my mind:** A close below 95.

## 0c7e4958de (DOGE)
- **Read:** Prior highs were 135–144 (days -123 to -108). The crash took it to about 87, and it based at 84–86.
- **Structure:** The surge spiked to 122.9 intraday but closed only around 112–114, and it has since faded 12% to 100. Heavy overhead supply sits at 105–125.
- **Weight:** 0.3. Recovery is only partial, the fade is large, and it is well below its old range.
- **Change my mind:** Up on a close above 110; down below 96.

## 8298e0ea34 (DOT)
- **Read:** A persistent downtrend from 188 through 170 and 150 to a low near 91. The surge's 126 intraday spike was fully rejected, and price is back to 100.
- **Structure:** It is the furthest of all ten windows below its earlier prices, with lower highs throughout.
- **Weight:** 0.1. This is the weakest window.
- **Change my mind:** A close above 115.

## a5ad065f01 (SOL)
- **Read:** Prior high was about 96 at day -111. The crash low was near 59, and it based at 72–76.
- **Structure:** Unlike the others, it kept climbing after day -8, posting a new 180-day closing high of 107.3 at day -3. The pullback to 100 is normal. Support is at 98.6, then 93.
- **Weight:** 0.8. This is the strongest window: a new range high, a higher high after the surge, and good volume.
- **Change my mind:** A close below 93.

## f7f53b1bff (LTC)
- **Read:** Prior range was 110–126. The crash low was about 86, and it recovered to roughly 99 before sliding to 92.
- **Structure:** The surge reached 110.9 and has faded to 100. The net gain from base is small (about 8%), and it remains below the 110–120 supply zone.
- **Weight:** 0.3.
- **Change my mind:** Up on a close above 108; down below 97.

## 920a4d5b59 (XRP)
- **Read:** It was in a downtrend into the base, from 85 to 73.8. Then came the most violent surge of the group: 73.8 to a 125 intraday high on 6x volume, closing at 112.
- **Structure:** This looks like a blow-off top, now fading to 100. It sits mid-to-high in its 74–114 range.
- **Weight:** 0.4. Momentum is strong, but the climactic volume and the fade argue against a heavy weight.
- **Change my mind:** Up on a close above 110; down below 95.

## e0f92789fd (AVAX)
- **Read:** Prior range was 125–147. The crash hit about 80, and it chopped at 87–95.
- **Structure:** The surge peaked at 116.9 intraday and 110 on a closing basis, then faded to 100. Large overhead supply remains.
- **Weight:** 0.3.
- **Change my mind:** Up on a close above 108; down below 96.

## 3cda7eb33c (LINK)
- **Read:** Prior high was about 96 at day -112. The crash low was near 63.
- **Structure:** It was already making higher lows before the surge (72 → 74.5 → 78.8 → 85.6, including a breakout at day -15). The surge carried it to 107.6, and it held 101–107 before today's dip to 100. It is above its old highs.
- **Weight:** 0.75. The trend is strong and the surge came out of a building base.
- **Change my mind:** A close below 95.

## 81505bbd74 (BTC)
- **Read:** Prior high was about 106 at day -116. The crash low was near 76, and it based at 81–84.
- **Structure:** The surge took it to 103.3, and it has consolidated tightly at 99–104 on falling volume. This is an orderly flag just under the old highs.
- **Weight:** 0.6. The structure is clean and low-volatility, but it has not yet cleared 105.
- **Change my mind:** A close below 97.

## 1a08dcadd7 (ADA)
- **Read:** Prior range was 125–150. The crash took it to about 77.
- **Structure:** It has produced repeated failed spikes: 99.7 at day -57 faded to 80, and 104 at day -24 faded to 90. The latest spike to 134 intraday has already faded back to 100, so the pattern of rejection continues. Overhead supply is heavy.
- **Weight:** 0.2.
- **Change my mind:** Up on a close above 112; down below 95.

{"9c36b22947 (ETH)": 0.7, "0c7e4958de (DOGE)": 0.3, "8298e0ea34 (DOT)": 0.1, "a5ad065f01 (SOL)": 0.8, "f7f53b1bff (LTC)": 0.3, "920a4d5b59 (XRP)": 0.4, "e0f92789fd (AVAX)": 0.3, "3cda7eb33c (LINK)": 0.75, "81505bbd74 (BTC)": 0.6, "1a08dcadd7 (ADA)": 0.2}

## Entscheidung 2026-09-06

**1. Strategy**

Every window shares the same shock: a crash around days −96 to −93, a basing period, a sharp rally from day −18 to −15, and about two weeks of consolidation. I favour markets where 100 sits at or above the pre-crash level and near the 180-day highs, and where the post-spike pullback held higher lows. Markets still well below their pre-crash range, or inside a longer-term downtrend, get less weight. I also reward a clean close at or above the post-spike consolidation highs.

**2. Windows**

**5d1403f3bd (LINK)**
- **Read:** The strongest structure. The market was already trending up before the spike (61.9 → 72 from day −27 to −19). The spike took it to 95.4. It then held a higher-low range of 82.4 to 92.5. On day 0 it broke out to 100.9 on 1.7× volume and closed at 100, a new 180-day high. The pre-crash range was 68–82, now far below.
- **Weight:** 1.0. Clear breakout to new highs on volume, with no overhead supply.
- **Change my mind:** a close below 86.

**52e481ac0e (SOL)**
- **Read:** The pre-crash range was 77–92 and price is now above all of it. Price kept rising after the spike, to 103.8 on day −10. The pullback found a higher low at 91.4 and price has recovered to 100. Resistance is 103.8.
- **Weight:** 0.9. Trend continuation with only the 103.8 high left to clear.
- **Change my mind:** a close below 91.

**64ae9fc394 (ETH)**
- **Read:** The old highs were 96–98 (days −145 to −142) and the pre-crash range was 80–85. After the spike it held a tight 94–101 base for two weeks, and day 0 closed at 100, the top of that base and effectively a 180-day closing high. Volume has dried up, which suggests absorption rather than distribution.
- **Weight:** 0.9.
- **Change my mind:** a close below 93.5.

**8bdc9d320f (BTC)**
- **Read:** A steady, low-volatility market. The 180-day high is 103.1 and the pre-crash range was 92–97. The post-spike base is 95–101.4, and it printed a higher close of 101.2 on day −3. Price is just under the 103 high.
- **Weight:** 0.8. Solid, but less explosive and has the 103 ceiling directly overhead.
- **Change my mind:** a close below 94.5.

**565152c14a (LTC)**
- **Read:** The 180-day high is 110 (day −119) and the pre-crash range was about 94–99. It was rising before the spike (74 → 87). The pullback after the spike went deeper, to 86.2. It then rallied back on 2.3× volume (day −1) to the spike high of 100.4–100.9.
- **Weight:** 0.75. Good recovery, but price is testing the spike high rather than through it, and the pullback was deeper than the leaders'.
- **Change my mind:** a close below 88.

**149c2fb8f4 (XRP)**
- **Read:** Above its pre-crash range of about 91–94. The 180-day high is 112.9, and there is a spike wick to 119.4 on 6× volume, which looks like a blow-off. Since then it has drifted between 92 and 104, with highs fading (107 → 104 → 101).
- **Weight:** 0.6. Constructive, but the spike top marks supply between 102 and 107.
- **Change my mind:** a close below 92.

**163530ff05 (AVAX)**
- **Read:** Still below its pre-crash range of 112–115, and the start of the window was 120–133. There was a second washout to 71.8 on day −79. The spike reached 105.2 and the consolidation ran 88.7–96.7. Day 0 closed at 100, breaking above that consolidation.
- **Weight:** 0.45. Short-term momentum is positive, but the larger structure is still repairing.
- **Change my mind:** a close below 89.

**bb5eff3cff (ADA)**
- **Read:** Volatile. The pre-crash range was 104–112 and the early highs were 132. It made a lower low at 61.9 after the crash. The spike reached a 115.7 wick, closes have ranged 84.8–102.6, and the day −3 high of 100.9 was rejected. Supply overhead runs from 102 to 112.
- **Weight:** 0.35.
- **Change my mind:** a close below 85 (lower); a close above 103 would make me raise the weight.

**fafdbebe96 (DOGE)**
- **Read:** Topped at 130.5 on day −115, with a pre-crash range of about 110. It was in a lower-highs downtrend into a 76–80 base. Since the spike it has made lower highs (110.9 → 104.7), and day −1 was a wick rejection at 104.7. It sits 10% below the pre-crash level.
- **Weight:** 0.35.
- **Change my mind:** a close below 88.

**8e8e2dfba9 (DOT)**
- **Read:** A persistent downtrend across the whole window: 170 → 140 → 120 → 77. Day 0 is a +7% breakout from an 83–92 range on 1.67× volume, but it is just a retest of the 100–105 zone (the spike high is 105.4). Price is far below every earlier level and the lower highs are intact.
- **Weight:** 0.2. Weakest structure, so this is a small momentum stake only.
- **Change my mind:** a close below 85; a close above 106 would make me add.

**3. Weights**

{"5d1403f3bd (LINK)": 1.0, "52e481ac0e (SOL)": 0.9, "64ae9fc394 (ETH)": 0.9, "8bdc9d320f (BTC)": 0.8, "565152c14a (LTC)": 0.75, "149c2fb8f4 (XRP)": 0.6, "163530ff05 (AVAX)": 0.45, "bb5eff3cff (ADA)": 0.35, "fafdbebe96 (DOGE)": 0.35, "8e8e2dfba9 (DOT)": 0.2}

## Entscheidung 2026-09-13

**Strategy:** All ten markets sold off together around day -100, based, then broke out together on heavy volume around day -25. They have since pulled back to 100. I weight each one by relative strength: where 100 sits against its own 180-day range and its pre-crash high, and whether the post-breakout floor (about 97–99) is holding. Markets that cleared their old highs get more weight; markets still in long downtrends, or whose spikes failed, get little.

## bc7ee402e2 (LINK)
- **Read:** The strongest structure in the group. It went from 82 at the window start to a 63.5 low, then broke out from about 73 to 107. Its last high was 122 at day -6, well above the pre-crash high of 97. The current pullback to 100 sits on the 98–99 shelf. The trend is up with higher lows: 63.5, then 70, then 98.
- **Weight:** 0.7. It has leadership, but it is also volatile, and the pullback from 122 is sharp.
- **Change my mind:** a close below 97.

## 69dfe31070 (SOL)
- **Read:** It ran from a 60.6 low to 111.4 and is now holding above the old high of 99. Support is at 98–99 and resistance at 107–111.
- **Weight:** 0.7. It is clearly above its prior range and up from 90.7 at the window start.
- **Change my mind:** a close below 98.

## c11292b634 (ADA)
- **Read:** A long downtrend from 142. The post-crash rallies stall in a pattern of lower highs: 127 at day -22, then 114 at day -5. Price sits in the middle of a 93–114 range, well below the window start.
- **Weight:** 0.15. Relatively weak.
- **Change my mind:** a sustained close above 112.

## ccda8614d8 (XRP)
- **Read:** The volume climax at day -22 left a 126.7 wick that sold off immediately. Since then the highs keep falling (113 → 110 → 108) toward 100, below the pre-crash range of 100–115. Support is at 98.
- **Weight:** 0.3. A fading spike.
- **Change my mind:** up on a close above 108; to zero below 97.

## 5512746e86 (DOT)
- **Read:** A persistent downtrend from 158. A blow-off to 128.5 at day -5 was fully given back within four days, which is a failed breakout. Support is at 99.5, then 85.
- **Weight:** 0.05. The weakest of the ten.
- **Change my mind:** reclaiming 112.

## 0a00cb3ecf (AVAX)
- **Read:** It is down from 133–144 and has spent the window below its pre-crash range. It made two highs near 112–114, and price is now at the bottom of a 98–112 band.
- **Weight:** 0.2.
- **Change my mind:** a close above 111.

## 8b22322d76 (LTC)
- **Read:** A lower-volatility version of the same pattern. The post-breakout range is 89–103, with a 110.6 wick that was rejected. Price is below the old 108–112 highs and roughly flat over the window.
- **Weight:** 0.35. Middling.
- **Change my mind:** up on a close above 104; down on a close below 96.

## a4b0fb3549 (BTC)
- **Read:** A smooth, low-volatility recovery that has nearly regained the pre-crash level of about 101–107. Since day -23 it has held a tight range of 99.5–106, and it is up from 92.7 at the window start.
- **Weight:** 0.5. Orderly and constructive, but it has not yet made new highs.
- **Change my mind:** a close below 99.

## 1778fe256e (DOGE)
- **Read:** A major top near 140–144 around day -122, followed by a downtrend. The post-breakout high was 122, then 115, and price has slid to 100. Support is at 98, then 85.
- **Weight:** 0.15.
- **Change my mind:** reclaiming 110.

## f9b7894557 (ETH)
- **Read:** Price is at the top of its 180-day range: 100 compares with a pre-crash high of 99.5 and a window start of 89. Since the breakout it has consolidated in a tight 96–103 range. The day -2 push to 107.6 showed buyers are present.
- **Weight:** 0.75. The cleanest relative strength with the tightest base.
- **Change my mind:** a close below 96.

{"bc7ee402e2 (LINK)": 0.7, "69dfe31070 (SOL)": 0.7, "c11292b634 (ADA)": 0.15, "ccda8614d8 (XRP)": 0.3, "5512746e86 (DOT)": 0.05, "0a00cb3ecf (AVAX)": 0.2, "8b22322d76 (LTC)": 0.35, "a4b0fb3549 (BTC)": 0.5, "1778fe256e (DOGE)": 0.15, "f9b7894557 (ETH)": 0.75}

## Entscheidung 2026-09-20

**1. Strategy**

I use relative-strength trend following. Markets at or near their 180-day highs, with higher lows and a month-long base that holds above the breakout level, get the most weight. Markets still below earlier spike highs or the early-window highs, with lower highs that suggest supply overhead, get less. A parabolic one-to-two-day move on extreme volume counts as strong momentum, but I size it down for gap and reversal risk.

**2. Windows**

**2ff6306461 (AVAX)**
- **Trend and structure:** The market fell from 85 to 52, based at 55–60 for about two months, then broke out at -32 to about 69 and held a 63–72 range.
- **Recent move:** In the last two sessions it went vertical, from 67 to 100 (about +50%), on volume of 3.9x and 6.1x average. It closed at a new window high, above 92.7 from day -133.
- **Assessment:** This is a blow-off rather than a base breakout. Day 0's range of 83.4–101.4 shows heavy two-way trade, and there is no support between 83 and 72.
- **Weight:** 0.35. Momentum is undeniable, but the risk/reward of chasing is poor.
- **Change my mind:** A close below 83 would cut it to 0. Holding above 95 for a week would raise it.

**6d75526f7e (ETH)**
- **Trend and structure:** The market crashed to 57, recovered to 72, gapped up at -32 to 85–95, and built a tight month-long base between 89 and 97.
- **Recent move:** It now closes at 100, a new window high above the prior peak of 93.2, with higher lows at 89.2.
- **Assessment:** Volume is calm (0.6–0.8) on the push into highs. This is the cleanest base breakout of the group.
- **Weight:** 0.9.
- **Change my mind:** A close below 89.

**9363cda43f (LINK)**
- **Trend and structure:** The market went from a 56 low to a 58–70 base, then a breakout to 96. It spiked to 109.3 at -13 and pulled back to 84.8.
- **Recent move:** It has recovered to 100.
- **Assessment:** The uptrend is intact with higher lows (84.8 above the base), but 101–109 is still overhead supply.
- **Weight:** 0.65.
- **Change my mind:** A close below 86.

**ed973da0b8 (ADA)**
- **Trend and structure:** The window began at 119 with a high of 126.7, and price is still 20% below that.
- **Recent move:** It spiked to 113.4 at -29, then made lower highs at 101.8 and 103.1. It is ranging between 84 and 103.
- **Assessment:** It is volatile and capped below prior highs.
- **Weight:** 0.35.
- **Change my mind:** A close above 104 would raise it. A close below 84 would cut it to 0.

**ee587ff360 (SOL)**
- **Trend and structure:** The market went from a 54 low to a 64–70 base, then a breakout to 85–98 and a consolidation between 86 and 96.
- **Recent move:** It is now at 100, above the early-window high of 88.5 and near the 102.8 wick, with higher lows at 86.2.
- **Assessment:** The structure is strong and almost as clean as 6d75.
- **Weight:** 0.8.
- **Change my mind:** A close below 86.

**82ed3e605a (DOT)**
- **Trend and structure:** The window began at 123 with a high of 126.7. The market made a deeper second low at 63.7 at -33 (a lower low than 70.0).
- **Recent move:** It spiked to 113.1 at -12, collapsed to 82.3, and is now at 100.
- **Assessment:** This is the most erratic window, with lower highs versus the early period and wide daily ranges.
- **Weight:** 0.3.
- **Change my mind:** A close below 82 would cut it to 0. A close above 105 would raise it.

**53e07def86 (BTC)**
- **Trend and structure:** The market fell from a 102 high to 72.8, based at 77–80, broke out at -32, and has held a tight 92–101 range for a month.
- **Recent move:** It now sits at 100, close to the 102.1 window high.
- **Assessment:** This is the lowest-volatility, most orderly trend, with higher lows (92.4).
- **Weight:** 0.8.
- **Change my mind:** A close below 92.

**2796064d29 (DOGE)**
- **Trend and structure:** The window high is 135.9 at -129. After the crash the market made lower highs: 115.5, 109.0, 104.6.
- **Recent move:** It is now at 100, still well below the old range.
- **Assessment:** It is lagging relative to its own history.
- **Weight:** 0.3.
- **Change my mind:** A close above 105 would raise it. A close below 89.7 would cut it to 0.

**263d1f6102 (LTC)**
- **Trend and structure:** The window high is 103.2 at -133. The market fell to 67, built a steady base at 74–80, and broke out at -30 to 90.
- **Recent move:** It has made higher lows (81.6, then 85.5) and is now at 100, just under the 101.2 wick and the 103 high.
- **Assessment:** The trend is healthy and close to a full-window breakout.
- **Weight:** 0.75.
- **Change my mind:** A close below 85.

**ac3b02cda2 (XRP)**
- **Trend and structure:** It slid from 110 to a 70 low, then had a climax spike to 120.5 at -29 on 5.9x volume.
- **Recent move:** Since then it has made lower highs (105.2, 106.1) and a wide range of 88.4–106. It is now at 100.
- **Assessment:** Distribution after the climax, and day -5 was a large bearish engulfing.
- **Weight:** 0.35.
- **Change my mind:** A close above 106 would raise it. A close below 88 would cut it to 0.

**3. Weights**

{"2ff6306461 (AVAX)": 0.35, "6d75526f7e (ETH)": 0.9, "9363cda43f (LINK)": 0.65, "ed973da0b8 (ADA)": 0.35, "ee587ff360 (SOL)": 0.8, "82ed3e605a (DOT)": 0.3, "53e07def86 (BTC)": 0.8, "2796064d29 (DOGE)": 0.3, "263d1f6102 (LTC)": 0.75, "ac3b02cda2 (XRP)": 0.35}

## Entscheidung 2026-09-27

**Strategy:** All ten markets share the same path: a crash around day -117 to -114, a grind lower, a volume-driven reversal at day -39, and a second leg up in the last ten days. I weight each one by relative strength: whether 100 is a new 180-day high or still below the earlier peak (overhead supply), whether the lows keep rising, and how orderly the advance is. Clean breakouts with rising lows get the most weight. Parabolic, single-spike or still-below-highs charts get the least.

## 3d77f309a8 (XRP)
**Read:** Started near 89 and peaked around 102 (day -136). It fell to about 65 by day -40, then spiked to 112 intraday at day -36. Since then it has chopped violently between 84 and 109. It closes at 100, above the old closing highs near 98, but the volatility is extreme (5.6x volume, then a 109 → 97.5 reversal at day -4). Support is 95.7; resistance is 107.5–112.
**Weight: 0.5.** It is a breakout, but a wide, noisy one with a poor risk/reward.
**Change my mind:** a close below 95.

## 774f3ae765 (DOT)
**Read:** Peaked at 113 (day -137) and bottomed near 57 (day -40). It has recovered sharply, but the swings are wild: 101 → 74.5 → 103. It is still below the 104–113 supply zone from the first half of the window. Support is 85–86.9 (day -4).
**Weight: 0.4.** A strong rebound into heavy overhead resistance.
**Change my mind:** a close below 85, or a close above 106 to raise the weight.

## 7988bc1cb3 (ADA)
**Read:** Peaked at 113 (day -140) and capitulated to about 54 (day -95). Since then it has made a clean staircase of higher lows: 54 → 60 → 67 → 74 → 75.7 → 91.5. It is now back at 100, with 104–113 overhead. Support is 91.5–96.5.
**Weight: 0.65.** Good structure, held back by the overhead supply.
**Change my mind:** a close below 91.

## bcc2efc07f (AVAX)
**Read:** Prior high was 96 (day -140). It bottomed at 52 (day -100) and built a long base between 56 and 62. Then it went parabolic in three days, from 69.8 to 103.7 on 5.7x volume. It now holds 93.6–103.7, above all prior highs. Support is 91.4–92.4.
**Weight: 0.55.** A genuine breakout, but a vertical one with large unfilled air below.
**Change my mind:** a close below 91.

## 3062eea5f4 (BTC)
**Read:** The smoothest chart of the group. The crash was shallow (low about 70), and the lows have risen steadily: 69 → 73 → 76 → 88.7 → 98. Closing at 100 is just under the closing high of 102.5 (day -6) and well above the earlier 98 peak. Volatility is very tight, with a range of 99.6–100.8 in the last few days.
**Weight: 0.9.** The best risk-adjusted trend of the ten.
**Change my mind:** a close below 94.5.

## 3d9b39d55f (SOL)
**Read:** Prior high was 80.7. It bottomed at 49.3 and is now 25% above that old high. The higher lows are persistent: 49 → 52.5 → 58 → 72 → 78.5 → 92.2. Volume expands on the up days. Support is 92–95.
**Weight: 0.9.** The strongest relative trend.
**Change my mind:** a close below 91.

## 25f6f39a65 (LTC)
**Read:** Prior high was 85. It bottomed near 55. Price climbed steadily to 88, then gapped to 101 on a 6.7x volume spike at day -3, and it has held between 98.7 and 105 since. Support is 96.7 first, then the 86.5–88 gap.
**Weight: 0.6.** Strong, but driven by a single event and not yet tested.
**Change my mind:** a close below 86.

## 85812d659c (LINK)
**Read:** Prior high was 77.5. It bottomed at 50 and is now far above that old high. It has a strong sequence of higher lows (50 → 56 → 77 → 86) and accelerating closes. Support is 86–94.
**Weight: 0.85.** A strong trend, slightly more volatile than the top two.
**Change my mind:** a close below 85.

## fa2045983b (ETH)
**Read:** Prior high was 91.7. It bottomed at 56. It broke out at day -39 to about 93, then spent 30 days in an orderly base between 88 and 95. It broke out again to 103 and is now holding 100 on light volume, which looks like a healthy pause. Support is 96.7–98.
**Weight: 0.85.** A textbook base-and-breakout.
**Change my mind:** a close below 96.

## 3e7a0e249c (DOGE)
**Read:** The highest prior peak in the group relative to today (122 at day -136). It fell to about 70 and is still 18% below that peak. The spike to 109 at day -5 faded to 94 the next day. Support is 94; resistance is 105–109 and then 112–122.
**Weight: 0.3.** The weakest relative to its own history.
**Change my mind:** a close below 94, or a close above 109.5 to raise the weight.

{"3d77f309a8 (XRP)": 0.5, "774f3ae765 (DOT)": 0.4, "7988bc1cb3 (ADA)": 0.65, "bcc2efc07f (AVAX)": 0.55, "3062eea5f4 (BTC)": 0.9, "3d9b39d55f (SOL)": 0.9, "25f6f39a65 (LTC)": 0.6, "85812d659c (LINK)": 0.85, "fa2045983b (ETH)": 0.85, "3e7a0e249c (DOGE)": 0.3}
