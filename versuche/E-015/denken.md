# E-015: was die KI gedacht hat (Set A)

Volle Antwort des Deciders pro Entscheidungswoche, unverändert. Er sah weder Datum noch Coin-Namen; die Namen in Klammern sind erst danach eingesetzt. Gesendeter Prompt und Daten: runs/<set>/<woche>/requests.json.

## Entscheidung 2026-07-05

**Strategy:** All ten windows share the same shape: a long decline, a sharp breakdown around day -33 to -30, and a rebound to 100. I go fully long (1) only when price has won back the pre-breakdown level and sits above its ~50-day average, with higher lows. I hold half (0.5) when there is a basing pattern (double bottom, or a reclaimed short-term range) but price is still below the breakdown level or the 50-day average. I stay flat (0) when the bounce is still inside a sequence of lower highs and lower lows, well under the 50-day average.

### 02d6fe7c74 (SOL)
- **Read:** Crashed from the ~100–105 range to 73.7 at day -29. Made a clearly higher low at 78.5 on day -10, then a steady advance with higher highs to 100. That puts it back inside the pre-breakdown band of 100–105. The 50-day average is about 92, so price is above it. Resistance is 105–110.
- **Weight:** 1.0. It is a V-shaped recovery with a higher-low structure and the breakdown level has been reclaimed.
- **Change of mind:** a close below 92.

### b610638c0a (LINK)
- **Read:** The breakdown came from ~112–117. It double-bottomed at 86.8 and 86.9, and price is now 100. The neckline is the day -20 high at 106.7, and the 50-day average (~103) is overhead.
- **Weight:** 0.5. The base is constructive, but the trend has not yet been reclaimed.
- **Change of mind:** above 106.7 I would go to 1; below 94 I would go to 0.

### a3feb6f657 (DOGE)
- **Read:** The breakdown came from ~129. It made a low of 99.7, then a lower high at 118.7 and a lower low at 89.3 on day -5. The bounce to 100 sits far below the 50-day average (~113).
- **Weight:** 0. It is still a downtrend of lower highs and lower lows.
- **Change of mind:** a close above 112.

### 6437bffb93 (AVAX)
- **Read:** The breakdown came from ~129. It made a capitulation low at 82.0 on day -16 on heavy volume, then a higher low at 86.0, and is now 100, around the day -20 high of 102. The 50-day average is ~108.
- **Weight:** 0.5. Capitulation followed by a higher low points to a base, but price is under its averages.
- **Change of mind:** above 103 I would go to 1; below 92 I would go to 0.

### b545d15984 (XRP)
- **Read:** The breakdown came from ~115. The lows were 90.7 and then a slightly lower 87.2, and price is now 100. Overhead are the spike high at 111.8 and the 50-day average at ~104.
- **Weight:** 0.5. It is basing but still capped.
- **Change of mind:** above 105 I would go to 1; below 92 I would go to 0.

### 0eab3ad18b (ADA)
- **Read:** The breakdown came from ~124. It made a lower low at 72.9 on day -10, then ran from 76 to 101 in four days on volume of 2x the average. That move broke above the day -20 high (100.3), and price is now roughly at the 50-day average (~101). It is very extended.
- **Weight:** 0.5. The momentum is real, but a vertical move straight into resistance makes the entry poor.
- **Change of mind:** above 105.5 I would go to 1; below 92 I would go to 0.

### 3a657df431 (DOT)
- **Read:** The breakdown came from ~135. It made a low of 100.3, a lower high at 118.8, and a lower low at 90.2. The bounce to 100 is well under the 50-day average (~118).
- **Weight:** 0. The downtrend is intact.
- **Change of mind:** a close above 115.

### b331ee4d10 (BTC)
- **Read:** The breakdown came from ~116. Lows were 92.9 and then 90.8, a rough double bottom, and price is now 100. Overhead are the day -20 high at 105.7 and the 50-day average at ~105.
- **Weight:** 0.5. It is a base, but the trend has not turned.
- **Change of mind:** above 106 I would go to 1; below 93 I would go to 0.

### 20c2f88858 (ETH)
- **Read:** The breakdown came from ~112. It double-bottomed at 84.3 and 84.7, and price is now 100, just under the 103.6 neckline. The 50-day average is ~101.
- **Weight:** 0.5. This is a clean double bottom, but it is not confirmed yet.
- **Change of mind:** above 104 I would go to 1; below 90 I would go to 0.

### 736dd0f2ac (LTC)
- **Read:** The breakdown came from ~113. Lows were 88.4 and then 85.7, and today's close of 100 is the highest close since day -33. The 50-day average is ~101.
- **Weight:** 0.5. It is basing and pressing on the 50-day average.
- **Change of mind:** above 102 I would go to 1; below 91 I would go to 0.

{"02d6fe7c74 (SOL)": 1.0, "b610638c0a (LINK)": 0.5, "a3feb6f657 (DOGE)": 0.0, "6437bffb93 (AVAX)": 0.5, "b545d15984 (XRP)": 0.5, "0eab3ad18b (ADA)": 0.5, "3a657df431 (DOT)": 0.0, "b331ee4d10 (BTC)": 0.5, "20c2f88858 (ETH)": 0.5, "736dd0f2ac (LTC)": 0.5}

## Entscheidung 2026-07-12

## Strategy
Every window is in a long-term downtrend: one crash around day -157, a second crash at days -40 to -37, a retest around days -18 to -17, and a rally that has pulled back to 100. I score the structure after the second crash.
- **Flat (0):** the retest low undercut the crash low (lower low).
- **Half (0.5):** the crash low held on the retest.
- **Full (1):** the crash low held, the latest rally high exceeded the day -27 high, and price is still above the most recent pullback low.

## 101ad36384 (ADA)
- **Read:** Fell from 260 to 100. The crash low was 91.7 (day -36). The retest broke lower to 85.3 (day -17), a lower low.
- **Structure:** The spike to 123.4 (day -8) fully reversed back to 100, a failed breakout on fading volume.
- **Weight 0:** The low did not hold, and the rally was rejected.
- **Change my mind:** A close above 118, which would retake most of the spike.

## cd424ff9d6 (ETH)
- **Read:** The crash low was 83.3 (day -36). The retest at 83.7 (day -16) held, giving a double bottom.
- **Structure:** Price has based between 95 and 101 since, with higher lows at 94.8 (day -4) and 98.5 (day 0) on shrinking volume. The highs are flat: 102.4 (day -27) and 101.5 (day -6).
- **Weight 0.5:** The base held, but there is no higher high yet, and the 111 breakdown level sits overhead.
- **Change my mind:** Below 94.5 I go flat. Above 102.5 I would consider full.

## 0e04cf77c0 (XRP)
- **Read:** The crash low was 96.7. The retest made a lower low at 93.2.
- **Structure:** Highs are falling: 119.1 (day -27), then 109.1 (day -8). Price is at 100.
- **Weight 0:** Lower lows and lower highs mean the downtrend is intact.
- **Change my mind:** A close above 109.5.

## 1dcc7b2f8f (BTC)
- **Read:** The crash low was 92.7. The retest made a slightly lower low at 91.1.
- **Structure:** Highs are falling: 105.5 (day -27), then 101.4 (day -6). Price is in a tight range of 99 to 101.
- **Weight 0:** The low was marginally undercut, and the highs are lower.
- **Change my mind:** A close above 105.5.

## ad1b0d50e1 (DOGE)
- **Read:** The crash low was 106.8. Later lows broke well below it: 98.3, then 95.6 (day -12).
- **Structure:** Highs are falling: 127.2 (day -30), then 109.2 (day -8). Volume is drying up near 100.
- **Weight 0:** This is a clean lower-low, lower-high sequence.
- **Change my mind:** A close above 109.5.

## 38744b0c58 (DOT)
- **Read:** The crash low was 104.7. Later lows broke below it: 97.0, then 94.2 (day -14).
- **Structure:** Highs are falling: 124.1 (day -27), then 107.6 (day -6). The day -2 pop to 106 was sold back to 100.
- **Weight 0:** The downtrend is intact.
- **Change my mind:** A close above 108.

## 41ac5ec73d (AVAX)
- **Read:** The true low was 88.7 (day -23). Later lows were higher: 92.9 (day -17).
- **Structure:** The highs match at 110.5 (day -27) and 111.1 (day -8), so this is a range of 89 to 111. Today's low of 98.0 broke the day -4 pullback low of 98.6.
- **Weight 0.5:** The low held and there is a marginal higher high, which would qualify for full. I downgrade to half because of today's break below the pullback low.
- **Change my mind:** Below 92.5 I go flat. Above 111 I go full.

