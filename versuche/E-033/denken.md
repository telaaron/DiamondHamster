# E-033: was die KI gedacht hat (Set A)

Volle Antwort des Deciders pro Entscheidungswoche, unverändert. Er sah weder Datum noch Coin-Namen; die Namen in Klammern sind erst danach eingesetzt. Gesendeter Prompt und Daten: runs/<set>/<woche>/requests.json.

## Entscheidung 2026-07-05

## Strategy

All ten windows share one structure. There is a six-month downtrend from 150–250 down to about 100, then a capitulation leg around days −33 to −30, a retest low around days −11 to −5, and a sharp 3–4 day rally into 100. I apply one rule to every window. Because price is below its 50-day trend everywhere, the weight is capped at 0.5. The weight is **0.5** if the close is above the 20-day SMA *and* above the close of the day −20 bounce high, which was the last lower high. It is **0.3** if the close is above the 20-day SMA but still below that lower high. It is **0.0** if the close is below the 20-day SMA.

---

### a5666e1567 (XRP)
- **Read:** Downtrend. The capitulation low was 90.7 (day −29) and the retest low was 87.2, a marginal lower low. The 4-day rally ran from 90 to 100. The 20-day SMA is about 95.7, so price is above it. The day −20 lower high closed at 107.0 (high 111.8), and price has not reclaimed it. Resistance is 102–107; support is 94 and 87.
- **Weight:** 0.3. Price is above the 20-day SMA but below the lower high.
- **Change mind:** A close above 107 raises the weight to 0.5. A close below 95 cuts it to 0.

### 842d7129d6 (SOL)
- **Read:** The capitulation low was 73.7 (day −29) and the retest low was 78.5, a higher low. Price has rallied through the day −20 high (93.3) and the 101–102 area. The 20-day SMA is about 88. This is a double bottom with a breakout. Overhead supply sits at 104–112 (days −50 to −45).
- **Weight:** 0.5. Both conditions are met, and the weight is capped by the long-term trend.
- **Change mind:** A close below 93 (failed breakout) cuts it to 0.3. A close below 88 cuts it to 0.

### 35cf8dfabe (AVAX)
- **Read:** The day −16 flush to 82.0 undercut the day −29 low of 89.9. Price then recovered to 100, above the day −20 close of 98.8 but below its wick at 102.2. The 20-day SMA is about 94. The structure is a reclaim of the range after a bear trap. Resistance is 102 and then 111 (gap-down origin).
- **Weight:** 0.5.
- **Change mind:** A close below 98 cuts it to 0.3. A close below 94 cuts it to 0.

### c317be351c (DOGE)
- **Read:** This window had a much higher post-crash range (105–114, day −21 close 114.2), so its decline into the day −5 low of 89.3 was steeper. The rebound to 100 is still below the 20-day SMA of about 100.6. Resistance is 101–108; support is 92 and 89.
- **Weight:** 0.0. Price is below the 20-day SMA.
- **Change mind:** A close above 102 raises the weight to 0.3. A close above 114 raises it to 0.5.

### b9ea9a000e (DOT)
- **Read:** The pattern matches the previous window. The post-crash range was 108–115 (day −20 close 114.8), and the low was 90.2. The 20-day SMA is about 101.5, so price at 100 is below it. Resistance is 101.5, 106 and 115.
- **Weight:** 0.0.
- **Change mind:** A close above 102 raises the weight to 0.3. A close below 90 confirms the downtrend.

### 15ca0b0427 (LINK)
- **Read:** The capitulation low was 86.8 and the retest low was 86.9 (day −10), a flat double bottom. The 20-day SMA is about 95.5, so price is above it. The day −20 lower high closed at 102.9 (high 106.7), and price has not reclaimed it.
- **Weight:** 0.3.
- **Change mind:** A close above 103 raises the weight to 0.5. A close below 95 cuts it to 0.

### 63279879e7 (BTC)
- **Read:** This is the lowest-volatility window. The low was 90.8 (day −4) after 92.9 on day −30. The 20-day SMA is about 97.5, so price is above it. The day −20 lower high closed at 104.2 and has not been reclaimed. Resistance is 101–104; support is 96 and 91.
- **Weight:** 0.3.
- **Change mind:** A close above 104.5 raises the weight to 0.5. A close below 96 cuts it to 0.

### 49ce2c5978 (ETH)
- **Read:** The capitulation low was 84.3 and the retest low was 84.7, a double bottom. The 20-day SMA is about 94, so price is above it. The day −20 lower high closed at 100.6 (high 103.6), and price at 100.0 is just below it. Day 0 volume (0.99) was elevated with the close at 100.
- **Weight:** 0.3.
- **Change mind:** A close above 101 raises the weight to 0.5. A close below 94 cuts it to 0.

### eaff3a44cd (LTC)
- **Read:** The capitulation low was 88.4. The retest low was 85.7, a slightly lower low, but it was quickly reclaimed. The 20-day SMA is about 95. The day 0 close of 100.0 sits at the session high (100.7) and above the day −20 close of 99.9, so it is a marginal breakout. Resistance is 101 and then 110–114.
- **Weight:** 0.5. This is the weakest of the 0.5 calls.
- **Change mind:** A close below 97 cuts it to 0.3. A close below 95 cuts it to 0.

### 210cd3c051 (ADA)
- **Read:** This was the deepest flush, to 72.9 (day −10), well below the day −29 low of 78.4. It was followed by a V-reversal from 76 to 101 in 4 days on high volume (1.8–2.2). Price has cleared the day −20 high of 100.3 on a close basis (94.2 close). The 20-day SMA is about 87. Momentum is strong but extended, and supply sits at 106–112 (the day −32 to −33 gap).
- **Weight:** 0.5.
- **Change mind:** A close below 94 (failed reclaim) cuts it to 0.3. A close below 87 cuts it to 0.

---

{"a5666e1567 (XRP)": 0.3, "842d7129d6 (SOL)": 0.5, "35cf8dfabe (AVAX)": 0.5, "c317be351c (DOGE)": 0.0, "b9ea9a000e (DOT)": 0.0, "15ca0b0427 (LINK)": 0.3, "63279879e7 (BTC)": 0.3, "49ce2c5978 (ETH)": 0.3, "eaff3a44cd (LTC)": 0.5, "210cd3c051 (ADA)": 0.5}

## Entscheidung 2026-07-12

**Strategy:** Every window is in a 180-day downtrend, roughly from 200 to 100, and well below its 50-day average. So I apply one rule: stay mostly flat, and add a small long only where the last 6 weeks show higher lows and price near the top of its post-crash range. Below the most recent swing low I go fully flat. Above the most recent swing high I would add.

## 4c6057abf0 (XRP)
- **Read:** Downtrend. After the day -37 flush (low 96.7), highs keep falling: 119.1, then 109.1. The low at -17 (93.2) undercut the flush low. Today's close of 100 sits mid-range.
- **Weight:** 0.1. The structure of lower highs and lower lows argues for staying near flat.
- **Change my mind:** a close above 109.1 (more long), or below 93 (flat).

## 848d80de99 (ETH)
- **Read:** Double bottom at 83.3 / 83.7 (days -36 and -16), followed by a steady advance with higher lows: 85.8, 94.8, 95.3. The close of 100 is at the top of the 83–102 range. Key resistance is 102.4.
- **Weight:** 0.3. This is one of the cleaner basing structures.
- **Change my mind:** above 102.4 (add), or below 94.8 (flat).

## 33eae1023a (DOGE)
- **Read:** Lower highs (163, 127, 109) and a lower low at 95.6 (day -12), below the crash low of 106.8. The current bounce is weak and comes on low volume.
- **Weight:** 0.05.
- **Change my mind:** above 109.2.

## d059800426 (BTC)
- **Read:** Range of 90.6–105.5 since the crash. Lows are slightly lower (92.7, then 90.6). The close of 100 is mid-range, and volatility is low.
- **Weight:** 0.15.
- **Change my mind:** above 105.5 (add), or below 96 (flat).

