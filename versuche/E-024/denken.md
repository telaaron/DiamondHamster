# E-024: was die KI gedacht hat (Set A)

Volle Antwort des Deciders pro Entscheidungswoche, unverändert. Er sah weder Datum noch Coin-Namen; die Namen in Klammern sind erst danach eingesetzt. Gesendeter Prompt und Daten: runs/<set>/<woche>/requests.json.

## Entscheidung 2026-07-05

**1. Strategy**

I follow the trend and want structure to confirm it. A window gets meaningful weight only if price has made higher lows and reclaimed the level where it broke down. When price sits below a falling medium-term trend and is still making lower lows, I stay mostly flat and keep only a small stake for the bounce. Open interest adjusts the weight: a high percentile with rising OI in a downtrend means crowded leverage, so I cut weight, while low or falling OI means positioning has been flushed, so I allow a bit more.

**2. Windows**

**d878df8da1 (AVAX)**
- **Read:** Long downtrend from about 210. The 125–145 range broke at day -33, with capitulation lows at 82 (day -16, 3x volume).
- **Structure:** Rising lows since then: 86, 92, 95.5. Price has reclaimed 100 and sits just under resistance at 102–103. The next resistance is 112–116.
- **Open interest:** Low at the 22nd percentile and down 9%, so leverage has been flushed.
- **Weight:** 0.3, an early base still below the medium-term trend.
- **Change my mind:** Below 92 I go flat. Above 103 I add.

**c80a06a508 (XRP)**
- **Read:** The 113–128 range broke to 92. The bounce failed at 111.8, then price made a lower low at 87.2 (day -9). It has rallied back to 100.
- **Levels:** Resistance at 102 and 107–112.
- **Open interest:** 94th percentile and up 9%, so leverage is crowded into a downtrend.
- **Weight:** 0.15.
- **Change my mind:** Below 88 I go flat. Above 107 I add.

**61070d3df6 (ETH)**
- **Read:** Double bottom at about 84.5 (days -29 and -9). Price has rallied to 100, under resistance at 103.6. The prior range was 110–120.
- **Open interest:** 88th percentile and flat over 4 weeks.
- **Weight:** 0.2.
- **Change my mind:** Below 87 I go flat. Above 104 I add.

**f6235111be (LINK)**
- **Read:** Double bottom at about 87 (days -29 and -10). Price is at 100, with resistance at 106.7 and the 112–120 breakdown zone above.
- **Open interest:** Neutral at the 48th percentile.
- **Weight:** 0.25.
- **Change my mind:** Below 88 I go flat. Above 107 I add.

**d3a53f8905 (ADA)**
- **Read:** The worst breakdown, 125 to 73, with a lower low on day -10. That was followed by a vertical 35% rally in five days on heavy volume, rejected at 105.5.
- **Levels:** The old breakdown zone, 110–122, is far above.
- **Open interest:** 99th percentile and up 9%, so the rally is leverage-driven and fragile.
- **Weight:** 0.15.
- **Change my mind:** Below 92 I go flat. A close above 106 would raise it.

**2b0414cdc8 (LTC)**
- **Read:** Low at 85.7 (day -10). A grinding recovery is now testing the 100–101 highs from days -20 to -19. Day 0 closed near its high.
- **Levels:** The breakdown range of 110–115 is next.
- **Open interest:** 40th percentile with a modest increase, so positioning is healthy.
- **Weight:** 0.3.
- **Change my mind:** Below 91 I cut. Above 102 I add.

**528ef10d70 (BTC)**
- **Read:** Lows at 92.9, 91.3 and 90.8, so a flat-to-lower base. Price is at 100, under resistance at 104–106. The prior range was 115–128.
- **Open interest:** 95th percentile, crowded.
- **Weight:** 0.15.
- **Change my mind:** Below 90.5 I go flat. Above 106 I add.

**71aa8f728b (DOT)**
- **Read:** A persistent pattern of lower highs and lower lows: 100.3, then 93, then 90.2 (day -7). The bounce to 100 sits well under the lower high at 118.8 (day -20).
- **Open interest:** 66th percentile and up 7%.
- **Weight:** 0.1, the downtrend is intact.
- **Change my mind:** Below 90 I go flat. Above 105 I add.

**4391487662 (SOL)**
- **Read:** The strongest structure here. The low was 73.7 (day -29), followed by a higher low at 78.5 (day -10). Price broke through 93 resistance and is now back at the pre-crash range of about 100–106. It is reclaiming the breakdown level.
- **Open interest:** 73rd percentile and only up 2%, so not building aggressively.
- **Weight:** 0.5.
- **Change my mind:** Below 92 I cut. Holding above 106 lets me add more.

**8d82a8f2bc (DOGE)**
- **Read:** The 125–150 range broke to 99.7. The bounce failed at 118.7, then price made a lower low at 89.3 (day -5). It is back at 100, under resistance at 102–108.
- **Open interest:** Up 16% to the 86th percentile, so leverage is piling into a downtrend.
- **Weight:** 0.1.
- **Change my mind:** Below 89 I go flat. Above 108 I add.

**3. Weights**

{"d878df8da1 (AVAX)": 0.3, "c80a06a508 (XRP)": 0.15, "61070d3df6 (ETH)": 0.2, "f6235111be (LINK)": 0.25, "d3a53f8905 (ADA)": 0.15, "2b0414cdc8 (LTC)": 0.3, "528ef10d70 (BTC)": 0.15, "71aa8f728b (DOT)": 0.1, "4391487662 (SOL)": 0.5, "8d82a8f2bc (DOGE)": 0.1}

## Entscheidung 2026-07-12

**1. Strategy.** I only add exposure when the structure since the latest crash has turned up, meaning a higher low followed by a higher high. Otherwise the position stays small, because every window is in a large downtrend from 150–270 down to 100. Open interest adjusts the weight: rising or high-percentile OI in a downtrend means crowded leverage, so I cut the weight. Low OI after a flush means leverage has been cleared, so I give a small boost.

**2. Windows**

**f9394b6e1f (LINK)**
- **Read:** Downtrend from 176. The highs keep falling: 135.9, 107.5, then 102.2. The lows at 87.5 and 87.7 form a double bottom, and price now sits in a 97–102 range. OI is neutral (pct 32).
- **Weight 0.2:** The base may be holding, but nothing has broken out yet.
- **Change my mind:** A close above 103 raises the weight; below 94 I go flat.

**a722570ab5 (XRP)**
- **Read:** Lower highs (142.7, 119.1, 109.1) and lower lows (96.7, then 92.9). The bounce to 109 has faded back to 100. OI pct 84 is crowded.
- **Weight 0.1:** Downtrend with leverage still high.
- **Change my mind:** Above 109.5 raises the weight; below 96 I go flat.

**840c466a3e (DOT)**
- **Read:** Fell from 270. The lows keep dropping (104.7, then 94.2), and the 106–107.6 area has capped price twice. OI is up 18% to pct 71 while price falls.
- **Weight 0.1:** The trend is down, and new leverage is piling in.
- **Change my mind:** Above 107.6 raises the weight; below 96 I go flat.

**c7505006dd (LTC)**
- **Read:** A range of 89.3–105.3 after the drop. The low at 89.3 slightly undercut 92.1, and the highs stand at 105.3 and 104.9. OI is up 12% but at a moderate percentile (41).
- **Weight 0.2:** Price is mid-range with no confirmed reversal.
- **Change my mind:** Above 105.5 raises the weight; below 93 I go flat.

**2591dd5ae3 (ADA)**
- **Read:** After a low at 85.3, a squeeze ran to 123.4 and has been fully retraced to 100. OI is up 31% at pct 97, the most crowded window here, and the rally failed.
- **Weight 0.0:** The flush risk is high.
- **Change my mind:** A reclaim above 118 would make me reconsider.

**d3d8addf28 (AVAX)**
- **Read:** The low came at 88.7. Since then the lows have risen (93, 98.6), inside a 97–111 range. OI is down 13% at pct 4, so leverage has been flushed. Today price tested 98 and closed at 100.
- **Weight 0.3:** Clean positioning and higher lows, but no higher high yet.
- **Change my mind:** Above 111 raises the weight; below 97 I go flat.

**54f8b64fee (ETH)**
- **Read:** A double bottom at 83.3 and 83.7, followed by a recovery to 100–101.5. It is pressing on the 102.4 high. OI pct 92 is crowded.
- **Weight 0.2:** The structure is improving, but leverage is heavy.
- **Change my mind:** Above 102.5 raises the weight; below 95 I go flat.

