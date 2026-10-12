# E-011: was die KI gedacht hat (Set A)

Volle Antwort des Deciders pro Entscheidungswoche, unverändert. Er sah weder Datum noch Coin-Namen; die Namen in Klammern sind erst danach eingesetzt. Gesendeter Prompt und Daten: runs/<set>/<woche>/requests.json.

## Entscheidung 2026-07-05

**Strategy:** Every window has the same backdrop: a long downtrend, a crash at about day -150, a 105–130 range, a second break at about day -33, and a sharp rally into 100. I estimate the day +7 odds from four things: the primary trend, whether the latest swing low was higher or lower, how close price is to resistance, and how stretched the last few days' rally is. Weight = 0.4 + 2 × (P(up) − P(down)), clipped to 0–1 and rounded to 0.05. The base of 0.4 reflects the bearish long-term backdrop.

## baa0c5a433 (ETH)
Scenarios: up 33, sideways 35, down 32

- **Trend:** Primary trend is down, from 185 to 100. The post-crash range of 110–135 broke at day -33.
- **Structure:** Double bottom at 84.3 (day -29) and 84.7 (day -9). Price then rallied five days in a row from 88 to 100 on modest volume.
- **Key levels:** Resistance at 101–103.6 (day -20 high). Support at 94–95, then 85.
- **Weight:** 0.4. The double bottom is constructive, but price is right at resistance inside a downtrend, so the odds are roughly balanced.
- **Change my mind:** a close above 104 (go higher) or below 94 (go flat).

## 572ba8d4d6 (SOL)
Scenarios: up 38, sideways 35, down 27

- **Trend:** Primary trend is down, but this is the strongest recovery of the set.
- **Structure:** Higher low at 78.5 (day -10) versus 73.7 (day -29). Price has already broken above the post-crash high of 93.3 and reached 102.9.
- **Key levels:** Support at 94–97. Old range floor and resistance at about 103–106.
- **Weight:** 0.6. Higher lows plus a breakout above the post-crash range tilt the odds up.
- **Change my mind:** a close below 94.

## 182785967b (BTC)
Scenarios: up 32, sideways 38, down 30

- **Trend:** A shallower decline than most windows. The 105–128 range broke at day -33.
- **Structure:** Lows at 92.9 (day -30) and 91.3 (day -10), essentially a double bottom. Price rallied into 100 on low volume.
- **Key levels:** Resistance at 103.4–105.7. Support at 94 and 91.
- **Weight:** 0.45. Balanced, with only a slight base forming.
- **Change my mind:** a close above 106 (go higher) or below 94 (go flat).

## f7ab670d14 (XRP)
Scenarios: up 30, sideways 37, down 33

- **Trend:** Down. The low of 87.2 at day -10 undercut the 90.7 low at day -29, a lower low.
- **Structure:** Rally to 100 that stalled at 102.3 on day -1. The day -20 spike to 111.8 failed.
- **Key levels:** Resistance at 102–107. Support at 94, then 87.
- **Weight:** 0.35. The lower low and failed spike lean slightly bearish.
- **Change my mind:** a close above 107.

## 5827c6fa78 (ADA)
Scenarios: up 35, sideways 25, down 40

- **Trend:** Steep downtrend, with a capitulation from 124 to 73 that included a lower low at 72.9 (day -10).
- **Structure:** Explosive rally of about 30% in four days on heavy volume (2.1–2.2× average) to 105.5. Day 0 is an inside, slightly bearish candle.
- **Key levels:** Resistance at 103–105.5. Support at 94–95, then 85.
- **Weight:** 0.3. A move this extended is prone to retrace and makes outcomes very wide, so I keep exposure small.
- **Change my mind:** a close above 106 would confirm a reversal.

## 96aec10a4c (AVAX)
Scenarios: up 34, sideways 38, down 28

- **Trend:** Down. Capitulation to 82 at day -16 on 3× volume.
- **Structure:** Higher lows since the capitulation at 86 and 90.6, then a steady climb to 100.
- **Key levels:** Resistance at 102–103. Support at 94–96.
- **Weight:** 0.5. The higher-low sequence after the volume climax leans mildly up.
- **Change my mind:** a close below 94.

## afb6d57568 (LTC)
Scenarios: up 33, sideways 38, down 29

- **Trend:** Down. The low of 85.7 at day -10 undercut the 88.4 low at day -29.
- **Structure:** Orderly recovery that closed day 0 at the high of the day (100.0, high 100.7).
- **Key levels:** Resistance at 101. A break there opens 105–110. Support at 95–96.
- **Weight:** 0.5. The strong close near resistance leans slightly up.
- **Change my mind:** a close below 95.

## f05bd1120a (DOT)
Scenarios: up 30, sideways 37, down 33

- **Trend:** Strongest downtrend of the set, with lower highs at 118.8 (day -20) and 111 (day -15), and a lower low at 90.2.
- **Structure:** Rally to 100 on falling volume.
- **Key levels:** Resistance at 102–111. Support at 93, then 90.
- **Weight:** 0.35. The downtrend structure is intact.
- **Change my mind:** a close above 111.

## 6a6d8479f5 (LINK)
Scenarios: up 33, sideways 37, down 30

- **Trend:** Down. Double bottom at 86.8 (day -29) and 86.9 (day -10).
- **Structure:** Rally to 100 on very light volume (0.34–0.38× average).
- **Key levels:** Resistance at 101.5–106.7. Support at 94, then 87.
- **Weight:** 0.45. The base is constructive, but the lack of volume undercuts the rally.
- **Change my mind:** a close above 107 (go higher) or below 94 (go flat).

## ddce9ddff2 (DOGE)
Scenarios: up 29, sideways 37, down 34

- **Trend:** Down. Lower highs at 118.7, 116.8 and 109.3, and a lower low at 91.8 (day -10) versus 99.7 (day -29).
- **Structure:** Bounce to 100 on light volume.
- **Key levels:** Resistance at 102–109. Support at 92.
- **Weight:** 0.3. The pattern of lower highs and lower lows argues for little exposure.
- **Change my mind:** a close above 109.

{"baa0c5a433 (ETH)": 0.4, "572ba8d4d6 (SOL)": 0.6, "182785967b (BTC)": 0.45, "f7ab670d14 (XRP)": 0.35, "5827c6fa78 (ADA)": 0.3, "96aec10a4c (AVAX)": 0.5, "afb6d57568 (LTC)": 0.5, "f05bd1120a (DOT)": 0.35, "6a6d8479f5 (LINK)": 0.45, "ddce9ddff2 (DOGE)": 0.3}

## Entscheidung 2026-07-12

**Strategy:** For each window I estimate up/sideways/down odds from the recent swing structure: whether lows are rising or falling, where price sits between the post-crash low and the latest rally high, and how volatile and active the tape is. The weight is P(up) / (P(up) + P(down)), rounded to 0.05, so sideways odds don't move the weight. The long-term downtrend (every window is far below its starting level) keeps up-odds modest unless the short-term structure is clearly constructive.

### 97474da358 (SOL)
Scenarios: up 32, sideways 36, down 32
- **Read:** Primary downtrend from about 190. The capitulation low of 78.2 (day -36) was followed by a higher low at 83.3 (-17) and a rally to 109.2 (-8). Price has since pulled back on fading volume to 100.
- **Levels:** Support is 98.3–99.2. Resistance is 107–109.
- **Weight 0.50:** The higher-low structure offsets the downtrend, and the quiet pullback is neither bullish nor bearish.
- **Change my mind:** A close below 97 would cut me to about 0.2. A close above 105 would raise me.

### 808c9499d7 (BTC)
Scenarios: up 25, sideways 50, down 25
- **Read:** Fell from about 150 to a 92.7 low (-37). It then made marginally lower lows at 91.1 and 90.6 (-17 to -11) and grinded up to a tight 99.8–101.4 range. Realized volatility is the lowest of the set, so sideways is the most likely outcome.
- **Levels:** Support is 96.5. Resistance is 101.4–103.
- **Weight 0.50:** The odds are balanced, and I hold a half position.
- **Change my mind:** A close below 96.5 means reduce. A close above 103 means add.

### 370001242c (AVAX)
Scenarios: up 28, sideways 34, down 38
- **Read:** Low of 88.7 (-23), then a rally to 111.1 (-8). Since then the highs have been lower (106.7, 106.0). Today it tagged 98.0 intraday before closing at 100.
- **Levels:** Support is 98, then 93. Resistance is 106–107.
- **Weight 0.40:** Rolling lower highs inside a long downtrend tilt the odds down.
- **Change my mind:** A close above 107 would make me go heavier. A close below 97 would take me to about 0.2.

### b2fd30806f (LTC)
Scenarios: up 30, sideways 42, down 28
- **Read:** Low of 89.3 (-18/-17), then a rally to 104.9 (-7), and now a quiet 98–104 range at 100 on low volume. The decline since -40 is orderly, not capitulative.
- **Levels:** Support is 98.1. Resistance is 104–105.
- **Weight 0.50:** The setup is neutral.
- **Change my mind:** A close below 97 means reduce. A close above 105 means add.

### b5e2db7b9e (DOT)
Scenarios: up 30, sideways 32, down 38
- **Read:** Low of 94.2 (-14), then a rally to 107.6 (-6) and a drop to 96.6. A spike to 106.0 (-2) on volume was rejected, and price closed back at 100. This window has the highest volatility of the set.
- **Levels:** Support is 96.6–97.3. Resistance is 106–107.6.
- **Weight 0.45:** The rejected rally and lower highs lean slightly bearish.
- **Change my mind:** A close below 96.5 takes me to about 0.2. A close above 106 raises me.