## c89d39d177 (LTC)
- **Read:** The crash low was 92.1. The retest made a lower low at 89.3.
- **Structure:** Highs are flat to lower: 105.2 (day -27), then 104.9 (day -7). This is a range of 89 to 105.
- **Weight 0:** The low did not hold.
- **Change my mind:** A close above 105.5.

## c73d8bd359 (LINK)
- **Read:** The crash low was 87.5. The retest at 87.7 held, giving a double bottom.
- **Structure:** Highs are lower: 107.5 (day -27), then 102.2 (day -8). Price is at 100 on very light volume.
- **Weight 0.5:** The base held, but the highs are falling.
- **Change my mind:** Below 94 I go flat. Above 102.5 I would add.

## 039ce6c6a2 (SOL)
- **Read:** The crash low was 78.2. The retest at 83.3 was a clear higher low, and the rally to 109.2 (day -8) beat the day -27 high of 98.9. This is the only window with a higher high and a higher low.
- **Structure:** Price has pulled back to 100. Today's low of 98.3 dipped under the day -4 low of 99.2, and price is still below the 105 to 107 breakdown shelf.
- **Weight 0.5:** The structure qualifies for full, but today's undercut of the pullback low cuts it to half.
- **Change my mind:** Below 96 I go flat. A close above 109.5 makes it full.

{"101ad36384 (ADA)": 0.0, "cd424ff9d6 (ETH)": 0.5, "0e04cf77c0 (XRP)": 0.0, "1dcc7b2f8f (BTC)": 0.0, "ad1b0d50e1 (DOGE)": 0.0, "38744b0c58 (DOT)": 0.0, "41ac5ec73d (AVAX)": 0.5, "c89d39d177 (LTC)": 0.0, "c73d8bd359 (LINK)": 0.5, "039ce6c6a2 (SOL)": 0.5}

## Entscheidung 2026-07-19

**Strategy:** I follow the trend after the crash around day -44. I compare price to its rough 20-day and 50-day averages and check whether the recovery has made higher highs and higher lows.
- **1.0:** price is above both averages and has cleared the post-crash swing high by more than 1%.
- **0.5:** price is above the 50-day average but has not broken out.
- **0:** price is below the 50-day average with lower highs.

## 50964d8701 (ETH)
- **Read:** Crashed to 80.4 at day -43, then retested 80.8 at day -23 and held, a double bottom. It rallied through the day -34 swing high of 98.8 to 104.0 at day -4. The lows since then are higher (93.5 at -6, 96.3 at -2).
- **Averages:** 50-day about 93, 20-day about 96. Price 100 is above both.
- **Weight 1.0:** a clear breakout above the post-crash high with a higher-low structure.
- **Change mind:** a close below 93.5.

## e0b0867945 (DOGE)
- **Read:** The highs keep falling: 127.7 at day -37, 108.4 at -16, 104.1 at -5. The 50-day average is about 112 and price 100 is below it.
- **Weight 0:** still a downtrend that is only moving sideways, between 98 and 104.
- **Change mind:** a close above 104.5.

## f8ff07699c (LTC)
- **Read:** The low of 83.5 at day -25 was followed by higher lows: 87.4 at -18 and 91.2 at -6. Day -1 broke above the day -34 high of 98.5 to 101.7, on above-average volume.
- **Averages:** 50-day about 94, 20-day about 94.5. Price 100 is above both.
- **Weight 1.0:** a fresh breakout with higher lows.
- **Change mind:** a close below 92.

## ea8d3487f2 (BTC)
- **Read:** The lows are rising: 89.8 at day -24, then 95.5 at -6. Price is above the 50-day average (about 97).
- **Resistance:** the day -34 high of 104.0 has not been reclaimed; the recent highs are 100.0 and 101.4.
- **Weight 0.5:** constructive, but no breakout yet.
- **Change mind:** above 104 I go to 1.0; below 95.5 I go to 0.

## aff324f938 (AVAX)
- **Read:** The highs are falling: 110.1 at day -15, 104.8 at -5. Price 100 is below the 50-day average (about 106) and the 20-day average (about 103).
- **Range:** price is stuck between 97 and 110.
- **Weight 0:** a range with a downward tilt, under both averages.
- **Change mind:** a close above 105.

## 5a61f5bcfe (SOL)
- **Read:** A strong rebound from 78.7 to 110.0 at day -15, followed by a pullback that is holding 96 to 97 (lows of 97.0 at -6 and 96.1 at -2).
- **Averages:** price is above the 50-day average (about 96) but below the 20-day average (about 102).
- **Weight 0.5:** the uptrend is intact but the pullback is not finished.
- **Change mind:** above 104 I go to 1.0; below 96 I go to 0.

## f7406dc1ca (ADA)
- **Read:** A spike to 120.3 at day -15 failed and was fully retraced back to 100. The 50-day average is about 104 and price is below it.
- **Resistance:** the area from 102 to 105 keeps capping price.
- **Weight 0:** a failed breakout, below the trend average.
- **Change mind:** a close above 105.

## d7d7a101b3 (XRP)
- **Read:** The highs are falling: 117.8 at day -34, 107.9 at -15, 103.0 at -4. Price 100 is below the 50-day average (about 103).
- **Weight 0:** lower highs persist.
- **Change mind:** a close above 103.5.

## fcb9690e4d (DOT)
- **Read:** The highs are falling: 127.7, then 110.7, then 109.1. Day 0 was a weak close, down about 2% with a low of 98.3. Price is below the 50-day average (about 112).
- **Weight 0:** the downtrend is resuming.
- **Change mind:** a close above 107.

## df2600db52 (LINK)
- **Read:** A double bottom at 83.4 and 83.6, then a higher low of 93.0 at day -6. Price is above the 50-day average (about 94) and the 20-day average (about 95.5).
- **Breakout test:** the high of 103.0 at day -4 cleared the day -34 high of 102.6 by only 0.4%, and price closed back at 100.
- **Weight 0.5:** constructive, but the breakout is not confirmed.
- **Change mind:** above 103.5 I go to 1.0; below 93 I go to 0.

{"50964d8701 (ETH)": 1.0, "e0b0867945 (DOGE)": 0.0, "f8ff07699c (LTC)": 1.0, "ea8d3487f2 (BTC)": 0.5, "aff324f938 (AVAX)": 0.0, "5a61f5bcfe (SOL)": 0.5, "f7406dc1ca (ADA)": 0.0, "d7d7a101b3 (XRP)": 0.0, "fcb9690e4d (DOT)": 0.0, "df2600db52 (LINK)": 0.5}

## Entscheidung 2026-07-26

**Strategy:** I follow the trend using swing structure since the shared capitulation low around day −50. I go fully long (1) when the window shows higher lows and price is at or breaking above its post-crash range highs, sitting above its rising 20/50-day averages. I go half (0.5) when the range is tightening with no breakout and lows are not clearly rising. I stay flat (0) when highs keep getting lower and price is below its 50-day average.

## 7a7b2f1540 (ETH)
- **Read:** Price fell from a 123.8 peak (−100) to a capitulation low of 77.0 (−50). It retested at 77.4 (−30), forming a double bottom. Since then the lows have risen steadily: 89.5, 92.2, 94.5. Today it closed at 100 with a high of 100.6, above the 99.6/100.1 highs of the last 40 days. That is a breakout from the base. It is above its 20-day (~95) and 50-day (~88) averages. The next resistance is 103, then 108.
- **Weight:** 1.0. The breakout comes after a clean sequence of higher lows.
- **Change mind:** a close below 94.5 (the latest higher low).

## bc4c8faef3 (DOGE)
- **Read:** Price fell from a 161.6 peak to 105.8 (−50) and bounced to 126. It then made a lower low at 94.7 (−26). Highs keep falling: 126, 108.2, 102.7, and now 100.9. Lows are drifting down too: 94.7, then 93.2 at −3. It is a flat to falling range of 93–103, below its 50-day average (~110).
- **Weight:** 0. The structure is still lower highs with no higher low.
- **Change mind:** a close above 103 (would take it to 0.5) or above 108 (to 1).

## f79661dca5 (BTC)
- **Read:** Price fell from a 126.7 peak to 90.4 (−51) and made a marginal lower low at 88.9 (−31). Since then the lows have risen: 93.7, 94.5, 95.6, 97.5. However, it is capped at 102.4–102.9, where it has made matching highs. It is above its 50-day average (~96).
- **Weight:** 0.5. The base is constructive but has not broken out.
- **Change mind:** a close above 103 (to 1) or below 95.5 (to 0).

