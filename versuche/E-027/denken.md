# E-027: was die KI gedacht hat (Set A)

Volle Antwort des Deciders pro Entscheidungswoche, unverändert. Er sah weder Datum noch Coin-Namen; die Namen in Klammern sind erst danach eingesetzt. Gesendeter Prompt und Daten: runs/<set>/<woche>/requests.json.

## Entscheidung 2026-07-05

**Strategy.** I weight each window by its own trend structure. The 180-day downtrend sets a low base weight. I add to it when the bounce off the recent lows has made higher lows or reclaimed the last bounce high, and I cut it when the last low undercut the post-crash low. The M2 line (+5% and accelerating for 4 months) is mildly supportive and the same for every window, so it nudges all weights slightly up but does not separate them.

**90c1c89fcd (BTC)**
- **Read:** Primary downtrend from about 147. It crashed to 92.9 (day -30), bounced to 105.7 (day -20), then made a slightly lower low at 90.8 (day -4). It is now 100, a weak rebound on low volume, and still below the 105–110 range.
- **Weight: 0.3.** The low was lower and the rebound has not yet reclaimed any resistance.
- **Change my mind:** a close above 105.7 means I add; a close below 90.8 means flat.

**8d80589cd8 (SOL)**
- **Read:** It crashed to 73.7 (day -29), then made higher lows at 78.5 (day -10) and 85.5. It broke above the 93.3 bounce high and traded up to 102.9. This is the clearest higher-low, higher-high recovery, though it is still far below the 105–120 range from before the crash.
- **Weight: 0.6.**
- **Change my mind:** below 92 cut; below 85 flat; above 103 add.

**4860e6955a (XRP)**
- **Read:** The low was 90.7 (day -29), and the retest at 87.2 (day -9) undercut it. It has bounced to 100 but is still below the 111.8 spike high from day -20.
- **Weight: 0.35.**
- **Change my mind:** above 107 add; below 87 flat.

**5f94d437ca (ETH)**
- **Read:** A double bottom at 84.3 and 84.7 (days -29 and -9). It is now 100, just under the 103.6 neckline.
- **Weight: 0.45.**
- **Change my mind:** a close above 103.6 means I add; below 84 flat.

**bb8cd5b309 (DOGE)**
- **Read:** It failed from the 152 rally and crashed to 99.7. It bounced to 118.7, then made a lower low at 89.3 (day -5). The sequence of lower highs and lower lows is intact.
- **Weight: 0.25.**
- **Change my mind:** above 108 add; below 89 flat.

**e72e6bf1e3 (LTC)**
- **Read:** Lows at 88.4 (day -29) and then 85.7 (day -10), which is lower. The steady recovery has brought it to 100, right at the 101.2 bounce high.
- **Weight: 0.35.**
- **Change my mind:** a close above 101.2 means I add; below 85.7 flat.

**d73af95893 (AVAX)**
- **Read:** A capitulation low at 82.0 (day -16, on 3× volume). Since then it has made higher lows near 86 and then 92, and it is now 100, testing 102.2. The structure is constructive.
- **Weight: 0.45.**
- **Change my mind:** above 102.8 add; below 91 cut.

**671ff362c4 (ADA)**
- **Read:** It made lower lows at 78.4 and then 72.9 (day -10). It then rose from 76 to 105.5 in four days on 2× volume, a high-volume V-reversal that cleared the 100.3 bounce high. A move that fast can retrace, and 120+ is still far above.
- **Weight: 0.5.**
- **Change my mind:** below 85 flat; holding above 97 with a push through 105.5 means I add.

**a67e086bf6 (DOT)**
- **Read:** It crashed to 100.3, bounced to 118.8 (lower than the earlier ~150 highs), then made a lower low at 90.2 (day -7). It is now 100, and the downtrend structure is intact.
- **Weight: 0.25.**
- **Change my mind:** above 111 add; below 90 flat.

**cf332e3a3d (LINK)**
- **Read:** A double bottom at 86.8 and 86.9 (days -29 and -10). It is now 100, below the 106.7 neckline.
- **Weight: 0.4.**
- **Change my mind:** above 106.7 add; below 86.8 flat.

{"90c1c89fcd (BTC)": 0.3, "8d80589cd8 (SOL)": 0.6, "4860e6955a (XRP)": 0.35, "5f94d437ca (ETH)": 0.45, "bb8cd5b309 (DOGE)": 0.25, "e72e6bf1e3 (LTC)": 0.35, "d73af95893 (AVAX)": 0.45, "671ff362c4 (ADA)": 0.5, "a67e086bf6 (DOT)": 0.25, "cf332e3a3d (LINK)": 0.4}

## Entscheidung 2026-07-12

**1. Strategy**

I follow the trend. Each asset gets a small weight while it is below its falling medium-term structure and making lower lows. I raise the weight only when there is a confirmed higher low and higher high. The M2 line (+5% and accelerating for 4 months) is a mild supportive backdrop, so I lift weights slightly but don't override price structure.

**2. Windows**

All ten windows have the same shape: a long decline from roughly 175–270 to 100, a capitulation leg from day -40 to -37, a retest around day -17, a bounce into day -9/-8, and a fade back to 100 now. What separates them is the retest structure.

**dbc84c8e73 (XRP)**
- **Read:** Down from about 200. The crash low was 96.7; the retest at 93.2 was a lower low. The bounce topped at 109.1 and price has faded to 100, below the roughly 112 average of the last 50 days.
- **Weight:** 0.15, because the downtrend is intact.
- **Change my mind:** a close above 109.5 (raise); a break below 93 confirms the downtrend.

**f029edb5e2 (SOL)**
- **Read:** The crash low was 78.2 and the retest held at 83.3, a higher low. The bounce to 109.2 cleared the post-crash high of 98.9, a higher high. Price is now pulling back to 100, near the 50-day mean of about 98.
- **Weight:** 0.4. This is the best-formed base of the ten.
- **Change my mind:** a close below 98 (cut); a close above 109.5 (add).

**6658df8adc (LINK)**
- **Read:** A double bottom at 87.5/87.7. The bounce reached 102.2 and the range is 87.5–107.5. Price is at 100, mid-range.
- **Weight:** 0.3, because the base is holding but there is no breakout yet.
- **Change my mind:** above 107.5 (add); below 87.5 (exit).

**cc85cdf6f1 (BTC)**
- **Read:** The crash low was 92.7 and the retest at 91.1 was slightly lower. The bounce capped at 101.4, below the earlier high of 105.5. The 50-day mean is about 105.
- **Weight:** 0.2.
- **Change my mind:** above 105.5 (raise); below 91 (cut).

**b595a8806b (DOT)**
- **Read:** Down from about 270, a persistent decline. Lows stepped down from 104.7 to 95.3 to 94.2. The bounce to 107.6 failed back to 100.
- **Weight:** 0.1.
- **Change my mind:** above 108 (raise); below 94 (stay minimal).

**ad50fdfe94 (DOGE)**
- **Read:** The crash low was 106.8, then a lower low at 95.6. The bounce to 109.2 is below the post-crash high of 127.2. Lower highs and lower lows.
- **Weight:** 0.1.
- **Change my mind:** above 110 (raise); below 95.5 (stay minimal).

**5bb7dd67df (AVAX)**
- **Read:** The crash low was 97.1, then a lower low at 88.7. The bounce to 111.1 is fading, and today's bar has a red body with a low of 98.
- **Weight:** 0.15.
- **Change my mind:** above 111 (raise); below 93 (cut).

