# E-010: was die KI gedacht hat (Set A)

Volle Antwort des Deciders pro Entscheidungswoche, unverändert. Er sah weder Datum noch Coin-Namen; die Namen in Klammern sind erst danach eingesetzt. Gesendeter Prompt und Daten: runs/<set>/<woche>/requests.json.

## Entscheidung 2026-07-05

**Strategy:** I classify each window by where day 0's close sits relative to the multi-month range it traded in before the breakdown around day -33.
- **Down:** price is still below that range's floor and the window shows lower highs. Weight 0–0.15, with the higher end only when a base is forming.
- **Sideways:** price has climbed back inside the prior range. Weight about 0.4.
- **Up:** price is above the range with higher highs and higher lows. Weight 0.8–1.0.

## aae74fdb4d (XRP)
Regime: down
- **Read:** The window falls from 199 to 100. From day -150 to -34 it ranged 113–128, then broke down at day -33 and bottomed at 87.2 on day -9. The last 4 days bounced to 100 on below-average volume. Resistance is 102.3, then 111.8 (day -20 high), then the old floor near 113.
- **Weight:** 0.1. A bounce inside a downtrend isn't a reversal yet.
- **Change my mind:** a close above 112 means it has reclaimed the old range.

## 8629969c90 (LINK)
Regime: down
- **Read:** The window falls from 174 to 100. It ranged 105–134 before failing at day -33, with a low of 86.9 on day -10. Volume on the current bounce is thin (0.34–0.38). Resistance is 101.5, then 106.7.
- **Weight:** 0.1.
- **Change my mind:** a close above 107.

## 7afeaebb2f (ETH)
Regime: down
- **Read:** The window falls from 185 to 100. The prior range was 112–135, then the breakdown came at day -33. The low is 84.7 on day -9, and it has bounced to 100. Resistance is 101.3, then 103.6 (day -20 high).
- **Weight:** 0.1.
- **Change my mind:** a close above 104, which would also put in a higher high.

## 421bf4ff56 (DOGE)
Regime: down
- **Read:** The window falls from 193 to 100. A rally to 152 on day -52 failed, followed by a steep slide with a low of 89.3 on day -5. Resistance is 101.9, then 114–118.7.
- **Weight:** 0.1. The lower-high structure is clear.
- **Change my mind:** a close above 115.

## 6f3abbff9d (BTC)
Regime: down
- **Read:** The window falls from 147 to 100. The prior range of 115–130 broke at day -33. The low is 90.8, and price has bounced to 100. Resistance is 100.5, then 105.7 (day -20).
- **Weight:** 0.1.
- **Change my mind:** a close above 106.

## 4ce1e8d799 (AVAX)
Regime: down
- **Read:** The window falls from 211 to 100. The prior range was 125–150. On day -16 it capitulated to 82 on 3x volume. Since then it has made higher lows (86, then 92, then 97.5), which is a tentative base. Resistance is 102.8, then 102.2.
- **Weight:** 0.15. It is still below the prior range, but the base earns a small position.
- **Change my mind:** a close above 103 raises the weight; a close below 86 sends it to 0.

## 0d757fb83a (LTC)
Regime: down
- **Read:** The window falls from 183 to 100. The prior range was 110–130. The low is 85.7 on day -10. Day 0 closed at the top of its range, 100, with resistance just above at 101.2.
- **Weight:** 0.15.
- **Change my mind:** a close above 101.5 that holds; below 89 the trend has resumed.

## d3e1ac11a3 (DOT)
Regime: down
- **Read:** The window falls from 254 to 100. It has made a series of lower highs at 188, 186, 157 and 118.8. The low is 90.2 on day -7. Resistance is 102.2, then 118.8.
- **Weight:** 0.1.
- **Change my mind:** a close above 119.

## 013a92f014 (ADA)
Regime: down
- **Read:** The window falls from 221 to 100. It crashed to 72.9 on day -10. Over the last 4 days it rallied in a V from 76 to a high of 105.5 on about 2x volume, and that is a sharp short-covering-style move. The prior range of 120–140 is far overhead. Resistance is 105.5; support is 92, then 85.
- **Weight:** 0.15. The momentum is real but the regime is still down, and the move is overextended.
- **Change my mind:** a close above 106 that holds; below 92 the rally has failed.

## 178edd3ca2 (SOL)
Regime: sideways
- **Read:** The window falls from 173, but from day -150 onward it ranged roughly 95–120. It broke down to 73.7 on day -29 and then made higher lows (76.4, then 78.5, then 88). Price is now back at 100, inside the old range floor of 98–100. Resistance is 102.9, then 110–113.
- **Weight:** 0.4. The breakdown was reclaimed and price is back in the range.
- **Change my mind:** below 92 makes it down and sends the weight to about 0.1; a close above 110 makes it up.

{"aae74fdb4d (XRP)": 0.1, "8629969c90 (LINK)": 0.1, "7afeaebb2f (ETH)": 0.1, "421bf4ff56 (DOGE)": 0.1, "6f3abbff9d (BTC)": 0.1, "4ce1e8d799 (AVAX)": 0.15, "0d757fb83a (LTC)": 0.15, "d3e1ac11a3 (DOT)": 0.1, "013a92f014 (ADA)": 0.15, "178edd3ca2 (SOL)": 0.4}

## Entscheidung 2026-07-12

**Strategy:** I name each window's regime from its swing structure since the sharp drop around day -40, read against the old pre-drop range.
- **Up:** higher highs and higher lows. Weight 0.6–0.8.
- **Down:** lower highs and lower lows, still under the broken range. Weight 0.0–0.1.
- **Sideways:** price is boxed between a defined low and high with no clear sequence. Weight 0.3–0.4, scaled by where price sits in the box.

## 7f9521d839 (LINK)
Regime: down
- **Read:** Before the drop, the range was 102–120 and the peak was 134 at day -63. Price broke down to 87.5 at -36.
- **Structure since then:** The bounces topped at 107.5 (day -27) and 102.2 (day -8), so the highs are falling. The lows held at 87.7.
- **Now:** Price sits at 100, under the old range floor of 102, on fading volume.
- **Weight:** 0.1, because the highs keep failing below the old support.
- **Change my mind:** a close above 108, or a break below 87.5 to confirm the downtrend.

## 9904a502e0 (DOGE)
Regime: down
- **Read:** The drop went from 140 to 106.8 (day -36). The bounce reached 127 (day -30).
- **Structure since then:** Price fell to a new low of 95.6 (day -12). The rebound highs were 109.2 and then 104, so the highs keep stepping down.
- **Now:** Price is 100, far below the 136–155 area where it traded before the drop.
- **Weight:** 0.0. Both the lows and the highs are falling.
- **Change my mind:** a close above 110.

## 05c26a6eda (ADA)
Regime: down
- **Read:** Price collapsed from 145 to 91.7, bounced to 117, then made a lower low at 85.3 (day -17).
- **Structure since then:** A spike to 123.4 (day -8) gave back its whole gain and price is now at 100.
- **Now:** The swings are very wide, and the failed spike points to sellers in control.
- **Weight:** 0.05.
- **Change my mind:** a close above 118, or a break below 85 to confirm.

## bfdc6cb672 (BTC)
Regime: down
- **Read:** Price fell from the 115–129 range to 92.7. The bounce reached 105.5.
- **Structure since then:** A slightly lower low came at 90.6 (day -11). The highs since then are lower, at 101.4.
- **Now:** Price is at 100. Volatility is low and the drift is slightly lower.
- **Weight:** 0.1.
- **Change my mind:** a close above 106.

## be12d15e9a (SOL)
Regime: up
- **Read:** The drop bottomed at 78.2 (day -36). Since then the lows have risen: 83.3 (day -17), then about 98 (days -4 and 0). The highs have also risen: 98.9 (day -27), then 109.2 (day -8).
- **Now:** Price is 100, above its roughly 96 average for the last 50 days. It is pulling back toward the breakout area of 97–99.
- **Weight:** 0.65. The structure is up, but price is still under the old 105–120 range, so I hold back from full size.
- **Change my mind:** a close below 93, which would break the higher-low sequence.

## bd15d1831c (LTC)
Regime: sideways
- **Read:** The drop went from 118 to 92.1. Since then price has stayed in a box of roughly 89.3 to 105.3.
- **Structure since then:** The highs were 105.3 and then 104.9, which is roughly flat. The low at 89.3 was only marginally lower.
- **Now:** Price is 100, in the middle of the box.
- **Weight:** 0.3.
- **Change my mind:** a close above 106 would make it up; a close below 89 would make it down.

