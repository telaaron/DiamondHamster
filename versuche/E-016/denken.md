# E-016: was die KI gedacht hat (Set A)

Volle Antwort des Deciders pro Entscheidungswoche, unverändert. Er sah weder Datum noch Coin-Namen; die Namen in Klammern sind erst danach eingesetzt. Gesendeter Prompt und Daten: runs/<set>/<woche>/requests.json.

## Entscheidung 2026-07-05

**Strategy:** The 180-day trend is down in every window, so I cap exposure well below fully long. Each window has a capitulation low (around day -30) and a relief-rally high (around day -20), and I weight on how price has behaved since then:

- **0.6:** a higher high above the relief high plus a higher low. Flip is below the last higher low.
- **0.3–0.4:** a basing or double bottom that is still under the relief high. Flip is a close above that resistance, which would justify adding.
- **0.2:** lower lows and lower highs still intact. Flip is above the nearest lower high.

**269af209d3 (ETH)**
- **Read:** Long decline from about 138 (-79). Crash low at 84.3 (-29), relief high at 103.6 (-20), then a retest at 84.7 (-9), which forms a double bottom near 85. The 4-day rally into 100 brings price up to the neckline at 101–103.6 on modest volume.
- **Weight 0.3:** the base is constructive but not confirmed.
- **Flip 104:** a close above the neckline would confirm the double bottom.

**362b61613e (AVAX)**
- **Read:** Crash low 89.9, relief high 102.2. The new low at 82.0 (-16) came on 3x volume, which looks like a selling climax. Since then the lows have been rising: 86, 86.1, 90.6, 92.2, 98. Price is 100, just under 102–102.8 resistance.
- **Weight 0.4:** the higher-low sequence is better than most windows here.
- **Flip 103:** a close above resistance would add.

**b0ec489261 (DOT)**
- **Read:** Persistent lower highs from 163 (-53). The crash low of 100.3 failed, and price fell to 90.2 (-7). The bounce to 100 is still below the lower highs at 106–114.
- **Weight 0.2:** the downtrend structure is intact.
- **Flip 106:** a close above that would break the sequence of lower highs.

**bf2a6c7452 (BTC)**
- **Read:** Crash low 92.9, relief high 105.7, slight undercut to 90.8 (-4). This is a 91–106 range, and price is mid-range at 100.
- **Weight 0.3:** no edge in the middle of the range.
- **Flip 106:** a close above the range top.

**474325b554 (ADA)**
- **Read:** Deepest selloff of the group: crash to 78.4, a lower low at 72.9 (-10), then a high-volume V-reversal (-4 to -1, volume around 2x) from 76 to a 105.5 high. That cleared the 100.3 relief high, and price is now holding 100 just above it. The larger trend is still bearish, with overhead supply at 120–130.
- **Weight 0.6:** strong momentum and a breakout.
- **Flip 92:** a close below the -1 low at 92.3 would mean the reversal failed.

**9cb9641d45 (SOL)**
- **Read:** Crash low 73.7, relief high 93.3, higher low at 78.5 (-10). Price is now 100, a clean higher high and higher low. The next resistance is the old 100–110 shelf from -100 to -35.
- **Weight 0.6:** this is the best-confirmed reversal structure.
- **Flip 93:** a close back below the prior relief high.

**12456e51ad (XRP)**
- **Read:** Crash low 90.7, relief high 111.8, lower low at 87.2 (-9). The bounce to 100 is still under 102.6/107/111.8.
- **Weight 0.3:** it is still a lower-low structure, but the bounce is firm.
- **Flip 103:** a close above the first lower high would add.

**84e7fa1707 (LINK)**
- **Read:** Crash low 86.8, relief high 106.7, double bottom at 86.9 (-10). Price is 100, with resistance at 102.9–106.7.
- **Weight 0.3:** a base below the neckline.
- **Flip 104:** a close above it would add.

**673713db86 (LTC)**
- **Read:** Crash low 88.4, relief high 101.2, lower low at 85.7 (-11/-10). Since then the lows have risen gradually, and price has reached 100 right at the 101.2 resistance.
- **Weight 0.3:** testing resistance, not through it.
- **Flip 102:** a close above that would confirm.

**990f5a978f (DOGE)**
- **Read:** Distribution from 152 (-52), crash low 99.7, relief high 118.7, then lower lows down to 89.3 (-5). The bounce to 100 is below the lower highs at 106–114.
- **Weight 0.2:** the downtrend is intact.
- **Flip 106:** a close above that would break the lower highs.

{"269af209d3 (ETH)": {"weight": 0.3, "flip": 104.0}, "362b61613e (AVAX)": {"weight": 0.4, "flip": 103.0}, "b0ec489261 (DOT)": {"weight": 0.2, "flip": 106.0}, "bf2a6c7452 (BTC)": {"weight": 0.3, "flip": 106.0}, "474325b554 (ADA)": {"weight": 0.6, "flip": 92.0}, "9cb9641d45 (SOL)": {"weight": 0.6, "flip": 93.0}, "12456e51ad (XRP)": {"weight": 0.3, "flip": 103.0}, "84e7fa1707 (LINK)": {"weight": 0.3, "flip": 104.0}, "673713db86 (LTC)": {"weight": 0.3, "flip": 102.0}, "990f5a978f (DOGE)": {"weight": 0.2, "flip": 106.0}}

## Entscheidung 2026-07-12

**Strategy:** Last week's weight and flip price stand unless a close since the last decision (day -5) has crossed the flip price. A low-weight flip sits above price and breaks on a close above it. A high-weight flip sits below price and breaks on a close below it. Where a flip has broken, I set a new weight by trend: price below the falling 180-day structure and failed rallies earn 0–0.3, and holding higher lows above reclaimed support earns more.

### 19d1ae2de3 (AVAX)
- **Read:** Long downtrend from 230. It crashed from 140 to 105 around day -37, retested 92 and recovered to about 108, and is now fading back to 100. Resistance is 108–111, support 92–97.
- **Flip check:** Closes since day -5 ranged 100.0–105.2, never above 111.3.
- **Decision:** Keep 0.40.
- **Change my mind:** A close above 111.3.

### 2ac0a7aa44 (LINK)
- **Read:** Crash to 88 at day -37, a lower low near 88 at day -17, then a bounce to about 100. It is still below the 104–107 breakdown zone. Support is 88–90.
- **Flip check:** Closes ranged 95.5–100.0, never above 104.9.
- **Decision:** Keep 0.30.
- **Change my mind:** A close above 104.9.

### 459e6bf395 (LTC)
- **Read:** Breakdown from 118 to 92. It has been basing at 89–104 and is now chopping around 100. Resistance is 104–106.
- **Flip check:** Highest close was 101.7, below 106.2.
- **Decision:** Keep 0.30.
- **Change my mind:** A close above 106.2.

### 492cedf89c (BTC)
- **Read:** Drop from 121 to 92. It is now in a tight range near 100 on contracting ranges. Resistance is 104–106, support 91.
- **Flip check:** Highest close was 100.6, below 105.8.
- **Decision:** Keep 0.30.
- **Change my mind:** A close above 105.8.

### 1b4d295c10 (DOT)
- **Read:** Persistent downtrend from 270, with lower highs at 124 and 107 after the crash. It is now around 100. Support is 95.
- **Flip check:** Highest close was 103.9, below 110.6.
- **Decision:** Keep 0.20.
- **Change my mind:** A close above 110.6.

### 20e8fb25d3 (DOGE)
- **Read:** Downtrend. It fell from 139 to 112, then from 122 to 98, with a weak bounce to 107 that is fading. Resistance is 107–113, support 96–98.
- **Flip check:** Highest close was 101.9, below 113.5.
- **Decision:** Keep 0.20.
- **Change my mind:** A close above 113.5.

### 5c4880cc5d (ADA)
- **Flip check:** Last week's 0.60 rested on support at 107.6. Day -4 closed at 103.1, so the flip broke and the weight is re-decided.
- **Read:** The spike from 89 to 118.6 on heavy volume (day -8) failed and gave back almost all of it, closing at 100. That is a failed breakout inside a long downtrend from 260. Support is 85–89, resistance 108–113.
- **Decision:** Cut to 0.20.
- **Change my mind:** A close back above 109, which reclaims the failed-breakout zone.

### 8b639c3fce (SOL)
- **Read:** Crash to 78, then higher lows at 83 and 88 and a breakout to 107. It is now pulling back to 100, the best structure in the set. Support is 98–99.
- **Flip check:** Lowest close was 99.8, above 98.6.
- **Decision:** Keep 0.60.
- **Change my mind:** A close below 98.6.