**4757d2eab7 (DOGE)**
- **Read:** Lower lows (106.8, then 95.6) and lower highs (127.2, then 109.2). OI is up 11% at pct 87.
- **Weight 0.1:** Downtrend with crowded leverage.
- **Change my mind:** Above 109.5 raises the weight; below 97 I go flat.

**18c99a229c (BTC)**
- **Read:** Lows at 92.7 and 90.6, and highs at 105.5 and 101.4, so it is still making lower highs. Price is in a tight coil at 100. OI pct 73.
- **Weight 0.15:** No trend signal yet.
- **Change my mind:** Above 105.5 raises the weight; below 96 I go flat.

**81e989e354 (SOL)**
- **Read:** This is the only window with a higher low (78.2, then 83.3) and a higher high (109.2 above the earlier 98.9). Price has pulled back to 100. OI is down 12% at pct 6, so leverage has been washed out.
- **Weight 0.5:** The structure has turned up and positioning is clean.
- **Change my mind:** Below 96 I go flat; above 109.5 I go higher.

**3. Weights**

{"f9394b6e1f (LINK)": 0.2, "a722570ab5 (XRP)": 0.1, "840c466a3e (DOT)": 0.1, "c7505006dd (LTC)": 0.2, "2591dd5ae3 (ADA)": 0.0, "d3d8addf28 (AVAX)": 0.3, "54f8b64fee (ETH)": 0.2, "4757d2eab7 (DOGE)": 0.1, "18c99a229c (BTC)": 0.15, "81e989e354 (SOL)": 0.5}

## Entscheidung 2026-07-19

1. **Strategy.** All ten windows show a long downtrend from roughly 140–230 down to 100, with a capitulation leg about 45 days ago. The rule: build a long position only where the last 4–6 weeks show a base, meaning a double bottom or higher lows plus a break of the bounce high. Size down in proportion to how much leveraged open interest is building into an unresolved downtrend. Low open-interest percentile after a flush is a mild positive; high and rising open interest while lower highs persist is a negative.

2. **Windows**

**c209eade7b (ADA)**
- **Read:** The trend went from 220 to 100. The crash low was 89 (day -43), followed by a lower low at 83 (day -24).
- **Structure:** A sharp squeeze to 120 (day -15) fully faded back to 100. The range is 93–105 and price is mid-range in a broken trend.
- **Open interest:** 87th percentile and up 11%, so leverage is crowding in.
- **Weight:** 0.2, a small probe only.
- **Change my mind:** A close above 110 would raise the weight; below 93 I go flat.

**5527ba19c3 (LTC)**
- **Read:** The trend went from 145 to 100. Lows were 86 (day -43) and 83.5 (day -24), followed by steadily higher lows: 87, 91, 92.
- **Structure:** Day -1 pushed through the 98–98.5 resistance on above-average volume. Price is above its roughly 30-day mean and the base is constructive.
- **Open interest:** 64th percentile, up 17%, which is moderate.
- **Weight:** 0.5.
- **Change my mind:** A close below 91 means a failed breakout, so I go flat. Above 104 I add.

**1f80032dfc (BTC)**
- **Read:** The trend went from 138 to 100. Lows were 91.4 and 89.8, then higher lows at 95.5 and 96.6.
- **Structure:** Price is in a 90–104 range and the bounce high at 104 has not been broken.
- **Open interest:** 71st percentile, up 4%, which is neutral.
- **Weight:** 0.3.
- **Change my mind:** A close above 104.5 would raise the weight; below 95 I go flat.

**4ff050698e (SOL)**
- **Read:** The trend went from 165 to 100. The capitulation low was 78.7, followed by a higher low at 83.8.
- **Structure:** A rally to 110 (day -15) broke the 99.6 bounce high. The pullback is holding 96–100, so the structure is higher highs and higher lows.
- **Open interest:** 12th percentile and down 11%, so leverage is flushed and the move looks cleaner.
- **Weight:** 0.45.
- **Change my mind:** Below 96 I cut. A close above 104 lets me add.

**d86d5f9ef8 (ETH)**
- **Read:** The trend went from 157 to 100. There is a double bottom at 80.4/80.8, followed by higher lows: 83, 92, 93.5, 96.3.
- **Structure:** The neckline is about 99. It broke at day -5, the move ran to 104, and price is now retesting about 98–100.
- **Open interest:** 81st percentile, up 4%, which is somewhat elevated.
- **Weight:** 0.5.
- **Change my mind:** A close below 96 means the retest failed, so I go flat.

**1273f16f00 (AVAX)**
- **Read:** The trend went from 187 to 100. The low was 87.9 (day -30), followed by higher lows at about 92, 97.7 and 98.
- **Structure:** Price is in a 98–110 range. Day 0 tested 98.9 and held.
- **Open interest:** 11th percentile and down 33%, a large deleveraging flush, which is supportive.
- **Weight:** 0.4.
- **Change my mind:** Below 97 I go flat. Above 106 I add.

**ff9867a4cc (DOT)**
- **Read:** This is the steepest trend, from 231 to 100. Lower highs run 127.7, then 110.7, then 106.
- **Structure:** Lows are 97–98. Day 0 closed weak near the bottom of its range.
- **Open interest:** 91st percentile and up 26%, so heavy leverage is building into a downtrend.
- **Weight:** 0.1.
- **Change my mind:** Above 109 I reconsider. A break below 97 confirms the continuation lower.

**ca2420940d (DOGE)**
- **Read:** The trend went from 163 at day -66 down to 100. Lower highs run 127.7, 109.6, 104.1.
- **Structure:** The floor is 96–98. This is a descending compression on dying volume (0.16–0.19).
- **Open interest:** 88th percentile and up 24%, so leverage is coiling at support.
- **Weight:** 0.15.
- **Change my mind:** Below 96 I go flat. Above 105 is a breakout from the compression, so I raise the weight.

**8f93fe56c8 (XRP)**
- **Read:** The trend went from 172 to 100. Lows were 95.7 and 91.9, then higher lows at 93, 96 and 97.4.
- **Structure:** The highs are falling too: 117.8, 107.9, 103. That makes a symmetric triangle around 97–103.
- **Open interest:** 94th percentile, which is crowded.
- **Weight:** 0.2.
- **Change my mind:** Above 103.5 I raise the weight; below 96.5 I go flat.

**f3a6a0860e (LINK)**
- **Read:** The trend went from 145 to 100. There is a double bottom at 83.4/83.6, followed by higher lows: 84.4, 89.7, 93, 95.5.
- **Structure:** Price broke the 97.6–102.6 area to reach 103 and is now holding about 98–100.
- **Open interest:** 23rd percentile, up 8%, so leverage is light.
- **Weight:** 0.55.
- **Change my mind:** Below 95 I cut. Above 104 I add.

3. **Weights**

{"c209eade7b (ADA)": 0.2, "5527ba19c3 (LTC)": 0.5, "1f80032dfc (BTC)": 0.3, "4ff050698e (SOL)": 0.45, "d86d5f9ef8 (ETH)": 0.5, "1273f16f00 (AVAX)": 0.4, "ff9867a4cc (DOT)": 0.1, "ca2420940d (DOGE)": 0.15, "8f93fe56c8 (XRP)": 0.2, "f3a6a0860e (LINK)": 0.55}

## Entscheidung 2026-07-26

**1. Strategy**

I go long in proportion to how intact the recovery from the most recent crash low is. That means a series of higher lows, price retaking the breakdown zone, and no string of lower highs. I cut the weight when perpetual open interest is crowded, meaning a high percentile, and especially when open interest is rising while price is flat or falling. Price below the latest swing low is a stop-level signal to go flat.

**2. Windows**

**b2dfe328e4 (ETH)**
- **Read:** The asset fell from 154 into a 100–125 range, then broke down. It crashed to 77 around day −51, with a retest at 77.4 around day −30. Since then it has made steady higher lows (87.7, 89.5, 92.2, 94.5) and is now back at 100. Resistance is 100–103, where the breakdown on day −55 started.
- **Positioning:** Open interest is crowded (93rd percentile) but flat over 4 weeks (+2%).
- **Weight 0.5:** The recovery structure is clean, but price sits at resistance and positioning is crowded.
- **Change of mind:** A close below 94.5 ends the higher-low sequence and would take me flat. A close above 103 would let me add.

**2ddad81611 (LTC)**
- **Read:** The crash low was 84.7 on day −50, then 82.1 on day −31. Higher lows since: 86, 90.2, 95.6. Price is pressing the 100–101 ceiling, and above that the old breakdown zone is 106–108.
- **Positioning:** Open interest is moderate (58th percentile), up 15% over 4 weeks, so the buildup comes from neutral levels.
- **Weight 0.6:** This is the best recovery structure with healthy positioning.
- **Change of mind:** A close below 95.6.

