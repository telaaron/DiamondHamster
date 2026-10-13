# E-026: was die KI gedacht hat (Set A)

Volle Antwort des Deciders pro Entscheidungswoche, unverändert. Er sah weder Datum noch Coin-Namen; die Namen in Klammern sind erst danach eingesetzt. Gesendeter Prompt und Daten: runs/<set>/<woche>/requests.json.

## Entscheidung 2026-07-05

**Strategy:** Trend-following with a market filter. I hold full size only when an asset is above its medium-term structure and making higher highs and higher lows while the market is not in a downtrend. In a falling market I go flat to small, and I add exposure only for clear relative strength, such as reclaiming the pre-crash level or breaking a base on volume.

**Market context (identical in every window):** The market is in a downtrend, from about 143 to a low of 92 at day −5. It has bounced to 100 but is still below its ~50-day area (about 110) and below the breakdown level near 115. It is a short-term bounce inside a downtrend, so base weights stay low.

### c2e3254f16 (AVAX)
- **Read:** Long downtrend, from 210 to a low of 82 at day −16. Higher lows since then (82, 86, 92) and price is now 100, back at the top of its one-month range. Overhead is the 110–116 gap left by the −33/−30 breakdown.
- **Weight: 0.3.** It is improving, but it is still a bounce in a downtrend.
- **Change my mind:** Below 90 I go to 0. A close above 103 lets me add.

### 4d60bda5f8 (BTC)
- **Read:** This asset tracks the market. Lows at 92.9 and 90.8 and price now 100. Resistance is 104–106, from the day −20 high, and support is 91.
- **Weight: 0.25.** There is no edge beyond the market's own bounce.
- **Change my mind:** Below 91 I go to 0. Above 106 I go to 0.5.

### 0f5cd43f21 (ADA)
- **Read:** It crashed to 73 at day −10, then rose from 76 to 101 in four days on 1.8–2.2× volume. That breaks the 73–90 base and clears the day −20 bounce high of 100. It shows strong relative strength against the market, though it is far below the 50-day level (~120).
- **Weight: 0.5.** This is a momentum breakout, kept at half size because the move was vertical and the market is weak.
- **Change my mind:** Below 88 (losing the breakout) I go to 0. Holding above 103 lets me add.

### f6ee48f1a1 (LTC)
- **Read:** Low of 85.7 at day −10, followed by a steady grind to 100. Price is testing the 101 resistance from day −20. It fell less than the other assets and is making higher lows.
- **Weight: 0.35.**
- **Change my mind:** Below 90 I go to 0. A close above 102 takes me to 0.6.

### b4def9c423 (DOGE)
- **Read:** A rally to 152 at day −52 failed completely. Since the crash the highs keep falling (118.7, 109, now 101). The low was 89.3 at day −5 and resistance is 105–110.
- **Weight: 0.2.** The structure is still lower highs.
- **Change my mind:** Below 92 I go to 0. Above 110 I go to 0.5.

### 2132450ec6 (LINK)
- **Read:** Double bottom near 87 (days −29 and −10), with price now 100. Resistance is 101.5–106.7 and the trend is still down.
- **Weight: 0.25.**
- **Change my mind:** Below 88 I go to 0. Above 107 I go to 0.5.

### 727098e9dc (SOL)
- **Read:** Low of 73.7 at day −29, then a higher low at 78.5 (day −10). Price is now 100, above the day −20 high of 93.3 and back at the pre-crash level (~100 at day −34). The highs and lows are both rising, and it has recovered the entire crash, which the market has not.
- **Weight: 0.5.**
- **Change my mind:** Below 88 I go to 0. Holding above 103 lets me raise it.

### 303acee46a (XRP)
- **Read:** Low of 87.2 at day −9, with price now 100. The day −20 spike to 111.8 failed, so resistance sits at 102–112. The highs are still falling.
- **Weight: 0.2.**
- **Change my mind:** Below 88 I go to 0. Above 108 I go to 0.5.

### ae1a0b68e0 (ETH)
- **Read:** Double bottom at 84.3/84.7, with price now 100, just under the day −20 high of 103.6. Day 0 volume picked up, but price did not move.
- **Weight: 0.3.**
- **Change my mind:** Below 88 I go to 0. A close above 104 takes me to 0.5.

### 129d4c0ebd (DOT)
- **Read:** A persistent downtrend from 250, with every rally failing (188 → 151 → 157 → 118 → 101). The low was 90.2 at day −7 and price is now 100. Resistance is 102 and then 111–118.
- **Weight: 0.2.**
- **Change my mind:** Below 91 I go to 0. Above 112 I go to 0.5.

{"c2e3254f16 (AVAX)": 0.3, "4d60bda5f8 (BTC)": 0.25, "0f5cd43f21 (ADA)": 0.5, "f6ee48f1a1 (LTC)": 0.35, "b4def9c423 (DOGE)": 0.2, "2132450ec6 (LINK)": 0.25, "727098e9dc (SOL)": 0.5, "303acee46a (XRP)": 0.2, "ae1a0b68e0 (ETH)": 0.3, "129d4c0ebd (DOT)": 0.2}

## Entscheidung 2026-07-12

## Strategy

I go long only when both the asset's own trend and the market's trend support it. Price must be above its 50-day mean, and the market's last close must be above its own 50-day mean. When both fail, the weight stays between 0 and 0.2. Within that band, the size depends on short-term structure: a higher low or double bottom with price above the 20-day mean scores higher, and a lower low or a failed breakout scores near 0.

**Market context, the same for every window:** the market has fallen from 152 to 100 over the window. The day −40 to −37 flush took it to 95.5, and it made a lower low at 91.9 on day −12. It has since bounced back to 100, but it is still below its 50-day mean (about 103) and well below the 120s range it held before the drop. That is a bear-market backdrop, so every weight stays small.

## a2efa01bcc (DOGE)
- **Read:** Down from 202 to 100, and lagging the market badly. After the day −37 crash, the bounce failed at 122, and price made a lower low at 95.6 on day −12. The bounce to 107–109 also failed. Price is below its 20-day mean (about 102.5) and far below its 50-day mean (about 118).
- **Weight:** 0. Downtrend intact, no base formed.
- **Change of mind:** a close above 109.

## ee2bd469ad (LINK)
- **Read:** Down from 176 to 100. Lows at 87.5 (day −36) and 87.7 (day −17) form a double bottom. Price is above its 20-day mean (about 96) but still below the 50-day mean (about 105) and below the 102–107 shelf.
- **Weight:** 0.15. Small position on the base, while the trend is still down.
- **Change of mind:** above 103 I add; below 87.5 I go flat.

## df125ed2dc (BTC)
- **Read:** Tracks the market almost one for one. It made a slightly lower low at 90.6 (day −11, against 92.7 on day −37) and has recovered to 100, above its 20-day mean (about 97). Resistance is at 104–105.
- **Weight:** 0.15.
- **Change of mind:** above 105 I add; below 90.6 I go flat.

## d0de6465a5 (ADA)
- **Read:** Down from 260 to 100, the weakest structure of the group. It made a lower low at 85.3 (day −17), then spiked to 123 on day −8 and fully gave the spike back. That is a failed breakout on fading volume.
- **Weight:** 0.05.
- **Change of mind:** a close back above 118 would justify adding; below 88 I go flat.

## bc198a6866 (DOT)
- **Read:** Down from 270 to 100. Lower highs and lower lows continue: 104.7 on day −36, then 94.2 on day −14. The rally to 106 on day −2 was rejected, and price is below its 20-day mean (about 101).
- **Weight:** 0.
- **Change of mind:** a close above 106.

## 5b05b68a29 (XRP)
- **Read:** Down from 199 to 100. It made a lower low at 92.9 (day −16), and the bounce stalled at 109. Price sits right at its 20-day mean (about 100.5) and well below its 50-day mean (about 112).
- **Weight:** 0.05.
- **Change of mind:** above 109 I add; below 93 I go flat.

## 80896997d4 (ETH)
- **Read:** Down from 185 to 100. Lows at 83.3 (day −36) and 83.7 (day −16) form a double bottom. It has bounced about 19% and sits above its 20-day mean (about 93). Overhead resistance is at 100–102.
- **Weight:** 0.15.
- **Change of mind:** above 102 I add; below 83 I go flat.