## 7940d94047 (DOT)
Regime: down
- **Read:** The drop went from 141 to 104.7. The bounce reached 124.1.
- **Structure since then:** Price made a lower low at 94.2 (day -14). The highs since then are lower, at 107.6 and 106.
- **Now:** Price is 100. The old range was 140–160, far above.
- **Weight:** 0.05.
- **Change my mind:** a close above 108.

## 59065c620e (ETH)
Regime: sideways
- **Read:** The drop went from 111 to 83.3 (day -36). Price then made a double bottom at 83.7 (day -16).
- **Structure since then:** The highs have been capped around 101.5–102.4.
- **Now:** Price is 100, near the top of the 83–102 box. A breakout is possible but not confirmed.
- **Weight:** 0.4.
- **Change my mind:** a close above 103 would make it up; a close below 86 would cut it to 0.

## 1040034735 (XRP)
Regime: down
- **Read:** The drop went from 123 to 96.7. The bounce reached 119.1.
- **Structure since then:** Price made a lower low at 92.9 (day -16) and a lower high at 109.1 (day -8).
- **Now:** Price is 100, well under the old 120–135 range.
- **Weight:** 0.1.
- **Change my mind:** a close above 110.

## d14cdb0f8c (AVAX)
Regime: sideways
- **Read:** The drop went from 141 to 97.1. A second flush on high volume went to 88.7 (day -23), which was a lower low.
- **Structure since then:** The recovery reached 111.1 (day -8), slightly above the earlier 110.5 high. That gives a mixed structure inside a box of roughly 88.7 to 111.
- **Now:** Price is 100, after a weak day-0 bar that dipped to 98 on rising volume.
- **Weight:** 0.3.
- **Change my mind:** a close above 111.5 would make it up; a close below 93 would make it down.

{"7f9521d839 (LINK)": 0.1, "9904a502e0 (DOGE)": 0.0, "05c26a6eda (ADA)": 0.05, "bfdc6cb672 (BTC)": 0.1, "be12d15e9a (SOL)": 0.65, "bd15d1831c (LTC)": 0.3, "7940d94047 (DOT)": 0.05, "59065c620e (ETH)": 0.4, "1040034735 (XRP)": 0.1, "d14cdb0f8c (AVAX)": 0.3}

## Entscheidung 2026-07-19

**Strategy:** I set the regime from the swing structure of roughly the last 50 days, which is the period since each window's second large breakdown. I read it against the larger downtrend that started at the peak around day -70. "Up" means higher lows plus a higher high that breaks the post-crash rebound high, and gets a weight of 0.65–0.7. "Sideways" means price is held inside a defined range with no confirmed breakout, and gets 0.3–0.45 depending on where price sits in the range. "Down" means lower highs and lower lows continuing into day 0, and gets 0.1–0.15.

## 5c47945846 (LINK)
Regime: sideways
- **Read:** The peak was 129.6 (day -70). Price then collapsed to 83.4 (day -43) and retested 83.6 (day -24), so there is a double bottom near 84. Since then the lows have risen to 89.7, 93.0 and 95.5.
- **Range and resistance:** The highs are 102.6 (day -34) and 103.0 (day -4). That second high is only marginally higher, not a breakout. The range is 84–103 and the close of 100 is near the top. Volume is very light at 0.18.
- **Weight:** 0.45. The structure is constructive, but price is still stuck under 103.
- **Change my mind:** Above 104 I would move to up and raise the weight. Below 95 I would cut it.

## 18d6ed3f2a (ADA)
Regime: sideways
- **Read:** The peak was 173.6 (day -70). The low was 89.4 (day -43) and then a lower low of 83.1 (day -24).
- **Rally and retrace:** A sharp spike reached 120.3 (day -15). It fully retraced to about 93–95, and the recent lows are 93.4 and 94.9.
- **Range:** The range is 83–120 and the close of 100 is in the middle.
- **Weight:** 0.4. The failed spike offsets the higher lows.
- **Change my mind:** Above 106 I would go more long. Below 93 I would treat it as down.

## 8d6f8f61d7 (DOT)
Regime: down
- **Read:** The highs keep falling: 173 (day -70), 127.7 (day -34), 110.7 (day -13), 106.6 (day -3).
- **Lows:** The lows also keep falling: 107.8 (day -43), then 97.0 (day -21). Day 0 sold off from 102.3 to 100 with a low of 98.3, on relatively heavy volume of 0.83.
- **Weight:** 0.1.
- **Change my mind:** A close above 107 would break the lower-high sequence. Below 97 the downtrend is confirmed.

## 2b8e6d638a (DOGE)
Regime: down
- **Read:** Price fell from 163.8 (day -66). The highs since then are 127.7 (day -37), 109.6 (day -15) and 104.1 (day -5), each lower than the last.
- **Lows and range:** The lows are 107.2, then 96.0 (day -19), then 97.9. Price is coiling in a tight 98–104 band on very low volume.
- **Weight:** 0.15.
- **Change my mind:** Above 105 the lower-high sequence would be broken. Below 96 I would go fully flat.

## 514ecb76ae (BTC)
Regime: sideways
- **Read:** The peak was 128 (day -74). Price dropped to 91.4 (day -44), bounced to 104.0 (day -34), and made a low of 89.8 (day -24).
- **Range:** The recent high of 100.6 is lower than the earlier 104. The range is 90–104 and the close is 100.
- **Weight:** 0.3. This is a slightly bearish range.
- **Change my mind:** Above 104.5 I would treat it as up. Below 95.5 I would treat it as down.

## b4bf30b348 (AVAX)
Regime: sideways
- **Read:** The peak was 162.3 (day -70). The crash reached 96.3, and a capitulation low of 87.9 (day -30) came on heavy volume.
- **Rising lows:** The lows have risen since then: 92.1, 97.2, 98.6, 98.9.
- **Range:** The highs are 109.5, 110.1 and 105.7, so the range is 88–110 and the close is 100.
- **Weight:** 0.4. The lows are rising, but the highs are capped.
- **Change my mind:** Above 106 I would go more long. Below 97 I would cut.

## f2e03e258f (XRP)
Regime: sideways
- **Read:** The peak was 141.2 (day -66). The lows are 95.7 (day -43) and 91.9 (day -23), and the highs are 117.8 (day -34), 107.9 (day -15) and 103.0 (day -4).
- **Structure:** The highs are falling against a floor around 92–96. The close is 100.
- **Weight:** 0.35.
- **Change my mind:** Above 104 I would raise the weight. Below 96 I would treat it as down.

## ec7447fa2b (SOL)
Regime: up
- **Read:** The peak was 128.8 (day -69) and the low was 78.7 (day -43).
- **Higher lows and highs:** The lows have risen: 83.8 (day -24), then 96.1 (day -2). The highs have also risen: 99.6 (day -34), then 110.0 (day -15).
- **Pullback:** The current pullback to 96–100 is holding above the breakout area around 97.
- **Weight:** 0.7.
- **Change my mind:** Below 96 the higher-low structure fails. Above 104 I would add.

## 00a4562048 (ETH)
Regime: up
- **Read:** The peak was 131.7 (day -93) and 127 (day -70). There is a double bottom at 80.4 and 80.8.
- **Higher lows and highs:** The lows have risen: 92.3, 93.5, 96.3. The high of 104.0 (day -4) cleared the earlier rebound high of 98.8, so this is a clear breakout. The close is 100.
- **Weight:** 0.65.
- **Change my mind:** Below 96 I would drop to sideways. Above 104 the uptrend is confirmed.

## e8dafd7c8f (LTC)
Regime: up
- **Read:** The peak was 128.8 (day -70). The lows are 86.1 (day -43) and 83.5 (day -25), followed by higher lows at 91.2 and 93.7.
- **Breakout:** Day -1 broke above the 98–98.5 rebound highs to 101.8, with volume above average. The close of 100 is holding the breakout.
- **Weight:** 0.7.
- **Change my mind:** Below 95 the breakout has failed. Above 102 I would add.

{"5c47945846 (LINK)": 0.45, "18d6ed3f2a (ADA)": 0.4, "8d6f8f61d7 (DOT)": 0.1, "2b8e6d638a (DOGE)": 0.15, "514ecb76ae (BTC)": 0.3, "b4bf30b348 (AVAX)": 0.4, "f2e03e258f (XRP)": 0.35, "ec7447fa2b (SOL)": 0.7, "00a4562048 (ETH)": 0.65, "e8dafd7c8f (LTC)": 0.7}

## Entscheidung 2026-07-26

# T-001 Weights

**Strategy:** I classify each window from its last ~50 days.
- **Up:** the close is above the approximate 50-day average and the latest swing low is higher than the previous one.
- **Down:** the close is below the 50-day average and the swing highs are falling.
- **Sideways:** anything else.

