# E-023: was die KI gedacht hat (Set A)

Volle Antwort des Deciders pro Entscheidungswoche, unverändert. Er sah weder Datum noch Coin-Namen; die Namen in Klammern sind erst danach eingesetzt. Gesendeter Prompt und Daten: runs/<set>/<woche>/requests.json.

## Entscheidung 2026-07-05

## 1. Strategy

All ten windows are in a 180-day downtrend, with price roughly halved, a capitulation leg around days -33 to -30, and a bounce back to 100 in the last few days. So the default is a small position.

I add weight when the bounce has built higher lows or reclaimed the post-crash range high. I cut weight when the recent lows are still lower lows or when the basis percentile is high (above about 80), because that means leveraged longs are crowded. I add a little when the basis is low.

## 2. Windows

### 5cd9deec18 (AVAX)
- **Read:** The downtrend runs from 210 to 100. Price crashed from 129 to 97 on days -33 to -30, then flushed to 82 on day -16 on heavy volume. Since then it has made higher lows at 86, 92 and 95.
- **Levels:** Price is now pressing the 102–103 bounce highs. The 50-day average is around 110 and still overhead. Basis is 53, which is neutral.
- **Weight:** 0.25. The base is improving, but the trend is still down.
- **Change my mind:** Below 92 I go to 0. A daily close above 103 adds weight.

### b20d50a3ed (ADA)
- **Read:** This is the deepest fall, from 221 to a low of 73 on day -11. It then had a violent four-day squeeze from 76 to 101 on 2× volume.
- **Levels:** Momentum is strong, but the move is overextended and runs into the 94–97 congestion area from days -21 to -20. Basis is 74, so the rally is already getting crowded.
- **Weight:** 0.3, as a momentum position that I am not chasing.
- **Change my mind:** Below 92 (the gap fill) I exit. Holding above 105.5 adds weight.

### de5b1106b8 (BTC)
- **Read:** The decline is shallower, from 147 to 100. It made a low of 92.9 on day -30 and a retest low of 90.8 on day -4. That is roughly a double bottom.
- **Levels:** Resistance is at 104–106 (day -20). The 50-day average is around 112. Basis is 92, which is crowded.
- **Weight:** 0.2. The structure is acceptable, but the basis is a headwind.
- **Change my mind:** Below 94 I go to 0. Above 106 adds weight.

### 22071d7d55 (LTC)
- **Read:** The downtrend runs from 183 to 100. It made a low of 88.4 on day -29 and a marginally lower low of 85.7 on day -10. Price has now rallied to the top of the post-crash range (100.7 against 101.2 on day -20).
- **Levels:** Basis is 30, which is favorable because longs are not crowded.
- **Weight:** 0.35. A breakout attempt with cheap positioning.
- **Change my mind:** Below 93 I go to 0. A close above 101.5 adds weight.

### abb5f568a0 (LINK)
- **Read:** The downtrend runs from 174 to 100. It has a clean double bottom at 86.8 (day -29) and 86.9 (day -10), with a steady climb since.
- **Levels:** Resistance is at 106.7 (day -20). Basis is 68.
- **Weight:** 0.3.
- **Change my mind:** Below 93 I exit. Above 107 adds weight.

### 274987e703 (XRP)
- **Read:** The downtrend runs from 199 to 100. The lows are 90.7 (day -29) and 87.2 (day -10), a slightly lower low. A wick to 111.8 on day -20 was rejected.
- **Levels:** Price is mid-range at 100. Basis is 36, which is supportive.
- **Weight:** 0.3.
- **Change my mind:** Below 93 I go to 0. Above 103, and later 112, adds weight.

### 98d8a7210f (SOL)
- **Read:** The downtrend runs from 173 to 100. It made a low of 73.7 (day -29) and a clearly higher low of 78.5 (day -10). Price then broke above the post-crash high of 93.3 and has reclaimed the full pre-crash level of about 100 (day -34).
- **Levels:** This is the best structure of the set. The 50-day average is around 103. Basis is 55.
- **Weight:** 0.5.
- **Change my mind:** Below 94 (failed breakout) I cut to 0.2. Above 103 adds weight.

### ce237b240d (ETH)
- **Read:** The downtrend runs from 185 to 100. It has a double bottom at 84.3 and 84.7 and is now near 103.6 resistance (day -20).
- **Levels:** Basis is 99, an extreme reading for longs paying up, so I expect a pullback or squeeze risk.
- **Weight:** 0.15.
- **Change my mind:** Below 94 I go to 0. A close above 104 with the basis cooling adds weight.

### 069b406635 (DOT)
- **Read:** The downtrend runs from 254 to 100 and is still printing lower highs (118.8 on day -20) and lower lows (100.3 on day -29, then 90.2 on day -7).
- **Levels:** The bounce is so far only a lower high in the making. Basis is 86.
- **Weight:** 0.15.
- **Change my mind:** Below 93 I go to 0. Above 105 starts to break the lower-high sequence.

### e09dc87ec9 (DOGE)
- **Read:** A failed recovery: price rallied to 152 (day -52) and then rolled over hard. The lows are 99.7 (day -29) and 89.3 (day -5), a lower low. Price now sits under 105–107 resistance.
- **Levels:** Basis is 88.
- **Weight:** 0.1.
- **Change my mind:** Below 94 I go to 0. Above 107 adds weight.

## 3. Weights

{"5cd9deec18 (AVAX)": 0.25, "b20d50a3ed (ADA)": 0.3, "de5b1106b8 (BTC)": 0.2, "22071d7d55 (LTC)": 0.35, "abb5f568a0 (LINK)": 0.3, "274987e703 (XRP)": 0.3, "98d8a7210f (SOL)": 0.5, "ce237b240d (ETH)": 0.15, "069b406635 (DOT)": 0.15, "e09dc87ec9 (DOGE)": 0.1}

## Entscheidung 2026-07-12

**Strategy:** I go long only in proportion to evidence of a base. That evidence is a higher low after the capitulation leg, plus price holding near or above its post-crash range high. I cut weight when the 6-month trend is still clearly down, when recent rallies failed, or when the basis percentile is very high, meaning leveraged longs are crowded. All weights stay small unless price reclaims the structure that broke down around day -40.

## 878e8503e8 (LTC)
- **Read:** Long downtrend from 177. The 115–137 range held for months, then broke at day -40. Lows are 92.1 (-36) and then 89.3 (-18), which is a lower low. The bounce stalled at 104.9 (-7), and price has drifted back to 100 on fading volume.
- **Basis:** 75, so longs are somewhat crowded.
- **Weight:** 0.15. There is no confirmed base and the trend is down.
- **Change my mind:** A close above 105 raises the weight. A break below 89 takes it to 0.

## 157d36d466 (DOGE)
- **Read:** Down from 204. The rally to 163 (-59) fully reversed. Lows keep falling: 106.8, then 98.3, then 95.6. The bounce capped at 109.2 and price is now 100, with volume very light.
- **Basis:** 78.
- **Weight:** 0.10, because of the clean lower-low structure.
- **Change my mind:** A close above 109.

## c9533e8f19 (BTC)
- **Read:** Down from 150, with a peak at 129.9 (-67). Lows went 92.7 (-37), then 90.6 (-12), a lower low. Price has recovered to 100 but sits right under the 101–101.5 short-term highs.
- **Basis:** 63.
- **Weight:** 0.15.
- **Change my mind:** A close above 101.5, then 105.5, adds weight. Below 90.6 takes it to 0.

## fa016f1424 (SOL)
- **Read:** Down from 189. Lows went 78.2 (-36), then 83.3 (-17), a higher low. Price then broke above the 98.9 swing high and reached 109.2 (-8). It has pulled back to 100 and is testing the breakout zone at 98–99.
- **Basis:** 43, which is neutral.
- **Weight:** 0.35. This is the best structure in the set.
- **Change my mind:** A close above 109 raises the weight. Below 98 cuts it. Below 83 takes it to 0.

## b906eef28f (XRP)
- **Read:** Down from 199. Lows went 96.7, then 92.9, a lower low. The rally to 109.1 faded back to 100.
- **Basis:** 100, the maximum crowding of leveraged longs.
- **Weight:** 0.05.
- **Change my mind:** A close above 109 with the basis cooling.

## fe6b95bcc7 (LINK)
- **Read:** Down from 176. There is a double bottom at 87.5/87.7 (-36/-17). The rally reached 102.2 and the pullback held at 94.1 (-4), a higher low. Price is now 100.
- **Basis:** 26, so longs are not crowded.
- **Weight:** 0.30.
- **Change my mind:** A close above 102.3 confirms the base and raises the weight. Below 94 cuts it.

