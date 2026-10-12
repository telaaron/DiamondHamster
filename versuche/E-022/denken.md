# E-022: was die KI gedacht hat (Set A)

Volle Antwort des Deciders pro Entscheidungswoche, unverändert. Er sah weder Datum noch Coin-Namen; die Namen in Klammern sind erst danach eingesetzt. Gesendeter Prompt und Daten: runs/<set>/<woche>/requests.json.

## Entscheidung 2026-07-05

# Analysis

**1. Strategy:** I can only veto a signal of 1, never override a 0. Every window here has signal 0, so every weight is 0. For each one I still give my read of the market and the level that would flip the rule back to 1. At that point I would decide whether to confirm or veto, based on whether price closes above the 20-week average with structure behind it (higher lows, holding support) or only spikes there on a short-covering bounce.

**2. Windows**

### 67120412c6 (SOL)
- **Read:** The asset crashed from about 170 to 96 early in the window. It then ranged between 95 and 120, broke down to about 74 around day -29, and has recovered in a choppy way back to 100. This is the window closest to the rule's line: close 100.0 against an average of 100.4.
- **Levels:** resistance 102–103, support 83–85 and then 74.
- **Weight:** 0, because the signal is 0.
- **Change of mind:** a weekly close above about 103 would flip the signal, and I would likely confirm it if it held above 98.

### c52e3684bc (LINK)
- **Read:** The trend is down. Price peaked near 133 at day -56, fell to 87 at day -30, made a lower high near 106 and a retest low around 87. It is now bouncing to 100 on low volume. The average is 109.
- **Levels:** resistance 101.5–107, support 87–88.
- **Weight:** 0.
- **Change of mind:** a sustained close above about 109.

### 7b2fb1c341 (ETH)
- **Read:** The asset is in a decline from about 135 at day -79, with a capitulation leg to 84. The bounce to 100 meets a prior lower high near 103.6. The average is 113.
- **Levels:** resistance 103.6, support 85.
- **Weight:** 0.
- **Change of mind:** a close above about 113.

### b0ed2bbdaf (DOGE)
- **Read:** Price fell from a 152 peak at day -52 to 89 and is now bouncing to 100. It sits well below the average of 120, so the trend is firmly down.
- **Levels:** resistance 102 and then 113–119, support 89–90.
- **Weight:** 0.
- **Change of mind:** a close above about 120.

### 5e5ccc578f (BTC)
- **Read:** The trend is down from 130 at day -60. Price made a low of 91, a lower high at 105.7, and a second low of 91. It is now back at 100. The average is 110.
- **Levels:** resistance 105.7, support 91.
- **Weight:** 0.
- **Change of mind:** a close above about 110.

### 009af2e782 (LTC)
- **Read:** The asset is down from 132 at day -56 to a low of 86. Its recovery to 100 is at the top of a recent range. The average is 113.
- **Levels:** resistance 101, support 86.
- **Weight:** 0.
- **Change of mind:** a close above about 113.

### fc6ddd161a (XRP)
- **Read:** Price fell from 134 to 87. Earlier it was rejected at 111.8 on day -20, and it is now bouncing to 100. The average is 114.
- **Levels:** resistance 102.3 and then 112, support 87.
- **Weight:** 0.
- **Change of mind:** a close above about 114.

### d52c62d3f9 (DOT)
- **Read:** This is a long secular decline from about 250, with a lower high at 163 and a low of 90. It is now bouncing to 100, far below the average of 138.
- **Levels:** resistance 102 and then 119, support 90.
- **Weight:** 0.
- **Change of mind:** a close above about 138.

### 7523652526 (AVAX)
- **Read:** The asset is down from 151 to a high-volume flush to 82 at day -16. It is recovering to 100 under a lower high of 102.8. The average is 123.
- **Levels:** resistance 102–103, support 82–86.
- **Weight:** 0.
- **Change of mind:** a close above about 123.

### 2971f146b7 (ADA)
- **Read:** Price crashed from 152 to a low of 73 at day -10. That was followed by a violent rally of about 30% in four sessions on heavy volume, reaching 105.5 and closing at 100. The move looks like short covering from oversold levels, and price is still far below the average of 122.
- **Levels:** resistance 105.5, support 75 and then 73.
- **Weight:** 0.
- **Change of mind:** a close above about 122.

{"67120412c6 (SOL)": 0.0, "c52e3684bc (LINK)": 0.0, "7b2fb1c341 (ETH)": 0.0, "b0ed2bbdaf (DOGE)": 0.0, "5e5ccc578f (BTC)": 0.0, "009af2e782 (LTC)": 0.0, "fc6ddd161a (XRP)": 0.0, "d52c62d3f9 (DOT)": 0.0, "7523652526 (AVAX)": 0.0, "2971f146b7 (ADA)": 0.0}

## Entscheidung 2026-07-12

**Strategy.** I confirm a signal of 1 only when price trades in a healthy uptrend above a rising average, without an exhaustion spike or a breakdown through recent support. I veto when price is barely above a falling average inside a larger downtrend, or when it has just failed at resistance. When the signal is 0 the weight is 0, so in every window below my job is only to say what would change the picture.

## 9be8ca0017 (LTC)
- **Read:** Long downtrend from about 174 to a capitulation low of 89.3 (day -18). Price then recovered to 104.9 and has drifted back to 100. Resistance sits at 104–105 and support at 89–92, all well below the 20-week average of 116.7.
- **Weight:** 0. The signal is flat and the trend is still down.
- **Change of mind:** A sustained close above about 117, which reclaims the average.

## fe3fbee8f8 (XRP)
- **Read:** Crash from about 197, with the big drop at days -40 to -37 reaching 98.5. A bounce failed at 119.1, price made a lower low at 92.9, then rebounded to 109.1 and faded back to 100. The highs are lower each time.
- **Weight:** 0. The signal is flat.
- **Change of mind:** A close above about 120, the average and the 119 swing high.

## e986807827 (AVAX)
- **Read:** Steep decline from 228 to a low of 88.7 (day -23) on heavy volume. A rebound stalled at 111.1 and price is back at 100. The average is far above, at 131.3.
- **Weight:** 0. The signal is flat.
- **Change of mind:** A close above about 131.

## 00237471f5 (SOL)
- **Read:** Downtrend from 190 to 78.2 (day -36), then a higher low at 83.3. A rally reached 109.2 and pulled back to 100. Structure is improving, and the average at 106.1 is the nearest of all the windows.
- **Weight:** 0. The signal is flat.
- **Change of mind:** A close above about 106–109, which would turn the signal on and confirm the higher-low base.

## 8f8ae7ff49 (DOGE)
- **Read:** Declined from 204 to 106.8 (day -36), then broke lower to 95.6 (day -12). A bounce to 109.2 failed, and price now sits at 100. The pattern is lower lows.
- **Weight:** 0. The signal is flat.
- **Change of mind:** A close above about 127.

## c5f6d5b509 (DOT)
- **Read:** Large decline from 270 to a low of 94.2 (day -14). A bounce capped at 107.6 and price is now at 100. The average is far above, at 141.
- **Weight:** 0. The signal is flat.
- **Change of mind:** A close above about 141.

## afcd0b01f4 (BTC)
- **Read:** Grinding decline from 150 to 90.6 (day -11). Price recovered to about 100–101, which is resistance, with the average at 109.7.
- **Weight:** 0. The signal is flat.
- **Change of mind:** A close above about 110.

## e172427295 (ETH)
- **Read:** Decline from 184, with a double bottom near 83.3 and 83.7. Price recovered to 101.5 and now sits at 100, testing that level as resistance. The average is 111.4.
- **Weight:** 0. The signal is flat.
- **Change of mind:** A close above about 111.5.

