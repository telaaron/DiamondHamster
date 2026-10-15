# E-032: was die KI gedacht hat (Set A)

Volle Antwort des Deciders pro Entscheidungswoche, unverändert. Er sah weder Datum noch Coin-Namen; die Namen in Klammern sind erst danach eingesetzt. Gesendeter Prompt und Daten: runs/<set>/<woche>/requests.json.

## Entscheidung 2026-07-05

**Strategy:** Start from a neutral 0.5. Cut toward 0.4 when the 180-day trend is clearly down and the latest bounce came off a *lower* low that is still under resistance. Edge toward 0.55 only when the recent lows are holding or rising and price has cleared the last swing high. All of these windows have been falling for months, so no window gets much above neutral and none goes flat on a bounce alone.

### fc11a02940 (BTC)
- **Read:** Long downtrend from about 147. The crash low was 92.9 on day -30, and the retest made a slightly lower low at 90.8 on day -4. Price has since bounced to 100 on fading volume, still below the 104–105 swing high from day -20. The broader structure is lower highs (the 130 peak, then 120s, now 100s).
- **Weight:** 0.4. This is a bounce inside a downtrend, with the low not confirmed as holding.
- **Change mind:** A close above 105 brings it back to 0.5. A close below 90.5 cuts it to 0.25.

### 576cc3dc0f (DOT)
- **Read:** Steep decline from about 250. The day -29 low of 100.3 gave way to a lower low at 90.2 on day -7. The rebound to 100 is back into old support from days -24 to -15 (about 104–115), which should now act as resistance.
- **Weight:** 0.4. The trend is down and the most recent low was a lower one.
- **Change mind:** Above 108 → 0.5. Below 90 → 0.25.

### 2cf58f83f2 (DOGE)
- **Read:** Down from about 190. The low was 99.7 on day -29, then a lower low at 89.3 on day -5. Price has bounced to 100. Resistance sits at 110–114, and the 128–130 range from days -40 to -34 is far above.
- **Weight:** 0.4.
- **Change mind:** Above 106 → 0.5. Below 89 → 0.25.

### 630aab2692 (ETH)
- **Read:** Down from about 185. There is a double bottom at 84.3 (day -29) and 84.7 (day -10), so the low held. A three-day rally took price to 100 on above-average volume (0.99 on day 0), just under the day -20 high of 103.6.
- **Weight:** 0.5. The base is holding, but the long-term trend is still down.
- **Change mind:** A close above 104 → 0.6. Below 87 → 0.35.

### 377093ae13 (ADA)
- **Read:** A capitulation drop from about 132 to 82.7 on days -33 to -30. That was followed by a lower low at 72.9 on day -10. Then came a violent V-reversal on heavy volume (about 2.1 on days -2 and -1), from 76 to 105.5. Price now sits at 100, above the 100.3 high from day -20. The move is strong but overextended, and the gap zone around 85–95 is unfilled.
- **Weight:** 0.5. The breakout is real, but the volatility and extension argue against adding.
- **Change mind:** Holding above 106 → 0.6. Below 90 → 0.35.

### 02b15ab883 (LINK)
- **Read:** Down from about 170. There is a double bottom at 86.8 (day -29) and 86.9 (day -10). Price has bounced to 100, with resistance at the day -20 high of 106.7 and the 112–121 range above that. Volume on the bounce is light.
- **Weight:** 0.5. The base is holding but resistance has not been cleared.
- **Change mind:** Above 107 → 0.6. Below 87 → 0.35.

### cdb771465a (AVAX)
- **Read:** Down from about 210. A capitulation low of 82.0 on day -16 came on 3x volume. Since then the lows have been rising: about 86, then 91.5, then 92. Price at 100 is now just under the day -20 high of 102.2 and day -1 high of 102.8.
- **Weight:** 0.5. The short-term structure is improving, but the window is still in a downtrend.
- **Change mind:** A close above 103 → 0.6. Below 91.5 → 0.35.

### 09de82b4ac (XRP)
- **Read:** Down from about 199. The day -29 low of 90.7 was followed by a lower low at 87.2 on day -9. Price has bounced to 100. Resistance is at 107 and then 111.8, the day -20 spike.
- **Weight:** 0.45.
- **Change mind:** Above 107 → 0.55. Below 88 → 0.3.

### c62c01256f (SOL)
- **Read:** Down from about 173. The low was 73.7 on day -29, then a higher low at 78.5 on day -10. Price then rallied to 100–103, clearing the day -20 high of 93.3, so the short-term pattern is higher highs and higher lows. Overhead, the 100–107 congestion from days -50 to -34 is resistance.
- **Weight:** 0.55. This has the cleanest short-term reversal of the set.
- **Change mind:** Above 107 → 0.65. Below 92 → 0.4.

### 5a7b735e48 (LTC)
- **Read:** Down from about 183. The low was 88.4 on day -29, then a slightly lower low at 85.7 on day -10. Price is now back at 100, roughly level with the day -20 high of about 101. Resistance is at 101 and then the 113–118 shelf.
- **Weight:** 0.45.
- **Change mind:** A close above 102 → 0.55. Below 89 → 0.3.

{"fc11a02940 (BTC)": 0.4, "576cc3dc0f (DOT)": 0.4, "2cf58f83f2 (DOGE)": 0.4, "630aab2692 (ETH)": 0.5, "377093ae13 (ADA)": 0.5, "02b15ab883 (LINK)": 0.5, "cdb771465a (AVAX)": 0.5, "09de82b4ac (XRP)": 0.45, "c62c01256f (SOL)": 0.55, "5a7b735e48 (LTC)": 0.45}

## Entscheidung 2026-07-12

**Strategy:** Hold 0.5 by default. Go modestly underweight (0.35 to 0.4) when the 180-day trend is clearly down, with lower highs and the bounce failing below prior breakdown levels. Return to 0.5 only when there is a higher-low structure off the lows. Move further only if price decisively breaks the recent low (go lower) or clears the recent swing high (go higher).

## e4710477d8 (XRP)
- **Read:** Long downtrend from about 199 to 100. A capitulation leg at days -40 to -37 reached 98.5, then a lower high at 119 (day -27). Price retested at 93.2 (day -17) and bounced to 109, another lower high. Now drifting at 100 on light volume. Support is 93 to 96, resistance is 109 then 119.
- **Weight:** 0.4. The trend is down and the highs are lower, but there is no fresh breakdown, so this is only a mild underweight.
- **Change my mind:** Below 93 cuts to 0.2. Above 110 goes back to 0.5 or higher.

## 592e3e128e (BTC)
- **Read:** Fell from 150 to 100. A recovery rally to 130 (day -67) fully failed into a crash to 92.7. Lows since then are 91 to 92 (days -17 and -12). The bounce stalls around 100 to 101, which is the old breakdown area. Support is 90.6, resistance is 101.5 then 105.
- **Weight:** 0.4. This is a range below broken support inside a downtrend.
- **Change my mind:** Below 90.5 goes lower. A close above 105 brings it back to 0.5.

## 2c7f896840 (DOGE)
- **Read:** Fell from 204 to 100. A strong rally to 163 (day -59) reversed sharply, losing about 40%. The low was 95.6 (day -12), the bounce peaked at 109, and price is now 100 on very low volume. Support is 95.6, resistance is 109 then 122.
- **Weight:** 0.4. The failed rally plus the downtrend argues against a full middle weight.
- **Change my mind:** Below 95 goes lower. Above 110 brings it back to 0.5.

