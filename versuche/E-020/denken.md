# E-020: was die KI gedacht hat (Set A)

Volle Antwort des Deciders pro Entscheidungswoche, unverändert. Er sah weder Datum noch Coin-Namen; die Namen in Klammern sind erst danach eingesetzt. Gesendeter Prompt und Daten: runs/<set>/<woche>/requests.json.

## Entscheidung 2026-07-05

**Strategy:** The weekly regime sets direction. Every window sits under a falling long average after a big decline and a sharp break about a month ago. I start from a low base weight of 0.1 to 0.2. I add a little only where the short rebound looks orderly and has a higher-low structure. I never chase a single extreme week. Each flip price is the level whose close would change the regime read: usually a hold above the post-crash range high, or a loss of the most recent higher low.

## 18e32e3f34 (LINK)
- **Read:** Long downtrend from 175 to 100, with a crash from 113 to 88 around day -30. Since then it has ranged between 87 and 107.
- **Momentum:** 8-week −25%, 4-week +2%, 2-week +4%. The signs are mixed, so there is no trend state.
- **Levels:** Price is below a falling 100-day average of about 110. Last week's +12% bounce is a rally inside a downtrend.
- **Weight:** 0.2, because the regime is down and volatility is high.
- **Flip:** A close above 107, the post-crash range high.

## e180ea7ec3 (ETH)
- **Read:** Same shape: 135 down to 85, then a rebound to 100.
- **Momentum:** 8-week −25%, 4-week +14%, 2-week +5%. Long and short momentum conflict.
- **Levels:** The long average is falling. Resistance is at 103.6 (the day -20 high), then about 113.
- **Weight:** 0.2.
- **Flip:** A close above 104.

## 3f78d4b448 (DOGE)
- **Read:** Peaked at 148 at day -52, then made lower highs at 118 and 107.
- **Momentum:** 2-, 4- and 8-week returns are all negative (−5%, −5%, −31%), which is a downtrend state. Last week's bounce from 92 to 100 does not change the weekly line.
- **Weight:** 0.1.
- **Flip:** A close above 108, the day -17 to -20 area.

## 55ac4942e5 (BTC)
- **Read:** Fell from 129 to 93, then went sideways between 91 and 105.
- **Momentum:** 8-week −23%. The 4- and 2-week returns are flat. The regime is down and short-term direction is unclear.
- **Weight:** 0.2.
- **Flip:** A close above 106, the range top.

## ed0b5479a3 (DOT)
- **Read:** Steady lower highs from 157 to 119 to 115, now at 100.
- **Momentum:** 2-, 4- and 8-week returns are all negative (−6%, −10%, −36%), with high ATR%. This is the clearest down regime of the set.
- **Weight:** 0.1.
- **Flip:** A close above 112, which would reclaim the day -17 to -13 shelf.

## 76ff955e0b (SOL)
- **Read:** Crashed to 74 at day -29, then made higher lows at 79 and 86–88 and higher highs. Price has reclaimed the pre-crash range of 100–105.
- **Momentum:** 4-week +23% and 2-week +13% against 8-week −15%. That conflict points to a possible turning point.
- **Weight:** 0.35, a middle weight rather than an extreme one.
- **Flip:** A close below 88, which would break the latest higher low.

## 4eb7875f84 (ADA)
- **Read:** Fell from 149 to 73, then jumped 32% in the last week on high volume.
- **Momentum:** The last week alone is extreme (z > 2). Longer windows do not confirm it: 8-week is −33%, while 4-week is +15%. A single extreme week is more likely a counter-move than a trend, and volatility is very high.
- **Weight:** 0.2.
- **Flip:** A close above 106, meaning the breakout above 100–105 holds.

## 8a3d60d1fa (XRP)
- **Read:** Fell from 128 to 87, then rebounded to 100.
- **Momentum:** 8-week −21%. The 4- and 2-week returns are flat to +3%, which is mixed.
- **Levels:** Below a falling long average. Range high is about 107 on a close basis (112 at the wick).
- **Weight:** 0.2.
- **Flip:** A close above 107.

## 2f156c8c12 (LTC)
- **Read:** Fell from 132 to 86, then rebounded. Today's close of 100 is a marginal new post-crash closing high, and volatility is somewhat lower than in its peers.
- **Momentum:** 8-week −24%, 4-week +7%, 2-week +3%. The weekly line has not turned.
- **Weight:** 0.25.
- **Flip:** A close above 103, which would confirm the range breakout.

## 4a2f95d7d6 (AVAX)
- **Read:** Fell from 148 to 82 (at day -16), then rebounded to 100.
- **Momentum:** 8-week −32%, 4-week +2%, 2-week +13%. The signs are mixed.
- **Levels:** Resistance is at 102 to 104.
- **Weight:** 0.2.
- **Flip:** A close above 104.

{"18e32e3f34 (LINK)": {"weight": 0.2, "flip": 107.0}, "e180ea7ec3 (ETH)": {"weight": 0.2, "flip": 104.0}, "3f78d4b448 (DOGE)": {"weight": 0.1, "flip": 108.0}, "55ac4942e5 (BTC)": {"weight": 0.2, "flip": 106.0}, "ed0b5479a3 (DOT)": {"weight": 0.1, "flip": 112.0}, "76ff955e0b (SOL)": {"weight": 0.35, "flip": 88.0}, "4eb7875f84 (ADA)": {"weight": 0.2, "flip": 106.0}, "8a3d60d1fa (XRP)": {"weight": 0.2, "flip": 107.0}, "2f156c8c12 (LTC)": {"weight": 0.25, "flip": 103.0}, "4a2f95d7d6 (AVAX)": {"weight": 0.2, "flip": 104.0}}

## Entscheidung 2026-07-12

**Strategy:** Weekly-level regime decides direction. I change a weight only on a confirmed change of state: a held breakout, a trend break, or a regime shift. Each window has a weight and flip price from last week, so I first check whether any close since then has crossed the flip price. If none has, the weight stays as it is: no change, no cost.

**86f19d3b0d (XRP)**
- **Read:** Long downtrend from about 200 to the mid-120s, then a sideways range, then a breakdown at day −40 to a low of about 96.
- **Recent action:** A rebound stalled at 106.6 and price drifted back to 100. The falling longer averages sit above price, around 115–125, and act as resistance. Momentum over 2, 4 and 8 weeks is mixed to negative.
- **Flip check:** The highest close last week was 106.6, below the 114.0 flip, so it was not broken.
- **Weight:** Keep 0.20.
- **Change my mind:** A close above 114.0, which would reclaim the pre-breakdown base and the day −27 spike high.

**5b0e9b3fd0 (LINK)**
- **Read:** Downtrend, a range around 105–135, then a breakdown from about 113 to 89. The rebound since has stalled at roughly 100–102. The lower highs are intact.
- **Flip check:** Highest close was 100.8, below 107.9. Not broken.
- **Weight:** Keep 0.20.
- **Change my mind:** A close above 107.9, back above the day −27 high and into the old range.

**b1da19334f (DOGE)**
- **Read:** The rally to about 159 failed, followed by a sharp breakdown below 125 and a drift lower to about 96–100.
- **Structure:** Lower highs at 122 and 107, with the long averages falling well above price. Bear regime.
- **Flip check:** Highest close was 107.1, below 115.6. Not broken.
- **Weight:** Keep 0.10.
- **Change my mind:** A close above 115.6.

**17f853ed41 (BTC)**
- **Read:** A slow grind up to about 128, then a breakdown at day −40 to 92–95. The recovery is choppy and has stalled at about 100–104.
- **Context:** The 50- and 100-day averages are falling above price.
- **Flip check:** Highest close was 100.6, below 105.8. Not broken.
- **Weight:** Keep 0.20.
- **Change my mind:** A close above 105.8, which would reclaim the day −27 high and confirm a higher high.

**c60f8469aa (SOL)**
- **Read:** Broke down to a low of about 81, then the strongest rebound in the set, with higher lows at 83 and 88 and a high of 107.
- **Recent action:** A pullback to 100, still above the 88–93 higher-low zone. The longer trend is still down, and the shorter structure is turning up. Conflicting timeframes argue for a middle weight.
- **Flip check:** Lowest close was 99.8, above 93.3. Not broken.
- **Weight:** Keep 0.35.
- **Change my mind:** A close below 93.3, which would break the higher-low structure.