**05173dc0e6 (SOL)**
- **Read:** After the crash to 78.3, price rallied strongly to 109.4 on day −22. It has since pulled back into a range of 95.6–103 with slightly lower highs (107.9, 103.0, 102.8).
- **Positioning:** Open interest is low (16th percentile) and falling (−12%). Leverage has been flushed out, which is a constructive backdrop.
- **Weight 0.5:** The base is constructive, but the range is not yet resolved.
- **Change of mind:** A close below 95.5 means flat. A close above 103 would raise the weight toward 0.8.

**c17f9fd6b9 (XRP)**
- **Read:** The low was 90.7 on day −30, followed by a rally to 106.4 and a range of 96–104.6 since. Price is still far below the 115–135 range that held before the drop.
- **Positioning:** Open interest is high (87th percentile) though easing (−6%).
- **Weight 0.4:** The asset is range-bound mid-range and positioning is crowded.
- **Change of mind:** A close below 96 means flat. A close above 104.6 would make me add.

**5da6cb326a (LINK)**
- **Read:** The double bottom is around 79.3–79.4 (days −50 and −31). Higher lows since: 85.2, 88.3, 90.7, 93.7. Today's high of 100.2 is the highest level since day −55, so price is breaking out of its post-crash structure. The next resistance is 102–104.
- **Positioning:** Open interest is neutral (55th percentile), up 9%.
- **Weight 0.6:** Uptrend structure with a breakout and neutral positioning.
- **Change of mind:** A close below 93.7.

**f81e52aa8b (BTC)**
- **Read:** There is a clean higher-low sequence from 88.9 (day −31) through 94.4 and 95.6 to 96.5. The recent high was 102.4 on day −5. The pre-crash level was around 112.
- **Positioning:** Open interest is extremely crowded (97th percentile) and still rising (+4%), so a long squeeze is a real risk.
- **Weight 0.45:** The structure is good, but positioning is stretched.
- **Change of mind:** A close below 96.5.

**a57e730ab2 (AVAX)**
- **Read:** The asset crashed from 133 to 92, then made a low of 84.2 on day −37. Since then it has ranged between 91 and 105.5 with lower highs (105.5, 101.3, 99.9). On day −3 it flushed to 91.0, and on day −1 it jumped to 100.5 on 1.5× volume. That is a reclaim, but it remains inside a choppy range.
- **Positioning:** Open interest is crowded (91st percentile) and rising (+7%).
- **Weight 0.4:** There is no clear trend and positioning is crowded.
- **Change of mind:** A close below 91 means flat. A close above 102 would make me add.

**9821c9395a (ADA)**
- **Read:** The asset is in a severe long-term decline from 217. The spike to 120.5 on day −22 failed completely. Since then price has ranged between 96 and 109 with lower highs (120.5, 108.9).
- **Positioning:** Open interest is crowded (93rd percentile).
- **Weight 0.3:** The bounce failed, the trend is down, and leverage is high.
- **Change of mind:** A close below 96.8 means flat. A close above 109 would raise the weight.

**b436bcfb5f (DOT)**
- **Read:** The asset fell from 226 to 100 in a persistent downtrend. Since day −31 it has ranged between 95 and 109.7 with lower highs (109.7, 108.1, 105.6, 105.0).
- **Positioning:** Open interest is up 18% to the 92nd percentile while price goes nowhere, so leverage is building into weakness.
- **Weight 0.2:** Downtrend, lower highs, and crowded positioning.
- **Change of mind:** A close below 95 means flat. A close above 106 breaks the lower-high pattern.

**083989a3d7 (DOGE)**
- **Read:** Price has declined steadily from 161.6 on day −73. It ranges between 92.9 and 108.2 with a clear series of lower highs (108.2, 107.4, 103.0, 102.7). On day −3 it dropped to 93.2 and then bounced.
- **Positioning:** Open interest is up 35% to the 89th percentile. That is heavy leverage piling into a falling market, which is fuel for a flush lower.
- **Weight 0.2:** Downtrend with leverage building into it.
- **Change of mind:** A close below 92.9 means flat. A close above 103 would let me reconsider.

```json
{"b2dfe328e4 (ETH)": 0.5, "2ddad81611 (LTC)": 0.6, "05173dc0e6 (SOL)": 0.5, "c17f9fd6b9 (XRP)": 0.4, "5da6cb326a (LINK)": 0.6, "f81e52aa8b (BTC)": 0.45, "a57e730ab2 (AVAX)": 0.4, "9821c9395a (ADA)": 0.3, "b436bcfb5f (DOT)": 0.2, "083989a3d7 (DOGE)": 0.2}
```

## Entscheidung 2026-08-02

**1. Strategy.** I go long in proportion to how intact the medium-term structure is. A sequence of higher lows and higher highs off the most recent major low earns weight. Persistent lower highs earn little. Open interest is a crowding filter: rising OI or a percentile above 90 into a flat or falling tape cuts the weight, and washed-out OI (low percentile, falling) adds a little.

**2. Windows**

**2fbaad498c (DOGE)**
- **Read:** Steady decline from 165 (day -80) to the 100 area. The last 40 days are a drifting range of 96–110 with lower highs (112, 106.7, 104.6). Day 0 bounced from 97.6 on very low volume.
- **OI:** +14% at the 86th percentile, so leverage is building while price stalls. That makes a flush likely.
- **Weight: 0.1.**
- **Change my mind:** a close above 106.

**20aa109c3c (ADA)**
- **Read:** Crash from 132 to 73 (day -38). A squeeze to 105.5 was followed by a pullback that held 81–82. Day 0 broke out to 100 on 1.7x volume, the top of the 30-day range.
- **OI:** at the 100th percentile, which is maximum crowding, so a long squeeze could reverse it fast.
- **Weight: 0.35.**
- **Change my mind:** above 105.5 confirms and would raise it. Below 85 means exit.

**a305ed2a32 (LINK)**
- **Read:** Fell from 129 to 83.4, then recovered into a range of 94–106. Lows are rising (83.6 → 89.7 → 94.1), but the range top at 105.5 is unbroken.
- **OI:** neutral (43rd percentile).
- **Weight: 0.4.**
- **Change my mind:** above 106 raises it. Below 94 cuts it.

**31010a54de (LTC)**
- **Read:** Decline from 135 to 88, then higher lows at 88, 96 and 97.6. Range of 97–108 for the last 3 weeks; day 0 is at mid-range, 100.
- **OI:** low-ish (37th percentile), flat.
- **Weight: 0.45.**
- **Change my mind:** below 97 means cut. Above 108 means add.

**9b0e3692ba (XRP)**
- **Read:** Down from 139 to 93. Since then the highs keep falling: 119, 109, 107. Lows are holding around 96 in a compressing range.
- **OI:** -11%, so deleveraging and neutral.
- **Weight: 0.3.**
- **Change my mind:** above 107 means add. Below 96 means flat.

**2d1f8a5b15 (BTC)**
- **Read:** Down from 130 to 91, then a recovery into a tight range of 98–105.
- **OI:** at the 98th percentile while price goes sideways, which is crowded positioning without progress.
- **Weight: 0.3.**
- **Change my mind:** above 105.5 means add. Below 98 means flat.

**7554ec6f53 (AVAX)**
- **Read:** Collapse from 160 to 86.7 (day -44), then a range of 92–108. Day -1 swept to 92.2 and day 0 reversed strongly to 100 on above-average volume.
- **OI:** at the 17th percentile, so positioning is light.
- **Weight: 0.4.**
- **Change my mind:** below 92 means flat. Above 108 means add.

**ef12c99f8b (SOL)**
- **Read:** Crash to 81.7, then a strong rally to 114. It has since faded with lower highs (114 → 107 → 104.7) back to support at 98–100.
- **OI:** -16% at the 6th percentile, very washed out, which offsets the weak tape.
- **Weight: 0.35.**
- **Change my mind:** below 95.9 means flat. Above 107 means add.

**f9a625c605 (DOT)**
- **Read:** Persistent downtrend from 208 to 93, with lower highs at 131, 113.6, 109 and 104. Day -6 broke down to 93.6; day 0 is only a weak bounce.
- **OI:** +21% at the 95th percentile, so leverage is piling into a falling tape.
- **Weight: 0.1.**
- **Change my mind:** a close above 110.

**65945ad16b (ETH)**
- **Read:** Low at 79.9 (day -57), then the cleanest recovery of the set. Higher lows at 80.2, 92.5 and 96.6, and higher highs at 97.2, 103.2, 104.3 and 105.1. Now pulling back to 100 inside the uptrend.
- **OI:** neutral (69th percentile).
- **Weight: 0.55.**
- **Change my mind:** below 96.5 means cut. Above 105 means add.