## 659ab86830 (SOL)
- **Read:** This has the strongest repair. From the crash low of 78.2, it put in higher lows (83.3 at -17) and higher highs (98.9, then 109.2). It is now pulling back to 100, which sits above the 97 to 99 breakout zone.
- **Weight:** 0.35.
- **Change my mind:** below 98.3/97 (cut to flat), or above 109.2 (add).

## 60b60ec899 (LTC)
- **Read:** The low at 89.3 (day -18) undercut the crash low of 92.1. The rally peaked at 104.9 with a lower high than 105.3, and the close of 100 is mid-range.
- **Weight:** 0.15.
- **Change my mind:** above 105.3 (add), or below 95 (flat).

## 4c1f7808a6 (DOT)
- **Read:** Lower lows: 104.7, then 94.2. The spike to 106 on day -2 was rejected, and price has given it all back to 100. Sellers are in control.
- **Weight:** 0.1.
- **Change my mind:** a close above 107.6.

## 9899f89e77 (LINK)
- **Read:** Double bottom at 87.5 / 87.7. Price rallied to 102.2 and is holding near 100. The prior high of 107.5 (day -27) is the breakout level, and the higher low at 94.1 is the line to defend.
- **Weight:** 0.2.
- **Change my mind:** below 94 (flat), or above 102.2 / 107.5 (add).

## 6dbfc2f1d0 (ADA)
- **Read:** The low at 85.3 (day -17) was a lower low. A spike to 123.4 on heavy volume then fully retraced to 100. That is a failed breakout and is bearish.
- **Weight:** 0.0.
- **Change my mind:** a reclaim above 108.

## b3869955f0 (AVAX)
- **Read:** The capitulation low was 88.7 (day -23). Lows have risen since (92.9, 97.9) and highs reached 111.1. But today's close of 100 is at the day's low of 98.0, which tests the support zone of 98 to 100.
- **Weight:** 0.15.
- **Change my mind:** below 97.9 (flat), or above 111.1 (add).

{"4c6057abf0 (XRP)": 0.1, "848d80de99 (ETH)": 0.3, "33eae1023a (DOGE)": 0.05, "d059800426 (BTC)": 0.15, "659ab86830 (SOL)": 0.35, "60b60ec899 (LTC)": 0.15, "4c1f7808a6 (DOT)": 0.1, "9899f89e77 (LINK)": 0.2, "6dbfc2f1d0 (ADA)": 0.0, "b3869955f0 (AVAX)": 0.15}

## Entscheidung 2026-07-19

**Strategy:** I go long in proportion to how much the short-term structure has turned up inside the larger downtrend. The checks are price against its roughly 50-day mean, whether the swing lows since the second crash (around day -44) are rising, and whether recent highs are lower or higher. A strong rebound with higher lows gets about 0.6 to 0.7, an unresolved range about 0.4 to 0.5, and a series of lower highs still under the 50-day mean 0.1 to 0.3, since every window sits under a falling 180-day trend.

## 99fc254061 (BTC)
**Read:** The long-term trend is down, from 138 through 120 to 100. The day -44 crash bottomed near 91, and the day -24 low at 89.8 held as a double bottom. Since then the lows have risen: 95.5 on day -6 and 96.6 on day -2. Price is coiling between 96.5 and 101.4 and sits slightly above the 50-day mean of about 97.

**Weight:** 0.5. The base is constructive but there is no breakout above 101.4 yet.

**Change my mind:** A close below 95.5 would take me flat. A close above 101.5 would take me to 0.8.

## 878dba8749 (ETH)
**Read:** Price bottomed at 80.4 on day -43 and made a higher low at 81.9 on day -24. It then rallied about 20% to 104.0 on day -4 and has pulled back to 100. It is clearly above the 50-day mean of about 91, with a higher-low sequence of 82.9, 93.5 and 96.3.

**Weight:** 0.6. The recovery has momentum, and the pullback is holding.

**Change my mind:** Below 96.

## db5fbca169 (DOT)
**Read:** This window is in a persistent decline from 160 to 100. Recent highs keep stepping lower: 110.7, 109.1, 106.6, then 104.1. Day 0 closed at the low of the week, at 100.0 against a low of 98.3, and is pressing the 98 to 100 support. Price is well below the 50-day mean of about 113.

**Weight:** 0.1. It is the weakest structure in the set, and support is close to breaking.

**Change my mind:** A close above 107 would show the lower-high series is broken.

## 0840371f18 (LINK)
**Read:** Price made a double bottom at 83.4 (day -43) and 83.6 (day -24). It rallied to 103.0 on day -4 and the pullback is holding 95.5. It is above the 50-day mean of about 94, and the lows are rising.

**Weight:** 0.6.

**Change my mind:** Below 95.5.

## bfd50be1f0 (ADA)
**Read:** Price spiked from 86 to 120 between days -19 and -15 and then gave the whole move back to about 100. It has since chopped between 93.4 and 102. The spike failed, but the lows at 93.4 and 94.9 are holding above the day -24 low of 83. Price is close to the 50-day mean of about 100.

**Weight:** 0.4. It is a neutral range that still carries the overhead supply left by the failed spike.

**Change my mind:** Below 93.4 would take me flat. Above 102 would take me to 0.6.

## 83149c3e36 (AVAX)
**Read:** Price bottomed at 87.9 on day -30 and has ranged between 97 and 110 since. Recent highs are lower: 110.1, 105.7, then 104.8. Day 0 was a red bar that tested 98.9. Price is slightly under the 50-day mean of about 103.

**Weight:** 0.3. The lower highs and the position under the mean argue for staying light.

**Change my mind:** A close above 105 would turn me up. A close below 97.7 would take me flat.

## 3302bbb042 (SOL)
**Read:** Price bottomed at 78.7 on day -43 and made a higher low at 83.8 on day -24. It rallied strongly to 110 on day -15 and is now retracing to 100, with lower highs at 108.4, 104.3 and 103.5. It sits above the 50-day mean of about 96.

**Weight:** 0.5. The medium-term structure is good, while the short-term pullback is unresolved.

**Change my mind:** Below 96 would take me flat. Above 103.5 would take me to 0.7.

## 22c3e97ae2 (XRP)
**Read:** The downtrend runs from 130 to 100. Price made a low at 91.9 on day -23 and rallied to 107.9, but it has faded since with lower highs at 106.1, 103.0 and 101.9. Price is at about 100, a bit under the 50-day mean of about 102. Volume is very low.

**Weight:** 0.4.

**Change my mind:** Below 96 would take me flat. Above 103 would take me to 0.6.

## 6560749971 (LTC)
**Read:** Price bottomed at 83.5 on day -25 and has made steadily higher lows: 87.4, 91.2, 92.2, 93.7, then 95.7. On day -1 it broke out of the 92 to 98 range to 101.7, on above-average volume. It sits above the 50-day mean of about 94. This is the best short-term structure in the set.

**Weight:** 0.7.

**Change my mind:** A close below 95 would mean the breakout failed.

## 6bf0b85bbd (DOGE)
**Read:** The decline runs from 160 to 100. Price made a low at 96.0 on day -19 and has ranged between 98 and 109 since, with lower highs at 109.6, 104.4 and 104.1. It is well below the 50-day mean of about 110, and volume is drying up near the lows.

**Weight:** 0.3.

**Change my mind:** A close above 104.5 would turn me up. A close below 97.9 would take me flat.

{"99fc254061 (BTC)": 0.5, "878dba8749 (ETH)": 0.6, "db5fbca169 (DOT)": 0.1, "0840371f18 (LINK)": 0.6, "bfd50be1f0 (ADA)": 0.4, "83149c3e36 (AVAX)": 0.3, "3302bbb042 (SOL)": 0.5, "22c3e97ae2 (XRP)": 0.4, "6560749971 (LTC)": 0.7, "6bf0b85bbd (DOGE)": 0.3}