## 5fe44c0a13 (XRP)
- **Read:** Price fell from a 139.2 peak to 94.3 and then made a lower low at 90.7 (−30). Highs are falling: 116.2, 106.4, 104.6. Lows are rising: 90.7, 94.6, 96.1, 97.5. That is a converging triangle centred near 100, roughly at its 50-day average. Volume is drying up.
- **Weight:** 0.5. The setup is neutral and coiling.
- **Change mind:** a close above 104.6 (to 1) or below 96 (to 0).

## 1afd265412 (SOL)
- **Read:** Price fell from a 128.2 peak to 78.3 (−50) and then made a clearly higher low at 83.4 (−31). It followed with a higher high of 109.4 (−22), above the earlier rebound high of 99.1. The pullback held at 95.6–95.7 twice, and price is back at 100, above its 50-day average (~95). This looks like an uptrend consolidating between 95.6 and 103.
- **Weight:** 1.0. Higher lows and a higher high make this a pullback within a new uptrend.
- **Change mind:** a close below 95.5.

## fd06f65642 (DOT)
- **Read:** Price fell from a 173.7 peak to 106.8 (−50) and then made a lower low at 96.0 (−28). Highs keep falling: 109.7, 108.1, 105.6, 105.0. The lows of 96.0 and 95.0 are flat to slightly lower. That is a descending triangle, below its 50-day average (~108).
- **Weight:** 0. Lower highs are pressing on support around 95.
- **Change mind:** a close above 105.6 (to 0.5) or above 110 (to 1).

## cefb11d280 (AVAX)
- **Read:** Price fell from a 155.5 peak to 92.3, then made a lower low at 84.2 (−37) on a volume spike. It rallied to 105.5 (−22). Since then the lows have slipped: 93.6, 93.1, then 91.0 (−3). Yesterday was a strong reversal day (+7.6%, volume 1.53), and price is back at 100. It sits in a 91–105.5 range near its 50-day average (~97).
- **Weight:** 0.5. The reversal is encouraging, but the range is unresolved and the lows have been slipping.
- **Change mind:** a close above 105.5 (to 1) or below 91 (to 0).

## c93deb12dd (LTC)
- **Read:** Price fell from a 126.7 peak to 84.7 and made a slight lower low at 82.1 (−31). Since then it has climbed steadily, with higher lows at 89.7, 92.2, 95.6 and 95.9. Highs have pushed up to 100.1–100.9, and today's close of 100 is near that ceiling on decent volume. It is above its 20-day (~95) and 50-day (~92) averages. The pre-crash shelf at 106–108 is the next target.
- **Weight:** 1.0. This is the steadiest uptrend of the set and it is pressing on resistance.
- **Change mind:** a close below 95.5.

## c2949a8b34 (ADA)
- **Read:** Price fell from a 173.9 peak to 89.5, made a lower low at 83.3 (−31), then spiked to 120.5 (−22). The spike faded fully, to 93.6. Since then the lows have risen (93.6, 95.1, 97.3), but highs of 105.1 and 108.9 were sold back to 100. This is choppy action around its 50-day average (~100).
- **Weight:** 0.5. Higher lows are offset by repeated failed rallies.
- **Change mind:** a close above 109 (to 1) or below 95 (to 0).

## f606821857 (LINK)
- **Read:** Price fell from a 123.2 peak and double-bottomed at 79.3/79.4 (−50/−31). Lows have risen steadily since: 85.2, 90.7, 93.7. Today's +5.3% close at 100 cleared the 97.5–99.3 highs, putting price at a new high since the crash. It is above its 20-day and 50-day averages. The next resistance is 103–106.
- **Weight:** 1.0. A double bottom with higher lows has now broken out.
- **Change mind:** a close below 93.7.

{"7a7b2f1540 (ETH)": 1.0, "bc4c8faef3 (DOGE)": 0.0, "f79661dca5 (BTC)": 0.5, "5fe44c0a13 (XRP)": 0.5, "1afd265412 (SOL)": 1.0, "fd06f65642 (DOT)": 0.0, "cefb11d280 (AVAX)": 0.5, "c93deb12dd (LTC)": 1.0, "c2949a8b34 (ADA)": 0.5, "f606821857 (LINK)": 1.0}

## Entscheidung 2026-08-02

## Strategy

All ten windows have the same shape: a long decline, a crash around day −61 to −58, then a base. I use one rule on each. **1.0** if the base shows higher lows and higher highs and price is at or above the first post-crash bounce high (around day −48), or has broken out of its recent range on volume. **0.5** if the base holds higher lows but price is still inside the range. **0** if highs keep falling into a flat or falling floor, because that is still a downtrend.

---

### 371cf23129 (XRP)
- **Read:** Prices fell from a 120–135 plateau and crashed to 101, with a further low at 93 (day −38).
- **Structure:** The rebound highs keep falling: 119, 109, 107, 105. The lows have flattened at 96–97, so the range is narrowing below its 101 midpoint. Day 0 is a mild up day on very light volume (0.31).
- **Weight 0:** This is a compressing range inside a downtrend, with no sign of buyers taking control.
- **Change mind:** A close above 105.5 would make me take a position. A break below 96 confirms flat.

### 1f6f3ce6d4 (DOT)
- **Read:** A persistent downtrend from 208, and the rebound highs keep falling: 131, 113.6, 112, 108.8.
- **Structure:** On day −6 price broke to a new low at 93.6. Day 0 is a bounce back to 100.
- **Weight 0:** The trend is clearly down and price is making new lows.
- **Change mind:** A close above 109 would break the pattern of falling highs.

### d2a0e44a18 (LINK)
- **Read:** A double bottom at about 84 (days −58 and −38), followed by a steady climb.
- **Structure:** Lows are rising: 89.7, 93, 95.5, 97.4. Highs are also rising: 102.6, 103, 104.5, 106.3. Price at 100 sits just below the 102.6–106 resistance band.
- **Weight 0.5:** The structure is constructive, but price has not broken out yet.
- **Change mind:** A close above 106.5 moves me to 1. A close below 94 moves me to 0.

### 6bfff59b12 (SOL)
- **Read:** A crash to 81.7, then a sharp rebound to 114 (day −29). Since then price has pulled back to about 100.
- **Structure:** Lows are rising: 81.7, 87, 99.7. Recent highs are slightly lower: 107, 105. Day −1 dipped to 95.9.
- **Weight 0.5:** The large base is intact, but price is drifting in the middle of the range.
- **Change mind:** A close above 107 moves me to 1. A close below 95.9 moves me to 0.

### c36be00736 (AVAX)
- **Read:** A fall from 156, a low at 86.7 (day −44), and a 91–108 range since then.
- **Structure:** Lows are holding at 92–96, while highs are drifting lower: 108.6, 104.5. Day 0 is a strong reversal from 94.5 to 100 on about twice recent volume, with an intraday high of 102.
- **Weight 0.5:** The floor is holding and buyers showed up on day 0, but the highs are still lower.
- **Change mind:** A close above 104.5 moves me to 1. A close below 92 moves me to 0.

### e2a91945db (LTC)
- **Read:** A crash low at 87.9 (day −38), followed by a clean staircase higher.
- **Structure:** Lows are rising: 96.6, 96.0, 98.7, 99.2. The highs reached 108 (day −7), above the 103.6 bounce high. Price at 100 is a pullback in an uptrend.
- **Weight 0.5:** The structure is healthy, but price is back below the 103.6 breakout level.
- **Change mind:** A close above 104 moves me to 1. A close below 96 moves me to 0.

### e8ace72f09 (ADA)
- **Read:** The deepest crash of the set, to 72.9. A spike to 105.5 (day −29) was followed by a retest to 81 (day −6), which held well above the low.
- **Structure:** Day 0 broke out of the 82–95 range with a close at 100 on 1.73 volume, and both the last two days were strong.
- **Weight 1:** This is a higher low followed by a volume breakout, the clearest momentum signal in the set. The next resistance is 105.5.
- **Change mind:** A close back below 91, inside the old range, would take me out.

### a3cc03c062 (BTC)
- **Read:** A shallower decline than the others, from the 115–128 area to lows at 91–93.
- **Structure:** Lows have risen steadily: 96.4, 97.3, 98.4, 99.3, 98.0. Price is in a tight 98–105.9 range, with resistance at 105.3–105.9.
- **Weight 0.5:** The base is constructive but price has not broken out.
- **Change mind:** A close above 106 moves me to 1. A close below 97 moves me to 0.