**3. Weights**

{"2fbaad498c (DOGE)": 0.1, "20aa109c3c (ADA)": 0.35, "a305ed2a32 (LINK)": 0.4, "31010a54de (LTC)": 0.45, "9b0e3692ba (XRP)": 0.3, "2d1f8a5b15 (BTC)": 0.3, "7554ec6f53 (AVAX)": 0.4, "ef12c99f8b (SOL)": 0.35, "f9a625c605 (DOT)": 0.1, "65945ad16b (ETH)": 0.55}

## Entscheidung 2026-08-09

1. **Strategy:** I go long when structure is constructive: higher lows after a capitulation, and price holding above recent support. I cut exposure when the window shows lower highs or a persistent downtrend. A high open-interest percentile with flat or falling price means crowded leverage and liquidation risk, so it lowers my weight; low open interest is neutral to mildly supportive.

## a697b015a1 (LTC)
- **Read:** The asset ranged at 115–133, then crashed from about -68 to -64 to a low of 89. The bottom held at 86.5 on day -46. Since then the lows have risen: 95 (-32), then 96 (-8). Price rallied to 105–106 (days -22 to -14) and is now consolidating at 97–102 on falling volume. Open interest is low (25th percentile) and falling, so leverage is not crowded.
- **Weight 0.5:** A constructive base under resistance at 105–106.
- **Change mind:** I go flat below 96, and add above 106.

## cb6d98fc15 (SOL)
- **Read:** Price crashed to 78.8 and rebounded to 110 (-37). Since then the highs have fallen: 108.5, 103.6, 101.1. Price bounced from 92.5 (-8) to 100 now. Open interest is low (16th percentile).
- **Weight 0.3:** The bounce sits inside a sequence of lower highs.
- **Change mind:** A close above 103.5 turns this constructive; below 92.5 I go flat.

## 27d0be11fe (BTC)
- **Read:** Price crashed from the 120s to 91, bottomed at 89.5 (-45), and has chopped between 96 and 103 for about a month. The lows are rising slightly. Open interest is at the 93rd percentile and up 6%, so leverage is building while price goes nowhere.
- **Weight 0.3:** Crowded positioning in a flat range.
- **Change mind:** I add on a break above 103.2; below 96 I go flat.

## 06f02e5855 (AVAX)
- **Read:** Price fell in two legs from about 140 to 88.5 (-51), rebounded to 110.8, and since then has ranged between 94 and 109 with slightly lower highs. Open interest is low (11th percentile).
- **Weight 0.4:** A neutral range at mid-range.
- **Change mind:** Below 94 I go flat; above 109 I add.

## 15a874da84 (DOT)
- **Read:** A persistent downtrend from above 200 to 100. The highs keep falling: 131, 113.6, 108.9 (-5). The latest low is 93.6 (-13). Open interest is at the 92nd percentile and up 15% while price falls.
- **Weight 0.1:** A clear downtrend with heavy leverage building into it.
- **Change mind:** Only a break above 109 makes me more constructive.

## 0d87186f15 (ETH)
- **Read:** A double bottom at 78.8 and 79.1 (-44). Since then the lows have risen steadily: 89.7, 91.6, 94.4, 95.4. Price is consolidating at 97–101, under a high of 103.7. Open interest is at the 77th percentile, with a flat 4-week change.
- **Weight 0.6:** The cleanest higher-low structure in this set.
- **Change mind:** Below 95.4 I go flat.

## 3ffad73fa7 (ADA)
- **Read:** Price crashed to 71 (-45), spiked to 102.8, faded to 79 (-13), then rallied hard to 108.8 (-3). It was rejected there and is now at 100. The low at 79 is higher than the low at 71, but price has twice failed in the 102–109 zone. Open interest is at the 97th percentile and up 9%, so the rally is leverage-driven.
- **Weight 0.35:** The upward structure is offset by crowded positioning and resistance overhead.
- **Change mind:** Below 95.6 I go flat; a hold above 105 lets me add.

## 3d95db531e (LINK)
- **Read:** A double bottom around 85.5 (-65 and -45), then higher lows at 91.9 and 96.3. Price rallied to 108.9 (-13) and is now consolidating at 98–104. Open interest is at the 74th percentile.
- **Weight 0.5:** A constructive base.
- **Change mind:** Below 96 I go flat; above 105 I add.

## 5c2d754107 (XRP)
- **Read:** After the crash low at 102, the highs keep falling: 125.6, 115, 113.1, 108.4, 106.2. Price is now at 100, near the recent low of 98.3. Open interest is at the 83rd percentile.
- **Weight 0.2:** A descending structure pressing on support.
- **Change mind:** Below 98 I go flat; above 106 I add.

## c9a34b4998 (DOGE)
- **Read:** A downtrend from 171 (-87) to 100. Since the rally to 114.5, the highs keep falling: 109, 106.8, 103.2. Support sits at 97.6–98.3, so this is a descending triangle. Open interest is at the 88th percentile and up 15%.
- **Weight 0.2:** Bearish compression with leverage building.
- **Change mind:** Below 97.6 I go flat; above 106.8 I turn constructive.

{"a697b015a1 (LTC)": 0.5, "cb6d98fc15 (SOL)": 0.3, "27d0be11fe (BTC)": 0.3, "06f02e5855 (AVAX)": 0.4, "15a874da84 (DOT)": 0.1, "0d87186f15 (ETH)": 0.6, "3ffad73fa7 (ADA)": 0.35, "3d95db531e (LINK)": 0.5, "5c2d754107 (XRP)": 0.2, "c9a34b4998 (DOGE)": 0.2}

## Entscheidung 2026-08-16

**1. Strategy**

I go long only when the trend has turned up: price is above its roughly 50-day mean, recent lows are higher, and price is breaking out of a range rather than drifting inside one. Persistent downtrends with lower highs get 0 regardless of other factors. High open-interest percentile reduces the weight, especially when it rises while price falls or stalls, because crowded leverage tends to unwind against price. Low open interest makes me slightly more willing to hold a base.

**2. Windows**

**cfcac03078 (XRP)**
- **Read:** Steady downtrend from 148 to 100. Lower highs at 130 (-62), 117 (-43) and 117 (-26). The last two weeks are a slow grind down from 109 to 100 on falling volume.
- **Open interest:** +18% to the 99th percentile while price falls. Leverage is building into weakness, which raises the risk of a flush below 99.
- **Weight:** 0.0.
- **Change my mind:** a close above 112, which reclaims the last month's range highs.

**6f496048d0 (LINK)**
- **Read:** Crashed to 75 at -72, built a base at 77–92, then broke out of an 85–90 range. Price reached 100 with a spike to 103.8 on day -1. It is now above the 50-day mean (~87) with higher lows at 75, 77, 84 and 87, so the trend has turned up.
- **Open interest:** +53% in 4 weeks, at the 100th percentile. The breakout is being chased with heavy leverage, so a shakeout back toward 93 is likely.
- **Weight:** 0.4. I am long the trend change but sized down for crowding.
- **Change my mind:** a close below 92 means the breakout failed, and I go flat.

**7675848791 (DOGE)**
- **Read:** Topped at 165–170 (-94) and fell to 100. The last 35 days are a very tight range of 98–106 on dying volume. This is a base, but inside a dominant downtrend.
- **Open interest:** 90th percentile, +18%. Leverage is building into a flat market.
- **Weight:** 0.1.
- **Change my mind:** a close above 106.5, the range top, would lift me to 0.4. Below 98, I go to 0.

**0a2e8f7019 (DOT)**
- **Read:** Long decline from 220 to 100. A bounce to 113 (-12) failed, and price has drifted down for 12 days with lower highs. Price is now at the 99–100 lows.
- **Open interest:** 97th percentile, which means crowded positioning into a downtrend.
- **Weight:** 0.0.
- **Change my mind:** a close above 113.

**50834b1ed4 (ETH)**
- **Read:** Crashed to 81, then recovered steadily. The lows run 81, 83, 97, 99, and price has spent the last 20 days in a 98–104 range. It sits above the 50-day mean (~96). The recovery is constructive, but momentum has stalled.
- **Open interest:** 95th percentile, but only +3% recently.
- **Weight:** 0.3.
- **Change my mind:** a close below 97 takes me to 0. A close above 105 takes me to about 0.6.

**2268f7511f (LTC)**
- **Read:** Crashed to 92 and rebounded to 108–109 (-29 to -21). It is now pulling back to 99–100, mid-range in 98–109. Price is roughly at the 50-day mean.
- **Open interest:** -7%, 46th percentile. Leverage is healthy and has been unwinding, not crowded.
- **Weight:** 0.3.
- **Change my mind:** a close below 98 takes me flat. A close above 109 takes me to 0.6.