### aa2a8e3244 (ETH)
Scenarios: up 35, sideways 37, down 28
- **Read:** Double bottom at 83.3 (-36) and 83.7 (-16), followed by a steady rally from 87 to 101.5. Price is now consolidating just under the 100–102.4 neckline on light volume.
- **Levels:** Support is 94.8–96.2. Resistance and the breakout trigger are at 102.4.
- **Weight 0.55:** The base is the most constructive in the set.
- **Change my mind:** A close below 94.8 means cut. A close above 102.4 means add.

### 179b0a2b58 (XRP)
Scenarios: up 30, sideways 38, down 32
- **Read:** Low of 96.7 (-36), then a lower low at 92.9 (-16) and a rally to 109.1 (-8). Price has since retraced to 100 on very low volume.
- **Levels:** Support is 98.5–99.6. Resistance is 106–109.
- **Weight 0.50:** The lower low is offset by the strong rebound.
- **Change my mind:** A close below 98 means reduce. A close above 106 means add.

### c9821d9d93 (ADA)
Scenarios: up 28, sideways 30, down 42
- **Read:** Crash low of 91.7 (-36), then 85.3 (-17), then a volume spike to 123.4 (-8). The whole spike has since retraced to 100, which is a failed breakout. Volatility is high.
- **Levels:** Support is 99.3, then 88–85. Resistance is 108, then 118.
- **Weight 0.40:** A full retrace of a blow-off rally is bearish.
- **Change my mind:** A close back above 108 would raise me. A close below 97 would take me to about 0.15.

### cf12d13b1b (DOGE)
Scenarios: up 28, sideways 42, down 30
- **Read:** Low of 95.6 (-12), then a rally to 109.2 (-8) and a fade to 100 on the lowest volume of the window. Highs keep falling from about 160, but the short-term lows are holding.
- **Levels:** Support is 97.6. Resistance is 105–109.
- **Weight 0.50:** Neutral, with a quiet tape.
- **Change my mind:** A close below 97 means reduce. A close above 105 means add.

### 40e3e6b110 (LINK)
Scenarios: up 32, sideways 40, down 28
- **Read:** Double bottom at 87.5 (-36) and 87.7 (-17), followed by a rally to 102.3. Price is now consolidating at 100 on low volume, with a shallow higher low at 94.1 (-4).
- **Levels:** Support is 94. Resistance is 102.3, then 107.5.
- **Weight 0.55:** A constructive base.
- **Change my mind:** A close below 94 means cut. A close above 102.5 means add.

{"97474da358 (SOL)": 0.5, "808c9499d7 (BTC)": 0.5, "370001242c (AVAX)": 0.4, "b2fd30806f (LTC)": 0.5, "b5e2db7b9e (DOT)": 0.45, "aa2a8e3244 (ETH)": 0.55, "179b0a2b58 (XRP)": 0.5, "c9821d9d93 (ADA)": 0.4, "cf12d13b1b (DOGE)": 0.5, "40e3e6b110 (LINK)": 0.55}

## Entscheidung 2026-07-19

**Strategy:** Every window is read on trend (where price sits against the 180-day decline and the most recent swing structure), on higher lows versus lower highs over the last 20–30 days, and on how volume behaves at key levels. I estimate up, sideways and down probabilities, then set weight = 0.40 + 2 × (P(up) − P(down)), clipped to 0–1. That gives a moderate base exposure that grows with upside skew and shrinks with downside skew.

### b0c1d3bc58 (ETH)
Scenarios: up 30, sideways 45, down 25

- **Read:** Long-term downtrend from about 157. A capitulation low came at 80.8 (day -23), followed by steady higher lows at 82.9, 91.5, 93.5 and 96.3.
- **Levels:** Price pushed to 104.0 and is now consolidating at 100 on light volume. Resistance is 104, support is 96.3.
- **Weight:** The short-term base is constructive but sits under a heavy long-term downtrend, so a mild positive skew gives 0.50.
- **Change my mind:** A close below 96 (bearish) or above 104 (bullish).

### 2f8f344cdb (LTC)
Scenarios: up 32, sideways 45, down 23

- **Read:** Low at 83.5 (day -25), then higher lows at 87.4, 91.2 and 93.7.
- **Levels:** Day -1 broke above the 97–98 range on above-average volume (101.7 high), and day 0 held 100. Support is 97 then 93.7, resistance is 102–105.
- **Weight:** A breakout with volume behind it earns the best skew in the set: 0.58.
- **Change my mind:** A close below 96 would mark the breakout as failed.

### 35aeb25093 (SOL)
Scenarios: up 26, sideways 47, down 27

- **Read:** The bounce from 78.7 peaked at 110 (day -15). Highs since then are lower (104.3, 103.5, 101.6), while lows hold around 96–97. This is a descending triangle into 100.
- **Levels:** Support 96, resistance 102–104.
- **Weight:** The setup is neutral to slightly bearish: 0.38.
- **Change my mind:** A close above 104 (bullish) or below 96 (bearish).

### f5cadea240 (XRP)
Scenarios: up 27, sideways 48, down 25

- **Read:** The decline from 177 bottomed at 91.9 (day -23). The rally to 107.9 faded.
- **Levels:** Price is in a tight 96–102 range with very low volume, now at 100. Support 96, resistance 102 then 108.
- **Weight:** Balanced, coiling price action: 0.44.
- **Change my mind:** A close below 96.

### ac377dc752 (DOT)
Scenarios: up 22, sideways 43, down 35

- **Read:** This is the steepest decline in the set, from 238 to 100. Lower highs continue (109.8, 109.1, 106.6).
- **Levels:** Day 0 closed at 100, near the low of the day (98.3), and slipped below the 101–104 shelf. The next supports are 97 and 99.4. Resistance is 104–107.
- **Weight:** A weak close inside a strong downtrend gives a bearish skew: 0.14.
- **Change my mind:** A close back above 105.

### 3836ac7d59 (DOGE)
Scenarios: up 25, sideways 48, down 27

- **Read:** A failed rally to 160 rolled over into a decline to 96–98.6. Lower highs since then are 109.6, 104.4 and 104.1.
- **Levels:** Price is in a very quiet range at 98–102, with volume drying up, so a breakout is likely but its direction is unclear. Support 98, resistance 104.
- **Weight:** 0.36.
- **Change my mind:** A close above 104 (bullish) or below 97.5 (bearish).

### 450345122e (BTC)
Scenarios: up 30, sideways 50, down 20

- **Read:** This is the shallowest drawdown in the set. The low was 89.3 (day -18), followed by a clean series of higher lows at 92.1, 94.7, 95.1, 95.5 and 96.6.
- **Levels:** Price is pressing resistance at 100.4–101.7. Support is 96.5.
- **Weight:** The structure is constructive: 0.60.
- **Change my mind:** A close below 96 (bearish) or above 102 (bullish).

### 0d900e1499 (AVAX)
Scenarios: up 27, sideways 47, down 26

- **Read:** The low was 87.9 (day -30). Price has ranged between 97 and 110 since then, with lower highs at 110.1, 105.7 and 104.8.
- **Levels:** Day 0 was rejected at 102.7 and closed at 100. Support is 97–98, resistance 104–105.
- **Weight:** Neutral: 0.42.
- **Change my mind:** A close below 97.

### dd0e657f5e (LINK)
Scenarios: up 30, sideways 45, down 25

- **Read:** A double bottom at about 83.5 (days -43 and -24), then higher lows at 89.7, 93.0 and 95.5.
- **Levels:** Price tagged 103 and is holding at 100. Support is 95.5, resistance 103.
- **Weight:** Mildly constructive: 0.50.
- **Change my mind:** A close below 95.5 (bearish) or above 103 (bullish).

### 99328c9449 (ADA)
Scenarios: up 29, sideways 40, down 31

- **Read:** A violent spike to 120 (day -15) was fully retraced back to 100. That is a failed breakout, though the lows at 93.4 and 94.9 are holding.
- **Levels:** Volatility is high and the range is 94–102.
- **Weight:** Wide, slightly bearish-skewed outcomes: 0.36.
- **Change my mind:** A close above 103 (bullish) or below 94 (bearish).

{"b0c1d3bc58 (ETH)": 0.5, "2f8f344cdb (LTC)": 0.58, "35aeb25093 (SOL)": 0.38, "f5cadea240 (XRP)": 0.44, "ac377dc752 (DOT)": 0.14, "3836ac7d59 (DOGE)": 0.36, "450345122e (BTC)": 0.6, "0d900e1499 (AVAX)": 0.42, "dd0e657f5e (LINK)": 0.5, "99328c9449 (ADA)": 0.36}

## Entscheidung 2026-07-26

## Strategy

I estimate the up/sideways/down odds from trend structure: the sequence of swing highs and lows, where the close sits against nearby support and resistance, and recent volume. The weight is P(up) / (P(up) + P(down)), rounded to 0.05, so sideways probability doesn't push the weight either way. A close beyond the stated invalidation level means I reassess.

## e2a1859f72 (LINK)
Scenarios: up 35, sideways 45, down 20

- **Trend:** Long decline from about 136 to a low of 79.4 (day -31).
- **Recovery:** Since then the lows have stepped higher: 80.2, 85.2, 93.7 and 94.9.
- **Day 0:** Closed at 100, the top of its range, breaking above the 99.3 high from day -5.
- **Levels:** Resistance at 103–105, which was support before the drop at day -54. Support at 94–95.