**967c5fe78c (ETH)**
- **Read:** A range around 110–130 broke down to about 84–87. The rebound reached about 99.6 and then flattened.
- **Context:** Price is still below the falling averages and below the day −27 high of 99.4–102.
- **Flip check:** Highest close was 99.6, below 102.8. Not broken.
- **Weight:** Keep 0.20.
- **Change my mind:** A close above 102.8.

**5d912fac7d (AVAX)**
- **Read:** A range around 140–160 broke down to a low of 92. The rebound is volatile and peaked at 108.8. Price is now back at 100 after a weak close.
- **Volatility:** Elevated, including large wide-range days around day −23.
- **Flip check:** Highest close was 108.2, below 112.4. Not broken.
- **Weight:** Keep 0.20.
- **Change my mind:** A close above 112.4.

**104da6120c (DOT)**
- **Read:** A long downtrend from about 270, with the spike rallies at days −137 and −118 failing. Breakdown below 137, then lower highs at 120 and 105.
- **Context:** Price is near the lows at about 96–100. Clear bear regime.
- **Flip check:** Highest close was 104.9, below 116.9. Not broken.
- **Weight:** Keep 0.10.
- **Change my mind:** A close above 116.9.

**5ff33ed665 (ADA)**
- **Read:** A crash to about 89, then a spike to 118.6 at day −8 that fully reversed back to 100. The spike was a single extreme week with no confirmation from the longer windows, so it was a failed move.
- **Context:** Volatility is high and the longer trend is down.
- **Flip check:** Highest close since last week was 116.9, below 123.9. Not broken.
- **Weight:** Keep 0.20.
- **Change my mind:** A close above 123.9.

**4628670781 (LTC)**
- **Read:** A tight range around 118–135 broke down to about 89–94. The recovery shows a higher low at 93 and stalls around 104. It is quieter than its peers.
- **Context:** The longer averages are still falling above price.
- **Flip check:** Highest close was 104.1, below 107.2. Not broken.
- **Weight:** Keep 0.25.
- **Change my mind:** A close above 107.2.

{"86f19d3b0d (XRP)": {"weight": 0.2, "flip": 114.0}, "5b0e9b3fd0 (LINK)": {"weight": 0.2, "flip": 107.9}, "b1da19334f (DOGE)": {"weight": 0.1, "flip": 115.6}, "17f853ed41 (BTC)": {"weight": 0.2, "flip": 105.8}, "c60f8469aa (SOL)": {"weight": 0.35, "flip": 93.3}, "967c5fe78c (ETH)": {"weight": 0.2, "flip": 102.8}, "5d912fac7d (AVAX)": {"weight": 0.2, "flip": 112.4}, "104da6120c (DOT)": {"weight": 0.1, "flip": 116.9}, "5ff33ed665 (ADA)": {"weight": 0.2, "flip": 123.9}, "4628670781 (LTC)": {"weight": 0.25, "flip": 107.2}}

## Entscheidung 2026-07-19

**Strategy:** I keep last week's weight unless a daily close since then has broken the flip price. When a flip is broken, I set a new weight from the weekly regime: the sign agreement of 2-, 4- and 8-week momentum, the slope of the long average, and swing structure. Volatility sets the size, I only close part of any gap, and changes under about 0.15 aren't worth the cost.

## f5b4723db8 (DOT)
- **Read:** Long downtrend from about 238 to 100, with a falling long average.
- **Recent action:** The price has drifted sideways between 99 and 108 for four weeks. The flip at 120.3 was not broken; recent closes were 100–104.
- **Weight:** Hold 0.10.
- **Change my mind:** A close above 120.3, which reclaims the October breakdown zone.

## 89a99081fa (XRP)
- **Read:** Downtrend, now in a 92–106 range since day −44.
- **Recent action:** No close near the flip at 112.8.
- **Weight:** Hold 0.20.
- **Change my mind:** Close above 112.8.

## 5f5f5c3228 (ADA)
- **Read:** Crash to about 86, then a spike to 120 that faded back to 95–100.
- **Recent action:** That failed breakout means no regime change. The flip at 120.8 is untouched.
- **Weight:** Hold 0.20.
- **Change my mind:** Close above 120.8.

## 6036ba844a (BTC)
- **Read:** Downtrend from 127 to 90, with a slow recovery to 100.
- **Recent action:** The highest close was 100.5, below the flip at 104.3.
- **Weight:** Hold 0.20.
- **Change my mind:** Close above 104.3.

## 875fcd6649 (ETH)
- **Flip broken:** Closes of 101.0 and 102.4 on days −5 and −4 broke the flip at 99.2, so I set a new weight.
- **Momentum:** 2-week is about +5% and 4-week about +10%, but 8-week is about −11% and the long average is still falling.
- **Structure:** Higher low at 81.9 (versus 80.4) and a higher high at 104 (above 98.8).
- **Read:** A possible turn, but still a rebound inside a downtrend.
- **Weight:** Raise in one step to 0.35, which is a mid weight rather than a full one.
- **Change my mind:** A close below 92 would undo the higher-low structure.

## 64ca6d696c (LTC)
- **Read:** Recovery from 87 to 100.
- **Recent action:** The highest close was 99.9–100.0, which does not break the flip at 100.2.
- **Weight:** Hold 0.25.
- **Change my mind:** Close above 100.2.

## f2fc744857 (LINK)
- **Read:** Range of 86–102 after a decline.
- **Recent action:** The highest close was 101.8, below the flip at 102.9.
- **Weight:** Hold 0.20.
- **Change my mind:** Close above 102.9.

## d02f20afd1 (SOL)
- **Read:** Rebound from 81 to 108, now pulling back to about 98–100.
- **Recent action:** The lowest close was 98.2, above the downside flip at 94.0.
- **Weight:** Hold 0.35.
- **Change my mind:** Close below 94.0.

## 41ad3a6a59 (AVAX)
- **Read:** Downtrend, now in a choppy 91–108 range.
- **Recent action:** No close near the flip at 111.4.
- **Weight:** Hold 0.20.
- **Change my mind:** Close above 111.4.

## 868dff08cf (DOGE)
- **Read:** Rolled over from 163 to 100, with the long average turning down.
- **Recent action:** Flat at 99–103, with no close near the flip at 116.1.
- **Weight:** Hold 0.10.
- **Change my mind:** Close above 116.1.

{"f5b4723db8 (DOT)": {"weight": 0.10, "flip": 120.3}, "89a99081fa (XRP)": {"weight": 0.20, "flip": 112.8}, "5f5f5c3228 (ADA)": {"weight": 0.20, "flip": 120.8}, "6036ba844a (BTC)": {"weight": 0.20, "flip": 104.3}, "875fcd6649 (ETH)": {"weight": 0.35, "flip": 92.0}, "64ca6d696c (LTC)": {"weight": 0.25, "flip": 100.2}, "f2fc744857 (LINK)": {"weight": 0.20, "flip": 102.9}, "d02f20afd1 (SOL)": {"weight": 0.35, "flip": 94.0}, "41ad3a6a59 (AVAX)": {"weight": 0.20, "flip": 111.4}, "868dff08cf (DOGE)": {"weight": 0.10, "flip": 116.1}}

## Entscheidung 2026-07-26

**Strategy.** I keep last week's weight unless a close since then has broken the flip price. If it has, I set a new weight from the weekly regime: 2-, 4- and 8-week momentum, the position of price relative to the falling long averages, and confirmed structure breaks. A rebound inside a falling long trend gets only a stepwise increase toward a middle weight, never a jump to full. Range position, single days and indicator levels are not signals, and I ignore changes under about 0.15.

## e76753751b (AVAX)
- **Read:** Price crashed from about 133 to 87 (days -54 to -37) and has since moved sideways between 92 and 104. The long averages are falling and sit well above price. Momentum is mixed: 8-week negative, 2-week flat. Day -1 was a +7.6 % bar, but it is a single day and doesn't change the weekly picture.
- **Flip check:** Highest close since last week is 100.5, below the 106.8 flip. Not broken.
- **Weight:** Keep 0.20.
- **Flip:** 106.8.