Weights follow the regime: up 0.7–1.0, scaled by how clean the higher-low structure is; sideways 0.4; down 0.1–0.15.

## 7ba1a8eca5 (LINK)
Regime: up
- **Read:** The window opens with a crash from 134 and then ranges 95–110. A rally to 121 at day -77 failed, and price fell to a 79.4 low at day -31. Since then the lows keep rising: 79.4, 85.2, 90.7, 93.7. Today it closed at 100.0, above the recent highs of 97.8 and 99.3. The 50-day average is about 90, so price is well above it.
- **Weight:** 0.8. Higher lows plus a fresh break of the swing high, but resistance from the old range sits at 105–110.
- **Change my mind:** a close below 93.7.

## 369b9f1f81 (XRP)
Regime: sideways
- **Read:** After the drop to 90.9 at day -31, the lows rise (90.9, 94.6, 97.5) but the highs fall (116.2, 106.4, 104.6). That is a contracting triangle with price at 100, right on the 50-day average of about 100.
- **Weight:** 0.4. Neither side has broken out.
- **Change my mind:** a close above 104.6 would make it up; a close below 97.5 would make it down.

## 1e5f7e1d39 (AVAX)
Regime: sideways
- **Read:** It collapsed to 84.2 at day -37 and has ranged 91–105 since. Day -3 broke down to 92.9, then day -1 reversed to 100.5 on 1.5x volume. The latest low (91.0) is below the prior one (93.1). Price sits just above a 50-day average of about 97.
- **Weight:** 0.4. This is a range, not a trend.
- **Change my mind:** above 105.5 would make it up; below 91 would make it down.

## 63c266b8de (DOGE)
Regime: down
- **Read:** The peak was about 161 at day -73. Since then the highs keep falling: 126, 108.2, 103.0, 100.9. Lows sit at 94.7 and 93.2. Price is below a 50-day average of about 105.
- **Weight:** 0.15. Lower highs and price under the average.
- **Change my mind:** a close above 103, and especially above 108.

## 332642010f (BTC)
Regime: up
- **Read:** The low was 88.4 at day -25. The swing lows have been rising steadily since: 93.7, 94.5, 95.6, 96.5, 97.5. Price is at 100, above a 50-day average of about 96. However, the day -41 high of 102.9 has not been cleared.
- **Weight:** 0.7. The structure is up, but the overhead level is still untested.
- **Change my mind:** a close below 96.5.

## ba3ae48def (DOT)
Regime: down
- **Read:** The long decline runs from 226 to 100. The day -77 high of 171 gave way to 126, then 109.7, 108.1, 105.6 and 105.0, so the highs keep falling. Support sits at 95–96, and price is below a 50-day average of about 107.
- **Weight:** 0.15. Lower highs and price under the average.
- **Change my mind:** a close above 109.7.

## 5035e49ee7 (SOL)
Regime: up
- **Read:** The washout low was 78.3 at day -50. Higher lows followed at 83.4, 95.6 and 95.7. Price is above a 50-day average of about 95. The high of 109.4 at day -22 is a cap, and the day -5 high of 102.8 was lower than it.
- **Weight:** 0.7. Higher lows, but a lower high is still in place.
- **Change my mind:** a close below 95.6.

## 452d7a9703 (ETH)
Regime: up
- **Read:** The lows were 77.0 at day -50 and 78.4 at day -31. Since then the structure is a clean staircase of higher lows (79.2, 87.7, 92.2, 94.5) and higher highs (92.5, 99.6, 100.6). Today closed at 100, the highest close since day -55. Price is well above a 50-day average of about 88.
- **Weight:** 1.0. This is the strongest trend in the set.
- **Change my mind:** a close below 94.5.

## d3a30ab8b6 (LTC)
Regime: up
- **Read:** The lows step up from 82.1 at day -31 through 86.0, 90.2, 92.2 and 95.6. Highs rose from 96.5 to 100.1 and then 100.9. Volume increased on the push at day -8. Price is above a 50-day average of about 91.
- **Weight:** 0.9. The structure is consistent, and price is pressing against 101.
- **Change my mind:** a close below 95.6.

## 2bfe3794de (ADA)
Regime: sideways
- **Read:** The swings are wide: 83.3, then a spike to 120.5, then 93.6, then 108.9, then 100. The lows are rising (93.6, 95.1, 97.3) but the highs are falling (120.5, 108.9). Price sits on a 50-day average of about 99.
- **Weight:** 0.4. The range is volatile with no clear direction.
- **Change my mind:** above 109 would make it up; below 93.6 would make it down.

{"7ba1a8eca5 (LINK)": 0.8, "369b9f1f81 (XRP)": 0.4, "1e5f7e1d39 (AVAX)": 0.4, "63c266b8de (DOGE)": 0.15, "332642010f (BTC)": 0.7, "ba3ae48def (DOT)": 0.15, "5035e49ee7 (SOL)": 0.7, "452d7a9703 (ETH)": 1.0, "d3a30ab8b6 (LTC)": 0.9, "2bfe3794de (ADA)": 0.4}

## Entscheidung 2026-08-02

**Strategy:** I classify each window by the structure of its swing highs and lows since its last major low, read against the 180-day trend. Higher highs with higher lows is **up**, and gets a weight of 0.6–0.7. A contracting or flat range is **sideways**, at 0.3–0.4. Lower highs with lower lows, especially inside a larger decline, is **down**, at 0.1–0.15.

## 74278592b6 (XRP)
Regime: sideways
- **Read:** The price fell from a 120–135 range to a low of 96.6 (day -57) and then 92.9 (day -37). Since then it has traded in a narrowing band. Highs have stepped down (119, 109, 107, 102.7) while lows have held near 96. The longer-term trend is down, but the last 40 days are a contracting range.
- **Weight:** 0.3. There is no trend to own, and the overhead supply is heavy.
- **Change my mind:** a close above 107 would mean up. A close below 96 would mean down.

## d5f4e44dec (LTC)
Regime: up
- **Read:** The low was 87.9 on day -38. Since then the price has made higher lows (93, 96, 98.7) and higher highs (103.3, 107.7, 108). It is currently pulling back from 108 to 99–100 and still holds the 97.5–98.7 support. It remains far below the old 120s.
- **Weight:** 0.6. This is a modest uptrend that is currently pulling back.
- **Change my mind:** a close below 97 would mean sideways or down. A close above 108 would justify a higher weight.

## ea9671ce47 (ETH)
Regime: up
- **Read:** The capitulation low was about 80 (days -57 and -37). Since then highs have risen (97.2, 103.6, 105.1) and so have lows (90.9, 95.6, 96.6). The price is at 100, sitting in the upper half of a rising structure.
- **Weight:** 0.7.
- **Change my mind:** a close below 95.5. Above 105, I would add.

## 92ad74f1b9 (SOL)
Regime: sideways
- **Read:** The price spiked from 87 up to 114 (day -29). It then faded, with lower highs (107.3, 107.1, 105.3) and lows drifting down (99.7, 98.2, 95.9). For 25 days it has held a 96–107 range, and the bias inside it is soft.
- **Weight:** 0.3.
- **Change my mind:** a close below 95.5 would mean down. A close above 107.5 would mean up.

## bf1bcbe065 (ADA)
Regime: up
- **Read:** This window had the deepest crash, to 72.9 (day -38). A spike to 105.5 failed, and the price then built a base at 81–89. Today the price broke out of that base, moving from 92 to 100 on 1.7x volume. Lows are rising from 73 to about 81, and today's close clears the 93–95 resistance.
- **Weight:** 0.65. The breakout is real, but 105.5 is overhead resistance.
- **Change my mind:** a close back below 88. A close above 105.5 would confirm the up regime.

## ee3f9da443 (BTC)
Regime: sideways
- **Read:** After the 91 lows (days -38 and -32), the price has held a 96–105 range. Lows are mildly higher (96.4, 97.3, 98.3) and highs are flat around 103–105. The decline from 129 was shallower here.
- **Weight:** 0.4.
- **Change my mind:** a close above 105.5 would mean up. A close below 96 would mean down.

## 07e8c39993 (DOGE)
Regime: down
- **Read:** The top was 167 (day -80). The price then made a sequence of lower highs: 130.6, 125, 112, 106.8, 104.6, 104.1. The low drifted to 95.6 at day -1. The decline is persistent, and every rally has been sold.
- **Weight:** 0.15.
- **Change my mind:** a close above 106.5.