**Weight 0.65.** The structure is constructive and the breakout came on the decision day. **Change my mind:** a close below 93.5.

## 87b33d5ca5 (XRP)
Scenarios: up 30, sideways 50, down 20

- **Trend:** Decline from 172 to a low of 90.7 (day -30), then a recovery to 104–106 (days -22 and -5).
- **Recovery:** Higher lows at 92.7, 94.6 and 97.3.
- **Day 0:** Closed at 100, in the middle of a 97–104.6 range, on quiet volume.

**Weight 0.6.** The bias is mildly positive but the price is stuck in its range. **Change my mind:** a close below 96.

## 11d2b79c5f (ADA)
Scenarios: up 30, sideways 45, down 25

- **Trend:** Crash from 217 to 83 (day -31).
- **Recent move:** A spike to 120.5 (day -22) failed. Since then the price has ranged between 93.6 and 109.
- **Recovery:** Lows have risen from 93.6 to 97.3, but the highs have been capped near 105–109.
- **Day 0:** Closed at 100.

**Weight 0.55.** **Change my mind:** a close below 95, which would break the higher-low pattern.

## 4f3729123c (LTC)
Scenarios: up 35, sideways 45, down 20

- **Trend:** Decline from 146 to 82 (day -32), followed by an orderly recovery with steady higher lows: 86, 90.2, 95.6 and 97.2.
- **Day 0:** Closed at 100 on above-average volume, pressing against the 100–100.9 resistance that has held since day -8.

**Weight 0.65.** **Change my mind:** a close below 95.5.

## fd8fabe2dc (BTC)
Scenarios: up 30, sideways 50, down 20

- **Trend:** Decline from 136 to 88.4 (day -25), then a recovery.
- **Range:** Price has held 96.5–102.4 for three weeks, with lows rising to 97.5.
- **Day 0:** Closed at 100, in the middle of the range.
- **Levels:** Resistance at 102.4. Support at 96.5–97.5.

**Weight 0.6.** **Change my mind:** a close below 96.5.

## 4359adf1d2 (DOGE)
Scenarios: up 27, sideways 45, down 28

- **Trend:** Decline from 172 to 94.7 (day -26).
- **Weakness:** The highs have been falling: 108.2, then 103, then 100.9.
- **Recent move:** Price dropped sharply to 93.2 at day -3, then rebounded to 100.
- **Levels:** Range of roughly 93–103.

**Weight 0.5.** The structure is mixed. **Change my mind:** a close above 103 would make me more bullish. A close below 93 would take me to flat.

## e544e5a326 (DOT)
Scenarios: up 27, sideways 45, down 28

- **Trend:** Crash from 226 to 96 (day -28).
- **Range:** Price has moved between 95 and 109.7 since then, with falling highs: 109.7, 108.1, 105.6, 105.0.
- **Recent lows:** The low at day -2 was 95.0, which retests support.
- **Day 0:** Closed at 100.

**Weight 0.5.** **Change my mind:** a close below 95 would take me to flat. A close above 105.5 would take me higher.

## bc62f3fd30 (ETH)
Scenarios: up 35, sideways 45, down 20

- **Trend:** Decline from 154 to 77 (day -50 and again at day -30), then a strong recovery.
- **Recovery:** Higher lows at 87.7, 92.2 and 94.5.
- **Day 0:** Closed at 100, up 4.3% on the day, near the 99.6–100.6 highs.

**Weight 0.65.** **Change my mind:** a close below 94.

## c4db5aa2c3 (SOL)
Scenarios: up 28, sideways 47, down 25

- **Trend:** Crash from 165 to 78.3 (day -50).
- **Recent move:** A rally to 109.4 (day -22) was followed by a pullback.
- **Weakness:** Highs have been falling: 109.4, then 103.8, then 102.8.
- **Support:** Lows have held at 95.6–96.5.
- **Day 0:** Closed at 100.

**Weight 0.55.** **Change my mind:** a close below 95.5.

## 64594bd586 (AVAX)
Scenarios: up 30, sideways 40, down 30

- **Trend:** Crash from 180 to 84.2 (day -37).
- **Range:** Choppy trading between 88 and 105.5, with falling highs: 105.5, 101.3, 100.7.
- **Recent move:** Price dropped to 91.0 at day -2, then jumped 7.6% on 1.5x volume to 100.5, closing at 100 on day 0.
- **Volatility:** High.

**Weight 0.5.** **Change my mind:** a close below 91 would take me to flat. A close above 105.5 would take me higher.

{"e2a1859f72 (LINK)": 0.65, "87b33d5ca5 (XRP)": 0.6, "11d2b79c5f (ADA)": 0.55, "4f3729123c (LTC)": 0.65, "fd8fabe2dc (BTC)": 0.6, "4359adf1d2 (DOGE)": 0.5, "e544e5a326 (DOT)": 0.5, "bc62f3fd30 (ETH)": 0.65, "c4db5aa2c3 (SOL)": 0.55, "64594bd586 (AVAX)": 0.5}

## Entscheidung 2026-08-02

**Strategy.** I read each window on its own: the trend since the crash low around day −58 to −38, the 20-day range, and whether highs and lows are rising or falling. Each scenario estimate uses about a ±3% move over a week against the window's recent volatility. The weight is then 0.5 + (up − down)/40, clamped to 0–1 and rounded to 0.05, so I only lean long or flat when the odds are lopsided.

## f5e2220d20 (ETH)
Scenarios: up 28, sideways 47, down 25
The 125 → 80 slide bottomed near 80 around day −38. Since then lows have been rising (80 → 91 → 95.6 → 96.6). For the last 20 days price has ranged 96.6–105.1 on low volume, and day 0 bounced from 97.8 to 100. Support is 96.5–97 and resistance 104–105. This is neutral with a slight upward tilt, so **weight 0.55**. A close below 96 changes my mind toward flat; a close above 105.5 toward long.

## bc94a7ee9a (BTC)
Scenarios: up 28, sideways 50, down 22
This one held up better: the post-crash low was 91.4, with a higher-low base near 98. Price has been in a tight 98–105.3 range for 3 weeks, and the day −2 dip to 98.3 was bought. Support is 98, resistance 105. It is basing above support, so **weight 0.65**. A close below 97.5 changes my mind.

## 61adc8d6f9 (XRP)
Scenarios: up 25, sideways 45, down 30
The low was 92.9, followed by a spike to 109 at day −29. Since then highs have been falling (109 → 107.1 → 102.7 → 100.6) and the recent lows sit at 96.1–96.4. Price is drifting down within a 96–103 band. Support is 96, resistance 102.7. I lean slightly bearish, so **weight 0.4**. A close above 103 changes my mind to long; a close below 96 to flat.

## 474869e346 (ADA)
Scenarios: up 40, sideways 30, down 30
This window is highly volatile. Price crashed to 72.9, rallied to 105.5, and fell back to 81. Day 0 is a strong breakout: +8.7% on 1.73× volume, through the 93–95 highs, to 100. The structure from 81 → 85 → 92 → 100 shows higher lows. Resistance is 101.4–105.5, and the breakout level of 95 is now support. Momentum favours longs, but the wide ranges keep the down risk high, so **weight 0.75**. A close back below 92 would cancel the breakout.

## 6703655125 (SOL)
Scenarios: up 25, sideways 45, down 30
The low was 87, followed by a rally to 114 at day −30. Since then highs have kept falling (114 → 108 → 106.5 → 104.7 → 101.8), and price is grinding into 96–98 support. The day −1 low was 95.9. This is a mild downtrend, so **weight 0.4**. A close below 95.5 means flat; a close above 104.5 means long.

## c0fb93e19c (LTC)
Scenarios: up 27, sideways 48, down 25
Price rose from the 87.9 low to 108 at day −7, then pulled back to 97.6–100. The prior breakout zone of 100–101 is being tested. Highs are rising on the 6-week view, but the last week was soft. Support is 97.5, resistance 105–108. This is neutral, so **weight 0.55**. A close below 97 changes my mind.

## eb94d13cf8 (AVAX)
Scenarios: up 32, sideways 40, down 28
There were two flushes, to 95 and to 86.7, followed by a choppy 92–108 range. Day −1 hit 92.2, then day 0 reversed sharply to 100 (+5.8%, 1.05× volume), which looks like a bullish rejection of the range floor. Support is 92–94, resistance 103–105. There is a slight long edge, so **weight 0.6**. A close below 94 changes my mind.

## eab52731f1 (DOGE)
Scenarios: up 25, sideways 45, down 30
Price has fallen from 160+ to about 100. Lower highs persist (125 → 112 → 106.5 → 104.6), and the recent lows are 95.6–96.7. Volume is fading, but the structure is still bearish. Support is 95.5, resistance 104.5. **Weight 0.4.** A close above 105 means long; a close below 95 means flat.

## 6cf597a3d7 (LINK)
Scenarios: up 30, sideways 43, down 27
Lows have been rising (83.6 → 89.7 → 95.5 → 94.1) and the high was 106.3 at day −6. Price is ranging 94–106. Day −1 hit 94.1, then day 0 bounced to 100 on 0.52× volume. Support is 94, resistance 105–106. This is slightly constructive, so **weight 0.55**. A close below 94 changes my mind.

