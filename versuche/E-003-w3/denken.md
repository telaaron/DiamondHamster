# E-003-w3: was die KI gedacht hat (Set A)

Volle Antwort des Deciders pro Entscheidungswoche, unverändert. Er sah weder Datum noch Coin-Namen; die Namen in Klammern sind erst danach eingesetzt. Gesendeter Prompt und Daten: runs/<set>/<woche>/requests.json.

## Entscheidung 2026-07-05

**Strategy:** All weights are capped because the 180-day trend is down: every window trades far below where it started. Within that cap, I score the structure of the bounce off the most recent sell-off (around day -30). A higher low plus a higher high earns the most weight. A double bottom earns a mid weight. A lower low with lower highs earns the least. Breaking the recent swing low means going flat, and closing above the rebound high means adding.

## ed221ddf7d (SOL)
- **Read:** The price fell from 173 to 96, then ranged between 95 and 120. It dropped again to 73.7 at day -29. The next low at day -10 was 78.5, a higher low. The rally then broke the day -20 high of 93.3 and reached 102.9. This is the only window with both a higher low and a higher high. The price is now back at the bottom of the old 100–110 range, and volume has been light for the last two days.
- **Weight:** 0.55, because the structure is the best in the set, but the long-term trend is still down.
- **Change my mind:** Above 103 I would add. Below 86 I would cut to 0.

## 79e8d3da9f (BTC)
- **Read:** The peak was 130 at day -60, followed by a drop to 92.9 at day -30. The rebound stalled at 105.7, and the next low was 90.8, a lower low. The highs are also falling, and the price is far below the old 115–125 range.
- **Weight:** 0.25, because both the lows and the highs are falling.
- **Change my mind:** Above 105.7 I would raise to 0.5. Below 90.8 I would go to 0.

## a103d9a33b (LINK)
- **Read:** The peak was 134.8 at day -56, followed by a drop to 86.8 at day -29. The rebound reached 106.7, and the next low was 86.9, a double bottom. The price is now 100, just under the 101–106.7 resistance, on fading volume.
- **Weight:** 0.35.
- **Change my mind:** Above 106.7 I would go to 0.6. Below 86.8 I would go to 0.

## 2c546f263e (DOT)
- **Read:** This is the steepest long-term decline, from 254 to 100. The price dropped from 163 to 100.3 at day -29, rebounded to 118.8, then made a lower low of 90.2 at day -7. It is now 100.
- **Weight:** 0.25.
- **Change my mind:** Above 104 I would add, and above 118.8 I would add more. Below 90 I would go to 0.

## b2efc0a8f7 (LTC)
- **Read:** The peak was 132 at day -56, followed by a drop to 88.4. The rebound reached 101.2, and the next low was 85.7, a lower low. The price closed day 0 at 100, right at the 100.7–101.2 resistance, on somewhat firmer volume.
- **Weight:** 0.35.
- **Change my mind:** A close above 101.5 would take me to 0.55. Below 89 I would go to 0.

## 32142103a8 (AVAX)
- **Read:** The peak was 151.5 at day -56, followed by a drop to 89.9. The rebound reached 102.2. At day -16 there was a capitulation low of 82.0 on 3x average volume, which is a lower low. The recovery since then has been steady, and the price is now at the 102 resistance.
- **Weight:** 0.35.
- **Change my mind:** Above 103 I would raise to 0.55. Below 86 I would go to 0.

## 4bf3847613 (ETH)
- **Read:** Highs have been falling since 138. The price dropped to 84.3 at day -29 and rebounded to 103.6. The next low at day -9 was 84.7, a double bottom. The price is now 100 on average volume, below the 103.6 resistance.
- **Weight:** 0.4, because the double bottom has held.
- **Change my mind:** Above 103.6 I would go to 0.6. Below 84 I would go to 0.

## 21f5ea416b (XRP)
- **Read:** The peak was 134 at day -52, followed by a drop to 90.7. The rebound reached 111.8, and the next low was 87.2, a lower low. The price is now 100, with resistance between 102 and 111.8.
- **Weight:** 0.3.
- **Change my mind:** Above 103 I would raise to 0.45. Below 87 I would go to 0.

## 5ef34160ed (DOGE)
- **Read:** The peak was 152 at day -52, followed by a drop to 99.7. The rebound reached 118.7, and the next low was 91.8. That gives a lower high and a lower low, below the 105–110 shelf where the price spent days -20 to -13.
- **Weight:** 0.25.
- **Change my mind:** Above 108 I would raise to 0.45. Below 91.8 I would go to 0.

## 4a1ed17665 (ADA)
- **Read:** The peak was 152 at day -56. The price then collapsed to 78.4, rebounded to 100.3, and made a lower low of 72.9. It then rallied from 76 to 105.5 in four days on 2x volume, breaking the 100.3 rebound high. Day 0 pulled back to 100. The momentum is strong, but it is a spike off a lower low.
- **Weight:** 0.4.
- **Change my mind:** Above 105.5 I would go to 0.6. Below 92 the spike has failed, and I would go to 0.1.

{"ed221ddf7d (SOL)": 0.55, "79e8d3da9f (BTC)": 0.25, "a103d9a33b (LINK)": 0.35, "2c546f263e (DOT)": 0.25, "b2efc0a8f7 (LTC)": 0.35, "32142103a8 (AVAX)": 0.35, "4bf3847613 (ETH)": 0.4, "21f5ea416b (XRP)": 0.3, "5ef34160ed (DOGE)": 0.25, "4a1ed17665 (ADA)": 0.4}

## Entscheidung 2026-07-12

**Strategy:** I follow the trend. When price is below the falling 50-day and 180-day trend and below the level where the last breakdown started, I keep exposure small: 0.1 to 0.25 depending on how intact the base is. I only scale up after a close above the post-crash range high, and I stay near flat if the post-crash lows are being undercut.

All ten windows share the same shape. There is a long decline from the 150–270 area, a capitulation leg around days -157/-156, and a lower range from roughly day -150 to -41. A second breakdown came at days -40 to -37 from about 112–140. Since then there has been a bounce, and price is now back at 100 on low volume.

---

### b1afdad113 (ADA)
- **Read:**
  - Severe downtrend, from 260 to 100. The prior range of 145–175 failed at day -40, with a 96.7 close on 3.85x volume.
  - Price made a lower low at 85.3 (day -17). It then squeezed to 123.4 (day -8) and gave the whole move back to 100.
  - That failed rally points to supply in the 110–120 band.
- **Weight: 0.10.** Lower lows, a rejected bounce and low-volume drift mean no edge to own it.
- **Change my mind:** a close above 119 (raise), or a break below 85 (go flat).

### cce84e9863 (SOL)
- **Read:**
  - Downtrend with the breakdown from the 105–113 range at day -40. The low was 78.2 (day -36).
  - The next low was higher, at 83.3 (day -17). Price rallied to 109.2 (day -8) and is now consolidating around 100 on fading volume.
  - Support is 98–99.
- **Weight: 0.20.** The higher low is constructive, but price is still well under the old range.
- **Change my mind:** a close above 109.5 (raise to about 0.5), or below 98 then 83 (cut).

### b878c81eae (LINK)
- **Read:**
  - Broke down from 113 to a low of 87.5 (day -36). Retested at 87.7 (day -17), forming a double bottom.
  - Range is 88–102.3 and price is in the upper half. Volume is very low (0.3x).
- **Weight: 0.20.** The base is holding, but there is no breakout yet.
- **Change my mind:** a close above 102.5 (raise), or below 87.5 (flat).

### 9bcd5a0351 (LTC)
- **Read:**
  - Broke down from 115 to a low of 92.1 (day -36), then undercut slightly to 89.3 (day -18).
  - Highs are 105.2 (day -26) and 104.9 (day -7), so price sits mid-range between 89 and 105.
- **Weight: 0.20.** Rangebound below the broken support at 115.
- **Change my mind:** a close above 105.5 (raise), or below 89 (flat).

### c00c478789 (BTC)
- **Read:**
  - Breakdown from 115 to a low of 92.7 (day -37), then 91.1 (day -17), a roughly flat double bottom.
  - Price is capped at 101.4–105.5 and is sitting at 100 in a tight range.