## Entscheidung 2026-07-26

**Strategy:** Every window is in a long-term downtrend: a crash near day −171, a slow bleed, and a second crash around day −54 to −51 into a base. I weight by the structure of the last ~30 days. Rising higher lows with a close at the top of the range earn 0.6–0.7. A flat range with no clear direction gets 0.3–0.45. Weak structure near range lows gets 0.2. Because the bigger trend is down, I cap weights at 0.7.

## 9e980735ca (DOT)
- **Read:** Price has fallen from 226 to 100. Since day −30 it has traded flat between 95 and 109, with lower highs (108.7 → 105.6 → 105.0). The last few days held a low of 95.0. The close at 100 sits mid-range with no momentum. This is the weakest base of the set.
- **Weight:** 0.2. A small stake for a possible base, but nothing confirms it.
- **Change mind:** Above 105 would build the position; below 95 would take it to flat.

## aeba235e05 (DOGE)
- **Read:** Since day −30 it has moved sideways between 93 and 108. On day −3 it flushed to 93.2, then reclaimed 100 within two days. That looks like a spring off the range floor, but the highs are still capped at 101–103.
- **Weight:** 0.3.
- **Change mind:** Above 103 means a bullish range break; below 92.9 means the spring failed.

## 609b25b329 (ADA)
- **Read:** It capitulated to 83.3 at day −31, then rallied sharply to 120.5 at day −22 on heavy volume. It retraced to about 94–98 and is now holding higher lows (93.6, 95.1, 96.8, 97.3). Volume is drying up into the 100 area. The structure is constructive, but the market is still digesting the spike.
- **Weight:** 0.5.
- **Change mind:** Above 109 would add; below 96.8 would cut.

## 2acce34cc7 (LINK)
- **Read:** A clean recovery from the 79.4 low. Each pullback holds higher: 80.2, 85.2, 88.3, 90.7, 93.7. Today it pushed through the 99.3 high to close at 100, the highest close since day −55.
- **Weight:** 0.7. This is an uptrend in place with a breakout close.
- **Change mind:** Below 93.7 breaks the higher-low sequence.

## b9e39bb7fc (XRP)
- **Read:** It bottomed at 90.7 on day −30 and rallied to 106.4. Since then it has chopped between 94.6 and 104.6. The close at 100 is mid-range on light volume, so the read is neutral.
- **Weight:** 0.35.
- **Change mind:** Above 104.6 is a breakout; below 96.1 means the floor is breaking.

## 20a7ae277a (LTC)
- **Read:** A steady climb from the 82.1 low at day −31. Lows step up (86.0 → 89.7 → 95.6) and highs step up (96.5 → 100.1 → 100.9). Volume is firmer than in its peers, and today closed at the high.
- **Weight:** 0.7.
- **Change mind:** Below 95.6.

## f3e6e00a1f (AVAX)
- **Read:** It made a second low at 84.2 on day −37, then a choppy range from 88 to 105.5. On day −3 it dropped to 91.9, and on day −1 it reversed hard to 101.5 on the heaviest volume in weeks. The range is intact, the reversal is promising, and the highs are capped near 101–105.
- **Weight:** 0.4.
- **Change mind:** Above 105.5 would raise the position; below 91 would go flat.

## 3eb0053027 (SOL)
- **Read:** It fell from 78.3 at day −50, then rallied to 109.4 at day −22. It has since pulled back with lower highs (107.9 → 103.0 → 102.8) to a 95.7 low two days ago, and is now back at 100. Higher lows hold from the base, but the short-term trend is drifting down.
- **Weight:** 0.45.
- **Change mind:** Above 103 would add; below 95.6 would cut.

## c953bd650b (BTC)
- **Read:** Low of 88.9 at day −31. It has been grinding up since, with higher lows (94.1, 94.5, 95.6, 97.5) and a high of 102.4 at day −5. Today closed at 100, near the top of a tightening range.
- **Weight:** 0.55.
- **Change mind:** Above 102.4 is the breakout trigger; below 97 breaks the higher-low sequence.

## a2be68507d (ETH)
- **Read:** The strongest recovery of the set: +29% from the 77.4 low, with steady higher lows (79.4, 87.7, 89.5, 92.2, 94.5). Today printed a range-high close at 100, though 100.1–100.6 is still being tested.
- **Weight:** 0.7.
- **Change mind:** Below 94.5.

{"9e980735ca (DOT)": 0.2, "aeba235e05 (DOGE)": 0.3, "609b25b329 (ADA)": 0.5, "2acce34cc7 (LINK)": 0.7, "b9e39bb7fc (XRP)": 0.35, "20a7ae277a (LTC)": 0.7, "f3e6e00a1f (AVAX)": 0.4, "3eb0053027 (SOL)": 0.45, "c953bd650b (BTC)": 0.55, "a2be68507d (ETH)": 0.7}

## Entscheidung 2026-08-02

**Strategy:** I combine the long-term trend with short-term structure. Every window has fallen sharply over 180 days, so the starting weight is cautious, around 0.3 to 0.4. I add weight when price shows higher lows and is reclaiming the recent range on rising volume, and I cut it when the recent highs keep getting lower. No window gets a full position while the long-term trend is still down.

## ff2fdbfce1 (DOT)
- **Read:** Persistent downtrend from about 188 to 100, with a crash at day -58 and another drop to 95 at day -6.
- **Structure:** Highs keep getting lower: 112, then 108.8, then 104. Price is bouncing off 93 to 95 support and has only just reached the 100 to 103 area that used to be support and is now resistance. This is the weakest trend in the set.
- **Weight:** 0.2. This is a dead-cat bounce inside a downtrend.
- **Change my mind:** A close above 106.

## 49166cead2 (LINK)
- **Read:** The crash bottomed at 84 to 86 (days -58 and -38). Since then the lows have been rising: 86, 91, 95, 96. Price has ranged between 95 and 105 for 20 days.
- **Structure:** Price sits mid-range at 100, close to its 20-day average. The decline over the full window was relatively mild (113 to 100).
- **Weight:** 0.5. The setup is neutral to constructive.
- **Change my mind:** Below 94 I would turn bearish. Above 105.5 I would go to 0.8.

## 6d5aa6555a (SOL)
- **Read:** Price fell to a low of 82, then rallied to 112 at day -30.
- **Structure:** Since that rally the highs keep getting lower (112, 107, 105). The latest bounce came off 96.
- **Weight:** 0.35. Momentum is fading, but support is holding.
- **Change my mind:** Below 95.5 I go flat. Above 106 I add.

## 0b910c5e72 (ETH)
- **Read:** The low was 80 at day -37. The lows since then are clearly rising: 82, 91, 97. Price now holds a 97 to 105 band.
- **Structure:** This is one of the better recovery structures in the set.
- **Weight:** 0.55.
- **Change my mind:** Below 96.5 I cut. Above 105.5 I go to 0.8.

## aee18a7071 (BTC)
- **Read:** The decline was shallow (119 to 100), with a low of 91 at day -38. Price is in a tight 98 to 105 range with low volatility.
- **Structure:** There is no strong signal in either direction.
- **Weight:** 0.45.
- **Change my mind:** Below 97.5 I cut. Above 105.5 I add.

## 20891ff8a5 (DOGE)
- **Read:** Price fell from a 167 peak at day -80 to about 100.
- **Structure:** Since the 110 high at day -29 the highs keep getting lower: 106.5, then 104.6, then 100.9. Support sits at 95.6 to 96.6.
- **Weight:** 0.3. The trend is still down and the range is drifting lower.
- **Change my mind:** Above 105 I add. Below 95.5 I go flat.

## 50b9fdc375 (ADA)
- **Read:** This had the deepest crash, to 73 at day -38, then a spike to 105.5 at day -29 and a base between 81 and 92.
- **Structure:** Day 0 jumped 8.7% to 100 on the highest volume in weeks (1.73). That breaks clearly above the base ceiling of 92 to 95. Resistance is at 105.5.
- **Weight:** 0.7. This is a momentum breakout with volume behind it.
- **Change my mind:** A close back below 92 means the breakout failed.