**cb1a834d0e (LTC)**
- **Read:** The crash low was 92.1 and the retest at 89.3 was lower. The bounce to 104.9 sits below the 50-day mean of about 108. Price is at 100.
- **Weight:** 0.15.
- **Change my mind:** above 105 (raise); below 89 (cut).

**6920588057 (ADA)**
- **Read:** The crash low was 91.7, then a lower low at 85.3. A volume spike to 123.4 was fully rejected and price has bled back to 100, so there is a blow-off and fade.
- **Weight:** 0.15.
- **Change my mind:** above 118 (raise); below 88 (cut).

**d80a9916b3 (ETH)**
- **Read:** A double bottom at 83.3/83.7 (higher low). The bounce to 101.5 is just under the prior high of 102.4. Price is at 100.
- **Weight:** 0.3, as a base forming.
- **Change my mind:** above 102.5 (add); below 86 (cut).

**3. Weights**

{"dbc84c8e73 (XRP)": 0.15, "f029edb5e2 (SOL)": 0.4, "6658df8adc (LINK)": 0.3, "cc85cdf6f1 (BTC)": 0.2, "b595a8806b (DOT)": 0.1, "ad50fdfe94 (DOGE)": 0.1, "5bb7dd67df (AVAX)": 0.15, "cb1a834d0e (LTC)": 0.15, "6920588057 (ADA)": 0.15, "d80a9916b3 (ETH)": 0.3}

## Entscheidung 2026-07-19

**Strategy:** In every window I weigh the long-term trend (where price sits against its 180-day path and the lower-highs structure) against the short-term base (whether recent swing lows are holding and rising). A long-term downtrend caps the weight near 0.5. A higher-low base with price above roughly 1-month support earns 0.4–0.6. Lower highs that are sliding toward support get 0.25–0.35. The M2 line (+5% year-on-year, 3-month growth rising for 4 months) is a mild tailwind in every window but does not override price.

**78aa2e89e5 (LINK)**
- **Read:** The longer trend is down, from about 148 to 100, with a lower high at 129 (day -70). Lows at 83.4 (day -43) and 83.6 (day -24) form a double bottom. Price has recovered to 100, just under resistance at 102–103, on fading volume.
- **Weight:** 0.5. The base is constructive, but the higher timeframe is still bearish.
- **Change my mind:** a close below 93.

**9ec2d724dd (ETH)**
- **Read:** The pattern is similar. Lows at 80.4 and 81.9 form a base, followed by a steady climb to 100 and a test of 103–104 resistance. The 150-day downtrend from about 131 has not been reclaimed.
- **Weight:** 0.5.
- **Change my mind:** a close below 93.

**ae4cdef1af (BTC)**
- **Read:** The lows are shallower, at 91.4 and 89.8. Price is grinding back to 100, which is a tight range, with resistance at 102–104 (day -34). The decline from 127 is intact on the bigger picture.
- **Weight:** 0.45. The base is stable, but price has not broken out.
- **Change my mind:** a close below 95.

**dbef858add (AVAX)**
- **Read:** There was a capitulation low at 87.9 (day -30), then a bounce to 110 (day -15). Since then highs have been lower, at 105 and 104.8, and price is drifting to 100 inside a 97–110 range.
- **Weight:** 0.35. Momentum after the bounce is fading.
- **Change my mind:** a close below 97.

**5eb71e2197 (SOL)**
- **Read:** The 78.7 low was followed by a higher low at 83.8 and a strong rally to 110 (day -15). Price has pulled back to 100 and is holding the 96–98 area.
- **Weight:** 0.5. The recovery structure is decent, and this looks like a pullback within it.
- **Change my mind:** a close below 96.

**07984cc4ca (DOGE)**
- **Read:** There is a persistent series of lower highs from 163 (day -66) to 109 (day -15). The low is 96 (day -19), and price is coiling around 100.
- **Weight:** 0.3. The trend is down, and the only thing in favour is that support is holding.
- **Change my mind:** a close below 97.

**0c47689b33 (LTC)**
- **Read:** The lows are rising: 83.5 (day -25), 91.2 (day -6), 93.7 (day -2). On day -1 price pushed to 101.7 on above-average volume, the best breakout attempt of the set. Resistance from the day -34 high is at 98.
- **Weight:** 0.6.
- **Change my mind:** a close below 92.

**2b5c809aa6 (ADA)**
- **Read:** This window had a severe drop from 140 to 89 (day -44) and a retest at 83.1 (day -24). A spike to 120 (day -15) was fully retraced. Price is now in a 93–102 range.
- **Weight:** 0.4. The failed breakout is a warning, but the base is holding.
- **Change my mind:** a close below 93.

**b57893febd (XRP)**
- **Read:** The lows are 95.7 and 91.9. A rally to 107.9 (day -15) has been retraced to 100. Support is at 96–97 and resistance at 103–108.
- **Weight:** 0.4.
- **Change my mind:** a close below 96.

**9291e9ccd8 (DOT)**
- **Read:** The downtrend from 168 is intact. The low is 97 (day -21), then a bounce to 110. On day 0 price fell from 102.3 to 100, near the day's low, on rising volume, so it is pressing support.
- **Weight:** 0.25.
- **Change my mind:** a close below 97.

{"78aa2e89e5 (LINK)": 0.5, "9ec2d724dd (ETH)": 0.5, "ae4cdef1af (BTC)": 0.45, "dbef858add (AVAX)": 0.35, "5eb71e2197 (SOL)": 0.5, "07984cc4ca (DOGE)": 0.3, "0c47689b33 (LTC)": 0.6, "2b5c809aa6 (ADA)": 0.4, "b57893febd (XRP)": 0.4, "9291e9ccd8 (DOT)": 0.25}

## Entscheidung 2026-07-26

**Strategy:** I follow the trend and size by structure. Price below its long-term range with lower highs gets a small weight (0.2–0.3). A window that is building higher lows and pressing the top of its recent range gets a moderate weight (0.4–0.5). Full size needs a break above the post-crash range ceiling. Money supply growth that is accelerating (+5% YoY, rising for 4 months) is a mild tailwind, so I keep a small long rather than going flat while a base is forming.

**ce7b8b4b74 (SOL)**
- **Read:** Long-term downtrend: 163 down to 100. It lost the 104–127 range at day −54 and bottomed at 80. The bounce made a lower high at 109 (day −22), and price now sits in a tight 95–103 range on fading volume. The old floor at 104–108 is now resistance.
- **Weight:** 0.3. The base is holding, but there is no reclaim yet.
- **Change of mind:** above 108, add; below 95, cut toward flat.

**5bffa10b64 (BTC)**
- **Read:** Fell from 125 (day −80) to 90 (day −51), retested 89 (day −26), then rose with higher lows at 94.5 and 97.5. It is pushing into resistance at 101–102.4. This is a cleaner base than most.
- **Weight:** 0.35.
- **Change of mind:** a close above 102.5 raises it; below 97, cut.

**b641036695 (DOGE)**
- **Read:** Rallied to 157 (day −73), then fell steadily to 93–95. Highs keep getting lower (108 at day −22, 101 now). It retested the low at 92.9 on day −2 and bounced to 100. Structure is still weak.
- **Weight:** 0.25.
- **Change of mind:** above 108, add; below 92.9, flat.