- **Weight: 0.20.** The base is intact, but the trend is still down.
- **Change my mind:** a close above 105.5 (raise), or below 91 (flat).

### bee81f5c0f (XRP)
- **Read:**
  - Breakdown from 122 to 96.7 (day -36), then a lower low at 92.9 (day -16).
  - Highs are falling: 119.1 (day -27) and 109.1 (day -8). Price is back at 100 on 0.3x volume.
- **Weight: 0.10.** Lower highs and lower lows.
- **Change my mind:** a close above 109.5 (raise), or below 93 (flat).

### fc12a5e638 (AVAX)
- **Read:**
  - Breakdown from 140 to 97.1, then a second flush to 88.7 (day -23) on 3x volume.
  - It recovered with a higher low at 92.9 (day -17) and a high of 111.1 (day -8).
  - Today is a wide-range down day to 98 on above-average volume relative to recent days.
- **Weight: 0.15.** The rebound structure is OK, but today's selling and the downtrend argue for caution.
- **Change my mind:** a close above 111 (raise), or below 93 (flat).

### 21bead6500 (ETH)
- **Read:**
  - Breakdown from 111 to 83.3 (day -36), retested at 83.7 (day -16), a clean double bottom.
  - Range highs are 102.4 (day -27) and 101.5 (day -6). Price closed at 100, near the top of the 84–102 range.
- **Weight: 0.25.** This is the best-formed base of the group, but it is not confirmed.
- **Change my mind:** a close above 102.5 (raise to about 0.6), or below 94.8 then 83.5 (cut).

### f9aefc0efe (DOGE)
- **Read:**
  - Breakdown from 139 to 106.8 (day -36).
  - The bounce to 127 failed, and price then made lower lows at 98.3 (day -17) and 95.6 (day -12). The high since then is 109.2.
  - The steady stair-step down is intact.
- **Weight: 0.10.** Lower lows following a failed bounce.
- **Change my mind:** a close above 109.5 (raise), or below 95.5 (flat).

### 0da8519e73 (DOT)
- **Read:**
  - Breakdown from 141 to 104.7 (day -36). The bounce topped at 124.1, then price made lower lows at 95.3 and 94.2 (days -16/-14).
  - Bounces to 107.6 (day -6) and 106 (day -2) were rejected on volume, so 106–108 is resistance.
- **Weight: 0.10.** Lower lows and a rejected rally.
- **Change my mind:** a close above 108 (raise), or below 94 (flat).

---

{"b1afdad113 (ADA)": 0.1, "cce84e9863 (SOL)": 0.2, "b878c81eae (LINK)": 0.2, "9bcd5a0351 (LTC)": 0.2, "c00c478789 (BTC)": 0.2, "bee81f5c0f (XRP)": 0.1, "fc12a5e638 (AVAX)": 0.15, "21bead6500 (ETH)": 0.25, "f9aefc0efe (DOGE)": 0.1, "0da8519e73 (DOT)": 0.1}

## Entscheidung 2026-07-19

**Strategy:** I go long when the close is above its rough 50-day average, the last few weeks show higher lows, and price is not pinned under a nearby lower high. I scale the weight down when price is below the 50-day average, the pattern is still lower highs, or the latest rebound has fully given back its gains. Weights stay moderate because every window is still inside a 6-month downtrend; none gets 1.0.

All ten windows share the same shape. There was a crash near day -164, a recovery that peaked around day -70, a second crash on days -47 to -44, then a base and a bounce back to 100. The differences are in the structure of the last six weeks.

## 46369147c1 (LINK)
- **Read:** Double bottom at 83.4 (day -43) and 83.6 (day -24), then a bounce to 100. Price is above the ~96 50-day average and the ~94 20-day average. Higher lows at 89.7 (day -11) and 93.0 (day -6). Resistance is at 102.6–103; support is at 95.5–93.
- **Weight:** 0.5. The basing structure is constructive, but price is right under resistance and volume is fading.
- **Change mind:** Close below 93 (go flat), or above 103.5 (add).

## 810aa479f2 (XRP)
- **Read:** The bounce from the 92.2 low peaked at 107.9, a lower high under the day -34 high of 117.8. Price is drifting at about 100, below the ~103 50-day average and flat against the 20-day. Support is 96–97.
- **Weight:** 0.3. The picture is neutral and the lower-high pattern is still intact.
- **Change mind:** Above 104 (raise weight), or below 96 (go flat).

## ee69559623 (BTC)
- **Read:** Lows have risen steadily: 89.8 (day -24), 89.9 (day -19), 95.5 (day -6), 96.6 (day -2). Price is 100, above the ~97.5 50-day average. Resistance is at 101.7 and then 104.
- **Weight:** 0.6. This is a clean higher-low base trading above its averages.
- **Change mind:** Below 95.5.

## 9dd8714bcf (LTC)
- **Read:** Lows of 83.5 on days -25 and -24, then a range of 91–98. On day -1 price broke out of that range to 99.9 on heavier volume (1.29), and the day 0 close of 100 held the move. Price is well above the ~93 50-day average. The old ceiling at 98 should now act as support.
- **Weight:** 0.7. This is the strongest setup: a range breakout confirmed by volume.
- **Change mind:** Back below 95.

## b44eb9f6c9 (AVAX)
- **Read:** The low at 87.9 (day -30) undercut the earlier 96.3 low. The bounce to 110.1 has faded to 100, a lower high. Price is below the ~104 50-day average and the ~103 20-day average. Day 0 was a down day that touched 98.9.
- **Weight:** 0.25. The pattern is lower highs with price under its averages.
- **Change mind:** Above 105.

## 13ad852520 (ETH)
- **Read:** Double bottom at 80.4 and 80.8, then a rally to 104 (day -4) that pulled back to 100. Price is above the ~93 50-day average. Support is 96.3 then 93.5; resistance is 104.
- **Weight:** 0.5. The base is constructive, but price has been rejected once at 104.
- **Change mind:** Below 94 (go flat), or above 104 (add).

## 6eafdf6121 (SOL)
- **Read:** Lows have risen: 78.7, then 83.8, then 96–97. The rally reached 110, and price has pulled back to 100. It is above the ~96 50-day average but below the ~102 20-day average.
- **Weight:** 0.5. This looks like a pullback inside a young uptrend.
- **Change mind:** Below 96 (the higher-low structure breaks), or above 104.

## a3c7b5e136 (DOT)
- **Read:** A persistent pattern of lower highs: 202.7, 175, 127.7, then 110.7 and 109.1. Day 0 was a wide down candle closing near its low at 100. Price is below the ~103.5 20-day average. Support is 97–98.
- **Weight:** 0.1. The downtrend is intact.
- **Change mind:** Above 108.

## 2cdf738cb0 (DOGE)
- **Read:** The decline has been staircase-shaped: 163.8, then 127.7, then 109.6, all lower highs, with a 96.0 low on day -19. Price is below the ~112 50-day average and flat at 100 on very low volume.
- **Weight:** 0.2.
- **Change mind:** Above 110 (raise weight), or below 96 (go to zero).

## d0f8be37b2 (ADA)
- **Read:** A low of 83.1, then a spike to 120.3 that fully retraced to 100. The recent range is 93.4–101.9. Price is about at its ~99 50-day average.
- **Weight:** 0.35. The higher low is positive, but the failed spike is negative.
- **Change mind:** Above 105 (go long), or below 93 (go flat).

{"46369147c1 (LINK)": 0.5, "810aa479f2 (XRP)": 0.3, "ee69559623 (BTC)": 0.6, "9dd8714bcf (LTC)": 0.7, "b44eb9f6c9 (AVAX)": 0.25, "13ad852520 (ETH)": 0.5, "6eafdf6121 (SOL)": 0.5, "a3c7b5e136 (DOT)": 0.1, "2cdf738cb0 (DOGE)": 0.2, "d0f8be37b2 (ADA)": 0.35}

## Entscheidung 2026-07-26

**Strategy:** Every window shows the same shape: a long decline, a capitulation leg around day -54 to -50, and then a basing period. I go long in proportion to how well the base has turned into an uptrend, meaning higher lows, a close near the top of the recent range, and prior swing highs being reclaimed. Bases that are still making lower highs or lower lows get small weights. Each weight has a stop level just below the most recent higher low.