## 22576f3ad9 (AVAX)
- **Read:** Fell from 230 to 100. After the crash there was a second flush to 88.7 (day -23) on heavy volume. It recovered to 111, then rolled over, and today it tagged 98 and closed at 100. Support is 93 then 88.7, resistance is 111.
- **Weight:** 0.4. Today's weak close and the lower highs argue for staying slightly under neutral.
- **Change my mind:** Below 93 goes lower. Above 111 brings it back to 0.5.

## 09181a3822 (ADA)
- **Read:** Fell from 260 to 100. The low was 85.3 (day -17). A violent spike to 123.4 (day -8) was fully retraced within a week, and today's close of 100 is a fresh multi-day low. Support is 92 then 85, resistance is 108 then 123.
- **Weight:** 0.35. A failed breakout is a bearish tell inside a primary downtrend.
- **Change my mind:** Below 92 goes lower still. Back above 108 brings it to 0.5.

## 0f64f0e2b7 (LTC)
- **Read:** Fell from 178 to 100 in a persistent grind lower. The low was 89.3 (days -18 and -17). The recovery is orderly, to 104.9, and price is now flat around 100. Support is 89.3, resistance is 105.
- **Weight:** 0.4. This is a range-bound bounce inside a downtrend.
- **Change my mind:** Below 89 goes lower. Above 105 brings it back to 0.5.

## 645144720f (DOT)
- **Read:** Fell from 270 to 100, the steepest decline of the group. The low was 94.2 (day -14), and price is chopping between 96 and 106. The day -2 rally to 106 was rejected. Support is 94, resistance is 106.
- **Weight:** 0.4. The downtrend dominates and the bounce has been rejected.
- **Change my mind:** Below 94 goes lower. Above 107 brings it back to 0.5.

## 1e99184c7b (ETH)
- **Read:** Fell from 184 to 100. The capitulation low was 83.3 (day -36) and the retest held at 83.7 (day -16), a double bottom. Price has since rallied to 100 to 101 and is closing near the top of its range, though the higher high is still unconfirmed. Support is 94.8 then 83.7, resistance is 101.5 then 102.4.
- **Weight:** 0.5. The double-bottom structure offsets the downtrend.
- **Change my mind:** Below 94 cuts to 0.35. A close above 103 lifts it to 0.6.

## db043bdd8d (LINK)
- **Read:** Fell from 176 to 100. The low was 87.5 (day -36) with a higher low at 87.7 (day -17). The recovery to 100 to 102 has stalled under the 102 to 103 band. Support is 94, resistance is 102.3 then 107.5.
- **Weight:** 0.45. The base is constructive but the overhead is unresolved.
- **Change my mind:** Below 94 goes to 0.35. Above 103 goes to 0.55.

## e747db7904 (SOL)
- **Read:** Fell from 190 to 100. The crash low was 78.2 (day -36), followed by a clear higher low at 83.3 (day -17). Price rallied to 109 and has now pulled back to 100, holding above the day -11 breakout area. This is the best-structured base of the group. Support is 98.3 then 93, resistance is 109.
- **Weight:** 0.5. The higher-low structure justifies the middle weight.
- **Change my mind:** Below 93 cuts to 0.35. Above 109 lifts it to 0.6.

{"e4710477d8 (XRP)": 0.4, "592e3e128e (BTC)": 0.4, "2c7f896840 (DOGE)": 0.4, "22576f3ad9 (AVAX)": 0.4, "09181a3822 (ADA)": 0.35, "0f64f0e2b7 (LTC)": 0.4, "645144720f (DOT)": 0.4, "1e99184c7b (ETH)": 0.5, "db043bdd8d (LINK)": 0.45, "e747db7904 (SOL)": 0.5}

## Entscheidung 2026-07-19

**Strategy:** Start from 0.5. Move toward 0 or 1 only when the multi-month trend and the recent structure agree. Every window here shows a long decline from the start of the window, a crash around day −45 and a base since then. I tilt by at most ±0.1, based on whether the base is making higher lows and breaking resistance (slightly long) or still making lower lows and failing rallies (slightly short).

### 7c0071d0c2 (LINK)
Price is in a long downtrend from 148, with a crash to 84.9 on day −44. It has double-bottomed near 83.6–84.9 and recovered to 100, which sits just under resistance at 102.6–103. Volume is fading into that resistance. The structure is neutral: a base without a breakout. **Weight 0.5.** A close above 103.5 would take me to 0.6; a close below 92 would take me to 0.4.

### 8e94d98353 (DOGE)
Price fell from 175, and the day −66 rally high of 163.8 failed badly. Lows keep stepping down: 109 → 98.6 → 96.0. It is now in a tight 98–104 range on very low volume. The trend is still down and there is no reversal structure. **Weight 0.4.** A close above 109 would make me neutral.

### 73b1467232 (LTC)
The crash low was 86.1, followed by a higher retest at 83.5–85. Price is now 100 after a high-volume breakout above the 97–98 range highs on day −1. This is the beginning of a turn from a base. **Weight 0.55.** A close below 92 would take me back to 0.45.

### 79abfec782 (SOL)
The lows step up: 78.7 on day −43, then 83.8 on day −24, then 96–97 recently. A rally reached 110 on day −15 and has pulled back to about 100. This is a higher-low structure with support at 96–97. **Weight 0.55.** A close below 95 would take me to 0.45.

### 16674e93d1 (DOT)
This is the steepest decline in the set, from 238. Lows keep falling: 107.8 → 97.0. Day 0 was a 2% down day from 104.8 toward the range floor of 97–98. The trend is clearly down. **Weight 0.4.** A close above 109 would move me to 0.5.

### f53d0db0fd (AVAX)
The crash low was 96.3, then a lower spike low of 87.9 on day −30 that was quickly bought. Since then price has chopped between 97 and 110 and now sits mid-range at 100. The picture is mixed. **Weight 0.5.** A close above 110 would take me to 0.6; a close below 96 would take me to 0.4.

### 728a4c34d6 (ADA)
Lows went lower: 89.4, then 83.1 on day −24. A high-volume spike to 120.3 on day −15 fully retraced back to 95–100, which is a failed rally inside a downtrend. **Weight 0.45.** A close above 108 would move me to 0.55; a close below 93 would move me to 0.35.

### b5acb3b8b2 (XRP)
Lows went lower, from 95.7 to 91.9 on day −23. Price has ranged 96–108 since then and is now 100 with very thin volume. This is a neutral range inside a downtrend. **Weight 0.5.** A close below 95 would take me to 0.4; a close above 106 would take me to 0.6.

### ab4c196057 (ETH)
There is a double bottom at 80.4–80.8, on days −43 and −23. Price then broke above the day −34 high of 98.8, reaching 104 on day −4, and is now holding at 100. This is a constructive base. **Weight 0.55.** A close below 93 would move me to 0.45.

### 26ea2ee9dc (BTC)
This is a shallower decline, from 138. The lows of 91.4 and 89.8 are roughly equal, and resistance sits at 101.7–104. Price is 100, mid-range. **Weight 0.5.** A close above 104 would take me to 0.6; a close below 95 would take me to 0.4.

{"7c0071d0c2 (LINK)": 0.5, "8e94d98353 (DOGE)": 0.4, "73b1467232 (LTC)": 0.55, "79abfec782 (SOL)": 0.55, "16674e93d1 (DOT)": 0.4, "f53d0db0fd (AVAX)": 0.5, "728a4c34d6 (ADA)": 0.45, "b5acb3b8b2 (XRP)": 0.5, "ab4c196057 (ETH)": 0.55, "26ea2ee9dc (BTC)": 0.5}

## Entscheidung 2026-07-26

## Strategy