### be306a519c (DOGE)
- **Read:** A fall from 167 (day −80) to a low near 98 (day −33).
- **Structure:** Highs keep falling: 112, 106.5, 104.6. Lows have been retested at 96.6 and 95.6. Day 0 has low volume (0.34).
- **Weight 0:** The pattern is a descending triangle inside a downtrend.
- **Change mind:** A close above 105 would make me take a position.

### e2950fd527 (ETH)
- **Read:** A double bottom near 80 (days −57 and −37), followed by a rising trend.
- **Structure:** Lows are rising: 90.9, 92.8, 95.6, 98.0, 96.6. Highs are also rising: 97.2, 103.2, 103.8, 105.1. Price at 100 holds above the 98 bounce high from day −48.
- **Weight 1:** The base is confirmed and price is trading above its first rebound high.
- **Change mind:** A close below 96.5 would break the higher-low sequence and take me out.

---

{"371cf23129 (XRP)": 0.0, "1f6f3ce6d4 (DOT)": 0.0, "d2a0e44a18 (LINK)": 0.5, "6bfff59b12 (SOL)": 0.5, "c36be00736 (AVAX)": 0.5, "e2a91945db (LTC)": 0.5, "e8ace72f09 (ADA)": 1.0, "a3cc03c062 (BTC)": 0.5, "be306a519c (DOGE)": 0.0, "e2950fd527 (ETH)": 1.0}

## Entscheidung 2026-08-09

**Strategy:** I go long when the window shows a recovering structure: higher lows since the major low, a close above its rising ~50-day zone, and expanding range or volume on up-moves. I use half weight when price is basing in a range but above that zone, and go flat when the recent sequence is lower highs and lower lows or the longer-term downtrend still dominates. Each window gets explicit levels for upgrading or cutting.

## e5d110c58a (LINK)
- **Read:** The peak was ~131 at day -91. It crashed to 85.5 at -64, then retested 85.6 at -45. It recovered to 108 at -14 and has since ranged 96–104 on drying volume. The lows are rising (86 → 92 → 96.3), but price sits well under old support near 110.
- **Weight: 0.5.** The structure is constructive basing, but there is no breakout yet.
- **Change of mind:** a close above 108 (go to 1), or below 96 (go to 0).

## 8794b06db5 (BTC)
- **Read:** The peak was 127.7, with crash lows at 91.1 and 89.5. It rebounded to 103 and has held a 96–103 range for a month, with a higher low at 96.0 on day -8. It is quiet and constructive but capped near 103.
- **Weight: 0.5.**
- **Change of mind:** above 103.5 (go to 1), or below 96 (go to 0).

## 58b06039a4 (ADA)
- **Read:** The crash ran from ~148 to a 71.1 low at -45. A V-thrust took it to 102.8, a retest held at 79.9, and a second thrust reached a higher high at 108.8 on day -3, with strong volume on the up-legs (1.8–2.4). Both highs and lows are rising. The current pullback to 100 is a normal retrace inside that trend. It is volatile, but this is the clearest momentum structure in the set.
- **Weight: 1.0.**
- **Change of mind:** a close below 93 (the day -6 low) breaks the higher-low sequence, so go to 0.

## d01e0f28b1 (SOL)
- **Read:** The crash low was 78.8. It recovered to 110 at -36, then made lower highs (110 → 103.6 → 101.6) and lower lows down to 92.5 at -8. The last day's push back to 100 tests the top of that drift. It is still far above the crash low, so the decline is a pullback rather than a breakdown.
- **Weight: 0.5.** The intermediate trend is up, but the short-term trend has been down.
- **Change of mind:** above 103.6 (go to 1), or below 94 (go to 0).

## aea01b7b52 (DOT)
- **Read:** The dominant trend is down: from 208 (day -165) to ~99.5, with every rally failing lower (173, 131, 113). The day -13 gap down to 93.6 recovered to 108.9 and then faded back to 100. Price sits in a 93.6–113 range under declining resistance.
- **Weight: 0.**
- **Change of mind:** a close above 113 (go to 0.5).

## 1ae24da4a9 (AVAX)
- **Read:** The longer-term trend fell from ~163 to a 96.9 crash low and an 88.5 capitulation low at -51 on 3.5x volume. Since then it has ranged 94–111 for 50 days with slowly rising lows (88.5 → 92.7 → 94.1). Price is mid-range.
- **Weight: 0.5.**
- **Change of mind:** above 111 (go to 1), or below 94 (go to 0).

## 99ab93303c (XRP)
- **Read:** After the crash low of 102, it bounced to 125.6, slid to 98 at -45, and rallied to 115. Since then it has made lower highs (113.1, 108.3, 106.2) and lower lows. Day -2 at 98.3 broke under the 101.5–103 shelf, so the short-term trend is down.
- **Weight: 0.**
- **Change of mind:** a close above 108 (go to 0.5).

## b0ed106221 (LTC)
- **Read:** The crash low was 86.4, retested at -45. Since then there is a steady staircase of higher lows (86.4 → 90.5 → 94.4 → 96.0) and a high of 106.2 at -14, with heavier volume on the advance (days -25 to -20). The current price of 100–101 is a pullback inside the uptrend, though it is still well under the 120s.
- **Weight: 0.5.**
- **Change of mind:** above 106.2 (go to 1), or below 96 (go to 0).

## 7dc3dd5518 (DOGE)
- **Read:** The peak was 171. It crashed to 112, bounced to 133, and dropped to 103. Since the 114.5 high at -36 it has made lower highs (108.7, 106.8, 103.2) and is coiling at 98–103 on very thin volume. It sits below its ~105 mid-term average with a downward bias.
- **Weight: 0.**
- **Change of mind:** a close above 107 (go to 0.5).

## 72b16ab160 (ETH)
- **Read:** There was a double bottom at 78.8 / 79.1. Since then lows have risen (89.7 → 91.6 → 95.4) and it reached 101.9 at -25. It has ranged 95.4–103.7 for a month, sitting at the upper half, above its rising ~50-day zone near 92.
- **Weight: 0.5.**
- **Change of mind:** above 103.7 (go to 1), or below 95.4 (go to 0).

{"e5d110c58a (LINK)": 0.5, "8794b06db5 (BTC)": 0.5, "58b06039a4 (ADA)": 1.0, "d01e0f28b1 (SOL)": 0.5, "aea01b7b52 (DOT)": 0.0, "1ae24da4a9 (AVAX)": 0.5, "99ab93303c (XRP)": 0.0, "b0ed106221 (LTC)": 0.5, "7dc3dd5518 (DOGE)": 0.0, "72b16ab160 (ETH)": 0.5}

## Entscheidung 2026-08-16

**Strategy:** I follow the trend and act only on confirmed structure. I go fully long (1) when price has broken out of a base or is making higher highs and higher lows above its recent trading range. I hold half (0.5) when a recovery shows higher lows but no breakout yet. I stay flat (0) when the trend is down or the market is chopping in a range of lower highs.

### b52249990d (DOGE)
- **Read:** Long decline from about 165 (day -94) to about 100. The crash at day -72 kept going down to 99.9. Since then price has moved sideways between 98 and 106 for about 50 days. Volume is drying up and there is no sign of buyers returning. Price is below the range midpoint and well below every higher-timeframe level.
- **Weight:** 0. This is a downtrend with no reversal.
- **Change mind:** A close above 106.5, which breaks the base.

### 2c017711a5 (ETH)
- **Read:** The crash from about 127 bottomed at 80.3 (day -71). Higher lows followed at 80.6, then about 91 (day -39), then 97 (day -15). Price recovered to about 100 and has held between 97 and 104 for a month. The recovery is intact, but resistance at 104–105 has not been cleared.
- **Weight:** 0.5. The structure is constructive but there is no breakout.
- **Change mind:** Below 97 I go to 0. Above 105 I go to 1.

### b60511f312 (DOT)
- **Read:** A persistent bear market, from about 220 down to 100, with lower highs all the way. The bounce to 114.6 (day -12) failed and gave back everything.
- **Weight:** 0. This is a clear downtrend.
- **Change mind:** A close above 115.

### 512930ab47 (XRP)
- **Read:** A steady decline from about 150 to 100. The highs keep stepping down: 130, 119, 117, 112, 110. Price is now at the lows of the last 50 days.
- **Weight:** 0. Lower highs and lower lows.
- **Change mind:** A close above 110.