## 74d18f318f (SOL)
- **Read:** The best structure in the group. It made a higher low at 83.3 (day −17, against 78.2 on day −36) and a higher high at 109 (day −8), and it is holding about 100, above its 20-day mean (about 98). It is still below its 50-day mean and the 105–107 pre-crash shelf.
- **Weight:** 0.2.
- **Change of mind:** above 109 I go to about 0.4; below 92 I go flat.

## 1f544167f8 (LTC)
- **Read:** Down from 178 to 100. It made a slight lower low at 89.3 (day −18, against 92.1 on day −36), then bounced to 104.9 and is now drifting back toward 100. Price sits near its 20-day mean (about 98.5).
- **Weight:** 0.1.
- **Change of mind:** above 105 I add; below 89 I go flat.

## b2eba15adf (AVAX)
- **Read:** Down from 230 to 100. It made a lower low at 88.7 (day −23) on heavy volume, and the bounce to 111 failed. Day 0 was a down day with rising volume, and price is below its 20-day mean (about 102.5).
- **Weight:** 0.05.
- **Change of mind:** above 111 I add; below 97 I go flat.

{"a2efa01bcc (DOGE)": 0.0, "ee2bd469ad (LINK)": 0.15, "df125ed2dc (BTC)": 0.15, "d0de6465a5 (ADA)": 0.05, "bc198a6866 (DOT)": 0.0, "5b05b68a29 (XRP)": 0.05, "80896997d4 (ETH)": 0.15, "74d18f318f (SOL)": 0.2, "1f544167f8 (LTC)": 0.1, "b2eba15adf (AVAX)": 0.05}

## Entscheidung 2026-07-19

**Strategy:** I go long in proportion to how intact the trend and structure are. Full weight needs price above its rising medium-term averages with higher highs and higher lows. Partial weight goes to bases that hold above the crash lows and show strength relative to the market. I stay near flat when lower highs keep forming. Because the overall market is in a downtrend (from 138 to a 90–102 base), no window gets more than about half weight.

## 05bfa1dcd3 (SOL)
- **Read:** Crashed from about 170 to the 100–128 range, then broke down again to 78.7 at day -43. It made a higher low at 83.8 (day -24) and rallied to 108.4 (day -16). Since then it has faded to the 96–102 area on shrinking volume.
- **Relative strength:** Clearly better than the market off the lows (+23% versus +6%).
- **Key levels:** Support 96–97, resistance 108–110.
- **Weight:** 0.3. The base is decent, but the trend is still down and price sits below the 100-day average (around 108).
- **Change my mind:** A close below 96 takes me to 0. A close above 109 raises the weight.

## 6deac1b862 (ADA)
- **Read:** A long collapse from 220 to 94. It spiked to 115.6 on heavy volume (days -16/-15) and fully gave that back to 100. That is a failed breakout inside a downtrend.
- **Key levels:** Support 93–94, then 83. Resistance 108 and 116.
- **Weight:** 0.15.
- **Change my mind:** A close below 93 takes me to 0. A close above 116 raises the weight.

## 7be671d2e6 (ETH)
- **Read:** A double bottom at 80–82 (days -43 and -24), followed by a stair-step of higher highs (95 → 98 → 104) and higher lows (82 → 92 → 93.5). Price is above its 20-day average (about 96) but well below the 125 prior range.
- **Key levels:** Support 93–96, resistance 104.
- **Weight:** 0.4.
- **Change my mind:** A close below 93 takes me to 0.1. A close above 105 raises the weight.

## 3b39933c78 (LTC)
- **Read:** A double bottom at about 83.5 (days -43 and -25). Since then the lows keep rising: 87.4, 91.2, 93.7. Day -1 broke above the 98 range top on above-average volume (1.29). This is the cleanest base-and-breakout structure in the set.
- **Key levels:** Support 95–96, then 92. Resistance 102, then 110.
- **Weight:** 0.5.
- **Change my mind:** A close back below 94 cuts it to 0.15. A close above 103 takes it to 0.7.

## 6173a13414 (LINK)
- **Read:** Very similar to 7be671d2e6 (ETH). It double-bottomed at 83.4–83.6, then rallied to 103 (day -4), and is now at 100. The higher lows are 84.4, 89.7 and 93.8.
- **Key levels:** Support 94, resistance 103.
- **Weight:** 0.35.
- **Change my mind:** A close below 93 takes me to 0.1. A close above 104 raises the weight.

## 82c3849100 (AVAX)
- **Read:** A flush to 87.9 (day -30), then higher lows at 92, 97 and 98.6. Price has been holding a 97–110 range for a month, and it has been firm relative to the market since day -30.
- **Key levels:** Support 97–98, resistance 108–110.
- **Weight:** 0.35.
- **Change my mind:** A close below 97 takes me to 0.1. A close above 109 raises the weight.

## 83987c2628 (XRP)
- **Read:** It broke from the 120–135 range down to 95.7, then made a lower low at 91.9 (day -23). It bounced to 107.9 and is now pinned at 99–100 on very low volume. There is no higher-low confirmation yet.
- **Key levels:** Support 96–97, resistance 103 and 108.
- **Weight:** 0.25.
- **Change my mind:** A close below 96 takes me to 0. A close above 104 raises the weight.

## a0346ac2ae (DOT)
- **Read:** A persistent downtrend from 238, with lower highs at 213, 202, 175, 165, 127 and 110. Today was a red day to 100 that touched 98.3, sitting just above the 97–98 lows. It is weak relative to the market.
- **Key levels:** Support 97, resistance 105–109.
- **Weight:** 0.1.
- **Change my mind:** A close above 109 raises the weight. A close below 97 takes me to 0.

## c1c504396e (DOGE)
- **Read:** It outperformed into 160 (day -66), then gave it all back with lower highs at 127.7, 109.6 and 104. Lows are at 96–98, and volume is drying up at 100.
- **Key levels:** Support 96, resistance 104 and 110.
- **Weight:** 0.15.
- **Change my mind:** A close above 110 raises the weight. A close below 96 takes me to 0.

## 40c3ac36bf (BTC)
- **Read:** This is the market proxy itself. It is in a downtrend from 138 and sits in a 89–102 base, with lows at 89.3–89.8 and lower highs at 104, 100 and 101.4. Price is below the 100-day average (about 108).
- **Key levels:** Support 95–96, then 89. Resistance 102–104.
- **Weight:** 0.3.
- **Change my mind:** A close below 95 takes me to 0.1. A close above 104 raises the weight.

{"05bfa1dcd3 (SOL)": 0.3, "6deac1b862 (ADA)": 0.15, "7be671d2e6 (ETH)": 0.4, "3b39933c78 (LTC)": 0.5, "6173a13414 (LINK)": 0.35, "82c3849100 (AVAX)": 0.35, "83987c2628 (XRP)": 0.25, "a0346ac2ae (DOT)": 0.1, "c1c504396e (DOGE)": 0.15, "40c3ac36bf (BTC)": 0.3}

## Entscheidung 2026-07-26

**Strategy:** I go long only where the asset is trending up on its own and outperforming the market. I check three things: whether price is above its recent swing structure with higher lows, how it has moved since the market's day −26 low (market +11.6% since then), and where it sits against its 50‑day range. The market itself is in a relief bounce inside a larger downtrend (125 → 89.6 → 100), so I cap weights below 1.0 and give laggards little or nothing.

## 9fde39d411 (XRP)
Long downtrend from 172. Over the last 30 days it has chopped between 91 and 106 below a lower high at 106.4 (day −22). It is up only about 7% since day −26 while the market is up 11.6%, so it is lagging. Price sits mid‑range with no structure. **Weight 0.2.** A close above 106.5 would make me add; a close below 94 would take me flat.

## 7419ea0b01 (LINK)
It fell from a 121.5 peak (day −77) to 79.4 (day −31), then built steady higher lows at 81.6, 86.6, 89.4, 93.5 and 94.5. Day 0 broke above the 98–99 ceiling and closed at the high, 100. It is up about 22% from the low, roughly double the market's bounce. Next resistance is around 103–105. **Weight 0.55.** A close below 93.7 would invalidate this.