## 32791cca7c (DOT)
Scenarios: up 27, sideways 40, down 33
This window has a persistent long downtrend from 208 to 93. Day −6 had a −8% gap down to 93.6, and price has only recovered to 100 since then. Highs keep falling (112 → 109 → 108.8 → 104.1). Resistance is 101–104, support 93. The bias is bearish, so **weight 0.35**. A close above 104.5 changes my mind to long; a close below 93 means flat.

{"f5e2220d20 (ETH)": 0.55, "bc94a7ee9a (BTC)": 0.65, "61adc8d6f9 (XRP)": 0.4, "474869e346 (ADA)": 0.75, "6703655125 (SOL)": 0.4, "c0fb93e19c (LTC)": 0.55, "eb94d13cf8 (AVAX)": 0.6, "eab52731f1 (DOGE)": 0.4, "6cf597a3d7 (LINK)": 0.55, "32791cca7c (DOT)": 0.35}

## Entscheidung 2026-08-09

**Strategy:** I read each window's trend and structure (swing highs and lows, the regime since the large crash around day -65, and volume behavior) and estimate the 7-day outcome probabilities from that. Weight = clamp(0.5 + 2 × (P(up) − P(down)), 0, 1). This keeps me neutral when there is no edge, and only a large directional edge pushes the weight towards 0 or 1.

### cd5a8f3fd3 (LINK)
Scenarios: up 30, sideways 42, down 28
- **Read:** The peak was about 130 (day -91), followed by a crash to 85.5. Since then the lows have been rising (85.6, 86.4, 91.9, 96.3, 98.0). For the last 10 days price has been compressed in a 98–103 range on fading volume. Resistance sits at 105–108 and support at 98.
- **Weight:** 0.54. Higher lows give a slight bullish tilt, but the range is tight and there is no breakout yet.
- **Change of mind:** a close below 97.5 (bearish) or above 104 (bullish).

### 1ed940c1c5 (LTC)
Scenarios: up 28, sideways 44, down 28
- **Read:** After the crash to 86.4, price recovered to 105–106. Recent highs are falling (106.2, then 102.3) and the low was 96 at day -8. It is now a range of 96–102 on low volume.
- **Weight:** 0.50. The structure is balanced and I have no edge.
- **Change of mind:** below 96 or above 103.5.

### e791c8fd05 (SOL)
Scenarios: up 27, sideways 40, down 33
- **Read:** Price rallied from 78.8 to 110 (day -36), then trended down with lower highs to a low of 92.5 at day -8. The latest bounce to 100 came on light volume, with resistance at 102–103.
- **Weight:** 0.38. The intermediate downtrend is intact and the bounce is into resistance.
- **Change of mind:** a close above 103.5.

### 8ac3e0e3ff (DOT)
Scenarios: up 25, sideways 38, down 37
- **Read:** This is a persistent downtrend from about 208 to 100, with lower highs at 131, 113.6, 112 and 108.9. The bounce from 93 to 108.9 has faded back to 100, and support is at 93–95.
- **Weight:** 0.26. The structure is bearish and the recent rally failed.
- **Change of mind:** a close above 109.

### 7183649586 (ETH)
Scenarios: up 32, sideways 42, down 26
- **Read:** After the crash low of 78.8, price has made steady higher lows (79, 89.7, 94.4, 95.4, 97.1). It is now holding 99–101 with very low volume, which looks like a tight base just under resistance at 102–104.
- **Weight:** 0.62. The recovery structure is constructive.
- **Change of mind:** a close below 96.5.

### 71ab10d137 (XRP)
Scenarios: up 25, sideways 40, down 35
- **Read:** The bounce off 98 topped at 115. Since then there have been lower highs (113, 109.7, 108.4, 106.2) and the latest dip reached 98.3. That threatens the base at 98–100.
- **Weight:** 0.30. Price is drifting lower and testing support.
- **Change of mind:** a close above 106.5.

### 1023b63c75 (AVAX)
Scenarios: up 31, sideways 38, down 31
- **Read:** After the crash to 88.5, price has spent about 40 days in a wide, choppy range of 94–109. Volatility is elevated and the current price is mid-range.
- **Weight:** 0.50. There is no directional edge.
- **Change of mind:** above 109 or below 94.

### 8bfde3d973 (BTC)
Scenarios: up 24, sideways 54, down 22
- **Read:** This is a low-volatility series. It recovered from 89.5 and has held a tight 96–103 range for a month, with a slight upward drift.
- **Weight:** 0.54. Sideways is the most likely outcome, with a slight tilt up.
- **Change of mind:** below 96 or above 103.5.

### b282aa3e9d (ADA)
Scenarios: up 36, sideways 32, down 32
- **Read:** After a deep crash to 71, price spiked to 102.8 and fell back to 79. It then made a strong high-volume rally from 79 to 108.8, breaking above the 79–93 range. It is now pulling back to 100 from resistance at 103–105, with support at 93–97. Volatility is high.
- **Weight:** 0.58. Momentum and the range breakout favor upside, but swings are large.
- **Change of mind:** a close below 95.

### 89dd07ff37 (DOGE)
Scenarios: up 26, sideways 46, down 28
- **Read:** This is a long decline from 171 to about 100, with lower highs at 114.5, 108.7, 106.8 and 103.2. Ranges are now very tight around 99–103 on low volume, so the downtrend looks to be stalling.
- **Weight:** 0.46. The trend is bearish, but compression makes sideways likely.
- **Change of mind:** above 104 (bullish) or below 97.5.

{"cd5a8f3fd3 (LINK)": 0.54, "1ed940c1c5 (LTC)": 0.5, "e791c8fd05 (SOL)": 0.38, "8ac3e0e3ff (DOT)": 0.26, "7183649586 (ETH)": 0.62, "71ab10d137 (XRP)": 0.3, "1023b63c75 (AVAX)": 0.5, "8bfde3d973 (BTC)": 0.54, "b282aa3e9d (ADA)": 0.58, "89dd07ff37 (DOGE)": 0.46}

## Entscheidung 2026-08-16

Strategy: I weight trend and structure most heavily, meaning the direction of swing highs and lows and whether price is above or below recent ranges. I then convert the scenario probabilities into a weight with one formula: weight = clamp(0.5 + (up − down)/40, 0, 1). Tight low-volume ranges get roughly neutral weights. Clear lower-high downtrends get low weights. Confirmed breakouts get higher weights.

## 13c76926cf (LINK)
Scenarios: up 34, sideways 40, down 26
- **Trend:** The market crashed from about 110 to 75 (days -75 to -72), based between 77 and 92, and has been rising since day -6.
- **Breakout:** Day -1 broke above the 92–95 range on volume of 1.66, touched 103.8 intraday, and closed at 100.9. Day 0 held at 100 on light volume.
- **Levels:** Support is 95 and then 92; resistance is 103.8 and then 106–110.
- **Weight 0.7:** The momentum and the volume-backed breakout favour the upside.
- **Change of mind:** A close below 94 would mean the breakout failed.

## 4634f69929 (BTC)
Scenarios: up 22, sideways 58, down 20
- **Trend:** The market fell from 130 to 94, recovered, and has held a tight 99–104 range for about 30 days on fading volume.
- **Bias:** The longer-term trend is still below the old 120s, but the short-term picture is balanced.
- **Weight 0.55:** The range is balanced, with a slight edge from its higher lows.
- **Change of mind:** A close below 99 would break the range.

## 4e85e6d40d (XRP)
Scenarios: up 20, sideways 50, down 30
- **Trend:** The market fell from about 150 to 110, bounced to 124 and then 116.5, and has made a steady series of lower highs since day -26.
- **Recent action:** Price has drifted from 112 to 100 over the last two weeks without a bounce, so the downtrend is intact.
- **Levels:** Resistance is 105 and then 110; support is about 99.3, then the 102–105 area of day -50, which has already been broken.
- **Weight 0.25:** The trend points down.
- **Change of mind:** A close above 105 would signal a turn.

## 67721c671c (LTC)
Scenarios: up 26, sideways 50, down 24
- **Trend:** The market crashed to about 89 and has built higher lows since (89, then 93, then 98). It rallied to 108 around day -28 and has pulled back to 100.
- **Levels:** Support is 98.3 and then 97; resistance is 104–105 and then 108.
- **Weight 0.55:** The pullback is holding inside a recovering structure, but the edge is small.
- **Change of mind:** A close below 98 would end the higher-low structure.

## e3a91a992c (DOT)
Scenarios: up 22, sideways 46, down 32
- **Trend:** This is a persistent downtrend from about 219 to 100, with lower highs throughout.
- **Recent action:** Price gapped down to 100 on day -20, bounced to 113, and was rejected back to 100.
- **Levels:** Support is about 99, below which there is little structure; resistance is 109 and then 113.
- **Weight 0.25:** The dominant trend is down and the last bounce failed.
- **Change of mind:** A close above 109 would change my view.

## 31a7413202 (AVAX)
Scenarios: up 26, sideways 48, down 26
- **Trend:** The market had two crashes (to about 98 and then 90). Since then it has traded a wide 97–110 range for about 50 days.
- **Recent action:** Day -1 spiked to 108.6 on volume and closed at 100, a rejection that is balanced by the solid base.
- **Levels:** Support is 96 and then 93; resistance is 106–108.
- **Weight 0.5:** The market is range-bound and two-sided.
- **Change of mind:** A close below 96 would make me more cautious.