**5b570ff63c (LTC)**
- **Read:** Low of 82 at day −31, followed by a steady staircase of higher lows: 86, 90, 95.6. It closed at 100 near a range high of 100.9. Of these windows, this one has the best short-term structure, though the larger trend is still down from 126.
- **Weight:** 0.45.
- **Change of mind:** above 101, confirms; below 95.5, cut.

**9c834015ed (LINK)**
- **Read:** Low of 79.4 at day −31, then higher lows at 85, 89 and 93.7. Day 0 closed at 100 with a +5% close near the high. It is recovering toward the 103–110 band from before the drop.
- **Weight:** 0.45.
- **Change of mind:** below 93.7, cut; above 103, add.

**1aeb04c8b5 (ETH)**
- **Read:** Double bottom at 77–78 (days −50 and −31), then higher lows at 87.7 and 94.5. It is now at the 99.6–100.6 ceiling. The base is constructive, and the 102–108 zone above it is still unreclaimed.
- **Weight:** 0.4.
- **Change of mind:** below 94.5, cut; above 101, add.

**de3fea6984 (XRP)**
- **Read:** Fell from 172 to a low of 90.7 (day −31). It bounced to 106, faded, and is now ranging 97–104.6. The old 117–120 floor is far overhead.
- **Weight:** 0.3.
- **Change of mind:** above 105, add; below 96, cut.

**3cb019a10e (DOT)**
- **Read:** Severe downtrend, from 226 to 100 with lower highs all the way down. The low is near 95–96 (days −28 and −2), and it is stuck in a 95–109 range.
- **Weight:** 0.25.
- **Change of mind:** above 108, add; below 95, flat.

**266b7b0b50 (ADA)**
- **Read:** Crashed from 216 to 83 (day −31). A spike to 120 at day −22 was fully rejected, which is a sign of supply overhead. It is now 97–105 and choppy.
- **Weight:** 0.25.
- **Change of mind:** above 109, add; below 96, flat.

**6ae434b1d1 (AVAX)**
- **Read:** Low of 84 at day −37, then an 88–105 range. It flushed to 91 at day −3 and reversed hard to 100.5 on high volume, which is a bullish sign. It is still deep below the earlier 130s range.
- **Weight:** 0.3.
- **Change of mind:** above 105, add; below 91, cut.

{"ce7b8b4b74 (SOL)": 0.3, "5bffa10b64 (BTC)": 0.35, "b641036695 (DOGE)": 0.25, "5b570ff63c (LTC)": 0.45, "9c834015ed (LINK)": 0.45, "1aeb04c8b5 (ETH)": 0.4, "de3fea6984 (XRP)": 0.3, "3cb019a10e (DOT)": 0.25, "266b7b0b50 (ADA)": 0.25, "6ae434b1d1 (AVAX)": 0.3}

## Entscheidung 2026-08-02

**Strategy:** I weight by trend structure on the 100 scale. Higher lows since the post-crash bottom (around day -60 to -38) earn 0.45–0.6. Persistent lower highs or a sideways base under resistance get 0.15–0.35. Expanding M2 with rising 3-month growth is a mild tailwind, worth a small upward tilt but never a reason to override the price structure.

## 8cc4bd1b44 (AVAX)
- **Trend and structure:** Long decline from the 150s. The crash at day -58 took price to ~100, then a lower low at 86.7 on day -44.
- **Range:** Since then price has been in a 92–108 range. Day 0 is a high-volume reversal from 94.5 back to 100.
- **Read:** Basing, but no higher-high structure yet. Resistance is 104–108; support is 92–94.
- **Weight: 0.3**, a partial stake on the base and the reversal day.
- **Change of mind:** Above 108, increase. Below 92, go flat.

## fc5d7dc68f (LINK)
- **Trend and structure:** Crash low 84.9 (day -58), then a marginal lower low at 83.6 (day -38). It has since recovered to 100–105.
- **Higher lows:** 89.7, 93.0, 95.5, 94.1. Resistance is 103–106; support is 94.
- **Read:** A tentative uptrend off the double bottom.
- **Weight: 0.5.**
- **Change of mind:** Below 94, cut. Above 106, raise toward 0.8.

## 30d77a83ca (ADA)
- **Trend and structure:** Low 72.9 (day -38). A violent rally to 105.5 (day -29) retraced to 80.9 (day -5), a higher low.
- **Day 0:** A strong breakout to 100 on 1.73x volume.
- **Read:** The strongest structure in the set. Resistance is 105.5; support is 88, then 81.
- **Weight: 0.6.**
- **Change of mind:** Below 88, reduce. Above 105.5, go fully long.

## 233f312a78 (ETH)
- **Trend and structure:** Low 80.2 (day -37), then steady higher lows: 90.9, 92.8, 95.6, 96.6.
- **Range:** Price is in a 96–105 range. Resistance is 103–105.
- **Read:** A constructive recovery.
- **Weight: 0.5.**
- **Change of mind:** Below 96.6, cut. Above 105, increase.

## 51ab3d80df (DOT)
- **Trend:** A persistent downtrend from ~200.
- **Lower highs:** 131, 113.6, 112, 108.8, 104. A gap down at day -6 reached 93.6, and day 0 is a weak bounce to 100.
- **Read:** No reversal evidence.
- **Weight: 0.15.**
- **Change of mind:** Above 109 (breaking the lower-high sequence), raise. Below 93, go flat.

## fb6b0e95bc (DOGE)
- **Trend:** Top at 167.5 (day -80), crash, low 100.9 (day -38).
- **Range:** Lower highs since then: 112, 106.8, 104.6. Price is stuck at 96–104.
- **Read:** A flat-to-down base.
- **Weight: 0.25.**
- **Change of mind:** Above 106.8, raise. Below 95.6, go flat.

## 3b151f7268 (SOL)
- **Trend and structure:** Low 81.7 (day -57). A rally to 114 (day -29) has faded with lower highs (107.3, 107.1, 105.3) to a low of 95.9 at day -1. Day 0 bounced to 100.
- **Read:** A recovery that is losing momentum.
- **Weight: 0.35.**
- **Change of mind:** Above 107, raise. Below 95.9, cut.

## 777d12dc79 (LTC)
- **Trend and structure:** Low 87.9 (day -38), then higher lows: 96.6, 98.7, 97.6. Peak 108 at day -7, pulling back to 100.
- **Read:** A shallow uptrend. Support is 97.6; resistance is 108.
- **Weight: 0.5.**
- **Change of mind:** Below 97, cut. Above 108, raise.

## 226703614c (XRP)
- **Trend and structure:** Low 92.9 (day -37). A spike to 109 at day -29, then a sideways range of 96–107.
- **Day 0:** 100, in the middle of the range.
- **Read:** No trend.
- **Weight: 0.35.**
- **Change of mind:** Above 107.1, raise. Below 96.1, cut.

## f9981239d4 (BTC)
- **Trend and structure:** Low 91.4 (day -38). Steady higher lows since: 96.8, 97.3, 98.3. Price is in a tight 98–105 range at 100.
- **Read:** Mildly constructive, low volatility.
- **Weight: 0.45.**
- **Change of mind:** Below 97.3, cut. Above 105.3, raise.

{"8cc4bd1b44 (AVAX)": 0.3, "fc5d7dc68f (LINK)": 0.5, "30d77a83ca (ADA)": 0.6, "233f312a78 (ETH)": 0.5, "51ab3d80df (DOT)": 0.15, "fb6b0e95bc (DOGE)": 0.25, "3b151f7268 (SOL)": 0.35, "777d12dc79 (LTC)": 0.5, "226703614c (XRP)": 0.35, "f9981239d4 (BTC)": 0.45}