## dbc345b9e5 (LTC)
It bottomed at 82.1 on day −31 and has recovered steadily, with higher lows at 86.0, 90.2, 89.7 and 95.6. It is pressing its 100–100.9 highs, has outperformed the market off the low (+17%), and volume has been firm on up days. **Weight 0.5.** A close below 95.5 would invalidate this; above 101 adds conviction.

## c95544f900 (BTC)
This tracks the market exactly. It is a bounce from 89.6 with higher lows (95.2, 97.5), sitting at 100 just under the 101.8 high. It is still well below the 113–125 levels it held 60 to 80 days ago, so the larger trend is down. **Weight 0.35.** A close below 97 would take me lower; above 102 would take me higher.

## c0c5ed870c (AVAX)
It went from 179 to 100, then crashed to 84.2 on day −37 and has ranged choppily between 91 and 105 since. The day −1 spike from 93 to 100.5 came out of a fresh dip to 91. It has gone nowhere since day −51 while the market rose, so relative strength is weak. **Weight 0.2.** A close above 105.5 would make me add; below 91 would take me flat.

## b8ffa4d716 (DOT)
This is the weakest chart: 226 down to 100 with persistent lower highs (122 → 106.9 → 105.9 → 105). It has been flat around 96–108 for 30 days while the market rallied 11%, so it is clearly lagging. **Weight 0.1.** Only a close above 109 would change my view.

## 14f562cf9f (SOL)
It rallied from 78.3 (day −50) to 107.3 (day −23), outperforming the market, then pulled back to 95.7 and is now bouncing to 100. The trend off the low is constructive, but the last 3 weeks show a lower high. **Weight 0.4.** A close above 103 would make me add; below 95.5 would take me flat.

## bd91e4e4c0 (ETH)
It made a double bottom around 77 (days −50 and −30), followed by higher lows at 79.3, 87.7, 92.2 and 94.5. Day 0 closed at 100, at the high, clearing the 99.6–100.1 resistance. It is up about 24% since day −26, double the market's move. **Weight 0.6.** A close below 94.5 would invalidate this.

## 45c795036c (ADA)
It is down from 217. A spike to 120.5 (day −22) was fully faded. It now sits in a 97–109 range, rejected at 105–109 on day −4, with fading volume. Its relative strength since day −26 is modest. **Weight 0.3.** A close below 97 would take me flat; above 105.5 would make me add.

## 08eb8d0d3f (DOGE)
It was the earlier leader, peaking at 161.6 on day −73, but has since collapsed to 94.3 (day −3, on above‑average volume). It is roughly flat since day −26 while the market is up 11.6%. It is stuck in a 93–108 range with a lower high at 108.2. **Weight 0.15.** A close above 106 would make me add; below 93 would take me flat.

{"9fde39d411 (XRP)": 0.2, "7419ea0b01 (LINK)": 0.55, "dbc345b9e5 (LTC)": 0.5, "c95544f900 (BTC)": 0.35, "c0c5ed870c (AVAX)": 0.2, "b8ffa4d716 (DOT)": 0.1, "14f562cf9f (SOL)": 0.4, "bd91e4e4c0 (ETH)": 0.6, "45c795036c (ADA)": 0.3, "08eb8d0d3f (DOGE)": 0.15}

## Entscheidung 2026-08-02

**Strategy:** I stay long when the trend structure is constructive: higher lows, price holding above recent range support, and strength equal to or better than the market. I cut the weight when the window shows a sequence of lower highs or has broken a range floor. Because the market is still basing after a large drop (from about 129 to 92, now ranging 98–105), I keep most weights moderate and don't go fully long.

## 6cf2f84bd1 (SOL)
- **Read:** It peaked near 132 (day -83), crashed to 84.5 (day -57), and rebounded to 112 (day -30). Since then it has made lower highs at 111.8, 107, 106 and 104.7. Support sits at 98–99, and that level was undercut intraday at 95.9 on day -1. It is drifting lower inside a range and tracking the market.
- **Weight:** 0.3. The base is still intact, but the highs keep stepping down.
- **Change of mind:** A close above 107 would raise the weight. A close below 95.9 would take it to 0.

## 0154071039 (ETH)
- **Read:** It bottomed at 80 (day -37), then made higher lows at 82, 91, 95.6 and 98. Highs are at 103–104 and it closes at 100. It has recovered much more from its lows than the market has.
- **Weight:** 0.5. The higher-low structure and relative strength justify it.
- **Change of mind:** A close below 96.6 would cut it. A break above 104 would add.

## d4e512fcf1 (LTC)
- **Read:** It fell to 88 (day -39), rallied to 107.7 (day -12), and is now pulling back from a 105–106 plateau. Higher lows sit at 96.6 and 97.6. It is a healthy pullback within an uptrend from the low.
- **Weight:** 0.45.
- **Change of mind:** A close below 97.5 means out. A close above 108 means add.

## 433bace030 (ADA)
- **Read:** It collapsed from about 150 to 73 (day -38) and spiked to 105 (day -29). It then faded to 81 (day -6). Day 0 was a large expansion bar from 92 to 100 on volume of 1.73, the highest in weeks. Resistance is the 101–105 spike zone.
- **Weight:** 0.45. The momentum and volume are good, but the asset is very volatile and sits right under resistance.
- **Change of mind:** A close above 105.5 would take it to full. A close below 88 means out.

## 88b85e8863 (XRP)
- **Read:** It declined from 136 to 93 (day -38) and rallied to 109 (day -29). Since then it has made lower highs at 107 and 105.2. Lows are around 96.1 and it closes at 100. The structure is a gently falling range.
- **Weight:** 0.3.
- **Change of mind:** A close below 96 means out. A close above 105.5 would raise it.

## b174161c15 (LINK)
- **Read:** It bottomed at 83.6 (day -38) and has made higher lows at 89.7, 93, 95.5 and 94.1. Highs are rising: 103, 104.5, 106.3. Day 0 was a strong recovery bar from 96 to 100.
- **Weight:** 0.45. The uptrend structure off the low is intact.
- **Change of mind:** A close below 94 means out. A close above 106.5 would add.

## 94daa95ab7 (BTC)
- **Read:** This window tracks the market almost exactly. It is basing at 98–105 after breaking down from the 115–125 range. Lows are stepping up gently (92.2, 97.3, 98.0).
- **Weight:** 0.4. I hold neutral-to-modest exposure to the base.
- **Change of mind:** A close below 97.3 means out. A close above 105.3 would add.

## d4e102ee44 (AVAX)
- **Read:** It crashed from 136 to 90 (day -44, with a wick to 86.7) and has ranged 92–108 since. Highs are lower (108.6, 104, 104.5). Day 0 was a sharp reversal from 94.5 to 100 on volume above average. It is range-bound.
- **Weight:** 0.35.
- **Change of mind:** A close below 92 means out. A close above 105 would add.

## 42b0c739a5 (DOGE)
- **Read:** It peaked at 167 (day -80) and has fallen persistently to around 100. Lower highs are at 112, 106.8, 104.6 and now about 101. It is clearly underperforming the market.
- **Weight:** 0.15. This is a weak downtrend.
- **Change of mind:** A close above 105 would make me reconsider. A close below 95.6 takes it to 0.

## da21491676 (DOT)
- **Read:** It has fallen from 208 to about 100 in a persistent downtrend. Lower highs are at 112, 109.4 and 104. It broke down to 93.6 on day -6 and is now bouncing back to 100. It has strongly underperformed the market.
- **Weight:** 0.1.
- **Change of mind:** A close above 104 would make me reconsider. A close below 93 takes it to 0.

{"6cf2f84bd1 (SOL)": 0.3, "0154071039 (ETH)": 0.5, "d4e512fcf1 (LTC)": 0.45, "433bace030 (ADA)": 0.45, "88b85e8863 (XRP)": 0.3, "b174161c15 (LINK)": 0.45, "94daa95ab7 (BTC)": 0.4, "d4e102ee44 (AVAX)": 0.35, "42b0c739a5 (DOGE)": 0.15, "da21491676 (DOT)": 0.1}