### 3201bd3835 (ETH)
- **Read:** Crash to 83, then a double bottom near 84. It is recovering toward 100 with resistance at 101–102.
- **Flip check:** Highest close was 100.0, below 102.8.
- **Decision:** Keep 0.30.
- **Change my mind:** A close above 102.8.

### b5c05271c4 (XRP)
- **Read:** Breakdown from 123 to 97 and a lower high at 114. It is now holding around 100 after a bounce to 106. Resistance is 106–110, support 93–96.
- **Flip check:** Highest close was 101.7, below 109.8.
- **Decision:** Keep 0.30.
- **Change my mind:** A close above 109.8.

{"19d1ae2de3 (AVAX)": {"weight": 0.4, "flip": 111.3}, "2ac0a7aa44 (LINK)": {"weight": 0.3, "flip": 104.9}, "459e6bf395 (LTC)": {"weight": 0.3, "flip": 106.2}, "492cedf89c (BTC)": {"weight": 0.3, "flip": 105.8}, "1b4d295c10 (DOT)": {"weight": 0.2, "flip": 110.6}, "20e8fb25d3 (DOGE)": {"weight": 0.2, "flip": 113.5}, "5c4880cc5d (ADA)": {"weight": 0.2, "flip": 109.0}, "8b639c3fce (SOL)": {"weight": 0.6, "flip": 98.6}, "3201bd3835 (ETH)": {"weight": 0.3, "flip": 102.8}, "b5c05271c4 (XRP)": {"weight": 0.3, "flip": 109.8}}

## Entscheidung 2026-07-19

## Strategy

All ten assets show the same picture over the window: a crash about 165 days ago, a failed recovery, and a second leg down about 45 days ago. Each one is now basing near 100. My rule is to stay small (0.2 to 0.4) while price is under the overhead supply left by the second leg down. I add exposure (0.5 to 0.6) only where price has reclaimed its recent range high and is making higher lows. I keep last week's weight unless a close since then crossed last week's flip price.

## aef0402ddc (DOGE)
- **Read:** Steady downtrend from about 160 to a low of 96 on day -19. Since then it has been a tight, low-volume range of about 98 to 104. Overhead resistance is 107.5 and 113–122.
- **Flip check:** The highest close since last week is 102.8, which is below the flip at 114. Not broken.
- **Weight:** Keep **0.20**. The range on falling volume is not yet a reversal.
- **Change my mind:** A close above 114.

## bec8030d06 (LINK)
- **Read:** Downtrend from 128 to a low of 83.6. Price rallied to 101.8 on day -4, which crossed last week's flip at 100, and is now holding about 100. Lower highs sit at 102.6 and 103.0. Support is 95.5, then 92.
- **Flip check:** Broken, so I am deciding fresh.
- **Weight:** **0.40**. Price is pressing the top of its range with higher lows (83.6, then 85, then 93.8, then 95.5), but it is still below the 103 lid.
- **Change my mind:** A close below 95 would break the higher-low sequence.

## c8585d515a (XRP)
- **Read:** Price failed at 105–107 and is now ranging 97–101.5. Resistance is 105.4 and 108–113. Support is 92–95.
- **Flip check:** The highest close since last week is 101.4, below the flip at 108.6. Not broken.
- **Weight:** Keep **0.30**.
- **Change my mind:** A close above 108.6.

## fb31282cef (ADA)
- **Read:** A sharp spike to 120 on day -15 fully retraced. Price is now chopping 94.8–100.2. Resistance is 105–115. Support is 93.4, then 86.
- **Flip check:** The highest close is 100.2, below the flip at 106.2. Not broken.
- **Weight:** Keep **0.20**.
- **Change my mind:** A close above 106.2.

## 83c2b29964 (AVAX)
- **Read:** Price is in a 97–108 range above an 88 capitulation low, with 103.8 as near resistance. Day 0 was a weak close at 100.
- **Flip check:** The highest close is 103.8, below the flip at 110.3. Not broken.
- **Weight:** Keep **0.40**.
- **Change my mind:** A close above 110.3.

## 99bb239acb (BTC)
- **Read:** Price is grinding higher from a low of 89.8 and is now at 100, with 100.5 as range resistance. Support is 96.3 and 92.
- **Flip check:** The highest close is 100.5, below the flip at 104.3. Not broken.
- **Weight:** Keep **0.30**.
- **Change my mind:** A close above 104.3.

## c9e1ccb791 (SOL)
- **Read:** Price rallied from 81.4 to 107.8, then pulled back to 98.2. That pullback closed below last week's flip at 99.3.
- **Flip check:** Broken, so I am deciding fresh.
- **Structure:** Higher lows at 81.4, then 88.7, then about 96–97. Range resistance is 107–110, with the bigger range at 110–115. Support is 96.
- **Weight:** **0.40**. The trend up from the low is intact, but momentum has stalled under 108.
- **Change my mind:** A close below 96 would break the higher lows.

## 0f75a3f7fe (LTC)
- **Read:** A base formed at 83.5–87 over days -25 to -23. On day -1 price broke out above the 97–98 range highs, closing 99.9 on above-average volume. It held at 100 on day 0.
- **Flip check:** The day -1 close crossed above last week's flip at 99.3. Broken, so I am deciding fresh.
- **Weight:** **0.60**. This is a breakout from the base. Resistance is next at 107–110.
- **Change my mind:** A close below 96 would mean the breakout failed back into the range.

## a199c353ae (ETH)
- **Read:** A double bottom at about 80.5–82, then a rally to 104 on day -4. Price pulled back to 98.4 and held, with 96.3 as support.
- **Flip check:** Last week's flip at 99.2 was crossed, so I am deciding fresh.
- **Structure:** Higher highs and higher lows over the last three weeks. Resistance is 104, then 108–113.
- **Weight:** **0.50**.
- **Change my mind:** A close below 96.

## 7b9b419554 (DOT)
- **Read:** Price is in a 99–109 range below a 123 lower high. Day 0 was a weak close at 100, near range support of about 98–99.
- **Flip check:** The highest close is 104.8, below the flip at 113.8. Not broken.
- **Weight:** Keep **0.20**.
- **Change my mind:** A close above 113.8.

{"aef0402ddc (DOGE)": {"weight": 0.2, "flip": 114.0}, "bec8030d06 (LINK)": {"weight": 0.4, "flip": 95.0}, "c8585d515a (XRP)": {"weight": 0.3, "flip": 108.6}, "fb31282cef (ADA)": {"weight": 0.2, "flip": 106.2}, "83c2b29964 (AVAX)": {"weight": 0.4, "flip": 110.3}, "99bb239acb (BTC)": {"weight": 0.3, "flip": 104.3}, "c9e1ccb791 (SOL)": {"weight": 0.4, "flip": 96.0}, "0f75a3f7fe (LTC)": {"weight": 0.6, "flip": 96.0}, "a199c353ae (ETH)": {"weight": 0.5, "flip": 96.0}, "7b9b419554 (DOT)": {"weight": 0.2, "flip": 113.8}}

## Entscheidung 2026-07-26

**Strategy:** I classify each window by trend structure: where price sits relative to its 180-day history, the sequence of swing highs and lows, and whether the recent base is holding. I size the long weight by how constructive that structure is, from 0 in a clean downtrend to 1 in a confirmed uptrend. Following the carry-over rule, I keep last week's weight and flip price unless a close since then has crossed the flip, meaning above an upside flip or below a downside flip. None of the ten windows has crossed its flip this week, so every weight carries over.

## 5919d4d79a (ADA)
- **Read:** Long downtrend from about 216 to a capitulation low near 89.5 at day -50, then a second low around 83–87 near day -30. A spike to 120.5 failed, and price has ranged roughly 94–109 since. The latest high was 108.9 and price is back at 100 on falling volume.
- **Resistance:** 105–109, then 120.
- **Support:** 94, then 85.
- **Weight:** Last week's flip of 106.4 was never closed above (best close 105.1), so the weight stays at **0.20**. The base is there but unconfirmed below a downtrend.
- **Flip:** 106.4

## bee05ab1b9 (DOT)
- **Read:** Downtrend from about 226 to the 96–98 area. The bottom has gone sideways in a 97–108 range for about four weeks, with lower highs since 108.7. Price is at 100.
- **Resistance:** 105–109, then 112.7.
- **Support:** 95.
- **Weight:** No close above 112.7 (max 102.3), so it stays at **0.20**.
- **Flip:** 112.7

