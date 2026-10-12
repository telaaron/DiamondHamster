# E-005: was die KI gedacht hat (Set A)

Volle Antwort des Deciders pro Entscheidungswoche, unverändert. Er sah weder Datum noch Coin-Namen; die Namen in Klammern sind erst danach eingesetzt. Gesendeter Prompt und Daten: runs/<set>/<woche>/requests.json.

## Entscheidung 2026-07-05

**1. Strategy.** I use a medium-term trend filter on the price path rebuilt from the returns. I go long when price is above both its 50-day and 100-day averages and the 4-month trend is up. I cut toward flat when price is below those averages, and I trim size after a vertical spike, because a chase entry has poor risk/reward. Every window shows the same pattern: a large drawdown early on, a base over the last ~120 days, a sharp selloff about 30–33 days ago (a 15–25% drop), and then a recovery.

**b2c9e5b9be (XRP)**
- **Read:**
  - Down 33% over 180 days and flat over 120 days.
  - Up 10.5% in the last 5 days and 14% above the 30-day low.
  - About 11% below the 60-day high and 2–5% above the 20/50/100-day averages.
- **Weight: 0.5.** It is a recovery inside a range and the longer-term trend is weak.
- **Change my mind:**
  - Below −6% (back under the averages): go flat.
  - Above +11% (new 60-day high): add.

**cfc692ed5c (ETH)**
- **Read:**
  - Up 11% over 120 days, so the base is rising.
  - Up 14% over 5 days and above all the averages.
  - 11% below the 60-day high.
- **Weight: 0.6.**
- **Change my mind:**
  - Below −6%: cut.
  - Above +11%: add.

**c07d39fffc (LINK)**
- **Read:**
  - Up 7% over 120 days and flat over 20 days.
  - Up 12% over 5 days, 2–4% above the averages, 11.5% below the 60-day high.
- **Weight: 0.55.**
- **Change my mind:**
  - Below −5%: cut.
  - Above +12%: add.

**9eea9345db (DOT)**
- **Read:**
  - Down 14% over 120 days and down 10% over 60 days.
  - Below the 50-day (−4%) and 100-day (−7%) averages.
  - Only 7% above the 30-day low; lower highs persist.
- **Weight: 0.2.** This is a downtrend with a weak bounce.
- **Change my mind:**
  - Above +7% (reclaims the 100-day average): go to 0.5.
  - Below −7% (new low): go flat.

**c2a4d40474 (BTC)**
- **Read:**
  - The strongest base: up 14% over 120 days, with the lowest volatility of the group.
  - Above all the averages and 11.5% below the 60-day high.
- **Weight: 0.6.**
- **Change my mind:**
  - Below −5%: cut.
  - Above +12%: add.

**2072aaa963 (LTC)**
- **Read:**
  - Up 6.6% over 20 days and up 5% over 120 days.
  - 4–7% above all the averages, with higher lows since the selloff.
  - 10.5% below the 60-day high.
- **Weight: 0.6.**
- **Change my mind:**
  - Below −7%: cut.
  - Above +10%: add.

**c24369747b (DOGE)**
- **Read:**
  - Down 33% over 180 days and down 7% over 20 days.
  - Below the 50-day average and flat to the 100-day.
  - 15.5% below the 60-day high, and the bounce came on thin volume.
- **Weight: 0.3.**
- **Change my mind:**
  - Above +5% (back above the 50-day average): go to 0.5.
  - Below −9% (30-day low): go flat.

**3be3b8db6d (ADA)**
- **Read:**
  - Crashed about 36% around days −33 to −30.
  - Then went vertical: up 29% in 5 days on 2× volume, and now 20% above the 20-day average.
  - Day 0 was the first down day.
  - Still 11.5% below the 60-day high.
- **Weight: 0.4.** The momentum is real, but the entry is badly extended and a fade back toward −10% to −15% is likely.
- **Change my mind:**
  - Below −15% (gives back the thrust): go flat.
  - Holding and breaking above +12%: add.

**c8d4279a30 (AVAX)**
- **Read:**
  - Up 12% over 120 days and up 6% over 20 days.
  - Bounced from a capitulation (days −17/−16) with strong volume on the reversal.
  - Above all the averages.
- **Weight: 0.6.**
- **Change my mind:**
  - Below −6%: cut.
  - Above +11%: add.

**a7f8295891 (SOL)**
- **Read:**
  - The stats run for this window came back cut off, so this read comes from the daily returns, not computed figures.
  - A strong recovery: a run of +5% days over the last two weeks and higher lows since day −29.
  - Likely above the averages and about 10% below the 60-day high.
- **Weight: 0.6.**
- **Change my mind:**
  - Below −7%: cut.
  - Above +10%: add.

{"b2c9e5b9be (XRP)": 0.5, "cfc692ed5c (ETH)": 0.6, "c07d39fffc (LINK)": 0.55, "9eea9345db (DOT)": 0.2, "c2a4d40474 (BTC)": 0.6, "2072aaa963 (LTC)": 0.6, "c24369747b (DOGE)": 0.3, "3be3b8db6d (ADA)": 0.4, "c8d4279a30 (AVAX)": 0.6, "a7f8295891 (SOL)": 0.6}

## Entscheidung 2026-07-12

## Strategy

I score each window by where the last close sits relative to the sharp sell-off around days −41 to −36, and by the shape of the rebound since. If the window recovered most of that drop and is holding near its rebound highs, it gets a meaningful long weight (0.4–0.6). If it failed to recover or is making lower highs, it gets a small weight (0.1–0.25). Recent low-volume drift counts as consolidation, not as a signal on its own. All levels below are summed daily % returns, so they are approximate.

## 99f951ca69 (SOL)
- **Read:** The −41…−36 crash cost about −27%. The rebound from −35 to −10 gained about +28%, so the drop was essentially fully retraced. The last 10 days pulled back about −5% on very light volume (0.4–0.6), which looks like an orderly consolidation under the rebound high (~+5% above the last close).
- **Weight:** 0.5. The trend has repaired, but the price is stalling just under resistance.
- **Change my mind:** above +6% (breakout) I would add; below −8% the rebound has failed and I would cut.

## d25e7e1782 (XRP)
- **Read:** The crash cost about −19%. The rebound peaked near +13% at −27, then faded back to roughly flat. The last 10 days are about 0%, so the price sits well below the pre-crash level. Structure is a lower high with a weak recovery.
- **Weight:** 0.25.
- **Change my mind:** above +8% I would add; below −6% I would go flat.

## 56ba382f51 (ETH)
- **Read:** The crash cost about −24%. The rebound reached +14%, dipped, then rose again: +6% over the last 10 days, with the last close at the highs of the recovery. This is the strongest structure: higher lows since −18.
- **Weight:** 0.6.
- **Change my mind:** below −7% (losing the −18 swing low area) I would cut to 0.3.

## 090759269c (BTC)
- **Read:** This is a lower-volatility asset. The crash cost about −19%. The rebound peaked near +9%, pulled back to −3.5%, and has since climbed back to about +5%. The last close is ~3–4% under the rebound high, and the trend is mildly up.
- **Weight:** 0.45.
- **Change my mind:** above +4% I would add; below −5% I would cut.

## bf8a36bd07 (LINK)
- **Read:** The crash cost about −20%. The rebound reached +12%, pulled back to about −2%, and has since recovered to about +9%. The last close is ~3% under the rebound high, on very low volume (0.3–0.4).
- **Weight:** 0.5.
- **Change my mind:** above +4% I would add; below −7% I would cut.

## a8ff6f16bc (LTC)
- **Read:** The crash cost about −22%. The rebound reached +10% and then chopped between −1% and +7%. The last close is about +6.5% from the trough, roughly 4% under the rebound high. The market is range-bound and has not reclaimed the pre-crash level.
- **Weight:** 0.4.
- **Change my mind:** above +5% I would add; below −6% I would cut.

## 975a8bf046 (ADA)
- **Read:** The crash cost about −38%, the deepest of these windows. The rebound faded to new lows. Days −11 to −8 then spiked about +30% on 2× volume, and the last 7 days gave back about −17% with no sign of stopping. This is a pump-and-fade, still falling.
- **Weight:** 0.2.
- **Change my mind:** a reclaim of +10% would raise the weight; below −8% (back toward the pre-spike base) I would go flat.

## ec83469095 (DOT)
- **Read:** The crash cost about −22%. The rebound only reached +7%, then made new lows at about −15%. The price is now around −10% from the crash trough. The day −2 jump of +6% was immediately sold. This is a clear downtrend with lower highs.
- **Weight:** 0.1.
- **Change my mind:** above +10% (a higher high) I would raise the weight.