## cee5e54b41 (AVAX)
- **Read:** Price has chopped between 92 and 108 since the day -44 low of 86.7. Day 0 rebounded 5.8% from 94.5 to 100.
- **Structure:** Resistance is at 103 to 104.5 and support at 92 to 94.
- **Weight:** 0.45. The rebound is constructive but the range is not resolved.
- **Change my mind:** Below 94 I cut. Above 104.5 I add.

## f6fd74b49f (LTC)
- **Read:** Price rallied from 88 at day -39 to 107 at day -7, and is now pulling back to 99 to 100.
- **Structure:** The rising lows from the base are still intact. The 20-day average is about 102 and support is at 97.6.
- **Weight:** 0.45. This looks like a pullback within a recovery.
- **Change my mind:** Below 97 I cut. Above 107 I add.

## 91dc67d191 (XRP)
- **Read:** Price recovered from 93 to 109 by day -29.
- **Structure:** Since then the highs keep getting lower (109, 107, 102.7). Support is at 96 to 97.
- **Weight:** 0.35.
- **Change my mind:** Below 96 I go flat. Above 103 I add.

{"ff2fdbfce1 (DOT)": 0.2, "49166cead2 (LINK)": 0.5, "6d5aa6555a (SOL)": 0.35, "0b910c5e72 (ETH)": 0.55, "aee18a7071 (BTC)": 0.45, "20891ff8a5 (DOGE)": 0.3, "50b9fdc375 (ADA)": 0.7, "cee5e54b41 (AVAX)": 0.45, "f6fd74b49f (LTC)": 0.45, "91dc67d191 (XRP)": 0.35}

## Entscheidung 2026-08-09

**Strategy:** Every window shares the same sharp crash around day -68 to -65, so I judge each one by how it has recovered since that crash. I score each window on its higher-low/higher-high structure since the day -45 trough and on where price sits within its last 20 days. Weight scales from about 0.2 for clear lower highs (still a downtrend) to about 0.65 for clean higher lows, with 0.4–0.5 for a range with no clear direction.

### e5ef5d40d4 (DOT)
- **Read:** A long downtrend from the 208 spike to 100. After the crash, price drifted from about 126 down to 93.6 at day -13. The bounce stalled at 108.9 and price is now back at 100, below its 20-day mean of about 102. Lower highs run 131 → 113.6 → 108.9.
- **Weight:** 0.2. The trend is still down, with only a small residual allowance for the 93.6 low holding.
- **Change my mind:** A close above 109 flips me to long. A break below 93.5 takes me flat.

### 553511e29c (BTC)
- **Read:** After the crash low of 89.5, price has ranged between 96 and 103 for about 30 days. Lows are rising slightly (89.5 → 94.5 → 96.0), but highs are capped at 103.2. Price is at 100, the middle of the range.
- **Weight:** 0.5. The structure is neutral to mildly constructive.
- **Change my mind:** Above 103.3 I add; below 96 I cut.

### 48660c0ae9 (LINK)
- **Read:** Price fell from 132.8 to 85.5, then rallied to 108.9 at day -13. It has since faded to 100, with the range tightening between 96.3 and 104. The structure is mixed: higher lows, but the recent high was rejected.
- **Weight:** 0.4.
- **Change my mind:** Above 104.2 I add; below 96.3 I cut.

### 4eb3c46db7 (AVAX)
- **Read:** Two flushes, to 96.9 and then 88.5. Since then price has ranged between 94 and 111. The highs keep falling (110.8 → 106.6 → 108.8 spike) while the lows hold in the mid-90s (94.1 at day -8). Price is at 100.
- **Weight:** 0.4.
- **Change my mind:** Above 108.8 I go long; below 94 I go flat.

### 57c934cda2 (SOL)
- **Read:** From the 78.8 low, price rallied to 110 and then made lower highs (103.6, 101.6) and lower lows down to 92.5. The last two days broke out to 102.1, but the close is back at 100. This is an early attempt to turn, not yet confirmed.
- **Weight:** 0.45.
- **Change my mind:** A close above 102.5 confirms the turn; below 94.3 I cut.

### dd3de7f80a (ADA)
- **Read:** The deepest crash (to 71) was followed by an impulsive rally to 102.8, a retest at 79 (a higher low), and a second strong rally on rising volume to 108.8. Price is now pulling back to 100. The structure is a clear higher low with momentum behind it.
- **Weight:** 0.6.
- **Change my mind:** Below 93.3 I cut. Above 105 I go fully long.

### bf290ad0a0 (XRP)
- **Read:** The highs keep falling: 115 → 113.1 → 108. The recent move broke the 101.5 floor, reaching 98.3 at day -2. Price is at 100, sitting just on the day -44 low of 98, which is now being tested.
- **Weight:** 0.25.
- **Change my mind:** Above 106 I go long. A close below 98 takes me flat.

### ce7b17e36b (DOGE)
- **Read:** A long distribution from 171 to 103, then a range between 98 and 109 with lower highs (114.5 → 109 → 106.8 → 103.2). Volume is drying up. Price is at 100, near the bottom of the range at 97.6–98.3.
- **Weight:** 0.3.
- **Change my mind:** Above 106.8 I go long; below 97.6 I go flat.

### 5fcfe54dee (ETH)
- **Read:** The cleanest recovery of the set. Lows step up 79.1 → 81.1 → 89.7 → 91.6 → 95.4, and highs step up 96 → 101.9 → 103.7. Price is at 100, pulling back inside an uptrend channel.
- **Weight:** 0.65.
- **Change my mind:** Below 95.4 I cut. Above 103.7 I go fully long.

### 2923ae779d (LTC)
- **Read:** Lows rise 86.4 → 90.5 → 94.4 → 96.0, and price reached 106.2 before pulling back. It is now 100, back above the 20-day mean of about 100.5 after a dip to 96.
- **Weight:** 0.55.
- **Change my mind:** Below 96 I cut; above 106.2 I add.

{"e5ef5d40d4 (DOT)": 0.2, "553511e29c (BTC)": 0.5, "48660c0ae9 (LINK)": 0.4, "4eb3c46db7 (AVAX)": 0.4, "57c934cda2 (SOL)": 0.45, "dd3de7f80a (ADA)": 0.6, "bf290ad0a0 (XRP)": 0.25, "ce7b17e36b (DOGE)": 0.3, "5fcfe54dee (ETH)": 0.65, "2923ae779d (LTC)": 0.55}

## Entscheidung 2026-08-16

**Strategy:** I follow the trend over two horizons: the 10–20 day structure (higher lows or lower highs, breakouts from ranges) and where price sits within the 50-day range. I go long in confirmed short-term uptrends, stay mostly flat in persistent downtrends, and hold a partial position when price is ranging. Each weight scales with how clean the structure is.

## 6ccdeb498d (DOT)
- **Read:** A long downtrend from about 220 to 100. A bounce to 112.9 (day -12) was fully given back, so price is back at the 98.6–100 lows. Lower highs at 117, 113 and 112.9.
- **Weight:** 0.1. The trend is still down and price is sitting on support with no reversal signal.
- **Change my mind:** a close above 113, or a break below 98.5, which would confirm more downside.

## 526212ac3b (SOL)
- **Read:** Crashed to 80.6, recovered to 112.6 (day -43), and has ranged between 94.6 and 105.7 for the past 30 days. Volume is drying up and price is at the middle of the range.
- **Weight:** 0.4. The setup is neutral with no edge either way.
- **Change my mind:** a close above 105.7 would make me bullish; a close below 94.6 would take me flat.

## f7877560e6 (AVAX)
- **Read:** Fell from 166 to 89.7, then recovered into a 96–110 range. Day -1 was rejected hard at 108.6 and closed at 100. The range highs keep capping price.
- **Weight:** 0.3. The bias is mildly bearish after the rejection.
- **Change my mind:** a close above 108.6.