## Entscheidung 2026-08-09

1. **Strategy:** I follow the trend over weeks to months. I hold more when price is making higher lows and holding above its recent range, and less when the window shows lower highs and a long-term decline. Every window had a crash around day -68 to -65, so I mainly judge how well each one recovered from that low. The M2 line (+5% year on year, growth rate rising for 5 months) is a mild tailwind, worth a small long tilt and no more.

2. **Windows**

**b73e89b0c0 (XRP)**
- **Read:** Fell from 135–140 to a crash low near 102, then made lower highs: 125.6, 115, 113, 108.8. It is now drifting at 100, just above the recent low of 98.3. The recovery is weak and the trend is still down.
- **Weight:** 0.2. I keep a small position only because of the M2 tilt.
- **Change my mind:** A close above 109 would turn me constructive. A break below 98 would take me flat.

**a3cfc3d99e (LINK)**
- **Read:** Crash low 85.6 at day -45, followed by higher lows (86.4, 91.9, 95.2). It rallied to 108.9 and is now consolidating between 98 and 105, holding the range after the recovery.
- **Weight:** 0.5.
- **Change my mind:** A close below 96 would cut the position. A close above 106 would add to it.

**ebb6e7a565 (SOL)**
- **Read:** Crash to 78.8, then recovered to 110 by day -36. It then pulled back with lower highs (103.4, 101.6) down to 92.5 at day -8, and has bounced to 100. The range is 92–110 and the near-term structure is mixed.
- **Weight:** 0.4.
- **Change my mind:** A close below 92 would take me flat. A close above 104 would raise the weight.

**709ca90dc1 (ETH)**
- **Read:** Crash low 78.8, then a clean run of higher lows: 79, 89.7, 94.4, 95.4, 99. Price is now pressing against the 100–103 area. This is the most orderly recovery of the group.
- **Weight:** 0.6.
- **Change my mind:** A close below 95 would cut the position. A close above 104 would lift it toward full.

**10b0b7ee1b (DOT)**
- **Read:** A long decline from above 200 to 100. Recent highs keep stepping down (112, 109, 108.9), with a low of 93.6 at day -13. The long-term downtrend is still intact.
- **Weight:** 0.15.
- **Change my mind:** A close above 110 would make me constructive. A close below 93 would take me flat.

**7971330b91 (BTC)**
- **Read:** Crash low 89.5, then higher lows at 94.5 and 96. Price is in a tight range of 96–103, just under the 103.7 recovery high. The structure is constructive but there is no breakout yet.
- **Weight:** 0.5.
- **Change my mind:** A close below 96 would cut the position. A close above 104 would add to it.

**d39473b11e (AVAX)**
- **Read:** Crash low 88.5 at day -51, then a choppy recovery into a 94–110 range. Recent swings are volatile (94.1 up to 108.8) and price sits mid-range at 100. The direction is unclear.
- **Weight:** 0.4.
- **Change my mind:** A close below 94 would take me flat. A close above 109 would raise the weight.

**9763f1326f (DOGE)**
- **Read:** Fell from about 165 to a crash low near 103. Recovery highs keep stepping lower (114.5, 109, 106.8), and price is now sideways at 98–106. The bias is a downtrend.
- **Weight:** 0.3.
- **Change my mind:** A close above 107 would raise the weight. A close below 97.5 would cut toward flat.

**833d8f856a (ADA)**
- **Read:** The deepest crash of the group, to 71. The first rebound reached 102.8 and failed back to 79, which was still a higher low. Price then broke out in the last week on strong volume, reaching 108.8, and is now retesting about 100. The base is improving.
- **Weight:** 0.55.
- **Change my mind:** A close below 95 means the breakout failed and I would cut the position. A close above 105 would add to it.

**dcf7765c59 (LTC)**
- **Read:** Crash low 86.4, then steady higher lows (90.5, 94.4, 96) and a recovery to 106.2. Price is holding 96–106 and sits at 100. The structure is constructive.
- **Weight:** 0.5.
- **Change my mind:** A close below 96 would cut the position. A close above 106 would add to it.

{"b73e89b0c0 (XRP)": 0.2, "a3cfc3d99e (LINK)": 0.5, "ebb6e7a565 (SOL)": 0.4, "709ca90dc1 (ETH)": 0.6, "10b0b7ee1b (DOT)": 0.15, "7971330b91 (BTC)": 0.5, "d39473b11e (AVAX)": 0.4, "9763f1326f (DOGE)": 0.3, "833d8f856a (ADA)": 0.55, "dcf7765c59 (LTC)": 0.5}

## Entscheidung 2026-08-16

**Strategy:** I follow the trend. I am long when the price is above its 50-day average with higher lows since the last major low. I go half-long when the price is basing sideways, and I stay mostly flat when lower highs and lower lows continue. M2 growing at +5% with an accelerating 3-month rate is a mild tailwind, so I lean slightly long in neutral cases, but it never overrides price structure.

## 6aff8458c4 (LTC)
- **Read:** Price crashed from 136.8 to 93.7 between days -98 and -71, then retested at 92.7 on day -52. It rallied to 108.3 by day -21 and has since slipped on falling volume. Recent highs are lower (108.3, 105.3), price is now 100, and support sits near 98.3.
- **Weight: 0.3.** The rebound is losing momentum, but the higher low above 92.7 still holds.
- **Change mind:** Below 98 I go flat. Above 105 I add.

## 97f82f79f5 (LINK)
- **Read:** The crash lows were 78.4 and 74.7. Since then the lows have been rising (84 on day -15), and on day -5 price broke through the 94–96 resistance on strong volume. It wicked to 103.8 and closed at 100, well above its 50-day average of about 87.
- **Weight: 0.7.** This is a clean recovery trend with a confirmed breakout.
- **Change mind:** Below 93, a failed breakout.

## 71ba75899d (ETH)
- **Read:** The crash lows were 84.4 and 80.6, followed by a steady recovery to 104. Price is now coiling between 98 and 103, with a higher low around 97 and very low volume.
- **Weight: 0.6.** The trend is intact and the pattern looks like a tight consolidation.
- **Change mind:** Below 97 I reduce. Above 105 I add.

## 2b3b79d3bc (BTC)
- **Read:** The crash lows were 94 and 92.4, and price has recovered into a flat 99–106 range for about 30 days. It is now at 100, in the lower half of that range.
- **Weight: 0.45.** The trend is neutral with a slight tilt toward support.
- **Change mind:** Below 99 I go near flat. Above 106 I add.

## e8dd9234eb (AVAX)
- **Read:** Price fell hard from 141 to 104, with a second flush to 89.7 on day -58. It then recovered into a volatile 95–110 range and now sits at 100 after a failed spike to 108.6.
- **Weight: 0.35.** The action is choppy, with no trend in either direction.
- **Change mind:** Below 95 I go flat. Above 108 I add.

## 063fbb6f78 (ADA)
- **Read:** The crash bottomed at 79. A spike to 114 on day -43 failed, and so did a rally to 121 on day -10. Price has since fallen for 10 straight sessions to 100, giving back the whole rally.
- **Weight: 0.25.** The breakout attempt failed and momentum is negative. Support is at 92–95.
- **Change mind:** Below 95 I go flat. Reclaiming 110 would change my view.