## 39665efc8c (LINK)
- **Read:** Decline from 176, with a double bottom near 87.5 and 87.7. Price recovered to 102.2 and now sits at 100. The average is 109.5.
- **Weight:** 0. The signal is flat.
- **Change of mind:** A close above about 110.

## 0078b46bcf (ADA)
- **Read:** Collapse from 260 to 85.3 (day -17). A volume spike then took price to 123.4 (day -8), and that move fully faded back to 100. The failed breakout is bearish, and the average is 139.6.
- **Weight:** 0. The signal is flat.
- **Change of mind:** A close above about 140.

{"9be8ca0017 (LTC)": 0.0, "fe3fbee8f8 (XRP)": 0.0, "e986807827 (AVAX)": 0.0, "00237471f5 (SOL)": 0.0, "8f8ae7ff49 (DOGE)": 0.0, "c5f6d5b509 (DOT)": 0.0, "afcd0b01f4 (BTC)": 0.0, "e172427295 (ETH)": 0.0, "39665efc8c (LINK)": 0.0, "0078b46bcf (ADA)": 0.0}

## Entscheidung 2026-07-19

**Strategy:** I take the rule's signal as the default and veto a "1" only when the price structure clearly contradicts it: a fresh breakdown below the average with heavy volume, lower highs rolling over, or a spike-and-fail with no follow-through. When the signal is 0, the weight must be 0. In each window I still note the level that would turn the setup constructive, meaning a reclaim of the 20-week average or of the most recent swing high.

### 9b2a480b9f (BTC)
- **Read:** The downtrend from the ~127 peak (day -70) broke hard at -47 to -44, on heavy volume down to 91.4. Price has since been basing between 90 and 101, with a slightly higher low at 95.5 (day -6). Price is at 100, below the 108 average. This looks like repair, not a trend.
- **Weight:** 0, which is the signal.
- **Change my mind:** a weekly hold above ~104, then a reclaim of 108.

### 47ec84058c (DOGE)
- **Read:** The decline is deeper: from ~163 (day -66) to the ~96 low (day -19). The bounce to 109.6 failed, and price is drifting at 100 on very thin volume (0.16–0.19). The average sits far above at 126. Lower highs are intact.
- **Weight:** 0.
- **Change my mind:** a break above 109.6, though the rule only turns on above ~126.

### 058e024acd (LINK)
- **Read:** The low was 83.4 (day -43), retested at 83.6 (day -24), which makes a rough double bottom. Price has recovered to 100 and pushed to 103 (day -4), but is still below the 104.2 average. Volume on the rally is light.
- **Weight:** 0.
- **Change my mind:** a close above ~104–105 that holds. Below 92, the base is invalidated.

### 4940b0a2fa (AVAX)
- **Read:** The crash from ~140 to 96 was followed by a further flush to 87.9 at day -30. The rebound capped at ~110 (day -15), and price has since faded to 100 with a lower high. The average is at 128, far above.
- **Weight:** 0.
- **Change my mind:** a break above 110. A loss of 97 would point toward retesting 88.

### 022097348a (XRP)
- **Read:** The fall from ~135 bottomed at 91.9 (day -23). The bounce to 107.9 (day -15) faded, and price is now range-bound between 96 and 103 at 100. It is below the 117 average with a lower-high structure.
- **Weight:** 0.
- **Change my mind:** a break above 108.

### 64b2b7efd1 (ETH)
- **Read:** There was a double low at ~80.4 and 80.8 (days -43 and -23). The rally went to 104 (day -4), then pulled back to 100. Price is just under the 107.3 average. Of the group, this has the most constructive base.
- **Weight:** 0.
- **Change my mind:** a hold above 104 and a reclaim of ~107. Below 93, the base fails.

### ed83d1a588 (DOT)
- **Read:** This is a long-term downtrend from 238 to 97 (day -21). Price is grinding sideways between 98 and 110, and the day-0 close of 100 is near the bottom of that range. It sits far below the 140.7 average.
- **Weight:** 0.
- **Change my mind:** a break above 110.7. Below 97, the next leg lower is in play.

### 19fe36d2b1 (SOL)
- **Read:** The low was 78.7 (day -43), with a higher low at 83.8 (day -24). The rally reached 110 (day -15), then retraced to the 96–103 range. Price is below the 106.4 average.
- **Weight:** 0.
- **Change my mind:** a reclaim of 106.5 and then 110. Below 96, it rolls over.

### a9b6f544e0 (LTC)
- **Read:** The lows were 86.1 (day -43) and 83.5 (day -25). Price is rising steadily, and day -1 broke above the ~98 range top on 1.29 volume. Price is at 100, still below the 108.4 average. The structure is improving.
- **Weight:** 0.
- **Change my mind:** follow-through above 102, then 108.4. Below 92, the breakout fails.

### 891d4b6293 (ADA)
- **Read:** A capitulation took price to 89.4 (day -43), then to 83.1 (day -24). A sharp spike to 120 (day -15) fully reversed. Price is now churning between 93 and 102. That failed spike marks resistance, and the average is far away at 132.9.
- **Weight:** 0.
- **Change my mind:** a sustained break above 110. Below 93, it likely retests 83.

{"9b2a480b9f (BTC)": 0.0, "47ec84058c (DOGE)": 0.0, "058e024acd (LINK)": 0.0, "4940b0a2fa (AVAX)": 0.0, "022097348a (XRP)": 0.0, "64b2b7efd1 (ETH)": 0.0, "ed83d1a588 (DOT)": 0.0, "19fe36d2b1 (SOL)": 0.0, "a9b6f544e0 (LTC)": 0.0, "891d4b6293 (ADA)": 0.0}

## Entscheidung 2026-07-26

## Strategy

I confirm a 1 signal only when the price structure backs it: higher lows, the close holding above recent swing highs, and no nearby breakdown. I veto when the close is only marginally above the 20-week average and the structure is still a downtrend or a stalled range under resistance. Windows with signal 0 are flat by rule; for those I only note the levels that would matter.

## dd034a9d91 (SOL)
- **Read:** A crash from about 107 to 81 around day -51 was followed by a rebound to about 109 (day -22). Since then price has drifted between 95.6 and 103, on fading volume. The close of 100 sits below the 105.5 average.
- **Weight:** 0. The signal is flat.
- **Change of view:** A close above about 109.

## c2d12a311c (ADA)
- **Read:** A collapse from about 140 to 94 was followed by a spike to 116 (day -22) that failed. Since then price has ranged between 94 and 109. The close of 100 is far below the 130.6 average.
- **Weight:** 0. The signal is flat.
- **Change of view:** A close above about 116.

## 5cbae5ced9 (DOT)
- **Read:** A long downtrend has run from 200+ to the 96–108 range, with lower highs throughout. The close of 100 is well under the 135.6 average.
- **Weight:** 0. The signal is flat.
- **Change of view:** A close above about 108.

## 8a30d14736 (ETH)
- **Read:** A crash to about 77 was followed by a steady recovery with higher lows: 77.4, then 87.7, then 94.5. Day 0 pushed to 100.6, but the close of 100 is still under the 102.8 average. Resistance sits at 103–104.
- **Weight:** 0. The signal is flat.
- **Change of view:** A close above about 104.

## b6050fd9be (DOGE)
- **Read:** The structure is a lower high at 108 after a breakdown from 137. Price is ranging between 93 and 103. The close of 100 is well under the 123.5 average.
- **Weight:** 0. The signal is flat.
- **Change of view:** A close above about 108.

## 4afac67e13 (BTC)
- **Read:** After the drop from 113 to 89, price has climbed slowly through 89–102 with higher lows. The close of 100 is below the 106.8 average. Resistance is at 102.4, then 109.
- **Weight:** 0. The signal is flat.
- **Change of view:** A close above about 107.