## da2a58599d (LINK)
- **Read:** Bottomed at 74.5 and has since put in higher lows (84, then 87). In the last 5 days it broke out of the 85–94 range on strong volume (1.54 and 1.66), up to a 103.8 high. It is holding 100 after the breakout.
- **Weight:** 0.7. This is the cleanest short-term uptrend in the set.
- **Change my mind:** a close back below 92, which would mean the breakout failed.

## 2d51fcd14c (LTC)
- **Read:** Recovered from 88.9 to 109.3, then drifted lower with lower highs (109.3, then 105.8, then 104.4). It now sits at the bottom of a 98–105 range.
- **Weight:** 0.35. Price is at support but the short-term trend is down.
- **Change my mind:** a close above 105 would make me bullish; a break below 98.3 would take me flat.

## 6f64d01345 (DOGE)
- **Read:** A long decline from 170 to 100, then a tight 97–106 range with very low volume. It failed at 105.1 on day -5. Price is below the 50-day average (about 104).
- **Weight:** 0.25.
- **Change my mind:** a close above 106.

## def7a4c95c (XRP)
- **Read:** A steady sequence of lower highs at 119.2, 117.2, 112.4 and 110 (day -14), with price grinding down to 100. That is a clean downtrend.
- **Weight:** 0.1.
- **Change my mind:** a close above 110.

## 0ea8e5c892 (ADA)
- **Read:** Crashed to 79, spiked to 114, fell back to 87.7, then rallied to 121 (day -10). It has since faded for 9 straight sessions to 100, and all of that rally has been given back.
- **Weight:** 0.2. The reversal attempt failed and the momentum is negative.
- **Change my mind:** a close above 110 would make me bullish; a break below 87.7 would take me fully flat.

## 12e547e393 (ETH)
- **Read:** Higher lows at 80.3, 82.5, 91.3 and 97.1 since the crash, but price has been capped around 104–106 and is consolidating near 100 with very low volume.
- **Weight:** 0.5. The structure is constructive but there is no breakout yet.
- **Change my mind:** a close above 105.6 would make me bullish; a close below 97 would take me flat.

## 91a58c8d74 (BTC)
- **Read:** Recovered from 92.4 to 106.4, then ranged between 99 and 106. Day -9 marked a slight lower high at 104 and price is drifting toward the 99 floor.
- **Weight:** 0.4.
- **Change my mind:** a close above 104.6 would make me bullish; a close below 99 would take me flat.

{"6ccdeb498d (DOT)": 0.1, "526212ac3b (SOL)": 0.4, "f7877560e6 (AVAX)": 0.3, "da2a58599d (LINK)": 0.7, "2d51fcd14c (LTC)": 0.35, "6f64d01345 (DOGE)": 0.25, "def7a4c95c (XRP)": 0.1, "0ea8e5c892 (ADA)": 0.2, "12e547e393 (ETH)": 0.5, "91a58c8d74 (BTC)": 0.4}

## Entscheidung 2026-08-23

## Strategy

All ten windows show the same setup: a long decline or flat base, then a 4-day vertical spike of 20–55% into the 100 area, with day 0 consolidating. My rule is to hold a partial long and size it by the quality of the spike. Weight goes up (about 0.45–0.55) when day -1 digests quietly on falling volume, with no big upper wick, and price is reclaiming an old range or making a new high. Weight goes down (about 0.15–0.35) when day -1 is a climax bar (high rejected well above 105 on record volume) inside a longer downtrend, or when the asset has a history of spikes that fully retrace. These windows clearly move together, so the combined book is effectively one correlated bet. That is one reason no weight goes above 0.55.

## 00570e4326 (BTC)
- **Read:** The base at 81–83 broke out to 102.3 on day -2. Day -1 was an inside bar (98.4–101.4) and volume has faded from 2.52 to 0.87. That is orderly digestion with no blow-off wick. Price is back inside the old 95–106 range (days -130 to -84), and the 100–106 zone is overhead supply.
- **Weight: 0.5.** This is the cleanest digestion of the group, but price sits right under resistance.
- **Change mind:** A close below 97.2 (day 0 low) means cut to flat. A close above 102.3 means add.

## acbc4bcac1 (XRP)
- **Read:** The downtrend ran from 105 to 65, with a tight base at 65–66. Price then went parabolic to 111.8 on day -1 on volume of 5.98, the largest in the window, and closed at 96.2, a classic exhaustion wick. The old supply zone is 88–98 (days -105 to -100). The move was +52% in 4 days.
- **Weight: 0.15.** The climax is the most extreme of the set.
- **Change mind:** A close above 102 (day 0 high) means the climax was absorbed, so raise to about 0.4. A close below 94.3 confirms the fade.

## 19518dc905 (LINK)
- **Read:** The trend was already turning before the spike, with higher lows from 70 to 82.7 between days -13 and -5. At 100, price is above the whole 180-day range (prior high 94.2). Day -1 had a wide wick (109.3/94.7), but day 0 held at 95.3+.
- **Weight: 0.5.** This is a genuine structural breakout to new highs, despite the wick.
- **Change mind:** A close below 94.7 (day -1 low, and also the old range top) means flat.

## 2be302be4e (AVAX)
- **Read:** A big downtrend from 138 crashed to 75–90, then a base at 83–85. The spike reached 109.3 on day -1 and reversed to 92 intraday. Price is in no-man's-land: support near 90, with heavy old supply at 115–125.
- **Weight: 0.3.** The wide two-sided day -1 bar signals indecision.
- **Change mind:** Below 95.6 means flat. A close above 103.7 means raise.

## 8874e0a74f (ADA)
- **Read:** The downtrend ran from 138 to a 61 low. This asset has already had two spikes that fully retraced: 63→88 (days -53 to -50) gave back to 73, and 72→93 (days -27 to -17) gave back to 77. The current spike reached 113.8 on day -1 and closed at 99.6, a large upper wick.
- **Weight: 0.15.** The repeated spike-and-fade behavior plus the climax wick argue against holding much.
- **Change mind:** A close above 103 that holds means raise. Below 94 (day 0 low) means flat.

## 4b7af401fe (DOGE)
- **Read:** Price fell from 127 to 75, then held a very tight, low-volume base at 74–76 for about 20 days, which is good accumulation structure. It then spiked to 107.9 on day -1 with a wick back to 88.8 and a close at 98.4. Overhead supply is at 107–120.
- **Weight: 0.35.** The base quality is good, but the day -1 climax wick offsets it.
- **Change mind:** Below 95 means flat. A close above 101.2 means raise.

## 6d964e0d8c (DOT)
- **Read:** This is the longest downtrend of the group, 189 to 78. The spike broke the most recent lower high at 93.8 (day -19), which is a structural improvement. Day -1, however, rejected at 111.2 and closed at 99.1.
- **Weight: 0.3.** The trend reversal is unconfirmed and the day -1 bar rejected the high.
- **Change mind:** Below 93.8 means flat, because the breakout failed. Above 101 means raise.

## b5586df9e2 (LTC)
- **Read:** This is the lowest-volatility name. The 100–115 range crashed to 75, recovered to 91, and faded back to 84–85. The spike reached 106.1 on day -1 with a moderate wick and closed at 100.3. Price is back at the bottom of the old 100–108 range.
- **Weight: 0.4.** The wick is moderate and price has reclaimed the bottom of the old range.
- **Change mind:** Below 96.3 (day -1 low) means flat. Above 103.7 means raise.

## c7e5bcbc75 (SOL)
- **Read:** The old range was 85–103, which crashed to 63. Price recovered to 87, then based at 76–80. The spike pushed through the prior high of 103.1 to 107.7, was rejected, and closed at 98.3, a failed first push above old resistance.
- **Weight: 0.35.** The breakout above 103.1 failed on its first attempt.
- **Change mind:** Below 96 (day 0 low) means flat. A close above 103 means raise.