## 0529131b7a (DOGE)
- **Read:** This is a long decline from 165 to a low of 99.9. Price has formed a base in a tight 99–103 range for weeks on very low volume.
- **Weight: 0.4.** A base may be forming, but there is no breakout yet.
- **Change mind:** Above 106 I add. Below 97 I go flat.

## 902b385a21 (DOT)
- **Read:** The decline from 219 to 100 has a persistent series of lower highs: 137.9, 119.6, then 114.6. Price fell sharply to 98.6 on day -20 and is now fading back toward that low.
- **Weight: 0.15.** The downtrend is intact.
- **Change mind:** Below 98.6 I go flat. Above 109 I reconsider.

## 06204ad0ea (XRP)
- **Read:** The highs keep stepping down (130, 119, 117, 110) and price is drifting to 100. It is now testing the day -52 low of 101.6 and has already printed 99.3.
- **Weight: 0.15.** The downtrend structure is breaking support.
- **Change mind:** Below 99 I go flat. Above 106 I reconsider.

## fa46ddf8ea (SOL)
- **Read:** The crash low of 80.6 was followed by a higher low at 85.8. Price then rallied to 112.6 and pulled back to 94.6. It is now basing between 100 and 102, still above that pullback low.
- **Weight: 0.45.** The recovery structure is intact but price is consolidating.
- **Change mind:** Below 96.5 I go flat. Above 105 I add.

{"6aff8458c4 (LTC)": 0.3, "97f82f79f5 (LINK)": 0.7, "71ba75899d (ETH)": 0.6, "2b3b79d3bc (BTC)": 0.45, "e8dd9234eb (AVAX)": 0.35, "063fbb6f78 (ADA)": 0.25, "0529131b7a (DOGE)": 0.4, "902b385a21 (DOT)": 0.15, "06204ad0ea (XRP)": 0.15, "fa46ddf8ea (SOL)": 0.45}

## Entscheidung 2026-08-23

**1. Strategy**

I go long when price breaks above its 180-day range and holds there. I cut exposure when price is still below the levels where it broke down earlier in the window (the old structure from before the crash around day -82) or when the breakout failed intraday with a long upper wick on heavy volume. The M2 line (+5% and rising) is a mild tailwind, so I lean slightly toward exposure, but price structure decides.

**2. Windows**

**225b95ff31 (SOL)**
- **Read:** Price fell from a pre-crash range of 86–90 to 63 and then built a base at 76–82 for 40 days. A 4-day breakout took it to 100, a new 180-day high. Day -1 spiked to 107.7 but closed at 98.3, a rejection on volume of 2.8. Day 0 was an inside day.
- **Key levels:** support 89–91 (the breakout gap), resistance 103 and then 108.
- **Weight:** 0.5. The breakout is real, but the blow-off wick tempers it.
- **Change my mind:** a close below 89 takes me flat; a close above 108 adds.

**1d5dcf1a84 (ETH)**
- **Read:** A base at 74–78 broke out to 100, retesting the prior high of 100.1 from day -128. Day -2 reached 103.4, and day -1 closed at 98.3, a smaller rejection than the others. Volume is cooling.
- **Key levels:** resistance 103.4, support 91.
- **Weight:** 0.55. Price is at the range highs, and the rejection was modest.
- **Change my mind:** below 91 goes flat; above 104 adds.

**82a66a79c7 (ADA)**
- **Read:** The window shows lower highs all the way down (138, 129, 127, 118, 127). The pre-crash zone of 102–110 caps price. Day -1 spiked to 113.8 and closed at 99.6 on volume of 3.0, a clean rejection at resistance.
- **Weight:** 0.3. This is a counter-trend spike into overhead supply.
- **Change my mind:** a close above 114 raises the weight; below 87 goes flat.

**e4c1b50439 (DOGE)**
- **Read:** Price peaked at 127 on day -101, then crashed from 108 and drifted near 74–80 for 50 days. The spike reached 107.9 on day -1, exactly at the pre-crash shelf of 108, and was rejected on volume of 3.46.
- **Weight:** 0.35. Price is still inside the broken-down range, with a failed test of resistance.
- **Change my mind:** a close above 108 raises the weight; below 86 goes flat.

**4256d7ee9d (DOT)**
- **Read:** A persistent downtrend from 179 to a low of 81. The pre-crash zone of 125–135 is far above. Day -1 reached 111 and closed at 99.1.
- **Weight:** 0.25. This is a bounce inside a major downtrend.
- **Change my mind:** a close above 112 raises the weight; below 85 goes flat.

**c593ff5353 (BTC)**
- **Read:** The 81–84 base broke out to 100, which is back at the pre-crash level of 95–100. Prior highs are at 102–106. Days -1 and 0 were tight, quiet consolidation with no blow-off wick and fading volume. That is constructive.
- **Key levels:** support 93, resistance 106.
- **Weight:** 0.55.
- **Change my mind:** below 93 goes flat; above 106 adds.

**1061277aa2 (LINK)**
- **Read:** Price had been making higher lows since day -22, at 70 → 76 → 82, before the breakout. It now sits above every earlier high in the window (old high 94.2). Day -1 reached 109.3 and closed at 100.9.
- **Weight:** 0.65. This is the clearest 180-day range breakout of the set, with structure that was building beforehand.
- **Change my mind:** a close below 91 means the breakout failed back into the old range.

**9aabef038d (LTC)**
- **Read:** Price has made lower highs from 115.9 down to 91. It has now recovered to the pre-crash level of 100, but the 104–116 supply zone sits overhead. Day -1 reached 106 and closed at 100.3.
- **Weight:** 0.4.
- **Change my mind:** below 89 goes flat; a close above 106 raises the weight.

**273fd6b4b2 (AVAX)**
- **Read:** A downtrend from highs of 138, with a pre-crash shelf at 117. Price had chopped at 81–90 before the spike. Day -1 reached 109.3 and closed at 98.5.
- **Weight:** 0.3. The bounce is still well below broken structure.
- **Change my mind:** a close above 109 raises the weight; below 89 goes flat.

**737c501ac0 (XRP)**
- **Read:** Price bled steadily to new lows near 65 and then went parabolic, up 52% in 4 days on volume as high as 6x. Day -1 reached 111.8 and closed at 96.2, a huge wick. The 180-day highs are 102–106.
- **Weight:** 0.4. There is momentum, but exhaustion and mean-reversion risk are high.
- **Change my mind:** below 83 goes flat; a close above 112 raises the weight.

**3. Weights**

{"225b95ff31 (SOL)": 0.5, "1d5dcf1a84 (ETH)": 0.55, "82a66a79c7 (ADA)": 0.3, "e4c1b50439 (DOGE)": 0.35, "4256d7ee9d (DOT)": 0.25, "c593ff5353 (BTC)": 0.55, "1061277aa2 (LINK)": 0.65, "9aabef038d (LTC)": 0.4, "273fd6b4b2 (AVAX)": 0.3, "737c501ac0 (XRP)": 0.4}

## Entscheidung 2026-08-30

**Strategy:** I stay long when price holds above a recent breakout from a multi-month base and the broader trend over 180 days is flat to rising. I cut the weight when the breakout was a fading spike inside a longer downtrend. I treat the M2 line (+5% year-on-year, growth slowing for 1 month) as mildly supportive, so it moves no weight on its own. The decision is the support zone at about 98–99: holding it keeps me long, losing it argues for flat.