## d27e72be90 (XRP)
- **Read:** Bear regime after the drop from about 120 to 94. The range since then is roughly 91–106, with highs at 104–106 capping price. Closes have stayed below the falling 100–200-day averages.
- **Flip check:** Highest close since last week is 102.7, below 111.2. Not broken.
- **Weight:** Keep 0.20.
- **Flip:** 111.2.

## b652d23ea2 (LTC)
- **Read:** After the crash to 85.5 (day -31), the structure has turned to higher lows (85.5, 91.1, 96.9) and higher highs (95.8, 98.3, 100.0).
  - Momentum: 2-week +8.7 %, 4-week +12 % (z about 1.2), 8-week about -8 %.
  - This is a rebound within a falling long trend; the 110–118 zone is falling resistance.
- **Flip check:** Closes of 99.0 and 100.0 broke the 98.6 flip, so I decide a new weight.
- **Weight:** Raise one step, 0.25 → 0.40. Short momentum and structure agree, but the long trend is still down, so a middle weight rather than full.
- **Flip:** 95.0. A close back below the old 96–97 ceiling would mean the breakout failed.

## f00cebad2e (DOT)
- **Read:** Steep downtrend from about 160 to 98, now drifting sideways between 97 and 107. Long averages are falling far above price.
- **Flip check:** Highest close since last week is 102.3, below 119.1. Not broken.
- **Weight:** Keep 0.10.
- **Flip:** 119.1.

## c38f1b705a (ETH)
- **Read:** Recovery from 80 to 100 with higher lows, but price is still below the falling long average near 105–110.
- **Flip check:** Lowest close since last week is 95.2, above the 88.1 flip. Not broken.
- **Weight:** Keep 0.35.
- **Flip:** 88.1.

## e060e686a7 (SOL)
- **Read:** Rebound from 81 to the 100–107 zone, followed by consolidation. The 8-week trend is still negative.
- **Flip check:** Lowest close since last week is 96.4, above the 93.5 flip. Not broken.
- **Weight:** Keep 0.35.
- **Flip:** 93.5.

## 80408ae80e (DOGE)
- **Read:** Downtrend from about 150 to 94–106. The range is sideways and the long averages are falling.
- **Flip check:** Highest close since last week is 100.0, below 114.6. Not broken.
- **Weight:** Keep 0.10.
- **Flip:** 114.6.

## 332f83e534 (BTC)
- **Read:** Fall from about 118 to 89, then a slow recovery to a 96–102 range. Long averages are falling above price.
- **Flip check:** Highest close since last week is 101.8, below 103.2. Not broken.
- **Weight:** Keep 0.20.
- **Flip:** 103.2.

## f85784449c (LINK)
- **Read:** Lows at 81.6–82.1 (days -31 and -26), followed by higher lows at 86.6 and 94.0. Today's close of 100 is above the range ceiling around 97.5–97.8, by about 0.7 ATR, though on low volume.
  - Momentum: 4-week +21 %, 2-week +10 %, 8-week about -4 %.
  - The long average is flattening around 100–105.
- **Flip check:** Closes of 98.1 and 100.0 broke the 97.8 flip, so I decide a new weight.
- **Weight:** Raise one step, 0.20 → 0.40. The breakout is not yet confirmed by a weekly hold and the long trend is not up, so this is a partial move only.
- **Flip:** 95.0. A close back inside the range would mean the breakout failed.

## 66092d374b (ADA)
- **Read:** Crash from about 140 to 87. A spike to 116 (day -22) faded back to about 100. The structure is mixed and long averages are falling well above price.
- **Flip check:** Highest close since last week is 105.1, below 121.0. Not broken.
- **Weight:** Keep 0.20.
- **Flip:** 121.0.

{"e76753751b (AVAX)": {"weight": 0.20, "flip": 106.8}, "d27e72be90 (XRP)": {"weight": 0.20, "flip": 111.2}, "b652d23ea2 (LTC)": {"weight": 0.40, "flip": 95.0}, "f00cebad2e (DOT)": {"weight": 0.10, "flip": 119.1}, "c38f1b705a (ETH)": {"weight": 0.35, "flip": 88.1}, "e060e686a7 (SOL)": {"weight": 0.35, "flip": 93.5}, "80408ae80e (DOGE)": {"weight": 0.10, "flip": 114.6}, "332f83e534 (BTC)": {"weight": 0.20, "flip": 103.2}, "f85784449c (LINK)": {"weight": 0.40, "flip": 95.0}, "66092d374b (ADA)": {"weight": 0.20, "flip": 121.0}}

## Entscheidung 2026-08-02

## Strategy

Last week's weight stays in place unless a daily close has crossed the flip price since the last decision (days −7 to 0). If it has, I set a new weight from the weekly regime. A price below a falling long average with turning short momentum gets a reduced weight. A sideways range keeps the weight unchanged. Changes smaller than about 0.15 are not worth the cost.

## ecf8291b98 (LTC)
- **Flip check:** Last week's flip was 101.7, below the close of 107.0 at the time. The day −2 close of 99.1 broke it, so I decide again.
- **Trend:** The window fell from about 125 to 88 (days −61 to −38) and recovered to about 107. The long average sits around 115 and is falling, with price below it.
- **Momentum:** 8-week momentum is positive, but 2- and 4-week momentum is negative. Lower highs since 108 point to a weakening rebound inside a downtrend.
- **Key levels:** support 97.5, resistance 107–108.
- **Weight:** 0.25 (down from 0.40), damage control in a downtrend with a failed rebound.
- **Flip:** a close above 108.0, which would mean a new rebound high.

## b40c36c88d (AVAX)
- **Flip check:** Last week's flip was 109.9 and the highest close since was 102.9, so it is not broken.
- **Trend:** Price is in a sideways range of 94–106 below a falling long average.
- **Weight:** 0.20 kept. **Flip:** 109.9.

## 789f6b4c5a (LINK)
- **Flip check:** Last week's flip was 100.0, below the close of 105.3 at the time. The day −4 close of 99.4 broke it, so I decide again.
- **Trend:** The window fell from about 110 to 84, then recovered to a range of 94–105. Price is still below a falling long average (about 108).
- **Momentum:** The 2-week return is flat and the last spike to 105.3 failed immediately. I treat this the same as ecf8291b98 (LTC).
- **Weight:** 0.25 (down from 0.40).
- **Flip:** a close above 106.5, which would clear the day −6 high.

## cdba25429e (ETH)
- **Flip check:** Last week's flip was 91.3 and the lowest close since was 97.9, so it is not broken.
- **Trend:** Price recovered from 80 to a range of 97–104.
- **Weight:** 0.35 kept. **Flip:** 91.3.

## b0ddeee95a (XRP)
- **Flip check:** Last week's flip was 113.9 and the highest close since was 102.4, so it is not broken.
- **Trend:** Price is in a range of 96–106, below a falling long average.
- **Weight:** 0.20 kept. **Flip:** 113.9.

## d9f75281a2 (ADA)
- **Flip check:** Last week's flip was 106.0 and today's close of 100.0 is the highest since, so it is not broken.
- **Trend:** Today's +8.7% day is a single extreme day, which on its own is not a signal. The downtrend is still intact below a long average of about 125.
- **Weight:** 0.20 kept. **Flip:** 106.0.

## cc7ab2fe89 (SOL)
- **Flip check:** Last week's flip was 97.5 and the lowest close since was 97.7, so it is not broken, though only narrowly.
- **Trend:** Price has been sideways between 98 and 106 after rising from 84.
- **Weight:** 0.35 kept. **Flip:** 97.5.

## 290af0f6b4 (DOT)
- **Flip check:** Last week's flip was 123.4 and the highest close since was 103.6, so it is not broken.
- **Trend:** This is a persistent downtrend from about 190 to 95.
- **Weight:** 0.10 kept. **Flip:** 123.4.

## 15406009e9 (BTC)
- **Flip check:** Last week's flip was 106.2 and the highest close since was 102.9, so it is not broken.
- **Trend:** Price is sideways between 98 and 105, below a falling long average.
- **Weight:** 0.20 kept. **Flip:** 106.2.