## 0f6667ab52 (SOL)
- **Read:** Price fell from 165 to a 78.3 low at day -50 and made a higher low at 83.4 near day -31. It rallied to 109 and is now consolidating between 95.7 and 103.
- **Support:** 95.5–96.
- **Resistance:** 103, then 109.
- **Weight:** The lowest close since last week was 96.4, above the 95.5 flip, so it stays at **0.40**. The structure is mildly constructive with higher lows.
- **Flip:** 95.5

## 366ffdd55c (AVAX)
- **Read:** Low at 84.2 on day -37, then a choppy recovery between 91 and 105. Day -3 dipped to 91.9, followed by a strong reversal close at 100.5 on 1.5x volume. The range is still intact.
- **Support:** 91–92.
- **Resistance:** 104–105.7.
- **Weight:** Max close was 100.5, below the 105.7 flip, so it stays at **0.40**.
- **Flip:** 105.7

## 663f86d09f (BTC)
- **Read:** This one held up better than the others. Low at 88.9 on day -31, followed by a slow grind of higher lows to the 98–102 area. Price is at 100, just under the recent 102.4 high.
- **Resistance:** 102.4, then 103.2.
- **Support:** 97.5.
- **Weight:** No close above 103.2 (max 101.8), so it stays at **0.30**.
- **Flip:** 103.2

## f86167d6fd (DOGE)
- **Read:** Downtrend from 170. Lows near 97 at day -31 and 93 at day -3, the latter a slight lower low that was quickly reclaimed. Price is ranging 93–108 with lower highs.
- **Resistance:** 106–108, then 112.5.
- **Support:** 93.
- **Weight:** No close above 112.5, so it stays at **0.20**.
- **Flip:** 112.5

## d414434622 (LTC)
- **Read:** Low at 82.1 on day -31, then a steady series of higher lows. Price broke above the 95–96 shelf at day -8 and is holding 97–99. Today's close at 100 is near the 100.6 range high.
- **Support:** 95.6–96.
- **Resistance:** 100.6, then 106.
- **Weight:** The lowest close since last week was 96.9, above the 94.5 flip, so it stays at **0.60**. This is the most constructive structure in the set.
- **Flip:** 94.5

## d84b40d30d (LINK)
- **Read:** Low at 79.4 on day -31, followed by higher lows at 85, 89, and 93.7. Today is a strong up day to 100, breaking the 99.3 high.
- **Support:** 93.7, then 90.
- **Resistance:** 103, then 111.
- **Weight:** The lowest close since last week was 94.5, above the 90.3 flip, so it stays at **0.40**.
- **Flip:** 90.3

## 581c652a99 (XRP)
- **Read:** Low at 90.7 on day -30. Price rallied to 106 and has been ranging 96–105, with the recent high at 104.6 and price at 100. Volume is drying up.
- **Resistance:** 104.6–106.4, then 107.1.
- **Support:** 96.
- **Weight:** No close above 107.1 (max 102.7), so it stays at **0.30**.
- **Flip:** 107.1

## 7642549d37 (ETH)
- **Read:** Lows at 77.0 on day -50 and 77.4 on day -30 form a double bottom. Since then, higher lows at 87.7 and 94.5, and price is pressing against the 99.6–100.6 highs.
- **Support:** 94.5, then 91.9.
- **Resistance:** 100.6, then 103–110.
- **Weight:** The lowest close since last week was 95.2, above the 91.9 flip, so it stays at **0.50**.
- **Flip:** 91.9

{"5919d4d79a (ADA)": {"weight": 0.2, "flip": 106.4}, "bee05ab1b9 (DOT)": {"weight": 0.2, "flip": 112.7}, "0f6667ab52 (SOL)": {"weight": 0.4, "flip": 95.5}, "366ffdd55c (AVAX)": {"weight": 0.4, "flip": 105.7}, "663f86d09f (BTC)": {"weight": 0.3, "flip": 103.2}, "f86167d6fd (DOGE)": {"weight": 0.2, "flip": 112.5}, "d414434622 (LTC)": {"weight": 0.6, "flip": 94.5}, "d84b40d30d (LINK)": {"weight": 0.4, "flip": 90.3}, "581c652a99 (XRP)": {"weight": 0.3, "flip": 107.1}, "7642549d37 (ETH)": {"weight": 0.5, "flip": 91.9}}

## Entscheidung 2026-08-02

**Strategy:** For each window I first check whether any close since last week's decision (days -6 to 0) has crossed the flip price, in whichever direction the flip was set relative to price at that time. If it hasn't, I keep last week's weight and flip unchanged. If it has, I re-decide using the trend since the day -58 crash low, the higher-low/lower-high structure of the recent swings, and the nearest breakout or breakdown levels.

## 814f51dcad (SOL)
- **Flip check:** Last week's 0.40 had a downside flip at 99.6, set when price was 104.3. The day -2 close of 99.0 broke it, so I re-decide.
- **Read:** The crash bottomed at 81.7 on day -57. The rebound topped at 114.1 on day -29. Since then the highs keep falling: 107.3, then 106.5, then 104.7. Price is stuck in a 96–105 range with fading volume. Day -1 dipped to 95.9 and today recovered to 100.0.
- **Weight 0.30:** The structure leans bearish, but support near 96 is still holding.
- **Flip 95.5:** A close below the 95.9 low confirms the breakdown.

## c7818b3e31 (ADA)
- **Flip check:** Last week's 0.20 had an upside flip at 93.2, set when price was 87.6. Today's close of 100.0 broke it, so I re-decide.
- **Read:** The base since the crash held at 72.9–95. Today is a +8.7% day on 1.73x volume. It cleared the month's range high of 95.4 (day -11) and the 93–94 area. Resistance is the day -29 spike high near 101.4–105.5.
- **Weight 0.60:** This is a range breakout on volume.
- **Flip 91.0:** A close back inside the old range means the breakout failed.

## 6feb0b95fd (XRP)
- **Flip check:** Upside flip at 109.7. The highest close since is 100.0, so it is not broken.
- **Read:** Flat 96–105 range below a falling 109 high.
- **Decision:** Keep 0.30, flip 109.7.

## 8f0e890593 (DOGE)
- **Flip check:** Upside flip at 116.6. The highest close since is about 100.1, so it is not broken.
- **Read:** Downtrend from 160, now basing at 96–105.
- **Decision:** Keep 0.20, flip 116.6.

## 44a14ed760 (DOT)
- **Flip check:** Upside flip at 116.8. The highest close since is 100.0, so it is not broken.
- **Read:** Persistent downtrend. Day -6 gapped down to 93.6, and price has since recovered to 100.
- **Decision:** Keep 0.20, flip 116.8.

## 3c66aa26a5 (LTC)
- **Flip check:** Last week's 0.60 had a downside flip at 101.2, set when price was 107.0. The day -2 close of 99.1 broke it, so I re-decide.
- **Read:** Lows have been rising since the crash: 88.0 (day -39), then 96.0 (day -20), then 97.6 (day -1). The highs reached 107.2–108. The pullback from 108 has trimmed momentum, but the higher-low structure is intact above 96–97.6.
- **Weight 0.40:** Reduced from 0.60 because momentum faded, but the uptrend structure still holds.
- **Flip 96.5:** A close below the higher lows breaks the structure.

## c6a8e94d6a (LINK)
- **Flip check:** Downside flip at 95.0. The lowest close since is 96.2, so it is not broken.
- **Read:** Recovery range of 94–105.
- **Decision:** Keep 0.40, flip 95.0.

## fbb22ab849 (BTC)
- **Flip check:** Upside flip at 106.2. The highest close since is 101.9, so it is not broken.
- **Read:** Tight 98–105 consolidation.
- **Decision:** Keep 0.30, flip 106.2.

## 32cbf614ba (AVAX)
- **Flip check:** Upside flip at 108.8. The highest close since is 100.4, so it is not broken.
- **Read:** Choppy 93–106 range. Today saw a sharp bounce off 94.4 on volume.
- **Decision:** Keep 0.40, flip 108.8.

## 3c6bf5d158 (ETH)
- **Flip check:** Downside flip at 95.3. The lowest close since is 97.9, so it is not broken.
- **Read:** Higher lows since the crash at 80.2 (day -37), with price holding 98–102.
- **Decision:** Keep 0.50, flip 95.3.