## 36042eeee5 (DOGE)
- **Read:** The crash cost about −20%. The rebound reached +8%, then rolled over to new lows near −12%. The price is now around −11% from the trough, with a downtrend and lower highs.
- **Weight:** 0.1.
- **Change my mind:** above +10% I would raise the weight.

## 458d13ce20 (AVAX)
- **Read:** The crash cost about −29%. The rebound was weak (+3%), followed by another flush at −24/−23. The price has been choppy since and is at about −2% from the trough. The last two days fell −5% with volume picking up. There is no recovery.
- **Weight:** 0.1.
- **Change my mind:** above +8% I would raise the weight; I already hold close to the minimum.

{"99f951ca69 (SOL)": 0.5, "d25e7e1782 (XRP)": 0.25, "56ba382f51 (ETH)": 0.6, "090759269c (BTC)": 0.45, "bf8a36bd07 (LINK)": 0.5, "a8ff6f16bc (LTC)": 0.4, "975a8bf046 (ADA)": 0.2, "ec83469095 (DOT)": 0.1, "36042eeee5 (DOGE)": 0.1, "458d13ce20 (AVAX)": 0.1}

## Entscheidung 2026-07-19

**Strategy:** I build an approximate price path by summing the daily returns, then judge the trend over the last 50 to 60 days and where the last close sits relative to its recent swing lows and highs. I add exposure when the window shows higher lows and is reclaiming its recent highs after the shared sell-off around day -47 to -44. I stay light or flat when price is still making lower lows or sits near its lows with no reversal. *(My scripts returned no output in this environment, so the path figures below are hand-summed approximations.)*

## 2cd2e372ac (DOGE)
- **Read:** Steady downtrend. Cumulative change is about -27% over the last 50 days, and price sits within about 1% of its window low. The bounce at days -17/-16 failed, and volume is drying up with no sign of buyers.
- **Levels:** Swing high about +7% (day -15). Low about -1%.
- **Weight:** 0.1, because the trend is down and there is no base yet.
- **Change of mind:** a close above +8% (reclaiming the day -15 high).

## a23c7f9cf5 (XRP)
- **Read:** Down about 17% over 50 days. Price is ranging between the day -19 low (about -5%) and the day -15 bounce high (about +5.5%), with no clear higher low.
- **Weight:** 0.2.
- **Change of mind:** above +6% I would raise it; below -5% I would go to 0.

## 68d325d038 (BTC)
- **Read:** This is the lowest-volatility window. Price made a low at day -19 (about -10% from here) and has since put in higher lows. It is now pressing the day -35 high, about +1% away.
- **Weight:** 0.45. The base is constructive, but the trend has not yet confirmed.
- **Change of mind:** below -4% (the day -11 higher low) I would cut; a close above +1.5% I would raise.

## 4e17da2ed9 (SOL)
- **Read:** V-shaped recovery from the day -43 low, now about +30% above it. Price peaked at day -17 (about +8% from here) and is pulling back in an orderly way. The recent low is about -2%.
- **Weight:** 0.65. The trend has turned up, and this is a pullback within it.
- **Change of mind:** below -3% I would drop toward 0.3; above +8% I would raise.

## 5842416c1e (AVAX)
- **Read:** Heavy damage: down about 40% at the day -30 low. The rebound stalled at day -15 (about +7% from here), and price is fading back toward the day -8 low (about -1%). The structure is still lower highs.
- **Weight:** 0.2.
- **Change of mind:** above +7% I would add; below -2% I would go to 0.

## 61cf0d588c (ADA)
- **Read:** A blow-off rally at days -18 to -15 (about +30%) has since retraced roughly half. The prior trend was a steep downtrend, and volatility is very high. The spike high is about +15% from here, and the recent low (day -6) is about -6%.
- **Weight:** 0.3. There is some reversal evidence, but price is unstable.
- **Change of mind:** below -6% I would go to 0.1; above +10% I would raise.

## e561e138d1 (DOT)
- **Read:** Persistent downtrend. Price is about 2% above the window low and has had four down closes into day 0 with rising volume. The earlier spikes all faded.
- **Levels:** Swing high about +7.5% (day -13).
- **Weight:** 0.05.
- **Change of mind:** a close above +8%.

## 2c53641d6a (ETH)
- **Read:** Double bottom near the day -44 and day -24 lows. Price has recovered about 20% since then and set a post-crash high at day -4, about +2.4% from here. Support is about -4% (day -8) and -7% (day -11).
- **Weight:** 0.75. The structure is higher highs and higher lows.
- **Change of mind:** below -7% I would cut to about 0.3.

## 66a33fdd18 (LINK)
- **Read:** Same pattern as 2c53641d6a (ETH): a double bottom about 15% below here and a breakout at day -5. Price is consolidating just under the high, about +1.7% away. Support is about -5%.
- **Weight:** 0.7.
- **Change of mind:** below -6% I would cut.

## 38d7e95a3a (LTC)
- **Read:** Price is about 16% above the day -26 low. Day -1 rose +4.1% on above-average volume and made a new high since day -44. Higher lows have been in place since day -26. Support is about -3% (the day -15 high) and about -7% (day -7).
- **Weight:** 0.7.
- **Change of mind:** below -7% I would cut toward 0.3.

{"2cd2e372ac (DOGE)": 0.1, "a23c7f9cf5 (XRP)": 0.2, "68d325d038 (BTC)": 0.45, "4e17da2ed9 (SOL)": 0.65, "5842416c1e (AVAX)": 0.2, "61cf0d588c (ADA)": 0.3, "e561e138d1 (DOT)": 0.05, "2c53641d6a (ETH)": 0.75, "66a33fdd18 (LINK)": 0.7, "38d7e95a3a (LTC)": 0.7}

## Entscheidung 2026-07-26

## Strategy

I use a trend-and-structure rule. For each window I take the 60-day and 20-day cumulative return and check where the last close sits between the post-crash low (around day −51 to −28) and the recent swing high. A window gets a larger weight only if it has recovered most of its day −54 to −51 crash, is putting in higher lows, and has a positive 20-day return.

All ten windows sit inside a 180-day downtrend with two capitulation legs, so no window gets more than 0.6. Windows still deep in the hole get 0.1 to 0.2.

## 3c7d513db6 (ADA)
- **Read:** 60-day return is about −30%. The day −25 to −22 rally (+30%) has been fully given back, and the last 20 days are −9.5%. There are lower highs and the swing high is about +10% above. Day 0 volume is very thin (0.24) on a small up day, which is not a reversal signal.
- **Weight:** 0.1. The trend is down and there is no structure to lean on.
- **Change my mind:** a close of +10% or more above the last close (back above the day −22 high area).

## 84fedcd49b (BTC)
- **Read:** this is a low-volatility version of the same tape. 60-day return is about −12%, it is up about 10% off the day −28 low, and the last 20 days are +2%. The range is roughly −4% to +2% around the current price.
- **Weight:** 0.3. It is stabilizing but there is no confirmed uptrend yet.
- **Change my mind:** above +3% I would raise toward 0.5; below −5% I would cut to 0.1.

## 10de2ed3f5 (AVAX)
- **Read:** 60-day return is about −26%, with a low of about −41% at day −37 and a partial recovery. The last 20 days are −2%. Day −1 was a +7.5% spike on 1.5× volume after a −5.4% day, and day 0 gave back a little. The structure is choppy.
- **Weight:** 0.2. One spike day inside a downtrend is not enough.
- **Change my mind:** a hold above +5% (follow-through on the spike) would raise it; −6% (undoing the spike) would cut it to 0.

## 24c7360575 (LINK)
- **Read:** the 60-day return is about flat (−1%) after recovering roughly 21% from the day −26 low. The last 20 days are +10%, and there have been higher lows since day −18. Day 0 was +5.3%, at or near a 60-day closing high, but on low volume (0.41).
- **Weight:** 0.6. This is among the cleanest recoveries in the set, capped because of the broader downtrend and the thin breakout volume.
- **Change my mind:** −6% (losing the breakout and the day −3/−2 lows).

## 5fccb25e72 (DOGE)
- **Read:** 60-day return is about −29%, with a lower low at day −26 and only a feeble bounce. The last 20 days are −4%. The day −3 drop of −5.2% on 1.0× volume was only partly recovered.
- **Weight:** 0.15.
- **Change my mind:** +8% (above the day −23 high).

## cfbd2e2284 (DOT)
- **Read:** this is the weakest window. 60-day return is about −37%, with lower lows into day −28 and the last 20 days at −6%. The day −16 spike of +6.2% faded.
- **Weight:** 0.1.
- **Change my mind:** +10% or more.

## ba87bdab9a (LTC)
- **Read:** 60-day return is about −7%, up roughly 16% off the day −31 low, and the last 20 days are +6.5%. It shows higher lows and steady accumulation, with volume around 1.1 to 1.3 on up days near day −11 to −8. Day 0 was +2.7%, near the top of the recent range.
- **Weight:** 0.55. It is an orderly recovery with constructive structure.
- **Change my mind:** −5% (back below the day −14/−13 base).