**6656767b5f (LINK)**
- **Trend and structure:** Price crashed to 66 (day -86), built a higher-low base at 73–75, then broke out on heavy volume through the old high of 96 to 111.
- **Now:** It is consolidating between 100 and 108, at 6-month highs.
- **Weight 0.7:** the base is clean and the old resistance at 96 should now act as support.
- **Change my mind:** a close below 97.

**e9aaf3bb8f (BTC)**
- **Trend and structure:** The base sat at 81–84, and the breakout ran to 102–105.
- **Now:** Price sits just under the earlier 101–107 highs from days -130 to -110. Volume after the breakout is calm and the range is tight at 99–105.
- **Weight 0.6:** constructive, but overhead supply remains.
- **Change my mind:** a close below 98.

**9c6e26f922 (DOT)**
- **Trend and structure:** The window is a long downtrend from 188 to about 92, with lower highs throughout.
- **Now:** A spike to a 126 high has given back nearly all of its gain (115 to 100), with prior swing highs at 104–108.
- **Weight 0.3:** this looks like a fading spike, not a trend change.
- **Change my mind:** below 98 I go flat; above 110 I would add.

**cbecc8e7dd (XRP)**
- **Trend and structure:** Price drifted down to a 73–74 base, then broke out on very large volume (6× average) to a 125 wick, which looks like a blow-off.
- **Now:** It has faded to 100, back inside the old 100–110 range.
- **Weight 0.5:** the move is strong but extended, and the wick means sellers showed up.
- **Change my mind:** a close below 98.

**e91074b685 (LTC)**
- **Trend and structure:** Higher lows run from 82 (day -67) through a 92–95 base. The breakout reached 115, and the old highs are far overhead at 120–126.
- **Now:** Price is pulling back to 100 at support.
- **Weight 0.6.**
- **Change my mind:** below 98.

**3a928d1e78 (SOL)**
- **Trend and structure:** Price crashed to 59, then made a series of higher lows (63, 66, 70, 72). The breakout ran to 108, well above the prior high of 96.
- **Now:** It is at 6-month highs and holding above 98.
- **Weight 0.7.**
- **Change my mind:** below 97.

**9513eb84c9 (AVAX)**
- **Trend and structure:** The trend fell from 140 to 87–95 over the window. The breakout spiked to 117 and has faded to 100.
- **Now:** It is barely above the 96–100 resistance from days -60 to -55.
- **Weight 0.5:** mixed.
- **Change my mind:** below 97 I go flat; holding above 106 would raise the weight.

**0fbaa51919 (ADA)**
- **Trend and structure:** The trend fell from 150 to 75. Spikes to 104 (day -57), 110 (day -24) and 134 (day -8) have each failed and fully reversed.
- **Now:** The pattern of failing spikes is repeating at 100.
- **Weight 0.3.**
- **Change my mind:** below 98 I go flat; a hold above 111 would make me re-evaluate.

**420b67fc67 (DOGE)**
- **Trend and structure:** The trend fell from 144 to an 84–86 base. A spike to a 123 wick has faded to 100, under the earlier lower highs of 108–112.
- **Weight 0.4.**
- **Change my mind:** below 98 I cut; above 110 I add.

**ac4c970562 (ETH)**
- **Trend and structure:** Price crashed to 62, recovered with higher lows to a 77–79 base, then broke out on a strong day (day -11) to 105.
- **Now:** It is consolidating at 99.5–106, at the old 98–102 highs.
- **Weight 0.6.**
- **Change my mind:** below 98.

{"6656767b5f (LINK)": 0.7, "e9aaf3bb8f (BTC)": 0.6, "9c6e26f922 (DOT)": 0.3, "cbecc8e7dd (XRP)": 0.5, "e91074b685 (LTC)": 0.6, "3a928d1e78 (SOL)": 0.7, "9513eb84c9 (AVAX)": 0.5, "0fbaa51919 (ADA)": 0.3, "420b67fc67 (DOGE)": 0.4, "ac4c970562 (ETH)": 0.6}

## Entscheidung 2026-09-06

## 1. Strategy

I go long when price has reclaimed its 50-day structure and is holding above a recent high-volume breakout. I size up when price has also cleared the old resistance from before the crash, and size down when overhead supply sits just above 100 or the post-breakout highs keep getting lower. M2 at +5% year-on-year with a mild one-month dip is neutral to slightly supportive, so it doesn't change any weight.

## 2. Windows

All ten windows share the same shape: a sharp drop around day -96 to -93, a 2–3 month base, a high-volume breakout around day -18 to -16, and a pullback that has now recovered to 100.

### 11c9a05195 (LTC)
- **Read:** Before the crash it traded 95–110; it bottomed near 73.7 and based at 76–87. The breakout reached 100.9, pulled back to 86.2, and has now reclaimed 100 on a strong day -1 (+7.8% on 2.3× volume). Higher lows at 86 and 90.
- **Supply:** The 100–110 zone from before the crash sits overhead.
- **Weight:** 0.7. The trend is intact and price is pressing the breakout high, but there is supply above.
- **Change my mind:** a close below 90.

### 16c8e540d9 (LINK)
- **Read:** The pre-crash range was only 63–82. Price is now well above it and closed at a window high of 100 on 1.7× volume, through the breakout high of 95.4. There is no overhead supply in the window.
- **Weight:** 0.9. This is the cleanest breakout in the set.
- **Change my mind:** a close below 87.

### b8151b0019 (AVAX)
- **Read:** The pre-crash range was 110–133, so 100 is still below the old 113–130 supply. Price recovered from a 71.8 low and the consolidation since the breakout ran from 89 to 105. It is now closing near the top of that range.
- **Weight:** 0.6. The uptrend is real, but heavy resistance sits at 105–120.
- **Change my mind:** a close below 89.

### e18ef5ee38 (BTC)
- **Read:** The pre-crash peak was about 103. Since the breakout it has held a tight 95–102 range with fading volume, and day 0 was a quiet inside day. Price is near the top of the range.
- **Weight:** 0.6. The trend is constructive but it has no breakout confirmation yet.
- **Change my mind:** a close below 94.5.

### c62900dd6f (ETH)
- **Read:** Price has cleared the pre-crash high of about 98 after recovering from a 60 low. It has held a 94–102 shelf for about two weeks, with the post-breakout lows holding near 93.7.
- **Weight:** 0.7.
- **Change my mind:** a close below 93.5.

### 532db04063 (ADA)
- **Read:** Very choppy. The rally attempts reached 89, 94.8 and then 115.7 intraday, each followed by a sharp reversal. Since the spike, the highs are lower (115.7, 101.7, 100.2), and the pre-crash range of 105–130 is overhead.
- **Weight:** 0.5. The direction is up, but the behaviour is unreliable.
- **Change my mind:** a close below 85.

### 4d6cdcdcb0 (DOGE)
- **Read:** The pre-crash peak was 130, so a lot of supply sits from 104 to 125. The breakout wick reached 110.9, and day -1 was rejected at 104.7. Price is now ranging 88–101.
- **Weight:** 0.5.
- **Change my mind:** a close below 88.

### 553caf4c7f (SOL)
- **Read:** Price has cleared the pre-crash high of 92.4. The day -10 high was 103.8, and since then it has made higher lows (91.4, then 95.4). Day 0 closed at 100 on above-average volume.
- **Weight:** 0.75.
- **Change my mind:** a close below 91.