## 3f6d15b986 (AVAX)
Regime: sideways
- **Read:** After the 86.7 low (day -44), the price has ranged between 91 and 108. Highs are declining (108.6, 104.3, 104.5) and lows have slipped to 92.2 (day -1). Today it reversed sharply to 100 on above-average volume. The structure is a range with a slight downward lean.
- **Weight:** 0.35.
- **Change my mind:** a close above 105 would mean up. A close below 92 would mean down.

## 7ed72b1bb7 (LINK)
Regime: up
- **Read:** The low was 83.4 (days -57 and -38). Since then highs have risen (97.5, 103, 104.5, 106.3) and so have lows (89.7, 94.1, 95.5). The price is at 100 after a test of 94 that held.
- **Weight:** 0.65.
- **Change my mind:** a close below 94. Above 106.5, I would add.

## 1f279cd37f (DOT)
Regime: down
- **Read:** The price peaked at 219 (day -158) and has made lower highs throughout: 174, 131, 113.6, 112, 109.4, 104.1. Lows broke to 93 on day -2, below the earlier 99.5 floor. This is a clear downtrend.
- **Weight:** 0.1.
- **Change my mind:** a close above 109.5.

{"74278592b6 (XRP)": 0.3, "d5f4e44dec (LTC)": 0.6, "ea9671ce47 (ETH)": 0.7, "92ad74f1b9 (SOL)": 0.3, "bf1bcbe065 (ADA)": 0.65, "ee3f9da443 (BTC)": 0.4, "07e8c39993 (DOGE)": 0.15, "3f6d15b986 (AVAX)": 0.35, "7ed72b1bb7 (LINK)": 0.65, "1f279cd37f (DOT)": 0.1}

## Entscheidung 2026-08-09

Not financial advice.

**Strategy:** I classify each window by its last ~45–60 days, using swing structure against the 180-day context. Higher highs and higher lows above a rising base is **up** (weight 0.7–1.0). An overlapping range with no clear swing direction is **sideways** (0.3–0.5). Lower highs pressing on support is **down** (0.0–0.1). Within a regime, conviction moves the weight slightly. The invalidation level is the swing point that would break the structure.

## afb3b0be4f (BTC)
Regime: sideways
- **Read:** Topped near 125 (day -95), crashed to 91 (day -65) and retested 89.5–90 (days -45 to -40). Since then it has ranged 96–103 with fading volume. It sits at 100, mid-range, below the old breakdown area of 110–113.
- **Weight:** 0.4. No trend either way; a partial position fits a base that is holding.
- **Change my mind:** a close above 103.5 would make it up; a close below 96 would make it down.

## d5c0126540 (LTC)
Regime: sideways
- **Read:** Peaked at 133 (day -91), crashed to 89, then made a lower low at 86.4 (day -45). It recovered to 105.9 (day -19). Lows are rising (94.4, then 96.0) while highs are flat at 105–106. Price is at 100.
- **Weight:** 0.5. A range with a slight bullish tilt.
- **Change my mind:** above 106 would make it up; below 96 would make it down.

## b1e8e42af2 (DOT)
Regime: down
- **Read:** Fell from 208 to 174, then crashed to 110. Highs keep falling: 131, 113.6, 112, 108.9. The lows also fell, from 99.5 to 93.6. Price is at 100, rejected from 108.9.
- **Weight:** 0.0. Persistent lower highs.
- **Change my mind:** a close above 109.

## 76edc91a59 (ETH)
Regime: up
- **Read:** Crashed from 129 to 79, double-bottomed at 79 (day -44), then climbed with higher highs (96.8, 101.9, 103.7) and higher lows (89.7, 91.6, 95.4). Price is at 100, above the rising base.
- **Weight:** 0.8. A clean recovery structure, though it is still far below the pre-crash levels of 110–120.
- **Change my mind:** below 95.

## 60558ee9d9 (AVAX)
Regime: sideways
- **Read:** Fell from 163 to 97, then made a capitulation low at 88.5 (day -51). Since then it has ranged 94–111. Highs are flat to lower (110.8, 106.6, 108.8) and lows are slightly lower (98.4, 95.6, 94.1). Price is at 100.
- **Weight:** 0.3. A range with a slightly heavy floor.
- **Change my mind:** above 109 would make it up; below 94 would make it down.

## cba718c164 (XRP)
Regime: down
- **Read:** Fell from 150 to a crash low of 102. Highs keep falling: 125.6, 115, 113.1, 108.4. Price is retesting the 98–100 lows, last touched at 98.3 on day -2.
- **Weight:** 0.0. Lower highs and price sitting on support.
- **Change my mind:** a close above 108.5.

## 640bfa8996 (DOGE)
Regime: down
- **Read:** Fell from 171 to 112, then highs kept falling: 133, 114.5, 108.7, 106.8, 103.2. Lows are grinding lower too (100.2, 98.3, 97.6). Volume is dry. Price is at 100.
- **Weight:** 0.0.
- **Change my mind:** a close above 107.

## 1a844a45de (SOL)
Regime: sideways
- **Read:** Crashed from 129 to 79. It rallied to 110 (day -36), then bled lower to 92.5 (day -8). The last two days bounced to 100–102. The net effect is a 92–104 range inside a broader recovery.
- **Weight:** 0.3. The last month leaned lower, and the bounce is not yet confirmed.
- **Change my mind:** above 104 would make it up; below 92.5 would make it down.

## 8b5fd251eb (ADA)
Regime: up
- **Read:** Crashed from 148 to 76, then made a lower low at 71 (day -45). It spiked to 102.8, pulled back to a higher low of 79 (day -13), then broke out to 108.8 on strong volume (days -7 to -3). Price is at 100, pulling back from the high.
- **Weight:** 0.8. A higher low followed by a higher high, with volume confirming.
- **Change my mind:** below 93.

## 434b80cb07 (LINK)
Regime: up
- **Read:** Crashed from 133 to 85.5, double-bottomed around 85.6 (day -45). Since then it has made higher highs (99.9, 105.4, 108.9) and higher lows (91.9, 95.2, 96.3). It is now consolidating at 98–103, with price at 100.
- **Weight:** 0.7. The structure is up, but price has stalled below 109.
- **Change my mind:** below 96.

{"afb3b0be4f (BTC)": 0.4, "d5c0126540 (LTC)": 0.5, "b1e8e42af2 (DOT)": 0.0, "76edc91a59 (ETH)": 0.8, "60558ee9d9 (AVAX)": 0.3, "cba718c164 (XRP)": 0.0, "640bfa8996 (DOGE)": 0.0, "1a844a45de (SOL)": 0.3, "8b5fd251eb (ADA)": 0.8, "434b80cb07 (LINK)": 0.7}

## Entscheidung 2026-08-16

Strategy: I classify each window's regime from the last 60 to 90 days of structure, looking at the sequence of swing highs and lows and where price sits relative to recent ranges. The weight follows from the regime:
- **Up** (higher highs and higher lows, or a breakout above the range): 1.0
- **Sideways** (bounded range): 0.3 to 0.5, with the higher end when the swing lows are rising
- **Down** (lower highs and lower lows into new lows): 0.0

The change-my-mind level is the price that would break the structure that defines the regime.

## ed9a5ac383 (BTC)
Regime: sideways

Price peaked near 131 (day -102), crashed to 94 (day -72), and retested 92 (day -52). Since then the swing lows have been rising: 97.8, 99.0, 99.4. Price has held a 99–106 band for about 40 days. Volume is drying up at 100, and the band's resistance is 104–106.

Weight: 0.4. This is a range with rising lows, but there is no breakout yet.

Change my mind: a close above 106.5 means up (raise the weight); a close below 98.5 means down (cut to 0).

## 05cb9d7f0b (LTC)
Regime: sideways

Price ran from a 137 peak to an 89 low (day -53), then rallied to 109 (day -21). Since then the highs have been lower: 108.4, then 105.3. Support sits at 98.3–98.8, which held 2 days ago, and price is now at 100. The range is 98–109, and the recent drift is downward.

Weight: 0.3.

Change my mind: below 98 turns it down (go to 0); above 105.5 restores the up-leg.

## 48ad715872 (ADA)
Regime: sideways

This is a very volatile range. Price fell from 160+ to 79 (day -52), spiked to 114, fell back to 88 (day -20), and then spiked to 121 (day -10). It has now bled for 9 straight sessions to 100 on fading volume. The lows are rising (79, then 88, then 99.8), but the last two spikes both fully retraced.

Weight: 0.3.

Change my mind: below 98 (failure of the higher-low pattern) means 0; reclaiming 110 means up.

## f218be0b5e (SOL)
Regime: sideways