## a965ca73f5 (SOL)
- **Read:** this window recovered fully from its crash. The 60-day return peaked at about +2% around day −23 and is now about −5%, roughly 7% below that peak, with a pullback and higher-low base. Day 0 was +3% on low volume.
- **Weight:** 0.5.
- **Change my mind:** +7% (a retake of the peak) would raise it to about 0.7; −6% would cut it to 0.2.

## 28fe57d029 (ETH)
- **Read:** 60-day return is about −1%, up roughly 23% off the day −31 low, and the last 20 days are +8.7%. It has higher lows, and day 0 was +4.3%, a new closing high for the recovery leg.
- **Weight:** 0.6.
- **Change my mind:** −6% (back under the day −3 to −1 lows).

## 26c148b80c (XRP)
- **Read:** 60-day return is about −15%, with a low of about −22% around day −26. The last 20 days are −3%, and the price is mid-range with no clear direction. Day 0 was +1.4% on very low volume (0.22).
- **Weight:** 0.3.
- **Change my mind:** above +5% I would raise to 0.5; −5% would cut it to 0.1.

{"3c7d513db6 (ADA)": 0.1, "84fedcd49b (BTC)": 0.3, "10de2ed3f5 (AVAX)": 0.2, "24c7360575 (LINK)": 0.6, "5fccb25e72 (DOGE)": 0.15, "cfbd2e2284 (DOT)": 0.1, "ba87bdab9a (LTC)": 0.55, "a965ca73f5 (SOL)": 0.5, "28fe57d029 (ETH)": 0.6, "26c148b80c (XRP)": 0.3}

## Entscheidung 2026-08-02

1. **Strategy.** I hold a base weight of about 0.4. I raise it when price has recovered most of the large crash around day -60 and the recent trend is up, especially on rising volume. I lower it when the rebound since the crash has failed, the lows keep getting lower, or the price action is directionless chop. Levels below are approximate cumulative moves from the last close, from summing the daily returns by hand.

## 8126a2088e (ADA)
- **Read:** There was a crash of about 32% (days -61 to -58), then a sharp rally on days -32 to -29 of about +30%. That gave back about 9%, and the last four days rose about +16%. Day 0 was +8.7% on 1.73× volume, which looks like a breakout to the post-crash high.
- **Structure:** Support from the day -6 swing low is about -14%. The post-crash high is roughly where price is now.
- **Weight:** 0.6. Momentum and volume support it, but the asset is very volatile and day 0 is extended.
- **Change of mind:** A drop of about -8% (giving back day 0 and more) cuts it to 0.3.

## c1105576a4 (LTC)
- **Read:** A crash of about 20%, then a steady low-volatility recovery that peaked around day -15, about 14% above the low. Since then it has drifted down about 5%. Volume is fading (0.37 on day 0).
- **Structure:** Support is about -4% (the day -40 swing area). The recent high is about +5%.
- **Weight:** 0.4. The recovery is intact but the near-term trend is soft.
- **Change of mind:** Below -4% goes to 0.2. Above +5% goes to 0.6.

## a245deaaff (LINK)
- **Read:** A crash of about 20%, then a recovery of about +15% net. A higher low formed around day -33, and the high was around day -11. Price has consolidated about 4% below that high, on very light volume.
- **Structure:** Support is about -6%. Resistance is about +4%.
- **Weight:** 0.55. The uptrend structure holds and the pullback has been orderly.
- **Change of mind:** Below -6% goes to 0.25. Above +4% goes to 0.75.

## 657006f270 (ETH)
- **Read:** A crash of about 24%, then a recovery of about +20%, with a higher low around day -36. The high was around day -11, and price is now about 3–4% below it. The shape is similar to a245, with quiet volume.
- **Structure:** Support is about -6%. Resistance is about +3.5%.
- **Weight:** 0.55.
- **Change of mind:** Below -6% goes to 0.25. Above +4% goes to 0.75.

## 0c2e686fcb (BTC)
- **Read:** A crash of about 19% on a low-volatility asset. The recovery has been only about +5% net, so price is still about 14% below the pre-crash level. It has drifted down about 4% over the last 10 days.
- **Structure:** Support is about -5%. Resistance is about +4%.
- **Weight:** 0.4. The recovery is weak, but there is no breakdown.
- **Change of mind:** Below -5% goes to 0.2. Above +4% goes to 0.55.

## 7adfc14c5c (SOL)
- **Read:** A crash of about 27%, then a strong rebound peaking near day -31, about 29% above the low. Since then price has faded about 9% as volume dried up, so momentum is rolling over.
- **Structure:** Support is about -6% (the day -25 to -20 lows). Resistance is about +9%.
- **Weight:** 0.4.
- **Change of mind:** Below -6% goes to 0.2. Above +5% goes to 0.6.

## af7149d5b7 (XRP)
- **Read:** A crash of about 19%, and price is essentially flat since then (about +1%). Two rally attempts both faded, and the last 10 days were about -5%. Price is still about 19% below the pre-crash level.
- **Structure:** Support is about -4%. Resistance is about +5%.
- **Weight:** 0.3. There is no recovery and the trend is weak.
- **Change of mind:** Above +5% goes to 0.5. Below -4% goes to 0.15.

## 39b077302b (DOGE)
- **Read:** A crash of about 21%. A brief bounce failed, and a new lower low around day -33 put price about 11% below the crash low. The bounce from there was small, and price is now about -13% net since the crash. The structure is a downtrend with lower highs.
- **Structure:** Support is the day -33 low, about -2%. Resistance is about +5%.
- **Weight:** 0.15.
- **Change of mind:** Above +5% goes to 0.4. Below -3% goes to 0.05.

## 88c735d396 (AVAX)
- **Read:** A crash of about 28%, then a second shock on days -45 and -44 (about -13%, volume 3.3×). The rebound after that has been very choppy, with swings of 5–7% (days -10, -8, -6, -1, 0). Price is about flat net since the crash.
- **Structure:** Support is about -6%. Resistance is about +3%.
- **Weight:** 0.25. The action is volatile and directionless.
- **Change of mind:** Above +5% goes to 0.45. Below -6% goes to 0.1.

## c29381db2b (DOT)
- **Read:** A crash of about 22%, then a failed bounce that made lower lows around day -36 (about 15% below the crash level). There was an -8.3% shock on day -6, followed by a +5% bounce over the last two days. Price is still near the lows.
- **Structure:** Support is about -4%. Resistance is about +6%.
- **Weight:** 0.15.
- **Change of mind:** Above +6% goes to 0.4. Below -4% goes to 0.05.

{"8126a2088e (ADA)": 0.6, "c1105576a4 (LTC)": 0.4, "a245deaaff (LINK)": 0.55, "657006f270 (ETH)": 0.55, "0c2e686fcb (BTC)": 0.4, "7adfc14c5c (SOL)": 0.4, "af7149d5b7 (XRP)": 0.3, "39b077302b (DOGE)": 0.15, "88c735d396 (AVAX)": 0.25, "c29381db2b (DOT)": 0.15}

## Entscheidung 2026-08-09

**Strategy.** I add up daily returns over three spans: the last 20 days, days -59 to -20, and the sharp sell-off around days -69 to -60 that appears in every window. Weight is high when the asset has recovered most of that sell-off and the last month is holding up. Weight is low when the trend since the sell-off is flat or falling and recent closes keep fading. I cap weights near 0.6 when daily ranges are wide, and keep a small floor rather than going fully flat.

## 2f9928f2c4 (XRP)
- **Read:** The sell-off cost about -18%. Days -59 to -20 added only about +2%, and the last 20 days lost about -7%, with a run of lower closes.
- **Weight:** 0.15. Volume is very light, so I see no sign of buyers returning.
- **Key levels:** About +4% to +5% would recover the level from roughly 10 days ago.
- **Change my mind:** Above +5%, I would raise the weight. Below -4%, I would cut it to 0.

## 5bd0fe8127 (SOL)
- **Read:** The sell-off cost about -25%. Since then the asset has gained roughly +20%, so it has recovered most of the drop. The last 20 days were flat, about -2%, but the last two days added about +3.5%.
- **Weight:** 0.6. The structure is higher lows, and daily ranges are narrowing.
- **Key levels:** Support is about -5% (the lows of the last 20 days).
- **Change my mind:** A close below -5%.

## 04d41301a9 (DOT)
- **Read:** The asset has fallen for a long time. The sell-off cost about -25%, days -59 to -20 lost about -9%, and day -13 alone was -8%. A +13% bounce faded, and the last four days were all down.
- **Weight:** 0.05.
- **Key levels:** Resistance is about +8% (the day -5 high).
- **Change my mind:** A close above +8%.