## ce4af937f2 (ETH)
- **Read:** The old range was 80–100, which crashed to 61. Price recovered with higher lows to a 76–78 base. The breakout started earlier, on day -4, and stair-stepped up to 103.4 on day -2. Day -1 was a mild pullback with no climax wick, and volume declined from 2.6 to 1.23. Price is at the prior range high of about 100.
- **Weight: 0.45.** The advance is orderly and volume is fading, similar to 00570e4326 (BTC).
- **Change mind:** Below 95.6 means flat. A close above 103.4 means add.

{"00570e4326 (BTC)": 0.5, "acbc4bcac1 (XRP)": 0.15, "19518dc905 (LINK)": 0.5, "2be302be4e (AVAX)": 0.3, "8874e0a74f (ADA)": 0.15, "4b7af401fe (DOGE)": 0.35, "6d964e0d8c (DOT)": 0.3, "b5586df9e2 (LTC)": 0.4, "c7e5bcbc75 (SOL)": 0.35, "ce4af937f2 (ETH)": 0.45}

## Entscheidung 2026-08-30

**Strategy:** All ten windows share the same structure: a long decline, a crash around day −89 to −86, a multi-week base, then a sharp breakout spike on days −11 to −8 that has been fading since. I size by how much of the spike has held. If price has given back less than about 30% of the base-to-high move, the breakout is intact and I lean long (0.7). If it has given back 30–50%, I go half (0.4–0.5). At 50–70% I hold a token amount (0.2–0.25). Above 70% the breakout has failed and I stay flat. On longs, a close below day 0's low (~98.5) is my exit signal.

## e824feafd2 (DOGE)
Long-term downtrend from 140 to an 84–86 base, which broke out to a 122.9 spike high on day −8. Closes since have been lower highs: 113.9, 109.8, 104.4, 103.9, 100.0. The retracement is about 60% of the 85→123 move. Support is around 98.5 (day 0 low), then the 91–93 breakout gap. Resistance is 104–110. **Weight 0.25:** the breakout is half-faded but still above the base. I'd change my mind on a close above 105 (add) or below 97 (flat).

## c8b2148232 (SOL)
This was the strongest follow-through. From a 72–75 base, price kept making higher highs into 108.7 on day −3. Only about 25% of the 74→108.7 move has been retraced. Support is 98.6, then 93–95. **Weight 0.7:** the trend is intact and this looks like a pullback. I'd cut below 97.

## 275751efac (AVAX)
Base 88–91, spike high 116.9 on day −8, then a steady fade. About 62% retraced. Support is 98.6, then 95; resistance is 104–107. **Weight 0.25.** Flat below 97; add above 106.

## ad8700e56e (ADA)
Base ~90–91, with a blow-off wick to 134.1 on day −8. Price has given back about 79% of that. There was an earlier failed rally to 109.9 (day −24) that then bled to 90. Choppy, weak follow-through. **Weight 0.0.** I'd re-enter on a close above 111.

## 797f033f86 (ETH)
A very tight base at 77–79, then a clean breakout to 104–106. It has consolidated between 100 and 104 for 7 days. Only about 22% retraced, with the breakout level holding. **Weight 0.7.** Cut below 98.

## 26192cd833 (LINK)
The base was already rising (73→85, higher lows) before the spike to 113.2. The day −3 bounce reached 107.5. About 40% retraced. Support is 98.6, then the 94–95 breakout level. **Weight 0.5.** Flat below 97; add above 108.

## 52a8210f1a (XRP)
Base 73–74, then a huge-volume spike (vol 6.0) to 125.2. About 49% retraced. There is a lot of cushion above the base, but the climactic volume hints at exhaustion. **Weight 0.4.** Flat below 97; add above 108.

## 672ec32400 (DOT)
Severe long-term downtrend: 188 → 92. The spike to 126 has retraced about 79%, and the pattern of lower highs persists. **Weight 0.0.** I'd reconsider above 108.

## ea3ae7a375 (LTC)
Base 92–93, spike high 115.7, about 69% retraced. Closes have drifted lower all week, from 109 to 100. **Weight 0.2.** Flat below 98; add above 106.

## 7bc6a91915 (BTC)
Base 81–83, then a breakout to 102–105. It has held a tight 99–105 range for 8 days, with low volume on the dips. About 21% retraced. **Weight 0.7.** Cut below 98.5.

{"e824feafd2 (DOGE)": 0.25, "c8b2148232 (SOL)": 0.7, "275751efac (AVAX)": 0.25, "ad8700e56e (ADA)": 0.0, "797f033f86 (ETH)": 0.7, "26192cd833 (LINK)": 0.5, "52a8210f1a (XRP)": 0.4, "672ec32400 (DOT)": 0.0, "ea3ae7a375 (LTC)": 0.2, "7bc6a91915 (BTC)": 0.7}

## Entscheidung 2026-09-06

**Strategy:** I use a trend-plus-structure rule. All ten windows share the same pattern: a long decline, a quiet base, a sharp volume spike around day −17 to −15, then a consolidation. In each one I size the long according to where the close (100) sits inside the post-spike range and whether the lows are rising. A close above the post-spike highs or at new window highs earns 0.8–0.9, a close mid-range with fading volume earns about 0.4–0.5, and a break back into the lower half of the range takes me out.

**a549281351 (DOGE)**
- **Read:** The prior peak was 128, followed by a crash and a long base at 76–78. The spike reached 110.9 intraday, then price consolidated between 88 and 105. The lows are rising (88.9, then 88.1, then 92.4), and the close at 100 sits in the upper part of the range, with resistance at 104.7–105.
- **Weight:** 0.6. The trend has turned constructive, but price is still below the spike high and the −1 bar was a large intraday rejection at 104.7.
- **Change my mind:** below 92.

**48dd64bf47 (DOT)**
- **Read:** The decline ran from 155 to 77, and the spike reached 105.4. The pullback bottomed at 82.5 on day −7. Since then the daily lows have stepped up steadily (85.6, 86, 90.3, 93.4). Day 0 closed at 100, at the session high of 101.3 on above-average volume, which is the highest close since the spike.
- **Weight:** 0.75. This is a clean higher-low sequence and a strong close.
- **Change my mind:** below 90.

**610ac1bb50 (LINK)**
- **Read:** The base at 61–63 began lifting around day −26, before the spike, which reached 95.4. Price consolidated between 82 and 92, and day 0 broke out to 100 near its 100.9 high on strong volume. This is a new high for the whole window, above the 95.4 spike high and the 82 peak at day −119.
- **Weight:** 0.9. This is the strongest structure of the ten, a breakout with nothing overhead.
- **Change my mind:** below 88.

**f5d421658e (AVAX)**
- **Read:** The peak was 132.7, followed by a crash to 71.8 and a base at 80–85. The spike reached 105.2, and the consolidation ran 88.7–97. The close at 100 is above the consolidation top of 96.7, the lows are rising from 88.7 to 95.2, and the spike high of 105.2 is the remaining resistance.
- **Weight:** 0.7. Price has broken out of the consolidation but is still below the spike high.
- **Change my mind:** below 91.

**32123e2f4d (XRP)**
- **Read:** The base was at about 70, and the spike was the largest of the ten (119.4 intraday on heavy volume). Price faded to a 92–104 range. Day −3 was rejected at 104.2, and the close at 100 came on falling volume (0.76, then 0.73). Price is in the middle of the range with no clear direction.
- **Weight:** 0.45. A blow-off spike followed by a fade argues for caution.
- **Change my mind:** below 94 I would go flat; above 104.5 I would add.

**e1380e4600 (ADA)**
- **Read:** The move was very volatile: 130 down to 62, up to 89.5, down to 69, up to 94.8, then a base at 77. The spike reached 115.7 intraday, and the consolidation ran 84.8–101.7. The lows are rising (84.8, then 85.9, then 93.6), and the close at 100 is near the top of the range, with 101.7 to clear.
- **Weight:** 0.6.
- **Change my mind:** below 93.