## 052827be0a (DOGE)
- **Flip check:** Last week's flip was 118.8 and the highest close since was 103.6, so it is not broken.
- **Trend:** This is a downtrend from about 160 to 100.
- **Weight:** 0.10 kept. **Flip:** 118.8.

{"ecf8291b98 (LTC)": {"weight": 0.25, "flip": 108.0}, "b40c36c88d (AVAX)": {"weight": 0.20, "flip": 109.9}, "789f6b4c5a (LINK)": {"weight": 0.25, "flip": 106.5}, "cdba25429e (ETH)": {"weight": 0.35, "flip": 91.3}, "b0ddeee95a (XRP)": {"weight": 0.20, "flip": 113.9}, "d9f75281a2 (ADA)": {"weight": 0.20, "flip": 106.0}, "cc7ab2fe89 (SOL)": {"weight": 0.35, "flip": 97.5}, "290af0f6b4 (DOT)": {"weight": 0.10, "flip": 123.4}, "15406009e9 (BTC)": {"weight": 0.20, "flip": 106.2}, "052827be0a (DOGE)": {"weight": 0.10, "flip": 118.8}}

## Entscheidung 2026-08-09

**Strategy:** The weekly regime decides direction and volatility decides size. I keep last week's weight unless a close has crossed last week's flip price. If it has, I re-decide using the weekly trend, the 2/4/8-week momentum agreement and the long-average regime. I change the weight only when the move is at least 0.15, and close only part of the gap.

## 1e038b7ce8 (XRP)
- **Market:** Long-term downtrend. Price fell from about 130–140 to a low near 98 (day -45). Since then it has moved sideways between about 99 and 112, and the last closes are at 99–101. Resistance is near 112 and 120. Momentum is negative or flat.
- **Flip check:** No close above 120.2 since last week.
- **Weight:** Hold 0.20.
- **Change my mind:** A close above 120.2.

## a63217f2bb (DOGE)
- **Market:** The breakdown from about 145 gave a downtrend. Over the last 6 weeks price has been in a flat range of about 98–107 under a falling long average.
- **Flip check:** The flip price of 121.3 was not reached.
- **Weight:** Hold 0.10.
- **Change my mind:** A close above 121.3.

## c1fb33141b (AVAX)
- **Market:** Price crashed from about 140 to a low near 88.5 (day -51). It has since moved sideways between about 96 and 108, so the trend is unclear and the efficiency ratio is low. The highest close last week was 104.2.
- **Flip check:** The flip price of 112.2 was not reached.
- **Weight:** Hold 0.20.
- **Change my mind:** A close above 112.2.

## 9c43217eb0 (DOT)
- **Market:** A long decline ran from about 170 to 93. Last week's rebound to 107 faded back to 100. The long average is falling.
- **Flip check:** Closes stayed far below 123.4.
- **Weight:** Hold 0.10.
- **Change my mind:** A close above 123.4.

## a43479c515 (SOL)
- **Market:** After the crash to about 80, price recovered to about 108 and is now ranging between 94 and 102. The latest close is 100, near the range middle.
- **Flip check:** The lowest close last week was 95.3, so the 94.1 flip was not broken.
- **Weight:** Hold 0.35.
- **Change my mind:** A close below 94.1.

## f2a8bd8ea2 (ADA)
- **Flip check:** The day -3 close of 103.4 crossed the 103.3 flip, so I re-decide this window.
- **Market:**
  - The asset is in a deep downtrend from about 150 to a 71 low at day -45, with the long averages falling well above price.
  - The structure has improved. The swing low at 79–80 (day -13) is higher than the 71 low. Closes have moved above the day -36 swing high of 98.8, reaching 102.6–103.4.
  - 2-, 4- and 8-week returns are all positive: about +17%, +20% and +6%.
  - This is a rebound inside a falling long-term regime, and volatility is elevated.
- **Weight:** 0.35. The rules say to raise weight only in steps here, not to jump.
- **Change my mind:** A close back below 93, which would mean the breakout above about 99 failed.

## f25b0fe1c1 (ETH)
- **Market:** A slow recovery from 79 to about 100, with higher lows (82 → 91 → 96). Price sits under a long average that is flattening.
- **Flip check:** No close below 90.1.
- **Weight:** Hold 0.35.
- **Change my mind:** A close below 90.1.

## ec5a5af8ed (LINK)
- **Market:** Price recovered from 85 to about 100–105 and has been moving sideways near 100 for 3 weeks. The long-term trend is neutral to down.
- **Flip check:** The flip price of 109.1 was not reached.
- **Weight:** Hold 0.25.
- **Change my mind:** A close above 109.1.

## 3f8e338834 (LTC)
- **Market:** Price recovered from 86 to about 105, then pulled back to a 97–101 range. The 6-month trend is still down.
- **Flip check:** The flip price of 106.2 was not reached.
- **Weight:** Hold 0.25.
- **Change my mind:** A close above 106.2.

## cc96f8629b (BTC)
- **Market:** A tight range of about 96–102 after the recovery from 89. Volatility is compressed and there is no direction.
- **Flip check:** The flip price of 104.0 was not reached.
- **Weight:** Hold 0.20.
- **Change my mind:** A close above 104.0.

{"1e038b7ce8 (XRP)": {"weight": 0.20, "flip": 120.2}, "a63217f2bb (DOGE)": {"weight": 0.10, "flip": 121.3}, "c1fb33141b (AVAX)": {"weight": 0.20, "flip": 112.2}, "9c43217eb0 (DOT)": {"weight": 0.10, "flip": 123.4}, "a43479c515 (SOL)": {"weight": 0.35, "flip": 94.1}, "f2a8bd8ea2 (ADA)": {"weight": 0.35, "flip": 93.0}, "f25b0fe1c1 (ETH)": {"weight": 0.35, "flip": 90.1}, "ec5a5af8ed (LINK)": {"weight": 0.25, "flip": 109.1}, "3f8e338834 (LTC)": {"weight": 0.25, "flip": 106.2}, "cc96f8629b (BTC)": {"weight": 0.20, "flip": 104.0}}

## Entscheidung 2026-08-16

**Strategy:** I keep last week's weight unless a close since then has crossed the flip price. Only then do I re-decide, using the weekly state: whether 2-, 4- and 8-week momentum agree in sign, the slope of the long average, and the volatility regime. Position in the range, single days and indicator distances do not change the weight; high volatility caps the size.

## 1783df9ac5 (LINK)
- **Flip check:** 95.1 was crossed upward (95.5 at day −2, then 100.9), so I decide again.
- **Trend:** After the crash at day −72 (to about 78) the asset based around 77–80. It has since made higher lows (about 84 → 85 → 87).
- **Momentum:** The 2-, 4- and 8-week returns are all positive (about +12 %, +12 % and +20 %). |z_4W| is about 1, so this is a trend state.
- **Breakout:** The close is above the 60-day closing high of about 94 and above the long, flattening average of roughly 93–95.
- **Caveat:** Day −1 alone was +5.6 %, but the longer windows confirm the move.
- **Weight:** 0.55. That is a partial step, not all the way, because the breakout still has to hold.
- **Flip:** 91.5, a close back below the breakout zone.

## c7cf6f4dd3 (DOT)
- **Flip check:** Not broken; closes are around 100–106, far below 129.9.
- **Market:** A persistent downtrend from about 200, with a falling long average.
- **Weight:** 0.10, flip 129.9.

## 1de1ec2609 (LTC)
- **Flip check:** Not broken; closes are 99–103, below 109.3.
- **Market:** Sideways at 99–108 below a falling long average.
- **Weight:** 0.25, flip 109.3.

## e1e13f7459 (AVAX)
- **Flip check:** Not broken; closes are around 100–102, below 113.8.
- **Market:** A range of 97–110 after the crash, with no trend.
- **Weight:** 0.20, flip 113.8.

## 4e3947b64d (SOL)
- **Flip check:** Not broken; closes are 100–102, above 96.2.
- **Market:** A flat consolidation at 97–105.
- **Weight:** 0.35, flip 96.2.