### 018e5c5e53 (DOT)
- **Read:** The longer-term downtrend runs from 167 to 77. Price broke out from 77 to an intraday high of 105.4 and is now making higher lows (82.5, 85.6, 86). Day 0 was +6.8% to 100 on 1.67× volume. Supply sits at 105 and again at 120–140.
- **Weight:** 0.55. The short-term trend is improving, but the long-term trend is still down.
- **Change my mind:** a close below 86.

### cb42bcc627 (XRP)
- **Read:** The pre-crash range was 91–108. The breakout was a blow-off spike to 119.4 on 6× volume. Since then the highs are lower (108.9, 104.2, 100.6) and price has ranged 92–104 with fading volume.
- **Weight:** 0.5. The spike looks like exhaustion more than a sustainable trend.
- **Change my mind:** a close below 92.

## 3. Weights

{"11c9a05195 (LTC)": 0.7, "16c8e540d9 (LINK)": 0.9, "b8151b0019 (AVAX)": 0.6, "e18ef5ee38 (BTC)": 0.6, "c62900dd6f (ETH)": 0.7, "532db04063 (ADA)": 0.5, "4d6cdcdcb0 (DOGE)": 0.5, "553caf4c7f (SOL)": 0.75, "018e5c5e53 (DOT)": 0.55, "cb42bcc627 (XRP)": 0.5}

## Entscheidung 2026-09-13

**Strategy:** I go long when price has broken out of a multi-week base on heavy volume and holds above that breakout zone. I go lighter when the post-breakout highs keep getting lower, when a spike was sharply rejected, or when price is still well below its earlier highs in the 180-day window. M2 growing about 5% a year is mildly supportive but neutral; it does not change any single weight much.

**7b51b33269 (DOGE)**
- **Read:** The longer trend is down: price peaked near 140 around day -122, crashed to about 85 and based there for weeks. It broke out between days -25 and -22 to 111–122. Since then the highs have fallen (122, 115.5, 111) and price is drifting down to 100, close to the 99–98 support.
- **Weight:** Moderate, 0.4. The breakout is still holding, but momentum is fading and the 140 high is far overhead.
- **Change my mind:** A close below 97 means the breakout failed.

**c6db54a0cd (LTC)**
- **Read:** Price based at 82–84, broke out to 103, and pulled back to 89. It then made a higher high, a 110.6 wick at day -6, and a higher low near 96. At 100 it is back inside the earlier 100–112 range.
- **Weight:** 0.6, because the higher-high and higher-low structure is constructive.
- **Change my mind:** Below 96.

**17bb80dd3b (DOT)**
- **Read:** A long downtrend ran from 162 to 72. The breakout reached 103 and then pulled back to 81. On days -6 to -5 there was a blow-off spike to 128.5 on about 4x volume, which reversed hard back to 100. The lows are rising, but the spike was clearly rejected.
- **Weight:** 0.3. A failed blow-off is a short-term warning.
- **Change my mind:** Below 96 to exit; reclaiming 112 to add.

**f27f24b740 (ETH)**
- **Read:** Price based at 75–78 and broke out on strong volume to about 102. It has held a tight 96–103 range for three weeks, above the pre-crash 81–95 range. This is a clean consolidation above the breakout.
- **Weight:** 0.7.
- **Change my mind:** Below 95.

**ddc815126e (AVAX)**
- **Read:** Price based at 86–90 and broke out to 108–114. It has since ranged 96–112. The latest high at 112.5 is slightly lower and price sits at 100, mid-to-low in the range.
- **Weight:** 0.5.
- **Change my mind:** Below 96.

**44252d3569 (ADA)**
- **Read:** After a very large crash, price based at about 85 and broke out to a 127 wick. It has consolidated between 93 and 114 since. The highs are falling (127, 114), while the lows have edged up from 93 to 98.5.
- **Weight:** 0.45. The structure is mixed and volatile.
- **Change my mind:** Below 93.

**2bc9f762f3 (LINK)**
- **Read:** Price recovered steadily from 62 to 85 before the breakout to 112, then made a higher high at 122 (day -6). It pulled back to 100. The lows are rising (98, then 100.4), and price is above the pre-crash 80–95 range.
- **Weight:** 0.6. The trend is up, though the pullback from 122 is sharp.
- **Change my mind:** Below 97.

**407b3824eb (XRP)**
- **Read:** Price based at 74–75, then spiked to 126.7 on about 6x volume. It has formed a narrowing triangle since: highs of 126.7, 115.6, 110.6 and 108.2, with lows around 98. Price at 100 sits near the lower bound.
- **Weight:** 0.45.
- **Change my mind:** Below 97 means the triangle breaks down; above 108 means it breaks up.

**6814680afa (SOL)**
- **Read:** Price based at 72–77 and broke out more gradually to 111.4, then consolidated between 99 and 108. It is above the pre-crash 82–98 range and is now testing 99–100 support.
- **Weight:** 0.55.
- **Change my mind:** Below 98.

**30fde1f346 (BTC)**
- **Read:** Price based at 82–84 and broke out to 103.5. It has held a tight 99–107 range for three weeks, near the earlier 107 high, with low volatility. It is now at the lower edge of that range.
- **Weight:** 0.6.
- **Change my mind:** Below 98.5.

{"7b51b33269 (DOGE)": 0.4, "c6db54a0cd (LTC)": 0.6, "17bb80dd3b (DOT)": 0.3, "f27f24b740 (ETH)": 0.7, "ddc815126e (AVAX)": 0.5, "44252d3569 (ADA)": 0.45, "2bc9f762f3 (LINK)": 0.6, "407b3824eb (XRP)": 0.45, "6814680afa (SOL)": 0.55, "30fde1f346 (BTC)": 0.6}

## Entscheidung 2026-09-20

**Strategy:** I go long when price is in an uptrend: a close near the top of the 180-day range, a structure of higher lows, and a base or consolidation that has held. I scale down when price is still under major overhead highs, is stuck mid-range after a one-off spike, or has stretched too far, too fast. M2 growth of +5% that is slowing for only one month is a mildly supportive backdrop; it doesn't change any weight much.

### 1d37248b92 (LINK)
- **Read:** Price based at 56–67 from about day −110 to −40. It then broke out sharply at −32/−30 to around 95, spiked to 109 at −14, and pulled back to a low of 84.8. It has now recovered to 100. The trend is up with higher lows, and price sits in the upper part of an 85–109 range.
- **Weight: 0.7.** The trend and structure are intact, but there is overhead supply at 105–109.
- **Change my mind:** a close below 85.