## 53ab19e723 (SOL)
- **Market read:** The long-term downtrend ran from about 165 to a capitulation low of 78.3 (day -50). The low was retested at 83.4 (day -31), and price then rallied to 109.4 (day -22).
- **Recent structure:** Price has since pulled back into a tight, low-volume range of 95.6–103. The higher-low sequence is 78 → 83 → 95.6.
- **Key levels:** Resistance is at 103, then 109. Major supply sits at 110–125.
- **Weight: 0.5.** The base is constructive but price is stuck in the middle of its range.
- **Change my mind:** A close below 95 means flat. A close above 103.5 means add.

## aadeaaa85d (DOGE)
- **Market read:** The distribution top was 161.6 (day -73), followed by a breakdown to 105.8. The bounces are getting weaker: highs of 126 → 108.2 → 102.7.
- **Recent structure:** The lows are still falling (97.4 → 94.7 → 92.9 on day -3). Today's bounce to 100 sits under falling resistance.
- **Weight: 0.2.** This is still a sequence of lower highs and lower lows, so I hold only a token position in case the base forms.
- **Change my mind:** A close above 103 (and then 108) would turn it bullish. A close below 92.9 means flat.

## 32acf92113 (LINK)
- **Market read:** There is a double bottom at 79.3/79.4 (days -50/-31). Higher lows followed at 85.2, 88.3, and 93.7.
- **Recent structure:** Today's close of 100 is a strong day: it broke the 97.8–99.3 highs and is the highest close since the breakdown (102.8 origin).
- **Key levels:** Next resistance is 103–106.
- **Weight: 0.7.** Clean trend reversal structure.
- **Change my mind:** A close below 93.5 means cut.

## 45cac6b028 (DOT)
- **Market read:** The decline is very steep, from 226 to 95. Since day -30 price has moved sideways in a 95–109 box.
- **Recent structure:** Lows at 96.0 and 95.0, highs at 108.7, 108.1, and 105. There is no clear higher-high yet.
- **Weight: 0.4.** It is a base with no breakout.
- **Change my mind:** A close above 109 means scale up. A close below 95 means flat.

## f7162d11e0 (LTC)
- **Market read:** The low was 82.1 (day -31). Since then the lows have risen steadily: 86.0 → 89.7 → 92.2 → 95.6.
- **Recent structure:** Price pressed 100.1 to 100.9 several times on firm volume, and today closed at the top of that range.
- **Key levels:** Resistance is around 101, then 106–109 (the pre-breakdown level).
- **Weight: 0.7.**
- **Change my mind:** A close below 95.5 means cut.

## bed5756c06 (ETH)
- **Market read:** There is a double bottom at 77.0/77.4. A sustained recovery followed with higher lows at 87.7, 89.5, 92.2, and 94.5.
- **Recent structure:** Today's wide-range close of 100 is the best close since day -55.
- **Key levels:** Resistance is 102.7, then 108–110.
- **Weight: 0.7.**
- **Change my mind:** A close below 94 means flat.

## fdf2263052 (BTC)
- **Market read:** This window had a shallower breakdown (low 88.9). The higher lows have been orderly: 93.7 → 94.1 → 95.6 → 97.5.
- **Recent structure:** The high is 102.4 (day -5). Price is consolidating at 98–101.
- **Key levels:** Above sits the 109–113 gap zone.
- **Weight: 0.65.**
- **Change my mind:** A close below 97 means cut. A close above 102.5 means add.

## 5513455d15 (XRP)
- **Market read:** The low was 90.7 (day -30). Since then price has ranged between 94.6 and 106.4.
- **Recent structure:** The highs are slipping, from 106.4 to 104.6, while the lows rise from 94.6 to 96.1 to 97.5. That is a contracting triangle on very low volume.
- **Weight: 0.5.** Neutral, waiting for the triangle to resolve.
- **Change my mind:** A close above 105 means add. A close below 97 means flat.

## 5b6bd5ec1f (ADA)
- **Market read:** There was a violent capitulation to 89.5 and a retest at 83.3. A spike to 120.5 (day -22) fully faded back to the 100 area.
- **Recent structure:** The lows are rising (93.6, 95.1, 96.8, 97.3) under a 105–109 cap.
- **Weight: 0.45.** The failed spike signals overhead supply.
- **Change my mind:** A close above 109 means add. A close below 96.5 means flat.

## ccae5af3d9 (AVAX)
- **Market read:** The breakdown low was 84.2 on a heavy-volume spike (day -37), with recovery afterwards. Since day -22, price has ranged between 91 and 105.5.
- **Recent structure:** A shakeout to 91.0 (day -2) was reversed by a strong day -1 (+7.6% on 1.5x volume).
- **Weight: 0.45.** The reversal is encouraging, but price is still mid-range.
- **Change my mind:** A close above 105.5 means add. A close below 91 means flat.

{"53ab19e723 (SOL)": 0.5, "aadeaaa85d (DOGE)": 0.2, "32acf92113 (LINK)": 0.7, "45cac6b028 (DOT)": 0.4, "f7162d11e0 (LTC)": 0.7, "bed5756c06 (ETH)": 0.7, "fdf2263052 (BTC)": 0.65, "5513455d15 (XRP)": 0.5, "5b6bd5ec1f (ADA)": 0.45, "ccae5af3d9 (AVAX)": 0.45}

## Entscheidung 2026-08-02

**Strategy:** Long-term trend first, then whether the recent swing structure confirms it. If the structure since the last major low shows higher lows and higher highs, I hold a moderate long. If it shows lower highs or a persistent downtrend, I stay small. Every window sits well below its pre-crash levels, so no weight goes above 0.6. Each invalidation level is the recent swing low, or a breakout level where that is the more useful trigger.

## ab144b11d3 (ETH)
- **Read:** Crashed from about 125 to 80 around day -57. The low at 80 held again at -37. Since then the lows are rising: 80, then 92, then 96.6. Price recovered to 103.6 at -12 and has pulled back to 100.
- **Long-term picture:** Still in a downtrend, with heavy overhead supply at 106–120.
- **Medium-term picture:** Up. The current pullback is holding above the 96.6 swing low.
- **Weight:** 0.5.
- **Change my mind:** A close below 96.

## 26ffc6b23f (SOL)
- **Read:** Rallied from the 82 crash low to 113 at -30. Since then it has made lower highs: 108, 107, 106.5, 104.7.
- **Recent lows:** 99.7, then 98.3, then 95.9. They are slipping, so the rebound is fading.
- **Weight:** 0.3.
- **Change my mind:** Below 95.9 means cut. Above 107 means add.

## 4ea0616773 (LINK)
- **Read:** Double bottom near 83.5 at -57 and -38. Higher lows since then: 89.7, 93, 94.1.
- **Recent action:** Pushed to 106.3 at -7. Day 0 bounced firmly from 96 to 100.
- **Weight:** 0.5.
- **Change my mind:** Below 94.

## 0014e9c13e (XRP)
- **Read:** Crashed from about 136 to 96.6. Since then the highs keep falling: 119, 109, 107.
- **Range:** Price is now sideways between 96 and 107, sitting mid-range at 100.
- **Weight:** 0.35.
- **Change my mind:** Below 96 means cut. A close above 107 means add.

## 22f4d0489e (AVAX)
- **Read:** Crashed from 137 to 95, with a secondary low at 86.7 at -44. Since then it has ranged between 92 and 108.
- **Day 0:** A strong reversal from a 92.2 intraday low to 100, on above-average volume (1.05). This is support defense inside a range, not a trend.
- **Weight:** 0.4.
- **Change my mind:** Below 92.

## 40f0623df4 (ADA)
- **Read:** The deepest decline in the set, from 125 to 72.9 at -38. A spike to 105.5 at -29 retraced to about 81.
- **Recent action:** The lows at 81–82 held above 72.9. Day 0 broke out to 100, with a high of 101.4, on 1.73x volume.
- **Momentum:** The strongest here.
- **Weight:** 0.6.
- **Change my mind:** Below 88, which would be a failed breakout.

## 90d824224a (LTC)
- **Read:** The cleanest recovery. Price went from 88 at -39 to 108 at -7, with steady higher lows: 88, 96, 97.6.
- **Current position:** Pulling back to 99–100, inside the up-channel.
- **Weight:** 0.6.
- **Change my mind:** Below 97.