## Entscheidung 2026-08-09

**Strategy:** I go long only when an asset's own structure is constructive and it is at least keeping pace with the overall market. Constructive means higher lows since the capitulation around day -65 to -45, holding above recent support, and no fresh lower highs. Persistent lower highs or a breakdown toward the lows get a near-flat weight. Weights scale with the strength of the base and the relative strength against the market, which is itself only basing (low 90.3 at day -40, range 96–102.5, now 100) and so caps conviction.

---

### 3dcb5a66a8 (DOGE)
- **Read:** A long downtrend from the 166 peak (day -96). Since day -37 the highs have kept falling: 113.2, 108.7, 106.8, 103.2. Price is now pinned in a 98–103 range on fading volume. From day -40 it has gone 103.9 → 100 while the market went 90 → 100, so it is clearly lagging.
- **Weight:** 0.1, because the trend is down and there is no relative strength.
- **Change my mind:** a close above 107 would break the lower-high sequence. A close below 97.6 would take the weight to 0.

### e483e72682 (AVAX)
- **Read:** It crashed from 163 to a low of 88.5 (day -51). Since then it has chopped in a 94–110 range. Highs are slightly lower (110.8, then 108.8), and the low at day -8 was 94.1. Price sits at 100, mid-range. Since the low it has roughly matched the market.
- **Weight:** 0.25. The structure is neutral range trading with no clear edge.
- **Change my mind:** a close above 109 would be a range breakout and I would add. A close below 94 would take it to flat.

### df9d045dd5 (LINK)
- **Read:** The low was 85.6 (day -45). The lows have risen since: 91.9, 96.3, and now 98.5–99.8. Highs sit at 105–109. Price is coiling at 100, above the rising lows, and moving in line with the market.
- **Weight:** 0.4 for a constructive base.
- **Change my mind:** below 96 the base fails and I would go to 0.1. A close above 109 would push it to 0.7.

### fd2c65c61c (ETH)
- **Read:** The low was 79.1 (day -44). Since then it has risen about 26% against roughly 11% for the market, the strongest relative recovery of the group. Higher lows are in place at 89.7, 94.4 and 95.4, with a tight 96–102 consolidation under 102.4.
- **Weight:** 0.5 for a clear uptrend from the lows with relative strength.
- **Change my mind:** below 95 the higher-low structure breaks and I would go to 0.15. A close above 103.7 would push it to 0.75.

### 3a1066ff4e (ADA)
- **Read:** It capitulated from 150 to a low of 71.1 (day -45). A first spike to 102.8 faded back to 79, then a second rally ran from 79 (day -13) to 108.8 intraday (day -3) on rising volume. That is very strong momentum. However, the 103–109 area rejected it, and it closed at 100.
- **Weight:** 0.45. Momentum and volume are good, but price is failing at the prior spike high and the swings are volatile.
- **Change my mind:** a close above 105 would confirm the breakout and I would add. A close below 93 would take it to 0.1.

### ffceb7ac58 (XRP)
- **Read:** The highs keep falling from the low of 98.0 (day -44): 115.0, 113.1, 106.2. The past week slid from 105.5 to a low of 98.3, so it is retesting the base lows. It is underperforming the market.
- **Weight:** 0.1, because it is weak and sitting on support with no sign of a bounce.
- **Change my mind:** a close above 108 would make me reconsider. A close below 98 would take it to 0.

### 60b17d9806 (BTC)
- **Read:** This tracks the market itself. The low was 89.1 (day -39), with higher lows since at 94.8, 95.3 and 96.0. It has been ranging 96–103 for a month, and the drop has not been recovered.
- **Weight:** 0.35. This is a neutral-to-constructive base, though not a trend yet.
- **Change my mind:** a close above 103.2 would add to the position. A close below 96 would cut it to 0.1.

### 63ec285256 (LTC)
- **Read:** The low was 86.4 (day -45). It rallied to 105.9 (day -19) and the lows have risen since, to 94.4 and then 96.0. It is holding 96–106 and is slightly stronger than the market.
- **Weight:** 0.4 for a constructive base.
- **Change my mind:** below 96 I would cut to 0.1. A close above 106 would push it to 0.7.

### 42f34dd757 (SOL)
- **Read:** It rallied to 110.1 (day -36) and has trended down since. The highs fell to 108.5, 103.6, 101.6 and 100.7, and the low slipped to 92.5 (day -8). It has just bounced to 100 and is testing the falling highs.
- **Weight:** 0.2. The trend is down, with only a small allowance for the bounce.
- **Change my mind:** a close above 103.5 would break the downtrend line. A close below 94 would take it to flat.

### d232524aa3 (DOT)
- **Read:** A severe downtrend from 208 (day -165) to 93.6 (day -13). Every rally since the crash has been capped around 108–113. The last spike to 108.9 failed straight back to 100. It is lagging the market badly.
- **Weight:** 0.1 for a persistent downtrend with failed rallies.
- **Change my mind:** a close above 109 would make me reconsider. A close below 93.6 would take it to 0.

{"3dcb5a66a8 (DOGE)": 0.1, "e483e72682 (AVAX)": 0.25, "df9d045dd5 (LINK)": 0.4, "fd2c65c61c (ETH)": 0.5, "3a1066ff4e (ADA)": 0.45, "ffceb7ac58 (XRP)": 0.1, "60b17d9806 (BTC)": 0.35, "63ec285256 (LTC)": 0.4, "42f34dd757 (SOL)": 0.2, "d232524aa3 (DOT)": 0.1}

## Entscheidung 2026-08-16

**Strategy:** I trend-follow with a relative-strength filter.
- Long exposure needs price above its recent range midpoint, higher lows, and performance at least matching the market, which is itself flat in a 93–106 range after crashing from ~130.
- Lower highs or underperformance push the weight towards 0.
- Tight, undecided ranges get small partial weights.

## 0aa8baf34d (DOT)
- **Read:** A long, persistent downtrend from the 219 spike. Each high is lower than the last: 183 → 138 → 119.6 → 114.6. Price sits at 100, just above the 98.6 low from day -20, and the asset has lagged the market badly.
- **Weight:** 0.0. There is no sign the downtrend has ended.
- **Change my mind:** a close above 115, which would break the lower-high sequence.

## 80534a249b (AVAX)
- **Read:** Crashed to 89.7 at day -58, then ranged 95–112 for two months. The highs inside the range are drifting lower: 112.4 → 110.4 → 108.6. Price is at 100, mid-range, moving roughly with the market.
- **Weight:** 0.2. The base is neutral and has no momentum.
- **Change my mind:** above 111 I add; below 95 I go flat.

## a4ddd99d5a (DOGE)
- **Read:** Fell from 170 to 100. It has spent about a month in a very tight 97–106 coil on shrinking volume. That shows no demand, and it has slightly underperformed the market.
- **Weight:** 0.15.
- **Change my mind:** a breakout above 106 to add; below 97, flat.

## e71150b5e0 (ADA)
- **Read:** Bottomed at 79 on day -52, then made higher lows (79 → 87.9) and higher highs (114 → 121). It clearly outperformed the flat market. The last 10 days pulled back from 115 to 100, but on low volume, so it looks like a correction rather than distribution.
- **Weight:** 0.4. The structure is constructive, but the pullback is still in progress.
- **Change my mind:** below 88 the structure is broken; a reclaim of 110 would let me raise the weight.

## ba340aff4e (LINK)
- **Read:** Double bottom at about 74.5 (days -71 and -52). Since then it has made higher lows at 80, 84 and 87, and it just broke out of an 85–95 range. Day -1 moved to 103.8 on 1.66x volume. The asset gained about 30% off the low while the market went nowhere, which is the strongest relative strength in this set. Resistance sits at 103–115, the old shelf from days -100 to -94.
- **Weight:** 0.7.
- **Change my mind:** a close back below 92 would mean a failed breakout.

## 3180a3fa18 (LTC)
- **Read:** Rebounded from 89 to 108.5 by day -28. Since then it has made lower highs (108.3 → 105.3 → 103.8) and is sliding back to 99–100. It roughly tracks the market.
- **Weight:** 0.3.
- **Change my mind:** below 98, flat; above 105, add.