## c96061ae85 (LINK)
- **Read:** Price crashed from about 104 to 79.4 (days -51 to -31). Since then it has set a clean series of higher lows: 79.4, 80.2, 85.2, 88.3, 90.7, 94.0. Day 0 was a strong bar from 95.0 to 100.0, closing above the prior swing high of 99.3 and just above the 99.2 average. Volume on the rally is light. Overhead supply sits at 102–104, the pre-crash range.
- **Weight:** 1, confirm. The higher-low staircase and the breakout above 99.3 support the signal, even though the margin over the average is thin.
- **Change of view:** A close below about 94, which would break the last higher low.

## 0d7793a9df (AVAX)
- **Read:** A crash to 84 was followed by choppy trade between 91 and 105. The close of 100 is far below the 121.2 average.
- **Weight:** 0. The signal is flat.
- **Change of view:** A close above about 105.5.

## dc165758f7 (LTC)
- **Read:** After bottoming near 82, price has made higher lows and is pressing against 100–101. The close of 100 is still below the 106.2 average.
- **Weight:** 0. The signal is flat.
- **Change of view:** A close above about 106.

## 43b856b5dc (XRP)
- **Read:** After the crash, price is ranging between 91 and 106 with a lower high at 104.6. The close of 100 is below the 114.8 average.
- **Weight:** 0. The signal is flat.
- **Change of view:** A close above about 106.5.

{"dd034a9d91 (SOL)": 0.0, "c2d12a311c (ADA)": 0.0, "5cbae5ced9 (DOT)": 0.0, "8a30d14736 (ETH)": 0.0, "b6050fd9be (DOGE)": 0.0, "4afac67e13 (BTC)": 0.0, "c96061ae85 (LINK)": 1.0, "0d7793a9df (AVAX)": 0.0, "dc165758f7 (LTC)": 0.0, "43b856b5dc (XRP)": 0.0}

## Entscheidung 2026-08-02

## Strategy

I can only veto a long signal, never create one. When the rule says flat (0), my weight is 0 with no exceptions. When it says invested (1), I confirm unless the structure clearly argues against it: price barely above a falling average, a failed breakout on heavy volume, or a fresh lower high under resistance.

---

### 189d9404a4 (XRP)
- **Market read:** Long decline from the 130s, with a breakdown near day -61 to about 101. Since then price has been in a base between 93 and 107 and is now 100. The 20-week average is 115.9 and falling, and volume is drying up. Support is 93–96; resistance is 105–107, then 114.
- **Weight:** 0. The signal is flat, so there is no choice.
- **Change-of-mind level:** A close above about 116 (the average) would turn the signal on, and I would then judge it on the merits.

### 064909181e (BTC)
- **Market read:** Topped around 129 at day -84, then broke down to 93 at day -58. It has recovered to a 98–105 range, with closes going sideways around 100. The average is 109.2. Support is 91–94; resistance is 105, then the 109 average.
- **Weight:** 0. The signal is flat.
- **Change-of-mind level:** Above about 109.

### a6695d8d24 (DOT)
- **Market read:** Steady decline from the 170–200 area down to the mid-90s. A gap down at day -6 took it to 95, and it has rebounded to 100. The average is far above at 136.5, so the downtrend is fully intact. Support is 93; resistance is 106–111.
- **Weight:** 0. The signal is flat.
- **Change-of-mind level:** Above about 136. Realistically, I would need a weekly close above 111 before I would even start to reconsider.

### 8425e606d1 (AVAX)
- **Market read:** Crashed from about 137 to about 100 at days -61 to -58, then made a capitulation low at 86.7 on day -44 with heavy volume. It has since been ranging between 95 and 106. Day 0 brought a strong reversal from 94.4 to 100 on rising volume. The average is 122.2. Support is 92–94; resistance is 106–108.
- **Weight:** 0. The signal is flat.
- **Change-of-mind level:** Above about 122.

### 643304058b (ETH)
- **Market read:** Broke down to about 80–84 at day -57, then put in a higher low near 80 at day -37. It has recovered to a 98–104 range, a modest base-building structure. The average is 105.8, and price is the closest to it of any window. Support is 96–97, then 92; resistance is 104–105.
- **Weight:** 0. The signal is flat.
- **Change-of-mind level:** A close above about 106 would flip the signal. I would likely confirm that one if it came with volume.

### 9ba9abb9cf (DOGE)
- **Market read:** Peaked around 163 at day -80, then slid steadily. After the breakdown it made lower highs at 130, 125 and 112, and it now sits at 96–105. The average is 126.1. Support is 96; resistance is 105, then 110.
- **Weight:** 0. The signal is flat.
- **Change-of-mind level:** Above about 126.

### a4b8895bc8 (LINK)
- **Market read:** Topped around 128 at day -84, then broke down to about 84 by day -58. It retested at 84 on day -38 and has recovered to a 94–105 range. The average is 103.8 and close. Support is 94–96; resistance is 105–106.
- **Weight:** 0. The signal is flat.
- **Change-of-mind level:** Above about 104. If that happens with a close above 106, I would confirm.

### 074e08afce (LTC)
- **Market read:** Topped around 135 at day -84, then fell to an 88–90 low around day -39. It recovered to 107 at day -7 and has since pulled back to 99–100. The average is 112.4. Support is 97–98; resistance is 107–108.
- **Weight:** 0. The signal is flat.
- **Change-of-mind level:** Above about 112.

### ab5706813f (SOL)
- **Market read:** Broke down to about 82–84 at day -57, then rallied sharply to 113 at day -30. That rally failed: the pattern since is lower highs at 108 and 106 and a drift lower to 96–100. The average is 108.8. Support is 96; resistance is 106–108.
- **Weight:** 0. The signal is flat.
- **Change-of-mind level:** Above about 109.

### 2445420eca (ADA)
- **Market read:** Severe decline from about 150 to a low near 73 at day -38. A spike to 105 at day -29 faded back to the 82–92 range. Day 0 broke out to 100 on 1.7x volume, which is a strong short-term thrust, but price is still below the 112 average and below the day -29 high of 105. Support is 88, then 82; resistance is 101–105.
- **Weight:** 0. The signal is flat.
- **Change-of-mind level:** Above about 112.

---

{"189d9404a4 (XRP)": 0.0, "064909181e (BTC)": 0.0, "a6695d8d24 (DOT)": 0.0, "8425e606d1 (AVAX)": 0.0, "643304058b (ETH)": 0.0, "9ba9abb9cf (DOGE)": 0.0, "a4b8895bc8 (LINK)": 0.0, "074e08afce (LTC)": 0.0, "ab5706813f (SOL)": 0.0, "2445420eca (ADA)": 0.0}

## Entscheidung 2026-08-09

## Strategy

The rule decides the default and I only remove risk; I never add it. When the signal is 1, I confirm unless the window shows a clear false break: price barely above the average inside a falling structure, a rally on fading volume into overhead resistance, or a fresh breakdown below recent support. When the signal is 0, my weight is 0 by construction, so for those windows my analysis covers what would need to happen before a future "1" would deserve confirmation.

All ten windows have signal 0, so every weight below is 0. For each window, the "change my mind" price is the level that would flip the rule to 1 and that I would then confirm. That level is roughly the 20-week average, plus whatever overhead structure sits near it.

## 92dfcbd8f0 (XRP)
- **Read:** A long range between 128 and 145 broke down hard around day -68 to -65, with heavy volume and a low near 102. A relief rally failed at 120–125 (day -55). Since then price has made lower highs: 115, 113, 108, 106. It is now pinned at 99–101 on shrinking volume, sitting on the 98–100 lows. Below the 120.6 average, with the trend down.
- **Weight:** 0 (signal 0).
- **Change my mind:** A weekly close above about 113 (the recent swing highs), and ultimately above 120.6. A close under 98 opens the 2024-style low area near 98–95.