## 223d6d4f5c (ADA)
- **Flip check:** 103.4 was broken downward (103.0 at day −2, then 100.0), so I decide again.
- **Swings:** Very choppy: 82 → 110 → 89 → 115 → 100.
- **Momentum:** Mixed. The 2-week return is about −8 %, while the 4- and 8-week returns are positive (+5 % and +12 %). That is no trend state.
- **Long trend:** Down from about 160; price is below a falling long average, and volatility is high.
- **Weight:** 0.20, a reduction because of the downtrend regime and high volatility.
- **Flip:** 115.5, a close above the recent swing high.

## d304cea23c (DOGE)
- **Flip check:** Not broken; closes are around 100, below 120.9.
- **Market:** A tight range at 99–105 after the downtrend.
- **Weight:** 0.10, flip 120.9.

## b4a6c9c485 (ETH)
- **Flip check:** Not broken; closes are around 100, above 91.8.
- **Market:** Sideways at 98–104 after the recovery.
- **Weight:** 0.35, flip 91.8.

## bdd956ef65 (BTC)
- **Flip check:** Not broken; closes are 100–103, below 107.3.
- **Market:** A flat range of 99–106.
- **Weight:** 0.20, flip 107.3.

## 3abf4aa589 (XRP)
- **Flip check:** Not broken; closes are around 100–104, below 124.6.
- **Market:** A slow downtrend, drifting lower from 116.
- **Weight:** 0.20, flip 124.6.

{"1783df9ac5 (LINK)": {"weight": 0.55, "flip": 91.5}, "c7cf6f4dd3 (DOT)": {"weight": 0.10, "flip": 129.9}, "1de1ec2609 (LTC)": {"weight": 0.25, "flip": 109.3}, "e1e13f7459 (AVAX)": {"weight": 0.20, "flip": 113.8}, "4e3947b64d (SOL)": {"weight": 0.35, "flip": 96.2}, "223d6d4f5c (ADA)": {"weight": 0.20, "flip": 115.5}, "d304cea23c (DOGE)": {"weight": 0.10, "flip": 120.9}, "b4a6c9c485 (ETH)": {"weight": 0.35, "flip": 91.8}, "bdd956ef65 (BTC)": {"weight": 0.20, "flip": 107.3}, "3abf4aa589 (XRP)": {"weight": 0.20, "flip": 124.6}}

## Entscheidung 2026-08-23

## Strategy

Weight follows the weekly trend state and is sized down when volatility is high. I don't chase a single extreme week. Last week's weight stays unless the close has broken last week's flip price. When it has broken, a breakout above a multi-month range with confirmed 2-, 4- and 8-week momentum justifies a moderate increase. That increase is capped because every window shows the same pattern: a one-week spike on 2–6× volume, a long upper wick on day -1, and σ20/σ90 far above 1.5. That pattern points to a possible counter-move. New flip prices sit where the breakout would fail, which is a close back inside the old range.

## 90c98cbb97 (LTC)
- **Flip check:** The close broke 92.3 on day -2, so I decide anew.
- **Trend:** The window drifted down from about 108 to a 75–92 range. Last week it rallied from 85 to 100 with a wick to 106.1.
- **Breakout:** The close is above the 60-day high (about 92) and above a flattening 100-day average (about 89).
- **Momentum:** 2-, 4- and 8-week returns are all positive, but they come mostly from one week.
- **Volatility:** It is spiking.
- **Weight:** 0.40, which is a partial step up.
- **Flip:** A close below 91 means the breakout failed.

## 221141c561 (DOGE)
- **Flip check:** The close broke 90.1, so I decide anew.
- **Trend:** It fell from 123 to a flat 73–79 base lasting about 40 days. It then jumped 33% to 100, with a wick to 107.9.
- **Averages:** The long average (about 88) is still falling. Price is above it, but this is the first week there.
- **Volatility:** It is extreme.
- **Weight:** 0.30.
- **Flip:** A close below 88 sends it back toward the base.

## 60a04e9366 (BTC)
- **Flip check:** The close broke 86.8, so I decide anew.
- **Range:** After the crash from about 95, it held a 75–86 range.
- **Breakout:** It broke above 86 and closed at 100, holding near the highs with a smaller wick than the other windows.
- **Context:** Price is above the 100-day average (about 87), and momentum is positive across all windows.
- **Weight:** 0.40.
- **Flip:** 90.

## 8068bf2a1d (XRP)
- **Flip check:** The close broke 81.4, so I decide anew.
- **Trend:** A long downtrend ran from 95 to 65.
- **Spike:** Price went from 66 to 100 in four days (+52%) on 6× volume, with a blow-off wick to 111.8. This is the most extreme single week of all the windows, with the highest reversal risk and the highest volatility.
- **Weight:** 0.30.
- **Flip:** A close below 84 puts it back under day -3's level and means the breakout failed.

## 471e0073b7 (SOL)
- **Flip check:** The flip at 75.2 is below the price and was never broken, so I keep 0.35.
- **Breakout:** Price is above the 78–83 range.
- **Weight:** 0.35, unchanged.
- **Flip:** A close below 84 means the breakout failed and I would reduce.

## 1f78c2f593 (LINK)
- **Flip check:** The flip at 74.4 was not broken, so I keep 0.55.
- **Structure:** Higher lows (61, then 68, then 70) were already in place before the spike, so the uptrend structure is intact.
- **Weight:** 0.55, unchanged.
- **Flip:** A close below 82 puts it back in the prior range.

## 091705fde5 (DOT)
- **Flip check:** The close never exceeded 106.2, so I keep 0.10.
- **Trend:** This is a long-term downtrend from about 180, and price is still below the falling long averages.
- **Resistance:** The swing highs at 108–109 are resistance.
- **Weight:** 0.10, unchanged.
- **Flip:** 106.2.

## 7c1cc32516 (ADA)
- **Flip check:** The close broke 89.0, so I decide anew.
- **Structure:** Lows are rising (61, then 67.5, then 75.4) and highs are rising (88, then 93, then 113.8 intraday), so a higher-high/higher-low structure is forming.
- **Context:** Price is above the 100-day average (about 82). Volatility is very high and there is a large wick.
- **Weight:** 0.40.
- **Flip:** A close below 86 puts it back under the prior high.

## af4c8f5dc7 (AVAX)
- **Flip check:** The close broke 94.7, so I decide anew.
- **Trend:** It crashed from 118 into an 80–92 range. Last week it broke out to 103, with a wick to 109.
- **Averages:** The 100-day average (about 93) is still falling.
- **Weight:** 0.35.
- **Flip:** 91.

## 037131fb10 (ETH)
- **Flip check:** The flip at 69.9 was not broken, so I keep 0.35.
- **Breakout:** Price broke above the 74–80 range.
- **Weight:** 0.35, unchanged.
- **Flip:** A close below 86 means the breakout failed.

{"90c98cbb97 (LTC)": {"weight": 0.4, "flip": 91.0}, "221141c561 (DOGE)": {"weight": 0.3, "flip": 88.0}, "60a04e9366 (BTC)": {"weight": 0.4, "flip": 90.0}, "8068bf2a1d (XRP)": {"weight": 0.3, "flip": 84.0}, "471e0073b7 (SOL)": {"weight": 0.35, "flip": 84.0}, "1f78c2f593 (LINK)": {"weight": 0.55, "flip": 82.0}, "091705fde5 (DOT)": {"weight": 0.1, "flip": 106.2}, "7c1cc32516 (ADA)": {"weight": 0.4, "flip": 86.0}, "af4c8f5dc7 (AVAX)": {"weight": 0.35, "flip": 91.0}, "037131fb10 (ETH)": {"weight": 0.35, "flip": 86.0}}

## Entscheidung 2026-08-30

**Strategy:** Last week's weight stays unless a daily close has crossed last week's flip price since then. When a flip is broken, I decide a new weight using the weekly trend, retracement of the recent swing, and volatility. I only change the weight if the move is at least about 0.15, and I set a new flip at a level that would mean a real change of state.

All ten windows show the same pattern: a long decline, then a sharp breakout spike about 9–11 days ago, now fading back toward 100.