**42a4ceb6bf (BTC)**
- **Read:** Crashed to 94 and recovered into a 99–106 range for about 40 days. Price is now at the bottom of that range at 100. The pre-crash range was 117–130.
- **Open interest:** 99th percentile, +10%. Leverage is crowded and price is sitting at support.
- **Weight:** 0.15.
- **Change my mind:** a close below 99 takes me to 0. A close above 106 takes me to 0.4.

**69e6aebc3c (SOL)**
- **Read:** Crashed to 80, rallied to 112 (-44), and faded to 96 (-15). Price is now at 100–102 with a minor higher low and a 96–105 range.
- **Open interest:** 12th percentile, -5%. Little leverage, so liquidation risk is low.
- **Weight:** 0.25.
- **Change my mind:** a close below 96 takes me to 0. A close above 105 takes me to 0.5.

**ec61a78d5a (AVAX)**
- **Read:** Fell from 160 to a capitulation low of 90 (-58). It has chopped in 97–110 for 50 days. Day -1 tried to push higher to 108.6 and was rejected back to 100, a bearish wick. There is no trend.
- **Open interest:** 11th percentile, flat. Not crowded.
- **Weight:** 0.2.
- **Change my mind:** a close below 96 takes me to 0. A close above 110 takes me to 0.5.

**85af48b4e4 (ADA)**
- **Read:** Crashed to 79 and made a higher low at 88 (-20). It rallied to 115–121 (-10), then fell nine sessions in a row back to 100. The structure of higher lows is intact, but short-term momentum is down, and the 50-day mean is near 98.
- **Open interest:** 83rd percentile, +5%.
- **Weight:** 0.15.
- **Change my mind:** a close below 89 takes me to 0. Reclaiming 110 takes me to 0.5.

**3. Weights**

{"cfcac03078 (XRP)": 0.0, "6f496048d0 (LINK)": 0.4, "7675848791 (DOGE)": 0.1, "0a2e8f7019 (DOT)": 0.0, "50834b1ed4 (ETH)": 0.3, "2268f7511f (LTC)": 0.3, "42a4ceb6bf (BTC)": 0.15, "69e6aebc3c (SOL)": 0.25, "ec61a78d5a (AVAX)": 0.2, "85af48b4e4 (ADA)": 0.15}

## Entscheidung 2026-08-23

1. **Strategy:** These windows all show the same setup: a slide from earlier highs, a crash around day −80, a quiet base, then a 25–50% surge over the last four days with a long upper wick on day −1. I add weight when the surge has reclaimed the pre-crash range or set new window highs, and when it is not crowded with leverage (low or falling open interest). I cut weight when heavy overhead supply sits just above 100, the longer-term trend is still lower highs, or open interest is near its highs. Day 0's low is usually the invalidation level.

2. **Windows**

**7ab869b6e4 (XRP)**
- **Read:** The pre-crash range was 85–100, then a crash to 69 and a long grind down to about 65.
  - The last four days went 66→100 on very heavy volume (6×) and wicked to 111.8 on day −1, which looks like a blow-off.
  - Price is back at the top of the old range (about 98–102 resistance).
  - Open interest is at the 84th percentile and flat over four weeks.
- **Weight: 0.35.** The thrust is strong, but the move is parabolic, met resistance and drew crowded positioning.
- **Change my mind:** below 94 I go flat; a close above 106 means more.

**6fa6f2ba4b (ADA)**
- **Read:** The longer-term trend is lower highs (130→124→88), with a crash to 61.
  - Since then the lows have risen (61, 68, 77), and price has now broken above the 88 and 93 highs.
  - The old breakdown zone at 104–110 sits overhead, and day −1 was rejected at 113.8.
  - Open interest fell 8% over four weeks and is at the 64th percentile, so the move may be partly short covering.
- **Weight: 0.45.**
- **Change my mind:** below 94 I go flat; above 110 I add.

**93ae5a2eb5 (SOL)**
- **Read:** The pre-crash range was 85–102. After the crash to 63, price recovered to 86 and based at 77–81.
  - It is now at 100, near the window high of 103.1, so it has reclaimed the whole range.
  - Open interest is at the 1st percentile and fell 11%, so the rally is not leverage-driven.
- **Weight: 0.7.** This is the cleanest structure, with the least crowding.
- **Change my mind:** below 92 (the breakout base); above 104 confirms.

**486a5b79d1 (AVAX)**
- **Read:** The pre-crash range was 115–138, then a crash to 75 and a base at 82–92.
  - Price is now 100 after a wick to 109, still well below the 115 breakdown level, so supply is heavy overhead.
  - Open interest fell 8% and is at the 61st percentile.
- **Weight: 0.4.**
- **Change my mind:** below 95; a close above 110 means more.

**5a0f995be0 (DOT)**
- **Read:** This is a persistent downtrend from 179 to 78. The last four days went 81→100.
  - Day −1 was rejected at 111.2, right at the 108–113 congestion zone (days −78 to −66).
  - Open interest is at the 41st percentile and fell 13%. Structure is the weakest of the set.
- **Weight: 0.3.**
- **Change my mind:** below 94; above 112 I would turn constructive.

**fa87e1c6c4 (LTC)**
- **Read:** The pre-crash range was 98–115, then a crash to 75 and recovery to about 90. The base was 84–88.
  - Price is now back at the lower edge of the old range (about 97–100), and day −1 wicked to 106.
  - Open interest is at the 65th percentile and flat.
- **Weight: 0.5.**
- **Change my mind:** below 96; above 106 I add.

**539229006e (LINK)**
- **Read:** The pre-crash range was 72–94, then a crash to 61.
  - Since −59 the lows have been rising, and price was already trending up (70→83) before the surge.
  - Price is now 100, above every prior high in the window (94.2), so this is a genuine breakout.
  - Open interest rose 21% and is at the 94th percentile, which is very crowded and creates flush risk.
- **Weight: 0.55.** The trend is strong, cut back for crowding.
- **Change my mind:** below 94 (back inside the old range); above 108 I add.

**4c4b4d6f8e (ETH)**
- **Read:** The pre-crash high was 100.1 and the range 80–100. After the crash to 61 and a base at 74–79, the price is back at the prior high.
  - Day −2 peaked at 103.4, and day −1 closed lower.
  - Open interest is at the 95th percentile, which is crowded.
- **Weight: 0.45.**
- **Change my mind:** below 95.5; a close above 104 confirms.

**7b72f257ab (BTC)**
- **Read:** The pre-crash range was 85–106. After the crash to 76, price recovered to 85 and based at 80–84.
  - The rally to 100 was orderly. Day −1 was a tight, low-volume consolidation with no blow-off wick, which is healthy.
  - Price is at the middle of the old range. Open interest is at the 80th percentile and flat.
- **Weight: 0.55.**
- **Change my mind:** below 97; above 106 I add.

**4aaba44a2e (DOGE)**
- **Read:** The pre-crash range was 95–127, then a crash to 74 and a long base at 73–80.
  - Price is now 100 after a wick to 107.9 on 3.5× volume. Overhead supply runs from 105 to 120.
  - Open interest is at the 81st percentile and up 3%.
- **Weight: 0.4.**
- **Change my mind:** below 95; above 108 I add.

{"7ab869b6e4 (XRP)": 0.35, "6fa6f2ba4b (ADA)": 0.45, "93ae5a2eb5 (SOL)": 0.7, "486a5b79d1 (AVAX)": 0.4, "5a0f995be0 (DOT)": 0.3, "fa87e1c6c4 (LTC)": 0.5, "539229006e (LINK)": 0.55, "4c4b4d6f8e (ETH)": 0.45, "7b72f257ab (BTC)": 0.55, "4aaba44a2e (DOGE)": 0.4}

## Entscheidung 2026-08-30

**Strategy:** I go long when a breakout from a base is holding and the higher-high/higher-low structure is intact. I cut the weight when price sits under heavy overhead supply from the pre-crash range, when the breakout looks like a blow-off that is fading, or when leverage is crowded (OI percentile above about 80, especially if OI is still rising). A low or recently flushed OI percentile lets me add weight.

## 5d6501be75 (LINK)
- **Read:**
  - The asset crashed to 63.9 at day -86, then built a base between 65 and 80 for about two months.
  - It broke out from about 74 to 107.6, with a high of 113.2 at day -8.
  - Price is now 100, above the old 180-day high of about 97.5.
  - Since the spike it has made lower highs (113.2, 107.5, 105.9), with support at 98–99.
  - OI is up 14% at the 85th percentile, so leverage is piling in behind the move.