## e224646c82 (ADA)
- **Read:** Down from 260. Lows went 91.7, then 85.3, a lower low. A spike to 123.4 (-8) was fully given back to 100, a failed breakout.
- **Basis:** 2, meaning sentiment is washed out. That gives some squeeze potential, but the price action is bearish.
- **Weight:** 0.10.
- **Change my mind:** A close above 108 raises the weight. Below 85 takes it to 0.

## 132bacab33 (AVAX)
- **Read:** Down from 230. Lows went 97.1 (-36), then 88.7 (-23). The bounce reached 111.1 (-8) and then made lower highs. Day 0 printed a low of 98 on rising volume.
- **Basis:** 42.
- **Weight:** 0.20.
- **Change my mind:** A close above 106.7 raises the weight. Below 98 reduces it.

## 71982bfbe4 (ETH)
- **Read:** Down from 184. There is a double bottom at 83.3/83.7. The rally reached 101.5, the pullback made a higher low at 94.8 (-4), and price now closes near the top of the range at 100.
- **Basis:** 69.
- **Weight:** 0.30.
- **Change my mind:** A close above 101.5 raises the weight. Below 94.8 cuts it.

## 124c1fcefd (DOT)
- **Read:** Down from 270. Lows went 104.7, then 95.3, a lower low. A spike to 106 (-2) faded immediately.
- **Basis:** 97, so longs are crowded.
- **Weight:** 0.05.
- **Change my mind:** A close above 106 with the basis easing.

{"878e8503e8 (LTC)": 0.15, "157d36d466 (DOGE)": 0.1, "c9533e8f19 (BTC)": 0.15, "fa016f1424 (SOL)": 0.35, "b906eef28f (XRP)": 0.05, "fe6b95bcc7 (LINK)": 0.3, "e224646c82 (ADA)": 0.1, "132bacab33 (AVAX)": 0.2, "71982bfbe4 (ETH)": 0.3, "124c1fcefd (DOT)": 0.05}

## Entscheidung 2026-07-19

**Strategy:** Every window shows a long decline followed by a capitulation leg about 45 days ago. I only take meaningful long exposure where the post-capitulation base has turned constructive. That means higher lows, a close above the last swing high, and price above the rough 50-day average (about 95–102 in most windows). Basis works as a crowding modifier: a low percentile adds a little to the weight and a high percentile (above 80) trims it.

### 57feef880b (SOL)
Read: the long downtrend from 170 ended in a flush to 78.7 at day -43. There is a higher low at 83.8 (day -24), and the bounce reached 108.4 at day -17. Price has since drifted down to a 96–103 shelf, which is holding. Price sits slightly above the rough 50-day average (about 96). Basis 14 means leverage is not crowded.
Weight 0.5: the base is constructive, but price is mid-range and has not yet reclaimed 104–108.
Change my mind: a close below 96 cuts to 0.1. A close above 104 adds.

### 915d88b96e (DOGE)
Read: the downtrend from 160 has a lower-high, lower-low sequence: 127.7 → 108.4 → 104.1 on the highs and 107.2 → 96.0 on the lows. Price is coiling at 98–104 with falling volume. Price is below the rough 50-day average (about 110). Basis 37 is neutral.
Weight 0.15: there is no evidence of a trend change.
Change my mind: a close above 108 raises it. A close below 96 goes to 0.

### 5eda246389 (XRP)
Read: the flush low was 95.7 (day -43), followed by a lower low at 91.9 (day -23). Lower highs run 117.8 → 107.9 → 103. Price is at 100, roughly at the 50-day average (about 102). Basis 28 is mildly low.
Weight 0.25: the structure is still bearish, but it is stabilising.
Change my mind: a close above 104 goes to 0.5. A close below 96 goes to 0.

### 4a58464b2a (ADA)
Read: the crash ran from 140 to 89 (day -43), with a further low at 83.1 (day -24). A volume thrust then reached 120 (day -15), a higher high than 114 (day -34). That move has fully retraced to 100, though the 93.4 low (day -6) has held. Basis at the 4th percentile is very washed out.
Weight 0.4: the thrust and the cheap basis are positive, but the full retrace shows supply.
Change my mind: a close below 93.4 goes to 0. A close above 106 goes to 0.7.

### 43cb3b53ea (LINK)
Read: a double bottom at 83.4/83.6 (days -43 and -24), followed by higher lows at 84.4, 92.5, 93.0 and 95.5. Day -4 reached 103.0, just above the 102.6 high from day -34, so the base has marginally broken out. Price is above the rough 50-day average (about 94). Basis 67 is elevated but not extreme.
Weight 0.6: the structure is the cleanest uptrend from a base among these windows.
Change my mind: a close below 95.5 goes to 0.2. A close above 103 adds.

### ce3a939ca3 (BTC)
Read: the crash low was 91.4 (day -44), then 89.3 (day -18). The rise since then has higher lows (95.5 at day -6) and reached 101.4 (day -4). The prior swing high of 104 (day -34) is still overhead. Basis 87 means longs are crowded.
Weight 0.45: the structure is constructive, but I trimmed for crowding.
Change my mind: a close below 95.5 goes to 0.1. A close above 104 goes to 0.7.

### 62282146d5 (AVAX)
Read: the capitulation low was 87.9 (day -30), followed by higher lows and a rally to 110.1 (day -15). Since then there are lower highs (105.7, 104.8) and price has faded to 100. Today closed at 100 off a 102.7 high, near the 97.2–98.6 lows. Basis 45 is neutral.
Weight 0.4: there is a higher-low base, but momentum is fading.
Change my mind: a close below 97 goes to 0.1. A close above 105 goes to 0.7.

### a26d5a65fd (ETH)
Read: a double bottom at 80.4/80.8 (days -43 and -23), followed by a steady rally with higher lows (93.5 at day -6) to 104 (day -4). Price is now 100, above the rough 50-day average (about 91). Basis at the 93rd percentile is very crowded.
Weight 0.45: the trend structure is good, but heavy leverage raises flush risk.
Change my mind: a close below 93.5 goes to 0. A close above 104 with the basis cooling goes to 0.7.

### cc10219d95 (DOT)
Read: lows run 102.7 → 99.9 → 97.0 (day -21), and highs fall 110.7 → 109.1 → 106.6. Today was a down day from 102.3 to 100 on above-average volume, with a low of 98.3. Price is sitting at the bottom of the 97–110 range. Basis 46 is neutral.
Weight 0.2: lower highs and pressure on support.
Change my mind: a close below 97 goes to 0. A close above 107 goes to 0.6.

### ccfc93fed9 (LTC)
Read: the low was 83.5 (days -25/-24), followed by higher lows at 87.4, 91.2 and 93.4. Day -1 broke above the 97–98.5 lid on rising volume, reaching 101.7, and today held 99.2 or better. Price is above the rough 50-day average (about 93). Basis 16 means the move is not crowded.
Weight 0.7: a fresh breakout with cheap leverage.
Change my mind: a close below 95 goes to 0.2. A close above 102 adds.

{"57feef880b (SOL)": 0.5, "915d88b96e (DOGE)": 0.15, "5eda246389 (XRP)": 0.25, "4a58464b2a (ADA)": 0.4, "43cb3b53ea (LINK)": 0.6, "ce3a939ca3 (BTC)": 0.45, "62282146d5 (AVAX)": 0.4, "a26d5a65fd (ETH)": 0.45, "cc10219d95 (DOT)": 0.2, "ccfc93fed9 (LTC)": 0.7}

## Entscheidung 2026-07-26

**1. Strategy**

I go long when price has formed higher lows since its post-crash bottom and is now breaking out of its recent range. I cut the weight when the structure still shows lower highs, or when basis is above about 85, which means crowded leveraged longs. A very low basis (washed-out sentiment) counts as a mild plus. Weights run from about 0.25 for a weak setup to 0.7 for a clean breakout with neutral basis.

**2. Windows**

**bd233b8476 (LINK)**
- **Read:** The crash bottomed at 80.7 (day -51), and the retest at 79.4 (day -31) held. Since then highs have risen through 87.8, 90.0 and 97.8. Day 0 closed at 100, above the 99.3 high from day -5. Overhead resistance is 103–106 (the pre-crash shelf), then 110.
- **Weight 0.6:** The trend structure is constructive. Basis at 66 is moderate, and volume on the breakout is light.
- **Change of mind:** below 93.7.