## ba492692f9 (BTC)
- **Read:** The low was 91.4 at -38. Higher lows since: 96.4, 97.3, 98.
- **Recent action:** A high of 105.3 at -12, then consolidation at 99–103.
- **Weight:** 0.55.
- **Change my mind:** Below 97.

## bc13367c87 (DOT)
- **Read:** A persistent decline from 208 to 93.
- **Recent action:** Lower highs at 112, 109, 104, then a gap-down at -6 to 93.6. The bounce to 100 is still below the 104 lower high.
- **Weight:** 0.2.
- **Change my mind:** Above 104 means add. Below 93 confirms staying flat.

## b4128f8c88 (DOGE)
- **Read:** Fell from 167 to 100.9.
- **Range:** Has ranged 96–112 since, with lower highs (112, 106.8, 104.6) and slipping lows (96.6, 96.3, 95.6).
- **Weight:** 0.3.
- **Change my mind:** Below 95.5 means cut. Above 106 means add.

{"ab144b11d3 (ETH)": 0.5, "26ffc6b23f (SOL)": 0.3, "4ea0616773 (LINK)": 0.5, "0014e9c13e (XRP)": 0.35, "22f4d0489e (AVAX)": 0.4, "40f0623df4 (ADA)": 0.6, "90d824224a (LTC)": 0.6, "ba492692f9 (BTC)": 0.55, "bc13367c87 (DOT)": 0.2, "b4128f8c88 (DOGE)": 0.3}

## Entscheidung 2026-08-09

**Strategy:** I weight each window by trend and structure since the capitulation low.
- **Higher lows and higher highs off the bottom:** larger long.
- **Lower highs, or price drifting toward its lows:** small or flat.
- **Sizing:** capped near 0.6, since every window is still well below its pre-crash levels on a 180-day view.

### 0e796db9f0 (AVAX)
- **Read:** Fell from 140–160 to a capitulation low of 88.5 on day -51. Since then it has moved sideways between 94 and 110 for about 50 days and closes at 100, mid-range. The highs are flat (110, 108.8) and the lows are slightly rising (93, 94, 96), with no clear direction.
- **Weight:** 0.3, a neutral base inside a long-term downtrend.
- **Change my mind:** a close above 109 means add; a close below 94 means flat.

### 7807ff2655 (XRP)
- **Read:** Crash low of 98 on day -45, then a rally to 115 on day -36. The highs have stepped down since (113, 111, 108.8, 106). It just tagged 98.3 on day -2 and is retesting the base.
- **Weight:** 0.2, because the structure is fading.
- **Change my mind:** a close below 98 means flat; a close above 108 means increase.

### 1b04cb5a47 (SOL)
- **Read:** The lows are rising: 78.8 (day -64), 84 (day -45), 92.5 (day -8). The rally peaked at 110 and price pulled back into the 92–103 range. A firm bounce on day -1 takes it to 100.
- **Weight:** 0.5, a constructive base with a key level at 92.5.
- **Change my mind:** a close below 92 means cut to 0; a close above 103.5 means add.

### ef8867fc8b (ETH)
- **Read:** Double bottom near 79 (days -64 and -44), followed by a steady staircase:
  - Higher lows at 89.7, 91.6, 94.4 and 95.4.
  - Highs at 96, 101.9 and 102.4.
  - Price is tightening just under 102.4.
- **Weight:** 0.6, the cleanest uptrend structure here.
- **Change my mind:** a close below 95 means cut; a close above 102.5 means add.

### cf107ad9dc (LINK)
- **Read:** Double bottom near 85.5, then higher lows at 92, 96.3 and 98. The highs reached 105.4, 107 and then 108.9 on day -14. Now 100, pulling back inside the uptrend.
- **Weight:** 0.55.
- **Change my mind:** a close below 96 means cut; a close above 105 means add.

### 3535fc24c6 (ADA)
- **Read:** Deep low of 71 on day -45, a sharp rally to 102.8, and a retrace to 79. It then broke out strongly on high volume to 108.8 on day -3, a higher high above 102.8. Now 100, giving back some of the breakout.
- **Weight:** 0.6 on momentum, though volatility is high.
- **Change my mind:** a close below 93 (the day -6 low) means cut; a close above 105 means add.

### 95e1089248 (BTC)
- **Read:** Low of 89.5 on day -45, then a slow grind to 103.2 on day -19. It now holds a tight 96–101 range at 100. The lows are mildly rising.
- **Weight:** 0.45.
- **Change my mind:** a close below 96 means cut; a close above 103.5 means add.

### 948d4cc731 (DOT)
- **Read:** A persistent downtrend from about 200. The highs keep falling (131, 113.6, 112, 108.9) and so do the lows (100.6, 98.5, 93.6 on day -13). A bounce to 108.9 has faded back to 100.
- **Weight:** 0.25, because the trend is still down.
- **Change my mind:** a close below 93.5 means flat; a close above 109 means increase.

### dc29aca214 (LTC)
- **Read:** Low of 86.4 on day -45, then higher lows at 90.5, 94.4 and 96. It peaked at 105.9 on day -19 and has since been flat to slightly lower between 96 and 102.
- **Weight:** 0.45.
- **Change my mind:** a close below 96 means cut; a close above 106 means add.

### fde917d592 (DOGE)
- **Read:** Crash from 145 to 103. Since then the highs have stepped down (114.5, 108.7, 106.8, 103.2) and the lows sit near 97.6–98.3. It is compressing at 100 toward the bottom of its range, on low volume.
- **Weight:** 0.3, because the highs keep falling.
- **Change my mind:** a close below 97.5 means flat; a close above 107 means add.

{"0e796db9f0 (AVAX)": 0.3, "7807ff2655 (XRP)": 0.2, "1b04cb5a47 (SOL)": 0.5, "ef8867fc8b (ETH)": 0.6, "cf107ad9dc (LINK)": 0.55, "3535fc24c6 (ADA)": 0.6, "95e1089248 (BTC)": 0.45, "948d4cc731 (DOT)": 0.25, "dc29aca214 (LTC)": 0.45, "fde917d592 (DOGE)": 0.3}

## Entscheidung 2026-08-16

**Strategy:** Trend and structure following. I go long when price makes higher lows and holds above its recent range or breakout level. I cut exposure when highs and lows keep falling or price sits on support with no follow-through. Breakouts on rising volume get the most weight, and a series of lower lows gets close to zero.

---

### 22716216ff (ETH)
**Read:** Price fell from a high of 131 to a crash low of 80.6 on day -51 and has since recovered to 100. Each low since then has been higher: 91, 96, 97, then 98.8. For 30 days price has moved in a tightening range of 97–105 on very low volume, which looks like a base forming. Price is above its 50-day average of about 95.
**Weight:** 0.6. The trend of higher lows is still intact, but there is no breakout yet.
**Change mind:** I would cut below 97 and add above 105.

### d3af72fd59 (XRP)
**Read:** Each high is lower than the last: 130, 119, 117, 112, 110, then 105.6. The lows are also falling: 105, 102, 99.8, then 99.3. Price is now testing the day -51 low near 101.6 and slipping under it. This is a clear downtrend.
**Weight:** 0.1.
**Change mind:** I would turn constructive only on a reclaim of 106.

### e245514dce (ADA)
**Read:** The structure is volatile. Price made a low of 79 on day -52, spiked to 114, fell to 88 on day -20, then rallied to 121 on day -10. It has since given back nearly the whole rally and is at 100, below the day -14 breakout level of about 100–108. The higher lows (79, 88) still exist, but momentum has broken.
**Weight:** 0.3.
**Change mind:** I would go to zero below 97 and turn constructive above 110.

### e3ad7e4bb1 (DOGE)
**Read:** After the crash, the lows kept falling (111, 103, 100). For 25 days price has been sideways at 98–106 with falling highs: 114, 108, 106, then 105. Volume is very thin. The bias is neutral to bearish.
**Weight:** 0.3.
**Change mind:** I would go flat below 97 and add above 106.

### a5c9bcd8c3 (BTC)
**Read:** Price fell from 131.7 to a low of 92 on day -46 and recovered to 106. For a month it has ranged between 99 and 104 with lows holding near 99–99.7. It currently sits near the bottom of that range.
**Weight:** 0.4.
**Change mind:** I would cut below 99 and add above 104.