## e5a7949f1a (BTC)
- **Market:** The breakout from the 81–83 range to about 101 has held at 100–104 for a week. Since day −7, the lowest close is 100.0, well above the flip at 90.1.
- **Weight:** Keep 0.40.
- **Flip:** 90.1. A close below it means the breakout failed back into the old range.

## 2f9279bb40 (XRP)
- **Market:** The spike from 74 to 125 (intraday) is fading, with closes moving 112 → 100. Volatility is very high. The flip at 94.1 has not been touched.
- **Weight:** Keep 0.30.
- **Flip:** 94.1.

## 23ae11b090 (ADA)
- **Market:** The longer trend is down, from about 143 to a low near 75.
  - The spike from 90.6 to 118.9 has retraced about two thirds, and today's close of 100.0 is below the flip at 101.3, so the flip is broken.
  - The 4- and 8-week returns are only about +2%, while volatility after the spike is high.
  - The breakout looks like it is failing.
- **Weight:** Reduce from 0.40 to 0.25.
- **Flip:** 111.0. Closes back above the post-spike range of about 110–111 would mean the breakout is holding again.

## 907bbf7257 (LINK)
- **Market:** A step-up from the 73–75 base through 85 to about 100–107, with a series of higher lows. The lowest close is 100.0, far above the flip at 84.9.
- **Weight:** Keep 0.55.
- **Flip:** 84.9.

## 95c970d4d1 (DOGE)
- **Market:** A long decline from 140 to 84, then a spike to 112, now back to 100.0. That is just below the flip at 100.2, so the flip is technically broken.
  - The spike has retraced only about 45% of the swing.
  - Price is still above the old 84–90 base.
- **Weight:** Keep 0.30. Any useful change would be under 0.15, which does not pay for its costs.
- **Flip:** 93.0. A close below it would mean the price is falling back toward the old base and the breakout has failed.

## a92abc1208 (AVAX)
- **Market:** The spike from 89 to 117 is holding at 100–107. The flip at 97.3 has not been broken.
- **Weight:** Keep 0.35.
- **Flip:** 97.3.

## 6f85223c2d (ETH)
- **Market:** A gap-up breakout from the 77–79 range to 100–104, and it is holding. Price is far above the flip at 87.7.
- **Weight:** Keep 0.35.
- **Flip:** 87.7.

## 5afbac6f4f (DOT)
- **Market:** A long downtrend from 188 to 92. The spike to 126 (intraday) has faded to 100. The upside flip at 120.3 has not been reached.
- **Weight:** Keep 0.10.
- **Flip:** 120.3.

## ea7f23c907 (SOL)
- **Market:** A breakout from the 72–75 range to 100–107. It is the strongest follow-through of these windows. Price is far above the flip at 78.8.
- **Weight:** Keep 0.35.
- **Flip:** 78.8.

## 42ef01f314 (LTC)
- **Market:** The recovery from 85 continued to 113, and price has now pulled back to 100.0. The lowest close is just above the flip at 99.2, so it has not been broken.
- **Weight:** Keep 0.40.
- **Flip:** 99.2.

{"e5a7949f1a (BTC)": {"weight": 0.40, "flip": 90.1}, "2f9279bb40 (XRP)": {"weight": 0.30, "flip": 94.1}, "23ae11b090 (ADA)": {"weight": 0.25, "flip": 111.0}, "907bbf7257 (LINK)": {"weight": 0.55, "flip": 84.9}, "95c970d4d1 (DOGE)": {"weight": 0.30, "flip": 93.0}, "a92abc1208 (AVAX)": {"weight": 0.35, "flip": 97.3}, "6f85223c2d (ETH)": {"weight": 0.35, "flip": 87.7}, "5afbac6f4f (DOT)": {"weight": 0.10, "flip": 120.3}, "ea7f23c907 (SOL)": {"weight": 0.35, "flip": 78.8}, "42ef01f314 (LTC)": {"weight": 0.40, "flip": 99.2}}

## Entscheidung 2026-09-06

**Strategy:** I keep last week's weight unless a daily close since then has crossed the flip price. If one has, I set a new weight from the weekly trend: 2-, 4- and 8-week momentum, the position relative to the long moving average, and swing structure. High volatility scales the weight down. I only change a weight when the move is at least 0.15, and I place the flip price at the level that would invalidate the structure.

## 13f4fba95c (LTC)
- **Market:** A long fall from about 106 to 75 is followed by a surge on days −18/−16 to about 97. The pullback held at 87.2 and price is now back at 100. The higher low around 87 is still intact.
- **Flip check:** The flip at 86.5 has not been broken.
- **Weight:** 0.40, unchanged.
- **Flip:** 86.5.

## 83265ba1e9 (DOGE)
- **Market:** The prior downtrend ran from about 127 to 76. A spike took price to 101 (wick to 111), it pulled back to 89.8, and it now closes at 100. Volatility is high.
- **Flip check:** The flip at 83.9 is far below every recent close.
- **Weight:** 0.30, unchanged.
- **Flip:** 83.9.

## 33c416e35a (LINK)
- **Market:** The trend has turned up. Higher lows ran from 54 to 61 to 72 to 84, and today's close at 100 is above the earlier peak of 90.6. Momentum is positive across all windows.
- **Flip check:** The flip at 71.5 has not been broken.
- **Weight:** 0.55, unchanged.
- **Flip:** 71.5.

## 510ba498b3 (ADA)
- **Market:** The flip at 95.7 was broken to the upside: closes of 99.0, 97.7 and 100.0. This needs a new decision.
- **Prior trend:** A crash from about 120 to 65, then a range from 70 to 90 with a slightly rising low.
- **Recent action:** A breakout on days −17/−16 to 102.6, with a wick to 115.7 that was not held. A pullback held at 86.3, which is above the earlier low of about 78. Price has recovered to 100.
- **Momentum:** The 4-week return is about +15% and the 8-week about +38%. The 2-week return is flat. All signs are positive.
- **Long-term context:** Price is above a flattening long moving average of roughly 90–95. Volatility is very high, which argues against a full weight.
- **Weight:** 0.45. This is a step-wise increase from 0.25, because the rebound comes out of a downtrend.
- **Flip:** 85.5, a close below the higher low of 86.3.

## b3c8c65181 (BTC)
- **Market:** After the breakout from 80 to 97, price has consolidated between 96 and 101. The trend is up and volatility is calmer here.
- **Flip check:** The flip at 87.1 has not been broken.
- **Weight:** 0.40, unchanged.
- **Flip:** 87.1.

## 9b9d51420b (AVAX)
- **Market:** The downtrend from about 130 to 75 was followed by a long range from 78 to 88. The breakout reached 99 and the pullback held at 89.9. Price now closes at 100, a new local high on a closing basis.
- **Flip check:** The flip at 87.5 has not been broken.
- **Weight:** 0.35, unchanged.
- **Flip:** 87.5.

## ae124103a8 (DOT)
- **Market:** A long downtrend ran from 167 to 76. The breakout from 77 reached 96, it pulled back to 83.7, and it has now risen to 100 (intraday high 101.3).
- **Flip check:** The flip at 100.6 is above the price. No close has broken it yet; the last close was 100.0.
- **Weight:** 0.10, unchanged.
- **Flip:** 100.6.

## 3fe3fe96e3 (XRP)
- **Market:** A sharp spike took price from 70 to 102–107 (wick to 119). It has since held in a range of 94 to 102, with very high volume and volatility.
- **Flip check:** The flip at 89.7 has not been broken.
- **Weight:** 0.30, unchanged.
- **Flip:** 89.7.

## 23d9babaf6 (SOL)
- **Market:** The trend has turned up from the 58 low, with a breakout from 70 to 102. The pullback low was 93.9, and the close of 100 is near the high.
- **Flip check:** The flip at 75.3 is far away.
- **Weight:** 0.35, unchanged.
- **Flip:** 75.3.

## fb2ec9f3af (ETH)
- **Market:** The recovery from 62 runs as a staircase of higher lows. A breakout reached about 100, followed by a tight range from 95 to 100.
- **Flip check:** The flip at 84.3 has not been broken.
- **Weight:** 0.35, unchanged.
- **Flip:** 84.3.