{"814f51dcad (SOL)": {"weight": 0.3, "flip": 95.5}, "c7818b3e31 (ADA)": {"weight": 0.6, "flip": 91.0}, "6feb0b95fd (XRP)": {"weight": 0.3, "flip": 109.7}, "8f0e890593 (DOGE)": {"weight": 0.2, "flip": 116.6}, "44a14ed760 (DOT)": {"weight": 0.2, "flip": 116.8}, "3c66aa26a5 (LTC)": {"weight": 0.4, "flip": 96.5}, "c6a8e94d6a (LINK)": {"weight": 0.4, "flip": 95.0}, "fbb22ab849 (BTC)": {"weight": 0.3, "flip": 106.2}, "32cbf614ba (AVAX)": {"weight": 0.4, "flip": 108.8}, "3c6bf5d158 (ETH)": {"weight": 0.5, "flip": 95.3}}

## Entscheidung 2026-08-09

**Strategy.** I hold last week's weight unless a daily close since then has crossed last week's flip price, in either direction. When no flip is broken, the position and flip carry over unchanged. When a window is free to re-decide, I size by trend structure: full long only above a reclaimed prior range, flat below broken support, and partial in between.

**Flip check.** I checked the closes from day −5 to day 0 against each flip price. None of the ten windows broke its flip, so every weight is kept.

---

### 9bec0d662d (SOL)
- **Read:** Price collapsed from about 128 to a low near 79 around day −65, then rebounded to about 108 by day −37.
  - It has since slid into a tightening range of 94–102 on fading volume.
  - Day 0 closed at 100.0, testing the top of the range.
  - Support sits at 92.5–94.5 and resistance at 102–103.
- **Flip check:** Last week's flip was 92.2. The lowest close since then is 95.3, so it was not broken.
- **Weight:** Keep 0.30. The base is constructive, but the trend is not confirmed.
- **Flip:** 92.2. A close below it loses the range floor.

### d0958ccba6 (DOGE)
- **Read:** A long downtrend runs from the 171 high: a crash to 114, a dead-cat bounce to 133, then a grind down to 98–106.
  - Price has been flat near 100 for three weeks on very low volume.
  - Support is 97.6–98.4. Resistance is 106–107, then 113.
- **Flip check:** Last week's flip was 119.1. The highest close since then is 101.6, so it was not broken.
- **Weight:** Keep 0.20. The trend is still down and the base is unproven.
- **Flip:** 119.1, where the trend structure would turn up.

### 72d91768bc (BTC)
- **Read:** Price topped near 127, then crashed to 91 and has been basing at 90–102 for two months.
  - The lows are rising: 89.5, then 96.2, then about 97.
  - Price is pinned at 100 on low volume, just under the 102.5–103 ceiling.
- **Flip check:** Last week's flip was 104.0. The highest close since then is 100.1, so it was not broken.
- **Weight:** Keep 0.30.
- **Flip:** 104.0. A breakout above the base would justify adding.

### eb17062e8b (ADA)
- **Read:** Price crashed from about 148 to a low near 71, rebounded to 99, and pulled back to 80.
  - A recent high-volume breakout reached 108.8 intraday and held 98–103.
  - Day 0 pulled back to 100.0.
  - Support is 95–97, then 86–88.
- **Flip check:** Last week's flip was 88.7. The lowest close since then is 98.3, so it was not broken.
- **Weight:** Keep 0.60. Momentum is up and there is a higher-low structure.
- **Flip:** 88.7. A close there would mean the breakout has failed back into the old range.

### 4602ff702f (DOT)
- **Read:** This is a persistent downtrend from the 219 spike high, with lower highs at 180, then 131, then 112, then 108.9.
  - The latest bounce to 107 failed, and price is back at 100.
  - Support is 93–95.
- **Flip check:** Last week's flip was 116.8. The highest close since then is 107.3, so it was not broken.
- **Weight:** Keep 0.20.
- **Flip:** 116.8. Only a close above the lower-high sequence changes the picture.

### 3d14f367dc (LINK)
- **Read:** Price fell from 132 to 85.5, then recovered and is holding a 96–108 range.
  - Higher lows are in place at 85.6, then 91.9, then 96.3.
  - Price sits at 100 in the middle of the range.
  - Resistance is 105–108.
- **Flip check:** Last week's flip was 97.3. The lowest close since then is 99.5, so it was not broken.
- **Weight:** Keep 0.40.
- **Flip:** 97.3. A close below it breaks the recent higher-low support.

### b3256588fe (LTC)
- **Read:** Price crashed from 133 to 86.4 and has recovered steadily to a 96–105 range.
  - The pullback held 96 and price is now recovering at 100.
  - Resistance is 105.
- **Flip check:** Last week's flip was 94.9. The lowest close since then is 97.4, so it was not broken.
- **Weight:** Keep 0.40.
- **Flip:** 94.9, just under the range floor.

### fb5f46adac (XRP)
- **Read:** Price is in a downtrend from 150, with a failed bounce at 125.6 and a lower high at 113.
  - It is drifting lower: day −3 closed at 100.5 and day −2 at 99.1, slipping below the 101.5–103 shelf.
  - The next support is 98.
- **Flip check:** Last week's flip was 115.8. The highest close since then is 104.3, so it was not broken.
- **Weight:** Keep 0.30. Structure is weakening, but the rule says hold.
- **Flip:** 115.8.

### 24baadd7dc (AVAX)
- **Read:** Price crashed from 163 to 88.5 and has been in a choppy, volatile range of 94–110 since.
  - Highs at 108.8–110.8 keep capping it.
  - Price is at 100.
- **Flip check:** Last week's flip was 111.0. The highest close since then is 104.2, so it was not broken.
- **Weight:** Keep 0.40.
- **Flip:** 111.0, a breakout above the range ceiling.

### 790bc9bf79 (ETH)
- **Read:** Price fell from 129 to a low of 78.8 and has since recovered in a series of higher lows: 79, then 89.7, then about 95.4.
  - It is holding 96–102 and sits at 100.
  - Resistance is 102–104.
- **Flip check:** Last week's flip was 94.0. The lowest close since then is 97.4, so it was not broken.
- **Weight:** Keep 0.50.
- **Flip:** 94.0, which loses the higher-low structure.

---

{"9bec0d662d (SOL)": {"weight": 0.30, "flip": 92.2}, "d0958ccba6 (DOGE)": {"weight": 0.20, "flip": 119.1}, "72d91768bc (BTC)": {"weight": 0.30, "flip": 104.0}, "eb17062e8b (ADA)": {"weight": 0.60, "flip": 88.7}, "4602ff702f (DOT)": {"weight": 0.20, "flip": 116.8}, "3d14f367dc (LINK)": {"weight": 0.40, "flip": 97.3}, "b3256588fe (LTC)": {"weight": 0.40, "flip": 94.9}, "fb5f46adac (XRP)": {"weight": 0.30, "flip": 115.8}, "24baadd7dc (AVAX)": {"weight": 0.40, "flip": 111.0}, "790bc9bf79 (ETH)": {"weight": 0.50, "flip": 94.0}}

## Entscheidung 2026-08-16

**Strategy:** I follow the weekly rule exactly. For each window I check whether any close since last week's decision (days −5 to 0) crossed the flip price. Below-price flips break on a close under them, and above-price flips break on a close over them. If no close crossed, I keep last week's weight and flip. If one did, I reprice using trend (where price sits relative to the post-crash range and the recent swing highs and lows) with a bias toward staying flat in downtrends.

All ten windows close between 99 and 107 over the past week, and none crossed its flip. Every weight is therefore carried forward unchanged.

## 4d300235ae (XRP)
- **Read:** A long decline from about 145 to 100. The crash near day −72 bottomed at 107.6, the bounce stalled at about 117, and price has since made steady lower highs and lower lows. It is now sitting at the 99–100 lows on very light volume.
- **Resistance and support:** Resistance is 105, then 109–112. Support is near 99.3, and below that the structure is unknown.
- **Weight:** Closes ran 100.0–102.9, nowhere near the 120 flip, so I keep **0.30**.
- **Flip:** 120.0. A close above it would mean the bearish structure is fully repaired.

## 40f119fd81 (ADA)
- **Read:** A crash low at about 79–83 (days −53 to −47). A strong rally followed, with highs at 114 (day −43) and 121 (day −10). Price has been pulling back from about 115 to 100, so the uptrend off the lows is intact but the trend is fading.
- **Support:** About 99.8 now, with 96 and 88–89 below.
- **Weight:** The lowest close was 100.0, above the 98.6 flip, so I keep **0.60**.
- **Flip:** 98.6. A close below it breaks the higher-low structure.

## c0a3b3ed0f (AVAX)
- **Read:** After the crash from about 141 to the 89.7 low (day −58), price has chopped sideways between roughly 97 and 110 for two months.
- **Recent action:** Day −1 spiked to 108.6 and was rejected, closing at 100.
- **Levels:** The range is bounded by 95–96 and 110.
- **Weight:** Closes ran 99.8–102.3, below the 112.6 flip, so I keep **0.40**.
- **Flip:** 112.6. A close above it would be a range breakout.