### 54d5e4ce0f (ADA)
- **Read:** A crash from about 135 to a low of 79 (day -52). It rallied hard to 121 (day -10), a higher high above 114 (day -43), and the lows have risen from 79 to 88. Price has now pulled back sharply for 8 days to 100. The trend is rising but the pullback is deep.
- **Weight:** 0.5. The structure is improving, but momentum is fading.
- **Change mind:** Below 95 I go to 0. A recovery above 110 sends me to 1.

### 6d44c8de06 (BTC)
- **Read:** The decline from about 131 crashed to 94 (day -72). Since then price has ranged 92–106 with lower highs: 106.4, then 104.6, then 104.0. It now sits at the bottom of the 99–104 band.
- **Weight:** 0. The range is weak and the larger trend is down.
- **Change mind:** A close above 104.5.

### 3a61f79b05 (LINK)
- **Read:** A crash from about 115 to 74.5 was followed by a 70-day base between 75 and 92. In the last week price broke above 92–95, and it pushed through to 103.8 on day -1 with high volume (1.66). That is the strongest level since day -88. Price is holding about 100.
- **Weight:** 1. A base breakout on volume.
- **Change mind:** A close back below 92, which means the breakout failed.

### addcd31c59 (LTC)
- **Read:** A crash from about 137 to 91.8. Lows have been higher since: 88.9, 97.2, 98.3. Price recovered to 109 (day -21) and has since pulled back to 100, holding the 98–99 support area. The high at 109 is far below the old peak.
- **Weight:** 0.5. Higher lows, but it is in a pullback.
- **Change mind:** Below 98 I go to 0. Above 105 I go to 1.

### 92e1d31e3c (AVAX)
- **Read:** A crash from about 165 to 98, then a deeper low of 89.7 (day -58). Since then price has chopped between 97 and 110 with repeated rejections: 112, 110.4, and 108.6 on day -1, which was a failed spike on 1.38 volume. Price is in the middle of the range.
- **Weight:** 0. The range is choppy and there is selling at the highs.
- **Change mind:** A close above 110.5.

### 255113ba0a (SOL)
- **Read:** A crash from about 131 to 80.6, a rally to 112.6 (day -43), and then a slide with lower highs: 112, 105.9, 104.3. The low was 94.6 at day -15. Price is now in a tight band between 97 and 104 at about 100.
- **Weight:** 0. Lower highs and no trend.
- **Change mind:** A close above 104.5.

{"b52249990d (DOGE)": 0.0, "2c017711a5 (ETH)": 0.5, "b60511f312 (DOT)": 0.0, "512930ab47 (XRP)": 0.0, "54d5e4ce0f (ADA)": 0.5, "6d44c8de06 (BTC)": 0.0, "3a61f79b05 (LINK)": 1.0, "addcd31c59 (LTC)": 0.5, "92e1d31e3c (AVAX)": 0.0, "255113ba0a (SOL)": 0.0}

## Entscheidung 2026-08-23

**Strategy:** I go long only when a stock breaks out of its post-crash base. I take a full position (1) if the breakout is holding without a reversal. I take half (0.5) if the latest day was a high-volume blow-off with a long upper wick. I stay flat (0) if the move is a climactic surge of more than 40% in a week on extreme volume, or if the spike was rejected at a prior lower high in a long-term downtrend.

### ea4b9ea388 (LTC)
- **Read:** The pre-crash range was 100–108. The crash bottomed at 77, then price based between 80 and 90. It then spiked from 85 to 101.7, about +18% in three days. Day -1 hit 106.1 and closed at 100.3 on the highest volume in the window (3.21), a blow-off wick right at the old breakdown zone of 100–104.
- **Weight:** 0.5. The breakout is real, but it is stalling at the pre-crash resistance on exhaustion volume.
- **Change my mind:** A close below 96 takes me to 0. A close above 106 takes me to 1.

### 34a3beba36 (ETH)
- **Read:** Price based between 75 and 78 for about 40 days on very low volume. It then broke out by about +28% to 102 on heavy volume, and now sits at the window highs (100.1 at -128, 103.4 at -2). Day -1 was a lower-high pullback on lighter volume, not a blow-off. Support is at 94–96.
- **Weight:** 1. This is a clean base breakout to multi-month highs, and the pullback is orderly.
- **Change my mind:** A close below 94 cuts me to 0.5. A close below 90 takes me to 0.

### 3d0037f864 (BTC)
- **Read:** The base ran from 81 to 84. Price broke out to 100.8, about +20%. Days -1 and 0 were tight inside candles on falling volume (1.05, then 0.87), which is constructive consolidation. Next resistance is the pre-crash 104–106 area.
- **Weight:** 1. The breakout is holding and there is no exhaustion signal.
- **Change my mind:** A close below 97 cuts me to 0.5. A close below 93 takes me to 0.

### 87698a6f0c (AVAX)
- **Read:** The long-term trend is down: price was 117–138 before the crash and based between 81 and 91 afterward. It spiked to 103 and cleared the base high near 93. Day -1 ran from 109.3 down to 92.0 and closed at 98.5, a wide blow-off reversal on 2.49 volume.
- **Weight:** 0.5. The breakout above the base counts, but the reversal candle and the heavy supply overhead argue for caution.
- **Change my mind:** A close below 92 takes me to 0. A close above 109 takes me to 1.

### d4a08e08e5 (XRP)
- **Read:** The base kept drifting lower, from 72 to 65. Price then went nearly vertical, up 52% from 65.9 to 100 in four days. Day -1 hit 111.8, dropped to 90.6 and closed at 96.2 on 5.98× volume, which is a climactic blow-off. The pre-crash range was 87–97.
- **Weight:** 0. The move is extremely extended on climax volume, so mean-reversion risk dominates.
- **Change my mind:** Above 112 I go to 0.5. The pullback-entry level would be around 88–90 if it holds.

### bbf47b1c7f (LINK)
- **Read:** The base was 70–73, followed by a higher-low ramp from 76 to 82 starting at -12. Price then broke out to 103.9, clearing all levels since -160 (the 94 pre-crash high). Day -1 went from 109.3 to 94.7 and closed at 100.9 on 2.86 volume, a blow-off wick.
- **Weight:** 0.5. The breakout to multi-month highs is good structure, but the wick says take only half.
- **Change my mind:** A close below 94.5 takes me to 0. A close above 109.5 takes me to 1.

### b2d7c66f0a (DOGE)
- **Read:** The base was very tight at 74–75, then price spiked about 33% to 98. Day -1 went from 107.9 to 88.8 and closed at 98.4 on 3.46 volume, a blow-off. The pre-crash range of 106–123 sits overhead.
- **Weight:** 0.5. The breakout from the coil is valid, but it came with an exhaustion candle.
- **Change my mind:** A close below 89 takes me to 0. A close above 108 takes me to 1.

### d6757377fc (DOT)
- **Read:** This is a persistent downtrend from 179 to 82, with lower highs at 150, then 112.8, then 97, then 93.8. Price spiked from 81 to 101. Day -1 hit 111.2, right at the post-crash lower high near 112.8, was rejected, and closed at 99.1.
- **Weight:** 0. The spike failed at descending resistance inside a primary downtrend.
- **Change my mind:** A close above 113 takes me to 0.5.

### 33f4dbea28 (SOL)
- **Read:** The base was 76–81, then price spiked about 25% to 98. Day -1 went from 107.7 to 91.9 and closed at 98.3 on 2.83 volume, a blow-off. Price is now inside the pre-crash range of 85–102.
- **Weight:** 0.5. The base breakout is valid, but the exhaustion wick tempers it.
- **Change my mind:** A close below 92 takes me to 0. A close above 108 takes me to 1.

### 9bfaf5a43f (ADA)
- **Read:** After the crash low near 61–65, earlier rallies to 88 (at -50) and 93 (at -17) both failed. This spike cleared both and reached 100.9. Day -1 went from 113.8 to 92.0 and closed at 99.6 on 3.0 volume, a blow-off. The pre-crash range of 100–125 sits overhead.
- **Weight:** 0.5. Clearing the failed-rally highs is constructive, but the reversal wick says take only half.
- **Change my mind:** A close below 92 takes me to 0. A close above 114 takes me to 1.

{"ea4b9ea388 (LTC)": 0.5, "34a3beba36 (ETH)": 1.0, "3d0037f864 (BTC)": 1.0, "87698a6f0c (AVAX)": 0.5, "d4a08e08e5 (XRP)": 0.0, "bbf47b1c7f (LINK)": 0.5, "b2d7c66f0a (DOGE)": 0.5, "d6757377fc (DOT)": 0.0, "33f4dbea28 (SOL)": 0.5, "9bfaf5a43f (ADA)": 0.5}