Start at 0.5. Move toward 0.6 only when the recent swing structure shows higher lows and price is pressing on resistance near the decision day. Move toward 0.4 when highs are still falling inside a larger downtrend. Every window shares the same broad shape: an early crash, then a range, then a second crash around day −51, then a recovery. So I stay close to the middle unless the post-crash structure clearly leans one way.

## dd6b356882 (ETH)
- **Read:** Long-term downtrend, from 154 at the start of the window to a low of 77–79 (days −51 and −30). Since day −30 the lows have risen steadily: 77.4, 87.7, 92.2, 94.5. The close of 100 sits at the recent highs of 100.1, with overhead supply at 105–110.
- **Weight:** 0.55. The recovery structure is constructive, but the price is still far below the old range.
- **Change of mind:** A close below 92.

## 6a0310af2a (LTC)
- **Read:** Lows were 82.1 (day −31) and then 90–92. Price has pushed back to the 100–101 highs it reached around day −8. The old range before the crash was 108–120.
- **Weight:** 0.55. Higher lows and price holding near the highs.
- **Change of mind:** A close below 95.5.

## 77a61f6dce (LINK)
- **Read:** Low of 79.4 at day −31. Lows have risen since: 85, 90.7, 94. Day 0 closed at 100, above the prior highs of 98–99.3.
- **Weight:** 0.6. This is the cleanest higher-low sequence and it has a small breakout.
- **Change of mind:** A close below 93.5.

## 22dd42106c (ADA)
- **Read:** A violent drop from 142 to 89, then a spike to 120.5 (day −22) that fully retraced. Price is now chopping between 97 and 108 on low volume, and the close of 100 is mid-range.
- **Weight:** 0.5. There is no edge here.
- **Change of mind:** A close below 96 (lower) or above 108 (higher).

## c0968af9ef (DOGE)
- **Read:** Lower highs since the 157 peak at day −73. Price is in a flat 93–103 range, and the bounces are capped near 107–108. Day −3 dipped to 93.2 before recovering.
- **Weight:** 0.45. The larger trend is still down, and the range is flat.
- **Change of mind:** A close below 93 (lower) or above 108 (higher).

## 5691b38616 (SOL)
- **Read:** Low of 78.3 at day −50, then a rally to 109.4 at day −22, then a pullback to the 95.6–97 area. That pullback held twice, at days −9 and −2. Close is 100.
- **Weight:** 0.5. The structure is acceptable, but the rally is consolidating below 103–109.
- **Change of mind:** A close below 95.

## 2d8fed5be9 (AVAX)
- **Read:** Low of 84.2 at day −37. Since then price has ranged between 91 and 105. Day −3 dropped to 91, and day −1 reversed sharply on 1.5× volume. Close is 100.
- **Weight:** 0.5. The range is intact, and the reversal is positive but a single day.
- **Change of mind:** A close below 91 (lower) or above 105 (higher).

## 496c0b7bed (XRP)
- **Read:** Low of 90.7 at day −31, then a pop to 106.4, then a range of 95–104.6. Volume is fading, and the close of 100 is mid-range.
- **Weight:** 0.5.
- **Change of mind:** A close below 95.

## b3cb5f72c0 (BTC)
- **Read:** Low of 88.9 at day −31, followed by a steady grind higher with higher lows at 94.5 and 97.5. The recent high was 102.4. The old range was 112–125.
- **Weight:** 0.55. An orderly recovery.
- **Change of mind:** A close below 95.

## 2489bd9629 (DOT)
- **Read:** A big downtrend from about 200. The lows since day −31 sit around 95–97, but the highs keep falling: 126, then 110, then 108, then 105. Price is coiling with a downward bias.
- **Weight:** 0.45.
- **Change of mind:** A close below 95 (lower) or above 108 (higher).

{"dd6b356882 (ETH)": 0.55, "6a0310af2a (LTC)": 0.55, "77a61f6dce (LINK)": 0.6, "22dd42106c (ADA)": 0.5, "c0968af9ef (DOGE)": 0.45, "5691b38616 (SOL)": 0.5, "2d8fed5be9 (AVAX)": 0.5, "496c0b7bed (XRP)": 0.5, "b3cb5f72c0 (BTC)": 0.55, "2489bd9629 (DOT)": 0.45}

## Entscheidung 2026-08-02

**Strategy:** Start at 0.5 and only move away on clear structure. Lean below 0.5 when the 180-day trend is lower highs and lower lows and price is stuck near the bottom of its range with no sign of recovery. Lean above 0.5 when price has made a higher-low recovery off a capitulation low or broken out of a base on volume. Keep every tilt modest, because signals near the middle of a range are weak.

## cc28ed4d47 (DOGE)
- **Read:** A persistent downtrend. Highs fell from 165 to 130 to 112 to 106. Price broke down at -61 and slid from about 142 to 98. For the last 35 days it has been a tight, quiet range between 96 and 106 on fading volume. It is basing, but there is no reversal yet.
- **Weight:** 0.4. The trend is down and price sits in the lower half of the base.
- **Change mind:** A close above 106 means go back to 0.5 or more. A close below 95.5 means cut further.

## 037c818185 (DOT)
- **Read:** A downtrend from 200+ to about 100. Price fell sharply to 95 at -6 and has crept back to 100. Lower highs are at 131, 113 and 108. The range is 93–112.
- **Weight:** 0.4. Structure is still bearish, and the -6 breakdown has not been fully repaired.
- **Change mind:** A close above 108 means raise. A close below 93 means cut.

## 1de1702fc5 (XRP)
- **Read:** A grind down from 135 to the mid-90s, with the low at 93 on day -37. Since then it has been a sideways range of 96–109 on low volume. It is a neutral-to-soft base.
- **Weight:** 0.45. This is a mild downtrend, flattening out.
- **Change mind:** Above 107 means go to 0.55. Below 93 means 0.35.

## 604b61ebff (ETH)
- **Read:** Capitulation to 80 at -57, followed by higher lows at 80, 83, 92 and 96. Highs reached 103–105. Price has recovered about 25% off the low and is holding the 97–105 band.
- **Weight:** 0.55. The recovery structure is constructive.
- **Change mind:** Below 96 means 0.45. Above 105 means 0.65.

## 226967d21d (LTC)
- **Read:** A low near 88 at -39, then higher lows at 96 and 97.6. It pushed to 107 at -15 and -7 and has now pulled back to 100. The base is constructive, with decent volume on the up-days.
- **Weight:** 0.55.
- **Change mind:** Below 97 means 0.45. Above 108 means 0.65.

## 21b585b9e9 (ADA)
- **Read:** A deep crash to 73 at -38. There was a sharp spike to 105, then a base between 81 and 93. Day 0 broke out of that base with an 8.7% gain to 100 on 1.7x volume. The low at 81 on day -6 was a higher low.
- **Weight:** 0.65. This is a clear base breakout on volume.
- **Change mind:** A close back below 92 (inside the base) means return to 0.5. Above 105 confirms the move.

## 8ee0099507 (LINK)
- **Read:** A low of 83.6 at -38. Price recovered to a 95–105 range and has chopped there for about 30 days. A higher low formed near 94. It is neutral.
- **Weight:** 0.5.
- **Change mind:** Above 106 means raise. Below 94 means cut.

## da51638fd5 (SOL)
- **Read:** A low of 82 at -57 and a rally to 113 at -30. Since then there has been a steady fade with lower highs at 107 and 105, now at 100. The range is 96–112, with mixed signals.
- **Weight:** 0.5.
- **Change mind:** Below 96 means 0.4. Above 107 means 0.6.