## aa7a8df9fc (DOGE)
- **Read:** The run-up to 166–171 (days -96 to -87) fully reversed. A crash at day -65 broke through 145 to about 114. The bounce stalled at 128–133, then price slid steadily to a 98–102 base over the last three weeks on very low volume. Lower highs throughout. The average at 127.3 is far above.
- **Weight:** 0.
- **Change my mind:** A recovery above 107–108 would be the first sign. A real reversal needs a close above about 127. Support is 97.6–98.6; losing it extends the decline.

## ba12ba784e (BTC)
- **Read:** A trend from 102 to 127 topped near day -91, rolled over, then gapped down on heavy volume from 113 to 91. Since then it has recovered in steps (89.5 low, then 96–100) and is flattening at 100 with a slightly rising base of 96–97. This is constructive but still under the 106.7 average.
- **Weight:** 0.
- **Change my mind:** A close above 103.2 (the day -19 high) and then 106.7 would turn it into a likely-confirm. A break below 96 invalidates the base.

## 631f0fd964 (LINK)
- **Read:** The run to 131 failed. A crash at day -65 reached 85.6–87, and price has since rebuilt into a 97–108 range, with the latest highs at 108 (day -14) and 105.6. It is choppy, holding around 100, and below the 106.0 average.
- **Weight:** 0.
- **Change my mind:** A close above 108 clears both the range top and the average. A close below 96 (the day -8 low area) brings back the 88–91 lows.

## 75bb8fc285 (AVAX)
- **Read:** A range from 135 to 163 broke down at day -65 to about 97–105, then had a second flush to 88.5 at day -51. Since then it has been a choppy recovery capped at 106–110, with the latest high a 108.8 spike. Price sits mid-range at 100, far below the 122.7 average.
- **Weight:** 0.
- **Change my mind:** A close above 110 would break the range top. Below 94 (the day -8 low) the 88.5 low comes back into play.

## 6adc7604e1 (LTC)
- **Read:** A slow decline from 133 led into a breakdown at day -68 to day -64, bottoming at 86.4. Since then there are higher lows (86, 90, 95, 96) and a 96–106 range, with a test of 105–106 rejected. Price is now at 100, still below the 109.6 average, though the structure is basing.
- **Weight:** 0.
- **Change my mind:** A close above 106 would put a reclaim of 109.6 in play. A close below 96 breaks the higher-low sequence.

## 1b0ff0660e (ADA)
- **Read:** A deep crash to 71 at day -45 was followed by a spike to 102 that failed. Price then built a base at 80–90, and since day -7 has ripped from 87 to 108.8 intraday on rising volume. Today it pulled back to 100. This is the strongest recent momentum in the set, but it is still under the 108.0 average, and the 102.8–108.8 zone has rejected price twice.
- **Weight:** 0.
- **Change my mind:** A close above 109 clears the spike high and the average, and I would likely confirm it. Below 95.6 the breakout fails.

## b4c7fae196 (ETH)
- **Read:** An uptrend to 129 ended in a crash to 79 at day -45. Price has since recovered steadily to a 96–103 range. Recent highs are capped at 102–104 with lows at 95.4. Volume is very thin, and price is below the 104.1 average but close to it.
- **Weight:** 0.
- **Change my mind:** A close above 104.1–104.5, ideally on volume, would reclaim the average. A close below 95 means the range breaks down.

## e1d49d54b0 (SOL)
- **Read:** The crash bottomed at 78.8, and a V-recovery reached 110 at day -36. Since then price has made lower highs (110, 104.5, 103.4, 101) and fell to 92.5 at day -8. It bounced to 100 at day -1 to day 0. Below the 104.4 average, with the intermediate trend down.
- **Weight:** 0.
- **Change my mind:** A close above about 104.5 breaks the lower-high sequence and the average. A close below 92.5 confirms continued weakness.

## 01ec3750f9 (DOT)
- **Read:** A blow-off gap to 219 at day -165 has been distributed lower ever since. A crash at day -65 reached about 110, and price kept trending down to 93.6 (day -13). A bounce to 108.9 at day -5 was immediately rejected, and price is back to 100. It is far below the 132.7 average, a clear downtrend.
- **Weight:** 0.
- **Change my mind:** A close above 109 clears the bounce high, though the average at 132.7 is far away. A close below 93.5 means new lows.

```json
{"92dfcbd8f0 (XRP)": 0.0, "aa7a8df9fc (DOGE)": 0.0, "ba12ba784e (BTC)": 0.0, "631f0fd964 (LINK)": 0.0, "75bb8fc285 (AVAX)": 0.0, "6adc7604e1 (LTC)": 0.0, "1b0ff0660e (ADA)": 0.0, "b4c7fae196 (ETH)": 0.0, "e1d49d54b0 (SOL)": 0.0, "01ec3750f9 (DOT)": 0.0}
```

## Entscheidung 2026-08-16

**1. Strategy**

I confirm a long signal when the price has a constructive base and a breakout. That means higher lows, a clean move above consolidation, and volume that expands on the up days. I veto a long signal when the move above the average is a weak, low-volume drift straight into nearby overhead supply. When the signal is 0, the weight must be 0. For those windows I only note the level that would flip the setup.

**2. Windows**

**61605a21da (SOL)**
- **Read:** A crash from about 110 to 83 around day -72 was followed by a recovery to 110. Since then the price has made lower highs and drifted between 97 and 104 on very light volume. The 20-week average at 106.2 sits overhead.
- **Weight:** 0. The signal is 0.
- **Change of mind:** A close above about 106.

**ee24dd01d9 (AVAX)**
- **Read:** This is a heavy downtrend from about 160. Two capitulation legs bottomed at 104 and then 93. Since then the price has been stuck in a range of roughly 98 to 108. Day -1's spike to 108.6 was rejected. The average at 122.6 is far above.
- **Weight:** 0. The signal is 0.
- **Change of mind:** Sustained trading above about 110, with the average needing to come down.

**9b53962550 (LINK)**
- **Read:**
  - The crash from about 110 to 78 was followed by a base around 75–78 between days -55 and -47.
  - Since then the price has made higher lows: 77, then 81, then 84–86.
  - A 85–90 consolidation broke out on day -5 at 93.5, with volume at 1.54.
  - Day -1 pushed to 100.9 (high 103.8) on volume of 1.66.
  - The close at 100 is well above the 92.9 average.
  - Overhead supply sits at roughly 100–104, from the day -90s distribution. The day -1 wick shows sellers there, but the base-and-breakout structure with rising volume is constructive.
- **Weight:** 1. Confirm.
- **Change of mind:** A close below about 92, which would mean a failed breakout and a move back under the average.

**a249a97adc (LTC)**
- **Read:** After the crash low near 89, the price recovered to 108. It has since faded steadily to about 100 on low volume. The average at 111.8 is overhead.
- **Weight:** 0. The signal is 0.
- **Change of mind:** A close above about 109.

**e0d58e43eb (BTC)**
- **Read:** After the low of 92.4, the price has been in a tight range of 99 to 106 that is now compressing near its bottom. The average at 109.9 is overhead.
- **Weight:** 0. The signal is 0.
- **Change of mind:** A close above about 107.

**851ae8112f (ETH)**
- **Read:** After the low of 80.6, the price recovered to about 104. It has been sideways between 98 and 104 with volume drying up. The average at 105.7 is just overhead.
- **Weight:** 0. The signal is 0.
- **Change of mind:** A close above about 106.

**78cc45113b (DOGE)**
- **Read:** The price fell from a peak near 170 through a crash to 100. It is now flat between 99 and 106 on very low volume. The average at 125.3 is far above.
- **Weight:** 0. The signal is 0.
- **Change of mind:** A move above about 112, plus an average that catches down.