## Entscheidung 2026-08-30

**Strategy:** I go long when the post-breakout consolidation holds above the pre-breakout base and above earlier swing highs in the window. I cut to half when a fading spike sits inside a larger range. I go flat when the long-term structure is lower highs and the spike has given back most of its gain. Key levels are the base under the breakout (about days -11/-12), the consolidation range since day -8, and swing highs earlier in the window.

## 415c6bcfbe (LINK)
- **Read:** The window started near 80. It peaked at 96 (day -112), crashed to about 64 (day -86), then based at 65–77. It broke out from 74 to 85 and then to a 113 peak, and the consolidation since has held a 98.6–108 range.
- **Structure:** Price is above every earlier high in the window, including 96. The pullback is orderly and volume is fading on down days.
- **Weight:** 1.0. The breakout to new window highs is holding.
- **Change my mind:** A close below 97, which loses the range and the old 96 high.

## 1e1a6ef57f (XRP)
- **Read:** The old range was 95–114. The crash went to 77, then a lower base formed at 73–76.
- **Spike:** It ran to 125 on 6x volume but closed at 107, which looks like a blow-off.
- **Structure:** Lower highs since then: 114, 109, 107, 103. Price is now 100, mid-way through the old range.
- **Weight:** 0.5. The breakout is real, but it shows exhaustion and drift.
- **Change my mind:** Flat below 98; full above 108.

## cf4d55863f (ETH)
- **Read:** The earlier top zone was 98–102 (days -139 to -116). The crash went to 62, and the base sat at 77–80.
- **Breakout:** It broke out to 106. It is now retesting the old 98–100 top from above, with the range low at 98.8.
- **Weight:** 1.0. Old resistance is acting as support.
- **Change my mind:** A close below 97.

## 4bcb32eaca (DOGE)
- **Read:** The bigger trend is down: 144 (day -108), then 112, then 96, with a base at 84–86.
- **Spike:** It reached 123 intraday and has since faded with lower highs (114, 113, 110, 104.5). Price has retraced about 60% of the spike.
- **Structure:** It did break the lower-high sequence by clearing 96.
- **Weight:** 0.5. The structure has improved but the momentum is fading.
- **Change my mind:** Flat below 98; full above 110.

## 58dc99264a (SOL)
- **Read:** The old highs were about 96. The crash went to 59, and the base was 72–76.
- **Breakout:** The advance is stepwise with higher highs: 101, then 108.7 (day -3). Price is now 100 on a routine pullback, above the 96 level.
- **Weight:** 1.0. This is the cleanest uptrend structure of the set.
- **Change my mind:** A close below 97, which would confirm a failed higher high back under the old 96 high.

## ef7d39148f (DOT)
- **Read:** This is a persistent downtrend from 200 to 92, with lower highs at 175, 164, 128, 110 and 106.
- **Spike:** It went to 126 intraday and has fully faded to 100, back below the 106–110 swing highs.
- **Weight:** 0.0. The primary trend is down and the spike failed.
- **Change my mind:** A close above 110.

## ec9c2e2931 (LTC)
- **Read:** The old range was 108–126. The crash went to 84, the recovery reached about 100 (days -43 to -35), and price then dipped to 91.
- **Spike:** It went to 115.7, followed by steady lower highs (113, 110.5, 106, 105, 103). Price is now testing the prior 100 high.
- **Weight:** 0.5. Support is being tested and momentum is waning.
- **Change my mind:** Flat below 98; full above 106.

## be381b514f (AVAX)
- **Read:** The old range was 120–147. The crash went to 80, and the base was 85–98.
- **Spike:** It reached 117 intraday and is now at 100, back at the prior 98–100 swing highs.
- **Structure:** Price is still far below the long-term range.
- **Weight:** 0.5. It is holding the breakout level but sits inside a broader downtrend.
- **Change my mind:** Flat below 97; full above 107.

## 44fdb762e6 (ADA)
- **Read:** The trend is down from 150 to 72. Rallies to 104 (day -57) and 110 (day -24) both failed.
- **Spike:** The latest spike reached 134 intraday on day -8. Closes have faded steadily since: 119, 117.8, 114.9, 108.5, 110.2, 110.9, 105.4, 104.7, now 100.
- **Weight:** 0.0. There is a repeated pattern of failed spikes inside a downtrend.
- **Change my mind:** A close above 111.

## 2ab82aefbd (BTC)
- **Read:** The window started near 88 and rose to 106 (day -112). The crash went to 76, and the base was 80–85.
- **Breakout:** It broke out in an orderly way to 104.9 with no blow-off wick. The consolidation is a tight 97–105 range with shrinking volume, and price is near the old 106 high.
- **Weight:** 1.0. This is a constructive base right under resistance.
- **Change my mind:** A close below 97.

{"415c6bcfbe (LINK)": 1.0, "1e1a6ef57f (XRP)": 0.5, "cf4d55863f (ETH)": 1.0, "4bcb32eaca (DOGE)": 0.5, "58dc99264a (SOL)": 1.0, "ef7d39148f (DOT)": 0.0, "ec9c2e2931 (LTC)": 0.5, "be381b514f (AVAX)": 0.5, "44fdb762e6 (ADA)": 0.0, "2ab82aefbd (BTC)": 1.0}

## Entscheidung 2026-09-06

**Strategy.** I apply one trend and structure rule to every window: go fully long (1.0) when price has broken out of a post-crash base and is at or near its highest closes since the crash, with a higher low on the pullback. Use half (0.5) when the breakout is intact but price is still below a blow-off spike or a rejected wick that acts as overhead supply. Go flat (0) only when price is back inside or below the base, which means the breakout failed.

## 1bbeff8803 (ADA)
- **Read:** The pre-crash range was 105–120. Price crashed to about 66 around day -92 and spent roughly 20 days basing at 78–81. On days -17 to -16 it broke out to 102.6, leaving a spike wick at 115.7. The pullback held at 84.8, a higher low, and price has since rallied back to 100. That is the highest close since day -16. Volatility is high.
- **Weight:** 1.0. The trend is up, the higher low is intact and price is reclaiming the breakout level.
- **Change my mind:** a close below 86.

## d79d017cf1 (AVAX)
- **Read:** The pre-crash range was 113–125. After the crash price based at 78–88 for months, then broke out to 99.1 with a 105.2 wick. The pullback held at 88.7, and the 100 close is the highest close since day -96. The last four sessions show steady higher closes.
- **Weight:** 1.0. This is a clean breakout continuation.
- **Change my mind:** a close below 89.

## d4ec05ddd5 (DOT)
- **Read:** This is a long decline from about 155 to about 74, followed by a spike to 96 with a 105.4 wick. The pullback held at 82.5, then came six straight higher closes. Today closed at 100 on 1.67× volume, the highest close since day -97. The decline from 155 is overhead supply, but short-term structure has turned up.
- **Weight:** 1.0. The volume breakout is backed by a higher low.
- **Change my mind:** a close below 85.

## 05606f2d29 (ETH)
- **Read:** The pre-crash range was 80–98. Price crashed to 60, then based at 74–76 with very low volume. A gap-up to 100 followed, and price has held a tight 94–102 range for two weeks. It is above all pre-crash highs (98), and today's close of 100 sits near the top of that range.
- **Weight:** 1.0. The breakout is holding firmly above the old range.
- **Change my mind:** a close below 93.5.

## 50dbf162c6 (LTC)
- **Read:** The pre-crash range was 95–110. Price crashed to 73.7, based at 79–87, and spiked to 100.9 on day -15. The pullback held at 86.2, then day -1 broke out on 2.32× volume and today held 100. Price is back at the pre-crash level, with resistance at 101 and then 105–110.
- **Weight:** 1.0. The high-volume breakout came after a higher low.
- **Change my mind:** a close below 92.

## abc9eaecea (SOL)
- **Read:** The pre-crash range was 75–92. Price crashed to 56.4 and based at 67–73, then broke out from day -18 and made a high of 103.8 on day -10. The pullback held at 91.4, which is above the pre-crash high of 92. Price is now 100. This is a strong trend.
- **Weight:** 1.0.
- **Change my mind:** a close below 91.

## d8caaed127 (BTC)
- **Read:** The pre-crash range was 85–103. Price crashed to 73.6 and based at 78–81. The breakout reached 97.5 on day -16, and price has since consolidated at 95–102 for two weeks with low volume. Today closed at 100, just under the 101–103 pre-crash highs. The structure is a tight bull flag.
- **Weight:** 1.0.
- **Change my mind:** a close below 95.