## 6c70951b76 (BTC)
- **Read:** Low volatility. The low was 91.4 at -38, and since then price has held a tight 97–105 range, sitting mid-range. There is no edge.
- **Weight:** 0.5.
- **Change mind:** Above 105.5 means raise. Below 97 means cut.

## 875f98772f (AVAX)
- **Read:** A collapse from 160 to 87 at -44. Since then it has been a wide range of 92–108. Day 0 was a reversal from 94.5 to 100 on 1x volume after a dip to 92. That is constructive short-term, but price is still inside the range.
- **Weight:** 0.5.
- **Change mind:** Above 108 means 0.6. A close below 92 means 0.4.

{"cc28ed4d47 (DOGE)": 0.4, "037c818185 (DOT)": 0.4, "1de1702fc5 (XRP)": 0.45, "604b61ebff (ETH)": 0.55, "226967d21d (LTC)": 0.55, "21b585b9e9 (ADA)": 0.65, "8ee0099507 (LINK)": 0.5, "da51638fd5 (SOL)": 0.5, "6c70951b76 (BTC)": 0.5, "875f98772f (AVAX)": 0.5}

## Entscheidung 2026-08-09

**Strategy:** Hold 0.5 by default. Move down to 0.3–0.4 only when there is a clear series of lower highs that is still pushing toward support. Move up to about 0.6 only when there are rising lows plus a high-volume breakout. Ranges that are tight and quiet stay at 0.5, because trading them costs more than it earns.

### fe9379038a (LINK)
- **Read:** The top was about 131 (day -91). Price crashed to 85.5 (day -64) and retested 85.6 (day -45). It has since recovered and is now in a quiet range of 96–108, below the old 110–120 band. Volume is drying up and there is no clear trend.
- **Weight:** 0.5. The range is neutral.
- **Change my mind:** Below 96 I cut; a close above 108 would lift it.

### 1997b81169 (DOT)
- **Read:** A steady decline from 208 to a low of 93.6 (day -13), with lower highs the whole way down. The latest bounce reached 108.9 and failed; price is drifting back toward 100.
- **Weight:** 0.35. The trend is still down.
- **Change my mind:** Above 109 I go back to neutral; below 93.5 I go lower.

### 25d4fa7379 (BTC)
- **Read:** The top was 127.7, and price crashed to 89.5 (day -45). It recovered into a very tight 96–103 range on low volume. This is a base, not a trend.
- **Weight:** 0.5.
- **Change my mind:** A break below 96 or above 103.5.

### 92b61d9dab (LTC)
- **Read:** The top was 133, and the low was 86.4 (day -45). Since then the lows have been rising: 86 → 90.5 → 94.4 → 96. Price reached 106 and pulled back to about 100. This is mildly constructive but not decisive.
- **Weight:** 0.5.
- **Change my mind:** A close above 106 would lift it; below 96 I cut.

### e72d2b35d1 (ETH)
- **Read:** The top was 129, and there is a double bottom near 79 (days -64 and -44). Price recovered to 100–103 and is now consolidating at 95–104 on very low volume. Overhead supply sits from 105 to 112.
- **Weight:** 0.5.
- **Change my mind:** Below 95 or above 104.

### aa2883b7a4 (SOL)
- **Read:** The low was 78.8, followed by a bounce to 110 (day -36). That bounce faded with lower highs (103.4, 101.6, 98) down to 92.5 (day -8). The latest move retook 100.
- **Weight:** 0.45. There is a slight downward lean from the lower highs.
- **Change my mind:** Below 92.5 I go lower; above 104 I go neutral or higher.

### 8a1c435900 (AVAX)
- **Read:** Price fell from about 160 to a capitulation low of 88.5 (day -51). Since then it has held a wide 94–110 range and sits in the middle at 100.
- **Weight:** 0.5.
- **Change my mind:** Below 94 or above 110.

### f6de8d73cb (XRP)
- **Read:** Price fell from about 150 to 98 (day -45). The bounce reached 115, then made lower highs at 113 and 108. Price has now dropped to about 100, near support at 98.
- **Weight:** 0.4.
- **Change my mind:** Below 98 I go to 0.25; above 111 I return to 0.5.

### 6595c4ef4c (DOGE)
- **Read:** A persistent decline from 171 (day -87). The lower highs run 133 → 114.5 → 108.7 → 106.8 → 103, pressing down on support around 98.
- **Weight:** 0.35.
- **Change my mind:** Above 107 I go back to neutral; below 98 I go lower.

### a2a193a95e (ADA)
- **Read:** The crash bottomed at 71.1 (day -45). A spike to 102.8 faded to 79–83. Since then the lows have been rising (71 → 79 → 83), and there was a high-volume push to 108.8 (day -3). Price is now holding about 100.
- **Weight:** 0.6. Momentum is turning up.
- **Change my mind:** Below 93 I return to 0.5 or lower.

{"fe9379038a (LINK)": 0.5, "1997b81169 (DOT)": 0.35, "25d4fa7379 (BTC)": 0.5, "92b61d9dab (LTC)": 0.5, "e72d2b35d1 (ETH)": 0.5, "aa2883b7a4 (SOL)": 0.45, "8a1c435900 (AVAX)": 0.5, "f6de8d73cb (XRP)": 0.4, "6595c4ef4c (DOGE)": 0.35, "a2a193a95e (ADA)": 0.6}

## Entscheidung 2026-08-16

**Strategy:** Start at 0.5 and move away from it only when the structure over the last 1 to 3 months is clear. That means higher lows with a breakout for a long tilt, or a series of lower highs with price pressing on support for a short tilt. Tilts stay modest, at most ±0.2, because every change in weight costs money. A tight range with no clear structure stays at 0.5.

### f1c761890d (LINK)
- **Read:** The price peaked near 114 at day −98 and crashed to about 75 at day −72. It then built a base between 75 and 92 for about two months, with rising lows at 74.7, 75.4 and 84. In the last week it broke out of the 85–90 range to about 101 on above-average volume, and the high on day −1 was 103.8.
- **Weight:** 0.65. The recovery is constructive and the breakout has volume behind it.
- **Change my mind:** a close below 92 (the breakout has failed). A close above 104 would support adding.

### 9c23166e10 (AVAX)
- **Read:** The price crashed from about 165 to a low of 89.7 at day −58. Since then it has been in a range from 95 to 111 and has not trended. The spike to 108.6 on day −1 was rejected, and it now sits mid-range at 100.
- **Weight:** 0.45. The range gives no edge, and the latest rally attempt failed.
- **Change my mind:** a close above 110 would make me go up; a close below 95 would make me go down.

### 788cb9bf7e (LTC)
- **Read:** The price fell from 137 to 92 and then recovered to 108 at day −28. Since then it has slipped slowly back to about 100 on fading volume. Support is at 98, and resistance is at 104–109.
- **Weight:** 0.5. The pullback is orderly and there is no clear signal either way.
- **Change my mind:** a close below 98, which would go down; a close above 105, which would go up.

### 8b1ce137f1 (DOT)
- **Read:** This is a persistent downtrend from about 219 to 100. Each rally has peaked lower: 137 at day −62, 119 at day −41, and 114.6 at day −12. The price is now drifting down toward the 98.6 low from day −20.
- **Weight:** 0.3. The lower-high structure is clear.
- **Change my mind:** a close above 115, which would break the pattern of lower highs.

### 92bb0a3c16 (ETH)
- **Read:** The price crashed from 131 to 80 and then recovered steadily to the 98–104 zone. It is now coiling very tightly around 100 with very low volume. The lows since day −45 have been rising.
- **Weight:** 0.5. The structure is mildly constructive, but the price is coiling with no direction yet.
- **Change my mind:** a close below 97 would make me go down; a close above 105 would make me go up.