## 91a8965401 (SOL)
Scenarios: up 24, sideways 54, down 22
- **Trend:** The market crashed to about 81 and recovered to 111. It retraced to about 95 and is now coiling between 97 and 104 on very low volume.
- **Levels:** Support is 96.5 and then 94.6; resistance is 104.3.
- **Weight 0.55:** The bias is neutral to slightly constructive given the higher low at 94.6 compared with 81.
- **Change of mind:** A close below 96.5 would make me cautious.

## 9c4e5b28db (ETH)
Scenarios: up 24, sideways 56, down 20
- **Trend:** The market crashed to about 80 and has made higher lows and higher highs since (80, then 91, then 96). It has held a tight 98–104 range for 30 days with volume drying up.
- **Levels:** Support is 97 and then 96; resistance is 104–106.
- **Weight 0.6:** The base is constructive, with a modest edge to the upside.
- **Change of mind:** A close below 97 would weaken that structure.

## 0faa8349b0 (ADA)
Scenarios: up 26, sideways 38, down 36
- **Trend:** Price action has been very volatile. A crash to 79 was followed by spikes to 114 and 121, and both faded.
- **Recent action:** Price has fallen for 9 straight sessions, from 115 to 100, on light volume, giving back the breakout.
- **Levels:** Support is 96 and then 89; resistance is 104 and then 109.
- **Weight 0.25:** The breakout failed and momentum is negative.
- **Change of mind:** A close above 109 would change my view.

## b85b7bc3ac (DOGE)
Scenarios: up 20, sideways 56, down 24
- **Trend:** The market has been in a long decline from 165 to about 100, with lower highs at 132, then 114, then 108.
- **Recent action:** It is now in a very tight 98–105 range on very low volume, a pause within the downtrend.
- **Levels:** Support is 97–98; resistance is 105.5 and then 108.
- **Weight 0.4:** The bias is neutral to slightly negative.
- **Change of mind:** A close above 105.5 would change my view.

{"13c76926cf (LINK)": 0.7, "4634f69929 (BTC)": 0.55, "4e85e6d40d (XRP)": 0.25, "67721c671c (LTC)": 0.55, "e3a91a992c (DOT)": 0.25, "31a7413202 (AVAX)": 0.5, "91a8965401 (SOL)": 0.55, "9c4e5b28db (ETH)": 0.6, "0faa8349b0 (ADA)": 0.25, "b85b7bc3ac (DOGE)": 0.4}

## Entscheidung 2026-08-23

**Strategy:** All ten windows show the same setup: a long decline, a crash around day −80, a weak base, then a 4–5 day vertical rally to about 100, often with a blow-off wick on day −1. In this setup, a week after an unconfirmed spike, a drop below 97 is about as likely as a rise above 103. I estimate the three scenarios from:
- how stretched the move is,
- whether day −1 left a big upper wick on heavy volume,
- where overhead supply sits.

The weight is 0.5 + (P_up − P_down)/100, rounded to 0.05. When I can't tell which way it breaks, the weight stays near half.

---

### b273c08d96 (XRP)
Scenarios: up 30, sideways 22, down 48

**Trend and structure**
- Downtrend from 101 (day −160) to 65 (day −7).
- Then +52% in five sessions.
- Day −1 was a climactic blow-off: volume 6×, high 111.8, low 90.6, close 96.2.
- Day 0 recovered to 100 on lower volume.

**Key levels**
- The old 94–97 range (days −128 to −100) is now support.
- Resistance is 101.5–105.7, then 111.8.
- The 83 and 72.7 gaps sit far below.

**Weight: 0.3.** This is the most stretched window, and the reversal-type day −1 favours a pullback. Momentum rules out zero.

**Change of mind:** a close above 112 would make me go long; a close below 90.6 confirms the top.

### 3eb563218f (LTC)
Scenarios: up 34, sideways 32, down 34

**Trend and structure**
- Crash from 104 to 78, then recovery to about 90.
- After that, a slow drift between 84 and 88.
- The spike from 85 to 100 is only +18%.
- Day −1 had a wick to 106.1 but closed at 100.3, and day 0 was quieter (volume 1.29).
- Price is reclaiming the pre-crash 99–104 shelf.

**Key levels**
- Support at 96.8, then 91.5.
- Resistance at 104–108.

**Weight: 0.5.** This is the least extended window and it is retaking an old base, so the odds are balanced.

**Change of mind:** above 106.1 I would raise the weight; below 96 I would cut it.

### 8a81a55fb8 (DOGE)
Scenarios: up 30, sideways 25, down 45

**Trend and structure**
- The pre-crash range was 107–110.
- After the crash, price bled to a quiet 73–75 base on dry volume.
- Then +33% in four days.
- Day −1 was a blow-off: high 107.9, low 88.8.

**Key levels**
- Support at 95, then 88.8.
- Supply at 100–108 from the pre-crash zone.

**Weight: 0.35.** The move is extended into heavy overhead supply.

**Change of mind:** a close above 108 or below 95.

### c6cd5c0970 (LINK)
Scenarios: up 38, sideways 25, down 37

**Trend and structure**
- This rally was more constructive than the others.
- The lows rose from 70 to 76 to 82 over days −12 to −5 before the spike.
- 100 is a new 180-day closing high, above the 94.2 peak from day −105.
- Day −1 wicked to 109.3 but held 94.7.

**Key levels**
- Support at 95.3, then 92.6.
- Resistance at 109.3.

**Weight: 0.5.** A breakout to a new high on a stair-step base offsets the stretch.

**Change of mind:** above 109.3 I would raise the weight; below 95.3 I would cut it.

### 182614e839 (ADA)
Scenarios: up 27, sideways 23, down 50

**Trend and structure**
- Steep downtrend from 130 to 61.
- Two earlier spikes failed and fully faded: 64→88 and 74→93.
- This spike went 77→100.
- Day −1 had the widest wick of the set: 113.8 to 92.

**Key levels**
- Supply at 103–110.
- Support at 94, then 92 and 88.

**Weight: 0.25.** The pattern of failed spikes plus the blow-off points down.

**Change of mind:** a close above 114.

### 6e7c73cd03 (ETH)
Scenarios: up 36, sideways 32, down 32

**Trend and structure**
- Spike from 78 to 102.1 (high 103.4) on day −2.
- Then two tight, lower-volume sessions held between 95.6 and 102.7.
- There was no climactic wick, so this looks more like a flag than a top.
- 100 sits near the day −128 high.

**Key levels**
- Support at 95.6, then 90.
- Resistance at 103.4.

**Weight: 0.55.** Orderly digestion near the highs.

**Change of mind:** below 95.6 I would cut; above 103.4 I would add.

### ba184355c5 (DOT)
Scenarios: up 28, sideways 25, down 47

**Trend and structure**
- Long downtrend from 179 to 78.
- Spike from 81 to 101.
- Day −1 hit 111.2 and closed at 99.1.
- Price is now pressing into the post-crash bounce zone (days −77 to −62), which is resistance at 103–112.

**Key levels**
- Support at 94.4, then 90.

**Weight: 0.3.** This is a counter-trend spike into resistance.

**Change of mind:** a close above 111.2.

### 8295135ed7 (AVAX)
Scenarios: up 29, sideways 24, down 47

**Trend and structure**
- Downtrend from 138 to 75.
- Spike from 83 to 103.
- Day −1 was a reversal: high 109.3, low 92, close 98.5.
- Price is into the 101–107 crash-gap supply.

**Key levels**
- Support at 95.6, then 92.

**Weight: 0.3.**

**Change of mind:** a close above 109.3.

### d8a0b9f607 (BTC)
Scenarios: up 30, sideways 42, down 28

**Trend and structure**
- Spike from 83 to 100.8.
- Then two quiet inside days (volume 1.05 and 0.87) with no blow-off.
- This window's normal volatility is low, so the 97–103 band holds more probability than elsewhere.
- 100 is the middle of the old 94–106 pre-crash range.

**Key levels**
- Support at 97.2.
- Resistance at 102.3, then 106.

**Weight: 0.5.**

**Change of mind:** below 97.2 I would cut; a close above 102.3 I would add.

### d1c5997d9d (SOL)
Scenarios: up 30, sideways 27, down 43

**Trend and structure**
- Crash from 86 to 63.
- A rally to 86 faded back to 75–80.
- Then a spike from 80 to 98.
- Day −1 was a blow-off: high 107.7, low 91.9.

**Key levels**
- Resistance at 101–103 (the day −105 high), then 107.7.
- Support at 96, then 91.9.

**Weight: 0.35.**

**Change of mind:** above 107.7 or below 91.9.

---

{"b273c08d96 (XRP)": 0.3, "3eb563218f (LTC)": 0.5, "8a81a55fb8 (DOGE)": 0.35, "c6cd5c0970 (LINK)": 0.5, "182614e839 (ADA)": 0.25, "6e7c73cd03 (ETH)": 0.55, "ba184355c5 (DOT)": 0.3, "8295135ed7 (AVAX)": 0.3, "d8a0b9f607 (BTC)": 0.5, "d1c5997d9d (SOL)": 0.35}

## Entscheidung 2026-08-30

## Strategy

All ten windows share the same broad structure. Each had a sharp capitulation near day −86, then a base, then a high-volume breakout around days −11 to −8. Since then there has been a consolidation, and day 0 is a wide-range down day closing at 100.

My rule rewards breakouts that are holding as a tight flag with intact higher lows, and penalizes blow-off spikes that have since printed a series of lower highs and given back much of the move. The weight is 0.5 + (up − down)/40, clamped to [0, 1] and rounded to 0.05.