### 6c58fbd29c (DOT)
**Read:** This has been a persistent downtrend since the spike to 230. The highs have fallen (183, 138, 120, then 115) and so have the lows (117, 105, then 98.6). Price is back at 100 and near the latest low.
**Weight:** 0.05.
**Change mind:** I would reconsider above 109.

### ca29ec1460 (AVAX)
**Read:** Price made a low of 89.7 on day -58 and has chopped between 95 and 112 since. On day -1, price spiked to 108.6 on high volume (1.38) and closed back at 100, a bearish rejection. There is no trend in either direction.
**Weight:** 0.3.
**Change mind:** I would go flat below 95 and add above 110.

### fa958ebc0a (LTC)
**Read:** Price recovered from a low of 89 on day -52 to 109 on day -21, making higher lows along the way (97 on day -34). It is now pulling back to about 98–100. Within the larger recovery from 89, this is a modest dip, though recent highs are slightly lower.
**Weight:** 0.45.
**Change mind:** I would cut below 98 and add above 105.

### 0b554b8e3e (LINK)
**Read:** Price based between 75 and 92 for months after the crash. In the last five days it broke out: 88, 93.5, 95.5, then a 103.8 high on day -1 with volume of 1.66. It closed at 100, holding above the old range top of 92–94. This is the highest level since day -91.
**Weight:** 0.8. This is a breakout from a long base on rising volume.
**Change mind:** I would cut below 93, a failed breakout.

### eefddddd00 (SOL)
**Read:** Price made a low of 86 on day -52, rallied to 112.6, and pulled back to 94.6 on day -15. Since then the lows have been higher (96.5, 97, then 100) and price is ranging between 99 and 104. The structure is constructive but undecided.
**Weight:** 0.5.
**Change mind:** I would cut below 97 and add above 105.

---

{"22716216ff (ETH)": 0.6, "d3af72fd59 (XRP)": 0.1, "e245514dce (ADA)": 0.3, "e3ad7e4bb1 (DOGE)": 0.3, "a5c9bcd8c3 (BTC)": 0.4, "6c58fbd29c (DOT)": 0.05, "ca29ec1460 (AVAX)": 0.3, "fa958ebc0a (LTC)": 0.45, "0b554b8e3e (LINK)": 0.8, "eefddddd00 (SOL)": 0.5}

## Entscheidung 2026-08-23

**Strategy:** I follow the trend but don't chase exhaustion. I go long when price has reclaimed its pre-breakdown range or is at a range high, with a series of higher lows behind it. I cut the weight when the window still sits inside a larger downtrend under overhead supply, or when the latest move is parabolic with a wide rejection wick. Every window here ends in a sharp 3–4 day surge to 100. The weights differ mainly by where 100 sits in each window's own 180-day structure and by how violent the surge was.

## 8c4f2efcb6 (LTC)
- **Read:** The range was 100–115 until the crash at day -82 took it to about 77.5. It then built a base at 83–90 with a higher low near 75 at -60. The last four days broke out from 85 to 100 on heavy volume (2.7–3.2x). Day -1 rejected at 106, and day 0 held 97–101.
- **Levels:** Price has reclaimed the breakdown level of about 97–100. Overhead supply sits at 104–108, then 112–115.
- **Weight:** 0.5. The breakdown has been reclaimed, but price is right under supply after a vertical move.
- **Change my mind:** A close below 91 (the -3 close) would negate the breakout.

## f4af7eb61b (LINK)
- **Read:** After bottoming at 60.7 (day -59), it made a clean series of higher lows: 66, 69, 71, 75, 80. At 100 it is above every prior high in the window (94.2 at -105/-4). This is a true 180-day range breakout. Day -1 has a wide wick from 109 to 94.7, but it closed near 101 and day 0 held 95+.
- **Weight:** 0.65. It is the strongest structure of the set.
- **Change my mind:** A close below 91.5 would fill the -4 breakout gap.

## 2a2ced9850 (XRP)
- **Read:** It drifted down from 95 to 65 through day -5 with no higher lows. Then it jumped 52% in four days on 4–6x volume. Day -1 spanned 90.6 to 111.8, which is climactic. It now sits above the old highs of 101.9 and 105.7, but the move looks event-driven and extremely extended from a 65–72 base.
- **Weight:** 0.35. I'm respecting the breakout but sizing down for blow-off risk.
- **Change my mind:** A close below 90 (day -1 low) would mean the spike is failing.

## 4d364aa7d1 (DOGE)
- **Read:** The peak was 120–127 around days -110 to -100. A downtrend and the crash at -82 took it to the 74–79 base. The surge to 100 has only returned it to the pre-crash 106–108 shelf from below. Supply is heavy at 108 and 115–125. Day -1 rejected at 108 with a low of 88.8.
- **Weight:** 0.45.
- **Change my mind:** A close below 88.

## ae217e84bc (DOT)
- **Read:** This is a large, persistent downtrend from 179 to a low of 77.9. Each prior rally failed: at 109 (-69) and at 97 (-48). The current surge to 100 is still below the 105–110 and 125–150 supply zones. Day -1 rejected at 111 with a low near 97.
- **Weight:** 0.35. This is a counter-trend bounce until it proves otherwise.
- **Change my mind:** Upside, a close above 111 would make me raise the weight. Downside, a close below 90.

## acb0bad97f (BTC)
- **Read:** The pre-crash range was 95–106. The crash took it to 76, then it formed a tight 80–85 base with steady higher lows from 74.4 to 80.4. The breakout to 100 put it back inside the old range. Day -1 was quiet (98.4–101.4 on 1.05x volume) and day 0 was similar. That is orderly digestion, not a blow-off.
- **Weight:** 0.6.
- **Change my mind:** A close below 93.

## eb5639e3c0 (AVAX)
- **Read:** The range was 115–138 with a peak at 137.9. Two crash legs took it to 74.7 at -65, followed by a choppy 80–92 base. The surge to 100 is still below the 105–120 supply zone. Day -1 had a wide rejection, from 109.3 down to 92.
- **Weight:** 0.4.
- **Change my mind:** A close below 92.

## 1cc139131a (ETH)
- **Read:** The window's highs are 96.9 (-160) and 100.1 (-128), so 100 is at the top of the 180-day range. There are higher lows from 61 through 70, 74 and 76. Day -4 broke out with a gap from 77.9 to 91.5. Day -1 had a modest 96.8–102.7 range and day 0 held 95.6+. This is a constructive retest of the old highs.
- **Weight:** 0.6.
- **Change my mind:** A close below 91 would fill the breakout gap.

## 1874cd917b (SOL)
- **Read:** The prior range was 85–103, peaking at 103.1 (-104). After the crash to 63 it recovered with higher lows (67, 73, 75, 78). It is now at the top of the range. Day -1 rejected from 107.7 to a low of 91.9.
- **Weight:** 0.55.
- **Change my mind:** A close below 91.

## 934ef5e883 (ADA)
- **Read:** This is a long downtrend from 138, with a crash to 61. Two earlier spikes failed: 88 at -50 faded to 69, and 93 at -17 faded to 76. This is the third spike, still below 104–124 supply. Day -1 rejected from 113.8 to 92.
- **Weight:** 0.35. The pattern of failed rallies argues for caution.
- **Change my mind:** A close below 92. A hold above 105 would make me raise the weight.

{"8c4f2efcb6 (LTC)": 0.5, "f4af7eb61b (LINK)": 0.65, "2a2ced9850 (XRP)": 0.35, "4d364aa7d1 (DOGE)": 0.45, "ae217e84bc (DOT)": 0.35, "acb0bad97f (BTC)": 0.6, "eb5639e3c0 (AVAX)": 0.4, "1cc139131a (ETH)": 0.6, "1874cd917b (SOL)": 0.55, "934ef5e883 (ADA)": 0.35}

## Entscheidung 2026-08-30

**Strategy:** I go long when price holds above the base it broke out of and its recent swing lows are rising. I cut or stay light when a volume spike has mostly retraced, or when the larger trend is still a sequence of lower highs. The weight scales with how well the breakout is holding and how far price sits from its invalidation level.