### e683ca39e7 (DOGE)
- **Read:** The price went from 170 to 111 and then slid further. Rally peaks have been lower each time: 133, 114 and 108. It is now flat at about 100 in a 97–105 range on very thin volume. The downtrend is flattening but has not reversed.
- **Weight:** 0.4. The trend is still down, but the momentum is fading.
- **Change my mind:** a close below 97 would make me go lower; a close above 106 would bring it back to neutral or a long tilt.

### e04d617520 (XRP)
- **Read:** The price fell from 156 to 102, bounced to 119, and has since made lower highs at 117, 115 and 112. It has drifted to about 100, which is a test of the 101–102 lows from about day −51. Recent closes are the lowest since the crash.
- **Weight:** 0.35. The trend is down and the price is pressing on support.
- **Change my mind:** a close above 110, which would be a higher high.

### c0ebcf954c (SOL)
- **Read:** The price crashed to 80.6 and recovered to 112. It then pulled back to 94.6 at day −15 and has firmed to 100–102 since. The range is 95–105, and the low at 94.6 is a higher low.
- **Weight:** 0.5. The price is mid-range.
- **Change my mind:** a close below 95 would make me go down; a close above 105 would make me go up.

### dca8b7a641 (BTC)
- **Read:** The price fell from 131 to 92 and recovered to a range of 99–106, where it has stayed for about six weeks. It now sits at 100, near the bottom of that range, on low volume.
- **Weight:** 0.5. The range gives no edge.
- **Change my mind:** a close below 98.5 would make me go down; a close above 106.5 would make me go up.

### efa90b270b (ADA)
- **Read:** The price crashed from 167 to 79. It then had sharp spikes, to 114 at day −43 and to 121 at day −10, and both faded. It has fallen for about seven days from 115 back to 100. The lows are still higher, at 79 and then 87.7, but this window is volatile and the price keeps giving rallies back.
- **Weight:** 0.45. The recovery structure is offset by a steady sell-off from the last peak.
- **Change my mind:** a close below 93 would make me go to about 0.3; a close back above 110 would bring it back to about 0.55.

{"f1c761890d (LINK)": 0.65, "9c23166e10 (AVAX)": 0.45, "788cb9bf7e (LTC)": 0.5, "8b1ce137f1 (DOT)": 0.3, "92bb0a3c16 (ETH)": 0.5, "e683ca39e7 (DOGE)": 0.4, "e04d617520 (XRP)": 0.35, "c0ebcf954c (SOL)": 0.5, "dca8b7a641 (BTC)": 0.5, "efa90b270b (ADA)": 0.45}

## Entscheidung 2026-08-23

**Strategy:** Start from 0.5 and move only on clear structure. A strong breakout from a long base can keep running, so it gets no penalty. A vertical spike that leaves a large rejection wick, or one that runs into heavy resistance from earlier in the window, is more likely to retrace, so it gets a modest cut below 0.5. I do not go above 0.5 on a move that has just finished a 20–50% run in four days.

## 31050834db (XRP)
- **Read:** The decline from about 105 (day −159) bottomed out in a tight 65–67 base. Over the last five days price went almost straight up, about 52%. Day −1 traded 90.6–111.8 on 6× volume and closed near its open at 96.2, which looks like exhaustion. Day 0 is consolidating at 100. Support sits at 90–94, resistance at 105–112.
- **Weight:** 0.4. The wick and volume climax suggest the move is extended, but there is no breakdown yet.
- **Change my mind:** a close above 112 means the spike is being accepted (raise). A close below 90 means a failed spike (cut further).

## 89ec2be8ee (ETH)
- **Read:** The base was 75–78. A clean gap-up on day −4 was followed by 102 on day −2 and a shallow pullback. There is no big rejection wick, and price is back at the 6-month highs near 100 (day −128). Support is 95.6, then 91.
- **Weight:** 0.5. The breakout is orderly, but it is testing a prior high.
- **Change my mind:** below 95 (lower), or a close above 103 (higher).

## cd682268bb (DOGE)
- **Read:** The base was 73–77. The spike reached 107.9 on day −1, which also traded down to 88.8, a very wide, unstable bar. Above, the earlier breakdown zone at 107–117 is heavy resistance. Support is 95, then 89.
- **Weight:** 0.45. The volatile bar sits right under supply.
- **Change my mind:** above 108 (raise), below 89 (cut).

## 34971f2e57 (LINK)
- **Read:** Price had already been making higher lows from 70 to 82 before the spike, so the trend started before the burst. The spike reached 109.3, and price is holding above the prior high of 94 from day −105. Support is 94.7–95.3.
- **Weight:** 0.5. The structure is constructive but extended.
- **Change my mind:** below 94.7 (lower), above 109 (raise).

## 4714977bb4 (LTC)
- **Read:** The base was 83–88, and the move was moderate at about 18% to a 106 high. Older resistance sits at 110–115. Support is 96–97.
- **Weight:** 0.5. There is no clear edge either way.
- **Change my mind:** below 96 (lower), a close above 106 (raise).

## 21d17a4804 (SOL)
- **Read:** The base was about 79. The spike reached 107.7, then day −1 reversed to close at 98.3. That puts price at the prior high zone of 101–103 from day −104. Support is 92–96.
- **Weight:** 0.45, because of the rejection wick at resistance.
- **Change my mind:** above 108 (raise), below 92 (cut).

## 7b9d100121 (ADA)
- **Read:** The bigger picture is a downtrend from 130. Two earlier spikes already faded: day −50 reached 88 and gave it back to 73, and day −17 reached 93 and gave it back to 77. The current spike reached 113.8 and closed at 99.6. Support is 92–94.
- **Weight:** 0.35. In this window, spikes have repeatedly failed.
- **Change my mind:** a close above 114 (raise), below 92 (cut further).

## a10661a54b (DOT)
- **Read:** Price has fallen from about 179 to 82, a long run of lower highs. The spike reached 111.2 and reclaimed the old breakdown area of 98–109, but resistance stays dense up to 130. Support is 94–97.
- **Weight:** 0.45. This is still a counter-trend bounce.
- **Change my mind:** above 112 (raise), below 94 (cut).

## 25c7787f27 (AVAX)
- **Read:** Price fell from about 137 to an 80–90 range. The spike reached 109.3 with a rejection back to 98.5. The overhead breakdown zone runs 105–118. Support is 92–95.
- **Weight:** 0.45. Price is extended into supply.
- **Change my mind:** above 110 (raise), below 92 (cut).

## 46c7d50754 (BTC)
- **Read:** The base was 80–84. The spike reached 102.3, followed by a quiet inside day with falling volume, which looks like digestion rather than rejection. Prior highs are at 105–106. Support is 97–98.
- **Weight:** 0.5. The action is clean, but there is no strong edge.
- **Change my mind:** below 97 (lower), a close above 106 (raise).

{"31050834db (XRP)": 0.4, "89ec2be8ee (ETH)": 0.5, "cd682268bb (DOGE)": 0.45, "34971f2e57 (LINK)": 0.5, "4714977bb4 (LTC)": 0.5, "21d17a4804 (SOL)": 0.45, "7b9d100121 (ADA)": 0.35, "a10661a54b (DOT)": 0.45, "25c7787f27 (AVAX)": 0.45, "46c7d50754 (BTC)": 0.5}

## Entscheidung 2026-08-30