The peak was 132 (day -97), with a low of 80.6 (day -71) and a higher low at 85.8 (day -52). Price rallied to 112.6, then pulled back to 94.6 (day -15), and has since stabilized at 100–104. The structure is a 95–105 range with rising major lows.

Weight: 0.4.

Change my mind: above 105 means up; below 96 means down.

## 2d8bb80bf3 (XRP)
Regime: down

The highs keep falling: 156, 130, 119, 117, 113, 110. Price has now slipped to 99.3–100, a fresh low for the post-crash period. The previous support at 101.6 (day -51) is being tested and has given way intraday.

Weight: 0.0.

Change my mind: a close above 110 would break the lower-high sequence.

## 1ff058a2a7 (DOT)
Regime: down

The long decline runs from 230 to 100. The lower highs since the crash are 138, 119.6, 114.6, and 103.4. Lows at 98.6 (day -20) and 99.1 (now) are being retested. The bounce to 114.6 failed completely.

Weight: 0.0.

Change my mind: a close above 109 (back above the last pivot) would make me reconsider.

## 9e0786a4e6 (DOGE)
Regime: down

Price fell from 170 (day -94) to 100. The lower highs are 132.9, 114.1, 108.3, 106.4, and 105.1. The last 30 days are compressed at 97–106 on very low volume, but that compression sits within a persistent downtrend. The day -5 pop to 105 was immediately sold.

Weight: 0.0.

Change my mind: a close above 106.5 (clearing the lower-high series) would make me reconsider.

## c4415ebe2c (LINK)
Regime: up

There was a double bottom at 74.5/74.7 (days -71 and -52), followed by a clean series of higher lows: 80.1, 84.0, 85.4, 87.0. Price broke out of the 85–94 range over the last 5 days on rising volume (1.54 and 1.66). It hit 103.8, above the day -86 to -82 resistance near 100–103. Price is holding 99–101 after the breakout day.

Weight: 1.0.

Change my mind: a close below 92 (back inside the old range) means the breakout failed.

## a4e14b87f7 (ETH)
Regime: sideways

Price double-bottomed near 80.5 (days -71 and -51), then made higher lows at 91.3, 96.1, and 97.1. For the past month it has ranged 97–105.6, and it now sits mid-range at 100 on very thin volume. The recovery structure is constructive, but it has stalled below 105.

Weight: 0.5. This is a range with clearly rising lows.

Change my mind: above 105.6 means up (go to 1.0); below 97 means down.

## e5b8f1cd1a (AVAX)
Regime: sideways

Price crashed from 166 to 104, then fell to 89.7 (day -58). Since then it has chopped between 95 and 112, with lows of 95.4 (day -15) and 96.5 (day -5). Yesterday it spiked to 108.6 and was rejected back to 100, with a long upper wick on high volume, which is bearish. There is no trend in either direction.

Weight: 0.3.

Change my mind: below 95 means down; a close above 108.6 means up.

{"ed9a5ac383 (BTC)": 0.4, "05cb9d7f0b (LTC)": 0.3, "48ad715872 (ADA)": 0.3, "f218be0b5e (SOL)": 0.4, "2d8bb80bf3 (XRP)": 0.0, "1ff058a2a7 (DOT)": 0.0, "9e0786a4e6 (DOGE)": 0.0, "c4415ebe2c (LINK)": 1.0, "a4e14b87f7 (ETH)": 0.5, "e5b8f1cd1a (AVAX)": 0.3}

## Entscheidung 2026-08-23

**Strategy:** I classify each window by where the close sits in the 180-day structure. If the close has reclaimed the level the price broke down from before the large crash around day -82 and is above the post-crash base, the regime is **up** (weight 0.55–0.8). If the close has broken out of the post-crash base but is still below that breakdown level and the older range, the regime is **sideways** (weight 0.35–0.4). Clean lower highs and lower lows with no reclaim would be **down** (weight 0–0.15). Within each regime, I cut the weight for a blow-off wick on day -1 or a near-vertical move, and add to it where the base had rising lows.

## 1c7327b1ee (AVAX)
Regime: sideways
- **Read:** The window opened near 125 and traded a 115–138 range until the crash. Price fell to 77.5 at day -65, then based between 80 and 92 for about 60 days. The last 4 days ran from 83 to a 109.3 high, and day -1 left a large wick down to 92 before closing at 98.5.
- **Levels:** The close at 100 is above the base top at about 92, but well below the breakdown zone at 115–117. The longer-term trend is still lower.
- **Weight: 0.4.** The breakout is real, but there is heavy overhead supply and a rejection wick.
- **Change my mind:** A close above 110 makes this up. A close below 90 makes it down.

## 21c78bc937 (SOL)
Regime: up
- **Read:** The pre-crash level was about 85 and the window started at 83. After the crash to 63, the base climbed from 66 to 80. The current price of 100 is above the breakdown level and near the prior swing high of 102–103 from day -104. Day -1 put in a 107.7 high and closed at 98.3.
- **Weight: 0.7.** The trend structure is up, trimmed because of the day -1 wick.
- **Change my mind:** A close below 90.

## 304e5a57a0 (ETH)
Regime: up
- **Read:** The window started at 75, and the pre-crash level was 81.5. Price bottomed at 61 and then made higher lows at 63, 70, 74 and 76. It is now at 100, back at the 100.1 high from day -128. Day -1 pulled back only mildly, with a 102.7 high and a 98.3 close.
- **Weight: 0.75.**
- **Change my mind:** A close below 90.

## e7459170d8 (LINK)
Regime: up
- **Read:** The window started at 71, and the pre-crash level was 78.5. The base made rising lows from 61 to 68, 70 and 77. The breakouts at day -12 and day -8 came before the spike. The close at 100 is above every prior high except the 109 wick on day -1.
- **Weight: 0.8.** This has the cleanest structure of the windows.
- **Change my mind:** A close below 91.

## 5622e1d186 (DOT)
Regime: sideways
- **Read:** The window peaked near 189 and then declined steadily through 150, 125 and 100 to 82. The pre-crash level was about 125. The spike from 81 to a 111 high closed at 99 with a big rejection. At 100, price is far below the 125–150 supply zone.
- **Weight: 0.35.**
- **Change my mind:** A close above 112 makes this up. A close below 90 makes it down.

## 1597098725 (LTC)
Regime: up
- **Read:** For most of the window, price traded a 100–116 range. The pre-crash close was 97. The base had rising lows from 75 to 83 and then 85. The close at 100 is just back above the breakdown level, but it is still at the bottom of the old range. Day -1 had a large-volume wick up to 106.
- **Weight: 0.6.**
- **Change my mind:** A close below 92.

## 8a1658a5ef (DOGE)
Regime: sideways
- **Read:** The window peaked near 127 at day -101. The pre-crash level was about 108. The base was flat to drifting lower at 74–80 for 60 days. The spike from 75 to 100 (+33%) ended in a day -1 wick from 108 down to 89. The close at 100 is still below 108.
- **Weight: 0.35.**
- **Change my mind:** A close above 109 makes this up. A close below 88 makes it down.

## 9836fd82f4 (BTC)
Regime: up
- **Read:** The window started at 82 and peaked at 106. The pre-crash level was about 95. The base climbed from 75 to 81 and then 83. The close at 100 is above the breakdown level. Day -1 had a tight range (98.4–101.4) on low volume, so the breakout held without a blow-off.
- **Weight: 0.75.**
- **Change my mind:** A close below 92.

## 60f0dc6185 (XRP)
Regime: up
- **Read:** The pre-crash level was 88, and the earlier high was 105. After the crash, price kept making lower lows down to 65. The last 4 days went from 66 to 100 (+52%) on 4–6x volume. Day -1 left a huge range from 111.8 down to 90.6. The close has reclaimed 88, but the move is parabolic.
- **Weight: 0.55.**
- **Change my mind:** A close below 88.

## 8d87bf4d83 (ADA)
Regime: sideways
- **Read:** The window started near 130. The pre-crash level was about 104. Price crashed to 61, and the base has been choppy between 61 and 88. The spike from 77 reached a 113.8 high, with a day -1 wick down to 92. The close at 100 is below 104 and the older 105–125 range.
- **Weight: 0.35.**
- **Change my mind:** A close above 106 makes this up. A close below 88 makes it down.

{"1c7327b1ee (AVAX)": 0.4, "21c78bc937 (SOL)": 0.7, "304e5a57a0 (ETH)": 0.75, "e7459170d8 (LINK)": 0.8, "5622e1d186 (DOT)": 0.35, "1597098725 (LTC)": 0.6, "8a1658a5ef (DOGE)": 0.35, "9836fd82f4 (BTC)": 0.75, "60f0dc6185 (XRP)": 0.55, "8d87bf4d83 (ADA)": 0.35}