- **Weight: 0.5.** The breakout is real and above prior highs, but crowded leverage and a fading follow-through cap the position.
- **Change my mind:** a close below 96 (exit), or a close above 108 (add).

## 311df88915 (ETH)
- **Read:**
  - Crash low was 62.3, followed by a steady base from 65 to 80.
  - It broke out from 79 to a 106.2 high.
  - Price is now 100, right inside the old supply zone of 97–102 (the highs at days -135 and -116).
  - Support sits at 97.5–98.8.
  - OI is at the 87th percentile but only up 3%.
- **Weight: 0.45.** Price is holding the breakout, but it is testing overhead supply with high leverage.
- **Change my mind:** a close below 97.5 (exit), or a close above 106.5 (add).

## cf04610d6c (XRP)
- **Read:**
  - The breakout ran from 74 to a blow-off wick at 125.2 on 6x volume, then closed at 107.7.
  - Since then the highs have stepped down: 112, 108.6, 105.6.
  - Price at 100 is back in the old pre-crash range of 96–108.
  - Support is at 98.4.
  - OI is up 5% at the 56th percentile.
- **Weight: 0.35.** The huge-volume rejection wick looks like distribution, but the base breakout from 74 is still well intact.
- **Change my mind:** a close below 97 (exit), or a close above 109 (add).

## 3b9bc0272a (LTC)
- **Read:**
  - The longer trend is down: from 126 to a low of 82.
  - The recovery base ran from 88 to 100, then spiked to 115.7.
  - Price has retraced to 100, which is the top of that prior base (99.9 to 100.7).
  - Pre-crash supply sits between 108 and 126, above current price.
  - OI is at the 70th percentile, up 6%.
- **Weight: 0.35.** The spike gave back most of its gains, and price is now just testing the old range top.
- **Change my mind:** a close below 97 (exit), or a close above 106 (add).

## c8778dfe11 (SOL)
- **Read:**
  - This is the cleanest structure in the set.
  - Lows have stepped up: 59, 62, 69, 72.
  - The first spike reached 101, and a second leg made a higher high at 108.7 on day -3.
  - Price at 100 is a normal pullback within that advance.
  - Support is 93.3–93.7.
  - OI is flat at the 14th percentile, so leverage is not crowded.
- **Weight: 0.7.** The trend is intact with low leverage.
- **Change my mind:** a close below 93 (exit), or a close above 109 (add).

## 2127a0a23f (AVAX)
- **Read:**
  - Pre-crash price traded between 125 and 147.
  - After the crash it ranged from 80 to 98 for about 80 days.
  - It spiked to a 116.9 wick, and price is now 100, just above the old range top of 96–98.
  - Supply overhead runs from 115 to 147.
  - OI is at the 29th percentile, up 2%.
- **Weight: 0.45.** Price is holding just above its range with modest leverage, but the long-term trend is down.
- **Change my mind:** a close below 96 (exit), or a close above 108 (add).

## c024de4c2d (DOGE)
- **Read:**
  - Price has trended down persistently: from 140 to 85.
  - It spiked to a 122.9 wick, then faded with lower highs: 115, 113.5, 110, 109.7.
  - Price at 100 has retraced about 50% of the move from 85 to 113.
  - OI is at the 68th percentile, down 2%.
- **Weight: 0.3.** The dominant trend is still down and the spike is fading.
- **Change my mind:** a close below 97 (exit), or a close above 110 (add).

## f2d839ab07 (ADA)
- **Read:**
  - Price is volatile but has made higher lows and higher highs:
    - Lows: 71.7, 79.6, 88.8.
    - Highs: 103.8, 109.9, 134.1.
  - Each spike has faded hard, and price at 100 is about 15% below the 117 closes.
  - Key support is 98.3, then 88.8.
  - OI is down 25% at the 50th percentile, so leverage has already been flushed.
- **Weight: 0.45.** The structure is rising and leverage is cleaned out, offset by its habit of fading every spike.
- **Change my mind:** a close below 95 (cut), a break of 88.8 (exit), or a close above 111 (add).

## 50f347470e (DOT)
- **Read:**
  - This is a long downtrend from 200 to 88, with lower highs at 170, 164.5, 127.8, 110.9 and 106.2.
  - The spike to 126 broke that lower-high sequence.
  - Price at 100 is back inside the recent range of 92–108.
  - OI is down 11% at the 58th percentile.
- **Weight: 0.3.** There is a first sign of a trend change, but the big-picture trend is still down and the spike has largely faded.
- **Change my mind:** a close below 97 (exit), or a close above 110 (add).

## ca4b476b4e (BTC)
- **Read:**
  - The post-crash base ran from 75 to 86.
  - The breakout to 102 was orderly rather than a blow-off.
  - Price has consolidated tightly between 97.2 and 104.9 for 9 days, near the old pre-crash range of 95–106.
  - OI is at the 91st percentile, down 1%, so leverage is very crowded.
- **Weight: 0.5.** The breakout is holding well, but leverage is crowded and supply sits overhead around 105–107.
- **Change my mind:** a close below 97 (exit), or a close above 105.5 (add).

{"5d6501be75 (LINK)": 0.5, "311df88915 (ETH)": 0.45, "cf04610d6c (XRP)": 0.35, "3b9bc0272a (LTC)": 0.35, "c8778dfe11 (SOL)": 0.7, "2127a0a23f (AVAX)": 0.45, "c024de4c2d (DOGE)": 0.3, "f2d839ab07 (ADA)": 0.45, "50f347470e (DOT)": 0.3, "ca4b476b4e (BTC)": 0.5}

## Entscheidung 2026-09-06

**1. Strategy.** I stay long when price is above its recent breakout zone and at or near its 180-day highs. I size down when the price still sits under higher resistance from earlier in the window, or when open interest is rising into the move at a high percentile, because that means crowded leverage. A close back inside the pre-breakout range (roughly the mid-70s to 80s) or below the post-breakout consolidation lows cancels the long case.

**2. Windows**

### 92d62d999b (ETH)
- **Read:** The asset sold off from about 96 (day -142) to 60 (day -93), then based between 62 and 77 for about two months. A volume breakout on days -18 to -16 carried it to 100. It has since held a tight 94–101 range, and today closes at 100, the top of that range and above the old 96–98 highs. Open interest is flat at a mid percentile (58), so leverage is not crowded.
- **Weight:** 0.8. The breakout is clean and holding, there is no overhead supply in this window, and positioning is neutral.
- **Change my mind:** a close below 93.7.

### 5706aa3a8f (ADA)
- **Read:** Price is still well below earlier highs of 126–130. It spiked to a 115.7 wick on day -15, retraced to 84.8, and now has higher lows (84.8 → 85.9 → 93.6) and closes at 100. Open interest fell 29% over 4 weeks (percentile 46), so leverage has been flushed, which is constructive.
- **Weight:** 0.6. The recovery is good, but there is resistance at 102–104 and then 115.
- **Change my mind:** a close below 89.

### b65b765fa0 (XRP)
- **Read:** Day -15 was a blow-off spike to 119.4 on six times average volume, which was rejected. Price has ranged 92–104 since and closes at 100. Earlier highs sit at 109–113. Open interest is down 9% (percentile 44), so it is not crowded.
- **Weight:** 0.55. The range is holding, but the rejected climax wick caps upside for now.
- **Change my mind:** a close below 92. A close above 104 would make me add.

### 1f9b546ba0 (LINK)
- **Read:** The trend has made higher lows since the 53 bottom. Today breaks the post-spike range (82–95) and closes at 100, the high of the day, on 1.7 times volume. That is far above every prior level in the window (the old high was 82), so it is a fresh 180-day high. Open interest is at percentile 78 and up 5%, elevated but not extreme.
- **Weight:** 0.85. This is the strongest trend in the set and the breakout is confirmed.
- **Change my mind:** a close below 90, which would mean a failed breakout back into the range.

### d4c02274b7 (BTC)
- **Read:** Price recovered from 73.6 to the 95–101 range and has consolidated there for two weeks with low volume. It now sits just under the prior high of 101–103 from day -123. Open interest is flat at percentile 76.
- **Weight:** 0.7. The trend is constructive and the consolidation is orderly, but it is pressing into prior resistance.
- **Change my mind:** a close below 94.9.

### e76708704a (LTC)
- **Read:** Price spiked to 100.9, faded to 86, and then jumped 7.8% yesterday on 2.3 times volume to retest about 100. Earlier highs are around 110. Open interest is up 29% at the 100th percentile, meaning the most leverage of the whole window is piling into this retest. That raises the risk of a long squeeze.
- **Weight:** 0.4. The price structure is acceptable, but positioning is crowded.
- **Change my mind:** a close below 92 means go flat. Closes above 102 with open interest stabilising would mean add.