**Strategy:** I start at 0.5 and only move away from it on clear structure. If a breakout holds above its prior range and the long-term trend is no longer falling, I lean long (0.55–0.6). If a spike is fading with lower highs inside a longer downtrend, I lean light (0.35–0.4). Each window has a level that would flip the view.

## 405da8e988 (BTC)
- **Read:** It fell from a ~105 high to 76, then based between 77 and 85 for about 80 days. A high-volume breakout ran from 83 to 102. Since then price has held a tight 99–105 range for a week on fading volume. That is constructive digestion, sitting at the old 100–105 range.
- **Weight:** 0.6. The breakout is holding and the pullbacks are shallow.
- **Change my mind:** A close below 97 undercuts the hold. A clean push above 105 would justify adding.

## 6084976159 (LINK)
- **Read:** It based between 63 and 80, then broke out sharply to 111, with a wick to 113. It has since ranged 98.6–108 and now sits at 100, near the bottom of that range. It remains above the prior swing high near 96.
- **Weight:** 0.55. The breakout is intact but it rejected hard at 113.
- **Change my mind:** Below 96, the breakout is failing. Above 108, it resumes.

## 984972e08f (SOL)
- **Read:** It based between 70 and 77, then made a staircase breakout with higher lows (86, 90, 93, 99) up to 108.7. It is pulling back to 100 and is still above the prior high of ~96.
- **Weight:** 0.6. The structure of higher lows is the cleanest in this set.
- **Change my mind:** Below 93, the higher-low sequence breaks.

## 11860401bf (ETH)
- **Read:** It based between 76 and 80, then gapped up to 104. It has held a flat 98.7–106 range for 8 days. The old 100 high from day -135 is now being tested as support.
- **Weight:** 0.55. It is holding, but range-bound.
- **Change my mind:** Below 97 is a failure. Above 106 is a continuation.

## 3f42fd9f33 (AVAX)
- **Read:** The long-term trend is down from the 140s. It based between 85 and 95, then spiked to 117 intraday and settled into a 98–108 range. It remains far below the 130s.
- **Weight:** 0.5. The breakout is real, but it sits inside a larger downtrend.
- **Change my mind:** Below 98, cut toward 0.35. Above 108, raise toward 0.6.

## 78d44bf0bd (LTC)
- **Read:** It recovered from 86 to 98 before the spike. The spike reached 115.7 and has faded steadily with lower highs (113, 110.5, 106, 104.6) back to its launch area near 98–100.
- **Weight:** 0.45. The gains are being given back, though the earlier recovery trend provides support.
- **Change my mind:** Below 98, it slips back into the pre-spike range. Reclaiming 106 would make it bullish.

## bdf3e2c6e5 (DOGE)
- **Read:** It is in a large downtrend from 140 to 84. A spike wicked to 123 and has faded with lower highs to 100. The 100–105 area was a former breakdown zone.
- **Weight:** 0.4. This looks like a fading spike inside a downtrend.
- **Change my mind:** Below 98 is weaker. Holding above 110 would be bullish.

## b74198859e (XRP)
- **Read:** It downtrended from 113 to a 73 low. Then came a climactic spike on 4–6x volume with a wick to 125. Lower highs since (114, 108.6) look like blow-off behavior. It is now at 100.
- **Weight:** 0.4.
- **Change my mind:** Below 98, cut toward 0.25. Above 109, reconsider.

## bcfbe84af6 (ADA)
- **Read:** The downtrend runs from 150 to 75, with repeated spikes that failed (99.7 → 82 and 104 → 90). The latest spike wicked to 134 and has already faded to 100.
- **Weight:** 0.35. The pattern of failed rallies is well established.
- **Change my mind:** A hold above 111 would break the pattern.

## 58a0b9fd6d (DOT)
- **Read:** It is in a persistent downtrend from 200 to ~91, with lower highs (170, 127, 110, 106). A spike wicked to 126 and faded back to 100.
- **Weight:** 0.35. The trend is still down.
- **Change my mind:** A close above 110 would make a higher high on a closing basis. A drop below 91 confirms the downtrend.

{"405da8e988 (BTC)": 0.6, "6084976159 (LINK)": 0.55, "984972e08f (SOL)": 0.6, "11860401bf (ETH)": 0.55, "3f42fd9f33 (AVAX)": 0.5, "78d44bf0bd (LTC)": 0.45, "bdf3e2c6e5 (DOGE)": 0.4, "b74198859e (XRP)": 0.4, "bcfbe84af6 (ADA)": 0.35, "58a0b9fd6d (DOT)": 0.35}

## Entscheidung 2026-09-06

## Strategy

Start at 0.5 and move only on clear evidence. I go to 0.6–0.7 when price is at or breaking 180-day highs, or holding the top of a range after a breakout with higher lows. I stay near 0.5 when heavy overhead supply or choppy failed breakouts make the move unproven. Every window here shares one shape: a sharp break around day −96, a long base, a high-volume breakout around days −18 to −15, then a pullback and a return to 100. I weight each by how clean that recovery is and how much resistance sits above it.

## 414aebfe06 (XRP)
- **Read:** The window opened near 97 and peaked at 108. It crashed to about 70 and based at 70–71 for weeks. The breakout spiked to 119 on very high volume, but that blow-off wick has not been reclaimed. Price pulled back to 92 (day −4) and is now 100, which is the mid-range of the pre-crash trading. The key support/resistance levels are 92 and 104–107.
- **Weight:** 0.55. The base and breakout are constructive, but the failed spike caps upside for now.
- **Change my mind:** a close below 92 cuts to 0.4; a close above 107 raises it.

## b0e2590f6f (LINK)
- **Read:** This is a persistent uptrend from 68 to 100 with higher lows: 53 → 55 → 60 → 83. Today it broke to a new 180-day high, through the 93.7 spike high, on 1.7× volume. There is no overhead supply.
- **Weight:** 0.7. This is the cleanest trend breakout in the set.
- **Change my mind:** below 83, the post-breakout pullback low.

## 4ebcadb29b (ETH)
- **Read:** The 75 base produced a breakout to 101. Since then price has held a tight 94–101 range for two weeks and now sits at the top of it. The prior window highs were about 96–98, so this is already above the pre-crash range.
- **Weight:** 0.6. A constructive flag, but it has not broken out yet.
- **Change my mind:** below 93.7.

## 0885789cf5 (DOGE)
- **Read:** The prior high was 130 (day −115) and the stock fell to 76. The spike reached 111 intraday, pulled back to 88, and is now 100. The 104–110 zone overhead held a lot of prior trading and is resistance. Swings are wide.
- **Weight:** 0.5. Too much overhead supply and noise to lean long.
- **Change my mind:** above 105 → 0.6; below 88 → 0.35.

## aa2f111ee5 (DOT)
- **Read:** A long downtrend ran from 155 to a 76 low. The spike to 105 failed, and the pullback held 82.5. Since then there is a series of higher lows (82.5, 85.6, 86) and a rally to 100 on rising volume. The longer-term trend is still down from 130+.
- **Weight:** 0.55. The short-term turn is real, but the bigger trend has not repaired.
- **Change my mind:** below 85.

## 15d135fa3c (SOL)
- **Read:** Price is up from 81 at the start of the window. The breakout made a high close of 102.4 at −10, pulled back to 91.4, and is now 100 with higher lows. It is well above the old 92 highs.
- **Weight:** 0.65.
- **Change my mind:** below 91.

## 2ac9473f1f (AVAX)
- **Read:** Price fell from 120–130 to a 72 low. It based at 80–85, broke out to a 105 wick, pulled back to 88.7, and closed today at 100 with steady higher lows. Pre-crash support at 113 is the next resistance overhead.
- **Weight:** 0.55.
- **Change my mind:** below 89.