---

### 0077234ec2 (SOL)
Scenarios: up 38, sideways 32, down 30

- **Read:** Long decline from about 95 to a 60 low. It recovered to an 80 area, then based at 72–76 on drying volume. The breakout from about 75 ran to 108.7 (day −3).
- **Structure:** The pullback lows are rising (86 → 93.7 → 100.5 → 98.6). Day 0 rejected 105.6 but held above about 98.5. Support is 93–95; resistance is 108–109.
- **Weight:** 0.7. The trend of higher lows is still intact.
- **Change my mind:** a close below 93.

### 70e5218ca1 (ETH)
Scenarios: up 38, sideways 36, down 26

- **Read:** The base was 77–80, tight with very low volume. It gapped to 93, then ran to 106.
- **Structure:** For 8 days it has flagged in a tight 99–106 range. Day 0 tested the flag low (98.8 vs 98.7) and held. Volume during the flag is fading, which is constructive. Support is 98.5; resistance is 106.
- **Weight:** 0.8. This is a clean flag above the breakout.
- **Change my mind:** a close below 97.

### 97f9eb4430 (ADA)
Scenarios: up 25, sideways 30, down 45

- **Read:** Earlier, a breakout to 109.9 (day −24) failed and faded back to 90.
- **Structure:** The new spike reached a 134 intraday blow-off on 3× volume and has since printed a steady run of lower closes (117 → 100). That is a 25% give-back from the high. Day 0 broke to 98.3. The breakout zone and gap sit at 90–97, an obvious magnet.
- **Weight:** 0.0. This is a failed blow-off, and the pattern repeats an earlier failure in the same window.
- **Change my mind:** a close above 111.

### 58c04818e3 (DOT)
Scenarios: up 26, sideways 32, down 42

- **Read:** Primary downtrend from about 200 to 92. The spike to a 126 intraday high has faded with lower highs (114.8 → 113.3 → 107.6 → 103.7 → 100).
- **Structure:** Old resistance at 104–106 is now overhead. The base and gap are at 92–96.
- **Weight:** 0.1. The bigger trend is down and the spike is fading.
- **Change my mind:** a close above 108.

### e6f38524db (DOGE)
Scenarios: up 28, sideways 30, down 42

- **Read:** Downtrend from 140 to 85, then a 30-day dead-flat base at 84–86. The spike reached 122.9.
- **Structure:** Closes since then have stepped down (113.9 → 108.6 → 103.9 → 100). Day 0 low was 98.5. Below that sits an air pocket to 90 and then the 86 base.
- **Weight:** 0.15. This looks like spike distribution.
- **Change my mind:** a close above 109.

### fdaaf464be (BTC)
Scenarios: up 38, sideways 40, down 22

- **Read:** The base was 80–84. A measured rally on solid volume took it to 100.8, with no blow-off wick.
- **Structure:** It has flagged in a tight 99–104 range for 8 days. Day 0 was an inside bar on low volume (0.53). The prior range highs at 105–107 are the next target. Support is 99.
- **Weight:** 0.9. This is the cleanest continuation setup of the ten.
- **Change my mind:** a close below 97.

### cb3e7fc80a (AVAX)
Scenarios: up 33, sideways 34, down 33

- **Read:** The base was a choppy 87–96 range. The spike reached 116.9, then the market consolidated at 101–108 with a mild lower-high drift.
- **Structure:** The old range top at 97–100 should act as support. Resistance is 108.
- **Weight:** 0.5. The evidence is balanced.
- **Change my mind:** a close below 96 (go flat) or above 108 (go long).

### 863b2dabc2 (XRP)
Scenarios: up 28, sideways 30, down 42

- **Read:** A grinding downtrend from 85 to 73 was followed by an explosive move on 4–6× volume to a 125 high. That looks like climactic news.
- **Structure:** Closes since then show lower highs (112 → 107 → 102.9 → 100). The gap down to 81–93 is largely unfilled.
- **Weight:** 0.15. Climactic volume plus fading closes argues against holding.
- **Change my mind:** a close above 108.

### 2ede2915f0 (LINK)
Scenarios: up 36, sideways 32, down 32

- **Read:** The base was 73–75. There was a first leg to 85 (days −19 to −15), then a second leg to 113.
- **Structure:** It has held a 99–108 range, with a bounce to 107 at day −3. Day 0 slipped marginally below the range at 98.6. Support is 95–98; resistance is 108.
- **Weight:** 0.6. The staircase advance is mildly constructive.
- **Change my mind:** a close below 96.

### 34b7b78674 (LTC)
Scenarios: up 32, sideways 34, down 34

- **Read:** The medium-term trend is up, with higher lows at 82, 90.5 and 92. The breakout reached 115.7.
- **Structure:** Since then there have been 9 days of steadily lower closes (110.9 → 100). Price is now retesting the prior highs at 99–100, where the breakout level should act as support. Resistance is 105–110.
- **Weight:** 0.45. The retest is constructive, but the downward drift has not stopped yet.
- **Change my mind:** a close below 97 (go flat) or above 105 (go long).

---

{"0077234ec2 (SOL)": 0.7, "70e5218ca1 (ETH)": 0.8, "97f9eb4430 (ADA)": 0.0, "58c04818e3 (DOT)": 0.1, "e6f38524db (DOGE)": 0.15, "fdaaf464be (BTC)": 0.9, "cb3e7fc80a (AVAX)": 0.5, "863b2dabc2 (XRP)": 0.15, "2ede2915f0 (LINK)": 0.6, "34b7b78674 (LTC)": 0.45}

## Entscheidung 2026-09-06

**Strategy.** I estimate the day +7 scenarios from three things: the trend structure, where price sits against the main swing levels, and how volume confirms moves. I then set weight = 0.5 + 1.5 × (P(up) − P(down)), clipped to the range 0 to 1 and rounded to the nearest 0.05. When the up and down odds are close the weight stays near half, and it moves toward fully long only when the upside clearly dominates.

---

### 349d5aa253 (DOT)
Scenarios: up 35, sideways 40, down 25
- **Read:** The series fell for a long time, from about 155 to a low near 74 at day −19. A high-volume thrust then reached 105.4 at day −15 and was rejected. The pullback held at 82.5 to 83.7, and since then the lows have been rising (85.6, 86.0, 90.3). Day 0 is a strong +6.8% bar on 1.67× volume that closed at 100, near its 101.3 high.
- **Levels:** resistance 101 to 105.4, support 90 and then 83.7.
- **Weight 0.65:** The bottoming structure looks constructive, but the 105 spike high is overhead and much higher levels (120 and above) are still in a broader downtrend.
- **Change my mind:** a close below 90.

### 944dbc6555 (SOL)
Scenarios: up 37, sideways 43, down 20
- **Read:** The series crashed at day −93 and based between 67 and 73 for about two months. A strong volume-backed breakout followed, peaking at 103.8 at day −10. The pullback held at 91.4, and price is back at 100. The pre-crash range (77 to 92) has been recovered, so price sits near the top of the whole 180-day window.
- **Levels:** resistance 103.8, support 94 and then 91.4.
- **Weight 0.75:** Of all the windows, this one has the cleanest trend reversal.
- **Change my mind:** a close below 91.

### 7af7fc92ef (BTC)
Scenarios: up 33, sideways 47, down 20
- **Read:** After the breakout from the 78 to 81 base, price has spent two weeks in a tight range between 95 and 101.4. Today's volume is light (0.53×). The prior swing highs at 101.4 to 103.1 sit just above, so a range break could run, but the most likely outcome is that the coil continues.
- **Levels:** resistance 101.4 to 103.1, support 95 to 96.
- **Weight 0.70**
- **Change my mind:** a close below 94.9.

### 59340a23bb (ADA)
Scenarios: up 33, sideways 37, down 30
- **Read:** This is the most volatile window. The spike wick reached 115.7 but closed at 101. Pullbacks went to 84.8, and the bars have been whipsawing (99 → 94.6 → 97.7 → 100). Resistance is heavy at 101.7 to 104.4, and the higher lows are rough.
- **Levels:** resistance 101.7 to 104.4, support 93.6 and then 85.
- **Weight 0.55:** The two-way risk is close to balanced.
- **Change my mind:** a close below 93.

### ada50fe1d7 (XRP)
Scenarios: up 32, sideways 43, down 25
- **Read:** A blow-off spike to 119.4 on 6× volume closed back near 103, which is a supply wick. Since then price has drifted between 92 and 104. It is now at 100 on fading volume, inside the pre-crash range of 93 to 104.
- **Levels:** resistance 104.2 and then 108.9, support 94 and then 92.
- **Weight 0.60**
- **Change my mind:** a close below 92.

### 4ab4527ea2 (ETH)
Scenarios: up 35, sideways 45, down 20
- **Read:** There was a gap-like breakout from the 74 to 76 base, followed by a sideways range between 93.7 and 102. Price is now pressing the top of that range at 100, which is above the 180-day pre-crash highs near 96 to 98. The highs are flat and the lows are firm.
- **Levels:** resistance 101.3 to 102.1, support 94 to 95.
- **Weight 0.70**
- **Change my mind:** a close below 93.5.

### c4f59a19f3 (AVAX)
Scenarios: up 35, sideways 40, down 25
- **Read:** A spike to 105.2 was rejected to 94.8. The pullback low was 88.7, and since then the lows have risen to 89.0 and then 93.3. Today closed firmly at 100. The pre-crash levels (113 and above) are far overhead, and the spike high is the next obstacle.
- **Levels:** resistance 105.2, support 93 and then 88.7.
- **Weight 0.65**
- **Change my mind:** a close below 89.