## Entscheidung 2026-08-30

**Strategy.** I classify each window by its own last 2–3 months. An **up** regime has higher lows and a breakout that holds above the prior range. A **down** regime has lower highs or a failed breakout that gives back most of its move. Anything else is **sideways**. Weights follow from the regime: up gets 0.6–1.0, scaled by how cleanly the breakout is holding; sideways gets 0.3–0.5; down gets 0–0.2.

## 55043c4302 (ETH)
Regime: up
- **Read:** The price fell from ~100 to 65 at day -86. It then built a base and rose steadily from 65 to 80. From day -11 it broke out of the 77–80 range up to 104 on rising volume, and it has held 99–105 for nine sessions.
- **Key levels:** Support is at 98–99 (the recent lows), with deeper support at 93. Resistance is at 105.
- **Weight:** 0.8. The breakout is holding tightly and the structure underneath is constructive.
- **Change my mind:** A close below 96.

## a90e1d8e11 (AVAX)
Regime: up
- **Read:** A long fall from the 130–147 area bottomed near 83 at day -72. After that it ranged between 85 and 98. The breakout from 89 reached 116.9 intraday, but it has faded back to 100.
- **Key levels:** 100 is just above the old range top at 98, so it is still holding above the range, but with less margin.
- **Weight:** 0.6. The trend is up, but the fade from the spike is sizable.
- **Change my mind:** A close below 96.

## 19d7736de9 (DOT)
Regime: down
- **Read:** The price fell persistently from 188 to 92, with a clear run of lower highs: 200, 175, 127, 110, 106. A spike reached 126 at day -8. Since then it has bled steadily from 114 to 100, giving back about 75% of the spike.
- **Key levels:** The 180-day structure is still lower highs.
- **Weight:** 0.1. The pop looks like a failed rally inside a downtrend.
- **Change my mind:** A recovery above 110 would make me reconsider. A break below 98 would confirm the downtrend.

## 27b1ea51b5 (SOL)
Regime: up
- **Read:** The price crashed to 59, recovered to 80, then ranged between 70 and 77. The breakout from 75 went in steps (92, then 97, then 107). Higher highs came at -3 on strong volume, and day 0 pulled back to 100.
- **Key levels:** Support is at 98–100, with deeper support at 93.
- **Weight:** 0.9. The breakout is clean, with higher highs and higher lows.
- **Change my mind:** A close below 93.

## 2ba41a464c (LINK)
Regime: up
- **Read:** After the crash to 63, the market made a steady staircase of higher lows and higher highs: 65, 72, 75, 79, 85, 107. A pre-breakout move from 74 to 85 came first, then the jump to 107. The price has held 100–107.
- **Weight:** 1.0. This has the strongest and most orderly trend of the set.
- **Change my mind:** A close below 95.

## a28de2c8c3 (LTC)
Regime: up
- **Read:** The price crashed from about 110 to 86. It recovered to 95–100 and paused between 91 and 96. The breakout from 92 reached 115.7, and it has since faded to 100, which is roughly the earlier recovery high near 100.
- **Weight:** 0.7. The structure is up, but the retest is now under way.
- **Change my mind:** A close below 96.

## da7fa34b78 (BTC)
Regime: up
- **Read:** The price fell from 106 to 76. It formed a base between 77 and 86 with higher lows. The breakout from 81 reached 104.9, and the price has held a tight 99–105 band with low-volume consolidation.
- **Weight:** 0.8. The breakout is holding well.
- **Change my mind:** A close below 97.

## 9bc08732f0 (XRP)
Regime: up
- **Read:** Before the breakout, the price was grinding lower with lower lows: 80, 77, 74, 73. It then exploded from 74 to a 125 high on six times average volume. That candle had a long upper wick, which is a possible climax. The price has since held 100–112 and is well above the prior structure at 91–95.
- **Weight:** 0.6. The regime has flipped up, but the blow-off risk keeps me from going full size.
- **Change my mind:** A close below 95.

## 3978aac10d (DOGE)
Regime: up
- **Read:** The price fell from 140 to 84. It then went flat between 84 and 90 for about 40 days. The breakout from 85 reached 122.9 and has faded to 100, which is still clearly above the base.
- **Weight:** 0.6. The breakout from the base is valid, but the fade is significant.
- **Change my mind:** A close below 96.

## f9fc89d0bd (ADA)
Regime: sideways
- **Read:** After the crash to 72, there were three spikes, to 104, 110 and 134. Each one was fully or mostly retraced. The lows are rising (72, then 80, then 89), but these are spike-and-fade swings rather than a trend.
- **Weight:** 0.4.
- **Change my mind:** A close above 111 would make me call it up. A close below 89 would make me call it down.

{"55043c4302 (ETH)": 0.8, "a90e1d8e11 (AVAX)": 0.6, "19d7736de9 (DOT)": 0.1, "27b1ea51b5 (SOL)": 0.9, "2ba41a464c (LINK)": 1.0, "a28de2c8c3 (LTC)": 0.7, "da7fa34b78 (BTC)": 0.8, "9bc08732f0 (XRP)": 0.6, "3978aac10d (DOGE)": 0.6, "f9fc89d0bd (ADA)": 0.4}

## Entscheidung 2026-09-06

**Strategy:** I classify each window by its structure over the last ~70 days: the sequence of highs and lows, whether recent breakouts have held, and where the close sits against the pivots that matter. Clean up-structures that are at or near highs get 0.8–1.0. Up-structures that still sit inside a larger downtrend, or that follow a blow-off spike, get 0.6–0.7. Sideways gets about 0.4 and down gets 0. Each window has an invalidation level at its most recent higher low.

## 7cf3c77742 (ADA)
Regime: up

The window opened near 117 and peaked at 131. It crashed to 66.5 around day -93, then built a base between 62 and 90 with higher lows: 61.9 at day -73, 68.8 at day -41, and 84.8 at day -7. A breakout ran from 78 to 102.6 and spiked intraday to 115.7. The pullback held 84.8, and price has reclaimed 100. The close is still well below the earlier 110–120 range, so overhead supply is heavy.

**Weight: 0.8.** The up-structure is intact, but the breakout has not cleared 102.6 or 115.7.

**Change my mind:** a close below 84.8.

## 576a69268b (ETH)
Regime: up

Price crashed from about 98 to 59.9 and based between 60 and 77. A gap-like breakout on day -18 took it from 76 to 100. Since then it has held a tight flag between 94 and 102, and it closes at 100 near the top of that flag. Price is above where the window started (81). Volume is drying up inside the flag, which is constructive.

**Weight: 1.0.**

**Change my mind:** a close below 93.7, the flag low.

## b2a5238841 (DOT)
Regime: up

The longer picture is a persistent decline from 169.8 to 73.9, with a sequence of lower highs: 142, 106.9, 92.7, 88.9. The breakout to 105.4 broke that sequence. The pullback then held 82.5, a higher low, and today closed at 100 on strong volume (1.67). Even so, 100 is far below the 118–130 supply zone.

**Weight: 0.6.** The recent up-structure is real, but it sits inside a larger downtrend.

**Change my mind:** a close below 82.5.

## fc069d23ba (BTC)
Regime: up

Price crashed from 103 to 73.6 and based between 72 and 83 with low volatility. It broke out to 101.4 and has held a tight range between 95 and 102 for two weeks. The close is at 100, and the prior high of 103 is the next level. This is a clean, low-volatility trend.

**Weight: 1.0.**

**Change my mind:** a close below 94.9.

## f5046aa793 (LTC)
Regime: up

Price fell from 110 to 73.7, then made higher lows from day -74 onward and based between 78 and 87. It broke out to 100.9, pulled back to 86.2, and yesterday rallied strongly on volume of 2.32. That day's low of 92.3 now acts as support, and the window's starting level was around 100.

**Weight: 0.9.**

**Change my mind:** a close below 89.

## 62c40972c5 (DOGE)
Regime: up

The window ran from 102 up to 130.5, crashed to 85, then drifted down to 74–78 on very low volume. A breakout spiked to 110.9 and pulled back to 88.1. Day -1 rallied with a wick to 104.7 and the close is 100. That wick and the 110.9 spike both left supply overhead, so the trend is choppy.

**Weight: 0.7.**

**Change my mind:** a close below 88.

## fc8b9d5c91 (XRP)
Regime: up

The base made lower lows down to 69.3 at day -23. Then came a huge breakout on 4–6x volume, up to a 119.4 spike with a long upper wick, which looks like a climax. The pullback held 92.0 and price recovered to 100. The higher low is positive, but the blow-off high caps price around 107–119.