## 65c6d1bfbe (LTC)
- **Read:** Before the crash the range was 108–126. The crash bottomed at 84.5. After that, lows rose (85.8, 90.5) and price based at 92–95. A spike from -11 to -8 reached 115.7 on about 3x volume. Price has since faded to 100 on falling volume, giving back about 70% of the spike.
- **Long-term structure:** Still down. The asset sits far below its pre-crash range.
- **Weight 0.4:** Price is still above the 92–95 base, but the spike looks like it is failing.
- **Change my mind:** A close below 95 means the base has failed, so I go to 0. A close above 106 means I add.

## e54b82a66f (ADA)
- **Read:** Very volatile. The crash went from about 120 to 71.7. Rallies to 103.8 and to 109.9 both faded. Lows are rising: 71.7, then 79.6, then 88.8. The latest spike hit 134.1 with a long upper wick and has fully reversed to 100.
- **Weight 0.35:** The higher lows are constructive, but rallies here fail repeatedly.
- **Change my mind:** A close below 88 breaks the series of higher lows. A close above 111 means I add.

## f4847a62e6 (XRP)
- **Read:** Price slid steadily from 105 to a 72.6 low. It then broke out on a 6x-volume climax to 125. The post-spike highs are lower: 114.2, then 108.6, then 105.6. The base at 73–74 is far below.
- **Weight 0.35:** The breakout reverses the downtrend, but the action since then is distribution with lower highs.
- **Change my mind:** A close below 95. A close above 109 means I add.

## f336636285 (AVAX)
- **Read:** The pre-crash range was 120–147. Price double-bottomed near 80 at -86 and -72, then ranged 85–98 for two months. The spike reached 116.9. Price is now retesting the top of that range near 98–100.
- **Weight 0.5:** This is a textbook retest of the breakout level.
- **Change my mind:** A close below 96 puts price back inside the range. A close above 108 means I add.

## d140b2bdc7 (LINK)
- **Read:** Price double-bottomed at 62.8 and 62.9. Lows rose steadily from there: 67.5, 69.9, 72, 72.4. Breakouts at 80 and 85 came on volume. Price peaked at 113.2 and now sits at 100, above the pre-crash high of 97.5.
- **Weight 0.7:** The uptrend structure is clean and price is holding above prior resistance.
- **Change my mind:** A close below 94 fills the gap and fails the move. A close above 108 means I add.

## bccbfa23d8 (DOT)
- **Read:** A long downtrend from 200 to 88, with lower highs at 175, 127.8, 110.9 and 106.2. The spike to 126 broke that sequence. Price has now fallen back to 100, below the 106 swing high.
- **Weight 0.3:** The larger trend is still down, and the breakout has largely failed.
- **Change my mind:** A close below 95 means I go to 0. A close back above 110 means I add.

## 20198e56dc (ETH)
- **Read:** Price double-bottomed at 62.3 and 62.6, then made higher lows into a tight 76–80 base. A gap breakout from 79 to 93 followed. For eight days price has held 99.5–105 with day-0 low at 98.8, near the pre-crash range top around 100.
- **Weight 0.7:** The breakout is holding in a tight flag above the base.
- **Change my mind:** A close below 96 heads toward filling the 93 gap. A close above 106 means I add.

## 7747bf7560 (DOGE)
- **Read:** The pre-crash peak was 144.6. Price crashed to 94.6, then trended down with lower highs (112.7, 96.7, 91.9, 89.8) to a low of 83.1. The spike reached 122.9 and has faded to 100, which is still above the 96.7 lower high.
- **Weight 0.4:** The downtrend line is broken, but the retracement is deep.
- **Change my mind:** A close below 95. A close above 110 means I add.

## 4847b664f9 (SOL)
- **Read:** The crash bottomed at 59.1. Price based at 71–77, then broke out at -11. Unlike most of these windows, it kept making higher highs after the spike: 101, then 108.7 at -3. Post-breakout lows also kept rising: 86.2, 90, 91.7, 93.7, 98.6. Price is now above the pre-crash high of 96.7.
- **Weight 0.75:** This window has the strongest trend structure of the set.
- **Change my mind:** A close below 93. A close above 109 confirms the trend continuing.

## 434e4f7bfb (BTC)
- **Read:** The pre-crash range was 85–106. The crash bottomed at 76.1, followed by a 75–86 base. The breakout to 102.3 was orderly. For eight days price has held 97–105, and day 0 had a tight range with low 99.1.
- **Weight 0.65:** The breakout is controlled and the base is holding well.
- **Change my mind:** A close below 97 means I cut. A close above 105.5 means I add.

{"65c6d1bfbe (LTC)": 0.4, "e54b82a66f (ADA)": 0.35, "f4847a62e6 (XRP)": 0.35, "f336636285 (AVAX)": 0.5, "d140b2bdc7 (LINK)": 0.7, "bccbfa23d8 (DOT)": 0.3, "20198e56dc (ETH)": 0.7, "7747bf7560 (DOGE)": 0.4, "4847b664f9 (SOL)": 0.75, "434e4f7bfb (BTC)": 0.65}

## Entscheidung 2026-09-06

**Strategy:** I follow the trend and favor breakouts. I want to be long when price has broken out of a long base on heavy volume, is holding most of that gain, and is trading at or near its highest levels with little overhead supply from earlier in the window. I cut the weight when old highs well above the current price, or a long upper wick on a climax-volume day, point to sellers overhead. The change-of-mind level is set below the low of the post-breakout consolidation.

## 0c3c70ab5c (BTC)
- **Read:** The pre-crash high was 103 (day -123). Price crashed into a 73–81 base and broke out from 80 to 97.5 on day -16 with heavy volume. It has since consolidated between 94.9 and 102.4, and the close at 100 sits in the upper part of that range.
- **Weight: 0.7.** The trend is constructive, but there is overhead supply at 101–103 from the earlier top, and recent volume is light.
- **Change my mind:** a close below 94.9.

## 9fcaf4021a (ADA)
- **Read:** The bigger structure is lower highs (130 → 129 → 89). The breakout from a 78 base spiked to a 115.7 wick and then faded. The range since then is 84.8–101.7, and price is now 100, near the top of that range. Old supply sits far above at 110–125.
- **Weight: 0.6.** Momentum is good, but the spike's rejection wick and the long-term downtrend argue against full size.
- **Change my mind:** a close below 85.

## 7fa1491466 (LINK)
- **Read:** The prior window high was about 82 (day -119). Price is now at 100, the highest level in the window. It just broke out of an 82–92 consolidation with a wide-range day on 1.70x volume. The lows have been rising since day -73 (53).
- **Weight: 1.0.** This is the cleanest breakout of the set, with no overhead supply.
- **Change my mind:** a close below 90.

## bc46e2a9c2 (AVAX)
- **Read:** Before the crash the range was 113–132. The breakout from an 80 base reached 105 intraday. Price then based at 88.7–96 and has rallied four days in a row to 100 on above-average volume. Supply sits overhead at 110–120.
- **Weight: 0.7.**
- **Change my mind:** a close below 89.

## 3fb77208be (LTC)
- **Read:** Before the crash the range was 95–110. The breakout from an 80 base reached 101. Price then pulled back to 86.2 and has now gapped back to 99.5–100 on 2.3x volume, its highest close since day -118. The 103–110 zone above is moderate resistance.
- **Weight: 0.8.**
- **Change my mind:** a close below 92.

## 052ae5fd64 (XRP)
- **Read:** A 70 base produced a parabolic move to a 119.4 wick on 6x volume, which looks like climactic selling. Since then price has drifted in a 92–108 range. It is now 100, mid-range, on fading volume. Highs of 103–113 from before the crash sit above.
- **Weight: 0.5.** The blow-off top and the mid-range position call for half size.
- **Change my mind:** a close below 92 (bearish), or a close above 108 (raise the weight).

## 120a547158 (DOT)
- **Read:** This is a long downtrend from 167 to 77. The breakout reached a 105 wick, after which price made higher lows at 82.5 and 85.6. It is now breaking up to 100 on 1.67x volume, the highest close since day -95. Supply is far overhead at 110–140.
- **Weight: 0.75.**
- **Change my mind:** a close below 85.

## 9987ce4ae2 (SOL)
- **Read:** The prior window high was 92 (day -118), and price has cleared it. The post-breakout high was 103.8. Lows are rising (91.4 → 94), and price is now 100, back near that high. There is little overhead supply.
- **Weight: 0.85.**
- **Change my mind:** a close below 91.