## a9f4477d5e (LINK)
- **Read:** The sell-off cost about -18%. Days -59 to -20 recovered about +14%, but the last 20 days gave back about -4%. The market is ranging, with mixed signals.
- **Weight:** 0.4.
- **Key levels:** The range runs from about -4% to +5%.
- **Change my mind:** A close above +5% would push me to 0.6. A close below -4% would cut me to 0.15.

## 322d332683 (LTC)
- **Read:** The sell-off cost about -21%. The rebound since then is about +13%. The last 20 days were about -4%, but the asset has drifted up over the last six sessions. Daily ranges are low.
- **Weight:** 0.45.
- **Key levels:** Support is about -4%.
- **Change my mind:** A close below -4% would cut me to 0.15. A close above +4% would raise me to 0.6.

## 8f630f4aa1 (AVAX)
- **Read:** This window had the deepest sell-off, about -33%. The recovery is only about +5%. Price action is very choppy, and the last 20 days were about -2%.
- **Weight:** 0.15. The asset is still well below where it was before the sell-off.
- **Key levels:** The range runs from about -6% to +6%.
- **Change my mind:** A close above +6%.

## 53c8691b6f (ETH)
- **Read:** The sell-off cost about -20%. The recovery is about +17%, and the last 20 days held flat, about +0.6%. Ranges and volume are extremely compressed, with day -1 range at 0.8%, which looks like consolidation inside an uptrend.
- **Weight:** 0.6.
- **Key levels:** Support is about -4%.
- **Change my mind:** A close below -4%.

## 65223d95e8 (ADA)
- **Read:** The sell-off cost about -36%. Since then the asset has made a strong recovery, about +23% over 60 days. The last three weeks gained about +15%, with up days on high volume.
- **Weight:** 0.55. The last three days were soft, and volatility is high.
- **Key levels:** Support is about -6% (the day -8 area).
- **Change my mind:** A close below -6%.

## d6753de99f (DOGE)
- **Read:** The sell-off cost about -18%, and there was no recovery: days -59 to -20 lost about -13%, and the last 20 days lost about -4%. The asset is grinding lower on low volume.
- **Weight:** 0.1.
- **Key levels:** Resistance is about +4%.
- **Change my mind:** A close above +4%.

## df75e251b7 (BTC)
- **Read:** The sell-off cost about -17%. The recovery is only partial, about +6%, and the last 20 days were flat. Volatility is low and the asset is moving sideways.
- **Weight:** 0.35.
- **Key levels:** The range runs from about -3% to +3%.
- **Change my mind:** A close above +3% would raise me to 0.55. A close below -3% would cut me to 0.15.

{"2f9928f2c4 (XRP)": 0.15, "5bd0fe8127 (SOL)": 0.6, "04d41301a9 (DOT)": 0.05, "a9f4477d5e (LINK)": 0.4, "322d332683 (LTC)": 0.45, "8f630f4aa1 (AVAX)": 0.15, "53c8691b6f (ETH)": 0.6, "65223d95e8 (ADA)": 0.55, "d6753de99f (DOGE)": 0.1, "df75e251b7 (BTC)": 0.35}

## Entscheidung 2026-08-16

**Strategy:** I add up daily returns to approximate the price path over the last ~20, ~60 and ~75 days. From that I judge trend structure (higher or lower swing lows), where the price sits within the post-crash range, and whether volume confirms the moves. Weight is high only when there is a clear uptrend or a confirmed breakout. Persistent downtrends get near zero, and range-bound or coiling windows sit in between. All levels below are approximate % moves from the last close.

## f03159f5be (AVAX)
- **Read:** A large crash of about -26% between days -76 and -60, with no real recovery since. Days -60 to -20 drifted to about -3%. The last 20 days are flat to slightly down (~-1%), with choppy, volatile swings.
- **Levels:** The range high is about +7% (the -22/-12 swing area). The range low is about -6%.
- **Weight 0.15:** The trend is down, there is no reclaim of the crash, and volatility is high.
- **Change my mind:** A close above +8% would mean a range breakout. A close below -7% confirms continuation lower.

## 1c0af62b79 (DOT)
- **Read:** A steady sequence of lower lows. It is about -27% over the last 60 days, on top of a ~-25% crash around day -75. A short rally from -15 to -12 (~+12%) has been fully given back. The last 9 days drifted lower on dying volume.
- **Weight 0.05:** This is a clean downtrend with no base.
- **Change my mind:** A close above +9% (the -12 high).

## 7d119ffbbd (DOGE)
- **Read:** About -20% over the last 60 days, with a series of lower highs. The last 20 days are flat inside a tightening range, and volume and range are both extremely compressed (v ~0.2). Resistance is about +4%, support about -4%.
- **Weight 0.1:** The price is coiling, but the coil sits inside a downtrend, so the break is more likely lower.
- **Change my mind:** A close above +5%, with volume expanding.

## 480f4eff40 (LINK)
- **Read:** Higher lows since day -48. The price is up roughly 28% from that low and has largely retraced the crash. The last week rallied about +14% on rising volume (1.5–1.65x), which looks like a breakout to new range highs. Day 0 is a small pullback.
- **Weight 0.7:** This is the only window with an uptrend confirmed by volume.
- **Change my mind:** A close below -7% (giving back the breakout, back under the -4/-3 area) would cut it to a low weight.

## 56f90534fb (XRP)
- **Read:** A lower high at -26, followed by a grind down of about -11% over 20 days. It is near or below the -52 low, about -19% over 60 days. Ranges are small, but the direction is persistently down.
- **Weight 0.05:** This is a downtrend that is making new lows.
- **Change my mind:** A close above +6% (reclaiming the -26 high area).

## 44db11a56d (SOL)
- **Read:** The strongest post-crash rebound in the set, at about +17%. A peak around day -45 was followed by a gentle range with lower highs. The price is now about -9% from that peak and about +10% above the -52 low. The last 20 days are flat, with very low volume and narrow ranges.
- **Weight 0.35:** A neutral range, with a modest lean positive given its relative resilience.
- **Change my mind:** A close above +5% (range top) would raise the weight. A close below -6% would cut it.

## 7e56b65ca2 (BTC)
- **Read:** A low-volatility asset. It fell about -21% in the crash and has recovered only about +8%. Since then it has moved sideways between roughly -5% and +5% around the current price, and is drifting slightly lower over the last 20 days. Volume and range are compressed.
- **Weight 0.3:** A range with no trend in either direction.
- **Change my mind:** A close above +4% would raise the weight. A close below -4% would cut it.

## 0b4d965597 (ETH)
- **Read:** A higher-low structure, up about +19% from the day -52 low. It has been consolidating about 4% below the recent highs (days -26 and -21). Volume is very low and ranges are extremely tight (0.6–1.2%), which looks like a coil within an uptrend.
- **Weight 0.45:** The bias is constructive, but there is no breakout yet.
- **Change my mind:** A close above +4% (new high) would raise the weight toward 0.7. A close below -5% would cut it.

## 108b068218 (LTC)
- **Read:** A range between the -53 low (about -8%) and the -21 high (about +7.5%). It is drifting lower over the last 20 days (about -4%) and sits in the lower-middle of the range.
- **Weight 0.3:** Neutral, with a slight downward drift.
- **Change my mind:** A close above +5% would raise the weight. A close below -7% would cut it.

## b1a5461466 (ADA)
- **Read:** A pump-and-fade asset. A spike around day -44 was fully faded. A second spike, from day -20 to -10, added about +30%, followed by 9 straight down days (about -14% from the peak) on light volume. The swing lows are higher (-18% → -8% relative to the -60 level), so the current pullback could be a bull flag or another full fade.
- **Levels:** Support is about -12% (the base before the pump). Resistance is about +15% (the spike high).
- **Weight 0.3:** The structure is ambiguous and the price is very volatile.
- **Change my mind:** Two up days on volume above 1, or a close above +6%, would raise the weight. A close below -10% would take it to 0.

{"f03159f5be (AVAX)": 0.15, "1c0af62b79 (DOT)": 0.05, "7d119ffbbd (DOGE)": 0.1, "480f4eff40 (LINK)": 0.7, "56f90534fb (XRP)": 0.05, "44db11a56d (SOL)": 0.35, "7e56b65ca2 (BTC)": 0.3, "0b4d965597 (ETH)": 0.45, "108b068218 (LTC)": 0.3, "b1a5461466 (ADA)": 0.3}

## Entscheidung 2026-08-23

**Strategy.** Every window has the same setup. Months of grinding drift and a sharp capitulation leg around days -82 to -79 led into a quiet, low-volume base. That base broke with a near-vertical 3-day rally, and day -1 printed a very wide-range, high-volume bar. I treat that as a fresh momentum breakout worth owning, but only partially, because it is extremely extended and the day -1 bar may be a blow-off. Weights run 0.2 to 0.5, higher when price is closing at or near the rally high and lower when it is already giving back. I cut to 0 if price loses roughly half the rally, and add if it closes clearly above the rally high.