## 1611b69058 (SOL)
- **Read:** The crash bottomed at 80.6 (day −71). A recovery reached about 112 (day −44), then price faded into a tight 97–104 consolidation.
- **Levels:** Support is 94.6–97, resistance is 104–105.
- **Weight:** Closes ran 100.0–102.3, above the 94.3 flip, so I keep **0.30**.
- **Flip:** 94.3. A close below it breaks the consolidation floor.

## 1229468716 (LINK)
- **Read:** The crash low was 74.5. A double bottom formed near 74.7, followed by a series of higher lows.
- **Recent action:** Price broke out of the 85–92 base this week on rising volume (day −5 close 93.5, day −1 close 100.9 on a high of 103.8) and now holds about 100. This is the strongest structure in the set.
- **Levels:** Support is 95, then 88. Resistance is 104, then 110–115.
- **Weight:** All closes were far above the 84.8 flip, so I keep **0.40**.
- **Flip:** 84.8.

## 4a674e6266 (ETH)
- **Read:** The crash low was 80.3. Price recovered back to about 100–103 and has spent five weeks in a tight sideways range of roughly 98–104 on shrinking volume.
- **Levels:** Support is 97–98, resistance is 104–105.
- **Weight:** Closes ran 99.8–100.5, above the 95.7 flip, so I keep **0.50**.
- **Flip:** 95.7. A close below it would break the range.

## 0b97844ca5 (DOGE)
- **Read:** Price topped near 165 (day −94) and has fallen steadily since. It now trades in a tight 98–106 range with low volume.
- **Levels:** Resistance is 106 and then 112–114, and the trend is down.
- **Weight:** The highest close was 103.3, far from the 118.7 flip, so I keep **0.20**.
- **Flip:** 118.7.

## c5ba6263e9 (LTC)
- **Read:** The crash low was 89 (day −53). A recovery peaked at 109 (days −29 to −21), and price is now drifting down in a 98–105 band.
- **Levels:** Support is 98.3, then 95.
- **Weight:** The lowest close was 99.3, above the 97.7 flip, so I keep **0.40**.
- **Flip:** 97.7. A close below it breaks the higher-low sequence.

## cd07667796 (DOT)
- **Read:** A persistent downtrend from about 200 to 100, with lower highs at 137, 119 and 114.6.
- **Recent action:** The day −12 bounce to 114.6 has fully retraced back to 100.
- **Levels:** Support is about 98.6, then 105.9 from the day −51 low. Resistance is 109, then 115.
- **Weight:** Closes ran 100.0–106.1, nowhere near the 123.0 flip, so I keep **0.20**.
- **Flip:** 123.0.

## 89a745d818 (BTC)
- **Read:** The post-crash low was 92.4 (day −52). Since then price has made a slow, low-volatility grind in a 99–106 band. The day −26 high of 106.4 is a lower high versus the pre-crash range of 117–130.
- **Levels:** Support is 99.3, resistance is 104–106.
- **Weight:** Closes ran 100.0–101.7, below the 107.3 flip, so I keep **0.30**.
- **Flip:** 107.3. A close above it clears the range top.

```json
{"4d300235ae (XRP)": {"weight": 0.30, "flip": 120.0}, "40f119fd81 (ADA)": {"weight": 0.60, "flip": 98.6}, "c0a3b3ed0f (AVAX)": {"weight": 0.40, "flip": 112.6}, "1611b69058 (SOL)": {"weight": 0.30, "flip": 94.3}, "1229468716 (LINK)": {"weight": 0.40, "flip": 84.8}, "4a674e6266 (ETH)": {"weight": 0.50, "flip": 95.7}, "0b97844ca5 (DOGE)": {"weight": 0.20, "flip": 118.7}, "c5ba6263e9 (LTC)": {"weight": 0.40, "flip": 97.7}, "cd07667796 (DOT)": {"weight": 0.20, "flip": 123.0}, "89a745d818 (BTC)": {"weight": 0.30, "flip": 107.3}}
```

## Entscheidung 2026-08-23

**Strategy:** Keep last week's weight unless the close has broken last week's flip price. Where a new decision is needed, I go long after a high-volume breakout above a multi-month base. The weight is sized down when the breakout ran into a blow-off reversal or old overhead supply. The flip sits just below the breakout level or back inside the old range.

Checking each flip against the closes from day -4 to day 0: five windows had a downside flip that was never touched, so they keep their weight. The other five had an upside flip that was broken by the rally, so they get a new decision.

## 530a1464b5 (LINK)
- **Read:** Crashed from about 90 to 61 and built a base at 62–75. Then a vertical breakout from 82.6 to 103.9 on very high volume, a long-wick reversal at 109.3, and a hold near 100.
- **Flip check:** Last week's flip of 69.0 was never closed below.
- **Weight:** Keep 0.40.
- **Flip:** 69.0.

## 0532434d98 (ADA)
- **Read:** Fell from 130 to 60, then a base at 68–88. Broke out from 77 to 100+ with a blow-off wick to 113.8.
- **Flip check:** The flip of 76.0 held; the lowest close was 76.9 on day -5, before this week.
- **Weight:** Keep 0.60.
- **Flip:** 76.0.

## 1dacb7dbb0 (SOL)
- **Read:** Base at 75–82 after the crash, then broke out to 98 and holds 100 after the 107.7 wick.
- **Flip check:** The flip of 73.7 was not broken.
- **Weight:** Keep 0.30.
- **Flip:** 73.7.

## 4c897e40c9 (AVAX)
- **Read:** Long decline from 138 to a 74.7 low, then a 60-day range at 80–92. The breakout cleared 92/93.7, which broke last week's flip, so this is a new decision. Day -1 rejected at 109.3, but day 0 held 95.6+ on lighter volume. Overhead supply sits around 117–120.
- **Weight:** 0.60, a confirmed range breakout with room up to the old supply.
- **Flip:** 91.0, which is a close back inside the old range.

## dff35dd02c (DOT)
- **Read:** Strong downtrend from 179 to 78 with a range at 80–96. The breakout to 101.3 broke the 100.6 flip, so this is a new decision. Day -1 was a shooting star at 111.2, right at the gap zone of 105–112 left during the crash. The broader trend is still down.
- **Weight:** 0.40.
- **Flip:** 92.0, back below the range top.

## 4bfc6aa5ef (BTC)
- **Read:** Topped at 106, crashed to 76, then ranged 75–86. Broke out cleanly through 86.8 (the old flip) to 100.8. The last two days are tight bars at 98–101 on falling volume, with no blow-off wick, so the breakout is being absorbed well. The prior high at 106 is the next target.
- **Weight:** 0.70.
- **Flip:** 92.0.

## dce1b15ff0 (LTC)
- **Read:** Steady recovery from the 75 low to a range at 84–92, then a breakout to 101.7. It holds 100 after the 106.1 wick.
- **Flip check:** The flip of 82.5 was not broken.
- **Weight:** Keep 0.40.
- **Flip:** 82.5.

## cafa74095f (DOGE)
- **Read:** Bled from 123 to a dead-flat range at 73–80 on very low volume. Then a spike from 75 to 98, which broke the 88.4 flip, so this is a new decision. Day -1 hit 107.9 and closed at 98.4 on 3.5x volume, a blow-off into the 105–110 supply.
- **Weight:** 0.50.
- **Flip:** 89.0.

## a9c376aa45 (ETH)
- **Read:** Base at 63–79, then a breakout gap from 78 to 91.5 and on to 102. It holds 100.
- **Flip check:** The flip of 72.9 was not broken.
- **Weight:** Keep 0.50.
- **Flip:** 72.9.

## 768f7167ae (XRP)
- **Read:** It was still making lower lows at 65–66 just before the move. Then it rose 50% in four days on 4–6x volume, breaking the 78.4 flip, so this is a new decision. Day -1 was a huge reversal, with a high of 111.8 and a close of 96.2. This looks the most like a climax: there is no base, only a short-squeeze profile. Resistance sits at 95–97.
- **Weight:** 0.40.
- **Flip:** 88.0, a close below the breakout shelf.