## c72b02e2f5 (DOGE)
- **Read:** The pre-crash high was 130 (day -115). The breakout reached a 110.9 wick, the range since has been 88–104, and day -1 printed a 104.7 rejection wick. Price is now 100, upper-mid range. There is heavy overhead supply at 110–127.
- **Weight: 0.65.**
- **Change my mind:** a close below 88.

## 9628840717 (ETH)
- **Read:** The prior window highs were 96–98 (days -142 and -137), and price has broken above them. The breakout from a 74–76 base reached 101–102. It has held a tight 93.7–102 range for two weeks and now closes at 100, near the top. Overhead is clear.
- **Weight: 0.85.**
- **Change my mind:** a close below 93.5.

{"0c3c70ab5c (BTC)": 0.7, "9fcaf4021a (ADA)": 0.6, "7fa1491466 (LINK)": 1.0, "bc46e2a9c2 (AVAX)": 0.7, "3fb77208be (LTC)": 0.8, "052ae5fd64 (XRP)": 0.5, "120a547158 (DOT)": 0.75, "9987ce4ae2 (SOL)": 0.85, "c72b02e2f5 (DOGE)": 0.65, "9628840717 (ETH)": 0.85}

## Entscheidung 2026-09-13

**Strategy:** Trend-following with a structure filter. I go long when price holds above its post-breakout consolidation floor and sits well above its 50-day base. I cut weight for blow-off reversals, sequences of lower highs, or a heavy long-term overhang. Weight scales with how cleanly the breakout is holding, and the invalidation level is the consolidation floor.

## c30e36f268 (XRP)
- **Read:** The asset declined from 113 to a 74–82 base, then broke out on very heavy volume (6x) from 75 to 109–113 at days -25 to -22, with a wick to 126.7. Since then it has ranged between 98 and 111 with lower highs (113.4, 110.6, 108.2, 106.9). The floor at about 97.7–99 is holding. Price is now 100, at the bottom of the range.
- **Weight:** 0.5. The breakout is intact and price is far above the base, but the highs keep fading toward the floor.
- **Change of mind:** A close below 97.5 takes me flat. A close above 110.6 takes me to full.

## 5c01c93a00 (LINK)
- **Read:** Higher lows since the 63 bottom (63, 70, 72, 73) and a breakout from 85 to 107. A second leg reached 122 at day -6, then reversed fully back to 100 within 5 days. The floor is at about 97.4–99.6.
- **Weight:** 0.45. The underlying uptrend is the strongest of the set, but the reversal at -6 looks like a blow-off.
- **Change of mind:** Below 97 goes flat. A reclaim of 109 goes to full.

## 9c37ed0f12 (BTC)
- **Read:** A low-volatility base at 81–86, then a breakout to about 102. The range since has been 99–107 with lower highs (107.1, 104.8, 104.0). Price is now 100, at the range floor and back into the old 100–106 supply zone from days -130 to -120.
- **Weight:** 0.45. The breakout is holding, but momentum is waning at the floor.
- **Change of mind:** Below 99 goes flat. Above 105 goes to 0.8.

## 7712211ae7 (ETH)
- **Read:** A breakout from a 76 base to 101.6, then a tight hold at 95–103. Price now sits at the top of the full 180-day window (the prior high was 99.5 at day -149), so there is no overhead supply. A wick to 107.6 at day -2 was rejected. Price is now 100, mid-range.
- **Weight:** 0.65. This is the cleanest structure: price is at range highs with a shallow consolidation.
- **Change of mind:** Below 95 goes flat. A close above 103.6 goes to full.

## 1398a19645 (LTC)
- **Read:** Price fell from 112 to 73, based at 82–85, and broke out to 103. It pulled back to a higher low at 88.2, then rallied to 102–103 with a 110.6 wick that was rejected. It is now 100. The support shelf is at about 96–97.
- **Weight:** 0.5. The higher-low structure is constructive, but the -6 wick shows supply at about 103–110.
- **Change of mind:** Below 96 goes flat. A close above 103 goes to 0.8.

## ddaca309e6 (DOGE)
- **Read:** The peak was 143 at day -122, followed by a crash and a base at 84–90. The breakout spiked to 122, and the range since has been 97–115. The rejection at 115.5 at day -8 was followed by a slide to 100. There is heavy long-term overhang from 120 to 140.
- **Weight:** 0.4. The breakout holds, but price is still deep within a larger downtrend.
- **Change of mind:** Below 97 goes flat. Above 111 goes to 0.7.

## a1379ebfc1 (DOT)
- **Read:** A long downtrend from 162 to 75. The first breakout to 103 faded to 81. A second surge to 128.5 at day -5 on 4x volume fully reversed to 100 in four sessions, which is a classic blow-off. There is no consolidation floor yet; the nearest support is about 81–84.
- **Weight:** 0.2. This is an exhaustion reversal inside a larger downtrend.
- **Change of mind:** A reclaim of 107 goes to 0.5. Below 95 goes flat.

## f8c23d0be8 (SOL)
- **Read:** Bottomed at 62.6, made higher lows, based at 72–78, and broke out to 110 at day -17. The range since has been 98–108 with mildly lower highs (111.4, 106.7, 108.1, 106.5). The floor is at about 98.1–98.7, and price is now 100.
- **Weight:** 0.5. The uptrend is sound, and price is testing the floor.
- **Change of mind:** Below 98 goes flat. Above 108 goes to full.

## a9b97d5d60 (ADA)
- **Read:** A downtrend from 142 to 73, then a series of rising lows (68, 75.5, 84, 93) and rising spike highs (98, 104, then a 127 wick). The range since the breakout has been 93–114. Price is now 100, mid-to-low in the range.
- **Weight:** 0.5. The improving higher-low staircase offsets the long-term overhang.
- **Change of mind:** Below 93 goes flat. Above 110 goes to 0.8.

## aea4590b75 (AVAX)
- **Read:** Price fell from 140 to a 78–85 crash low, recovered into an 85–96 range, and broke out to 107.5 with a 114 wick. The range since has been 96–112. It rallied to 110.8 at day -6, then dropped three days back to 100. The floor is at about 96.2.
- **Weight:** 0.45. The structure holds, but the recent sharp fade weighs on it and there is overhead supply at 125–140.
- **Change of mind:** Below 96 goes flat. Above 109 goes to 0.8.

{"c30e36f268 (XRP)": 0.5, "5c01c93a00 (LINK)": 0.45, "9c37ed0f12 (BTC)": 0.45, "7712211ae7 (ETH)": 0.65, "1398a19645 (LTC)": 0.5, "ddaca309e6 (DOGE)": 0.4, "a1379ebfc1 (DOT)": 0.2, "f8c23d0be8 (SOL)": 0.5, "a9b97d5d60 (ADA)": 0.5, "aea4590b75 (AVAX)": 0.45}

## Entscheidung 2026-09-20

**Strategy:** I go long when price trends up from a confirmed base: a breakout above a multi-month range, higher lows since then, and a close near or above the 180-day high. I size by how clean the structure is and how much room there is to overhead resistance. I cut the weight when price is just mid-range inside a volatile post-spike range, or after a parabolic move with no consolidation.

## 360209ced1 (LTC)
- **Read:** The decline from 103 (-133) bottomed near 69–70. It based at 74–78, then broke out hard at -30 (75 → 90 on 2.7x volume). It consolidated at 81–94 with higher lows (80.7, 85.5) and has now pushed to 100. That is close to the 180-day high of about 103, and the -13 wick at 101.2 is already being tested.
- **Weight: 0.8.** The trend is up, the structure is clean and volume confirms it. The only overhead supply is 101–103.
- **Change my mind:** a close below 86.

## 773da5f669 (DOGE)
- **Read:** The window started at 109 and peaked at 135.9 (-129). Price crashed to 78–80 and based there, then spiked to 115.5 (-29). Since then it has been ranging 90–109 and now sits at 100, in the middle of that range. It is still far below the earlier highs at 125–135, which leaves heavy overhead supply.
- **Weight: 0.5.** The bounce is constructive but there is no breakout yet.
- **Change my mind:** below 89 → flat; a close above 109 → raise.