## 6b3f190c8d (DOT)
- **Market:** A long downtrend with failed bounces, then a tight, low-volume base from about day -18 to -5. The rally from day -4 is about +23%. Day -1 had a 14% range on 2.6x volume and closed -2.1%, and day 0 was an inside bar at +0.9%. Price is 1.2% under the rally high, and the pre-rally base is about -19%.
- **Weight: 0.35.** The breakout is valid, but day -1 shows supply and price has not reclaimed the high.
- **Change my mind:** At -9% (half the rally lost) I go to 0. At +4% (a new high) I raise to about 0.6.

## 682b981fd4 (XRP)
- **Market:** The same long base with very compressed ranges. The rally is the strongest of the set at about +52%. Day -1 had a 22% range on 6x volume and still closed green, and day 0 added +4% on 2.6x volume. Price is closing at the rally high, and the base is about -34%.
- **Weight: 0.5.** Demand absorbed the climax bar, so momentum is the best here. The move is very stretched, which caps the size.
- **Change my mind:** At -13% I go to 0. Holding above the high (+3%) moves me to 0.7.

## 499a12d051 (SOL)
- **Market:** A choppy decline, then a base. The rally is about +24%, with day -1 at a 16% range closing flat and day 0 at +1.7% on falling volume. Price is closing at the high, and the base is about -19%.
- **Weight: 0.45.** The trend is orderly and the highs are holding.
- **Change my mind:** At -9% I go to 0. At +4% I raise.

## dbee1db741 (ADA)
- **Market:** A deep capitulation near day -80 and a spike rally at days -53 to -50 that fully faded. The current rally is about +30%. Day -1 had a 21.6% range on 3x volume and closed -1.4%, and day 0 was flat. Price is 1% under the high, and the base is about -23%.
- **Weight: 0.35.** This asset has already failed one spike in the window, so I discount this breakout.
- **Change my mind:** At -11% I go to 0. At +4% I raise to 0.55.

## 2062b84299 (LINK)
- **Market:** The base was already rising from day -12 with volume pickup. The rally is about +21%, but there are two red days in a row: day -1 at -2.9% on a 14% range, and day 0 at -0.9% on 1.8x volume. Price is 3.8% under the high, and the base is about -17%.
- **Weight: 0.2.** Follow-through is fading with distribution volume.
- **Change my mind:** At -7% I go to 0. A recovery of +5% back above the high moves me to 0.45.

## d5ba01ff56 (AVAX)
- **Market:** A choppy, volatile base with repeated failed pops. The rally is about +20%. Day -1 had a 16.8% range and closed -4.4%, a clear rejection, and day 0 bounced +1.5%. Price is 3% under the high, and the base is about -17%.
- **Weight: 0.25.** There was rejection at the high and this asset has a history of failed breakouts.
- **Change my mind:** At -7% I go to 0. At +4% I raise to 0.45.

## 7cb75039a2 (LTC)
- **Market:** The lowest-volatility asset of the set, with a mild drift down and a tight base. The rally is about +18%, mostly on day -2. Day -1 closed -1.4% on 3.2x volume, and day 0 was -0.3%. Price is 1.7% under the high, and the base is about -15%.
- **Weight: 0.25.** The high-volume stall right after a one-day thrust is weak follow-through.
- **Change my mind:** At -7% I go to 0. At +3% I raise to 0.45.

## fc9395f2d5 (BTC)
- **Market:** A steadier asset with a gentle drift and a very quiet base. It rallied about +20% over three steady days. Day -1 was a small, contained pullback (3% range, normal volume), and day 0 was +0.9%. Price is 0.7% under the high, and the base is about -17%.
- **Weight: 0.45.** This is the cleanest structure: no climax bar and an orderly consolidation.
- **Change my mind:** At -8% I go to 0. At +2% (a new high) I raise to 0.65.

## 645fe865b6 (ETH)
- **Market:** The base was very tight, with ranges below 1% around days -15 to -7. The rally is about +29%, led by a +17.5% gap-like day -4. Day -1 closed -3.7%, and day 0 bounced +1.7%. Price is 2.1% under the high, and the base is about -22%.
- **Weight: 0.35.** The thrust is strong and the pullback is shallow so far.
- **Change my mind:** At -10% I go to 0. At +3% I raise to 0.55.

## 2bdc1424ae (DOGE)
- **Market:** A drift lower, then a very quiet base (volume 0.2 to 0.4x). The rally is about +33%. Day -1 had a 19% range on 3.5x volume and closed green, and day 0 added +1.7%. Price is closing at the high, and the base is about -25%.
- **Weight: 0.45.** The climax bar was absorbed and price is still printing highs.
- **Change my mind:** At -11% I go to 0. At +4% I raise to 0.65.

{"6b3f190c8d (DOT)": 0.35, "682b981fd4 (XRP)": 0.5, "499a12d051 (SOL)": 0.45, "dbee1db741 (ADA)": 0.35, "2062b84299 (LINK)": 0.2, "d5ba01ff56 (AVAX)": 0.25, "7cb75039a2 (LTC)": 0.25, "fc9395f2d5 (BTC)": 0.45, "645fe865b6 (ETH)": 0.35, "2bdc1424ae (DOGE)": 0.45}

## Entscheidung 2026-08-30

1. **Strategy**

I compound the daily returns to rebuild the recent path: the pre-surge base, the 3-day surge from day -11 to -9, the post-surge peak, and the current distance from both. Weight rises with how much of the breakout is still held, how tight the pullback is, and whether the trend before the surge was up. A surge that has mostly been given back on falling volume, inside a longer downtrend, gets a low weight. All windows share the same pattern (a crash near day -88, a quiet base, a violent surge, then a fade), so the differences come from retention and how orderly the pullback is.

2. **Windows**

## 148f0bcbe6 (DOGE)
- **Read:** The longer trend is down. The crash near day -88 cost about 20%, then the price drifted about 13% lower into day -12.
- **Surge and fade:** The surge added about 33% to a peak at day -7. The price is now about 12% below that peak, with lower highs and a -3.8% close on day 0.
- **Key levels:** The pre-surge base is about 15% below; the peak is about 14% above.
- **Weight:** 0.2. The breakout is fading, but about +17% of it is still held.
- **Change my mind:** A gain of 8% or more (reclaiming the day -3 high) would make me add. A fall of 8% would take me flat.

## 5cd2f5e445 (DOT)
- **Read:** The longer trend is down. After the day -88 crash the price kept bleeding, with only a short rally from day -29 to -26.
- **Surge and fade:** The surge added about 25%. The price is now 13% below the peak, so only about 9% of the surge is retained.
- **Key levels:** The base is about 8% below.
- **Weight:** 0.1. Most of the breakout has been given back.
- **Change my mind:** A gain of 10% or more would make me add. A fall of 6% (back into the base) would take me flat.

## 597d661ed1 (ETH)
- **Read:** The price recovered after the day -86 crash, then rose with higher lows from day -60 to -40. A very tight base followed (daily ranges of 1–2%), then a +17.5% breakout day on 2.7× volume.
- **Surge and fade:** The surge added about 31%. The price is only about 4% below the peak and is consolidating sideways.
- **Key levels:** The peak is about 4% above. Support is near day -8's close, about 3% below.
- **Weight:** 0.7. This is the cleanest breakout-and-hold.
- **Change my mind:** A fall of 8% or more would cut it to about 0.3. A gain of 5% (a new high) would take it to full.

## 0f4233f162 (XRP)
- **Read:** The price drifted slightly lower from day -40 to -12. The surge came on very heavy volume (4–6×).
- **Surge and fade:** The surge added about 45%, peaking at day -7. The price is now about 11% below that peak, but about 35% of the move is still held.
- **Key levels:** The peak is about 12% above. The day -9 close is about 4% below.
- **Weight:** 0.4. Retention is strong, but the pullback has a lower-high structure.
- **Change my mind:** A fall of 10% or more would take me to about 0.1. A gain of 8% would take me to about 0.7.

## bc7d14df60 (LINK)
- **Read:** The price had an uptrend from day -60, and from day -19 to -13 it had already risen about 15% before the surge.
- **Surge and fade:** The surge added about 26%. The price is now about 7% below the peak.
- **Key levels:** The peak is about 8% above. The day -4/-3 lows are about 3% below.
- **Weight:** 0.5. Higher lows are holding on the larger timeframe.
- **Change my mind:** A fall of 9% would take me to about 0.2. A gain of 6% would take me to about 0.8.