{"13f4fba95c (LTC)": {"weight": 0.40, "flip": 86.5}, "83265ba1e9 (DOGE)": {"weight": 0.30, "flip": 83.9}, "33c416e35a (LINK)": {"weight": 0.55, "flip": 71.5}, "510ba498b3 (ADA)": {"weight": 0.45, "flip": 85.5}, "b3c8c65181 (BTC)": {"weight": 0.40, "flip": 87.1}, "9b9d51420b (AVAX)": {"weight": 0.35, "flip": 87.5}, "ae124103a8 (DOT)": {"weight": 0.10, "flip": 100.6}, "3fe3fe96e3 (XRP)": {"weight": 0.30, "flip": 89.7}, "23d9babaf6 (SOL)": {"weight": 0.35, "flip": 75.3}, "fb2ec9f3af (ETH)": {"weight": 0.35, "flip": 84.3}}

## Entscheidung 2026-09-13

**Strategy:** I keep last week's weight unless a daily close since then has crossed the flip price. When a flip is triggered, the weekly regime sets the direction: 2/4/8-week momentum, the slope of the long average, and whether structure is HH/HL or LH/LL. Volatility then sets the size: a high σ20/σ90 ratio or a failed spike means a smaller weight. I make no change smaller than about 0.15 and close only part of any gap.

## a588cbdc04 (AVAX)
**Read:** Late-day breakout from the 85–92 base, from 87 to 108 and then 111. Price has given most of the last week back and sits at 100. Higher lows are holding (96–98), and the long 100–180-day average is still falling from above.

**Decision:** Flip 94.9 was not broken; the lowest close was 100.0. Weight stays at **0.35**.

**Flip:** 94.9.

## f1e8072a76 (BTC)
**Read:** Broke out of the 81–85 base on day −25 and has held a 99.6–106 shelf for three weeks. Volatility is moderate, and momentum is positive over 4 and 8 weeks.

**Decision:** Flip 91.1 was not broken. Weight stays at **0.40**.

**Flip:** 91.1.

## 5ef9939a20 (DOGE)
**Read:** Spike from 85 to 122 intraday, then a choppy range of 99–111. Today closed at 100, near the bottom of that range. Volatility is high.

**Decision:** Flip 92.6 was not broken; the lowest close was 100.0. Weight stays at **0.30**.

**Flip:** 92.6.

## ab04198a15 (XRP)
**Read:** Squeeze breakout from 74 to 126 (wick), now ranging 99–113. Volatility is very high, and momentum over 4 and 8 weeks is positive.

**Decision:** Flip 95.2 was not broken; the lowest close was 99.5. Weight stays at **0.30**.

**Flip:** 95.2.

## 01a714f437 (SOL)
**Read:** Up from 75 to 110, now holding 99–107. Higher lows are intact above 98, and momentum is positive.

**Decision:** Flip 80.8 is far below and was not broken. Weight stays at **0.35**.

**Flip:** 80.8.

## 5e08d8355f (DOT)
**Read:** A long downtrend from 160 to 76 bottomed around day −26. Since then:
- Two thrusts, to 94 and then a blow-off to 128.5 intraday on day −5.
- Price has retraced fully to 100.
- 2-, 4- and 8-week returns are all positive (about +22%, +31% and +22%).
- The 100-day average (~88) is flattening and price is above it.

However, last week was an extreme week with a long upper wick (week high 128.5, close 100). Volatility is in its top bracket (σ20/σ90 well above 1.5).

**Flip check:** The decision-day close was 98.0, and every close since then has been above 98.6. That breaks the upside flip, so a new decision is due.

**Weight: 0.35.** This is a partial move toward a trend weight. The momentum state has flipped positive, but the extreme volatility and the failed spike argue for a reduced size. The change of 0.25 clears the cost threshold.

**Flip:** 88.0. A close below it would break the post-breakout higher-low zone (82–90) and the momentum case.

## 9d6e9ce7ee (LINK)
**Read:** Steady base-building from 65 to 85, a breakout to 122, now back at 100. The structure of higher lows above ~97 is intact.

**Decision:** Flip 84.5 was not broken. Weight stays at **0.55**.

**Flip:** 84.5.

## acb327b33a (LTC)
**Read:** Broke out from 82 to 103, pulled back to 89, then retested 110 intraday. Price is now around 100 and momentum is positive.

**Decision:** Flip 88.4 was not broken. Weight stays at **0.40**.

**Flip:** 88.4.

## f7d6c2bfbb (ETH)
**Read:** Gapped up from 77 to 101 on day −25 and has since held a tight 96–102 range. The breakout is holding.

**Decision:** Flip 85.6 was not broken. Weight stays at **0.35**.

**Flip:** 85.6.

## 7454442ab7 (ADA)
**Read:** Volatile recovery from 70 to 127 (wick), now ranging 95–112. Higher lows are around 94–98, and volatility is high.

**Decision:** Flip 93.9 was not broken; the lowest close was 100.0. Weight stays at **0.45**.

**Flip:** 93.9.

{"a588cbdc04 (AVAX)": {"weight": 0.35, "flip": 94.9}, "f1e8072a76 (BTC)": {"weight": 0.40, "flip": 91.1}, "5ef9939a20 (DOGE)": {"weight": 0.30, "flip": 92.6}, "ab04198a15 (XRP)": {"weight": 0.30, "flip": 95.2}, "01a714f437 (SOL)": {"weight": 0.35, "flip": 80.8}, "5e08d8355f (DOT)": {"weight": 0.35, "flip": 88.0}, "9d6e9ce7ee (LINK)": {"weight": 0.55, "flip": 84.5}, "acb327b33a (LTC)": {"weight": 0.40, "flip": 88.4}, "f7d6c2bfbb (ETH)": {"weight": 0.35, "flip": 85.6}, "7454442ab7 (ADA)": {"weight": 0.45, "flip": 93.9}}

## Entscheidung 2026-09-20

**Strategy:** Last week's weight stays unless a daily close has fallen below last week's flip price. Within a regime, changes are driven only by state changes: a confirmed trend break, or a breakout that holds on weekly closes. Changes in distance or position in the range don't count, and changes under about 0.15 aren't worth the cost. Volatility sets position size, not direction.

## 7ca3d44133 (LTC)
- **Market:** A long downtrend from about 103 to 70 ran from day −135 to day −88. It was followed by a base at 74–80 and a breakout at day −30 to about 90. Price pulled back to 81.6, and the higher low held. The close is now 100, at the top of the 180-day range. Weekly structure is higher highs and higher lows, and 2-, 4- and 8-week momentum is positive.
- **Volatility:** Elevated after the breakout.
- **Flip:** No close since last week went below 80.9 (lowest was 87.3).
- **Weight:** Hold at 0.40. A high position in the range means hold, not add.
- **Change my mind:** A close below 80.9.

## 54212840e5 (XRP)
- **Market:** A downtrend from 105 to 71 was followed by a vertical spike to 103–108 at day −30. Since then it has been a wide sideways range of about 91–108, with very high volatility (wicks to 120 and 89.7).
- **Flip:** The lowest close was 91.0, so 90.5 was not broken.
- **Weight:** Hold at 0.30. Volatility is in its upper fifth, and the trend is unclear.
- **Change my mind:** A close below 90.5.

## 5158d7ff5b (ADA)
- **Market:** A crash from 124 to 61 was followed by a recovery with higher lows (61, 67, 76, 84). The breakout at day −30 reached 100, and price is now at 100 again. Momentum is positive, but volatility is high.
- **Flip:** The lowest close was 85.7, above 83.8.
- **Weight:** Hold at 0.45.
- **Change my mind:** A close below 83.8.

## 6f5002420c (DOT)
- **Market:** A long downtrend from 125 to 66 is now turning. There was a blow-off spike to 113 at day −12, a pullback to 83, and price is back at 100. Structure is still uneven, and volatility is very high.
- **Flip:** The lowest close was 83.3, above 77.5.
- **Weight:** Hold at 0.35.
- **Change my mind:** A close below 77.5.