## 6a418158b3 (LINK)
- **Read:** The pre-crash range was 64–82. Price crashed to 52.9, based at 54–65, and has been rising since day -26. It spiked to 95.4, pulled back with a higher low at 82.4, and today broke out to 100 on 1.7× volume. That is a new 180-day high, so there is no overhead supply.
- **Weight:** 1.0. This is the strongest setup of the set.
- **Change my mind:** a close below 87.

## 70e25c8127 (XRP)
- **Read:** The pre-crash range was 90–108. Price drifted down to about 69, then had a blow-off spike to a 119.4 wick on 6× volume. The highest close was 106.8 on day -14. Price has since faded to 92 and recovered to 100, but volume is now falling (0.7). Closes of 102–107 and the climactic wick sit overhead.
- **Weight:** 0.5. The breakout is intact, but the blow-off top caps it.
- **Change my mind:** above 107 I would go to 1.0. Below 92 I would go to 0.

## 1605d4ad2b (DOGE)
- **Read:** The pre-crash range was 100–130. Price kept declining to a 74.4 low, then spiked to a 110.9 wick, and the highest close was 102.7. The pullback held at 88.1. Day -1 printed a 104.7 wick that was rejected, and price is now 100, still below the post-spike closing highs. There is heavy supply above from the old range.
- **Weight:** 0.5.
- **Change my mind:** above 105 I would go to 1.0. Below 88 I would go to 0.

{"1bbeff8803 (ADA)": 1.0, "d79d017cf1 (AVAX)": 1.0, "d4ec05ddd5 (DOT)": 1.0, "05606f2d29 (ETH)": 1.0, "50dbf162c6 (LTC)": 1.0, "abc9eaecea (SOL)": 1.0, "d8caaed127 (BTC)": 1.0, "6a418158b3 (LINK)": 1.0, "70e25c8127 (XRP)": 0.5, "1605d4ad2b (DOGE)": 0.5}

## Entscheidung 2026-09-13

**Strategy:** Trend-following on breakouts. If price holds above the post-breakout support and swing highs inside the consolidation are flat or rising, go 1.0. If price is above support but the structure is damaged (lower highs pressing on the range floor, or a rejected blow-off spike), go 0.5. If price closes below breakout support, go 0.

## 232946c875 (SOL)
- **Read:** Price fell from about 95 to 64, based at 72–78 for two months, then broke out on heavy volume (day −25) to 111.4. It has consolidated at 98–108 for three weeks with lows holding 98–99 and swing highs roughly flat (106.7, 108.1, 106.5). The close of 100 is at the range floor, but the structure is intact.
- **Weight:** 1.0. Breakout held, the range is constructive, and price sits well above the base.
- **Change my mind:** a close below 97.5.

## e7019ecafa (DOT)
- **Read:** The first breakout to 103 faded back to 81. A second spike to 128.5 on 4× volume (days −6/−5) then fully unwound to 100 within four days. That is a classic blow-off rejection, though price is still well above the 75–88 base.
- **Weight:** 0.5. The trend is up from the low, but the distribution spike is a warning.
- **Change my mind:** below 95 means flat; reclaiming 110 means full.

## 8eceb4c225 (ADA)
- **Read:** Spike from 86 to 127, then a 93–114 range. Lows are rising (93.1, 97.8, 98.5) and highs are rising (110.7, 111.6, 114.1). Close 100 is mid-to-low in the range.
- **Weight:** 1.0. Higher-low/higher-high structure with the breakout intact.
- **Change my mind:** below 97.

## dfd442e042 (XRP)
- **Read:** Largest breakout in the set, 74.7 to 126.7 on 6× volume. Since then highs have been lower (110.6, 108.2, 106.9) and lows are flat around 98–99.6. Price is pressing the floor at 100.
- **Weight:** 0.5. Still far above the base, but the range is compressing downward.
- **Change my mind:** below 97.5 means flat; above 108 means full.

## feaf0e469f (AVAX)
- **Read:** Broke out of the 85–92 base to 114, then ranged 96–112. Lows are rising (96.2, 96.6, 99.8) and the highs at days −6/−5 (112.5) exceeded the day −10 high (104). Pulled back to 100.
- **Weight:** 1.0. Higher lows and higher highs.
- **Change my mind:** below 96.

## 52e6b7b83a (LTC)
- **Read:** Broke out of the 82–85 base to 103, retested 88, then made a higher low and pushed to 110.6 (wick). Lows are stepping up (88.2, 96.0, 99.1). Price is reclaiming the pre-crash 100–105 zone.
- **Weight:** 1.0. Clear higher-low staircase.
- **Change my mind:** below 96.

## 145f2fbd1b (LINK)
- **Read:** Strongest prior trend in the set, from a 62.4 low to a 112 breakout. But the day −7/−6 spike to 122.2 was rejected sharply back to 100, below its 107 origin.
- **Weight:** 0.5. The trend is intact, but the spike failure argues against full size.
- **Change my mind:** below 97 means flat; above 110 means full.

## ec47195639 (DOGE)
- **Read:** Broke out of the 83–89 base to 122, then ranged 97–115. Lows are holding (97.2, 99.9, 99.9) and highs are 109, then 115.5, then 111. Close 100 at range support.
- **Weight:** 1.0. The range is intact and highs are not deteriorating materially.
- **Change my mind:** below 97.

## 4042ca9281 (ETH)
- **Read:** Broke out from 61 to 77 and then to 102.8, followed by a tight 95–103 shelf for 20 days. Lows are rising (95.1, 97.1, 98.3). The day −2 wick to 107.6 was rejected but closed in the range.
- **Weight:** 1.0. Tight consolidation above the breakout is constructive.
- **Change my mind:** below 95.

## 850fcb4562 (BTC)
- **Read:** Broke out of the 82–84 base to 103.5 into the old 100–107 supply zone. Highs are lower (107.1, 104.8, 104.0) and lows are flat around 99. Low-volatility drift at the floor, at 100.
- **Weight:** 0.5. It is holding, but making no progress beneath overhead supply.
- **Change my mind:** below 98.5 means flat; above 105 means full.

{"232946c875 (SOL)": 1.0, "e7019ecafa (DOT)": 0.5, "8eceb4c225 (ADA)": 1.0, "dfd442e042 (XRP)": 0.5, "feaf0e469f (AVAX)": 1.0, "52e6b7b83a (LTC)": 1.0, "145f2fbd1b (LINK)": 0.5, "ec47195639 (DOGE)": 1.0, "4042ca9281 (ETH)": 1.0, "850fcb4562 (BTC)": 0.5}

## Entscheidung 2026-09-20

**Strategy:** I go fully long (1) when price is at or near new 180-day highs and the swing lows since the breakout are rising. I go half (0.5) when price has broken out of its base but is still inside a choppy range below major overhead highs, or when the move is so extended that a pullback is likely. I go flat (0) when price is in a downtrend below broken support.

---

**83cf71dfdb (DOGE)**
- **Read:** Topped near 135 (day -129) and collapsed to a long base at 78–82. A breakout at day -32 spiked to 115.5 and failed. Since then it has chopped between about 90 and 109, and the latest low (89.8) is slightly below the prior one (92.6). It sits at 100, mid-range and far below the 130s.
- **Weight:** 0.5. The breakout from the base is intact, but there is no trend inside the range.
- **Change of mind:** Close above 105 → 1; close below 89.5 → 0.

**966d3dbd2b (BTC)**
- **Read:** The range high was about 102 (day -137). It fell to 72.8, based at 72–82, and broke out at day -32 to 97. Since then it has held a tight 92–101 range with lows holding (93.7, 92.4) and now closes at 100, at the top of that range and just below the 180-day high.
- **Weight:** 1. A clean breakout with a tight, steadily rising consolidation.
- **Change of mind:** Close below 92.

**7cce848f7a (SOL)**
- **Read:** The prior 180-day high was 88.5 (day -133). It based at 64–70, broke out at day -32, consolidated at 86–96, and broke out again at day -2 to 102.8. It is at new highs.
- **Weight:** 1. Higher highs, with the consolidation resolving upward.
- **Change of mind:** Close below 86.

**aaafbc96a9 (LINK)**
- **Read:** It climbed steadily from a 64–66 base (day -50) to a spike at 109.3 (day -13), pulled back to 84.8, and has recovered to 100. It is well above the old 86.8 high, and the larger trend is up.
- **Weight:** 1. The trend is intact, and the pullback held well above the breakout zone.
- **Change of mind:** Close below 84.