**Weight: 0.7.**

**Change my mind:** a close below 92.

## a5a5aace7d (AVAX)
Regime: up

The window opened near 120 with a high of 133. It crashed to 78.7, then flushed again to 71.8 at day -79. From there it based between 76 and 88. A breakout reached 105.2 and the pullback held 88.7. Today's close of 100 is the highest close since the breakout. Heavy supply sits between 113 and 125.

**Weight: 0.8.**

**Change my mind:** a close below 88.7.

## 4428511b08 (SOL)
Regime: up

Price crashed from 91 to 56.4 and based between 66 and 77. It broke out in steps, with a higher close at 102.4 on day -10, pulled back to 91.4, and now closes at 100. Price is above the window's starting level (about 81) and above the earlier highs of 92. This is the cleanest trend among the windows.

**Weight: 1.0.**

**Change my mind:** a close below 91.4.

## e38a4e14f0 (LINK)
Regime: up

Price crashed from 82 to 52.9, then made a rising base with higher lows: 53.0, 59.6, and 61.7. It broke out to 95.4, pulled back to 82.4, and today closed at 100, a new window high, on volume of 1.70. Price is far above the window's starting level of 68, so this is a strong uptrend.

**Weight: 1.0.**

**Change my mind:** a close below 86.

{"7cf3c77742 (ADA)": 0.8, "576a69268b (ETH)": 1.0, "b2a5238841 (DOT)": 0.6, "fc069d23ba (BTC)": 1.0, "f5046aa793 (LTC)": 0.9, "62c40972c5 (DOGE)": 0.7, "fc8b9d5c91 (XRP)": 0.7, "a5a5aace7d (AVAX)": 0.8, "4428511b08 (SOL)": 1.0, "e38a4e14f0 (LINK)": 1.0}

## Entscheidung 2026-09-13

**Strategy:** I classify each window by the last 25–60 days, with the 180-day path as context. A window is "up" if price broke out of a post-crash base and is still holding higher lows above that breakout. It is "sideways" if the post-breakout action shows clearly lower highs, or a failed spike, while lows still hold. It is "down" if price has lost the breakout zone. Weights are 0.6–0.7 for up (lower when volatility is high or highs are falling), 0.3–0.4 for sideways and 0–0.1 for down.

---

### 9647d49381 (AVAX)
Regime: up

- **Structure:** Price fell from 140 to a crash low near 78 (day -86), then based between 85 and 93 for about 60 days.
- **Breakout:** It broke out at -25 to 107.5, pulled back to 96 (-14), and made a new high at 112.5 (-6).
- **Now:** Price is at 100, sitting on the 99.8–96 higher-low zone. The 180-day picture is still below the start, but the recent structure is constructive.
- **Weight:** 0.6.
- **Change my mind:** a close below 96.

### 9c5e063bb7 (LINK)
Regime: up

- **Structure:** Price started at 87, bottomed at 62 (-99) and based between 63 and 78.
- **Breakout:** It broke out to 110 and then to 122 (-6). Higher lows have formed at 97.4 (-11) and 100.4 (-2).
- **Now:** Price is at 100, well above the window start, so the trend is clear even after an 18% pullback from the high.
- **Weight:** 0.7.
- **Change my mind:** a close below 97.

### b5308bc609 (LTC)
Regime: up

- **Structure:** Price started at 108, crashed to 75, then based between 80 and 89.
- **Breakout:** It broke out to 103, retested 88 (-14), then pushed to a new high at 110.6 (-6).
- **Now:** Price is at 100, holding the 96–99 area.
- **Weight:** 0.6.
- **Change my mind:** a close below 96.

### d6d8b3a86f (BTC)
Regime: up

- **Structure:** Price crashed from 107 to 77, then based between 81 and 87 for two months.
- **Breakout:** It broke out at -25 to about 103, and has held a tight 99–107 range for three weeks.
- **Now:** Price is at 100, at the bottom of that range. This looks like consolidation after a breakout.
- **Weight:** 0.6.
- **Change my mind:** a close below 98.5.

### 04435282e2 (ADA)
Regime: up

- **Structure:** Price started at 142 and crashed to 73. Since then it has been very volatile but has kept making higher lows: 68.6, 75.3, 84, 93, 98.5.
- **Spike:** It spiked to 127 (-22) and is now at 100.
- **Weight:** The trend is up, but the wide daily ranges argue for less size, so 0.5.
- **Change my mind:** a close below 93.

### 89b653bc7b (DOT)
Regime: sideways

- **Structure:** This is a long downtrend from 162 to 72 (-26). Two spikes followed: one to 103, then a 4×-volume blow-off to 128.5 (-5). That blow-off fully reversed to 100 within four days.
- **Reading:** The higher lows (72 → 81 → 99.6) are offset by the failed spike and the lower long-term trend.
- **Weight:** 0.3.
- **Change my mind:** above 112 I would turn up; below 90 I would turn down.

### d95e6f6247 (DOGE)
Regime: sideways

- **Structure:** Price peaked at 144, crashed to 94, slid to an 83–90 base, then broke out to 122 (-22).
- **Since the breakout:** Highs have fallen (122, 115.5, 111, 107) while lows hold around 97–99. This is a contracting triangle.
- **Now:** Price is at 100, near the lower edge.
- **Weight:** 0.4.
- **Change my mind:** below 97 I would turn down; above 111 I would turn up.

### 92e6703d83 (XRP)
Regime: sideways

- **Structure:** Price crashed from 113 to 78, then kept drifting lower to 73.5 (-30). It then spiked to 126.7 on 6× volume.
- **Since the spike:** Highs have fallen (126.7, 115.6, 110.6, 108, 107) while lows hold at 97.7–98.
- **Now:** Price is at 100 and still far above the 75 base, but the spike is digesting rather than trending.
- **Weight:** 0.4.
- **Change my mind:** below 97 I would turn down; above 108 I would turn up.

### edc4e9f5e5 (ETH)
Regime: up

- **Structure:** Price started at 93 and crashed to 61. It then grinded up in a steady 61→78 advance with higher lows.
- **Breakout:** It broke out at -25 to 102.8 and has held a 95–103 range since.
- **Now:** Price is at 100, above the window start, with a clean higher-low sequence (61, 73.6, 95).
- **Weight:** 0.7.
- **Change my mind:** a close below 95.

### 429723718a (SOL)
Regime: up

- **Structure:** Price started at 95, crashed to 60.6, and based between 71 and 79.
- **Breakout:** It broke out to 111.4 (-17).
- **Since the breakout:** Lows are holding at 98.1 and 98.7, while highs are easing (111.4, 108, 107, 106.5).
- **Now:** Price is at 100, above the window start.
- **Weight:** 0.6.
- **Change my mind:** a close below 98.

```json
{"9647d49381 (AVAX)": 0.6, "9c5e063bb7 (LINK)": 0.7, "b5308bc609 (LTC)": 0.6, "d6d8b3a86f (BTC)": 0.6, "04435282e2 (ADA)": 0.5, "89b653bc7b (DOT)": 0.3, "d95e6f6247 (DOGE)": 0.4, "92e6703d83 (XRP)": 0.4, "edc4e9f5e5 (ETH)": 0.7, "429723718a (SOL)": 0.6}
```

## Entscheidung 2026-09-20

**Strategy:** I classify each window by structure over the last ~60 days. Up means higher highs and higher lows, with the close near the top of its recent range. Down means lower highs and lower lows. Sideways means a wide range with no clear direction. Up gets 0.65–0.9 (less when the move is parabolic or whipsawing), sideways gets about 0.5, and down gets 0–0.2.

## b832cf72e5 (ADA)
Regime: up
- **Read:** Crashed from about 118 to 65 (day -106), then made higher lows at 61, 67, 75 and 84. The breakout at -30 spiked to 113.4, and the market has since ranged 84–103. Today it closes at 100 after a strong two-day push from 86.
- **Weight:** 0.8, because the higher-low structure is intact. The volatility around the 113 spike keeps it below full.
- **Change my mind:** A close below 84.

## f2e2a4af16 (SOL)
Regime: up
- **Read:** Crashed to 54, based at 64–70, then broke out to 99.5 at -24. It consolidated at 86–96 and has now made new closing highs around 100–101.
- **Weight:** 0.9, a clean breakout from consolidation.
- **Change my mind:** A close below 86.

## 89e6489fa8 (ETH)
Regime: up
- **Read:** Crashed to 57 and based at 69–73. A gap-up at -32 took it to 95, followed by a tight 89–97 range. The close is near the high, with a high of 100.9.
- **Weight:** 0.9, steady and orderly trend.
- **Change my mind:** A close below 89.