**75e1210d8e (ADA)**
- **Read:** The crash ran from 142 to 89.5. A spike to 120.5 (day -22) fully faded. Price is now in a 93.6–108.9 range and sits in the middle of it. Lows are rising: 83.3, then 93.6.
- **Weight 0.5:** Basis at 4 means sentiment is washed out, which supports a long. But the range has no breakout yet.
- **Change of mind:** below 96. I would add above 109.

**ee6d8ecce9 (LTC)**
- **Read:** Lows came at 84.7 and then 82.1, followed by steady higher lows. Day 0 made a new 50-day high at 100.9, clearing the 100.1–100.6 cap. The next level is 105–109.
- **Weight 0.6:** This is a clean breakout, but basis at 77 is elevated.
- **Change of mind:** below 95.6.

**1328f90224 (AVAX)**
- **Read:** After the crash low of 92.3 came a lower low at 84.2 (day -37). Price recovered to 105.5, then pulled back to 91.0. Day -1 was a high-volume reversal up to 100.5. The range is 91–105.5.
- **Weight 0.45:** Price is mid-range, the swing structure is choppy, and basis is 67.
- **Change of mind:** below 92. Above 105.5 I would raise the weight.

**173eb717bc (ETH)**
- **Read:** The crash low was 77.0 and the retest at 77.4 held. Highs have risen through 92.5, 99.6 and 100.1, and day 0 pushed to 100.6 and closed at 100. Resistance is around 103.
- **Weight 0.7:** This has the cleanest higher-high/higher-low sequence of the set, with neutral basis at 42.
- **Change of mind:** below 94.5.

**d3591924b6 (DOGE)**
- **Read:** The crash went to 105.8, then made a lower low at 94.7. Highs keep falling: 126, 108.2, 102.7, 100.9. Day -3 dropped to 93.2 and price has recovered to 100.
- **Weight 0.25:** The structure is still a downtrend, and basis at 87 is crowded.
- **Change of mind:** above 103.

**bd15750b1a (XRP)**
- **Read:** The crash low was 94.3, followed by a lower low at 90.7. Highs have fallen through 116.2, 106.4 and 104.6. Price is now 100 in a 97–104.6 band.
- **Weight 0.25:** The lower-high sequence is intact, and basis at 94 is extremely crowded.
- **Change of mind:** above 105.

**5b64f99962 (BTC)**
- **Read:** The crash low was 90.4, followed by a slightly lower low at 88.4 (day -25). Price recovered to 102.4 (day -5) and is now 100, under the 102.9–102.4 resistance.
- **Weight 0.45:** The recovery is decent but there is no breakout yet, and basis is 74.
- **Change of mind:** below 97.5. Above 103 I would raise the weight.

**311291b4c6 (SOL)**
- **Read:** The crash low was 78.3. Price rallied hard to 109.4 (day -22), pulled back to 95.6, and is now at 100. The lows are rising: 78, 83.4, 95.6.
- **Weight 0.35:** The structure is fine, but basis at 99 is an extreme crowding signal.
- **Change of mind:** below 95.6.

**c5c8013445 (DOT)**
- **Read:** This is a long decline from 200, with the low at 96 (day -28). Price is now in a 95–109.7 range with falling highs: 109.7, 108.1, 105.6, 105.0. It sits at 100.
- **Weight 0.3:** The primary trend is down and the range keeps compressing lower. Basis is 71.
- **Change of mind:** above 106.

**3. Weights**

{"bd233b8476 (LINK)": 0.6, "75e1210d8e (ADA)": 0.5, "ee6d8ecce9 (LTC)": 0.6, "1328f90224 (AVAX)": 0.45, "173eb717bc (ETH)": 0.7, "d3591924b6 (DOGE)": 0.25, "bd15750b1a (XRP)": 0.25, "5b64f99962 (BTC)": 0.45, "311291b4c6 (SOL)": 0.35, "c5c8013445 (DOT)": 0.3}

## Entscheidung 2026-08-02

**Strategy:** I weight by trend structure over the last 60 days: higher lows and a reclaimed range earn more weight, and lower highs inside a longer downtrend earn less. Weights stay moderate because every window sits well below where it started 180 days ago. I use basis as a crowding adjustment: a high percentile (above 90) trims weight because leveraged longs are crowded, and a low percentile (below 30) adds a little.

### 11aca3d169 (SOL)
- **Read:** Price fell from about 130 to 81.7 (day -57) and bounced to 113 (day -30). Since then it has made lower highs at 113, 107.2 and 107.1, and drifted into a 96–107 range. Today it closes 100 on low volume. Basis 55 is neutral.
- **Weight 0.3:** The structure is still a lower-high drift, with no confirmation of a turn.
- **Change mind:** Above 107.5 I'd add. Below 95.9 I'd go flat.

### 86feb61ae4 (LINK)
- **Read:** Double bottom at 83.4 and 83.6. Lows have risen since: 89.7, 92.6, 95.5, 94.1. Highs have also risen, from 97.5 to 104.5 to 106.3. Today is a strong reversal day off 96.1. Basis 53 is neutral.
- **Weight 0.5:** This is an early uptrend structure.
- **Change mind:** Below 94 I'd cut. Above 106.3 I'd add.

### 899b6eb23a (LTC)
- **Read:** Lows at 90.7 and 87.9, then a rally to 107–108 (days -15 to -7). It is now pulling back to 100, with support around 97.6–98.9. Basis 14 means positioning is not crowded.
- **Weight 0.45:** Higher-low structure, helped by the low basis.
- **Change mind:** Below 97.5 I'd cut. Above 108 I'd add.

### 273ef22463 (DOT)
- **Read:** A persistent downtrend from about 208 to 93.6. Highs keep falling: 131, 113.6, 108.8, 104.1. Day -6 broke down to 95, and price has only partly retraced to 100. Basis 56 is neutral.
- **Weight 0.15:** The trend is clearly down.
- **Change mind:** A close above 104.1 would make me reconsider. Below 93 I'd go flat.

### 95cce28051 (AVAX)
- **Read:** Lows at 95 and 86.7, a rally to 108.6, then a 92–108 range. Today is a sharp bounce from 92.2 to 100 on higher volume. Basis 32 is mildly favourable.
- **Weight 0.35:** Price is in the middle of the range with no trend.
- **Change mind:** Below 92 I'd go flat. Above 106 I'd add.

### cd76922de8 (XRP)
- **Read:** A downtrend from about 136 to a 92.9 low. Lower highs at 119, 109 and 107.1, and a 96–105 range since then. Basis 94 shows crowded longs.
- **Weight 0.15:** Weak structure combined with an expensive basis.
- **Change mind:** Above 107.1 I'd add. Below 96 I'd go flat.

### 390a7394da (DOGE)
- **Read:** A long decline from 167 to a 100.9 low. Lower highs at 112.1, 106.5 and 104.6, and a 96–105 range. Basis 6 means positioning is washed out.
- **Weight 0.25:** The trend is weak, partly offset by the low basis.
- **Change mind:** Above 104.6 I'd add. Below 95.6 I'd go flat.

### 34b14e9328 (ADA)
- **Read:** A crash to 72.9 and a spike to 105.5, followed by a higher low at 80.9. Today is a strong breakout day from 92 to 100 on 1.73x volume. However, basis 97 shows extreme leverage and squeeze risk.
- **Weight 0.35:** Momentum is positive but the trade is crowded.
- **Change mind:** A close above 105.5 would lift me to 0.6. Below 88 I'd cut.

### 6537778476 (BTC)
- **Read:** An orderly decline from 129 to 91, then steady higher lows at 90.9, 96.4, 97.3 and 98.3. Price is in a tight 98–105 range. Basis 95 is crowded.
- **Weight 0.35:** Constructive grind, trimmed for the high basis.
- **Change mind:** Below 98 I'd cut. Above 105.3 I'd add.

### 5f6c780ec6 (ETH)
- **Read:** Double bottom at 79.9 and 80.2. Higher lows since at 90.9, 92.8, 95.6 and 96.6, and highs at 103.6 and 105.1. Basis 26 is not crowded.
- **Weight 0.5:** Clean recovery structure.
- **Change mind:** Below 96.5 I'd cut. Above 105.1 I'd add.