## ba3af08e56 (SOL)
- **Read:** The price rallied from day -65 to -59. After the surge it kept extending and made a new high at day -3 on 2× volume.
- **Surge and fade:** The total move from the base is about 40%. The price is now about 7% below the high and about 32% above the base.
- **Key levels:** The high is about 7% above. Support near day -5's close is about 6% below.
- **Weight:** 0.6. The momentum is the most persistent of the set.
- **Change my mind:** A fall of 8% or more would take me to about 0.25. A gain of 5% would take me to about 0.85.

## 15ef1babf7 (BTC)
- **Read:** This is a low-volatility asset. After the surge of about 21%, it made a slightly higher high at day -3.
- **Surge and fade:** The price is only about 3% below the peak. Day 0 fell 0.7% on light volume, which is an orderly pullback.
- **Key levels:** The peak is about 3% above. The day -8 low is about 3% below.
- **Weight:** 0.6.
- **Change my mind:** A fall of 5% or more would take me to about 0.25. A gain of 3% (a new high) would take me to about 0.85.

## edce249538 (AVAX)
- **Read:** The longer structure is choppy and high-volatility, and broadly flat to down after the crash.
- **Surge and fade:** The surge added about 24%. The price is now about 9% below the peak, holding about 12% of the move, with lower highs.
- **Key levels:** The base is about 11% below.
- **Weight:** 0.25.
- **Change my mind:** A fall of 7% would take me flat. A gain of 8% would take me to about 0.5.

## 17d9e38416 (ADA)
- **Read:** The price fell about 13% from day -22 to -12 before the surge.
- **Surge and fade:** The surge added about 31%. Since then there has been a sharp 16% fade with big down days (-5.6%, -5.0%, -4.5%), so only about 10% of the move is retained.
- **Key levels:** The base is about 9% below.
- **Weight:** 0.1. This is the weakest follow-through.
- **Change my mind:** A gain of 10% would take me to about 0.4. A fall of 8% would take me flat.

## 561524f97b (LTC)
- **Read:** The longer trend is flat to down.
- **Surge and fade:** The surge added about 20%. Since then the price has bled steadily, with 7 of the last 9 days down, and is now about 10% below the peak, holding only about 8% of the move.
- **Key levels:** The base is about 7% below.
- **Weight:** 0.15.
- **Change my mind:** A gain of 7% would take me to about 0.4. A fall of 6% would take me flat.

3. **Weights**

{"148f0bcbe6 (DOGE)": 0.2, "5cd2f5e445 (DOT)": 0.1, "597d661ed1 (ETH)": 0.7, "0f4233f162 (XRP)": 0.4, "bc7d14df60 (LINK)": 0.5, "ba3af08e56 (SOL)": 0.6, "15ef1babf7 (BTC)": 0.6, "edce249538 (AVAX)": 0.25, "17d9e38416 (ADA)": 0.1, "561524f97b (LTC)": 0.15}

## Entscheidung 2026-09-06

## Strategy

Every window gets the same test: trend over the last 20 to 60 sessions, where the last close sits against the post-breakout range, and whether volume confirms. The base is 0.5. Weight goes up when the close is at or near new highs after a held breakout with orderly pullbacks. It goes down when price is well off the highs, the action is messy, or the last days look stretched. I exit the long thesis on a close back inside the pre-breakout base, below the consolidation low.

All levels below are cumulative closes rebased to 1.00 at day -19, just before the breakout.

## 7dc64f3c61 (XRP)
- **Read:** A three-day breakout from -18 to -16 of about +45% on 4 to 6x volume, peaking at 1.52 on day -14.
  - It pulled back about 11% to 1.35 by day -4, then a +7.4% day carried it to 1.42 now.
  - The close is about 6% below the high. The consolidation low is about 5% below.
  - Before the breakout the trend drifted down.
- **Weight 0.6:** The breakout held but price has not reclaimed its high. Recent days are on light volume.
- **Change my mind:** A close below -6% (under the consolidation low), or above +7% (new high), which would raise the weight.

## 3b655f9e08 (DOT)
- **Read:** Breakout to 1.25, then a pullback to 1.09 (−13%) that fully retraced it.
- **Structure:** Seven straight up days to 1.30, a new high, finishing with +6.9% on 1.67x volume.
  - The longer history is weak: a downtrend from -174 to -19.
  - Support is at the old 1.25 high (about −4%) and the swing low at 1.09 (about −16%).
- **Weight 0.6:** Momentum is strong and it is a fresh high. But the run is extended after seven up days, and the longer trend is poor.
- **Change my mind:** A close back below about −5% (failed breakout).

## 75beee2513 (BTC)
- **Read:** The calmest window. A breakout of about +21%, then a very tight consolidation between 1.19 and 1.22. The +5.1% day at -3 made a new high near 1.26.
  - It now sits at 1.24, about 1% off the high.
  - Volatility is low and the longer-term trend is a gentle uptrend.
- **Weight 0.8:** A clean trend with orderly consolidation.
- **Change my mind:** A close below −4% (the 1.19 base).

## 05e4b970c1 (LINK)
- **Read:** The accumulation started before the breakout: about +14% from -26 to -22.
- **Breakout:** +26% to 1.26, then a mild pullback to 1.17.
- **Now:** It surged to 1.40, a new high, with +9.8% on 1.7x volume today.
  - Higher lows hold since day -60.
  - Support is about −9% at the old high zone (1.26).
- **Weight 0.75:** The strongest trend structure. I trim slightly from full because today's +9.8% bar is stretched.
- **Change my mind:** A close below −10% (back under the 1.26 breakout level).

## a4b0504c02 (SOL)
- **Read:** The breakout kept running to about 1.42 at day -10.
  - It pulled back about 8% to 1.30, then climbed to 1.38 now, about 3% below the high.
  - It is higher than the pullback low and today's volume is firm.
- **Weight 0.7:** The trend is intact and price is near its highs.
- **Change my mind:** A close below −6% (the 1.30 pullback low).

## 4d09410861 (ADA)
- **Read:** Very high volatility over the whole window.
  - A crash of about −33% from -96 to -93.
  - Two sharp rallies, each of which faded.
  - A +31% breakout to 1.31, a −12% pullback to about 1.15, and a rebound to 1.28 now, about 3% below the peak.
  - Daily ranges of 5 to 10% are routine.
- **Weight 0.55:** The direction is fine, but the risk per unit of trend is the worst here, and earlier rallies failed.
- **Change my mind:** A close below −10% (about 1.15). A close above +3% (new high) would raise the weight.

## d467059e5d (AVAX)
- **Read:** Breakout to 1.24, then a pullback of about −8% to 1.14. Today it closed at a new closing high of about 1.25 (+4.1%).
  - The pullback stayed moderate.
- **Weight 0.7:** It confirmed a new high.
- **Change my mind:** A close below −6% (about 1.17, back into the range).

## 64afc4f1a7 (LTC)
- **Read:** Breakout to 1.20, then a deeper drift of −10% to 1.08.
  - It recovered with a +7.7% day on 2.3x volume to 1.23, a new high, and held it today.
  - The asset has relatively low volatility, and the longer trend is mildly up.
- **Weight 0.7:** It made a new high with volume behind it.
- **Change my mind:** A close below −5% (back under 1.17).

## 462a23255b (DOGE)
- **Read:** Breakout to about 1.33, then a pullback of −13% to 1.16.
  - Two strong up days (+7.4% and +5.8%, the second with a 13% intraday range) brought it to 1.29, about 3% below the peak.
  - The action is choppy, with wide ranges.
- **Weight 0.6:** It is recovering, but has not made a new high, and the bars are erratic.
- **Change my mind:** A close below −7% (about 1.20). A close above +3% would raise the weight.

## c6e26358fc (ETH)
- **Read:** A +17.5% gap day started a +31% breakout. The consolidation was very shallow, holding between 1.25 and 1.31.
  - It is now at 1.31, matching the high.
- **Weight 0.75:** The breakout held tightly and the close is at the highs.
- **Change my mind:** A close below −5% (under the 1.25 range low).

{"7dc64f3c61 (XRP)": 0.6, "3b655f9e08 (DOT)": 0.6, "75beee2513 (BTC)": 0.8, "05e4b970c1 (LINK)": 0.75, "a4b0504c02 (SOL)": 0.7, "4d09410861 (ADA)": 0.55, "d467059e5d (AVAX)": 0.7, "64afc4f1a7 (LTC)": 0.7, "462a23255b (DOGE)": 0.6, "c6e26358fc (ETH)": 0.75}

## Entscheidung 2026-09-13

**Strategy:** I reward windows where the price holds or extends a large recent upside break (here, a three-day gap of about 20–45% around day −25) and stays near its post-break highs on calm volume. I scale down windows where the gains are being given back, there was a blow-off spike, or volatility is rising into the decision day. Levels are cumulative returns measured from the last close, approximated by summing daily returns.