### c72500ae54 (LINK)
Scenarios: up 38, sideways 37, down 25
- **Read:** The 54 to 67 base broke out, and day 0 delivered a +9.8% close at 100 on 1.70× volume. That is a new closing high above the 95.4 spike wick and well above the pre-crash range of 68 to 81. The trend is strong, but price is short-term extended (+19% in three days), so a pullback toward 91 to 95 is plausible.
- **Levels:** support 95.4 and then 91, no overhead supply in the window.
- **Weight 0.70**
- **Change my mind:** a close below 91.

### 67f7966915 (LTC)
Scenarios: up 36, sideways 42, down 22
- **Read:** Day −1 was a +7.8% bar on 2.3× volume, and day 0 held it at 100, just under the 100.9 spike high. The pullback from the spike was shallow, bottoming at 86.2. The swing highs at 105 to 110 are the next resistance.
- **Levels:** resistance 100.9 and then 105 to 110, support 92 and then 86.2.
- **Weight 0.70**
- **Change my mind:** a close below 92.

### 6e56e73ae3 (DOGE)
Scenarios: up 32, sideways 40, down 28
- **Read:** Price has been rejected twice from above: the spike wick to 110.9, then the day −1 wick to 104.7, which closed back at 98.6. The range runs from 88 to 105. The pre-crash supply at 110 to 127 sits well above, and the upper wicks point to sellers.
- **Levels:** resistance 104.7 and then 110.9, support 92 and then 88.
- **Weight 0.55**
- **Change my mind:** a close below 88.

---

{"349d5aa253 (DOT)": 0.65, "944dbc6555 (SOL)": 0.75, "7af7fc92ef (BTC)": 0.7, "59340a23bb (ADA)": 0.55, "ada50fe1d7 (XRP)": 0.6, "4ab4527ea2 (ETH)": 0.7, "c4f59a19f3 (AVAX)": 0.65, "c72500ae54 (LINK)": 0.7, "67f7966915 (LTC)": 0.7, "6e56e73ae3 (DOGE)": 0.55}

## Entscheidung 2026-09-13

**Strategy:** I look at trend, base, breakout and pullback structure, and at where support and resistance sit on the 100 scale. From these I estimate the probabilities for day +7. The weight is clamp((up − down + 20) / 40, 0, 1), rounded to the nearest 0.1, so a symmetric outlook gives 0.5.

---

### 27b84e9d81 (DOGE)
Scenarios: up 35, sideways 33, down 32

- **Read:** The price fell from 120 to a 50-day base at 84–90. It broke out at day −25 to a 122 wick, retested 97–100, then made a 115.5 wick on day −8. It has since faded back to 100 on low volume (0.39 and 0.48).
- **Levels:** Higher lows hold at 97.2, 99.9 and 99.6. Resistance is 110–111, then 115.
- **Weight 0.6:** The breakout is intact and support is still holding, but momentum is fading.
- **Change my mind:** a close below 97.

### 9e1f28f4ba (ADA)
Scenarios: up 34, sideways 32, down 34

- **Read:** This had a deeper crash to 68, then a breakout wick to 127. Lower highs followed at 111.6 and 114.1.
- **Levels:** Support is 93–94 (day −14 low). Price sits in the middle of a 93–111 range.
- **Weight 0.5:** There is no edge either way.
- **Change my mind:** a close above 108 would raise the weight; a close below 93 would cut it to 0.

### 256729202a (LINK)
Scenarios: up 36, sideways 32, down 32

- **Read:** The base was at 64–77, followed by a breakout to 112.6. Day −6 made a higher high at 122.2, the only window with a clean higher high. It then gave back 18% in four days to 100.
- **Levels:** Support is 97.4–98.3. Resistance is 108–109, then 114.
- **Weight 0.6:** The trend still makes higher highs and higher lows, though the latest fade is sharp.
- **Change my mind:** a close below 97.

### beedd69059 (AVAX)
Scenarios: up 34, sideways 34, down 32

- **Read:** The base was at 85–93, followed by a breakout to 114.1. The next high was lower at 112.5. Price is now at 100.
- **Levels:** Support is 96.6–97.6. Resistance is 107.5, then 110.
- **Weight 0.5:** The outlook is roughly balanced (0.55 rounds down).
- **Change my mind:** a close below 96.5, or above 108.

### ffeb2c646e (XRP)
Scenarios: up 30, sideways 34, down 36

- **Read:** The pre-breakout base was weak and still making lower lows at 73.5. A climactic 6× volume spike made a 126.7 wick. Since then the highs keep falling (115.6, 110.6, 108.2, 106.9) while the lows sit near 98. That is a descending triangle into support.
- **Levels:** Support is 97.7–98.0. Resistance is 108.
- **Weight 0.3:** The structure leans toward resolving downward.
- **Change my mind:** a close above 107 would raise the weight; below 97 would take it to 0.

### d25a0a081f (SOL)
Scenarios: up 33, sideways 34, down 33

- **Read:** The base was at 71–78, followed by a breakout. Day −17 made a higher high at 111.4. Lower highs followed at 108.1, 107.8 and 106.5, with lows near 98.1–98.7.
- **Levels:** Support is 98–99. Resistance is 106.5–108.
- **Weight 0.5:** The picture is balanced and the range is tightening.
- **Change my mind:** a close below 97.5, or above 107.

### a09670ab8a (LTC)
Scenarios: up 36, sideways 34, down 30

- **Read:** The base was at 81–89. A first breakout to 103 failed back to 88, but the second push reached 110.6. The low has risen from 88.2 to 96.0, and the closing high from 98.9 to 102.7. Price is back above the 94–97 breakdown zone.
- **Levels:** Support is 96. Resistance is 103, then 110.
- **Weight 0.6:** The structure is improving (0.65 rounds down).
- **Change my mind:** a close below 96.

### 401d76a3cd (DOT)
Scenarios: up 27, sideways 30, down 43

- **Read:** This is a long downtrend from 162 to 75. The first breakout failed at 103. Then came a parabolic spike to 128.5 on 4× volume, which fully reversed to 100 within four days. That looks like a blow-off top with distribution.
- **Levels:** Support is 91–94, then 87. Resistance is 104–106, then 112.
- **Weight 0.1:** Downside risk dominates.
- **Change my mind:** a close back above 106.

### 0701f1eabd (BTC)
Scenarios: up 30, sideways 45, down 25

- **Read:** There was a tight base at 81–87, then an orderly breakout to 105. For three weeks price has held a calm 99–106 range with small daily ranges. Volume is drying up near support.
- **Levels:** Support is 99.0–99.5. Resistance is 104.5–106.
- **Weight 0.6:** The breakout is holding with low volatility.
- **Change my mind:** a close below 97.

### ca4adf2601 (ETH)
Scenarios: up 32, sideways 40, down 28

- **Read:** The base was at 75–78, followed by a breakout to 102.8 on volume. Since then price has consolidated between 95 and 103. A 107.6 wick on day −2 was rejected.
- **Levels:** Lows sit at 95.1, 96.2 and 97.1, with support at 95–97. Resistance is 103, then 107.6.
- **Weight 0.6:** The consolidation is constructive.
- **Change my mind:** a close below 95.

---

{"27b84e9d81 (DOGE)": 0.6, "9e1f28f4ba (ADA)": 0.5, "256729202a (LINK)": 0.6, "beedd69059 (AVAX)": 0.5, "ffeb2c646e (XRP)": 0.3, "d25a0a081f (SOL)": 0.5, "a09670ab8a (LTC)": 0.6, "401d76a3cd (DOT)": 0.1, "0701f1eabd (BTC)": 0.6, "ca4adf2601 (ETH)": 0.6}

## Entscheidung 2026-09-20

**Strategy.** I read each window's trend and structure: where price sits against its recent range, whether highs and lows are rising, and how fast it moved into the current level. From that I estimate the three day +7 scenarios. The weight is `0.5 + (up − down)/40`, clipped to 0–1 and rounded. Wide, whippy ranges stay near 0.5, clean breakouts from tight bases get more, and blow-off moves get less.

## 9a9280fb61 (BTC)
Scenarios: up 33, sideways 40, down 27

- **Trend:** Up. Price rebuilt from the 72–80 base into a sharp rally on day -32.
- **Structure:** Since then it has ranged 92.4–101.4, with lows holding around 92–93.
- **Now:** Day -2 lifted price to 100, near the top of the range, on modest volume.
- **Key levels:** 101.4 (range high), 102.1 (180-day high), 92.4 (support).
- **Weight 0.65:** The trend is up and price is near a breakout, but resistance at 101–102 is overhead.
- **Change my mind:** A close below 93.

## 9f36138f8a (ADA)
Scenarios: up 38, sideways 26, down 36

- **Trend:** Very volatile, with daily swings of 4–5%. It bottomed near 61 and spiked to 113.4 on day -29.
- **Structure:** Since then it has ranged 83.5–102. On day -2 it jumped from 89 to 98.5 and now sits at 100.
- **Key levels:** 102–103 (resistance), 84 (support).
- **Weight 0.55:** The direction is barely tilted and volatility is high, so the position stays near neutral.
- **Change my mind:** A close below 89.

## 50d04cb61c (LINK)
Scenarios: up 38, sideways 30, down 32