### e4fdbc62cc (DOGE)
- **Read:** The longer trend fell from 127 to 76. The spike to 110.9 failed, and price has chopped between 88 and 104 since. Yesterday's wick to 104.7 was rejected. Open interest is up 9% at percentile 91, which is crowded.
- **Weight:** 0.45. This is a choppy range below major supply at 110–130, with leverage high.
- **Change my mind:** a close below 88. A close above 105 would make me add.

### a302661fe4 (AVAX)
- **Read:** Earlier highs are at 125–132. The breakout wick to 105.2 failed, the pullback found support at 88.7, and price has risen steadily back to 100, closing at the high. Open interest is up 21% at percentile 90, so leverage is building into the move.
- **Weight:** 0.5. The structure is improving, but resistance sits at 105 and positioning is crowded.
- **Change my mind:** a close below 89.

### 2db008e145 (DOT)
- **Read:** This is the weakest longer-term chart: a long decline from 167 to 77. The spike to 105 was rejected down to 82.5. Price is now on a six-day advance to 100 with today's volume at 1.67 times. Open interest is down 7% at percentile 66, so the move is not leverage-driven. Resistance is at 101–105, then the 120s.
- **Weight:** 0.55. Momentum is good, but the price is still below the broader prior range.
- **Change my mind:** a close below 85.

### e0d309b3b1 (SOL)
- **Read:** Highs and lows have been rising cleanly: the base at 67–72, then 96.4, then 103.8, then a hold of 91.4. Price closes at 100, above the old high of 92.4 from day -118. Open interest is at the 1st percentile and down 8%, so the rally is happening with almost no leverage. That is a healthy, spot-led move with little squeeze risk.
- **Weight:** 0.8.
- **Change my mind:** a close below 91.

{"92d62d999b (ETH)": 0.8, "5706aa3a8f (ADA)": 0.6, "b65b765fa0 (XRP)": 0.55, "1f9b546ba0 (LINK)": 0.85, "d4c02274b7 (BTC)": 0.7, "e76708704a (LTC)": 0.4, "e4fdbc62cc (DOGE)": 0.45, "a302661fe4 (AVAX)": 0.5, "2db008e145 (DOT)": 0.55, "e0d309b3b1 (SOL)": 0.8}

## Entscheidung 2026-09-13

**1. Strategy**

I go long when price has broken out of a multi-month base and is holding above the breakout zone, sized up when it has also cleared older resistance. I size down when the bounce makes lower highs, when there is heavy overhead supply, or when a blow-off spike is reversing. Open interest adjusts the size: a high percentile with rising open interest means crowded longs and I cut; washed-out open interest with price holding up is cleaner and I add.

**2. Windows**

**1f368360a9 (BTC)**
- **Read:** Prior high was about 107 (day -130). Price crashed to 77, then based at 77–87. The day -25 to -23 breakout took it to about 102. For three weeks it has held a 99–106 range and now sits near the bottom of that range.
- **Open interest:** neutral (pct 54, -7%).
- **Weight:** 0.6. The breakout is holding, but there is supply at 105–107.
- **Change my mind:** a close below 98.5.

**3221ef7535 (ETH)**
- **Read:** Price is at its highest level of the window, above the old 94–99 highs. The base was 63–78 and the breakout went 77 to 102. It has consolidated at 95–103, and a day -2 spike to 107.6 was rejected.
- **Open interest:** fairly elevated (pct 76) but flat.
- **Weight:** 0.6.
- **Change my mind:** a close below 95.

**c2e3c311ce (ADA)**
- **Read:** Price crashed from 120–140 down to 73, then made a choppy base at 70–98. It broke out to a 127 wick, and since then highs have been lower: 127, 114, 110. The range is 93–114, and the window started far above current prices.
- **Open interest:** has been flushed (-24%, pct 36), which helps.
- **Weight:** 0.4.
- **Change my mind:** a close below 93.

**174b3aee3c (DOT)**
- **Read:** There is a long downtrend from 162 and a base at 75–87. Price spiked to 103 and fell back to 82. Then came a blow-off to 128.5 on 4× volume, fully faded within 4 days back to 100.
- **Open interest:** at pct 92, which is crowded.
- **Weight:** 0.2. This looks like a failed spike.
- **Change my mind:** a reclaim above 107. Below 95, I would go flat.

**669473851d (AVAX)**
- **Read:** Price fell from 140 to a 78 low, then based at 85–95. The breakout wicked to 114 and price has since ranged 96–112. The latest high, 112.5, is lower than the earlier one, and price sold off from there to 100.
- **Open interest:** rising (+9%), mid percentile (pct 50).
- **Weight:** 0.5.
- **Change my mind:** a close below 96.

**fb088e8294 (LTC)**
- **Read:** Prior high was 112. Price crashed to 73 and based at 80–89. It broke out to 99, pulled back to 88, then pushed to a 110.6 wick that was rejected; it is now at 100.
- **Open interest:** building (+11%, pct 88), so leverage is getting crowded.
- **Weight:** 0.4.
- **Change my mind:** a close below 96.

**7322935193 (LINK)**
- **Read:** Price is above the prior 97 high. It has made higher lows (about 97–98) after a run to 118–122, which retraced to 100.
- **Open interest:** washed out (-32%, pct 28), which is a clean setup.
- **Weight:** 0.6.
- **Change my mind:** a close below 97.

**43e2f61f86 (SOL)**
- **Read:** Price is above the prior 98 high. The base was 72–78 and the breakout ran to 110. It has ranged 98–111 since.
- **Open interest:** very low leverage (pct 3), so it is not crowded.
- **Weight:** 0.65.
- **Change my mind:** a close below 98.

**33b1902a7a (DOGE)**
- **Read:** There is heavy overhead supply at 120–140. The base was 83–90, and the breakout wicked to 122. Price has since ranged 97–115 and is now near the lower end at 100.
- **Open interest:** neutral (pct 65, -10%).
- **Weight:** 0.45.
- **Change my mind:** a close below 97.

**eab4060bb9 (XRP)**
- **Read:** Prior high was 115. The base was 73–86, and the breakout went to a 126.7 wick on huge volume. Price has consolidated at 98–110 and is now at 100.
- **Open interest:** flushed (-28%, pct 31).
- **Weight:** 0.5.
- **Change my mind:** a close below 97.5.

**3. Weights**

{"1f368360a9 (BTC)": 0.6, "3221ef7535 (ETH)": 0.6, "c2e3c311ce (ADA)": 0.4, "174b3aee3c (DOT)": 0.2, "669473851d (AVAX)": 0.5, "fb088e8294 (LTC)": 0.4, "7322935193 (LINK)": 0.6, "43e2f61f86 (SOL)": 0.65, "33b1902a7a (DOGE)": 0.45, "eab4060bb9 (XRP)": 0.5}

## Entscheidung 2026-09-20

**1. Strategy**

Go long when price is in a confirmed uptrend: higher lows, and a close at or above a multi-week range or a prior 180-day resistance, with the breakout holding. Cut the weight when the move is a fresh blow-off, when price sits in the middle of a choppy range under lower highs, or when open interest is both crowded (high percentile) and rising fast. Each weight carries an invalidation level near the nearest structural support.

**2. Windows**

**1871bc2483 (SOL)**
- **Read:** Crashed from about 75 to 56 (days -110 to -107), then built a 62–70 base for two months. Broke out at -32 to the 85–98 area and consolidated 86–96 for four weeks. Day -2 broke out to a new window high around 101 (prior high 88.5) and has held near 100 for two days.
- **OI:** Low at the 18th percentile and +4%, so leverage is not crowded.
- **Weight:** 0.9. This is a clean base, breakout, consolidation and second breakout.
- **Change my mind:** a close below 86.

**6aeff8fe4a (LTC)**
- **Read:** The same base-and-breakout pattern. It is now testing the window high near 103 (day -133) and the day -13 wick at 101.
- **OI:** At the 100th percentile and +22% in four weeks, so heavily crowded.
- **Weight:** 0.6. The trend is up, but crowded leverage at resistance raises flush risk.
- **Change my mind:** a close below 86. A close above 104 would let me add.

**db5c8c9350 (DOGE)**
- **Read:** The early window traded 105–135, then fell to an 80 base. The day -29 spike reached 115.5 but failed, and highs since then are lower: 109, 105, 104.6. Price is at 100, mid-range between 90 and 105.
- **OI:** 81st percentile.
- **Weight:** 0.3. The structure is a range with lower highs, well below the early-window levels.
- **Change my mind:** a close above 105 would make me go long. Below 89.7 I go flat.