**e428d4d640 (DOGE)**
- **Read:** Before the break, a long downtrend with a capitulation around day −100. The break (~+31%) was followed by choppy distribution. Price is about 9% below the day −7 high and about 10% below the post-break close. The break base sits roughly 15–18% below.
- **Weight:** 0.4. Most of the gap is held, but highs are getting lower and the last four days are weak.
- **Change of mind:** above +6% (reclaim the high), I'd add; below −8% (gap fill starts), I'd cut to 0.

**d166a797eb (LTC)**
- **Read:** A ~+19% break that has fully held. Price dipped about 10% and then recovered, and the last close is about 2–3% under the post-break high. Day 0 was flat on normal volume.
- **Weight:** 0.7. This is the cleanest hold of the break, with higher lows since day −14.
- **Change of mind:** below −8% (the day −14 low), I'd cut.

**81c199ff44 (ETH)**
- **Read:** A ~+31% break followed by a tight 5% flag just under the post-break high. Ranges and volume are contracting, and price is about 2% below the high.
- **Weight:** 0.65. This is a constructive bull flag.
- **Change of mind:** below −4.5% (the flag low), I'd cut.

**17177b4952 (SOL)**
- **Read:** A ~+22% break that extended another ~15% to day −17, then pulled back about 8%. Price is still about 7% above the post-break level. The trend is the strongest of the group.
- **Weight:** 0.6. The trend is intact, and the pullback has come on light volume.
- **Change of mind:** below −7% (the post-break level), I'd cut.

**f353d069fb (DOT)**
- **Read:** A long prior downtrend, then the break. That was followed by a parabolic run of +7%, +9% and +17% on 4× volume into day −5. The reversal since then is about −20% over five straight down days.
- **Weight:** 0.2. This is a blow-off top under active distribution.
- **Change of mind:** above +10%, I'd reconsider. Below −10%, I'd cut to 0.

**26488fc5cb (ADA)**
- **Read:** A ~+31% break with very volatile chop since. The −17% swing was followed by a recovery, and price is now again about 10% below the post-break close. Earlier rallies in this window also faded.
- **Weight:** 0.4. The gap is held, but the tape is noisy and failing.
- **Change of mind:** above +10%, I'd add. Below −7% (the day −14 low), I'd cut.

**2ba79c3e05 (BTC)**
- **Read:** A ~+21% break, followed by a tight ±3% range with very low ranges. Price is about 1.5% below the post-break close and about 5% below the day −10 high.
- **Weight:** 0.65. It is a quiet, orderly hold.
- **Change of mind:** below −4%, I'd cut.

**0362733415 (XRP)**
- **Read:** The largest break, ~+46% on 4–6× volume. The fade since then is about 11% from the day −21 high, but most of the gain is retained.
- **Weight:** 0.5. The break is strong, but the drift is still lower.
- **Change of mind:** above +8%, I'd add. Below −8%, I'd cut.

**3fbffb0b83 (LINK)**
- **Read:** A pre-break uptrend, then a ~+26% break. A +10% spike at day −7 has been fully reversed, and price is about 15% off that spike and about 6% below the post-break close.
- **Weight:** 0.35. A failed breakout extension with lower lows.
- **Change of mind:** above +8%, I'd add. Below −5%, I'd cut.

**b9c85c830b (AVAX)**
- **Read:** A ~+24% break with an immediate −4% reversal the next day. Price rallied to day −6 and has now fallen about 10%, back near the post-break lows (about −3% further down).
- **Weight:** 0.4. Support is being tested.
- **Change of mind:** below −4% (support fails), I'd cut. Above +7%, I'd add.

{"e428d4d640 (DOGE)": 0.4, "d166a797eb (LTC)": 0.7, "81c199ff44 (ETH)": 0.65, "17177b4952 (SOL)": 0.6, "f353d069fb (DOT)": 0.2, "26488fc5cb (ADA)": 0.4, "2ba79c3e05 (BTC)": 0.65, "0362733415 (XRP)": 0.5, "3fbffb0b83 (LINK)": 0.35, "b9c85c830b (AVAX)": 0.4}

## Entscheidung 2026-09-20

## Strategy

I follow the trend. I sum the daily returns to rebuild the price path, then check where the last close sits against its recent range: above or near a breakout high is bullish, back inside or below the base is not. I start long when price holds near its highs and then scale down for three things: distance below the recent peak, choppy high-volatility structure, and parabolic, climax-volume moves where a sharp reversal is likely.

Every window has the same broad shape. There was a crash around day −110 to −105, then a recovery, then a quiet, low-volume base from about −50 to −33. Around −32 to −30 came a high-volume breakout of roughly 20–40%, followed by a choppy consolidation and a sharp up-day at −2. The levels below are approximate % distances from the last close.

## 33c8a02ddd (LTC)
- **Read:** Breakout of about +19% at −32/−30, then a pullback of about −10% into the consolidation. The rally resumed at −17/−15 and again at −3/−2 (+4.4, +7.8). The last close is at a new high for the advance.
- **Structure:** Higher lows. Support is about −10% (the −5 low) and about −14% (the −21 low).
- **Weight:** 0.8. The trend is intact, price is at highs, and the −2 thrust came on solid volume.
- **Change my mind:** A drop of about −10% or more, back below the −5 swing low.

## b5368b08b5 (ETH)
- **Read:** +17.5% gap at −32 on 2.8x volume, then +8%. The consolidation held tightly within about 10% of the highs. The +6.7% day at −2 took price to new highs, about +37% over the base.
- **Structure:** Support is about −8% (the −5 low).
- **Weight:** 0.8. Clean breakout and a tight flag that resolved upward.
- **Change my mind:** A drop of about −9% or more, below the −5 low.

## bf91ff5a40 (LINK)
- **Read:** An early lead-in rally at −40/−36, then a breakout of about +24% at −32/−30. A second leg peaked at −14 (+9.8%). From there price fell about −14% into −5 and has since rebounded about +13%. The close is about 4% below the −14 peak.
- **Structure:** Range from about −13% (the −5 low) to +4% (the −14 high).
- **Weight:** 0.7. Uptrend intact, but the peak hasn't been reclaimed yet and swings are wide.
- **Change my mind:** A drop of about −12%, below the −5 low. A move of about +5% to new highs would take me to 0.85.

## 4ccd59ef56 (SOL)
- **Read:** Breakout of about +20% at −32/−30 that kept extending to −24 (about +36%). It consolidated between about −10% and 0% of that level. A +10.9% thrust at −2 made a new high, and price is holding there.
- **Structure:** Support is about −13% (the −5 low).
- **Weight:** 0.8. New highs with persistent buying.
- **Change my mind:** A drop of about −12%, back into the consolidation lows.

## f7e25b39c0 (AVAX)
- **Read:** Breakout of about +22% at −32/−30, then a range of about 13–25% for three weeks. The last three days are parabolic: +7.8, +23.0, +12.1, on 2.5x, 3.9x and 6.1x volume. Day 0's range was 20%.
- **Structure:** This is climax behaviour. The prior range top sits about −30% below the close.
- **Weight:** 0.5. Momentum is extreme, but a blow-off on exhausted volume often retraces hard. I hold half.
- **Change my mind:** A drop of about −15% (a failed breakout day) and I go to 0. If price holds within about 5% for a week and volume calms, I raise the weight.

## 1e18e9a273 (XRP)
- **Read:** Huge breakout of about +40% at −32/−30 on up to 5.9x volume, peaking around −28. Since then the market has chopped sideways between about −10% and +5% of the current level, including a −9.8% day at −5. Price recovered at −2 (+7.7). The close is about 5% under the peak.
- **Structure:** Range of about −9% to +5%.
- **Weight:** 0.6. Price holds the breakout, but there is no follow-through after a month and volatility is high.
- **Change my mind:** A drop of about −10%, below the −5 low. A move above about +6% (a new high) would take me to 0.8.

## 556f1f0ea1 (ADA)
- **Read:** The most volatile window. The crash at −110/−107 was about −37%, followed by strong rallies at −81/−78 and −54/−45. Price faded at −43/−33, then broke out about +29% at −32/−30. It retraced about −17% by −21, recovered, dipped about −16% at −5, and has now returned to the highs on a +10.8% day.
- **Structure:** Range of about −16% to 0%, with the close at the top.
- **Weight:** 0.7. Constructive, but swings are wide.
- **Change my mind:** A drop of about −13%, below the −5 low.