- **Trend:** Up, with higher lows (57 → 65 → 85).
- **Structure:** Price peaked at 109.3 on day -13, pulled back to 84.8, and has recovered to 100.
- **Key levels:** 101.4 / 109 (overhead), 85 (support).
- **Weight 0.65:** The uptrend is intact and the pullback was bought.
- **Change my mind:** A close below 86.

## 254e09ab11 (DOT)
Scenarios: up 36, sideways 24, down 40

- **Move:** A blow-off spike to 113 on day -12 (volume about 4x) collapsed to 82.3.
- **Now:** Price has bounced back to 100 on heavy, churning volume (2.07). Day 0 ranged from 94.4 to 103.3.
- **Structure:** The base a month ago was 66–80, so price is extended and the structure is unstable.
- **Key levels:** 103.3 / 113 (overhead), 88 / 82 (support).
- **Weight 0.4:** Downside risk slightly outweighs upside.
- **Change my mind:** A close above 104.

## 3156d7691f (SOL)
Scenarios: up 38, sideways 37, down 25

- **Trend:** A cleaner uptrend, from 67 to 98 by day -24.
- **Structure:** Price consolidated between 86 and 96, then broke out to 101.4 on day -2 on about 2x volume. It is holding 100, the highest level since day -132.
- **Key levels:** 102.8 (breakout high), 96 / 92 (support).
- **Weight 0.8:** The breakout is holding.
- **Change my mind:** A close below 92.

## 9800319db4 (AVAX)
Scenarios: up 35, sideways 20, down 45

- **Move:** A parabolic run from 67 to 72.5, then 89, then 100 in three days, on volume of 2.5x, 3.9x and 6.1x. Day 0 ranged 83.4–101.4.
- **Context:** Price broke out of a long 55–72 base and is now at levels last seen 165 days ago.
- **Risk:** It is extremely extended, so a retrace toward 85–90 is likely, although momentum could continue.
- **Weight 0.25:** Reversal risk dominates.
- **Change my mind:** Consolidation that holds above 95 for several days.

## 0623fe7ac1 (XRP)
Scenarios: up 32, sideways 36, down 32

- **Move:** A spike to 120.5 on day -29, followed by a wide, whippy range of 88.4–108.
- **Volume:** There was heavy two-way volume, including a failed rally to 106 and a drop to 89.7 on day -5.
- **Now:** Price is at 100, mid-range, with no edge.
- **Key levels:** 103–106 (resistance), 88–91 (support).
- **Weight 0.5:** No directional edge.
- **Change my mind:** A close above 106 (bullish) or below 91 (bearish).

## c91b120a36 (ETH)
Scenarios: up 35, sideways 42, down 23

- **Move:** A gap rally on day -32 from 72 to 95.
- **Structure:** A month of tight consolidation between 89 and 97, followed by a clean push to 100, above the range top.
- **Volume:** Low on the move, so this is orderly accumulation.
- **Key levels:** 100.9 (wick high), 96–97 (breakout level), 89 (range low).
- **Weight 0.8:** A clean breakout from a tight range.
- **Change my mind:** A close back below 94.

## 618e6620da (DOGE)
Scenarios: up 32, sideways 38, down 30

- **Context:** The 180-day high is 135, and price fell to about 78 before the day -32 rally.
- **Move:** The rally spiked to 115.5 and was followed by a 89.7–109 range.
- **Now:** Price is at 100, mid-range, with mild support at 92–94.
- **Key levels:** 104.6 / 109 (resistance), 89.7 (support).
- **Weight 0.55:** Neutral, with a slight upward tilt.
- **Change my mind:** A close below 92.

## db2bec49db (LTC)
Scenarios: up 35, sideways 40, down 25

- **Trend:** Steadier than the others. It rallied from 75 to 90.5, then based at 81–94 with rising lows (80.7 → 85.5).
- **Now:** It is pushing to 99–100 on above-average volume.
- **Key levels:** 101.2 (day -13 high), 103 (180-day high), 91 / 85.5 (support).
- **Weight 0.75:** Rising lows and a push toward the highs.
- **Change my mind:** A close below 90.

{"9a9280fb61 (BTC)": 0.65, "9f36138f8a (ADA)": 0.55, "50d04cb61c (LINK)": 0.65, "254e09ab11 (DOT)": 0.4, "3156d7691f (SOL)": 0.8, "9800319db4 (AVAX)": 0.25, "0623fe7ac1 (XRP)": 0.5, "c91b120a36 (ETH)": 0.8, "618e6620da (DOGE)": 0.55, "db2bec49db (LTC)": 0.75}

## Entscheidung 2026-09-27

**Strategy:** I treat each window as a trend-and-volatility read. I estimate the chance of a ±3% move by day +7 from the current trend structure (higher highs and lows versus lower highs), where price sits relative to key levels, and how volatile the window has been. The weight is set mechanically as w = 0.5 + 1.5 × (P(up) − P(down)), clipped to the range 0 to 1. One week is mostly noise, so the weights stay moderate unless the structure is clear.

## a897e016bd (SOL)
Scenarios: up 40, sideways 30, down 30
- **Read:** A strong uptrend from 61 (day −41) to new highs around 100–102, with higher lows at 79, 91 and 92.
- **Daily range:** About 2.5%, so a ±3% weekly move is likely either way.
- **Risk:** The trend is extended, but there is no reversal signal yet.
- **Weight:** 0.65.
- **Change my mind:** A close below 92 (the day −4 low).

## b5c88e78e8 (DOGE)
Scenarios: up 33, sideways 30, down 37
- **Read:** The 180-day structure is lower highs from 120.
- **Recent action:** A blow-off to 109 on heavy volume at day −5, which reversed to 94 within a day. Price now sits at 100, mid-range between 94 and 109.
- **Risk:** Very volatile, and the spike failed, so the down side gets a slight edge.
- **Weight:** 0.44.
- **Change my mind:** Above 104 I would get more constructive; below 94 I would go flat.

## fb07f0d5bf (ETH)
Scenarios: up 37, sideways 36, down 27
- **Read:** A clean uptrend from 71 to 100, with a tight base between 99 and 103.
- **Volume:** Fading volume, which looks like healthy consolidation under the 104.4 high.
- **Weight:** 0.65.
- **Change my mind:** A close below 96.7.

## 4b349c4212 (ADA)
Scenarios: up 36, sideways 28, down 36
- **Read:** A sharp rally from 75.7 to 104, but with wide daily swings (for example, 103 to 91.5 at day −4).
- **Longer view:** The 180-day highs at 107–113 cap the picture, and history shows repeated failed spikes.
- **Weight:** 0.50.
- **Change my mind:** Below 91.5 is bearish; above 104 is bullish.

## ccc53bdb2e (XRP)
Scenarios: up 35, sideways 30, down 35
- **Read:** A spike to 112 at day −36 was followed by a high-volatility range between 83 and 109.
- **Current position:** Price is at 100, mid-range, with heavy two-way volume.
- **Weight:** 0.50.
- **Change my mind:** Above 107.5 or below 95.7.

## b35680795c (LINK)
Scenarios: up 40, sideways 30, down 30
- **Read:** Consistent higher lows (77.6 → 86 → 98.9) and new highs at 103.4.
- **Volume:** Volume confirmed the push at day −2.
- **Weight:** 0.65.
- **Change my mind:** A close below 94.

## d2953458f2 (AVAX)
Scenarios: up 37, sideways 30, down 33
- **Read:** An event-driven gap from 70 to 104 on 5.7× volume (days −8 to −7).
- **Since then:** Price pulled back to 91.4 and has recovered to 100. The range since the gap is 91 to 108.
- **Interpretation:** The breakout held, but volatility is high.
- **Weight:** 0.56.
- **Change my mind:** Below 91.4.

## 9df3c66360 (DOT)
Scenarios: up 38, sideways 25, down 37
- **Read:** A spike to 101 at day −19, a full retrace to 74, then a V-shaped recovery to 100 with a higher low at 85.
- **Resistance:** Price is testing 101–103, with older highs at 106 and 112 above that.
- **Risk:** Extremely volatile, with little directional edge.
- **Weight:** 0.52.
- **Change my mind:** A close above 103 is bullish; below 86 is bearish.

## be3ddb11e8 (BTC)
Scenarios: up 33, sideways 45, down 22
- **Read:** A smooth, low-volatility uptrend, with a breakout to 103.5 that is now basing very tightly between 99.6 and 100.8 on light volume.
- **Interpretation:** The trend supports the long side, and the low volatility favours a sideways week.
- **Weight:** 0.67.
- **Change my mind:** A close below 98.

## 06b33648fb (LTC)
Scenarios: up 38, sideways 32, down 30
- **Read:** A 6.7× volume breakout at day −3, from 87 to 101, which is a new 180-day high (the prior high was 85).
- **Hold:** Price has held between 97 and 105 since.
- **Risk:** A gap-fill toward 87 is possible.
- **Weight:** 0.62.
- **Change my mind:** A close below 96.5.

{"a897e016bd (SOL)": 0.65, "b5c88e78e8 (DOGE)": 0.44, "fb07f0d5bf (ETH)": 0.65, "4b349c4212 (ADA)": 0.5, "ccc53bdb2e (XRP)": 0.5, "b35680795c (LINK)": 0.65, "d2953458f2 (AVAX)": 0.56, "9df3c66360 (DOT)": 0.52, "be3ddb11e8 (BTC)": 0.67, "06b33648fb (LTC)": 0.62}