## 336bf94426 (ADA)
- **Read:** Price fell from 130 to 62. It has a history of failed rallies: 89 at −64 and 95 at −31 both fully reversed. The latest spike hit a 115.7 wick, retreated to 84.8, and is back to 100. The structure is choppy, with 104–112 overhead.
- **Weight:** 0.5. The repeated false breakouts argue against conviction.
- **Change my mind:** below 85 → 0.35; a close above 104 → 0.6.

## f31e5b5a66 (LTC)
- **Read:** Price fell from about 100–110 to 74, recovered gradually, and the spike reached 100.9. It pulled back to 86. A strong 2.3× volume day (−1) pushed it back to 100, which is the old range midpoint, and higher lows are intact.
- **Weight:** 0.6.
- **Change my mind:** below 87.

## 5672465f96 (BTC)
- **Read:** The pre-crash peak was 102 and the low was 72. Price based at 78–81, broke out to 99, then consolidated tightly at 95–101 on fading volume. It is now 100, just under the 101–102 resistance.
- **Weight:** 0.6. A tight, orderly flag.
- **Change my mind:** below 94.9.

{"414aebfe06 (XRP)": 0.55, "b0e2590f6f (LINK)": 0.7, "4ebcadb29b (ETH)": 0.6, "0885789cf5 (DOGE)": 0.5, "aa2f111ee5 (DOT)": 0.55, "15d135fa3c (SOL)": 0.65, "2ac9473f1f (AVAX)": 0.55, "336bf94426 (ADA)": 0.5, "f31e5b5a66 (LTC)": 0.6, "5672465f96 (BTC)": 0.6}

## Entscheidung 2026-09-13

**Strategy:** Start every window at 0.5. Go modestly above 0.5 only when a breakout above the prior base has held, with higher lows and support close below. Go below 0.5 when the bigger trend is down or rallies keep failing at spike highs. Below 0.35 or above 0.65 needs strong evidence, and none of these windows has it.

**15128f5944 (LINK)**
- **Read:** Price fell from about 87 to 64 (day −100), then based in the 65–77 range. A breakout from 85 ran to 107 with heavy volume, and a second push reached 122 (day −7). It has since slid back to 100.
- **Levels:** Price is still well above the old window highs near 97. Support is 97–99 (lows on days −14 to −11). Resistance is 108, then 122.
- **Weight: 0.55.** The breakout structure is intact, but the 122 rejection limits the upside case.
- **Change my mind:** a close below 97.

**03f64c2a7c (LTC)**
- **Read:** Price crashed from 112 to 77, recovered to about 89, then based at 82–85. It broke out to 100 and retested 89 (day −14). It then pushed to 110.6 (day −6) but was rejected.
- **Levels:** Range is 96–103 within a wider 89–110. Overhead supply sits at 108–112.
- **Weight: 0.5.** Price is in the middle of the range and the signals conflict.
- **Change my mind:** a close below 96 or above 103.

**63618a6543 (ETH)**
- **Read:** After a crash to 61, price built a tight base at 75–77. A gap breakout took it to 91–102, and it has held 95–103 for three weeks with higher lows.
- **Levels:** Price is above the earlier window high of 99.5. Support is 95–96.
- **Weight: 0.6.** The breakout has held cleanly.
- **Change my mind:** a close below 95.

**94017b9970 (DOGE)**
- **Read:** Price fell from 143 to 86 and based at 84–86. A spike to 122 failed. Since then the highs have stepped down (122, then 115.5, then 111).
- **Levels:** Support is 97–98. Price sits far below the old 130–140 zone.
- **Weight: 0.45.** The highs keep fading.
- **Change my mind:** a close below 97 means cut further; a close above 111 means raise.

**9731fb776a (DOT)**
- **Read:** This is a long downtrend from 162 to 75. A blow-off spike to 128.5 (day −5) on 4x volume collapsed immediately back to 100.
- **Levels:** Resistance is 110–112. Support is 95, then 88.
- **Weight: 0.35.** This is a failed spike inside a downtrend.
- **Change my mind:** a reclaim of 110.

**746c44e95c (BTC)**
- **Read:** Price fell from 108 to 77 and based at 82–85. It broke out to about 100–106 and has held a tight, quiet 99.5–106 range for three weeks.
- **Levels:** Support is 99. Resistance is 106–108.
- **Weight: 0.6.** The consolidation above the breakout looks orderly.
- **Change my mind:** a close below 99.

**8476d8f62a (SOL)**
- **Read:** Price crashed to 61, recovered to 83, and based at 72–78. A breakout ran to 111 (day −17), and price is now 100.
- **Levels:** Price is above the prior high of 99. Support is 98. Resistance is 108–111.
- **Weight: 0.55.** The breakout is holding, but only just.
- **Change my mind:** a close below 98.

**9203c6882e (ADA)**
- **Read:** This is a long decline from 142 to 70. Three spikes have failed: 98, 104, and 127. The most recent highs are 114 and 111. The lows are rising, though: 70, 76, 85, 93.
- **Levels:** Support is 93–94. Resistance is 110–114.
- **Weight: 0.45.** Repeated failures outweigh the rising lows.
- **Change my mind:** a close below 93, or above 111.

**c2bca07d9a (AVAX)**
- **Read:** Price fell from 140 to a base of 85–95. It broke out to 114, then made a lower high at 112.5. It is now 100.
- **Levels:** Range is 96–112. The 120–140 zone above is far away.
- **Weight: 0.5.** This is neutral mid-range action.
- **Change my mind:** a close below 96 or above 108.

**170a6e7da3 (XRP)**
- **Read:** Price drifted from 113 down to 74. A breakout on huge volume (6x) spiked to 126.7 and was rejected. Price has held 98–110 since.
- **Levels:** Support is 97–98. Resistance is 108–110.
- **Weight: 0.5.** Strong demand on the breakout is balanced by the spike rejection.
- **Change my mind:** a close below 97.

{"15128f5944 (LINK)": 0.55, "03f64c2a7c (LTC)": 0.5, "63618a6543 (ETH)": 0.6, "94017b9970 (DOGE)": 0.45, "9731fb776a (DOT)": 0.35, "746c44e95c (BTC)": 0.6, "8476d8f62a (SOL)": 0.55, "9203c6882e (ADA)": 0.45, "c2bca07d9a (AVAX)": 0.5, "170a6e7da3 (XRP)": 0.5}

## Entscheidung 2026-09-20

## Strategy

The base weight is 0.5. I move to 0.6–0.7 when price sits at or above the top of its recent range, with higher lows and a clear invalidation level. I move below 0.5 only for a broken structure or a climactic, exhausted spike. Volatile, rangebound windows stay at 0.5, because trading them costs more than it earns.

## e1dfc4fb17 (LINK)
- **Read:** The stock crashed to about 56 around day -107 and built a base between 57 and 67 that lasted two months. It broke out from day -40 and rallied to 95 and then 109 (day -13). It pulled back to 85–87, which held as a higher low, and has now recovered to 100. The trend has turned up.
- **Weight:** 0.65. The structure is constructive with higher lows.
- **Change mind:** A close below 86.

## d0ab1fc5a5 (DOT)
- **Read:** The stock fell from 123 to about 66 over five months. At day -12 a climactic spike reached 113, then collapsed to 82. It has now recovered to 100 on heavy volume. It is very volatile, and the old supply zone of 110–120 sits overhead.
- **Weight:** 0.55. The recovery is real, but the swings are wild.
- **Change mind:** Below 82 I cut; a hold above 110 would justify more.