## e447d5baf2 (DOT)
- **Read:** Breakout of about +23% at −32/−30, then a pullback to about +10%. A second leg went vertical at −14/−12 (+6.9, +8.6, +17.2 on 4x volume) and reversed by about −20% into −5. Price has since bounced about +19%. The close is about 7% below the −12 spike high.
- **Structure:** Overhead supply sits at about +8%. Support is about −17%.
- **Weight:** 0.55. The trend is up, but blow-off-and-reversal behaviour and 9% daily ranges argue for caution.
- **Change my mind:** A drop of about −10% (failure of the bounce). A move of about +8%, reclaiming the spike high, would take me to 0.75.

## 0e91d37b9b (DOGE)
- **Read:** Breakout of about +28% at −32/−30, then a choppy range of about +15% to +30% relative to the base. The close is about 5% below the −30 high. The +7% day at −2 faded slightly on day 0.
- **Structure:** Range from about −8% (the −5 low) to +5%.
- **Weight:** 0.6. The breakout holds, but price is going sideways with lower highs since −30.
- **Change my mind:** A drop of about −9%, below the −5 low. A move of about +6% to new highs would take me to 0.8.

## 95baf5b570 (BTC)
- **Read:** The lowest-volatility window. A three-day breakout of about +20% at −32/−30 was followed by a tight 17–24% range. The +5.8% day at −2 made a marginal new high, and the last two days are quiet with small ranges.
- **Structure:** Support is about −6% (the −5 low).
- **Weight:** 0.85. A clean uptrend at highs with low volatility gives the best risk/reward.
- **Change my mind:** A drop of about −6%, below the −5 low.

{"33c8a02ddd (LTC)": 0.8, "b5368b08b5 (ETH)": 0.8, "bf91ff5a40 (LINK)": 0.7, "4ccd59ef56 (SOL)": 0.8, "f7e25b39c0 (AVAX)": 0.5, "1e18e9a273 (XRP)": 0.6, "556f1f0ea1 (ADA)": 0.7, "e447d5baf2 (DOT)": 0.55, "0e91d37b9b (DOGE)": 0.6, "95baf5b570 (BTC)": 0.85}

## Entscheidung 2026-09-27

# E-005 position weights

## Strategy

I go long when the window shows a clear uptrend: the last close is near the 180-day highs after higher-low impulse legs, and selloffs get bought back. I size down when the latest leg is parabolic or a single climactic volume spike, because the reversal risk is higher there. I cut to flat or near-flat if the market closes below the base of the last impulse leg, since that would mean the breakout failed.

All levels below are rough mental compounding of the daily returns, as % from the last close.

## 191dac6f9b (AVAX)

- **Trend:**
  - It crashed around day -117 to -114 and chopped for months.
  - A first impulse came at days -39 to -37, about +23%.
  - It then ranged for about 30 days.
  - From day -10 it went vertical: about +50% in three days (-9 to -7, with +23% on 3.7x volume and 5.7x the next day).
  - A -9% shakeout at day -4 was absorbed, and the last 3 days closed green with ranges still about 6% and volume about 1.8x.
- **Key levels:**
  - The spike high is roughly +3 to +5% above the last close.
  - The day -4 low is about -10%.
  - The base before the spike is about -40%.
- **Weight: 0.55.** The trend is strong and the shakeout was bought, but this is a parabolic blow-off with climactic volume, so the position is reduced.
- **Change my mind:** a close below about -11% (under the shakeout low).

## 6e945fc4e5 (LINK)

- **Trend:**
  - Breakout at days -39 to -37 (about +25%).
  - A pullback of about -15% into day -12.
  - A new leg from day -11 of about +25%, made of steady gains rather than one spike.
  - Day -4 (-5%) was fully recovered by days -3 and -2.
- **Key levels:** the close is about at the window high, and the day -4 low is about -11%.
- **Weight: 0.75.** It is a clean staircase uptrend at new highs.
- **Change my mind:** a close below about -10%.

## 85c6bcd9af (SOL)

- **Trend:**
  - Days -39 to -31 rallied about +40%, then it corrected about -12%.
  - From day -11 it rallied about +23%, with the day -9 +11% on 2x volume.
  - The last few days are a tight hold with low ranges.
- **Key levels:** the high is about +0 to 2%, the day -4 pullback low is about -6%, and the day -12 base is about -22%.
- **Weight: 0.75.** It is a higher-low trend holding near the highs on quiet volume.
- **Change my mind:** a close below about -8%.

## b855b6f1d5 (DOGE)

- **Trend:**
  - Days -39 to -37 rallied about +30% on heavy volume.
  - A correction followed.
  - Day -6 jumped +14% on 3.8x volume, and day -4 gave back -7.7%.
  - Days -3 and -2 recovered, day -1 dipped -2.3%, and day 0 was flat.
- **Key levels:** the day -6 to -5 high is about +2 to 4%, the day -4 low is about -8%, and the base before day -9 is about -22%.
- **Weight: 0.6.** The uptrend is intact, but the spike was partly retraced and the follow-through is modest.
- **Change my mind:** a close below about -8%.

## 9ab6cc2aab (DOT)

- **Trend:**
  - It ran +22% at days -39 to -37, then had a blow-off at days -21 to -19 (+35%).
  - It then corrected about -20%.
  - From day -11 a strong new leg added about +35%, including the day -4 -9.6% flush, which was recovered within 2 days.
  - It closed up 4 days in a row on 1.4 to 2x volume.
- **Key levels:** the close is at or just above the prior day -19 high. The day -4 low is about -12%, and the day -12 low is about -30%.
- **Weight: 0.7.** It made a higher high after a higher low, and demand is persistent.
- **Change my mind:** a close below about -12%.

## 9d30a77bc3 (XRP)

- **Trend:**
  - Days -39 to -36 were an explosive +46% on 3.5 to 5.5x volume.
  - It then gave back about -15% over 25 days, including a -9.8% day at -12.
  - A new leg from day -10 added about +20%.
  - The last 2 days were down (-2.6%, -0.7%) as volume cooled to about 1.1x.
- **Key levels:** the high is about +3%, the day -4 low is about -7%, and the day -10 base is about -20%.
- **Weight: 0.6.** The uptrend is valid, but the momentum is fading slightly at the top.
- **Change my mind:** a close below about -8%.

## ac339c8912 (BTC)

- **Trend:**
  - This is a low-volatility asset.
  - Days -39 to -37 gained +21%, followed by a sideways range.
  - Steps of +5.8% at day -9 and +6.7% at day -6 broke it out.
  - For the last 5 days it has held flat, with ranges contracting to 0.8 to 1.2% on low volume.
- **Key levels:** the close is at the highs, the day -4 low is about -3%, and the breakout base is about -12%.
- **Weight: 0.75.** It is a textbook tight flag above the breakout.
- **Change my mind:** a close below about -4%.

## a0fa124f6a (ETH)

- **Trend:**
  - Day -39 was +17.5% on 2.8x volume, and days -39 to -37 totaled +30%.
  - A shallow pullback followed.
  - Days -9 to -6 added about +13%.
  - It is now flat, with ranges 1.2 to 2% and volume at 0.3 to 0.5x.
- **Key levels:** the close is at the highs, the day -4 low is about -4%, and the day -12 base is about -15%.
- **Weight: 0.75.** It is in a low-volatility consolidation at the highs after higher-low legs.
- **Change my mind:** a close below about -5%.

## ea90be915b (ADA)

- **Trend:**
  - This is a high-volatility asset.
  - Days -39 to -37 added +31%, then it corrected about -15%.
  - From day -11 it rallied about +25% (the day -9 +10.8% and day -6 +7.5%).
  - The day -4 drop of -6.3% was recovered, and it is now holding with smaller ranges.
- **Key levels:** the high is about +2%, the day -4 low is about -9%, and the day -12 base is about -25%.
- **Weight: 0.65.** The trend is intact, sized for the high volatility.
- **Change my mind:** a close below about -10%.

## 59f1a6055a (LTC)

- **Trend:**
  - Days -39 to -37 rallied about +20%, then it ranged.
  - From day -10 a steady leg added about +20%.
  - Day -3 was a +16% gap or spike, with a 21% range on 6.7x volume.
  - It held for 2 days, then day 0 fell -1.8%.
- **Key levels:** the spike high is about +4%, the close before the spike is about -15%, and the day -4 low is about -17%.
- **Weight: 0.55.** This is an event-driven spike on climactic volume, with unfilled air below it, so the risk of a retrace into the gap is meaningful.
- **Change my mind:** a close below about -8% (half the spike day erased).

{"191dac6f9b (AVAX)": 0.55, "6e945fc4e5 (LINK)": 0.75, "85c6bcd9af (SOL)": 0.75, "b855b6f1d5 (DOGE)": 0.6, "9ab6cc2aab (DOT)": 0.7, "9d30a77bc3 (XRP)": 0.6, "ac339c8912 (BTC)": 0.75, "a0fa124f6a (ETH)": 0.75, "ea90be915b (ADA)": 0.65, "59f1a6055a (LTC)": 0.55}