**cf4f1471aa (XRP)**
- **Read:** This is a persistent downtrend with lower highs: 130, then 119, then 117, then 112. The price is grinding lower toward 100. The average is at 123.3.
- **Weight:** 0. The signal is 0.
- **Change of mind:** A close above about 112.

**3bddeb4c4f (ADA)**
- **Read:** The crash bottomed at 79. A rally to 121 on day -10 was fully reversed, falling back to 100. That failed rally is bearish. The average is at 118.2.
- **Weight:** 0. The signal is 0.
- **Change of mind:** A reclaim of about 115.

**a9c6319d13 (DOT)**
- **Read:** This is a long decline from about 220, with lower highs. The rally to 114.6 on day -12 failed, and the price is now at 100. The average is at 136.4.
- **Weight:** 0. The signal is 0.
- **Change of mind:** A close above about 117.

**3. Weights**

{"61605a21da (SOL)": 0.0, "ee24dd01d9 (AVAX)": 0.0, "9b53962550 (LINK)": 1.0, "a249a97adc (LTC)": 0.0, "e0d58e43eb (BTC)": 0.0, "851ae8112f (ETH)": 0.0, "78cc45113b (DOGE)": 0.0, "cf4f1471aa (XRP)": 0.0, "3bddeb4c4f (ADA)": 0.0, "a9c6319d13 (DOT)": 0.0}

## Entscheidung 2026-08-23

# T-001 Veto Review

## 1. Strategy

All ten windows show the same setup. A long decline or base is followed by a sharp 4-day thrust of about +20–50% that lifts the close to 100 and above the 20-week average.

I confirm the signal when the thrust has cleared the pre-crash range highs and is holding there without a climactic rejection. I veto when price is still inside or below heavy overhead supply from the old range. I also veto when the thrust ended in a blow-off: a long upper wick on day -1 on the window's peak volume. If the signal is 0, the weight is 0.

## 2. Windows

### a6915c7c58 (ETH)
- **Read:** The pre-crash range was 86–98, topping near 98–100 around day -128. After the crash, price based at 76–78 for weeks, then broke out from 78 to 102.1. It held well: day -1 had only a modest wick (high 102.7, close 98.3), and day 0 closed at 100 on falling volume. Price now sits above the old range top, around 96–98.
- **Weight: 1, confirm.** This is a clean breakout over prior resistance with an orderly pullback.
- **Change my mind:** a close below 91, which would fill the breakout gap.

### 073170a6a7 (SOL)
- **Read:** The old range was 86–97, with a single peak at 102–103 around day -104. Price based at 76–80, then thrust up. Day -1 was a rejection candle: high 107.7, low 91.9, close 98.3, on the window's top volume (2.83). Price is now pinned at the old 100–103 ceiling.
- **Weight: 0, veto.** This looks like a climactic wick into resistance.
- **Change my mind:** a close above 103.

### 0797e1bb38 (DOGE)
- **Read:** The old range was 105–123. Price crashed to 87 and based at 74–77. The current 100 is still below the 105–120 supply zone. Day -1 spiked to 107.9 and closed at 98.4 on volume of 3.46, the window peak.
- **Weight: 0, veto.** Price is under heavy overhead supply after a blow-off wick.
- **Change my mind:** a close above 108.

### f9b61adbe7 (LINK)
- **Read:** The old range was 75–93, peaking at 94.2. The base had been making higher lows since day -59, and pre-breakout momentum was already building, with 76 then 82 at days -12 and -8. Price thrust to 103.9, wicked to 109.3 on day -1, and held near 100–101. It is now above all of the prior structure.
- **Weight: 1, confirm.**
- **Change my mind:** a close below 92, back inside the old range.

### b7b5e3d9bd (LTC)
- **Read:** The old range was 100–116. After the crash to 79, price recovered gradually to 85–91. The thrust to 101.7, followed by a day -1 wick to 106.1 on volume of 3.21, failed right at the bottom of the old supply zone. Price at 100 sits in the middle of the former congestion.
- **Weight: 0, veto.**
- **Change my mind:** a close above 106.

### d053ce1518 (BTC)
- **Read:** The old range was 95–106. Price based at 80–84, then made a steady thrust to 100.8. There was no rejection afterward: day -1 traded 98.4–101.4 and day 0 closed at 100, with volume tapering to 0.87. This is orderly absorption at the lower edge of the old range, where the next resistance is 105–106.
- **Weight: 1, confirm.** Holding without rejection is constructive.
- **Change my mind:** a close below 93.

### 603397e0aa (AVAX)
- **Read:** Price is below the 20-week average at 101.1. Day -1 left a long wick to 109.3.
- **Weight: 0**, as the rule requires.
- **Would revisit:** a close above 104.

### 85b68dbe62 (DOT)
- **Read:** This is a long downtrend from 179 to 81, and price is still below the 20-week average at 109.8.
- **Weight: 0**, as the rule requires.
- **Would revisit:** a close above 112.

### f6677d5851 (XRP)
- **Read:** Price fell steadily to 65, then went parabolic, up 52% in 4 days. Day -1 printed volume of 5.98 with a wick to 111.8 and a close of 96.2, which is classic climactic exhaustion. The old range at 86–97 also caps price.
- **Weight: 0, veto.**
- **Change my mind:** a close above 103.

### 40aeb653eb (ADA)
- **Read:** The old range was 104–124 before a crash to 61. This is the third spike attempt:
  - days -51/-50 reached 88 and then faded to 69;
  - day -17 reached 93 and then faded to 77;
  - day -1 reached 113.8 and closed at 99.6 on volume of 3.0.

  This is a pattern of repeated failed thrusts below old supply at 104–110.
- **Weight: 0, veto.**
- **Change my mind:** a close above 105.

## 3. Weights

{"a6915c7c58 (ETH)": 1.0, "073170a6a7 (SOL)": 0.0, "0797e1bb38 (DOGE)": 0.0, "f9b61adbe7 (LINK)": 1.0, "b7b5e3d9bd (LTC)": 0.0, "d053ce1518 (BTC)": 1.0, "603397e0aa (AVAX)": 0.0, "85b68dbe62 (DOT)": 0.0, "f6677d5851 (XRP)": 0.0, "40aeb653eb (ADA)": 0.0}

## Entscheidung 2026-08-30

# Analysis

## Strategy
Every window has the same shape: a sharp drop around day -88, a base, then a strong surge around days -11 to -9, and a pullback to 100 today. When the signal is 1, I confirm it if the surge broke out of the base, the base was building higher lows, and price has held most of the surge on calm volume. I veto it if the surge came at the end of a series of lower highs and lower lows, and looks like a blow-off: an extreme volume spike, a long upper wick and a fast give-back of the gain. When the signal is 0, the weight is 0.

## a3aef04b67 (ADA)
- **Read:** Long-term downtrend. Price went from about 140 down to a crash low near 72, and later bases sat at 85 to 90. The spike reached 134 but closed 117 on day -8, and price has faded to 100, below the 20-week average of 105.5. Support is 90; resistance is 105 to 118.
- **Weight:** 0, because the signal is 0.
- **Change of mind:** A close above 106 would turn the rule invested.

## 03604ade44 (LINK)
- **Read:** The old range was 82 to 96. After the crash low of 63, the base built steady higher lows: 65, 70, 73, then 77 and 85 before the spike. The breakout cleared both the 86 base ceiling and the old 96 to 97 highs. Price has held between 100 and 107 for 9 sessions while volume faded, which looks like digestion rather than distribution. The 20-week average is 80.6.
- **Weight:** 1 (confirm).
- **Change of mind:** A close below 94 would mean the price is back inside the old range.