### e3608a1da9 (AVAX)
- **Read:** A long base at 52–60. A first push to 69–73 at −30 faded. Over the last two days price jumped from 67 to 100 on very high volume (3.9× and 6.1× average), clearing every high in the window (prior top about 92.7). This is a powerful breakout, but it is extremely extended and day 0's range was 83–101.
- **Weight: 0.5.** I want exposure to a high-volume breakout from a long base, but I'm holding back because of blow-off and gap-fill risk.
- **Change my mind:** a close below 83 (day 0's low).

### b0af5d817c (DOGE)
- **Read:** Highs of 130–135 around day −130, then a decline to 79. A spike at −30/−29 reached 115 intraday and failed. Since then price has ranged 90–105 and is now 100, mid-range and well below the earlier highs. There is no clean trend.
- **Weight: 0.4.**
- **Change my mind:** a close above 106 would be bullish; a close below 90 would take me flat.

### db1047b652 (XRP)
- **Read:** Price drifted from 105 down to 70 and then spiked to 120 intraday at −29, a failed blow-off. It has ranged 88–108 since. The 100 level is mid-range, with lows at 88–89 holding.
- **Weight: 0.5.**
- **Change my mind:** a close below 88 would take me out; a close above 108 would add.

### b62d0f4f7d (SOL)
- **Read:** The low was 54 at −106. Price then based at 64–74, broke out at −32, and has stair-stepped with higher lows (78.9, then 86.2). At −2 it closed 101.4, a new high for the window, and it is holding about 100. This is a clean uptrend with no overhead supply.
- **Weight: 0.8.**
- **Change my mind:** a close below 86.

### ab5852f179 (DOT)
- **Read:** A long downtrend from 124 to 66. A spike to 113 at −12 retraced to 82. Price has rebounded to 100, but the window has a declining long-term structure and heavy overhead at 110–125. It is volatile.
- **Weight: 0.45.**
- **Change my mind:** a close below 82 would take me flat; a close above 113 would raise the weight.

### 5a319e9997 (ADA)
- **Read:** Price started at 117–124 and crashed to 61. It rallied to 88, then spiked to 113 at −29. Since then it has ranged 84–102 and is now 100, near the top of that range. Overhead from 105–124 remains.
- **Weight: 0.45.**
- **Change my mind:** a close below 84 would take me flat; a close above 103 would add.

### 3f1103fb27 (ETH)
- **Read:** Price based tightly at 70–73. The −32 breakout came on strong volume, and price has since consolidated at 89–96. It is now at 100, the highest close in the window and above the prior high of 91–93 from day −156. This is constructive.
- **Weight: 0.75.**
- **Change my mind:** a close below 89.

### 1682906213 (LTC)
- **Read:** A high of 103 at −133, then a drop to 67. The recovery has made higher lows (67, then 74, 80, 85.5). After the breakout at −30 price reached 101 at −13, and it is now 100, just under the window high of 103. The uptrend is intact.
- **Weight: 0.7.**
- **Change my mind:** a close below 85.5.

### b717af9564 (BTC)
- **Read:** A high of 102 at −137 and a low of 72. Price recovered steadily, broke out at −32, and has held a tight 92–101 range with lower volatility. It is now 100, near the window high. The structure is orderly.
- **Weight: 0.7.**
- **Change my mind:** a close below 92.

{"1d37248b92 (LINK)": 0.7, "e3608a1da9 (AVAX)": 0.5, "b0af5d817c (DOGE)": 0.4, "db1047b652 (XRP)": 0.5, "b62d0f4f7d (SOL)": 0.8, "ab5852f179 (DOT)": 0.45, "5a319e9997 (ADA)": 0.45, "3f1103fb27 (ETH)": 0.75, "1682906213 (LTC)": 0.7, "b717af9564 (BTC)": 0.7}

## Entscheidung 2026-09-27

**Strategy:** I follow the trend. I go long when price sits above a rising medium-term structure and at or near window highs. I size down when there is heavy overhead supply from earlier in the window, a climactic or blow-off move, or wide chop around 100. M2 at +6% year-on-year is mildly supportive but decelerating, so it does not change sizing much.

### 2064f8d74b (SOL)
- **Read:** The base at 60–62 broke out at day -39 and ran to 77–90. Price then consolidated at 80–87, broke out again at day -9 above 90, and now sits at window highs (100, intraday 102.4).
- **Structure:** Clean higher highs and higher lows. The earlier high at about 80 is far below.
- **Weight:** 0.9, because it is a strong, uncluttered uptrend.
- **Change my mind:** a close below 90, the day -8/-9 breakout zone.

### 1ee3628d05 (LTC)
- **Read:** The base at about 62 broke out to 74–77, pulled back to 67, then ground up to 77–83.
- **Structure:** Day -3 jumped from 87 to 101 on 6.7x volume, and price has held 97–105 since. The day 0 close of 100 is off the 105 high.
- **Weight:** 0.7. The trend is intact, but that volume spike looks climactic.
- **Change my mind:** below 96.7, the day -2 low. Below 94 I would go flat.

### cf465ed82d (LINK)
- **Read:** Breakout at day -39, first peak at 97.6 on day -20, pullback to 77.6, then a rally to new highs at 100–103.
- **Structure:** Higher low, higher high.
- **Weight:** 0.85.
- **Change my mind:** a close below 93; the day -4 low is 86.

### 52059cce1a (DOGE)
- **Read:** Earlier in the window price traded at 110–122. The day -37 breakout spiked to 104 and failed back to 83. The day -6 spike to 109 also faded to 96.
- **Structure:** Chop at 95–105 with heavy overhead supply at 103–120.
- **Weight:** 0.5.
- **Change my mind:** above 105 I would add; below 94 I would cut.

### c315a298fe (BTC)
- **Read:** The earlier high was 98 at day -144, and price is now just above it at 100.
- **Structure:** The breakout consolidated at 89–96, then pushed through to 102.5. It is now a tight, quiet range of 98–103 on low volume, which is constructive.
- **Weight:** 0.75.
- **Change my mind:** a close below 96.

### 52ce4514b2 (XRP)
- **Read:** The day -38/-36 explosion reached 112 and then retraced to 83–85.
- **Structure:** Higher lows at 84.6 and 97.5, but the range is a volatile 85–112, with the 109 high on day -4 capping price.
- **Weight:** 0.65.
- **Change my mind:** below 95.

### adf67b9e22 (ETH)
- **Read:** The earlier window high was 91.7. The day -39 breakout gap went to 94.7, then consolidated at 88–95.
- **Structure:** Price is now holding 99–104 quietly, above all prior highs.
- **Weight:** 0.8.
- **Change my mind:** a close below 96.

### 1178e332aa (DOT)
- **Read:** Earlier highs were at 105–113, and price fell to 59 before recovering.
- **Structure:** The day -19 spike to 101 failed down to 74. Price has climbed back to 100 with a higher low at 85, but it sits right under 100–113 supply and is volatile.
- **Weight:** 0.55.
- **Change my mind:** below 85 I would go flat; above 104 I would add.

### 8b84343c8c (ADA)
- **Read:** Earlier highs were at 105–113, followed by a crash to 54. Price recovered to 101 on day -37, pulled back to 75, and is now at 100–104 again.
- **Structure:** This is a third test of the 100–104 area, with older supply above it.
- **Weight:** 0.55.
- **Change my mind:** below 91 I would cut; a close above 105 I would add.

### 35c04da5d2 (AVAX)
- **Read:** The base at 57–62 had a weak breakout to 76 that faded to 66.
- **Structure:** Days -8/-7 gapped from 70 to 105 on 3.7–5.7x volume, a blow-off. Price pulled back to 92 and is now at 100, above the prior high of 96.
- **Weight:** 0.6. The momentum is strong but the move is very extended.
- **Change my mind:** below 91.

{"2064f8d74b (SOL)": 0.9, "1ee3628d05 (LTC)": 0.7, "cf465ed82d (LINK)": 0.85, "52059cce1a (DOGE)": 0.5, "c315a298fe (BTC)": 0.75, "52ce4514b2 (XRP)": 0.65, "adf67b9e22 (ETH)": 0.8, "1178e332aa (DOT)": 0.55, "8b84343c8c (ADA)": 0.55, "35c04da5d2 (AVAX)": 0.6}