{"11aca3d169 (SOL)": 0.3, "86feb61ae4 (LINK)": 0.5, "899b6eb23a (LTC)": 0.45, "273ef22463 (DOT)": 0.15, "95cce28051 (AVAX)": 0.35, "cd76922de8 (XRP)": 0.15, "390a7394da (DOGE)": 0.25, "34b14e9328 (ADA)": 0.35, "6537778476 (BTC)": 0.35, "5f6c780ec6 (ETH)": 0.5}

## Entscheidung 2026-08-09

**Strategy:** I follow trend and structure. I want higher lows and price holding above the recovery range after the shared crash around day -65; lower highs or a test of the range floor argue for being flat or small. I then adjust for basis: above 80 means crowded leveraged longs, so I cut the weight. Below 30 means little leverage, so I add a little.

### e5a16b028d (ADA)
- **Read:** Price crashed from about 128 to a 72 low at day -45, with higher lows since (72 → 79 → 83). It ranged 80–90, then broke out over the day -36 spike high of 98.8 to reach 108.8. It is now 100, retesting the breakout zone. The longer-term trend from 150 is still down.
- **Weight 0.45:** The breakout structure is constructive, but basis at 84 says longs are crowded.
- **Change my mind:** a close below 93 (failed breakout) takes me flat.

### 5c76e0a9c3 (DOT)
- **Read:** A persistent downtrend from about 200. Since day -40 it has ranged 93–112 with lower highs (112, 109, 108.9), a low of 93.6 at day -13, and price now 100. No reversal structure.
- **Weight 0.15:** downtrend intact, basis 64 is neutral to elevated.
- **Change my mind:** a close above 109 would raise it.

### 3e1f75e44d (LTC)
- **Read:** Crashed to 86.4, then a steady recovery with higher lows (86.4 → 94.4 → 96). Range 96–106 for the past month, quiet volume, price at 100.
- **Weight 0.55:** constructive base, and basis at 18 means little leverage to unwind.
- **Change my mind:** below 96 I go flat; above 106 I would add.

### c78701f39c (XRP)
- **Read:** Lower highs since the crash (125.6 → 115 → 113 → 108). Price is drifting down to test the range floor around 98, with a 98.3 low at day -2.
- **Weight 0.1:** bearish structure and basis at 81 is crowded.
- **Change my mind:** a reclaim above 109.

### d9d67328e4 (AVAX)
- **Read:** After lows of 88.5 at day -51, a choppy range of 94–110. Recent swing from 94.1 to 108.8 and back to 100. No clear trend.
- **Weight 0.4:** a neutral range, supported by very low basis at 8.
- **Change my mind:** below 94 I go flat; a close above 109 would make me bullish.

### 56017042b9 (DOGE)
- **Read:** Downtrend from the 171 peak. After the 100 low at day -40, a series of lower highs (114.5 → 108.7 → 106.8 → 103.2). Volatility is compressing just above the 98.4 lows, on very low volume.
- **Weight 0.2:** downtrend compression near support, with no confirmation yet.
- **Change my mind:** above 107 I would raise it; below 98 I go flat.

### 95bce8d348 (LINK)
- **Read:** Low of 85.6 at day -45, then higher highs (105.4 → 107 → 108.9) and a higher low at 96.3. It has pulled back to 100, in the middle of a 96–109 range.
- **Weight 0.5:** a recovery uptrend that is intact, with low basis at 26.
- **Change my mind:** below 96 I would cut.

### 8e778003b0 (SOL)
- **Read:** Recovered from 78.8 to 110, then faded with lower highs to a 92.5 low at day -8. Now bouncing to 100, with a 102.1 high on the decision day.
- **Weight 0.15:** lower-high structure, and basis at 98 is extremely crowded.
- **Change my mind:** a close above 104.

### 13dcf045ef (BTC)
- **Read:** Low of 89.5 at day -45, recovery to about 100, then a very tight 96–103 range for a month. Well below the pre-crash 113–125 area.
- **Weight 0.35:** flat base with no momentum, basis 60.
- **Change my mind:** above 103 I would raise it; below 96 I go flat.

### 2f22b4f153 (ETH)
- **Read:** Low of 79.1 at day -44, then clear higher lows (89.7 → 94.4 → 95.4) and highs up to 103.7. Now 100, consolidating under resistance at 102–104.
- **Weight 0.5:** a recovery uptrend, though basis at 66 is somewhat elevated.
- **Change my mind:** below 95 I go flat; above 104 I would add.

{"e5a16b028d (ADA)": 0.45, "5c76e0a9c3 (DOT)": 0.15, "3e1f75e44d (LTC)": 0.55, "c78701f39c (XRP)": 0.1, "d9d67328e4 (AVAX)": 0.4, "56017042b9 (DOGE)": 0.2, "95bce8d348 (LINK)": 0.5, "8e778003b0 (SOL)": 0.15, "13dcf045ef (BTC)": 0.35, "2f22b4f153 (ETH)": 0.5}

## Entscheidung 2026-08-16

**Strategy:** Go long in proportion to how intact the uptrend is: higher lows, a recent break above the range, and holding above recent support. Cut exposure when the structure shows lower highs, or when price sits at fresh lows below the post-crash range. A very high basis percentile (above ~85) means leveraged longs are crowded, so it trims the weight. A low basis is mildly supportive but never overrides a downtrend.

## 1d51b2098a (ETH)
- **Read:** Prior top near 131. It crashed to about 80 (days -72 and -51) and recovered in higher lows: 80.6, 92, 97, 99.6. Price has been compressing between 98 and 104 for about 30 days on fading volume, and it is still well below the pre-crash range of 107–125. Basis 93 means longs are crowded.
- **Weight 0.3:** The constructive base is offset by the crowded basis and no breakout yet.
- **Change mind:** A close above 105 raises the weight. A close below 97 takes it to flat.

## d48a1bfa81 (DOGE)
- **Read:** Top at 170, crashed to 111, then kept bleeding to about 100. Highs keep falling: 133, 114, 108, 105. The flat 99–103 range of the last month is drift, not accumulation. Basis 75.
- **Weight 0.15:** Primary downtrend with no reversal.
- **Change mind:** A close above 106 raises the weight. A close below 97 takes it to flat.

## 4d24497eab (BTC)
- **Read:** Top at 131, crashed to 94, recovered into a 99–106 range. The highs are slightly lower (106.4, then 104.6, then 104). Basis 72.
- **Weight 0.3:** Neutral range with a mild downward tilt.
- **Change mind:** Above 106.5 raises the weight. Below 99 takes it to flat.

## a5abb289e9 (AVAX)
- **Read:** Top at 166, crashed twice, to 98 and then 89.7. It has ranged 95–112 since. Highs are falling (112.4, 110.4, 108.6), and yesterday's spike to 108.6 was fully rejected. Basis 37.
- **Weight 0.25:** Choppy range with lower highs and a failed breakout.
- **Change mind:** Above 110 raises the weight. Below 95.5 takes it to flat.

## 807945e280 (DOT)
- **Read:** Steady decline from 230 to 100. The lower highs are clear: 138, 120, 114.6. Price is sitting near the day -20 low of 98.6. Basis 41.
- **Weight 0.1:** Persistent downtrend, testing support.
- **Change mind:** Above 115 raises the weight. Below 98 takes it to flat.

## 36f590936b (SOL)
- **Read:** Top at 132, crashed to 80.6, rebounded to 112.6, then faded to a 94.6 low. Price is now 100, inside a 95–105 range. Basis 62.
- **Weight 0.3:** The recovery has stalled and the structure is neutral.
- **Change mind:** Above 105 raises the weight. Below 94.5 takes it to flat.

## 7e0fe80b59 (XRP)
- **Read:** Grinding decline from 156 to 100. Lower highs at 130, 119, 117, 112. Price is now making fresh lows near 99–100. Basis 22.
- **Weight 0.05:** Clean downtrend at its lows.
- **Change mind:** Above 110 raises the weight. Below 99 confirms flat.

## fcb8606b64 (LINK)
- **Read:** Crashed to 74.5 and double-bottomed around 74.7. It based between 84 and 92, then broke out on volume over the last 5 days (93.5, then a 103.8 high). It is holding 100. The next resistance is around 104 and then 110–115. Basis 78 is elevated.
- **Weight 0.65:** The only clear breakout from a base. Weight is trimmed for the elevated basis.
- **Change mind:** Below 92 (back inside the range) takes it to flat. Holding above 104 adds.