**b2b732b18b (LTC)**
- **Read:** The prior high was 110 at day −119. Price based at 80–83, and the spike reached 100.9. The pullback low was 86.2, followed by a series of higher lows. On day −1 a heavy-volume bar ran to 100.7, and the close at 100 is retesting the spike high of 100.9.
- **Weight:** 0.65. Momentum is good, but price sits right at resistance.
- **Change my mind:** below 92.

**06c44dec88 (ETH)**
- **Read:** The crash low was 59.9, followed by a recovery to 77 and a base at 74–76. The spike reached 101.3, and the consolidation has been tight at 93.7–102.1. The close at 100 is near the top of that range on light volume, which looks like healthy digestion.
- **Weight:** 0.6.
- **Change my mind:** below 94.

**dc11ba9ba9 (BTC)**
- **Read:** This window has the lowest volatility. The prior high was 103.1 at day −123, and price based at 78–81. The spike reached 99, and the consolidation ran 94.9–102.4. The close at 100 came on thin volume (0.54, then 0.53), with the overhead supply at 102–103 still to clear.
- **Weight:** 0.55.
- **Change my mind:** below 95.

**9c88e3ee8d (SOL)**
- **Read:** The crash low was 56.4, followed by a recovery to 77.7 and a base at 67–73. After the spike to 96.4, price kept going and made a higher high of 103.8 on day −10. The pullback held at 91.4, above the old 92.4 peak zone. Day 0 closed at 100, near its 100.8 high, and the trend is intact.
- **Weight:** 0.65.
- **Change my mind:** below 93.

{"a549281351 (DOGE)": 0.6, "48dd64bf47 (DOT)": 0.75, "610ac1bb50 (LINK)": 0.9, "f5d421658e (AVAX)": 0.7, "32123e2f4d (XRP)": 0.45, "e1380e4600 (ADA)": 0.6, "b2b732b18b (LTC)": 0.65, "06c44dec88 (ETH)": 0.6, "dc11ba9ba9 (BTC)": 0.55, "9c88e3ee8d (SOL)": 0.65}

## Entscheidung 2026-09-13

**Strategy:** Every window shows the same structure: an old downtrend, a capitulation around day -100, a base, and then a high-volume breakout near day -25. My rule is to stay long while price holds above the post-breakout range support, and to size by how clean that consolidation is. I cut the weight when the last few weeks show blow-off spikes that reversed, or a close sitting right at support with lower highs.

### f29cb430cb (AVAX)
- **Read:** The base was 86–90. The breakout reached 114 at day -22. Since then price has ranged 96–112.5, with a second push to 112.5 at day -6 that faded back to 100. Highs are slightly lower (114, then 112.5) and lows are holding at about 99.8 and 96.2. Support is 96–99.8 and resistance is 108–112.
- **Weight:** 0.5. The breakout structure is still intact, but price sits mid-range after a failed retest of the highs.
- **Change my mind:** a close below 96.

### 688919b21e (ETH)
- **Read:** The base was 75–77. A strong breakout ran to 102.8, and price has held a tight 95–103 range for about 22 days. The day -2 spike to 107.6 was rejected, but the lows are firm. Support is 95–97 and resistance is 103–107.6.
- **Weight:** 0.6. This is the cleanest post-breakout hold, with flat consolidation above a big base.
- **Change my mind:** a close below 95.

### 8ac68ebf10 (ADA)
- **Read:** The base was 85. The breakout wick hit 127, followed by a wide, choppy range of 93–114. An earlier breakout at day -72 to 98 fully faded. The spike to 114 at day -5 has unwound to 100. Support is 93–94.7 and resistance is 110–114.
- **Weight:** 0.4. The swings are wide, and this asset has a history of failed breakouts.
- **Change my mind:** a close below 93.

### 3bf15455f4 (DOGE)
- **Read:** The base was 84–85. The breakout reached 122, and price has ranged 97–115 since. Price is near the lower part of the range. Lows are at 97.2 (day -11) and 99.6 (today), and the spike to 115.5 at day -8 failed. Support is 97–99.6 and resistance is 110–115.
- **Weight:** 0.45. Price is holding support, but the recent highs were rejected.
- **Change my mind:** a close below 97.

### b21f165786 (XRP)
- **Read:** This had the deepest base (74–75, after a long slide). It had the biggest-volume breakout, to 126.7, and has ranged 97.7–115 since. Repeated tests of 98–100 have held. Support is 97.7–99 and resistance is 108–110.6.
- **Weight:** 0.5. The breakout has strong volume behind it, and range support is still intact.
- **Change my mind:** a close below 97.5.

### 72f2b2b720 (SOL)
- **Read:** The base was 75–77. Price climbed in a staircase to 111.4 at day -17, then ranged 98–108. The lows are rising slightly: 98.1, then 98.7, then 99.9. Support is 98–99 and resistance is 106.5–108.
- **Weight:** 0.5. The trend was orderly, and price is now at range support.
- **Change my mind:** a close below 98.

### fa0195ffec (DOT)
- **Read:** The base was 76. The first breakout to 103 fully faded back to 81. A second parabolic run reached 128.5 at day -5 on 4x volume, then reversed hard, with four straight lower closes back to 100. This looks like a blow-off top with distribution. Support is 96–99.6 (the gap area) and resistance is 104–112.
- **Weight:** 0.15. The failed blow-off and falling momentum make this the weakest setup.
- **Change my mind:** a reclaim above 112.

### 139843b9ea (BTC)
- **Read:** The base was 82–84. The breakout reached 103.5, followed by a tight 99–107 range for 23 days on low volume. Today's close of 100 is at range support (99.0–99.5). Support is 99 and resistance is 104.4–107.
- **Weight:** 0.55. The consolidation is tight and orderly, and the entry is right at support.
- **Change my mind:** a close below 98.9.

### 374267e35f (LINK)
- **Read:** The base was rising from 72 to 85 before the breakout, so the uptrend was strong going in. The breakout reached 112.6, and a second spike hit 122 at day -6, which has now fully unwound to 100. Support is 97.4–99.6 and resistance is 108–114.
- **Weight:** 0.4. The underlying trend is good, but the recent spike failure is a concern.
- **Change my mind:** a close below 97.

### 9e06dfe667 (LTC)
- **Read:** The base was 82–84. The breakout reached 103 and faded to 88 by day -14. A second leg wicked to 110.6 at day -6, and price has drifted back to 100. Higher lows (88, then 96) remain intact. Support is 96–97 and resistance is 103–110.
- **Weight:** 0.45. The higher-low structure helps, but the upper wicks show selling into strength.
- **Change my mind:** a close below 96.

{"f29cb430cb (AVAX)": 0.5, "688919b21e (ETH)": 0.6, "8ac68ebf10 (ADA)": 0.4, "3bf15455f4 (DOGE)": 0.45, "b21f165786 (XRP)": 0.5, "72f2b2b720 (SOL)": 0.5, "fa0195ffec (DOT)": 0.15, "139843b9ea (BTC)": 0.55, "374267e35f (LINK)": 0.4, "9e06dfe667 (LTC)": 0.45}

## Entscheidung 2026-09-20

**Strategy:** I follow the trend and check where price sits in its structure. I go long when price holds above its post-breakout base and is pressing into or through range highs. I size down when the window is a wide, whipsawing range or has just made a parabolic move. My weight rises with the cleanness of higher lows and falls with distance from support and with exhaustion risk.

## 5d1ca8e227 (LTC)
- **Read:** The crash bottomed near 69. The base then broke out around day -30, with the move to 90 on heavy volume. Since then the lows keep rising: 81.6, then 86.4, then 87.8. Price has reclaimed 99–100 after a strong day -2. The only overhead reference is the 101–103 zone from days -133 and -13. The trend is clearly up.
- **Weight:** 0.7. The trend is strong, but price sits just under resistance.
- **Change my mind:** a close below 91.