{"530a1464b5 (LINK)": {"weight": 0.4, "flip": 69.0}, "0532434d98 (ADA)": {"weight": 0.6, "flip": 76.0}, "1dacb7dbb0 (SOL)": {"weight": 0.3, "flip": 73.7}, "4c897e40c9 (AVAX)": {"weight": 0.6, "flip": 91.0}, "dff35dd02c (DOT)": {"weight": 0.4, "flip": 92.0}, "4bfc6aa5ef (BTC)": {"weight": 0.7, "flip": 92.0}, "dce1b15ff0 (LTC)": {"weight": 0.4, "flip": 82.5}, "cafa74095f (DOGE)": {"weight": 0.5, "flip": 89.0}, "a9c376aa45 (ETH)": {"weight": 0.5, "flip": 72.9}, "768f7167ae (XRP)": {"weight": 0.4, "flip": 88.0}}

## Entscheidung 2026-08-30

**Strategy:** I hold last week's weight unless the close has crossed last week's flip price since then. When it has, I size the position from the 180-day trend and the most recent structure. Here that structure is a sharp volume breakout from a long base, followed by a pullback. I keep the weight low when the long-term trend is down and the breakout has given back most of its gain, and I set the flip at the level that would confirm or refute the breakout.

## 0105747b64 (LTC)
- **Read:**
  - Price crashed from about 121 to 86 around day -89, then built a base between 88 and 97.
  - The volume breakout on days -11 to -9 reached 115.7. Price has since pulled back to 100, which is above the breakout origin at about 92.5.
  - Last week's flip at 90 was never closed below; the lowest close since then is 100.0.
- **Weight:** 0.40, kept.
- **Flip:** 90.0.

## 791cfca668 (DOT)
- **Read:**
  - This is a persistent downtrend, from 188 to about 92. The base since day -60 sits between 91 and 108, with lower highs.
  - The spike reached 126 on day -8 and failed. Closes since then went 113 → 104 → 107.6 → 100.
  - Last week's flip at 104.2 was crossed both ways: up on day -4 at 107.0, then down on day -2 at 103.7. It counts as broken, so I make a new decision.
  - The breakout has given back most of its gain, and price sits mid-base inside a bigger downtrend.
- **Weight:** 0.20, kept small.
- **Flip:** 108.0. A close above the post-spike closing highs (about 107.6) would revive the breakout and justify adding.

## aa4f62b7c9 (BTC)
- **Read:**
  - Price broke out of an 80–85 base to about 101 and is holding tightly between 100 and 103.
  - That is the strongest hold among these windows. The flip at 92.1 is untouched.
- **Weight:** 0.70, kept.
- **Flip:** 92.1.

## dfd7c81815 (SOL)
- **Read:**
  - Price rallied from a 70–76 base to 107 and is now at 100. That is a higher high than the day -59 peak near 81.
  - The flip at 69.1 is far below.
- **Weight:** 0.30, kept.
- **Flip:** 69.1.

## 7a8a1ea5d2 (AVAX)
- **Read:**
  - The base ran from 87 to 95, followed by a spike to 117 on day -8. Price has since settled at 100–106.
  - The flip at 97.3 was not closed below; the lowest close is 100.0.
- **Weight:** 0.60, kept.
- **Flip:** 97.3.

## 3cb0faa5b0 (XRP)
- **Read:**
  - Price had drifted down to about 73, then broke out on very heavy volume (6x average) to a 125 high.
  - It is now 100. Day 0's intraday low of 98.4 came close to the flip, but the close of 100.0 held above 98.6.
- **Weight:** 0.40, kept.
- **Flip:** 98.6.

## 0f65d37fbb (ADA)
- **Read:**
  - Price swung between 75 and 104, then spiked to 134 on day -8 and is now back at 100. That is a deep give-back, but still above the 90 base.
  - The flip at 89.5 is untouched.
- **Weight:** 0.60, kept.
- **Flip:** 89.5.

## 2933751d08 (LINK)
- **Read:**
  - There is a staircase of higher lows from 63, through 70 and 73, up to 85, then a breakout to 113.
  - Price is now at 100, and the flip at 71.5 is far below.
- **Weight:** 0.40, kept.
- **Flip:** 71.5.

## 4ed58688ef (DOGE)
- **Read:**
  - Price peaked near 144, collapsed to an 84–90 base, then spiked to 123 on day -8.
  - Today's close of 100.0 is below last week's flip at 101.3, so it is broken and I make a new decision.
  - Price is still well above the 90 base top, but momentum has faded after four lower closes from 108.6.
- **Weight:** 0.30, cut back modestly.
- **Flip:** 109.0. A close above the recent high closes (about 108.6) would justify re-adding.

## e6132d5ded (ETH)
- **Read:**
  - Price broke out of a 77–80 base to 105 and is holding between 100 and 104.
  - The flip at 74.3 is untouched.
- **Weight:** 0.50, kept.
- **Flip:** 74.3.

{"0105747b64 (LTC)": {"weight": 0.40, "flip": 90.0}, "791cfca668 (DOT)": {"weight": 0.20, "flip": 108.0}, "aa4f62b7c9 (BTC)": {"weight": 0.70, "flip": 92.1}, "dfd7c81815 (SOL)": {"weight": 0.30, "flip": 69.1}, "7a8a1ea5d2 (AVAX)": {"weight": 0.60, "flip": 97.3}, "3cb0faa5b0 (XRP)": {"weight": 0.40, "flip": 98.6}, "0f65d37fbb (ADA)": {"weight": 0.60, "flip": 89.5}, "2933751d08 (LINK)": {"weight": 0.40, "flip": 71.5}, "4ed58688ef (DOGE)": {"weight": 0.30, "flip": 109.0}, "e6132d5ded (ETH)": {"weight": 0.50, "flip": 74.3}}

## Entscheidung 2026-09-06

**Strategy:** I keep last week's weight and flip unless a daily close since last week (days -5 to 0) has crossed the flip price. When the flip is broken, I re-decide using trend structure: a high-volume breakout from a long base, followed by a held higher low and a reclaim of the breakout highs, earns a large long. The new flip goes just below the most recent swing low. Without a breakout of that kind, I stay light.

## 99cba7bd77 (ETH)
Read: The stock fell from about 96 to a 60–63 low. It then built a base at 74–77 and broke out sharply on high volume (days -18 to -16) to about 100. Since then it has held a range of 94–101.
Flip check: The flip is 71.4. Closes over the past week stayed between 95 and 100, so it was not broken.
Decision: Keep weight 0.50. Flip stays at 71.4.

## b88d5f1e49 (ADA)
Read: The stock crashed to 70 and spent a long time in a 65–90 range. It then spiked to 102–115 on very high volume, pulled back to 86, and has now recovered to 100.
Flip check: The flip is 77.2. The lowest close this week was about 88, so it was not broken.
Decision: Keep weight 0.60. Flip stays at 77.2.

## 643c8b5500 (LTC)
Read: The stock bottomed near 75. It recovered into an 80–87 range, then broke out to 95–100. After pulling back to 87, it surged on day -1 (volume 2.3) to 99.5 and closed at 100 today.
Flip check: The flip is 78.5. Closes stayed above 88, so it was not broken.
Decision: Keep weight 0.40. Flip stays at 78.5.

## d62e1067c4 (DOGE)
Read: The stock had a long decline from 127 to a flat base at 76–78, with very low volume. Days -18 to -15 brought a high-volume breakout to about 101. It pulled back to an 88–90 floor and then reclaimed the area: 96.6, then 98.6 on volume 1.8, then 100.0 today.
Flip check: The flip is 98.4, above where price stood a week ago (about 90). Closes of 98.6 and 100.0 broke it to the upside, so I re-decide.
Decision: The structure is a breakout from the base, a retest that held near 88, and a renewed push toward the 101–104 highs. That is bullish, so I raise the weight to 0.70. I would change my mind on a close below 88.0, which would undercut the retest low.

## 3708bdb838 (DOT)
Read: The stock fell steadily from 155 to a base at 76–80. It broke out on high volume to 96 (intraday high 105), then pulled back to a higher low of 83.7 around days -7 and -6. It has since climbed 89 → 91 → 92 → 94 → 100, with today's close on volume of 1.67. That close is above the breakout-day close of 96.
Flip check: The flip is 90.3. Closes of 90.8 and higher broke it upward, so I re-decide.
Decision: A higher low followed by a new closing high after the base breakout is a bullish continuation pattern. The longer downtrend is still in the background, so I take weight 0.70 rather than 1.0. I would change my mind on a close below 84.0, the higher low.

## 9c9b41becb (AVAX)
Read: The stock went from a crash low near 72 into a base at 78–88. It then broke out to 99–105, held a pullback at about 89, and has climbed back to 100.
Flip check: The flip is 87.5. The lowest close was about 89.9, so it was not broken.
Decision: Keep weight 0.60. Flip stays at 87.5.