## 95f5b5fe64 (LTC)
- **Read:** Crashed to 89, recovered to 108.5, and is now pulling back to 100. Lows are rising: 88.9, 97.2, 98.3. The range is 98–105. Basis 23 means longs are not crowded.
- **Weight 0.45:** Higher-low structure with clean positioning.
- **Change mind:** Above 105 raises the weight. Below 97.5 cuts it.

## 2f83c4477e (ADA)
- **Read:** Crashed to 79, rallied sharply to 121 (day -10), and has since retraced about two-thirds of that move to 100. The fade has come on declining volume. The broader lows of 79–88 are still higher lows. Basis 22.
- **Weight 0.3:** Pullback inside a recovering structure, but the momentum is negative right now.
- **Change mind:** Above 110 raises the weight. Below 96 takes it to flat.

{"1d51b2098a (ETH)": 0.3, "d48a1bfa81 (DOGE)": 0.15, "4d24497eab (BTC)": 0.3, "a5abb289e9 (AVAX)": 0.25, "807945e280 (DOT)": 0.1, "36f590936b (SOL)": 0.3, "7e0fe80b59 (XRP)": 0.05, "fcb8606b64 (LINK)": 0.65, "95f5b5fe64 (LTC)": 0.45, "2f83c4477e (ADA)": 0.3}

## Entscheidung 2026-08-23

**Strategy:** I go long when price has reclaimed the structure that broke in the big crash (around day -80) and is holding the breakout, and I scale down when that is undercut. Several things cap the size: a perp basis percentile at an extreme (crowded leveraged longs), a vertical multi-day spike, and a long rejection wick on the latest bar. Every window here shows a sharp 4-day rally into an extreme basis, so all weights are partial. They are higher where price has cleanly reclaimed prior structure and the base before the spike was constructive, and lower where the spike stalled below old resistance or looks like a blow-off.

### cefa98f348 (DOT)
- **Read:** Long downtrend from about 180 to a 78–83 base. Then a 4-day squeeze to 111.2, rejected to a 99.1 close, with day 0 an inside bar at 100. Price is still below the pre-crash range of about 105–110, which is now overhead resistance. Basis is at the 97th percentile.
- **Weight: 0.3.** The trend is improving off the base, but the rally was rejected under resistance and longs are crowded.
- **Change mind:** above 112 I add; below 90 I go flat.

### 7e9f5aef9d (ETH)
- **Read:** A steady pattern of higher lows from 62 to 78 over 60 days, then a breakout to 103.4. Price now sits at 100, above the pre-crash range of about 82–95. The wick on day -1 is modest (102.7). Basis is at the 100th percentile.
- **Weight: 0.5.** The reclaim is clean and the base was constructive. Size is capped by the extreme basis and the vertical move.
- **Change mind:** below 91 (the breakout gap) I go flat; above 103.5 I add.

### 367ac18882 (ADA)
- **Read:** This market has a pattern of pumps that fade: the spike to 88 at day -50 was fully retraced. The current spike hit 113.8 and was rejected to 99.6, still inside the pre-crash range of 100–110. Basis is at the 100th percentile.
- **Weight: 0.25.** The pattern of fading rallies plus the rejection wick argue for a small position.
- **Change mind:** below 92 (the day -1 low) I go flat; a close above 114 means I add.

### 76b3ad614e (SOL)
- **Read:** The base around 77–80 broke out to 107.7, which was wicked back to 98. Price is now above the pre-crash range of about 86–90. Basis is at the 100th percentile.
- **Weight: 0.4.** Structure is reclaimed, but the rejection wick is large.
- **Change mind:** below 92 I go flat; above 108 I add.

### bca9e23d90 (XRP)
- **Read:** A persistent decline to 65, then a parabolic gain of more than 50% in 4 days. Volume reached about 6x the window average on the 111.8 rejection bar, which looks like a blow-off. Basis is at the 100th percentile. Price is technically above the pre-crash range of 85–95.
- **Weight: 0.25.** The move is too vertical and too crowded to hold a large position.
- **Change mind:** below 90.6 I go flat; above 112 I add.

### 9d29766d7e (LINK)
- **Read:** Higher lows had already formed (70 → 76 → 82) before the spike. Price is above the pre-crash range of 78–90 and held 100 after a high of 109.3. Basis is lower than in the other windows, at the 88th percentile.
- **Weight: 0.5.** This is the best base before a breakout among these windows, with less crowding.
- **Change mind:** below 91.5 I go flat; above 109.5 I add.

### d31d57fc21 (AVAX)
- **Read:** Price spent 60 days in an 80–90 range, then spiked to 109.3 and was rejected to 98.5. It remains well below the pre-crash range of 115–125. Basis is at the 100th percentile.
- **Weight: 0.3.** There is a breakout from the range, but major resistance is overhead and longs are crowded.
- **Change mind:** below 92 I go flat; above 110 I add.

### e37a9c9ee0 (BTC)
- **Read:** Price rose from a tight 80–84 base to 102.3. It is consolidating near the highs (day -1 range 98.4–101.4, low volume) rather than wicking hard, and sits at the pre-crash level of about 95–100. Basis is at the 100th percentile.
- **Weight: 0.45.** The digestion after the move is healthier, but price is at resistance and longs are crowded.
- **Change mind:** below 93.5 I go flat; above 102.5 I add.

### 31f520b88a (DOGE)
- **Read:** A grind in the 74–76 range, then a spike to 107.9, rejected exactly at the pre-crash shelf of 107–110 and closing at 98.4 on heavy volume. Basis is at the 100th percentile.
- **Weight: 0.3.** The rejection came at clear resistance.
- **Change mind:** below 89 I go flat; above 108 I add.

### ec45d9ec97 (LTC)
- **Read:** A recovery from the crash low of 77 to a base of about 84–90, then a spike to 106.1, rejected to 100.3. Price is near the pre-crash range of 99–100, with 110+ above that. Basis is at the 100th percentile.
- **Weight: 0.35.** The structure is decent, but the rally was rejected and longs are crowded.
- **Change mind:** below 96 I go flat; above 106.5 I add.

{"cefa98f348 (DOT)": 0.3, "7e9f5aef9d (ETH)": 0.5, "367ac18882 (ADA)": 0.25, "76b3ad614e (SOL)": 0.4, "bca9e23d90 (XRP)": 0.25, "9d29766d7e (LINK)": 0.5, "d31d57fc21 (AVAX)": 0.3, "e37a9c9ee0 (BTC)": 0.45, "31f520b88a (DOGE)": 0.3, "ec45d9ec97 (LTC)": 0.35}

## Entscheidung 2026-08-30

**1. Strategy.** I go long when price holds above its pre-breakout base and above prior swing highs, with the long-term trend not clearly down. I cut size when the basis percentile is high, because crowded leveraged longs make a failed spike more likely, and add a little when it is low. Windows still in a 180-day downtrend that have given back most of a spike get small weights.

---