**6de7752c48 (ADA)**
- **Read:** It peaked at 126.7 and crashed to 61. Rallies failed at 87 and 93, then a breakout spike reached 113.4 (day -29) and faded. It now ranges between 83 and 103, with a double bottom near 83 (days -21 and -4), and sits at 100. That is under resistance around 102–103 and well below the 117–126 highs.
- **Weight:** 0.5. The range is constructive but has no confirmed upward trend.
- **Change of mind:** Close above 104 → 1; close below 83 → 0.

**7e6addfaa0 (XRP)**
- **Read:** It traded in a 92–110 range early in the window, crashed to 70, and based there. A blow-off spike at day -29 reached 120.5, followed by a 89–106 range. The swings are violent: up to 106 at day -6, down to 89.7 at day -5, and now back to 100. Price is pressing into the old 100–105 resistance zone.
- **Weight:** 0.5. The swings are too large and the resistance too close to go fully long.
- **Change of mind:** Close above 106 → 1; close below 89 → 0.

**02711c6287 (AVAX)**
- **Read:** The 180-day high was 92.7 (day -133). It crashed to 50 and based at 54–60. Price then moved from 67 to 100 in two days on 3.9x and 6.1x volume, closing near the day's high of 101.4. That is a new 180-day high, but the move is roughly 50% above its 20-day average.
- **Weight:** 0.5. The breakout momentum is strong, but the move is extremely stretched and likely to retest.
- **Change of mind:** If it consolidates above 90 → 1; if it closes below 83.4 (day 0 low) → 0.

**0c4455241a (LTC)**
- **Read:** The 180-day high was 103.2 (day -133). It based at 70–78 and has climbed in a clean staircase since: highs at 94.4, then 101.2, then 101.1, and lows at 80.7, then 85.5. It is at 100, just under the window high.
- **Weight:** 1. Higher highs and higher lows, pressing on the high.
- **Change of mind:** Close below 85.

**b95a83f090 (ETH)**
- **Read:** The 180-day high was 93.2 (day -156). It based at 70–73 and broke out sharply at day -32. It then held a tight 89–97 range for a month and is now breaking above it, reaching 100.9.
- **Weight:** 1. A new high after an orderly consolidation.
- **Change of mind:** Close below 89.

**2f52605237 (DOT)**
- **Read:** It was around 123 at the start of the window and peaked at 126.7, then crashed to 64 and based at 66–70. A spike at day -12 reached 113.1 and collapsed to 82.3 (day -5); it has since rebounded to 100. The trend is up since day -33, but the spike failure is fresh, the volatility is high, and the price is far below the earlier 120s.
- **Weight:** 0.5.
- **Change of mind:** Close above 104 → 1; close below 82 → 0.

---

{"83cf71dfdb (DOGE)": 0.5, "966d3dbd2b (BTC)": 1.0, "7cce848f7a (SOL)": 1.0, "aaafbc96a9 (LINK)": 1.0, "6de7752c48 (ADA)": 0.5, "7e6addfaa0 (XRP)": 0.5, "02711c6287 (AVAX)": 0.5, "0c4455241a (LTC)": 1.0, "b95a83f090 (ETH)": 1.0, "2f52605237 (DOT)": 0.5}

## Entscheidung 2026-09-27

## Strategy

I follow the trend and judge how far price sits from overhead supply. **1.0** goes to a window in a clear uptrend that is making new 180-day highs with rising swing lows and no blow-off. **0.5** goes to a window in an uptrend where price is still below a major earlier high, or where the last move was a vertical, climax-volume spike. **0.0** goes to a window in a downtrend, meaning lower highs and lower lows below the main resistance. Every window here shares the same history: a selloff around day -115, a base, and a sharp rally starting near day -39. So the call comes down to where price sits relative to the earlier highs, and how clean the advance is.

## c13637d294 (LINK)
- **Read:** Price climbed from a 50–52 base to 100. It broke well above the earlier window high of 77.5 and set a new high at 103.4. Swing lows keep rising: 75.7, then 77.0, then 86.0. Volume expands on up days.
- **Weight:** 1.0. This is a clean trend at new highs with no overhead supply.
- **Change my mind:** a close below 86.

## 094f176124 (DOT)
- **Read:** The window opened near 99 and topped at 105–113 (day -137 to -140). Price crashed to 63, then rallied back to 100. Trading is very volatile: there was a spike to 101.3 on day -19 that fell back to 74.5. Recent highs are 103.0. Price is still below the 105–113 supply zone.
- **Weight:** 0.5. The trend is up, but price is hitting old resistance with wide swings.
- **Change my mind:** a close above 106 moves me to 1.0. A close below 85 moves me to 0.

## d53a14c6e3 (XRP)
- **Read:** A blow-off on day -36 hit 112 on 5.6x volume. Since then price has ranged between about 83 and 109. Lows are rising (83.4, then 97.5), but highs are capped at 107–109. It is above the early-window highs near 99.6.
- **Weight:** 0.5. Higher lows are constructive, but price keeps failing below 109–112.
- **Change my mind:** a close above 109.5 moves me to 1.0. A close below 95 moves me to 0.

## d7026ce725 (BTC)
- **Read:** A steady stair-step from 70 to 100 put in a new window high at 103.5. Price is now consolidating tightly between 98.5 and 100.9 on light volume, holding its gains above the early highs near 98.
- **Weight:** 1.0. This is an orderly uptrend digesting a breakout.
- **Change my mind:** a close below 95.

## 023ab3a1d7 (LTC)
- **Read:** Price rose from 57 to 100. On day -3 it jumped about 16% on 6.7x volume to a high of 105.0. It is now holding 98.7–105. That is far above the early highs near 85, but the jump has the look of a climax move.
- **Weight:** 0.5. The trend is strong, but I expect the climax spike to retrace or need to be absorbed first.
- **Change my mind:** a close above 105.5 moves me to 1.0. A close below 92 moves me to 0.

## 610595a3cb (ETH)
- **Read:** Price rose from 56 to 100, breaking above the early highs near 91.7, and made a new high at 104.4. It is now coiling between 99 and 100 on very low volume. Higher lows run 87.7, then 96.7.
- **Weight:** 1.0. This is a clean trend with a tight flag at the highs.
- **Change my mind:** a close below 96.

## 0930045be1 (AVAX)
- **Read:** Price spent a long time basing at 57–62. Then, over days -8 and -7, it went nearly vertical from 70 to 105 on 3.7x and 5.7x volume. Since then it has ranged between 91.4 and 108.2. It is above the early highs near 96.
- **Weight:** 0.5. The move was a single gap-like spike, which carries meaningful retrace risk.
- **Change my mind:** a close above 108.5 moves me to 1.0. A close below 91 moves me to 0.

## 0f753d969e (ADA)
- **Read:** The earlier top was 107–113 (day -140). Price crashed to 54, then recovered with higher lows (74.6, then 91.3) back to 100, with a recent high of 104. Price is still beneath the 107–113 supply zone.
- **Weight:** 0.5. The recovery trend is good, but resistance overhead is heavy.
- **Change my mind:** a close above 105 moves me to 1.0. A close below 91 moves me to 0.

## 599a9744b7 (SOL)
- **Read:** Price went from 49 to 100, breaking the early high of 80.7 by a wide margin, and printed a new high of 102.4 on day 0. Lows are rising (78.5, then 92.2), and the advance is steady rather than climactic.
- **Weight:** 1.0. The trend is clean at new highs.
- **Change my mind:** a close below 92.

## d9b84a9d78 (DOGE)
- **Read:** The major earlier top was 113–122 (days -150 to -135). Price fell to 72 and has recovered to 100. A spike to 109.3 on day -5 was rejected down to 94. Price is below a large supply zone running from 105 to 122.
- **Weight:** 0.5. The trend is up, but the spike was rejected right under heavy resistance.
- **Change my mind:** a close above 106 moves me to 1.0. A close below 94 moves me to 0.

{"c13637d294 (LINK)": 1.0, "094f176124 (DOT)": 0.5, "d53a14c6e3 (XRP)": 0.5, "d7026ce725 (BTC)": 1.0, "023ab3a1d7 (LTC)": 0.5, "610595a3cb (ETH)": 1.0, "0930045be1 (AVAX)": 0.5, "0f753d969e (ADA)": 0.5, "599a9744b7 (SOL)": 1.0, "d9b84a9d78 (DOGE)": 0.5}