## 88a8366107 (LINK)
- **Market:** A base at 57–67 was followed by a staged breakout: 76, then 92, then 105, with the pullback low at 86.9. Price is now at 100, near the 180-day high. The trend is clean, with a higher-high/higher-low structure and positive momentum across all windows.
- **Flip:** The lowest close was 86.9, above 75.6.
- **Weight:** Hold at 0.55.
- **Change my mind:** A close below 75.6.

## 234320b255 (AVAX)
- **Market:** Price sideways at 55–60 for months. It broke out to about 65–71 at day −30, then made an extreme two-day move from 67 to 100 on very high volume (z well above 2).
- **Reading:** A single extreme week leans toward a counter-move and raises expected volatility. That argues against adding.
- **Flip:** The lowest close was 64.3, above 61.2.
- **Weight:** Hold at 0.35.
- **Change my mind:** A close below 61.2.

## f9141aec10 (DOGE)
- **Market:** The high was about 132 at day −129, followed by a downtrend to 79. The breakout at day −30 reached 105, after which price moved sideways at 92–105. The close is 100, below the old highs, and the long average has only just flattened.
- **Flip:** The lowest close was 91.7, above 87.4.
- **Weight:** Hold at 0.30.
- **Change my mind:** A close below 87.4.

## 00b1efe496 (ETH)
- **Market:** A base at 70–73 broke out at day −32 to about 93. Since then price has consolidated at 90–96 and closed at 100, at the top of that range. Higher lows are in place and momentum is positive.
- **Flip:** The lowest close was 90.7, above 80.2.
- **Weight:** Hold at 0.35.
- **Change my mind:** A close below 80.2.

## 7f1fb37a55 (BTC)
- **Market:** The high was about 101 at day −137, with a low near 72. A breakout at day −30 was followed by a tight range of 93–100, and price closed at 100, at the top of the range. Volatility is moderate and structure is constructive.
- **Flip:** The lowest close was 93.2, above 86.2.
- **Weight:** Hold at 0.40.
- **Change my mind:** A close below 86.2.

## 11f5f22703 (SOL)
- **Market:** A low at 54–56 was followed by a recovery and a breakout from 69 to 98. Price consolidated at 87–96, then jumped to 101 on day −2. It is now at 100, the 180-day high, with positive momentum.
- **Flip:** The lowest close was 87.1, above 72.2.
- **Weight:** Hold at 0.35.
- **Change my mind:** A close below 72.2.

{"7ca3d44133 (LTC)": {"weight": 0.40, "flip": 80.9}, "54212840e5 (XRP)": {"weight": 0.30, "flip": 90.5}, "5158d7ff5b (ADA)": {"weight": 0.45, "flip": 83.8}, "6f5002420c (DOT)": {"weight": 0.35, "flip": 77.5}, "88a8366107 (LINK)": {"weight": 0.55, "flip": 75.6}, "234320b255 (AVAX)": {"weight": 0.35, "flip": 61.2}, "f9141aec10 (DOGE)": {"weight": 0.30, "flip": 87.4}, "00b1efe496 (ETH)": {"weight": 0.35, "flip": 80.2}, "7f1fb37a55 (BTC)": {"weight": 0.40, "flip": 86.2}, "11f5f22703 (SOL)": {"weight": 0.35, "flip": 72.2}}

## Entscheidung 2026-09-27

## Strategy

I hold last week's weight unless a daily close since that decision (days −6 to 0) has fallen through the stored flip price. Only a broken flip opens a new decision. Inside that, the weekly trend sets direction, volatility sets size, and changes below about 0.15 are skipped because of the 0.2 % switching cost. All ten flip prices sit well below this week's closes, so every weight carries over unchanged.

## 5af27d4ab7 (LTC)
- **Market:** Strong breakout. Price ran from the 62–64 base through the 74–83 zone to about 100 in the last week. Day −3 was a blow-off candle on 6.7× volume, and the market has held 100–102 since then.
- **Trend and volatility:** 2-, 4- and 8-week momentum all point up. Volatility is sharply elevated (σ20 is far above σ90), which argues against adding.
- **Flip check:** The lowest close this week was 86.8, far above the flip at 66.7. The flip was not broken.
- **Weight:** Hold 0.40.
- **Flip:** 66.7. A close below that would undo the breakout from the base.

## 34589936b6 (BTC)
- **Market:** Uptrend from the 74–77 base. Price broke above the 96 range top on day −6 and has held about 100 for five days on falling volume.
- **Structure:** Higher highs and higher lows.
- **Flip check:** The lowest close this week was 99.6, above 82.8.
- **Weight:** Hold 0.40.
- **Flip:** 82.8.

## 85fbc603ae (ETH)
- **Market:** Gap-driven trend out of the 70 base. The 89–94 range broke upward on day −6, and price is now holding about 100.
- **Trend:** Momentum is aligned upward across windows.
- **Flip check:** The lowest close this week was 99.9, above 78.9.
- **Weight:** Hold 0.35.
- **Flip:** 78.9.

## 44e826a0cf (DOGE)
- **Market:** Very volatile. Day −6 spiked to 109, the next day closed at 95.7, and price has since recovered to 100.
- **Trend and volatility:** The trend from the 72 base points up, but volatility is very high, so a small weight is appropriate.
- **Flip check:** The lowest close this week was 95.7, above 78.7.
- **Weight:** Hold 0.30.
- **Flip:** 78.7.

## 74fce9f448 (XRP)
- **Market:** Choppy rise from the 66 base. It made higher lows (84.6, then 99) and ran wide intraday swings on high volume.
- **Volatility:** Elevated.
- **Flip check:** The lowest close this week was 99.0, above 84.2.
- **Weight:** Hold 0.30.
- **Flip:** 84.2.

## d0d2ee6451 (LINK)
- **Market:** The cleanest trend in the set. Higher lows ran 77.6, then 88, then 100. Price is at a 180-day high, with the earlier 97–103 area left behind.
- **Trend:** Momentum is aligned upward.
- **Flip check:** The lowest close this week was 88.1, above 67.5.
- **Weight:** Hold 0.55.
- **Flip:** 67.5.

## c61b35538e (SOL)
- **Market:** Uptrend from the 60 base. Price cleared the 85–90 range and is now at 100, with higher lows at 79.4 and 94.3.
- **Flip check:** The lowest close this week was 94.3, above 65.8.
- **Weight:** Hold 0.35.
- **Flip:** 65.8.

## bfb98d4315 (AVAX)
- **Market:** Explosive two-day move from about 70 to 104, followed by a pullback to 93.6 and a recovery to 100.
- **Volatility:** Extremely high, with a single-shock character, which argues against adding.
- **Flip check:** The lowest close this week was 93.6, above 63.5.
- **Weight:** Hold 0.35.
- **Flip:** 63.5.

## 31baece8e7 (DOT)
- **Market:** Price spiked to 98 on day −19, retraced to 74.5, and is now back at 100 after several wide swings (for example 86.9 to 98).
- **Volatility:** High.
- **Flip check:** The lowest close this week was 86.9, above 69.4.
- **Weight:** Hold 0.35.
- **Flip:** 69.4.

## fee6d9bb68 (ADA)
- **Market:** Higher lows ran 76.6, then 93.5, with price back at 100 after a 104 high.
- **Trend and volatility:** Momentum points up, volatility is elevated, and the 8-week trend is up.
- **Flip check:** The lowest close this week was 93.5, above 74.9.
- **Weight:** Hold 0.45.
- **Flip:** 74.9.

{"5af27d4ab7 (LTC)": {"weight": 0.40, "flip": 66.7}, "34589936b6 (BTC)": {"weight": 0.40, "flip": 82.8}, "85fbc603ae (ETH)": {"weight": 0.35, "flip": 78.9}, "44e826a0cf (DOGE)": {"weight": 0.30, "flip": 78.7}, "74fce9f448 (XRP)": {"weight": 0.30, "flip": 84.2}, "d0d2ee6451 (LINK)": {"weight": 0.55, "flip": 67.5}, "c61b35538e (SOL)": {"weight": 0.35, "flip": 65.8}, "bfb98d4315 (AVAX)": {"weight": 0.35, "flip": 63.5}, "31baece8e7 (DOT)": {"weight": 0.35, "flip": 69.4}, "fee6d9bb68 (ADA)": {"weight": 0.45, "flip": 74.9}}