**2513f3b302 (DOT)**
- **Read:** Long downtrend from 188 to a base around 92–94. A spike on day -8 reached 126, and price has since faded to 100, giving back most of it. Resistance is 104–106, the pre-spike swing highs. Support is 98.7 (today's low), then the 92–94 base. Basis 83 means longs are crowded.
- **Weight:** 0.2. A failed spike inside a downtrend, with crowded longs.
- **Change of mind:** A close above 110 would make me more bullish. A close below 92 would take me flat.

**8f7c455336 (XRP)**
- **Read:** Fell from 118 to a tight 73–75 base. The breakout came on very large volume (6x) and spiked to 125. Price is holding 98–112 for 8 days and sits mid-range in the 180-day span of 74–118. Support is 98.4. Basis 14 means leverage is not crowded.
- **Weight:** 0.5. A real base breakout and a clean basis, though price has retraced a lot.
- **Change of mind:** A close below 95 would cut the position. A close above 112 would add.

**76051539ac (LINK)**
- **Read:** Based at 73–75, then made higher lows from day -19 (78, 85) before spiking to 113. Price is now 100, above the old 180-day swing high near 97.5. Support is 97–98.6. Basis 59 is neutral.
- **Weight:** 0.55. Structure turned up before the spike, and price is holding above the old highs.
- **Change of mind:** A close below 97 would cut it. A close above 108 would add.

**0f7758cac4 (DOGE)**
- **Read:** Downtrend from 140 to an 84–86 base. A spike to 123 has faded to 100. Resistance is 110–114. Support is 98.5, then 86. Basis 91 means longs are very crowded.
- **Weight:** 0.15. A fading spike in a downtrend with crowded longs.
- **Change of mind:** A close above 110 would make me more bullish. A close below 98 would take me flat.

**0adbb927a9 (BTC)**
- **Read:** Based at 81–84, then broke out to 102.3. It has consolidated tightly at 99–104 for 8 days, a flag shape with shallow retracements. The prior 180-day high is about 106.7. Basis 48 is neutral.
- **Weight:** 0.6. A tight hold after the breakout, with no sign of distribution.
- **Change of mind:** A close below 97 would cut it. A close above 105 would add.

**a9d68ee004 (ETH)**
- **Read:** Based at 77–79, then a gap and spike to 105, now consolidating at 99.5–106. Price is just under the prior 180-day high of about 102. Support is 98.8. Basis 82 means longs are crowded.
- **Weight:** 0.4. Structure is good, but the basis is high.
- **Change of mind:** A close below 98 would cut it. A close above 106 would add.

**26ac568d24 (AVAX)**
- **Read:** Downtrend from 147 to an 88–98 range that lasted about 80 days. A spike to 117 has faded to 100, just above the top of that range. The breakdown level from above is 115–125. Basis 74 is elevated.
- **Weight:** 0.3. Price is barely above the range, and both the trend and the basis are unfavorable.
- **Change of mind:** A close below 97 would take me flat. A close above 108 would add.

**d0c739f86a (ADA)**
- **Read:** Downtrend from 150 to a 72 low, followed by repeated pump-and-fade moves to 104, 110 and 134. Each fade has made a higher low (72, 80, 89). Price is now 100, below the 110 high from day -24 and having given back most of the spike. Support is 98.3, then 89. Basis 36 is lowish.
- **Weight:** 0.35. Higher lows argue for a position, but the repeated failed spikes keep it small.
- **Change of mind:** A close below 95 would take me flat. A close above 111 would add.

**afb23b4607 (LTC)**
- **Read:** Downtrend from 126 to 82, then a steady recovery with higher lows to a 91–99 base. A spike to 115.7 has faded to 100. Price is still above the pre-spike range high of about 96–99. Basis 57 is neutral.
- **Weight:** 0.5. The intermediate trend has been up since day -66.
- **Change of mind:** A close below 96 would cut it. A close above 106 would add.

**06d149df33 (SOL)**
- **Read:** Crash low at 59, a 70–76 base, then a more gradual climb to 108.7 on day -3 before a pullback to 100. Price is above the 180-day high of about 96.7. Support is 98.6, then 93. Basis 94 means longs are extremely crowded.
- **Weight:** 0.3. Price structure is constructive, but the extreme basis argues against size.
- **Change of mind:** A close below 93 would take me flat. A close above 109 would add.

---

{"2513f3b302 (DOT)": 0.2, "8f7c455336 (XRP)": 0.5, "76051539ac (LINK)": 0.55, "0f7758cac4 (DOGE)": 0.15, "0adbb927a9 (BTC)": 0.6, "a9d68ee004 (ETH)": 0.4, "26ac568d24 (AVAX)": 0.3, "d0c739f86a (ADA)": 0.35, "afb23b4607 (LTC)": 0.5, "06d149df33 (SOL)": 0.3}

## Entscheidung 2026-09-06

**Strategy:** I go long when price is in a rising structure: higher lows, a hold above the most recent consolidation floor, and the close near or above recent swing highs. I scale the weight down when there is heavy overhead supply from an older range or a failed spike high. I also scale it down when the basis percentile is high (above roughly 80), because crowded leveraged longs make pullbacks more likely. A low basis during an uptrend is a mild positive.

## fb88dfac97 (LINK)
- **Read:** The cleanest trend in the set. Price based between 55 and 65 for about 70 days, broke out at day -18, and built a flag between 83 and 92. Day 0 broke out of that flag to close at 100 (high 100.9), a new 180-day high above the 82 peak from day -119, on rising volume (1.70). There is no overhead supply, and the basis (59) is neutral.
- **Weight:** 0.9, because this is a trend continuation with clear air above.
- **Change my mind:** a close below 83, the flag floor.

## 3b81dd288c (AVAX)
- **Read:** The earlier range was 110–133. Price crashed to about 72, based between 77 and 88, then rallied, with a spike high of 105.2 at day -15. Since then it has made higher lows (88.7, then 89.0) and today closes at 100. Resistance sits at 105, then at the old range floor of 110–113. The basis (64) is moderate.
- **Weight:** 0.6. The trend is up, but there is overhead supply above 105.
- **Change my mind:** a close below 88.7.

## d20cdd8f60 (BTC)
- **Read:** The earlier top was 98–103 (days -125 to -115). Price crashed to 73, based between 74 and 82, then rallied to 97.5 and has held tightly between 95 and 101 for 15 days. It closes at 100 on low volume (0.53), so it is pressing into the old top at 101–103. The basis (45) is neutral.
- **Weight:** 0.6. The structure is constructive, but price is at resistance without volume confirmation.
- **Change my mind:** a close below 94.9.

## 6b5039e1be (DOGE)
- **Read:** The earlier peak was 130, followed by a crash and a base between 75 and 82. A spike reached 110.9 and failed. Price pulled back to 88, and day -1's push to 104.7 was rejected. It closes at 100. The action is choppy, with long wicks on both sides, and the basis (91) is crowded.
- **Weight:** 0.4. There is some upward structure, but rejections plus a crowded basis argue for caution.
- **Change my mind:** below 88 to exit. A close above 105 would raise the weight.

## e6c086260a (LTC)
- **Read:** The earlier range was 95–110. Price crashed to 74, based between 79 and 87, then spiked to 100.9 and pulled back to 86.2. A higher-low rally followed, and a high-volume push on day -1 (2.32) brought price back to 100. It is now testing the spike high at 100.9 and the bottom of the old range. The basis (83) is elevated.
- **Weight:** 0.55. The higher lows are bullish, offset by the high basis and resistance at 101–105.
- **Change my mind:** a close below 86.

## 10fa8af6ff (SOL)
- **Read:** The earlier peak was 92.4. Price crashed to 56, based between 67 and 77, then rallied through the old peak to 103.8. The pullback held at 91.4, right on the old 92 high, which has turned from resistance into support. Price closes at 100. The basis (15) is low, so longs are not crowded.
- **Weight:** 0.8. The breakout above the prior range has been retested and held, and positioning is clean.
- **Change my mind:** a close below 91.

## 26ddead6e9 (ADA)
- **Read:** The earlier range was 105–125. Price crashed to 66, followed by violent swings (89.5, 64, 94.8, 78). At day -15 a spike reached 115.7 and failed. Price pulled back to 84.8 and closes at 100. It sits below the spike and the old range, the volatility is extreme, and the basis (90) is crowded.
- **Weight:** 0.4. The trend is unclear, there is a lot of overhead supply, and positioning is crowded.
- **Change my mind:** below 85 to exit. A close above 106 would raise the weight.

## 0aa2bd3d77 (ETH)
- **Read:** The earlier high was 98 (day -142). Price crashed to 60, based between 62 and 77, then broke out sharply to 101.3. It has consolidated between 93.7 and 102 with higher lows and closes at 100, at the 180-day high zone. The basis (82) is elevated.
- **Weight:** 0.6. The trend and structure are good, trimmed for the basis and the double-top risk around 101–102.
- **Change my mind:** a close below 93.7.

## 1a7588db90 (XRP)
- **Read:** The earlier range was 92–112. Price crashed to 74, then drifted lower to 70. At day -15 there was a blow-off spike to 119.4 on 6x volume that closed at 102.7. Since then the highs keep falling (108.9, 104.2, 100.6), which looks like distribution. Price closes at 100, and the basis (98) is extreme.
- **Weight:** 0.25. The spike failed, the highs are declining, and leveraged longs are as crowded as they get.
- **Change my mind:** a close above 104.2 would be bullish. Below 92, I would go flat.

## 4947fae50a (DOT)
- **Read:** A long downtrend ran from 167 to 76 with lower highs. A spike to 105.4 failed, but the pullback held at 82.5, a higher low than the 76 from day -41. Day 0 broke out to 100 (high 101.3) on 1.67 volume. The basis (38) is not crowded. The spike high at 105.4 is the next resistance.
- **Weight:** 0.55. A trend reversal is underway, but it is still under the spike high, and the larger trend is down.
- **Change my mind:** a close below 85.

{"fb88dfac97 (LINK)": 0.9, "3b81dd288c (AVAX)": 0.6, "d20cdd8f60 (BTC)": 0.6, "6b5039e1be (DOGE)": 0.4, "e6c086260a (LTC)": 0.55, "10fa8af6ff (SOL)": 0.8, "26ddead6e9 (ADA)": 0.4, "0aa2bd3d77 (ETH)": 0.6, "1a7588db90 (XRP)": 0.25, "4947fae50a (DOT)": 0.55}

## Entscheidung 2026-09-13

**Strategy:** After a breakout from a multi-month base, I stay long while price holds above the lows of the consolidation that followed the breakout. I cut size when price sits on those lows, when the latest push was a blow-off spike that has been fully given back, or when the basis percentile is high (above about 65, meaning crowded leveraged longs). A low basis is mildly supportive. A close below the consolidation lows means flat.

## 49f58d2020 (XRP)
- **Read:** Price fell from about 113 into a long, slowly declining base between 74 and 85, which bottomed near 74. It broke out hard at day -25 and wicked to 126.7. Since then it has consolidated between 98 and 110 with lower highs: 110.6, then 108.2, then 106.9. Support is 97.7–99, and the close of 100 sits right on it. Price is back inside its old pre-crash range of 98–110. Basis 54 is neutral.
- **Weight: 0.5.** The breakout structure is intact, but price is pressing support under a series of lower highs.
- **Change my mind:** a close below 97 (go flat), or a close above 107 (add).

## 11a457863f (SOL)
- **Read:** The base sat between 72 and 78. The breakout carried to 111.4 at day -17. The consolidation since runs 98–108, with lows at 98.1, 98.7 and 99.2. Price is now above its pre-crash range of 82–98, so it has regained more ground than most windows. Basis 28 means leverage is not crowded.
- **Weight: 0.6.** Strong relative structure, support holding, and cheap leverage.
- **Change my mind:** a close below 97.5.

## 410072572d (ADA)
- **Read:** The crash ran from about 135 down to 73. The base between 70 and 100 includes an earlier failed rally that topped near 104 at day -38. The breakout at day -22 wicked to 127. The consolidation since runs 93–114, with lows at 93.1 and 98.5. Price is still far below its pre-crash range of 115–135. Basis 30.
- **Weight: 0.45.** Wide, choppy support and a lot of overhead supply above.
- **Change my mind:** a close below 93 (go flat), or a reclaim above 110.

## 351317391e (AVAX)
- **Read:** The crash ran from 140 to 78, followed by a base between 84 and 95. The breakout went to 114. The consolidation since runs 96–112. The latest high of 112.5 at days -6/-5 was sold back down to 100. Support is 96–99.8. Basis 11 is very low, so leverage is not crowded.
- **Weight: 0.5.** The structure is fine, but the rejection from 112 weighs on it. The low basis offsets some of that.
- **Change my mind:** a close below 96.

## 3c6a4f70cd (BTC)
- **Read:** A tight base between 81 and 85 broke out to 103.5, and price later reached 107 at day -10. The consolidation runs 99–107, with repeated lows at 99.0–99.5. Price is back at its pre-crash range of 95–107. Volume is fading. Basis 63 is on the high side.
- **Weight: 0.45.** Price is sitting exactly on support, and the elevated basis adds risk.
- **Change my mind:** a close below 98.5.

## c96b5b8b55 (ETH)
- **Read:** The base sat between 74 and 78. A single-day breakout came at day -25, and price has held between 95 and 103 ever since, with a 107.6 wick at day -2. The lows are higher than the base, at 95.1, 96.4 and 97.1. Price is above its pre-crash range of 80–97. Basis 43.
- **Weight: 0.55.** Steady acceptance above the breakout level, with support a little further below than in the other windows.
- **Change my mind:** a close below 95.

## eaf4c1dbc6 (LINK)
- **Read:** The base sat between 72 and 75, and price started rising early, from day -33. The breakout went to 112. A further spike to 122 at days -7/-6 was fully retraced back to 100. Support is 97.4–100. Price is above its pre-crash range of 75–97. Basis 42.
- **Weight: 0.5.** The trend is up, but the failed spike is a warning.
- **Change my mind:** a close below 97.

## 8343ac6a28 (LTC)
- **Read:** The base sat between 81 and 88. The breakout went to 103 and then retraced to 88.2 at day -14. A higher rally followed, wicking to 110.6 at day -6, and the latest higher low is 96 at day -3. Price is near the middle of its pre-crash range of 95–112. Basis 8 is very low.
- **Weight: 0.5.** Higher lows and very cheap leverage, but the 110 wick was rejected.
- **Change my mind:** a close below 96.

## 47f0bbdd82 (DOT)
- **Read:** A long downtrend ran from 162 to a base between 75 and 80. The first breakout reached 103 but faded back to 81. Then came a parabolic spike to 128.5 on 4x volume, which was fully reversed to 100 within four days. This is a classic blow-off and failure. Basis 73 means leveraged longs are crowded.
- **Weight: 0.2.** A blow-off reversal combined with crowded leverage.
- **Change my mind:** a reclaim above 107 (add), or a close below 95 (go flat).

## 140e734683 (DOGE)
- **Read:** The crash ran from 140 to 86, followed by a base between 84 and 88. The breakout went to 122. The consolidation since runs 97–115, with lows at 97.2, 98.1 and 99.9. Recent highs are lower: 115.5, then 111.7, then 107.2. Price is still far below its pre-crash range of 120–140. Basis 48.
- **Weight: 0.45.** Support is holding, but highs are lower and there is heavy overhead supply.
- **Change my mind:** a close below 97.

{"49f58d2020 (XRP)": 0.5, "11a457863f (SOL)": 0.6, "410072572d (ADA)": 0.45, "351317391e (AVAX)": 0.5, "3c6a4f70cd (BTC)": 0.45, "c96b5b8b55 (ETH)": 0.55, "eaf4c1dbc6 (LINK)": 0.5, "8343ac6a28 (LTC)": 0.5, "47f0bbdd82 (DOT)": 0.2, "140e734683 (DOGE)": 0.45}

## Entscheidung 2026-09-20

## Strategy

I follow the trend. A window gets a large long weight when price is breaking above or holding near the top of its last month's range and the 180-day structure is recovering. I cut the weight when the basis percentile is above 90, because leveraged longs are crowded, and when the last few days have been a vertical move that often gives some of it back. Each window has a close below a nearby support level that would make me exit.

## cf90f3921f (ETH)
- **Read:** The crash bottomed near 57 around day -107. The base and recovery ran from 59 to 72, then a jump at day -32 took price to 95. It held a 89–96 range for a month. Days -2 to 0 broke out to 100, the highest close in the window and above the old highs near 91–93.
- **Levels:** Support is 89–90 (the day -5 low). Resistance is the 100.9 high.
- **Basis:** 74, raised but not extreme.
- **Weight:** 0.8. This is a clean breakout from a month-long range, and leverage is not crowded.
- **Change of mind:** A close below 89.

## 246d87a50e (LINK)
- **Read:** Price recovered from the 56 low to 95 at day -30. It spiked to 109 at day -13, then dropped to 84.8 at day -4. It has rebounded to 100, which is mid-to-upper range but below the 106–109 spike highs.
- **Levels:** Support is 85–87.
- **Basis:** 77, moderate.
- **Weight:** 0.6. The trend is up, but the failed spike leaves supply overhead between 102 and 109.
- **Change of mind:** A close below 86 means flat. A close above 106 would raise the weight.

## db666deefb (XRP)
- **Read:** Price jumped from 71 to a 120.5 wick at day -29. That was a blow-off, and since then it has chopped between 89 and 108. It sits at 100, mid-range, with big two-way swings: the day -5 range was 106 down to 89.7. The longer-term level is unchanged from the window start, about 100, and the old highs are 104–110.
- **Basis:** 99, extremely crowded.
- **Weight:** 0.3. There is no clear trend in the range, and this is the most crowded leverage of any window.
- **Change of mind:** A close below 89 means flat. A close above 108 would raise the weight to about 0.6.

## bc6756f9ea (AVAX)
- **Read:** Price spent more than 100 days in a 52–72 base. Over the last 3 days it went vertical: 67, then 72.5, then 89, then 100, on volume of 2.5 to 6 times average. Day 0 had a 83.4–101.4 range. It has cleared every resistance level in the window, including 88–92.
- **Basis:** 82.
- **Weight:** 0.4. The breakout from the base is very strong, but a gain of about 50% in 3 days with climactic volume has a high chance of a sharp pullback toward 85–90.
- **Change of mind:** A close below 83, the day 0 low, means flat. Holding above 95 for a week would raise the weight.

## ebb3347b15 (ADA)
- **Read:** The long-term trend fell from 119 to 63, then recovered. A spike wicked to 113 at day -29. Since then price has ranged 84–102, and it is now at 100, near the top. The range highs are 101.8 and 103.1, and lows have been rising: 83.1, then 84.7, then 83.5.
- **Basis:** 88.
- **Weight:** 0.55. It is at range resistance and has not broken out yet.
- **Change of mind:** A close below 85 means flat. A close above 103 means add.

## 2d06191508 (DOT)
- **Read:** The 180-day trend is down, from 123 to 64. Then price spiked to 113 at day -12 and retraced to 82.3 at day -5. A sharp V took it back to 100, making a higher low above the 71–74 base.
- **Basis:** 64, the least crowded of the windows.
- **Weight:** 0.6. Momentum is recovering and leverage is not stretched, but volatility is high and there is supply at 103–113.
- **Change of mind:** A close below 88. A close above 104 would raise the weight.

## 3938c1e3dc (SOL)
- **Read:** This is the most orderly uptrend: price has stair-stepped from 67 to 100. Day -2 broke above the 98–99.5 resistance to 101.4. Price has since held at 100, near the window high of 102.8. Support is 91–92, and below that 86.
- **Basis:** 94, crowded.
- **Weight:** 0.65. The trend and breakout are strong, and I trim for leverage.
- **Change of mind:** A close below 91.

## c80b73e5d1 (BTC)
- **Read:** Price rallied to 96.5 at day -30, then ground in a tight 92–101 range for a month. It now sits at the top of that range. The resistance levels are 101.4 (day -17) and 102.1 (the old high at day -137). Volatility is low.
- **Basis:** 91.
- **Weight:** 0.6. It is a constructive coil at the highs, but the breakout is not confirmed and leverage is crowded.
- **Change of mind:** A close below 92. A close above 102 means add.

## f7a5c67a8c (LTC)
- **Read:** Price went from 75 to 92, pulled back to 81, then rallied to 94–101. Day -5 made a higher low at 85.5, and price is now 100. That is the highest close since the 103 peak around day -133. The trend is up but slower than the others.
- **Basis:** 96, very crowded.
- **Weight:** 0.5.
- **Change of mind:** A close below 86. A close above 103 would raise the weight.

## c3c6ed3b61 (DOGE)
- **Read:** The larger structure is weak. Price peaked at 135 around day -129, crashed to 79, and the rebound spiked to 115.5 before failing. Since then it has ranged 90–109 and is at 100, mid-range and well below the earlier highs. The last month shows lower highs: 109, then 105, then 104.6.
- **Basis:** 94, crowded.
- **Weight:** 0.35.
- **Change of mind:** A close below 89 means flat. A close above 106 would raise the weight to about 0.6.

{"cf90f3921f (ETH)": 0.8, "246d87a50e (LINK)": 0.6, "db666deefb (XRP)": 0.3, "bc6756f9ea (AVAX)": 0.4, "ebb3347b15 (ADA)": 0.55, "2d06191508 (DOT)": 0.6, "3938c1e3dc (SOL)": 0.65, "c80b73e5d1 (BTC)": 0.6, "f7a5c67a8c (LTC)": 0.5, "c3c6ed3b61 (DOGE)": 0.35}

## Entscheidung 2026-09-27

# T-001 Weights

## 1. Strategy
I go long in proportion to trend strength. The case for a long is a breakout above the window's prior range that is now holding, with higher lows and orderly consolidation near the highs. I cut the weight when the perp basis percentile is high (crowded leveraged longs), when price is still below older overhead highs, or when recent action is a wide, failing swing range. Each window gets an invalidation level, usually just under the most recent swing low; a close below it means the breakout is failing.

## 2. Windows

### 9df11d71bd (XRP)
- **Read:** The decline from about 97 to a 65–66 base ended in a violent breakout at day −39 (high 112.1). Since then price has ranged 84–104 with rising lows: 84.6 at day −12, 97.5 at day −4. The last week pushed to 109.3 and 107.5 but could not hold above 104, and it now sits at 100.
- **Basis:** 77, elevated.
- **Weight: 0.55.** The uptrend is intact, but repeated rejections at 104–109 and a crowded basis cap the position.
- **Change my mind:** a break below 95.7.

### ae5ca7106b (DOGE)
- **Read:** Price is still below the older 116–122 highs from days −145 to −136. The post-breakout range is 81–109. It spiked to 109.3 at day −5 and then dropped hard to 95.7 the next day. Lows are higher (80.9 then 94.0), but the structure is choppy.
- **Basis:** 87, very crowded.
- **Weight: 0.4.** There is overhead supply, a failed spike, and an expensive basis.
- **Change my mind:** a break below 94.

### e6a56ccc58 (ETH)
- **Read:** A clean staircase. Price broke out from 71 to about 94, based between 87 and 95 for about four weeks, then broke to 104.4 at day −6. It is now consolidating tightly at 99–100 on fading volume, above every earlier high in the window (91.7).
- **Basis:** 65, moderate.
- **Weight: 0.8.** This is a textbook breakout-and-hold.
- **Change my mind:** a break below 96.7.

### bbe3e6f24c (DOT)
- **Read:** Price went from a 60 base to 101 at day −19, retraced to 73.7, and then rallied with higher lows (73.7, then 85.0) back to 103 at day −1. It is volatile but trending up. The older highs at 109–113 are still overhead.
- **Basis:** 18, so longs are not crowded and the rally is not leverage-driven.
- **Weight: 0.65.** The momentum and low basis are good, but high volatility and the overhead highs keep this below full.
- **Change my mind:** a break below 85.

### 61d167a44c (AVAX)
- **Read:** A long base at 57–60, then a near-vertical move from 70 to 105 at days −8 and −7. Since then it has held 92–104 for about a week and is above the older highs near 96. The move is very young and extended.
- **Basis:** 72.
- **Weight: 0.5.** A strong breakout, but a single vertical leg is prone to a deeper retrace.
- **Change my mind:** a break below 91.4.

### 4b4b7d73bd (BTC)
- **Read:** A breakout from 76 to a 90–96 base, then a new high at 103.5 at day −6. It has since compressed to 99–100.6 on low volume, above the earlier window high of 98.1. This is the most orderly structure in the set.
- **Basis:** 37, not crowded.
- **Weight: 0.85.**
- **Change my mind:** a break below 98.

### 766f47c074 (SOL)
- **Read:** A persistent run of higher highs and higher lows from 62 to 100, now at new highs, well above the earlier 80.7 peak. Pullbacks have been shallow, at 79–81 and 92.6.
- **Basis:** 88, very crowded.
- **Weight: 0.6.** The trend is excellent, but leverage risk is high.
- **Change my mind:** a break below 92.

### c6a5cf358b (ADA)
- **Read:** The post-breakout range is 74–104, with rising lows (74.6, then 91.3). Price is at 100, below 104 and well below the older 107–113 highs. The ranges are wide and the swings two-sided.
- **Basis:** 76.
- **Weight: 0.5.**
- **Change my mind:** a break below 91.

### cf2316c773 (LTC)
- **Read:** A slower uptrend from 62 to about 77–88, then a climactic volume day at day −3 (6.7x average) that jumped from 87 to 105. Price has held 97–105 for three days and is far above the old highs near 85. A climactic spike can mark exhaustion.
- **Basis:** 64.
- **Weight: 0.6.**
- **Change my mind:** a break below 96.7.

### 7cb9c64d40 (LINK)
- **Read:** A base at 58–60, a breakout to an 76–97 range, and now new highs at 100–103, well above the old 77.5 peak. Higher lows: 75.7, then 86.0, then 94.1.
- **Basis:** 59, moderate.
- **Weight: 0.75.**
- **Change my mind:** a break below 94.

## 3. Weights

{"9df11d71bd (XRP)": 0.55, "ae5ca7106b (DOGE)": 0.4, "e6a56ccc58 (ETH)": 0.8, "bbe3e6f24c (DOT)": 0.65, "61d167a44c (AVAX)": 0.5, "4b4b7d73bd (BTC)": 0.85, "766f47c074 (SOL)": 0.6, "c6a5cf358b (ADA)": 0.5, "cf2316c773 (LTC)": 0.6, "7cb9c64d40 (LINK)": 0.75}