## 3cc40b50b3 (XRP)
- **Read:** A blow-off spike reached 120.5 on day -29. Since then price has chopped in a wide 89–108 range. Day -5 swung from 106 to 89.7 inside one session. Price is now 100, mid-range, with no directional edge and high volatility.
- **Weight:** 0.4. Choppy ranges reward small sizing.
- **Change my mind:** below 89 (range breakdown), or a close above 106, which would make me add.

## 86c95c08bc (AVAX)
- **Read:** This one went vertical: 67 to 72.5, then 89, then 100 in three days, on volume of 2.5, 3.9 and 6.1. It is a new 180-day high, above 92.7. Day 0 traded 83.4–101.4 and closed near the high. Momentum is very strong, but the move is parabolic and extended far above the 63–72 base.
- **Weight:** 0.6. I want the momentum, but I respect the exhaustion risk.
- **Change my mind:** below 89, which would be failing back into the gap.

## 0412fa0591 (DOT)
- **Read:** The bigger trend is down from 123, with a low near 64. A spike reached 113 on day -12 and then retraced to 82. Price has now recovered to 100 with a higher low at 82.3. Overhead supply sits at 103–113.
- **Weight:** 0.5. The recovery is constructive, but this window is the most volatile.
- **Change my mind:** below 88.

## 1ac1b50b72 (ADA)
- **Read:** A spike reached 113.4 on day -29. Price has ranged 83–101 since, with highs near 99–103 that keep capping it. It now sits at 100, the top of that range.
- **Weight:** 0.5. It is testing resistance and has not broken it.
- **Change my mind:** below 88, or a close above 103, which would make me add.

## 309f501f3f (DOGE)
- **Read:** The spike topped at 115.5. Since then the highs keep falling: 109, then 105.4, then 104.6. The lows sit around 90–93. Price is now 100, mid-range, and the structure is drifting lower.
- **Weight:** 0.4.
- **Change my mind:** below 91, or a close above 105, which would make me add.

## 796e6a471e (LINK)
- **Read:** The uptrend runs from the 56 low. Price peaked at 109.3 on day -13, pulled back to a higher low at 84.8, and is now back at 100. Resistance is at 105–109.
- **Weight:** 0.6.
- **Change my mind:** below 86.

## 7d067f937c (ETH)
- **Read:** A clean breakout ran from 72 to 95. It was followed by a tight, low-volatility consolidation between 89 and 97 for about four weeks. Price is now pushing out to 100, above the 180-day high of about 93. This is a textbook flag resolving upward.
- **Weight:** 0.75.
- **Change my mind:** below 92.

## 3d593fff24 (SOL)
- **Read:** The highs keep rising: 92.4, then 99.5, then 102.8. The lows also rise from 86.2. The day -2 breakout closed at 101.4 and is now holding at 100. The trend is strong and orderly.
- **Weight:** 0.7.
- **Change my mind:** below 91.

## 9c7f2c51fd (BTC)
- **Read:** After the breakout, price has spent about a month in a tight 93–101 range. It now sits at 100, near the top of that range, and the 180-day high is 102.1. Volatility is low, which favors an upside resolution, but the break has not been confirmed.
- **Weight:** 0.6.
- **Change my mind:** below 93.

{"5d1ca8e227 (LTC)": 0.7, "3cc40b50b3 (XRP)": 0.4, "86c95c08bc (AVAX)": 0.6, "0412fa0591 (DOT)": 0.5, "1ac1b50b72 (ADA)": 0.5, "309f501f3f (DOGE)": 0.4, "796e6a471e (LINK)": 0.6, "7d067f937c (ETH)": 0.75, "3d593fff24 (SOL)": 0.7, "9c7f2c51fd (BTC)": 0.6}

## Entscheidung 2026-09-27

**Strategy:** Trend-following with a penalty for climaxes. I go long when price is at or near new highs, the structure is a series of higher lows, and the advance was orderly. I cut size when the latest leg was a high-volume spike, or when the price sits under a higher overhead high in the window. Weight reflects trend quality: 0.8 for clean breakouts to new highs, about 0.5 for spike-driven or range-bound setups.

## 9287988f11 (SOL)
- **Read:** Clean uptrend since the -114 crash low of about 49, with a staircase of higher highs (80.7 → 90.7 → 98.4 → 102.4). Price at 100 is at the window's all-time high, and the steps were orderly on moderate volume. Support is 92–94, and the breakout pivot is 98.
- **Weight:** 0.8, for a strong trend at new highs with no climax.
- **Change my mind:** a close below 92.

## 4fbdb840eb (AVAX)
- **Read:** Price based at 58–60 for months, then went vertical on days -8 and -7 (69.8 → 103.7) on extreme volume (5.7). Since then it has chopped in a 92–108 range with a lower high (103.5 versus 108.2). This is a blow-off followed by a range, not a trend.
- **Weight:** 0.5, since the breakout is real but extended and digesting.
- **Change my mind:** a close below 91, the range floor.

## c74955b1d0 (ADA)
- **Read:** A choppy uptrend from 56, with higher lows at 74.6, 75.7 and 91.5. Recent highs are 101.8 and 104, but the older high of 113 (day -140) is overhead. The swings are wide.
- **Weight:** 0.6, because the trend is up but there is resistance and volatility.
- **Change my mind:** a close below 91.

## 134bbbf5e6 (DOGE)
- **Read:** Price is still below the earlier 116–122 highs. A spike to 109 on day -5 (volume 3.8) was immediately sold to 94, so it is now in a 94–109 range.
- **Weight:** 0.5, because there is overhead supply and the spike failed.
- **Change my mind:** a close below 94.

## f94b670b5e (DOT)
- **Read:** A spike to 101 at day -19 collapsed to 74. Price then recovered to 100–103, which is a potential double top at 101–103, and the swings are large (85 to 103 within the last week).
- **Weight:** 0.5.
- **Change my mind:** a close above 103 would raise the weight; a close below 85 would take it to flat.

## 907691467a (ETH)
- **Read:** A breakout gap at day -39 (71 → 84) was followed by a smooth, low-volatility grind higher. Price is now in a tight 99–104 coil near the 104.4 high, with volume drying up, which is constructive.
- **Weight:** 0.7.
- **Change my mind:** a close below 96.

## 443020b8b9 (LINK)
- **Read:** A strong uptrend with higher highs (77.7 → 97.6 → 103.4) and higher lows (77 → 86). Price is at new window highs, well above the old 77 peak, and volume confirms the up-legs.
- **Weight:** 0.8.
- **Change my mind:** a close below 86.

## d64d1a4e87 (BTC)
- **Read:** A steady uptrend with low volatility. Price cleared the prior 98 high (day -144) and is now consolidating tightly at 98–103.5. It is an orderly structure.
- **Weight:** 0.7.
- **Change my mind:** a close below 98.

## 6b21e4aa2a (XRP)
- **Read:** A wicky spike to 112 on day -36, then a wide 83–110 range. Recent highs are 106–109, but price is fading back to 100 on heavy, two-sided volume.
- **Weight:** 0.5, since it is range-bound and noisy.
- **Change my mind:** a close below 95.

## fa5c314b71 (LTC)
- **Read:** A climactic gap on day -3 (86.8 → 100.9, volume 6.7) put price at new highs far above the old 85. It has held 99–105 for three days, but the gap is unfilled and the move is extended.
- **Weight:** 0.6.
- **Change my mind:** a close below 96, which would signal that the gap is failing.

{"9287988f11 (SOL)": 0.8, "4fbdb840eb (AVAX)": 0.5, "c74955b1d0 (ADA)": 0.6, "134bbbf5e6 (DOGE)": 0.5, "f94b670b5e (DOT)": 0.5, "907691467a (ETH)": 0.7, "443020b8b9 (LINK)": 0.8, "d64d1a4e87 (BTC)": 0.7, "6b21e4aa2a (XRP)": 0.5, "fa5c314b71 (LTC)": 0.6}