## f311e95160 (ETH)
- **Read:** Rising lows (80.6 → 91.3 → 96.1 → 97.1) after the crash, now in a tight 97–105 consolidation on very low volume. It is slightly stronger than the market off the lows.
- **Weight:** 0.4.
- **Change my mind:** below 97, cut; a breakout above 105, add.

## fcc577007e (BTC)
- **Read:** This asset moves essentially in line with the market. It is a contracting triangle: lows rising (92.4 → 97.5 → 99.0) and highs falling (106.4 → 104.6 → 104.1). Price at 100 sits near the lower edge.
- **Weight:** 0.3. It is neutral beta exposure.
- **Change my mind:** below 99, flat; above 104.5, add.

## 661b8799e3 (XRP)
- **Read:** The 130 spike at day -62 failed. Since then it has made a clean staircase of lower highs (119 → 117 → 112 → 110 → 105) and lower lows down to 100, underperforming the market.
- **Weight:** 0.05.
- **Change my mind:** a close above 110.

## ce6463521f (SOL)
- **Read:** Rallied from 80.6 to 112.6 by day -43, then gave back most of the move. It has settled into a 94.6–105 range and is drifting at 100. The higher low against the crash is intact, but momentum has faded.
- **Weight:** 0.25.
- **Change my mind:** below 96, flat; above 105, add.

{"0aa8baf34d (DOT)": 0.0, "80534a249b (AVAX)": 0.2, "a4ddd99d5a (DOGE)": 0.15, "e71150b5e0 (ADA)": 0.4, "ba340aff4e (LINK)": 0.7, "3180a3fa18 (LTC)": 0.3, "f311e95160 (ETH)": 0.4, "fcc577007e (BTC)": 0.3, "661b8799e3 (XRP)": 0.05, "ce6463521f (SOL)": 0.25}

## Entscheidung 2026-08-23

**Strategy.** I go long when a window has broken out of its recent base and price is near or above the levels it broke down from. I cut the weight when there is overhead supply from an older range, when the last bars show blow-off wicks on climactic volume, or when the asset has a history of pumps that fade. The market series sets the backdrop: it fell from about 105 to 76, based at 77–85 for two months, then rallied about 23% in 4 days to 100. That rally is real, but it is extended in the short term, so no window gets a full 1.0.

## b73900da87 (DOGE)
- **Read:** The asset broke down from a 105–125 range (day -82) to a 74–79 base that lasted about 50 days. It then ran +33% in 4 days on 2–3.5x volume.
- **Levels:** Day -1 wicked to 107.9 and closed at 98.4, a rejection right at the old breakdown zone of 105–110. Before the spike it was weaker than the market.
- **Weight:** 0.45. The breakout from the base is valid, but there is heavy supply directly overhead and a blow-off wick.
- **Change my mind:** A close below 88 means the breakout failed (go to 0). A close above 108 means I add.

## 43b47ddde6 (LTC)
- **Read:** It tracks the market closely. It based at 83–91 and broke out to 100.
- **Levels:** The old range at 100–110 sits overhead. Day -1 wicked to 106 and was rejected, but the close held near 100. The higher lows since day -60 (75 → 83 → 84) are constructive.
- **Weight:** 0.55. A clean base breakout, with resistance close by.
- **Change my mind:** A close below 91.

## ddb7c1413e (XRP)
- **Read:** A persistent downtrend took it from 95 to 65 with lower lows all the way to day -5. It then went parabolic, +52% in 4 days.
- **Levels:** Day -1 had 6x volume, a wick to 111.8 and a close at 96, which looks like a climax. Even so, price has reclaimed the whole 87–95 range and sits near its 180-day highs.
- **Weight:** 0.4. The trend has reversed, but the move is very extended and the volume looks exhausted, so a retest toward 85–90 is likely.
- **Change my mind:** A close below 88.

## 8e04abbb4a (SOL)
- **Read:** After the crash low at 63 (day -78) it has made higher lows: 67, 74, 75. It then broke out of a 76–82 base to 100.
- **Levels:** Resistance is the day -104 high of about 103. The day -1 wick to 107.7 was rejected.
- **Weight:** 0.6. The structure is constructive and only modest resistance remains overhead.
- **Change my mind:** A close below 92.

## a678c771bc (ETH)
- **Read:** It double-bottomed at 61 (days -78 and -58) and then trended steadily higher, 63 → 78, before breaking out to 100–102.
- **Levels:** Price is above the prior peaks of 96–100 (days -132 to -128), so it is at 180-day highs. There is no climactic wick, and volume is cooling in an orderly way after the breakout.
- **Weight:** 0.7. This is the cleanest trend structure of the set.
- **Change my mind:** A close below 90.

## 139f124376 (LINK)
- **Read:** It made higher lows from 60.7 and was already rising (70 → 83) before the market spike. It is now at 100, above every level in the window; the prior high was 94.2.
- **Levels:** It shows strong relative strength against the market. The day -1 wick to 109 is the only blemish.
- **Weight:** 0.75. It is breaking to new highs, and the pre-existing uptrend has now been confirmed.
- **Change my mind:** A close below 91, which would mean the breakout gap is filling.

## 934d173586 (ADA)
- **Read:** It crashed from 131 to 61. Since then it has spiked and faded twice: to 88 at day -50 (fell back to 69) and to 93 at day -17 (fell back to 77). It is now on a third spike, with a wick to 113.8.
- **Levels:** The old range at 104–124 is overhead.
- **Weight:** 0.3. The pump-and-fade behaviour has repeated, and the blow-off wick sits right into resistance.
- **Change my mind:** A close below 92 means exit. A close above 110 would earn more weight.

## 2ec4f349d5 (BTC)
- **Read:** Its closes match the market series, so this is the benchmark itself. It based at 75–85, broke out to 100, and is consolidating calmly; day -1 had a narrow range and volume was normalizing.
- **Levels:** Resistance is the 100–106 range high from days -123 to -105.
- **Weight:** 0.6. The base breakout is orderly, and it has no excess wick.
- **Change my mind:** A close below 92.

## f18183e22e (DOT)
- **Read:** A long primary downtrend took it from 179 to 81. The spike to 100, with a wick to 111, broke the lower-high sequence (97 → 93).
- **Levels:** The 100–110 area is the breakdown zone from day -82, so there is overhead supply. The larger trend is still down.
- **Weight:** 0.35.
- **Change my mind:** A close below 90.

## 9a9fb6ddcf (AVAX)
- **Read:** It broke down from a 115–135 range to a 75 low, then based at 82–92. It spiked to 103, wicked to 109 on day -1 and closed at 98.5.
- **Levels:** The breakdown level at 107–117 is overhead.
- **Weight:** 0.45. The base breakout is valid, but supply is heavy above and the wick shows rejection.
- **Change my mind:** A close below 90.

{"b73900da87 (DOGE)": 0.45, "43b47ddde6 (LTC)": 0.55, "ddb7c1413e (XRP)": 0.4, "8e04abbb4a (SOL)": 0.6, "a678c771bc (ETH)": 0.7, "139f124376 (LINK)": 0.75, "934d173586 (ADA)": 0.3, "2ec4f349d5 (BTC)": 0.6, "f18183e22e (DOT)": 0.35, "9a9fb6ddcf (AVAX)": 0.45}

## Entscheidung 2026-08-30

## Strategy
I follow the trend and filter by the market. The market (its largest coin) broke out of a 77–86 range that lasted about 75 days, jumped to about 100, and has held there for a week, so the backdrop favours longs. For each coin I size by three things: whether it is holding above its pre-spike base, how much of the spike it has already given back, and how it has done against the market since the breakout (market: 81 → 100, about +23%). Strong, shallow pullbacks get a large weight. Weak coins that have given back most of the spike get a small one.