## 91bc7bc810 (LTC)
- **Read:** The old range was 108 to 126, and the crash low was 84. The recovery stalled at 98 to 100 and then drifted down to 92. The spike to 116 has faded back to 100, below the 20-week average of 102.2. Resistance is 100 to 103 and support is 92.
- **Weight:** 0, because the signal is 0.
- **Change of mind:** A close above 103.

## f91218451f (XRP)
- **Read:** Before the spike, the structure was clearly bearish. Highs fell from 109 (day -108) to 87, 84, 80 and 74, and lows fell to 73. The spike from 73 to 125 came on 4 to 6 times normal volume and left a huge upper wick: day -8 hit 125 but closed 107.7. Since then price has kept giving back the gain (112, 106, 102, 100), with each lower high below the last. This looks like a news-driven blow-off, not a base breakout. Price also sits below the old 102 to 109 range, which now acts as resistance.
- **Weight:** 0 (veto).
- **Change of mind:** A close above 108 would reclaim the post-spike highs and the old range.

## a83df63b5c (ETH)
- **Read:** The old range was 83 to 100, and the crash low was 62. The base made steady higher lows (63, 70, 73, 76), then compressed tightly at 77 to 79 on very low volume. The breakout from 79 to 104 was decisive. Price has held at 100 to 104 for 8 sessions, right at the old 98 to 100 ceiling, which looks like a retest of that ceiling from above. The 20-week average is 83.2.
- **Weight:** 1 (confirm).
- **Change of mind:** A close below 96.

## f9003aad94 (SOL)
- **Read:** The old range was 80 to 96, and the crash low was 59. Price rallied to 81, then based at 71 to 76. The breakout from 76 kept making higher highs after the spike (92, 97, 100, then 107 on day -3). Today's 100 is a pullback inside a rising sequence and sits above the old range highs. The 20-week average is 79.5.
- **Weight:** 1 (confirm).
- **Change of mind:** A close below 93 would break the post-spike higher lows.

## 14e368e487 (DOGE)
- **Read:** Price peaked near 140 and has trended down since, with the base sitting at 84 to 86. The spike reached 123 but closed 112, and price has faded to 100, below the 20-week average of 105.8.
- **Weight:** 0, because the signal is 0.
- **Change of mind:** A close above 106.

## 55fc213ccf (AVAX)
- **Read:** Downtrend from 147. The base sat at 88 to 95, and the spike to 117 faded to 100, below the 20-week average of 106.8. Support is 89 and resistance is 107 to 110.
- **Weight:** 0, because the signal is 0.
- **Change of mind:** A close above 107.

## cac187bef3 (DOT)
- **Read:** Steep long-term downtrend, from 200 down to a low of 91. The spike to 126 has faded to 100, well below the 20-week average of 122.0.
- **Weight:** 0, because the signal is 0.
- **Change of mind:** A close above 122.

## f3ecd96b61 (BTC)
- **Read:** The old high was 106, and the crash low was 76. Price recovered to 86, then based at 80 to 84 with flat lows. The breakout from 83 to 100 was orderly and not a blow-off: no extreme wick, and volume peaked at 2.6. Price has held a tight 99 to 104 range for 9 sessions, with volume drying up today (0.53). The 20-week average is 90.0. The old 100 to 106 zone is overhead, but the consolidation is constructive.
- **Weight:** 1 (confirm).
- **Change of mind:** A close below 96 would mean the consolidation has failed.

{"a3aef04b67 (ADA)": 0.0, "03604ade44 (LINK)": 1.0, "91bc7bc810 (LTC)": 0.0, "f91218451f (XRP)": 0.0, "a83df63b5c (ETH)": 1.0, "f9003aad94 (SOL)": 1.0, "14e368e487 (DOGE)": 0.0, "55fc213ccf (AVAX)": 0.0, "cac187bef3 (DOT)": 0.0, "f3ecd96b61 (BTC)": 1.0}

## Entscheidung 2026-09-06

## Strategy
I confirm the signal when the post-spike consolidation is constructive: closes at or near the post-spike highs, rising lows, and preferably little overhead supply from the pre-crash range. I veto when the spike was sharply rejected and the market has since made lower highs while sitting inside heavy prior supply. If the signal is 0, the weight is always 0.

## cae6463e99 (ADA)
- **Read:** Price fell from the 105–130 range to 64 and based there. A spike at day -15 reached 115.7 but was rejected. Since then the market has held 85–102, with lows rising (84.8 → 85.9 → 93.6 → 96.4) under a flat top at about 101–103. That is an ascending-triangle shape. Overhead supply sits at 105–112.
- **Weight:** 1. The base is constructive and the close is near the post-spike high.
- **Change my mind:** a close below 93.

## dbb10310d4 (LINK)
- **Read:** Today closed at 100, a new window high that clears the 92.5 cap of the consolidation on 1.7x volume. The prior range was 64–80, so there is no overhead supply. Clean trend.
- **Weight:** 1.
- **Change my mind:** a close below 87.

## 34dadc940a (LTC)
- **Read:** Since the spike, lows have risen steadily (86.2 → 87.9 → 90.6 → 92.3 → 97.2). The day -1 thrust came on 2.3x volume and price is now testing 100.9, the spike high. Pre-crash supply sits at 103–110, though the structure is strong.
- **Weight:** 1.
- **Change my mind:** a close below 92.

## 42676ce049 (XRP)
- **Read:** The spike was a blow-off at 6x volume to 119.4, with a long upper wick. Since then highs have kept falling (108.9 → 104.2 → 100.6) while lows sit at 92–94. Volume today is fading (0.73). Price sits back inside the old 92–104 pre-crash range, which acts as supply. Momentum is fading.
- **Weight:** 0 (veto).
- **Change my mind:** a close above 105.

## eea2843985 (SOL)
- **Read:** Price is above the entire pre-crash range (77–91). After a higher high at 103.8 (day -10), it is holding 92–100. This is a breakout and hold.
- **Weight:** 1.
- **Change my mind:** a close below 91.

## 96e3c9e4a8 (BTC)
- **Read:** A tight, low-volume consolidation between 95 and 101.4 is sitting under the prior peak at 102–103, with rising lows. A clean base.
- **Weight:** 1.
- **Change my mind:** a close below 94.5.

## 303a13215c (DOGE)
- **Read:** The spike to 110.9 was rejected, and day -1 was rejected again at 104.7. The highs have been choppy and falling, and lows sit at 88–92. Heavy supply sits at 100–127 from a long downtrend.
- **Weight:** 0 (veto).
- **Change my mind:** a close above 105.

## ac60ea41c8 (DOT)
- **Read:** The signal is 0. Price is in a long downtrend from 167, though today's rally to 101.3 on 1.67x volume is notable.
- **Weight:** 0 (forced by the rule).
- **Change my mind:** n/a; the rule would flip to invested on a close above about 101.

## c4d63510a0 (AVAX)
- **Read:** The spike to 105.2 was rejected, but lows have risen since (88.7 → 89.0 → 91.9 → 93.3 → 95.2). Today's close of 100 is the best close since the spike. Supply sits at 103–113.
- **Weight:** 1.
- **Change my mind:** a close below 91.

## ce17f071e3 (ETH)
- **Read:** Price has cleared the pre-crash high of about 98 and has held a tight 94–101 range for two weeks. Constructive.
- **Weight:** 1.
- **Change my mind:** a close below 93.5.

{"cae6463e99 (ADA)": 1.0, "dbb10310d4 (LINK)": 1.0, "34dadc940a (LTC)": 1.0, "42676ce049 (XRP)": 0.0, "eea2843985 (SOL)": 1.0, "96e3c9e4a8 (BTC)": 1.0, "303a13215c (DOGE)": 0.0, "ac60ea41c8 (DOT)": 0.0, "c4d63510a0 (AVAX)": 1.0, "ce17f071e3 (ETH)": 1.0}

## Entscheidung 2026-09-13