## 651f9406df (LINK)
- **Read:** The low of 56 (-88) was followed by a steady series of higher lows: 63, 64, 65. The breakout came at -32/-30 to 85–99. After that came a spike to 109 (-13), a pullback to 84.8, and now a recovery to 100. Price is above everything in the window except the -13 spike.
- **Weight: 0.8.** This is a well-formed uptrend with higher lows.
- **Change my mind:** a close below 85.

## c362f4090a (AVAX)
- **Read:** The long base ran at 52–60 with a modest rise to 65–72. Then came a parabolic move: 67 → 72.5 → 89 → 100 in three days, on 2.5x, 3.9x and 6.1x volume. Day 0's range was 83–101 and it closed at the high. That is a new 180-day high, above 92.7, but the move is extremely extended with no consolidation.
- **Weight: 0.5.** Momentum is strong, but blow-off and giveback risk is high.
- **Change my mind:** below 83, the day 0 low → flat.

## 8b0c59086c (DOT)
- **Read:** Price fell from 123–127 to a low of 66. It broke out to 90 at -29, spiked to 113 at -12, and then retraced fully to 83. It is now back at 100. The swings are very large, with roughly 20% reversals inside two weeks, and the overhead supply from 110–125 is substantial.
- **Weight: 0.5.**
- **Change my mind:** a close below 88.

## a33f973cc1 (ETH)
- **Read:** After a crash to 57, price based tightly at 70–73. The breakout at -32 was a gap from 72.5 to 85 and then 95. It then held a tight month-long consolidation at 89–97 with low volatility. It is now at 100, which clears the range top and the earlier 180-day highs (93.2, 96.3).
- **Weight: 0.9.** This is the cleanest base-and-breakout continuation of the set.
- **Change my mind:** a close below 89.

## 07622eea12 (BTC)
- **Read:** The high of 102 (-137) gave way to a low of 73. Price based at 77–80, then broke out to 96 at -30. It has consolidated at 92–101 for a month, with lows at 92.4–94, and is now at 100. That sits at the range top, just under the 180-day resistance of 101–102. Volatility is low.
- **Weight: 0.75.** The trend is up, but the price is right at resistance.
- **Change my mind:** a close below 92.

## 9d38d854e5 (ADA)
- **Read:** The window started at 117 with a high of 126.7, then crashed to 61. Recovery has been choppy, with failed spikes at -78 (88) and -45 (93). The breakout spike reached 113 (-29) and price has since ranged 83.5–103. It is now 100, in the upper half of that range but well below the earlier highs.
- **Weight: 0.5.** The structure is volatile and repeated spikes have failed.
- **Change my mind:** below 84 → flat; a close above 104 → raise.

## ed18ebf54d (XRP)
- **Read:** The high of 110 gave way to a slow bleed down to 70–72. The breakout at -31/-29 was violent, reaching 120.5 on 6x volume. Since then price has chopped at 88–108. A sharp rejection at -5 (106 → 91) was followed by a recovery to 100, which is mid-range. That leaves overhead supply at 103–110 and a news-driven profile.
- **Weight: 0.5.**
- **Change my mind:** a close below 88.

## 9aaf9606db (SOL)
- **Read:** After a crash to 54, price based at 64–70. The breakout ran from 69 to 99 over -32 to -24. It consolidated at 87–96 with higher lows (86.2 at -5) and broke to 101.4 at -2. That is a new 180-day high, and price is holding at 100.
- **Weight: 0.8.**
- **Change my mind:** a close below 86.

{"360209ced1 (LTC)": 0.8, "773da5f669 (DOGE)": 0.5, "651f9406df (LINK)": 0.8, "c362f4090a (AVAX)": 0.5, "8b0c59086c (DOT)": 0.5, "a33f973cc1 (ETH)": 0.9, "07622eea12 (BTC)": 0.75, "9d38d854e5 (ADA)": 0.5, "ed18ebf54d (XRP)": 0.5, "9aaf9606db (SOL)": 0.8}

## Entscheidung 2026-09-27

**Strategy:** I follow the trend and buy strength. I go long when price has recovered above its prior structure and is making higher lows. The weight scales up when the stock is breaking into new highs on an orderly move. It scales down when the move is a single-spike gap, the trend is choppy, or overhead supply from before the crash is still close. I exit if the most recent higher low breaks.

## f9f8fc0968 (ADA)
- **Read:** The stock crashed from about 98 to 61, built a base at 55–68, then rallied strongly from -39. Since -12 it has made higher lows at 74.6 and 91.5. It is now back at its pre-crash level near 100. Overhead supply from before the crash sits at 104–113.
- **Weight:** 0.65. The trend is strong, but the stock is volatile and is running into old resistance.
- **Change my mind:** a close below 91.

## b0ef0c3abc (DOT)
- **Read:** The stock had a blow-off spike to 101 on -19 and then faded to 74.5. It has since rebuilt steadily, with a higher low at 85 on -4, and has returned to 100 on rising volume. Resistance from before the crash is at 103–110.
- **Weight:** 0.6. The trend is good, but the stock has already been rejected at 101 once.
- **Change my mind:** a close below 85.

## 6ee442e683 (BTC)
- **Read:** This is an orderly, low-volatility uptrend from the 70 lows. It has broken out above the prior 180-day high of about 98. It is now consolidating tightly at 98–103 on light volume, which is a constructive pause.
- **Weight:** 0.8.
- **Change my mind:** a close below 95.

## b09c5278e1 (ETH)
- **Read:** The stock broke out with a large gap at -39 and then built a base at 87–95. It has pushed to new highs above the prior 91.7 peak and is consolidating at 99–104 on very low volume.
- **Weight:** 0.8. This is a clean breakout followed by a tight hold.
- **Change my mind:** a close below 96.

## 9013980f1d (LINK)
- **Read:** Price has doubled from 50 to 100, far above the prior high of 77. It made a higher low at 86 on -4 and a strong push on -2 with volume of 2.5. The stock is extended, but the trend is very strong.
- **Weight:** 0.75.
- **Change my mind:** a close below 86.

## 8560f5705b (AVAX)
- **Read:** The stock went sideways for a long time at 57–62. Then it surged about 50% in two days (-8 and -7) on extreme volume of 5.7. Since then it has traded in a range of 91–108 and is holding up, but the gain comes from one spike rather than a built trend. The pre-crash high was about 96.
- **Weight:** 0.5.
- **Change my mind:** a close below 91.

## 37cb1953b8 (LTC)
- **Read:** The stock rose steadily from 62 to 87. Then it gapped up on -3 from 87 to 101 on volume of 6.7, and has held that gap for three days. It is now well above its prior high of 85.
- **Weight:** 0.65. The breakout is strong, but the gap is untested.
- **Change my mind:** a close below 95, since filling the gap toward 87 would end the thesis.

## 8ed9a3e06b (DOGE)
- **Read:** The stock recovered from 72 to 100. A spike to 109 on -5 was rejected. Price is still below its pre-crash range of 100–122, so heavy overhead supply remains. Higher lows are at 81 and 94.
- **Weight:** 0.55.
- **Change my mind:** a close below 94.

## 29ea62f453 (SOL)
- **Read:** The uptrend from 51 is steady, with higher lows at 78.5 and 92. Price is at new highs, well above the prior 80.7 peak, and volume is healthy without looking like a blow-off.
- **Weight:** 0.8.
- **Change my mind:** a close below 92.

## 43372b246f (XRP)
- **Read:** The stock spiked to 112 at -36 and has chopped in a wide 83–109 range since. Price is now 100, near the pre-crash high of about 102. Swings are wide and volume is high, but recent lows are rising: 83.4, then 95.7.
- **Weight:** 0.55. The stock is range-bound with no clean breakout.
- **Change my mind:** a close below 95.

{"f9f8fc0968 (ADA)": 0.65, "b0ef0c3abc (DOT)": 0.6, "6ee442e683 (BTC)": 0.8, "b09c5278e1 (ETH)": 0.8, "9013980f1d (LINK)": 0.75, "8560f5705b (AVAX)": 0.5, "37cb1953b8 (LTC)": 0.65, "8ed9a3e06b (DOGE)": 0.55, "29ea62f453 (SOL)": 0.8, "43372b246f (XRP)": 0.55}