## 1bb152cb59 (XRP)
Read: The stock drifted down to a quiet base near 70. A very high-volume blow-off (volume 4–6) took it to 103–119. It then settled into a range of 92–104 and closes at 100 today.
Flip check: The flip is 94.0. Closes this week were 95.0, 94.9, 101.9, 98.2, 99.2 and 100.0, so it was not broken.
Decision: Keep weight 0.40. Flip stays at 94.0.

## 11dd0cd8de (BTC)
Read: The stock found a low near 74, built a tight base at 78–81, broke out to 97–101, and has been consolidating between 95 and 101.
Flip check: The flip is 89.1, and it was not broken.
Decision: Keep weight 0.70. Flip stays at 89.1.

## 0a03f88be2 (SOL)
Read: The stock bottomed at 58 and built a base around 67–72. It then broke out to 100–104, held a pullback at 92–94, and closes at 100.
Flip check: The flip is 66.0, and it was not broken.
Decision: Keep weight 0.30. Flip stays at 66.0.

## c80bf6dd62 (LINK)
Read: The stock hit a low near 53 and climbed through higher lows into the low 60s. It then broke out in stages through 72 and 90, held between 84 and 88, and closed at 100 today on volume of 1.7.
Flip check: The flip is 60.2, and it was not broken.
Decision: Keep weight 0.40. Flip stays at 60.2.

{"99cba7bd77 (ETH)": {"weight": 0.5, "flip": 71.4}, "b88d5f1e49 (ADA)": {"weight": 0.6, "flip": 77.2}, "643c8b5500 (LTC)": {"weight": 0.4, "flip": 78.5}, "d62e1067c4 (DOGE)": {"weight": 0.7, "flip": 88.0}, "3708bdb838 (DOT)": {"weight": 0.7, "flip": 84.0}, "9c9b41becb (AVAX)": {"weight": 0.6, "flip": 87.5}, "1bb152cb59 (XRP)": {"weight": 0.4, "flip": 94.0}, "11dd0cd8de (BTC)": {"weight": 0.7, "flip": 89.1}, "0a03f88be2 (SOL)": {"weight": 0.3, "flip": 66.0}, "c80bf6dd62 (LINK)": {"weight": 0.4, "flip": 60.2}}

## Entscheidung 2026-09-13

# T-001 trader decisions

**Strategy:** Last week's weight stays unless a daily close since day −5 has gone below last week's flip price. Only then do I set a new weight from trend, structure and volume. Each flip is reset to the nearest support below the current range, so a real breakdown triggers a review next week instead of waiting for a deep drawdown.

Only one window broke its flip: **2b2e98185e (XRP)** closed at 99.5 on day −3, below its 99.8 flip. All others keep their weight.

### ac1cecb7ee (ETH)
- **Read:** The 76–77 base broke out on high volume at day −25 and pushed to about 100. Since then price has held a 95–103 range for three weeks. A spike to 107.6 on day −2 was rejected. Support is 95.1–96.2.
- **Flip check:** Not broken. The lowest close since last week is 98.4, well above 72.5.
- **Weight:** Keep 0.50.
- **Flip:** 95.0. A close below it loses the post-breakout range.

### 8effa8bd36 (LINK)
- **Read:** The breakout ran to a blow-off high of 122.2 on day −6, then price fell back to 100. That is volatile, but price is still above the 97.4–98.1 range lows.
- **Flip check:** Not broken. The lowest close is 100.0, above 71.1.
- **Weight:** Keep 0.40.
- **Flip:** 97.0.

### d88b49a005 (ADA)
- **Read:** A gap-and-run move topped at 127 on day −22, and price has since made a higher low around 93–95. It now sits in the middle of a 98–111 range.
- **Flip check:** Not broken. The lowest close is 100.0, above 84.7.
- **Weight:** Keep 0.60.
- **Flip:** 94.0. A close below it loses the day −14 low.

### 2b2e98185e (XRP)
- **Read:** The breakout from the 74–75 base came on the heaviest volume in the window (4–6x). Price then held a 99–113 range. The day −3 close of 99.5 was immediately reclaimed, and price is now at the bottom of the range.
- **Flip check:** Broken (99.5 close below 99.8), so I decided a new weight.
- **Weight:** 0.40. Volume still supports holding the breakout, but price is testing support, so I stay moderate.
- **Flip:** 97.5. A close below it, under the 97.7–98.0 lows, would start filling the breakout gap.

### 36f1a71a89 (AVAX)
- **Read:** The breakout from the 86–88 base made higher highs up to 112.5, then pulled back to about 100. Support is 96.2–97.6.
- **Flip check:** Not broken. The lowest close is 100.0, above 94.9.
- **Weight:** Keep 0.60.
- **Flip:** 96.0.

### b044b9fb42 (DOT)
- **Read:** A climax spike to 128.5 on day −5 came on 4x volume, and price has given almost all of it back to 100. That pattern is a warning, but the earlier 85–92 base is still well below.
- **Flip check:** Not broken. The lowest close is 100.0, above 82.3.
- **Weight:** Keep 0.70.
- **Flip:** 95.5. A close below it, under the day −6 low, would confirm the spike has failed.

### f34c0427a3 (BTC)
- **Read:** After the breakout from the 82–84 base, price has held a tight 99–106 range with low volatility. Support is 99.0–99.5.
- **Flip check:** Not broken. The lowest close is 99.6, above 93.2.
- **Weight:** Keep 0.70.
- **Flip:** 98.5.

### 3ed720faef (SOL)
- **Read:** The breakout from the 75–77 base peaked at 111.4 on day −17. Since then highs have been lower (108, 106.5) and price is back to 100. Support is 98.1–98.7.
- **Flip check:** Not broken. The lowest close is 99.4, above 70.8.
- **Weight:** Keep 0.30.
- **Flip:** 97.5.

### 812d37efa9 (DOGE)
- **Read:** The breakout from the 84–86 base hit 122 and later retested at 115.5. Price is now at 100, just above the 97.2–98.1 lows.
- **Flip check:** Not broken. The lowest close is 100.0, above 97.1.
- **Weight:** Keep 0.70.
- **Flip:** 97.0.

### b643301a3c (LTC)
- **Read:** The breakout from the 82–83 base reached 103. The trend has been choppier but higher, with a low near 88 at day −14 and a spike to 110.6 on day −6 that was rejected. Support is 96.0–96.6.
- **Flip check:** Not broken. The lowest close is 96.9, above 80.3.
- **Weight:** Keep 0.40.
- **Flip:** 95.5.

{"ac1cecb7ee (ETH)": {"weight": 0.5, "flip": 95.0}, "8effa8bd36 (LINK)": {"weight": 0.4, "flip": 97.0}, "d88b49a005 (ADA)": {"weight": 0.6, "flip": 94.0}, "2b2e98185e (XRP)": {"weight": 0.4, "flip": 97.5}, "36f1a71a89 (AVAX)": {"weight": 0.6, "flip": 96.0}, "b044b9fb42 (DOT)": {"weight": 0.7, "flip": 95.5}, "f34c0427a3 (BTC)": {"weight": 0.7, "flip": 98.5}, "3ed720faef (SOL)": {"weight": 0.3, "flip": 97.5}, "812d37efa9 (DOGE)": {"weight": 0.7, "flip": 97.0}, "b643301a3c (LTC)": {"weight": 0.4, "flip": 95.5}}

## Entscheidung 2026-09-20

**Strategy:** Each window is a mechanical check first. If no close since last week's decision (days -4 to 0) has broken the flip price, I keep last week's weight and flip. Only when the flip has been broken do I re-assess. For a re-assessment I look at trend, range structure and volume, size the position by how clearly price sits above support, and set the flip just below the nearest meaningful support.

## 328c5ffde7 (XRP)
- **Rule check:** Broken. Closes at -4 (92.1) and -3 (91.9) were below the 92.7 flip, so a new decision is needed.
- **Read:** The asset fell from about 100 to a base near 70–72, then broke out at -32 to -29 on very heavy volume (4–6x average) to 103–107. Since then it has traded in a wide, volatile range of roughly 89–106. Last week whipsawed: a spike to 106.1 at -6, a flush to 89.7 at -5, then a recovery to 100 on above-average volume. Range support is 88.4–89.7, and resistance is 103–106 (the 120.5 spike high is an outlier). The structure is a high-level consolidation after a breakout, with price mid-range.
- **Weight:** 0.50. The breakout has held for a month and demand keeps defending 89–92. Choppy two-way volatility argues against a full position.
- **Flip:** 88.5. A close below the range floor would mean the breakout is failing.