**Strategy:** I confirm a 1 signal when price has broken out of its prior base and is holding that breakout. That means higher lows, or a defended range well above the old base. I veto when the close sits only marginally above the 20-week average right after a failed blow-off spike with exhaustion volume and consecutive lower lows, since that looks like a move unwinding back into the average. A 0 signal is always 0.

## ac827536d8 (ADA)
- **Read:** The base after the crash ran 70–90. The −23/−22 breakout on heavy volume spiked to 127 and closed 111. Since then price has ranged 94.7–114 for about 25 days. Highs are lower (127 → 114 → 106), but the lows held at 94.7 and then 98.5. The close of 100 is only 1.7% above the average at 98.3, so the margin is thin.
- **Weight: 1.** The breakout from the 85–90 base is intact and the retests have held. This is range consolidation, not a breakdown.
- **Change my mind:** a close below 94.

## 632ac3d7e3 (LTC)
- **Read:** The 81–89 base broke out at −23 to about 100. The pullback held 89.2, and a later push printed a 110.6 wick. Lows are rising (89.2 → 96.0 → 96.6), with the close of 100 about 10% above the average at 91.0.
- **Weight: 1.** The trend structure is clean with higher lows.
- **Change my mind:** a close below 96.

## d0c604ecb1 (ETH)
- **Read:** A tight 75–78 base gapped up on volume to 91–101. Price has since consolidated in a narrow 95–103 band for about 25 days, and the close of 100 is 22% above the average at 81.9.
- **Weight: 1.** This is a strong breakout with orderly digestion.
- **Change my mind:** a close below 95.

## cc0f028dca (XRP)
- **Read:** A 74–75 base produced a climactic spike to 126.7 on about 6× volume. Price then settled into 98–110. Highs are falling (115.6, 110.6, 108.2), but support at 97.7–99.1 has held four times, and the close of 100 is about 9% above the average at 92.
- **Weight: 1.** Price is still far above both the base and the average, and support is flat. The pattern is a triangle, not a reversal yet.
- **Change my mind:** a close below 97.5.

## cf866d6b97 (DOGE)
- **Read:** The breakout from the 84–86 base faded. Highs are lower (122 → 115.5 → 111), and the close of 100 is below the average at 104.2.
- **Weight: 0.** The signal is 0.
- **Change my mind:** n/a, but a close above 104–105 would flip the rule.

## 857ff0adbf (BTC)
- **Read:** The 82–85 base broke out to 100–107. Price has held a 99–106 range for over 20 days, and the close of 100 is about 9.5% above the average at 91.3.
- **Weight: 1.** The breakout is holding well above the base.
- **Change my mind:** a close below 98.5.

## 8acc34c10d (AVAX)
- **Read:** The breakout from the 85–90 range peaked near 112 and is fading. The close of 100 is below the average at 101.9.
- **Weight: 0.** The signal is 0.
- **Change my mind:** n/a, but a close above 102 would flip the rule.

## 53118ae52e (LINK)
- **Read:** A rising base from 72 to 85 broke out to 107–112. The pullback held at 97.4. A spike to 122 at −6 retraced, but the lows held at 98–100. The close of 100 is 21% above the average at 82.8.
- **Weight: 1.** The higher-low structure remains and price is far above the average.
- **Change my mind:** a close below 97.

## d30c72eedf (DOT)
- **Read:** A long downtrend ran from 160 to 76. The −22 spike to 103 failed back to 81. The latest leg blew off to 128.5 on about 4× volume and reversed immediately, with five straight lower lows (109 → 107 → 103 → 101 → 99.6). Price has given back nearly the entire blow-off, and the close of 100 is only 2.7% above the average at 97.4. Below that, the pre-spike area is 90–92.
- **Weight: 0 (veto).** This is an exhaustion spike that is unwinding toward the average. I judge it a false signal.
- **Change my mind:** a close back above 106–107 while holding 99.6.

## 141c5d4554 (SOL)
- **Read:** The 72–78 base broke out to 88–111. Lows are rising (88.3 → 93.9 → 98.1/98.7/99.9), and the close of 100 is 20% above the average at 83.3.
- **Weight: 1.** The uptrend structure is intact.
- **Change my mind:** a close below 98.

{"ac827536d8 (ADA)": 1.0, "632ac3d7e3 (LTC)": 1.0, "d0c604ecb1 (ETH)": 1.0, "cc0f028dca (XRP)": 1.0, "cf866d6b97 (DOGE)": 0.0, "857ff0adbf (BTC)": 1.0, "8acc34c10d (AVAX)": 0.0, "53118ae52e (LINK)": 1.0, "d30c72eedf (DOT)": 0.0, "141c5d4554 (SOL)": 1.0}

## Entscheidung 2026-09-20

**Strategy:** I confirm the signal when price is building constructive structure: higher lows, a hold above a breakout zone, and a close at or above the top of its recent range. I veto when the asset is chopping inside a range with lower highs under heavy overhead supply, or when it sits barely above the average with nothing behind it. Each window is judged only on its own structure.

### 7e35b6a640 (ADA)
- **Read:** The price crashed from about 110 to 63 (day -107 to -87) and has recovered since with higher lows at 63, 68, 76, 84 and 85. The day -29 spike to 113 faded into an 84–99 range. The last two sessions pushed back to 100, which is the top of that range and the bottom of the pre-crash 100–110 supply. The 20-week average is 87.3.
- **Weight 1:** The trend is up and the higher-low sequence is intact. The breakout to 100 came on above-average volume.
- **Change my mind:** a close below 85.

### e546520bfe (BTC)
- **Read:** The price crashed to 73 and then spent months in a 73–80 base. It gapped to about 96 at day -30 and consolidated at 93–100 for a month. It now closes at 100, the top of that consolidation, just under the window high of about 102.
- **Weight 1:** This is a tight, orderly flag above a long base, a textbook continuation.
- **Change my mind:** a close below 92.5.

### 1918a25ea7 (SOL)
- **Read:** The price crashed from 74 to 54 and based at 64–70. It broke out at day -32 and climbed to 98, then held 87–99. It now closes at 100, above every pre-crash high in the window (the highest was 88.5).
- **Weight 1:** The price is at new window highs with a well-defined support zone underneath. The structure is strong.
- **Change my mind:** a close below 86.

### 967a31b537 (DOT)
- **Read:** The price fell from about 120 to 63 and is recovering with higher lows at 63.7, 71 and 82. A blow-off at day -12 (high 113) reversed to 83, and the price has rebounded to 100 on heavy volume. Overhead supply sits at 103–113. The price is volatile, and the day 0 range ran from 94 to 103.
- **Weight 1:** The higher lows and strong demand on the rebound outweigh the overhead supply. It is the riskiest confirm in this set.
- **Change my mind:** a close below 88.

### d06457ca16 (ETH)
- **Read:** The price gapped at day -32 from 72 to 85 and then consolidated at 89–96 for a month. It now closes at 100, above that consolidation and above all prior window highs (93 at day -156).
- **Weight 1:** This is a clean breakout from a flag that followed a long base.
- **Change my mind:** a close below 89.

### 8cdfd9c034 (LINK)
- **Read:** The price based at 57–67 after a crash and broke out at day -32. It spiked to 109 at day -13, pulled back to 85, and has now recovered to 100. The pre-crash highs were about 87, so the price is well above them. The lows are rising at 85 and 87.
- **Weight 1:** The trend is up and the pullback was absorbed above the old highs.
- **Change my mind:** a close below 84.5.

### e9914f4232 (DOGE)
- **Read:** The pre-crash range was 115–135. After the crash the price drifted down to 79–84, then spiked to 115.5 at day -29. Since then the highs have been lower: 109, 105.4 and 104.6. The price has chopped between 90 and 105 and now sits at 100, only 3% above the 97.2 average, with heavy supply overhead.
- **Weight 0 (veto):** The signal is marginal, with lower highs inside a range and well below the prior distribution zone.
- **Change my mind:** a close above 105.5.