## 83fafdeb6d (XRP)
- **Read:** The coin fell from about 105 to a 73–75 base, then spiked to a high of 125.
- **Since the spike:** It has made a run of lower highs (112 → 109 → 107 → 103) and now sits at 100. That is about half the spike retraced, but it is still far above the base.
- **Versus the market:** 74 → 100 (+35%), better than the market.
- **Key levels:** Support is 98.4 (today's low), then the 93–95 gap. Resistance is 107–108.
- **Weight: 0.5.** It is strong against the market, but the falling highs are a warning.
- **Change my mind:** A close below 96 cuts it to 0.2. A close above 108 raises it to 0.8.

## 175496ed25 (LTC)
- **Read:** The base was about 92–93. It spiked to 115.7 and has given back about two thirds of the move to reach 100.
- **Versus the market:** 92.6 → 100 (+8%), well behind the market. Volume is fading.
- **Key levels:** Support is 98.9, then 92. Resistance is 105–110.
- **Weight: 0.3.**
- **Change my mind:** Below 97 goes to 0. A reclaim of 106 goes to 0.6.

## 3cc461550a (LINK)
- **Read:** The trend was already turning up before the spike, with higher lows at 65, 73, 85 and now about 100. It is above the pre-crash range of 81–96.
- **Since the spike:** It peaked at 113 and the pullback is orderly.
- **Versus the market:** 74.5 → 100 (+34%), ahead of the market.
- **Key levels:** Support is 98.6, then 95. Resistance is 107.5 and 113.
- **Weight: 0.7.**
- **Change my mind:** A close below 95 cuts it to 0.3.

## b8746583f1 (ETH)
- **Read:** The base was 77–79. It spiked to 105.4 and has given back only about 20% of that.
- **Context:** It has reclaimed the pre-crash range of 83–98 and is holding at 100–104.
- **Versus the market:** 78 → 100 (+28%), slightly ahead of the market.
- **Key levels:** Support is 98.8, then 96. Resistance is 104–106.
- **Weight: 0.7.**
- **Change my mind:** A close below 96 cuts it to 0.3. A break above 106 raises it to 0.9.

## ae4be0bf8e (BTC)
- **Read:** This series tracks the market. It broke out of the 77–86 range to 100 and is moving sideways between 99 and 104 on falling volume, which looks like a bull flag.
- **Key levels:** Support is 99, then 94. Resistance is 104–105.
- **Weight: 0.65.**
- **Change my mind:** A close below 94 cuts it to 0.25. A close above 105 raises it to 0.9.

## 35d3a185fa (DOGE)
- **Read:** The coin has been in a long decline (141 → 84). It spiked from a base of about 85 to 122.9 and has given back about 60% of that, with lower highs.
- **Versus the market:** 85 → 100 (+18%), behind the market.
- **Key levels:** Support is 98.5, then 90. Resistance is 109–110.
- **Weight: 0.4.**
- **Change my mind:** Below 96 goes to 0.1. Above 110 goes to 0.7.

## f8ca6f81c6 (ADA)
- **Read:** The coin keeps pumping and then fully fading. It spiked to 104 around day -57 and faded back to 81. It spiked to 110 around day -24 and faded back to 91. It has now spiked to 134 and is about 78% retraced.
- **Versus the market:** 90.6 → 100 (+10%), weak.
- **Key levels:** Support is 98.3, then 91. Resistance is 111.
- **Weight: 0.2.**
- **Change my mind:** A close above 111 raises it to 0.5. A close below 95 takes it to 0.

## b148c43f64 (SOL)
- **Read:** This is the cleanest structure in the set. It has made higher highs (101 → 108.7) and higher lows (92 → 95 → 100) after the breakout, and it is above the pre-crash range of 80–95.
- **Versus the market:** 75 → 100 (+33%), well ahead.
- **Key levels:** Support is 98.6, then 93–95. Resistance is 108.7.
- **Weight: 0.8.**
- **Change my mind:** A close below 94 cuts it to 0.35.

## 1ca7ac78e9 (DOT)
- **Read:** The coin is in a long decline (200 → 92). It spiked to 126 and has given back about 76% of that.
- **Versus the market:** 93 → 100 (+7.5%), weak.
- **Key levels:** Support is 98.7, then 92. Resistance is 108–110.
- **Weight: 0.25.**
- **Change my mind:** Above 110 goes to 0.6. Below 95 goes to 0.

## 76be154062 (AVAX)
- **Read:** The coin is in a decline (147 → 89) and sat in a base of 88–92 for about 40 days. It spiked to 116.9 and has given back about 60% of that.
- **Versus the market:** 89 → 100 (+12%), behind the market.
- **Key levels:** Support is 98.6, then 92. Resistance is 107.
- **Weight: 0.35.**
- **Change my mind:** Below 95 goes to 0.1. Above 108 goes to 0.65.

{"83fafdeb6d (XRP)": 0.5, "175496ed25 (LTC)": 0.3, "3cc461550a (LINK)": 0.7, "b8746583f1 (ETH)": 0.7, "ae4be0bf8e (BTC)": 0.65, "35d3a185fa (DOGE)": 0.4, "f8ca6f81c6 (ADA)": 0.2, "b148c43f64 (SOL)": 0.8, "1ca7ac78e9 (DOT)": 0.25, "76be154062 (AVAX)": 0.35}

## Entscheidung 2026-09-06

## Strategy
I go long when an asset has broken out of a multi-month base, holds above the breakout consolidation, and the overall market agrees. The weight scales with relative strength against the market, with how clean the structure is (higher lows, closing near the highs), and with how much supply sits overhead from the earlier crash. If price loses the post-breakout consolidation lows, the breakout is treated as failed and the weight goes to flat.

**Market context, applied to every window:** The market fell from about 102 to 76 between day -119 and day -93. It then based between 73 and 83 for about 75 days and broke out at day -18. It is now holding 96–101, which is constructive.

## b04ab62aa4 (SOL)
- **Structure:** Fell from 91 to 58, then based between 63 and 77 for months. Broke out at day -18 from 72 and has run to 100.
- **Since the breakout:** It has held 91–104, and the lows are rising: 91.4, then 93.1, then 96.8.
- **Relative strength:** Up about 43% from the base, versus about 27% for the market.
- **Levels:** It is above the old pre-crash range (78–92), so there is little overhead. Resistance is 103.8; support is 91–94.
- **Weight:** 0.8, for a strong trend with clear relative strength.
- **Change my mind:** A close below 91.

## 82e8309214 (XRP)
- **Structure:** Based at 70–80, then had a blow-off spike with a wick to 119.4. Since then it has digested between 92 and 107.
- **Overhead:** The pre-crash range at 93–106 sits right here.
- **Today:** Low volume, with no follow-through above 102.
- **Weight:** 0.6. The trend is up, but the spike high marks a supply zone and price is chopping inside the old range.
- **Change my mind:** A close below 92.

## 1e164430b2 (DOT)
- **Structure:** A 6-month downtrend from 155 to 77, then a breakout spike to 105.4. It pulled back to a higher low at 83.7 and has rallied five days in a row.
- **Today:** Closed at 100, the top of the range, on 1.67 volume.
- **Overhead:** Heavy, at 110–140.
- **Weight:** 0.6. The momentum is fresh, but this is the start of a reversal inside a larger downtrend.
- **Change my mind:** A close below 88.

## 4a110cff5f (LINK)
- **Structure:** Based at 53–65, then stair-stepped higher: 72 at day -22, 90 at day -16, and a breakout today to 100 on 1.70 volume.
- **Levels:** This is the highest level in 180 days, above the old highs of 76 and 82, so there is no overhead supply.
- **Relative strength:** It is clearly the strongest name here.
- **Weight:** 0.9.
- **Change my mind:** A close below 89, which would mean losing the consolidation.

## 62ead1913e (AVAX)
- **Structure:** Fell from 130 to 72, then based at 76–88. Broke out with a wick to 105, held 89–96, and is now pushing to 100 with higher lows.
- **Overhead:** Supply at 110–125 limits the upside.
- **Weight:** 0.65.
- **Change my mind:** A close below 89.

## a8c0775f12 (LTC)
- **Structure:** Fell from 110 to 72, then recovered to 80–87. Broke out to 100.9, pulled back to 86, and reclaimed 100 on a 2.3-volume day at day -1.
- **Overhead:** The old range at 100–110 is overhead.
- **Weight:** 0.65.
- **Change my mind:** A close below 90.

## c438589c09 (BTC)
- **Structure:** This series tracks the market itself. It broke out of the 73–83 base and has held 95–101.
- **Levels:** It is testing the pre-crash high at 101–103.
- **Today:** Low volume.
- **Weight:** 0.7. The trend is constructive, but price is at resistance.
- **Change my mind:** A close below 94.5.

## 82483e0db5 (ADA)
- **Structure:** Fell from 130 to 66, then rallied and failed twice: to 89 at day -64 and to 95 at day -31. It then spiked to 115.7 and has ranged 85–102.
- **Volatility:** High, with a pattern of rallies fading.
- **Positives:** The most recent lows are rising: 84.8, then 85.9, then 93.6.
- **Overhead:** Supply at 105–125.
- **Weight:** 0.5.
- **Change my mind:** A close below 85.

## 1ee3c102f8 (ETH)
- **Structure:** Fell from 96 to 60, then recovered steadily from 62 to 76. Broke out to 100 on a gap day at day -18 and has held 94–102 since.
- **Levels:** It is now at the pre-crash highs (96–98), with little supply above.
- **Weight:** 0.8, for a clean, orderly trend.
- **Change my mind:** A close below 93.5.

## 0ee4e5af83 (DOGE)
- **Structure:** Peaked at 130, fell to 76, and spent a long time ranging at 76–81. Spiked to 110.9, then pulled back to 88. It has since swung widely, including a wick to 104.7 at day -1 that faded.
- **Overhead:** Heavy, at 110–127.
- **Weight:** 0.55.
- **Change my mind:** A close below 88.

{"b04ab62aa4 (SOL)": 0.8, "82e8309214 (XRP)": 0.6, "1e164430b2 (DOT)": 0.6, "4a110cff5f (LINK)": 0.9, "62ead1913e (AVAX)": 0.65, "a8c0775f12 (LTC)": 0.65, "c438589c09 (BTC)": 0.7, "82483e0db5 (ADA)": 0.5, "1ee3c102f8 (ETH)": 0.8, "0ee4e5af83 (DOGE)": 0.55}

## Entscheidung 2026-09-13

## Strategy

I follow the trend and filter by the market. I go long when price has broken out of a base and is holding above it with higher lows, and I add when the range is tight and the asset is strong relative to its own history. I cut exposure after a blow-off spike that gets rejected, or when price loses the low of the post-breakout range. Every window in this set shares one market backdrop: a crash from about 106 to about 77, a 60-day base at 76–85, and a breakout at day −25 that is now holding 99–106. That backdrop supports moderate exposure but not maximum exposure.

---

### 27533e9764 (DOT)
- **Read:** A long downtrend took price from 160 to 76, then it based at 76–85. A first breakout reached 103 and faded back to 82. On day −5 a climactic spike hit 128.5 on 4× volume, then reversed hard to 100.
- **Structure:** This is a classic blow-off and rejection. Price is still above the base, but the spike's range of 104–128 is now overhead supply. Supports are at 90 and 84.
- **Weight:** 0.25. I keep a small position because the base held and the market is supportive. I don't add, because the spike failed.
- **Change mind:** A close above 112 means the spike was absorbed, so I'd raise. A close below 90 means flat.

### 10b6ba32f8 (LTC)
- **Read:** The pre-crash range was 100–112. The crash took price to 77, then it based at 82–88. The breakout reached 103, pulled back to 89, then made a higher high attempt at 110.6 that was wicked off. Closes are now holding 97–102.
- **Structure:** Higher lows at 89 and then 96 point upward. Price is retesting the old pre-crash range floor at about 100.
- **Weight:** 0.55.
- **Change mind:** I'd add above 103 and go flat below 95.

### 0d37355410 (XRP)
- **Read:** A slow bleed took price to 74, followed by a vertical breakout to a 126.7 wick. Since then it has ranged 98–113. The lows at 99–100 (days −14, −11, −3) have held three times.
- **Structure:** The range sits well above the base. Highs are lower (113, 110, 108), so the move is compressing toward support.
- **Weight:** 0.45.
- **Change mind:** I'd add above 108. Below 98, support is lost and I go flat.

### 3bf83627f1 (ADA)
- **Read:** This is a volatile name. It crashed to 68, saw several failed spikes (98, 104), then broke out to a 127 wick. Since then it has ranged 93–114 with lower highs (114, 111, 110). It sits at 100.
- **Structure:** The post-breakout range is intact, but momentum is fading. Support is at 93–95.
- **Weight:** 0.4.
- **Change mind:** I'd add above 110. Below 93 means flat.

### 9ebfc7d6b2 (ETH)
- **Read:** The crash bottomed at 61, followed by a steady recovery and a base at 75–77. A gap-and-go breakout reached 101.6. Since then price has held a tight 96–103 flag for three weeks, and the day −2 spike to 107.6 had its closes held.
- **Structure:** This is the strongest structure in the set. Price is above the pre-crash range of 81–95 and near the 6-month highs. Volatility is contracting above the breakout.
- **Weight:** 0.7.
- **Change mind:** I'd add above 104 and cut below 95.

### a9cd48fa50 (SOL)
- **Read:** Price based at 72–78, broke out, and made a higher high at 110 on day −17. It pulled back to a higher low at 98 and is now at 100. The old pre-crash highs at 94–98 now act as support.
- **Structure:** The uptrend is intact, with higher lows at 98 and 99.
- **Weight:** 0.6.
- **Change mind:** I'd add above 108. Below 97 means a failed higher low, and I'd cut to 0.2.

### ad89560147 (LINK)
- **Read:** The breakout came early, at day −33 from a 73 base. Price reached 107, then a second leg spiked to 122 on day −6. It has now fully retraced to 100, while earlier lows sit at 97.4–98.
- **Structure:** The trend is up, but the last push failed and gave back everything. Price is now testing the key 97–98 shelf.
- **Weight:** 0.45.
- **Change mind:** Holding above 104 would let me raise. Below 97 means flat.

### 51a50be1ab (AVAX)
- **Read:** A downtrend from 140 ended in a crash to 81–92, then a base at 85–93. The breakout reached 114, and since then price has ranged 96–112 with lower highs. It sits at 100, near the bottom of that range.
- **Structure:** The asset is weak relative to its own history and trades far below its earlier 125–140 levels. The range is still holding.
- **Weight:** 0.35.
- **Change mind:** I'd add above 109. Below 96 means flat.

### 81fc4a4166 (DOGE)
- **Read:** The earlier range was 110–140. It crashed and based at 84–89, broke out to a 122 wick, then made lower highs at 115 and 111. Price is at 100, sitting on the 98–100 support.
- **Structure:** This is a range with a bearish tilt. Old pre-crash support at 105–110 now acts as overhead resistance.
- **Weight:** 0.35.
- **Change mind:** I'd add above 110. Below 97 means flat.

### 8edeadbe51 (BTC)
- **Read:** This series is the market itself. A V-shaped breakout took it from the 82–85 base to 102–106, and it has held a 99–106 range for three weeks. It is now at the range low of 100, just under the old 100–107 distribution zone.
- **Structure:** The breakout is constructive and the base is retaken. Price is pinned at range support.
- **Weight:** 0.55.
- **Change mind:** I'd add above 106. Below 99 I'd cut to 0.25, and below 95 I'd go flat.

{"27533e9764 (DOT)": 0.25, "10b6ba32f8 (LTC)": 0.55, "0d37355410 (XRP)": 0.45, "3bf83627f1 (ADA)": 0.4, "9ebfc7d6b2 (ETH)": 0.7, "a9cd48fa50 (SOL)": 0.6, "ad89560147 (LINK)": 0.45, "51a50be1ab (AVAX)": 0.35, "81fc4a4166 (DOGE)": 0.35, "8edeadbe51 (BTC)": 0.55}

## Entscheidung 2026-09-20

**Strategy:** I go long when price is above its 1–2 month trend and holding higher lows, and the crypto market is also trending up. The market recovered from about 72 to 100 and is back near its 6‑month highs, so the regime is supportive. I size up for clean breakouts to new window highs, size down for wide volatile ranges, and cut for parabolic, climax‑volume moves.

### 2969257cc2 (DOT)
- **Read:** The asset fell from 120 to a 64–67 base, then broke out. It spiked to 113 at day -12 and faded to 83. It has rebuilt higher lows (83.3, then 89.8) and is now back at 100.
- **Key levels:** Resistance is 103–113. Support is 88–83.
- **Weight:** 0.6. The trend is up with market support, but it is still capped below the 113 spike high.
- **Change my mind:** a close below 88.

### 8df0f375bd (ADA)
- **Read:** The asset fell from 124 to 61, rallied to a 113 wick, and has ranged 84–100 for a month. It is now at the top of that range, with higher lows at 83.5 and 85.7.
- **Key levels:** Resistance is 102–113. Support is 85.
- **Weight:** 0.6.
- **Change my mind:** a close below 85.

### 8641f52898 (DOGE)
- **Read:** The asset fell from 135 to a flat 78–81 base, then broke out to 105–115. It has ranged 90–105 since, and 100 is mid‑to‑upper range. Its relative strength is weaker than its peers'.
- **Key levels:** Resistance is 105–109. Support is 90–92.
- **Weight:** 0.5.
- **Change my mind:** a close below 89.

### ac502a50b7 (BTC)
- **Read:** This series tracks the market itself. It has a steady uptrend from 72, holds higher lows at 92.4 and 93.2, and sits at 100 just under the 6‑month high of 101–102.
- **Volatility:** low.
- **Weight:** 0.7.
- **Change my mind:** a close below 92.

### 69f21ba63c (LTC)
- **Read:** The asset went from a 67 low to 100. It is pressing the top of a one‑month range (101.2), and the 6‑month high is 103. Its lows are rising (81.6, 86.4, 85.5).
- **Weight:** 0.65.
- **Change my mind:** a close below 86.

### 5d03acab4f (SOL)
- **Read:** The asset rose from a 54 low to 100, which is above every price in the window; the prior high was 88.5. It has the strongest structure here: it broke out, pulled back to 86–87, and broke out again.
- **Key levels:** Support is 86–89.
- **Weight:** 0.75.
- **Change my mind:** a close below 86.

### 7bd06b7772 (XRP)
- **Read:** The asset spiked to 120 on very heavy volume and has ranged 89–108 since, with whipsaws such as the drop from 106 to 89.7 at day -5. It is now at 100, mid‑range.
- **Weight:** 0.5. The trend is up, but the noise is high.
- **Change my mind:** a close below 89.

### 44d3e7cba3 (AVAX)
- **Read:** The asset went from 64 to 100 in two days on 4–6× volume. That breaks a 55–73 range that held for months, and it is above the 92.7 prior high. This is a parabolic climax, and pullback risk is high.
- **Weight:** 0.3. I keep a small position for the momentum but expect a retrace toward 83–90.
- **Change my mind:** holding above 90 for a week would make me add; a close below 83 would take me to flat.

### dfc43a05ef (ETH)
- **Read:** The asset went from a 57 low to a month‑long 89–97 consolidation and has now broken to 100. That is a new 180‑day high; the prior high was 93.2.
- **Key levels:** Support is 89–92.
- **Weight:** 0.75.
- **Change my mind:** a close below 89.

### 14dfa1aa42 (LINK)
- **Read:** The asset rose from a 56 low to a 109 spike, retraced to 85, and is now back at 100. That is well above the prior 6‑month high of 86.8. Its lows are rising.
- **Key levels:** Resistance is 106–109. Support is 85–87.
- **Weight:** 0.65.
- **Change my mind:** a close below 85.

{"2969257cc2 (DOT)": 0.6, "8df0f375bd (ADA)": 0.6, "8641f52898 (DOGE)": 0.5, "ac502a50b7 (BTC)": 0.7, "69f21ba63c (LTC)": 0.65, "5d03acab4f (SOL)": 0.75, "7bd06b7772 (XRP)": 0.5, "44d3e7cba3 (AVAX)": 0.3, "dfc43a05ef (ETH)": 0.75, "14dfa1aa42 (LINK)": 0.65}

## Entscheidung 2026-09-27

## Strategy
Follow the trend, using the market as a filter. The market has broken out to a new 180-day high at 100, above its earlier peak of 97.3. So I go long assets that sit above their earlier highs and keep making higher lows. I reduce the weight when an asset is pushing into heavy overhead resistance from before the crash, or when the move rests on a single vertical, volume-spike pump that has not yet been tested.

## 11cc451df9 (ADA)
- **Read:** Before the crash it traded 92–110. It crashed to about 55, and has now fully recovered to 100. That is stronger than the market.
- **Structure:** Higher lows at 74.6, then 91.5. Price is now at the bottom edge of the old 104–110 supply zone.
- **Weight:** 0.75. The trend is strong, but resistance overhead caps the size.
- **Change my mind:** A close below 91.

## dd78509e87 (DOT)
- **Read:** The old range was 95–110 and the low was about 57. A spike to 101 at day -19 collapsed to 74.5. Price then rebuilt to 100 on heavy volume.
- **Structure:** Higher lows at 74.5 and 85. It is volatile and has failed at this level once already.
- **Weight:** 0.65.
- **Change my mind:** A close below 85.

## 5c3f80f313 (ETH)
- **Read:** Price is above the earlier high of 91.7 from before the crash. It is consolidating tightly between 99 and 103 on fading volume, which looks like a clean base after the breakout.
- **Weight:** 0.9.
- **Change my mind:** A close below 96.5.

## 4c8e693357 (LTC)
- **Read:** The old high was 85. On day -3 it gapped up on 6.7x volume, from 86.8 to 100.9. It has held between 98.7 and 105 for three days. The trend is up, but it is extended and may be a blow-off.
- **Weight:** 0.7.
- **Change my mind:** A close below 96.5, which would mean it is giving back the gap.

## 22d635e3db (BTC)
- **Read:** This series tracks the market almost exactly. It is at a new high of 100 after breaking above 97.3. It is consolidating between 98 and 103.5 after the push on day -6.
- **Weight:** 0.9.
- **Change my mind:** A close below 95.7.

## 8906519e2a (DOGE)
- **Read:** Before the crash it traded 100–120, so price is now back at the bottom of that range. A spike to 109 on day -5 was rejected to 94.
- **Structure:** Higher lows at 80.8 and 94. There is heavy supply between 105 and 120.
- **Weight:** 0.55.
- **Change my mind:** A close below 94 to turn bearish. A close above 110 would raise the weight.

## 7147714b50 (XRP)
- **Read:** A blow-off wick to 112 came on day -36, followed by a choppy range of 83–110. Recent highs at 109.3 and 107.5 are lower, while lows at 82, 95.7 and 99 are rising, so price is compressing toward the low 100s.
- **Weight:** 0.6.
- **Change my mind:** A close below 95.5. A close above 110 would add.

## 67435a2db6 (SOL)
- **Read:** Price is far above the earlier high of 80.7 and is in a steady staircase uptrend. Higher lows at 78.5 and 92.2.
- **Weight:** 0.9.
- **Change my mind:** A close below 92.

## d7be8fd737 (LINK)
- **Read:** Price is far above the earlier high of 77.5 and at new highs of 101–103. Higher lows at 75.7 and 86, and day -2 was a strong breakout on volume.
- **Weight:** 0.85.
- **Change my mind:** A close below 93 for the near term. Below 86 the structure breaks.

## 91108d2062 (AVAX)
- **Read:** The asset was dead between 55 and 70 for about 100 days. It then made a single vertical pump on days -8 and -7, from 70 to 104 on 5.7x volume, and has since chopped between 91 and 108. There is no prior base at this level, and a pump like this has a high risk of retracing.
- **Weight:** 0.35.
- **Change my mind:** A close above 108 would add. A close below 91 means exit.

{"11cc451df9 (ADA)": 0.75, "dd78509e87 (DOT)": 0.65, "5c3f80f313 (ETH)": 0.9, "4c8e693357 (LTC)": 0.7, "22d635e3db (BTC)": 0.9, "8906519e2a (DOGE)": 0.55, "7147714b50 (XRP)": 0.6, "67435a2db6 (SOL)": 0.9, "d7be8fd737 (LINK)": 0.85, "91108d2062 (AVAX)": 0.35}