## 032bf91ed3 (AVAX)
- **Rule check:** Not broken. Closes since last week ran 66.1, 67.3, 72.5, 89.2 and 100, all far above 61.9.
- **Read:** A violent breakout from the 63–72 range: +38% in two days on 4–6x volume.
- **Weight:** Kept at 0.60.
- **Flip:** 61.9, carried over. The breakout zone at about 72 is now the first support.

## 4b0f26aaa9 (SOL)
- **Rule check:** Not broken. Closes since last week were 88.7, 91.4, 101.4, 99.9 and 100, all above 87.1.
- **Read:** Uptrend from the 66–69 base. Price broke above the 88–96 consolidation at -2 and is holding about 100.
- **Weight:** Kept at 0.30.
- **Flip:** 87.1.

## 4a3507fc71 (DOGE)
- **Rule check:** Not broken. The lowest close since last week was 92.7, above 91.6.
- **Read:** A recovery from the 80 base into a 90–105 range, now back at 100.
- **Weight:** Kept at 0.70.
- **Flip:** 91.6.

## 554afddfdd (LINK)
- **Rule check:** Not broken. Closes since last week were 88.3 to 100, above 86.8.
- **Read:** A rising trend from 64–66, with a pullback that held near 85–87. It is back at 100, under the 109 high.
- **Weight:** Kept at 0.40.
- **Flip:** 86.8.

## ba440ecf72 (BTC)
- **Rule check:** Not broken. Closes since last week were 93.9 to 100, above 93.2.
- **Read:** A steady uptrend after the 77–80 base, with a tight 93–101 consolidation. It is near the top of that range on quiet volume.
- **Weight:** Kept at 0.70.
- **Flip:** 93.2.

## 00a24cb7d0 (DOT)
- **Rule check:** Not broken. Closes since last week were 89.8 to 100, above 84.1.
- **Read:** The 113 spike faded to 83, then price rebounded sharply to 100 on strong volume.
- **Weight:** Kept at 0.70.
- **Flip:** 84.1.

## b30a8b8c3e (LTC)
- **Rule check:** Not broken. Closes since last week were 88.0 to 100, above 87.4.
- **Read:** A grinding uptrend from 75. A breakout above the 93–94 consolidation is holding at 100.
- **Weight:** Kept at 0.40.
- **Flip:** 87.4.

## 68b61341c7 (ADA)
- **Rule check:** Not broken. Closes since last week were 86.2 to 100, above 83.9.
- **Read:** Higher lows at 63, 68, 77 and 84 within a volatile uptrend. Resistance is near 102–113.
- **Weight:** Kept at 0.60.
- **Flip:** 83.9.

## 97b74c357b (ETH)
- **Rule check:** Not broken. Closes since last week were 91.4 to 100, above 89.0.
- **Read:** A breakout from the 70–72 base, followed by a 90–96 shelf and now a push to 100 on light volume.
- **Weight:** Kept at 0.50.
- **Flip:** 89.0.

{"328c5ffde7 (XRP)": {"weight": 0.5, "flip": 88.5}, "032bf91ed3 (AVAX)": {"weight": 0.6, "flip": 61.9}, "4b0f26aaa9 (SOL)": {"weight": 0.3, "flip": 87.1}, "4a3507fc71 (DOGE)": {"weight": 0.7, "flip": 91.6}, "554afddfdd (LINK)": {"weight": 0.4, "flip": 86.8}, "ba440ecf72 (BTC)": {"weight": 0.7, "flip": 93.2}, "00a24cb7d0 (DOT)": {"weight": 0.7, "flip": 84.1}, "b30a8b8c3e (LTC)": {"weight": 0.4, "flip": 87.4}, "68b61341c7 (ADA)": {"weight": 0.6, "flip": 83.9}, "97b74c357b (ETH)": {"weight": 0.5, "flip": 89.0}}

## Entscheidung 2026-09-27

**Strategy:** I apply last week's weight unless any daily close since that decision has broken the flip price. All ten windows are long positions, so the relevant break is a close below the flip. I only re-decide a window when its flip has been breached. When the hold rule applies, I carry the flip forward unchanged so the exit discipline stays consistent.

## f15041a3ee (ADA)
- **Market read:** The market crashed from about 98 to 56 (days -117 to -90), then made higher lows: 61, then 68, then 75. The current rally runs from 76.6 to about 100, with resistance at 101–104. Support sits at 91.5–93.5, then 76.
- **Flip check:** Last week's flip was 75.0. The lowest close in the past week was 93.5, so it held.
- **Decision:** Keep **0.60**. Flip stays at **75.0**.

## 5ed6d55dbd (DOT)
- **Market read:** After a long decline to about 59, there was a volume-driven spike to 98 on day -19, a pullback to 74.5, and a rebound to 100. Highs are near 101–103. Support is at 85–87, then 74.5.
- **Flip check:** The flip was 75.3. The lowest close this week was 86.9, so it held.
- **Decision:** Keep **0.70**. Flip stays at **75.3**.

## d802cf23ba (SOL)
- **Market read:** The market is in a steady uptrend from about 61 to 100 since day -40, with higher lows at 79.4, 92.6 and 98.2. It is now at the prior range top near 100–102.
- **Flip check:** The flip was 79.4. The lowest close this week was 94.3, so it held.
- **Decision:** Keep **0.30**. Flip stays at **79.4**.

## c220895137 (LTC)
- **Market read:** There was a climactic volume bar on day -3 (6.7x average) that took price from 87 to 101. Price is holding 99.5–101.8 since then. Support is at 86.5, then 72.
- **Flip check:** The flip was 72.0. The lowest close this week was 86.8, so it held.
- **Decision:** Keep **0.40**. Flip stays at **72.0**.

## d30ee5e989 (AVAX)
- **Market read:** A breakout on very heavy volume ran from about 70 to 104 (days -9 to -7). Price pulled back to 92.4 and recovered to 100. The resistance band is 104–108.
- **Flip check:** The flip was 64.2. The lowest close this week was 93.6, so it held.
- **Decision:** Keep **0.60**. Flip stays at **64.2**.

## 319f66a678 (DOGE)
- **Market read:** Price spiked to 109 on day -5, retraced to 94, and is now consolidating at 98–102. Support is at 94, then 81–83.
- **Flip check:** The flip was 82.5. The lowest close this week was 95.7, so it held.
- **Decision:** Keep **0.70**. Flip stays at **82.5**.

## 1072c27361 (XRP)
- **Market read:** Price is making higher highs at 106 and 109 in a volatile range of 97.5–109. Support is at 97.5, then 82–85.
- **Flip check:** The flip was 82.3. The lowest close this week was 99.0, so it held.
- **Decision:** Keep **0.50**. Flip stays at **82.3**.

## 056561e4b9 (LINK)
- **Market read:** The uptrend has run from about 58 to 101, with higher lows at 75.7 and 86. It is at new highs near 103.
- **Flip check:** The flip was 77.5. The lowest close this week was 88.1, so it held.
- **Decision:** Keep **0.40**. Flip stays at **77.5**.

## f2fdcdd3ab (ETH)
- **Market read:** After a breakout at 84–94, price is in a tight base at 99–101 on drying volume. The high is 104.4. Support is at 96.7, then 87.7.
- **Flip check:** The flip was 87.6. The lowest close this week was 99.9, so it held.
- **Decision:** Keep **0.50**. Flip stays at **87.6**.

## 22f1cd0e5d (BTC)
- **Market read:** Price is in a stair-step uptrend and is now coiling at 99–100 under the 103.5 high. Support is at 98, then 88.7–89.5.
- **Flip check:** The flip was 89.6. The lowest close this week was 99.6, so it held.
- **Decision:** Keep **0.70**. Flip stays at **89.6**.

{"f15041a3ee (ADA)": {"weight": 0.6, "flip": 75.0}, "5ed6d55dbd (DOT)": {"weight": 0.7, "flip": 75.3}, "d802cf23ba (SOL)": {"weight": 0.3, "flip": 79.4}, "c220895137 (LTC)": {"weight": 0.4, "flip": 72.0}, "d30ee5e989 (AVAX)": {"weight": 0.6, "flip": 64.2}, "319f66a678 (DOGE)": {"weight": 0.7, "flip": 82.5}, "1072c27361 (XRP)": {"weight": 0.5, "flip": 82.3}, "056561e4b9 (LINK)": {"weight": 0.4, "flip": 77.5}, "f2fdcdd3ab (ETH)": {"weight": 0.5, "flip": 87.6}, "22f1cd0e5d (BTC)": {"weight": 0.7, "flip": 89.6}}