**7cd2650088 (ETH)**
- **Read:** A gap breakout at -32 from 72 to 85+, then a month consolidating 89–96. It is now breaking out to 100, above the prior window highs of 91–93.
- **OI:** 91st percentile but flat over four weeks.
- **Weight:** 0.75. The breakout is clean; the elevated OI trims it.
- **Change my mind:** a close below 89.

**5eb41bc80e (LINK)**
- **Read:** A breakout from a 65–76 base. It peaked at 109 (day -13), pulled back to 85, and has recovered to 100. Lows near 85–88 are holding.
- **OI:** Down 16% (deleveraging), 44th percentile, so healthy.
- **Weight:** 0.6. Price is still below the 106–109 high.
- **Change my mind:** a close below 85. Above 106 I would add.

**0a69c028a7 (XRP)**
- **Read:** A blow-off spike to 120.5 (day -29, volume 5.9×) failed. Highs since then are lower (110, 105, 106, 103) and swings are wide, roughly 89–106. Price is mid-range at 100, near the old 93–105 range from the start of the window.
- **OI:** 76th percentile.
- **Weight:** 0.4. The trend is unresolved.
- **Change my mind:** a close below 88. Above 106 would be a range breakout.

**de32489179 (BTC)**
- **Read:** A steady recovery from 77 to 100 in a tight 93–101 consolidation with low volatility. It is now at resistance near 101–102 (the window high, day -137).
- **OI:** 87th percentile, +2%.
- **Weight:** 0.7. The trend is orderly; breakout confirmation is still pending.
- **Change my mind:** a close below 92.4.

**8f06a89483 (ADA)**
- **Read:** A high-volatility name. The early range was 100–127, followed by a crash to 61. The day -29 spike reached 113 and failed, and price has since traded 84–103. It is now at 100, near the top of that range and still below the early 115–127 levels.
- **OI:** Down 8%, 61st percentile.
- **Weight:** 0.45.
- **Change my mind:** a close below 83.5. A hold above 103 would let me add.

**619df9d4fe (AVAX)**
- **Read:** A long decline from 90 to a 50–60 base, a slow climb to 72, then +23% and +12% in two days on 3.9× and 6.1× volume. Day 0 ranged 83–101. This is parabolic and runs straight into the old 85–92 supply zone.
- **OI:** +26% and 98th percentile, so very crowded.
- **Weight:** 0.3. There is real momentum, but chasing a vertical move with leveraged positioning carries high reversal risk.
- **Change my mind:** a close below 83 means flat. Consolidation holding above 90 would raise the weight.

**952e476850 (DOT)**
- **Read:** A downtrend from 124 to 66. A spike to 113 (day -12) reversed to 82, and price has climbed back to 100. The structure is choppy and still under the early-window levels of 105–125.
- **OI:** +25%, 88th percentile, so crowded.
- **Weight:** 0.4.
- **Change my mind:** a close below 88. Above 110 would let me add.

**3. Weights**

{"1871bc2483 (SOL)": 0.9, "6aeff8fe4a (LTC)": 0.6, "db5c8c9350 (DOGE)": 0.3, "7cd2650088 (ETH)": 0.75, "5eb41bc80e (LINK)": 0.6, "0a69c028a7 (XRP)": 0.4, "de32489179 (BTC)": 0.7, "8f06a89483 (ADA)": 0.45, "619df9d4fe (AVAX)": 0.3, "952e476850 (DOT)": 0.4}

## Entscheidung 2026-09-27

**Strategy:** I follow the trend. When price breaks to new highs of the 180-day window, higher lows are intact and the breakout is holding, I go fully or mostly long. I cut size when the move is a fresh vertical spike, when long upper wicks show selling into the high, or when overhead resistance is still nearby. I also cut size when open interest has jumped and its percentile is very high, because crowded leverage tends to unwind.

## 60b1411abc (BTC)
- **Read:** The market crashed from about 93 to 70 between days -118 and -114, then based between 69 and 78 until day -40. The rally from day -39 cleared the earlier 180-day high of 98.1 on day -6. Since then price has held a tight 98–103 band, with higher lows at 88.7, 90.0 and 98.1. Open interest is low (percentile 8) and fell 12% over 4 weeks, so the move looks spot-driven rather than leveraged.
- **Weight:** 0.9. This is a clean breakout and consolidation with no leverage froth.
- **Change my mind:** a close below 95.

## 614710fdd9 (XRP)
- **Read:** The trend is up from 65, but the path is very choppy. Price spiked to 112.1 on day -36, swung between 83 and 104, and recently printed long upper wicks at 109.3 and 107.5. Lows are rising: 83.4, then 95.7, then 99. Open interest is neutral (percentile 53, flat).
- **Weight:** 0.6. The trend is up, but sellers are clearly active between 104 and 112.
- **Change my mind:** a close below 95. A close above 107 would make me add.

## 6b226aba49 (ETH)
- **Read:** The old high of 91.7 broke on day -39. Price consolidated between 88 and 95, then broke out again at day -6 to 104.4. It is now holding 99–103 on falling volume. Higher lows are intact and open interest is average (percentile 43).
- **Weight:** 0.85. The breakout is constructive.
- **Change my mind:** a close below 96.

## e52ecac122 (LINK)
- **Read:** Price doubled from the 50 low in a steady staircase and made new highs at 103.4 on day -1. Pullbacks are sharp but get bought: 86 on day -4 recovered the next day. Open interest is elevated (percentile 81) but flat over 4 weeks.
- **Weight:** 0.75. Momentum is strong, trimmed slightly for elevated leverage and wide swings.
- **Change my mind:** a close below 93.

## 3248c4e84b (ADA)
- **Read:** Price recovered from 55 to 100, but the 180-day high of 113 from day -140 still sits overhead. There was a wick to 101.3 on day -36, then a fall to 75, then a rebound into 100–104. Swings are wide, for example a low of 91.5 on day -4. Open interest is neutral (percentile 57).
- **Weight:** 0.6. The uptrend is real, but price faces resistance at 104 and again at 107–113.
- **Change my mind:** a close below 91. A close above 104 would make me add.

## d3fb400771 (SOL)
- **Read:** This is a steady uptrend from 49, with new 180-day highs well above the old 80.7. Higher lows run 78.5, then 92.2, then 98.2. Open interest is low (percentile 23), so leverage is not driving the move.
- **Weight:** 0.85.
- **Change my mind:** a close below 94.

## aed26721bf (DOT)
- **Read:** The price action is very volatile. It spiked to 101.3 on day -19, collapsed to 73.7, then rallied back to a wick at 103 on day -1. On day -4 it dropped from 96 to 85 in a single session. The 180-day highs of 110–113 are still overhead. Open interest is neutral (percentile 43).
- **Weight:** 0.5. This could be a double top near 101–103, inside a high-volatility regime.
- **Change my mind:** a close below 90. A close above 104 would make me add.

## 067fc937dd (DOGE)
- **Read:** Price spiked to 109.3 on day -5 and was rejected straight away, falling to 94. It is now drifting just under that high, and the 180-day high of 122 is far above. Open interest is high (percentile 84) and rose 12%, so leverage is building into resistance.
- **Weight:** 0.45.
- **Change my mind:** a close below 94. A close above 106 would make me add.

## 43b205b27a (AVAX)
- **Read:** Price went near-vertical from 70 to 108 between days -9 and -6, on volume up to 5.7 times the window average. It has since held a 92–104 range, which is above the old range top of about 96. Open interest jumped 36% and sits at the 97th percentile, a crowded long.
- **Weight:** 0.35. The breakout is valid, but a leverage flush is a real risk.
- **Change my mind:** a close below 91. A close above 108 with open interest stable would make me add.

## 89fda1aeb3 (LTC)
- **Read:** On day -3 price gapped from 87 to 101 on volume 6.7 times the average, clearing the 180-day high of 85. It is holding 99–105. Open interest rose 43% to the 99th percentile, the most crowded reading of all ten windows.
- **Weight:** 0.35. Same logic as 43b205b27a (AVAX): the breakout is real but leverage is extreme.
- **Change my mind:** a close below 96. A close above 105 would make me add.

{"60b1411abc (BTC)": 0.9, "614710fdd9 (XRP)": 0.6, "6b226aba49 (ETH)": 0.85, "e52ecac122 (LINK)": 0.75, "3248c4e84b (ADA)": 0.6, "d3fb400771 (SOL)": 0.85, "aed26721bf (DOT)": 0.5, "067fc937dd (DOGE)": 0.45, "43b205b27a (AVAX)": 0.35, "89fda1aeb3 (LTC)": 0.35}