## 00c4a802fb (XRP)
Regime: sideways
- **Read:** Fell from 100 to 70. A climactic spike to 120.5 at -29 came on 5.9x volume. Since then, highs have kept getting lower (110, 105, 106, 103) while lows hold at 88–90. It closes at 100, in the middle of the range.
- **Weight:** 0.5, a range with failing highs and no clear direction.
- **Change my mind:** Above 106 I would raise the weight; below 88 I would cut it.

## 947a14fce5 (LTC)
Regime: up
- **Read:** Fell from 96 to 69, based at 74–78, and broke out to 94. Higher lows followed at 80.7 and 85.5, and a high of 101.2 came at -13. It closes at 100, at the top of the range.
- **Weight:** 0.85, higher highs and higher lows.
- **Change my mind:** A close below 85.

## a81c34370f (DOGE)
Regime: sideways
- **Read:** Peaked at 135 and then slid to a 78–84 base. It spiked to 115.5 at -29 and has since made lower highs (109, 104.6) while holding lows near 90. It closes at 100, mid-range.
- **Weight:** 0.5, choppy with the longer-term trend still down from 135.
- **Change my mind:** Above 105 I would raise the weight; below 89.7 I would cut it.

## cf4bf1e674 (LINK)
Regime: up
- **Read:** Crashed to 56, then steadily climbed from 63 (-50) to 76. It broke out to 100.8 and then 109.3 at -13, pulled back to 84.8, and has recovered to 100.
- **Weight:** 0.8, higher lows throughout, though the 109 failure leaves overhead supply.
- **Change my mind:** A close below 85.

## 709b7d5931 (DOT)
Regime: up
- **Read:** The longer-term trend is down from 123 to 64. The last 50 days show higher lows (63.7, 71, 82.3) and higher highs (90.9, then 113). The 113 spike reversed sharply, but price has recovered to 100 with heavy volume today and a high of 103.3.
- **Weight:** 0.65, the structure is up but the spike reversal and volatility argue for caution.
- **Change my mind:** A close below 82.

## 1cc51d0ac0 (BTC)
Regime: up
- **Read:** Peaked at 102, crashed to 73, and based at 72–82. It broke out to 98 at -30, then held a tight, low-volatility range of 92.4–101.4. It closes at 100, near the top of that range.
- **Weight:** 0.85, an orderly trend.
- **Change my mind:** A close below 92.

## a78fdbc795 (AVAX)
Regime: up
- **Read:** Fell from 85 to 50, then based at 53–62 for about 60 days. It rallied to 73.5 and pulled back to 62. The last two days went 67 to 100 (+49%) on 3.9x and 6.1x volume, a breakout from a long base. Today's bar ranged 83.4–101.4 and closed at the high.
- **Weight:** 0.7, the strength is real but the move is parabolic and could be a climax.
- **Change my mind:** A close below 83.

{"b832cf72e5 (ADA)": 0.8, "f2e2a4af16 (SOL)": 0.9, "89e6489fa8 (ETH)": 0.9, "00c4a802fb (XRP)": 0.5, "947a14fce5 (LTC)": 0.85, "a81c34370f (DOGE)": 0.5, "cf4bf1e674 (LINK)": 0.8, "709b7d5931 (DOT)": 0.65, "1cc51d0ac0 (BTC)": 0.85, "a78fdbc795 (AVAX)": 0.7}

## Entscheidung 2026-09-27

**Strategy:** I classify each window's regime from the last ~40 days, checking whether the swing highs and lows are rising, and from where price sits against the pre-crash highs (day -150 to -136) and the post-crash base. An up regime gets a weight of 0.7–1.0, sideways gets 0.5 and down gets 0. Within the up regime I reduce the weight by 0.1–0.3 when the latest leg is parabolic or very volatile.

---

**86698cdbb7 (AVAX)**
Regime: up

- **Read:** Price crashed to 54 (day -100) and based at 57–63 until day -40. It broke out to 72, consolidated at 65–75, then went vertical from 70 to 104 in two days (volume 3.7–5.7x). The high was 108.2 at day -6. The pullback low was 92.4 and price recovered to 100. Price is above the pre-crash range of 83–93.
- **Weight:** 0.7. The trend is up, but the last leg is a blow-off of about 45% in 10 days, so the risk of a retrace is high.
- **Change mind:** a close below 92.

**3b594980a1 (DOGE)**
Regime: up

- **Read:** The pre-crash high was 122. Price crashed to 80, bled down to a 70–73 base, and broke out at day -39 (high 104). It then ranged 82–96 and pushed through at day -6 (high 109.3). Higher lows are 80.8 (day -12) and 94.0 (day -4). Resistance is 104–109.
- **Weight:** 0.8. The structure is up, but price is capped below the 109 high and well below the old 120s.
- **Change mind:** a close below 94.

**1b74f19356 (LINK)**
Regime: up

- **Read:** This is a clean staircase. Highs are 90 (day -36), 97.6 (day -20) and 103.4 (day -1). Lows are 77.0 (day -12) and 86.0 (day -4). Price is far above the pre-crash high of 77.5. Volume expands on up days.
- **Weight:** 1.0. This is the textbook uptrend in the set.
- **Change mind:** a close below 86.

**66abc747f8 (LTC)**
Regime: up

- **Read:** Price based at 60–67 and broke out at day -39. Higher lows came at 66.5, 70.4 and 82.5. At day -3 a 6.7x-volume spike reached 105, and price is holding at 99–102. It is above the pre-crash high of 85.
- **Weight:** 0.8. The trend is intact, but the climax-volume day adds short-term risk.
- **Change mind:** a close below 95.

**480034f2f4 (DOT)**
Regime: up

- **Read:** Price made lower lows into 57 (day -40). Since then it spiked to 101.3 (day -19), fell back to 73.7, and rallied again to 103 (day -1). The low of 73.7 is well above 57, and price is near a double top at 101–103. The pre-crash range was 95–113. Swings are wide.
- **Weight:** 0.7. The regime is up, but volatility is high and price is testing the double top.
- **Change mind:** a close below 85.

**a0942b4c83 (ADA)**
Regime: up

- **Read:** Price crashed from about 110 to 58, then rose in waves. It broke out at day -39 (high 101), then ranged 75–91 with lows at 74.2 and 74.6. A new push reached 104 (day -1), and the latest higher low is 91.5. Resistance is 101–104.
- **Weight:** 0.8.
- **Change mind:** a close below 91.

**6e5e9483b9 (XRP)**
Regime: sideways

- **Read:** Price spiked to 112 at day -36 on 5.6x volume. Since then closes have ranged from 84 to 104. The recent high of 109.3 (day -4) is a lower high than 112. The day -3 low of 95.7 is a higher low, so price is coiling at 95–110 in the upper half of a month-long range.
- **Weight:** 0.5, the weight for a range.
- **Change mind:** a close above 110 would make this up (raise the weight). A close below 95 would make me cut it.

**3959724063 (ETH)**
Regime: up

- **Read:** Price based tightly at 68–72, broke out at day -39, held 88–95 for a month, and then stepped up to 103 (day -6). It is now consolidating at 99–102 on falling volume (0.3–0.5x), which is orderly. Price is above the pre-crash high of 91.7. Higher lows are 87.7 and 96.7.
- **Weight:** 0.9.
- **Change mind:** a close below 96.

**0e8b8fdf4c (SOL)**
Regime: up

- **Read:** Price is in a steady advance from a 57–64 base to new highs. It reached 89.5 at day -31, ranged 79–88, broke to 92 at day -9 and is at 100 now. Higher lows are 78.5 and 92.2. Price is far above the pre-crash high of 80.7.
- **Weight:** 1.0.
- **Change mind:** a close below 92.

**edd9505e6f (BTC)**
Regime: up

- **Read:** Price broke out from a 73–79 base at day -39, then held 89–97. It stepped up to 103.5 (day -6) and is now very tight at 98–101. Higher lows are 88.7 and 98.1. Price is above the pre-crash high of 98.1.
- **Weight:** 0.9.
- **Change mind:** a close below 97.

---

{"86698cdbb7 (AVAX)": 0.7, "3b594980a1 (DOGE)": 0.8, "1b74f19356 (LINK)": 1.0, "66abc747f8 (LTC)": 0.8, "480034f2f4 (DOT)": 0.7, "a0942b4c83 (ADA)": 0.8, "6e5e9483b9 (XRP)": 0.5, "3959724063 (ETH)": 0.9, "0e8b8fdf4c (SOL)": 1.0, "edd9505e6f (BTC)": 0.9}