### de3861d60e (AVAX)
- **Read:** The price based at 55–60 for about three months, and an earlier spike at day -29 (to 73.5) faded. Then came a two-day surge from 72 to 100 on 3.9x and 6.1x volume. Day 0 closed at its high, above all window prices including the pre-crash 85–92 zone. The price is extremely extended, about 50% above the 66.7 average.
- **Weight 1:** A new window high on enormous volume, closing at the top of the bar, is a genuine regime break and not a weak signal. Expect volatility.
- **Change my mind:** a close below 83, the day 0 low.

### 9e1558a6ef (LTC)
- **Read:** The price crashed from about 89 to 67 and has recovered with higher lows at 67, 74, 81 and 85.5. The day -13 test of 101 was rejected, but the price is back at 100. The pre-crash range was 88–103.
- **Weight 1:** The price is retesting the range top with rising lows underneath, so a breakout is likely.
- **Change my mind:** a close below 85.5.

### de24faa46f (XRP)
- **Read:** The price spiked from 71 to 120.5 at day -29 on extreme volume. Since then the highs keep falling: 120.5, 109.9, 105.2, 106.1 and 103.1. The swings are wide, including a 106-to-89.7 drop on days -6/-5. The price now sits mid-range at 100 inside 89–106, and the heavy volume on down days suggests distribution.
- **Weight 0 (veto):** This looks like distribution after a blow-off, with no higher-high structure.
- **Change my mind:** a close above 106.5.

{"7e35b6a640 (ADA)": 1.0, "e546520bfe (BTC)": 1.0, "1918a25ea7 (SOL)": 1.0, "967a31b537 (DOT)": 1.0, "d06457ca16 (ETH)": 1.0, "8cdfd9c034 (LINK)": 1.0, "e9914f4232 (DOGE)": 0.0, "de3861d60e (AVAX)": 1.0, "9e1558a6ef (LTC)": 1.0, "de24faa46f (XRP)": 0.0}

## Entscheidung 2026-09-27

## Strategy

I confirm the signal when the recovery above the 20-week average has cleared the pre-crash range, so that no old supply sits overhead, and is printing higher lows on supportive volume. I veto when price is still pushing into the pre-crash distribution zone after repeated spike-and-fade failures in that area, because a trend-filter long there is likely buying into overhead supply. Each window gets an invalidation level near the most recent higher low or failed-breakout level.

---

### 50d7768fba (XRP)
- **Market read:** The pre-crash range was 87–97, with a wick high of 102.2. Price crashed to 65 and based there for about 75 days. A volume blow-off at -36 reached a high of 112.1, then price chopped between 84 and 101.
- **Structure now:** The lows are rising (84.6 → 85.5 → 97.5 → 99.1), and closes are holding at 99–104, above the old 97 ceiling. Volume is heavy and the bars are wide. There is resistance at 106–112, but the old range is now support.
- **Weight:** 1 (confirm). Price is through the pre-crash highs and the lows keep rising.
- **Changes my mind:** a close below 92.

### 47480a35e9 (ETH)
- **Market read:** The pre-crash high was 91.7. After a base near 70, price gapped up at -39 and spent a month in a tight 88–95 flag. It broke out at -9 to 103–104 and now sits in a calm 99–101 range on low volume, which reads as orderly digestion above the old high.
- **Weight:** 1 (confirm). This is a clean base, flag and breakout.
- **Changes my mind:** a close below 96.

### a1fc393c28 (DOT)
- **Market read:** The pre-crash range was 95–113, with closes of 104–109 between -145 and -136. Price crashed to 57.
- **Failed spikes:** The rally at -37/-36 hit 81 and faded to 64. A second spike at -19 printed 101.3 and collapsed to 74.5 within a week.
- **Now:** Price is back at 100, with violent daily swings (-4 reached 96.7 and closed 86.9). It is directly beneath the failed 101 level and the 104–113 supply.
- **Weight:** 0 (veto). Price is retesting a failure point under heavy overhead supply, with erratic structure.
- **Changes my mind:** a close above 104.

### 55e80cc983 (LINK)
- **Market read:** The pre-crash high was 77.5, so price is now about 25% above any prior trading. Higher highs run 94.4 → 101.4 → 103.4, and higher lows run 77.6 → 88.1 → 99.2. Volume expands on up legs.
- **Weight:** 1 (confirm). This is a clean uptrend in price discovery.
- **Changes my mind:** a close below 93.

### 0c493f4a3c (SOL)
- **Market read:** The pre-crash high was 80.7. Price has made a steady staircase from the 61 base: 90 → 97.5 → 100.8. Higher lows run 79.4 → 92.2 → 98.5. Price is at new highs and volume is moderate.
- **Weight:** 1 (confirm).
- **Changes my mind:** a close below 94.

### 5f750ee947 (ADA)
- **Market read:** The pre-crash range was 92–113, with closes above 100 between -145 and -136. Price crashed to 54.
- **Pattern:** Rallies have repeatedly spiked and faded: 78 → 61 at -85, 83 → 68 at -52, and 101.3 → 75 at -36.
- **Now:** Price is testing 101–104 again. The -4 and -1 bars show highs of 102.8 and 104.0 but closes of 93.5 and 99.6, which is rejection at the bottom of the old supply zone. Higher lows (75.7 → 91.5) are the only positive.
- **Weight:** 0 (veto). The asset has a history of failing at exactly this zone.
- **Changes my mind:** a close above 105.

### 1694551aed (AVAX)
- **Market read:** The pre-crash range was 80–96, with a high of 96.2. Price based at 57–62 for months. A two-day event gap from 69.8 to 103.7 came on 5.7x volume.
- **Since the gap:** For eight days price has held 92–108, with higher lows (91.4 at -3, then 97.8 at day 0). It is above the pre-crash highs. Gaps that hold like this tend to drift higher.
- **Weight:** 1 (confirm).
- **Changes my mind:** a close below 91. That would start filling the gap, with risk toward 75.

### 154895ab02 (BTC)
- **Market read:** The pre-crash high was 98.1. Price broke above it at -6 (102.5) and has since consolidated tightly at 99.6–100.9 on low volume (0.5–0.6x). This is a quiet retest of the old high as support.
- **Weight:** 1 (confirm).
- **Changes my mind:** a close below 97.

### 015e3ebaf4 (DOGE)
- **Market read:** The pre-crash range was 95–122, with closes of 105–119 between -151 and -118, which is a heavy supply zone.
- **Failed spikes:** At -36, price spiked to 104 and faded to 82.6. At -6/-5 it reached 105–109, but -4 reversed hard to 95.7.
- **Now:** Price is at 100, just under 103–119 supply, after a rejection.
- **Weight:** 0 (veto). It is rejected at the base of the old range and the spikes keep failing.
- **Changes my mind:** a close above 108.

### b090113454 (LTC)
- **Market read:** The pre-crash high was 85.0. Price climbed steadily from a 62 base through 75 and 82 to 88, then gapped at -3 on 6.7x volume to 100.9. It has held 96.7–105 for three days since. Price is well above all prior history and the lows are rising.
- **Weight:** 1 (confirm).
- **Changes my mind:** a close below 95.

{"50d7768fba (XRP)": 1.0, "47480a35e9 (ETH)": 1.0, "a1fc393c28 (DOT)": 0.0, "55e80cc983 (LINK)": 1.0, "0c493f4a3c (SOL)": 1.0, "5f750ee947 (ADA)": 0.0, "1694551aed (AVAX)": 1.0, "154895ab02 (BTC)": 1.0, "015e3ebaf4 (DOGE)": 0.0, "b090113454 (LTC)": 1.0}