## 58d1c0c236 (ETH)
- **Read:** A gap from 72 to 95 at days -32 to -30 was followed by a tight consolidation between 89 and 97 that lasted a month. Price is now pressing the top of that range at about 100. This is a clean flag.
- **Weight:** 0.65.
- **Change mind:** A close below 89.

## d66c03dc33 (LTC)
- **Read:** The prior high was 103 (day -133). The stock crashed to 69, then recovered steadily to 80, broke out to 90–94, held 81–94, and has now reached 100. It is retesting the old highs at 101–103.
- **Weight:** 0.6.
- **Change mind:** A close below 86.

## 608b165970 (SOL)
- **Read:** A breakout from a 66–70 base ran to 98, followed by a 86–96 range. A strong push at day -2 reached 102.8, and price is holding around 100. Higher lows are in place.
- **Weight:** 0.6.
- **Change mind:** A close below 86.

## bd5680654f (BTC)
- **Read:** Price is back at the prior major highs of 100–102 (days -138 to -133) after a crash to 73 and a full recovery. It has ranged between 92 and 101 for a month with low volatility. This is a test of resistance.
- **Weight:** 0.55.
- **Change mind:** Below 92 I go to 0.4; a close above 102 would justify going to 0.7.

## e964a0de09 (XRP)
- **Read:** A blow-off spike reached 120 on a volume ratio of 5.9 (day -29). Since then price has chopped between 89 and 106 on high volume, with no progress. It is also back in its old 95–105 range.
- **Weight:** 0.5.
- **Change mind:** Below 88 I go to 0.3; a close above 107 would justify going to 0.65.

## b92e4889c0 (DOGE)
- **Read:** The old high was 135 (day -129). The stock crashed to 79, spiked to 115 (day -29), and has since ranged between 90 and 109. It is still well below the old supply zone, and the highs have stalled near 104–109.
- **Weight:** 0.5.
- **Change mind:** Below 89 I go to 0.3; above 109 I go to 0.65.

## 0ad0c9243a (ADA)
- **Read:** Highs were 124 earlier. A crash to 61 was followed by repeated spike-and-fade rallies (to 88 and 92, then 113 at day -29). It has ranged between 84 and 102 since. This is erratic and event-driven.
- **Weight:** 0.5.
- **Change mind:** Below 84 I go to 0.3; above 103 I go to 0.6.

## 4d622570ba (AVAX)
- **Read:** The stock declined from 90 to 50, based between 54 and 60 for three months, and ground up to about 72. Then it went vertical: +23% (day -1) and +12% (day 0) on volume ratios of 3.9 and 6.1, with a wide day-0 range of 83.4 to 101.4. This looks like a news gap and climax. Similar spikes in comparable structures often retrace a large part of the move, and there is no structure above 72 to lean on.
- **Weight:** 0.4. This is a modest underweight because the move is extended, and I am not shorting into strength.
- **Change mind:** If it holds above 95 for a week, back to 0.5–0.6. If it closes below 83, cut to 0.2.

{"e1dfc4fb17 (LINK)": 0.65, "d0ab1fc5a5 (DOT)": 0.55, "58d1c0c236 (ETH)": 0.65, "d66c03dc33 (LTC)": 0.6, "608b165970 (SOL)": 0.6, "bd5680654f (BTC)": 0.55, "e964a0de09 (XRP)": 0.5, "b92e4889c0 (DOGE)": 0.5, "0ad0c9243a (ADA)": 0.5, "4d622570ba (AVAX)": 0.4}

## Entscheidung 2026-09-27

**Strategy:** Start at 0.5. Tilt toward long (0.65–0.7) when price has broken above the window's prior major highs and is making higher lows. Stay near 0.5 when price is still below older resistance, or when the move is parabolic or whipsawing. Change only on a clear break of structure.

### 600cc1e3e4 (ETH)
- **Read:** The old high was about 91.7. The base at 70 broke out at day -39, consolidated between 89 and 95, then broke out again to about 103.
- **Structure:** Price is holding 99–101 on low volume. Lows are rising: 87.7, then 96.7. It is at a clean new 180-day high.
- **Weight:** 0.7.
- **Change my mind:** a close below 96.

### e558d83854 (BTC)
- **Read:** Price has moved just past the old high of about 98, with a 180-day high at 103.5.
- **Structure:** It is an uptrend from 75, with lows at 88.7 and then 98.1. The margin over the old high is thinner than in 600cc1e3e4 (ETH).
- **Weight:** 0.65.
- **Change my mind:** a close below 95.

### cf16ab1bbb (SOL)
- **Read:** Price is far above the prior range high of about 80.7. It has trended steadily from 62 to 100.
- **Structure:** Lows are rising: 78.5, then 92.2, then 98.5. Volume is firm on up days.
- **Weight:** 0.7.
- **Change my mind:** a close below 92.

### a05f9076a4 (ADA)
- **Read:** Price is still below the older highs at 107–113. It is very volatile, with a range of 91–104 over the last week.
- **Structure:** Lows are rising (74.6, then 91.3), but the overhead supply limits conviction.
- **Weight:** 0.55.
- **Change my mind:** a close below 91 would take me to 0.4. A close above 105 would raise the weight.

### 788f0632ba (DOGE)
- **Read:** Price is well below the older highs at 116–122. The spike to 109 on day -5 reversed sharply to 94, which looks like a blow-off with a failed follow-through.
- **Structure:** Price is choppy between 94 and 103.
- **Weight:** 0.5.
- **Change my mind:** a close below 94.

### 2a3cfecfb1 (AVAX)
- **Read:** Price jumped from 70 to 105 in two days on huge volume, gave back to 92, and has recovered to 100. It sits above the old high of about 96.
- **Structure:** This is a parabolic event move. The trend is up, but it is not yet settled.
- **Weight:** 0.55.
- **Change my mind:** a close below 91.

### dd1bffceab (XRP)
- **Read:** The old highs were about 102, with a spike to 112 on day -36. Price is ranging between 83 and 109.
- **Structure:** Lows are rising (82.2, then 95.7), but price is still inside a wide, volatile range.
- **Weight:** 0.55.
- **Change my mind:** a close below 95. A close above 108 would raise the weight.

### ab08489e66 (LTC)
- **Read:** On day -3, price gapped from 87 to 101 on 6.7× volume, and the gap has held for three days at 99–102.
- **Structure:** This is a decisive break of the old high of about 85, at a new 180-day high.
- **Weight:** 0.65.
- **Change my mind:** a close below 96, which would signal the gap failing toward 87.

### c81a502156 (DOT)
- **Read:** Price is below the older highs at 105–113. It spiked to 101 on day -19, fell to 73.7, and has recovered to 100.
- **Structure:** The swings are very wide, and price is now retesting the spike high.
- **Weight:** 0.55.
- **Change my mind:** a close below 85.

### b0e321bc75 (LINK)
- **Read:** Price is far above the prior highs of about 77.5, at a new high of 103.4.
- **Structure:** It is a persistent uptrend with rising lows: 75.7, then 86.0, then 99.2.
- **Weight:** 0.7.
- **Change my mind:** a close below 93.

{"600cc1e3e4 (ETH)": 0.7, "e558d83854 (BTC)": 0.65, "cf16ab1bbb (SOL)": 0.7, "a05f9076a4 (ADA)": 0.55, "788f0632ba (DOGE)": 0.5, "2a3cfecfb1 (AVAX)": 0.55, "dd1bffceab (XRP)": 0.55, "ab08489e66 (LTC)": 0.65, "c81a502156 (DOT)": 0.55, "b0e321bc75 (LINK)": 0.7}
