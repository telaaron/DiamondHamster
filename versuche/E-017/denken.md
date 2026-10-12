# E-017: was die KI gedacht hat (Set A)

Volle Antwort des Deciders pro Entscheidungswoche, unverändert. Er sah weder Datum noch Coin-Namen; die Namen in Klammern sind erst danach eingesetzt. Gesendeter Prompt und Daten: runs/<set>/<woche>/requests.json.

## Entscheidung 2026-07-05

## Strategy

The weekly level sets the direction. I raise the weight only on a confirmed state change: a sustained break above the falling long average or the old pre-crash range, with 2-, 4- and 8-week returns all agreeing. Volatility controls size. A rebound inside a falling regime gets a below-middle weight and no chasing. A sharp one-week spike is treated as a reversal candidate, not as momentum.

All ten windows share the same shape:
- a crash around day −150;
- a range;
- a rally that peaks around day −56;
- a fade, then a second crash around day −30;
- a 2–4 week rebound back to 100.

The 8-week return is negative and the 2- and 4-week returns are positive, so momentum is mixed. That is a possible turning point, not a trend state. Price is still below a falling 100–200 day average, and volatility is elevated after the crash. Weight goes to the reduced side of the middle, scaled by how stretched the rebound is.

## d8c14090d2 (ETH)
- **Read:** Downtrend from about 180. The pre-crash range was 113–135, the crash low was 84.7 and price has rebounded to 100. Resistance is about 103.6 (day −20 high), then 112–119.
- **Weight:** 0.3. This is a rebound below a falling long average with mixed momentum.
- **Change of mind:** Weekly closes above about 113 would raise the weight. A close below about 86 would lower it.

## e986524e05 (LTC)
- **Read:** Same pattern. Lows are 85.7, recent highs about 101. The old range at 113–123 sits above as resistance.
- **Weight:** 0.3. Mixed momentum and a downtrend regime.
- **Change of mind:** Above about 114 on weekly closes I would raise it. Below about 86 I would cut it.

## 00deb6e1f1 (DOT)
- **Read:** This one has the steepest decline, from 150–160 (day −56) down to 90.2. The rebound to 100 is still well below the day −20 high of 118.8, with lower highs throughout.
- **Weight:** 0.25. The downtrend is the clearest of the ten.
- **Change of mind:** A hold above about 119 would raise it. Below about 90 I would cut it.

## 5dcca012ce (LINK)
- **Read:** The low is 86.9 and resistance is 106.7 (day −20). The old range at 112–118 is above.
- **Weight:** 0.3. Rebound inside a falling regime.
- **Change of mind:** Weekly closes above about 112 would raise it. Below about 87 would lower it.

## a2588cc759 (DOGE)
- **Read:** Price fell from 145–150 to 89.3. Resistance is 116.8–118.7, and the long average is falling.
- **Weight:** 0.3. Mixed momentum.
- **Change of mind:** Above about 119 I would raise it. Below about 89 I would cut it.

## cf579d5b2e (AVAX)
- **Read:** The low is 82 (day −16), followed by higher lows at 86 and 92. Price is at 100, near the recent high of 102.8. The old range at 128–140 is far above.
- **Weight:** 0.3. The short-term structure is improving, but the weekly regime is still down.
- **Change of mind:** Above about 110 on weekly closes would raise it. Below about 91 would lower it.

## 6ab679b55c (SOL)
- **Read:** Lows are 73.7 then 78.5, a higher low. Price is 100, above the day −20 swing high of 93.3, so short-term HH/HL is in place. It is back inside the old pre-crash range of 100–110. The 8-week return (from 118) is still negative.
- **Weight:** 0.35. This has the best structure of the set, but the weeks do not yet confirm it.
- **Change of mind:** Weekly closes above about 110 would raise it. Below about 88 would cut it.

## d32656b352 (ADA)
- **Read:** Price went from 76 to 101 in four days on heavy volume. That is an extreme single week (z well above 2) with no confirmation from the longer windows. The pre-crash range at 122–133 is far above, and the low is 72.9.
- **Weight:** 0.2. The spike is a reversal candidate and volatility is high.
- **Change of mind:** Holding above about 100 for two or more weekly closes and then breaking about 105 would raise it. Below about 85 would lower it.

## bef5cb21e8 (BTC)
- **Read:** Lower volatility than the others. Price fell from 129 to a low of 90.8 and rebounded to 100. Resistance is 105.7, then the old range at 115–122.
- **Weight:** 0.3. Mixed momentum.
- **Change of mind:** Above about 115 I would raise it. Below about 91 I would cut it.

## a918394cde (XRP)
- **Read:** The low is 87.2 and resistance is 111.8 (day −20 spike high). The old range at 114–125 is above.
- **Weight:** 0.3. Rebound inside a downtrend.
- **Change of mind:** Weekly closes above about 112 would raise it. Below about 87 would lower it.

{"d8c14090d2 (ETH)": 0.3, "e986524e05 (LTC)": 0.3, "00deb6e1f1 (DOT)": 0.25, "5dcca012ce (LINK)": 0.3, "a2588cc759 (DOGE)": 0.3, "cf579d5b2e (AVAX)": 0.3, "6ab679b55c (SOL)": 0.35, "d32656b352 (ADA)": 0.2, "bef5cb21e8 (BTC)": 0.3, "a918394cde (XRP)": 0.3}

## Entscheidung 2026-07-12

**Strategy:** Direction comes from the weekly level. I compare 2-, 4- and 8-week momentum and check where price sits against the long (100–180 day) average and its slope. Every window here shows the same pattern: a long, falling trend; a crash leg about 40 days ago; and then a 4–5 week base around 100. A price below a falling long average with negative 8-week momentum is a downtrend regime, so the weight is reduced. A short recovery without the weekly line turning only gets slightly more weight, never a jump to the extreme. Volatility after the crash is still elevated, which also argues for a smaller size.

**2c315436e1 (DOT)**
- **Market read:** Steady downtrend from about 270 to 100. Price fell from about 150 (day −45) to 100, and lows keep getting lower (95 at day −16).
- **Momentum:** 2 weeks slightly positive, 4 and 8 weeks clearly negative.
- **Levels:** Resistance at 106–107, support at 95.
- **Weight:** 0.15, for a downtrend regime with no turn.
- **Change of mind:** Weekly closes above about 112.

**230dd5dff2 (ADA)**
- **Market read:** Crash down to 86, then a spike to 123 (day −8) that was given back almost entirely.
- **Momentum:** 2 weeks +13%, 4 and 8 weeks negative. That mix is a rally inside a downtrend.
- **Levels:** Support at 86–88, resistance at 118–123.
- **Weight:** 0.2.
- **Change of mind:** Weekly closes above 118 raise the weight. A close below 86 takes it to 0.1.

**3666cb2716 (ETH)**
- **Market read:** Low at 83.7. Recovery to about 100, a little higher lows.
- **Momentum:** 2 weeks +15%, 4 weeks +5%, 8 weeks −15%. Momentum is contradictory and the long average is falling.
- **Levels:** Support at 84–87, resistance at 102.
- **Weight:** 0.25, a middle-to-low weight because the timeframes disagree.
- **Change of mind:** Closes above about 103 sustained over weeks, or a break below 84.

**94610a1c0b (AVAX)**
- **Market read:** Sell-off down to 88.7 (day −23), then a rebound to 111, and price is falling back again.
- **Momentum:** 2 weeks flat, 4 and 8 weeks negative.
- **Levels:** Resistance at 108–111, support at 89–93.
- **Weight:** 0.15.
- **Change of mind:** Weekly closes above about 111.

**323f44270e (SOL)**
- **Market read:** Lows at 78 and then 83 form a higher low. The high at 109 (day −8) is above the previous 99.
- **Momentum:** 2 and 4 weeks +8%, 8 weeks negative.
- **Structure:** An early HH/HL pattern, but it sits under a falling long average.
- **Weight:** 0.3.
- **Change of mind:** Closes above 110 would justify a higher weight. A close below 83 means 0.15.

**4506103096 (BTC)**
- **Market read:** Slowest-moving asset of the group, at about 100 after a fall from 150.
- **Momentum:** 2 weeks +7%, 4 weeks −3%, 8 weeks −18%.
- **Levels:** Support at 91, resistance at 104–105.
- **Weight:** 0.2.
- **Change of mind:** Weekly closes above 105.

**59137a8806 (DOGE)**
- **Market read:** Clearly falling: 8 weeks from about 150 down to 100, 4 weeks from 122 down to 100. The highs are getting lower (127, then 109).
- **Volume:** Very thin.
- **Weight:** 0.15, for a downtrend regime.
- **Change of mind:** Closes above about 110. A break below 95 would be a further, but small, reduction.

**8795cbf22e (LINK)**
- **Market read:** Lows at 87.5 and 87.7, so a double bottom has not been confirmed. Recovery to 100.
- **Momentum:** 2 weeks +10%, 4 weeks about flat, 8 weeks negative.
- **Levels:** Neckline at about 102–103, support at 87.5.
- **Weight:** 0.2.
- **Change of mind:** Weekly closes above about 103 sustained over weeks (a confirmed bottom) mean 0.35. A close below 87 means 0.1.

**f9ca1894c8 (XRP)**
- **Market read:** Lower highs at 119, then 109, and now 100. The low was 93.
- **Momentum:** 4 and 8 weeks negative.
- **Levels:** Resistance at 109, support at 93.
- **Weight:** 0.15.
- **Change of mind:** Weekly closes above 110.

**f469f5d3c0 (LTC)**
- **Market read:** Fall from about 130 to a low of 89. Sideways around 95–105, with a high at 105.
- **Momentum:** 2 weeks slightly positive, 4 and 8 weeks negative.
- **Levels:** Support at 89, resistance at 105.
- **Weight:** 0.2.
- **Change of mind:** Weekly closes above 106.

```json
{"2c315436e1 (DOT)": 0.15, "230dd5dff2 (ADA)": 0.2, "3666cb2716 (ETH)": 0.25, "94610a1c0b (AVAX)": 0.15, "323f44270e (SOL)": 0.3, "4506103096 (BTC)": 0.2, "59137a8806 (DOGE)": 0.15, "8795cbf22e (LINK)": 0.2, "f9ca1894c8 (XRP)": 0.15, "f469f5d3c0 (LTC)": 0.2}
```

## Entscheidung 2026-07-19

**Strategy:** The weekly regime sets direction. That means the sign agreement of 2-, 4- and 8-week returns, plus where price sits against the falling long average of roughly 100 to 140 days. A full downtrend (all signs negative, price under a falling long MA) gets a low weight of about 0.1–0.15. Mixed signals (short-term positive, long-term negative) get a reduced middle weight of about 0.2–0.3, never a jump to full long. Position in the range, single big days and short-term rebounds are not signals, and I would raise weight only after weekly closes back above the range top following the crash around day −44.

## 443f4c18e3 (DOT)
- **Trend:** A clean downtrend from about 238 to 100.
- **Momentum:** 2W −7%, 4W −13%, 8W −34%, all negative.
- **Structure:** Lower highs at 127.7, 110.7 and 109.1. Price sits on the low of the 98–110 range, under a falling long MA of about 130.
- **Volatility:** Elevated since the crash.
- **Weight: 0.10.** This is a confirmed downtrend.
- **Change of mind:** Weekly closes above about 111.

## b43d54fc14 (BTC)
- **Momentum:** 2W +2%, 4W +2%, 8W −16%, so mixed.
- **Structure:** A flat range of 89.8–102.5 since day −44, under a falling long MA of about 108.
- **Signal:** Low volume, no breakout, so there is no signal.
- **Weight: 0.25.**
- **Change of mind:** Raise on weekly closes above about 103. Cut to 0.1 below about 89.

## 26b8c31ebc (LINK)
- **Momentum:** 2W +4%, 4W +8%, 8W −11%, so mixed.
- **Structure:** A higher low at 83.6 (day −24) versus 83.4 (day −43), which is essentially a double bottom. The range is 83.5–103 and price is in its upper half.
- **Trend:** The long MA of about 105 is still falling.
- **Weight: 0.30.**
- **Change of mind:** Raise on closes above about 103.5. Cut below about 85.

## 7359ba37ee (ETH)
- **Momentum:** 2W +5%, 4W +10%, 8W −11%, so mixed.
- **Structure:** A recovery from the 80.4–81.9 lows to 100. The high at 104 (day −4) was not held, and the long MA of about 108 is falling.
- **Weight: 0.30.**
- **Change of mind:** Raise on weekly closes above about 104. Cut below about 90.

## e1aeb18c4e (LTC)
- **Momentum:** 2W +3%, 4W +6%, 8W −11%, so mixed.
- **Structure:** The last close of 100 is slightly above the highs of the past 6 weeks (about 98.5). This is a breakout that is not yet confirmed, and it came with no volume increase. The long MA of about 108 is still falling.
- **Weight: 0.30.**
- **Change of mind:** Raise if two weekly closes hold above about 101.5. Cut on a close back below about 92.

## 79e2c8d8c5 (XRP)
- **Momentum:** 2W −5%, 4W −2%, 8W −19%. All negative, but the short-term readings are small.
- **Structure:** The bounce failed at 107.9 and price has drifted lower in the 92–108 range. The long MA of about 118 is falling.
- **Weight: 0.15.**
- **Change of mind:** Weekly closes above about 108.

## 98c1bb8cb9 (ADA)
- **Momentum:** 2W −12%, 4W +6%, 8W −31%.
- **Structure:** The spike to 120.3 (day −15) collapsed back to 100. It was a failed breakout, a single extreme week that was not held.
- **Volatility:** High.
- **Weight: 0.15.**
- **Change of mind:** Raise on weekly closes above about 116. Cut toward 0.05 below about 83.

## a0fb85a525 (SOL)
- **Momentum:** 2W −6%, 4W +5%, 8W −10%, so mixed.
- **Structure:** A rebound from 78.7 to 110 is fading. It still shows higher lows (83.8 at day −24, 96.1 recently), but price sits under a falling long MA of about 108.
- **Weight: 0.25.**
- **Change of mind:** Raise above about 110. Cut below about 96.

## 83206bedaf (AVAX)
- **Momentum:** 2W −7%, 4W +6%, 8W −30%, so mixed with a heavy long-term negative.
- **Structure:** A range of 88–110, rolling over from 110, under a falling long MA of about 130.
- **Weight: 0.20.**
- **Change of mind:** Raise above about 110.5. Cut below about 96.

## 188373570e (DOGE)
- **Momentum:** 2W −7%, 4W −12%, 8W −29%, all negative.
- **Structure:** Lower highs at 127.7, 117.5 and 109.6. Price is at the bottom of the 96–110 range, under a falling long MA of about 125.
- **Weight: 0.10.**
- **Change of mind:** Weekly closes above about 110.

```json
{"443f4c18e3 (DOT)": 0.10, "b43d54fc14 (BTC)": 0.25, "26b8c31ebc (LINK)": 0.30, "7359ba37ee (ETH)": 0.30, "e1aeb18c4e (LTC)": 0.30, "79e2c8d8c5 (XRP)": 0.15, "98c1bb8cb9 (ADA)": 0.15, "a0fb85a525 (SOL)": 0.25, "83206bedaf (AVAX)": 0.20, "188373570e (DOGE)": 0.10}
```

## Entscheidung 2026-07-26

## 1. Strategy

Direction comes from the weekly level. I treat 2-, 4- and 8-week returns with the same sign as a trend state. I treat "price below a falling 100–180-day average for several weekly closes" as a down-regime, which justifies a reduced weight. Recoveries inside a down-regime only allow gradual increases, and range position and single big days are ignored. With volatility now well below the crash period, it does not trigger extra cuts.

## 2. Windows

The same pattern appears in every window:
- **Crash** around day −171.
- **Range**, with a rally into roughly days −80 to −75.
- **Second leg down** around day −54 to −51.
- **Bottoming** around day −30.

So the long average is falling and price sits below it. Momentum is mixed in all of them: 2- and 4-week returns are positive, 8-week returns are negative. None of them is in a clean trend state, so weights stay below the middle and are graded by how far each rebound has progressed.

**6eda03c302 (DOGE)**
- **Read:** 2W +0.9%, 4W +0.2%, 8W −27%. Flat base between 94 and 106 below a falling long average (about 120+). It dipped to 92.9 three days ago and recovered. No trend; down-regime intact.
- **Weight:** 0.25
- **Change my mind:** weekly closes above 108 would raise the weight; a close below 92 would cut it further.

**4952e56f60 (BTC)**
- **Read:** 2W +2.6%, 4W +9.8%, 8W −11%. Higher lows (89.6 → 94.5 → 97.5); price is capped near 102. This is a rebound inside a down-regime, with the long average around 108 and falling.
- **Weight:** 0.35
- **Change my mind:** weekly closes above 103 would raise it; below 94 would lower it.

**413cd707be (ADA)**
- **Read:** 4W +15%, but the spike to 115.8 (day −22) failed back into a 95–105 range. 8W is −30%, and price is far below a falling average.
- **Weight:** 0.3
- **Change my mind:** a weekly close above 109; below 93 would lower it.

**2df4767e60 (LTC)**
- **Read:** 2W +8.7%, 4W +12.5%, 8W −8.6%. Steady higher lows; the close of 100 is at the post-crash high (about 100.1–100.9). The long average is around 108–110 and falling.
- **Weight:** 0.4
- **Change my mind:** weekly closes held above 102 would raise it; below 95 would lower it.

**730ab8ca91 (ETH)**
- **Read:** 2W +8%, 4W +24%, 8W −2.6%, so the 8-week sign is close to flipping. Recovery from 77 to 100 with higher lows, testing the 99.6–100.6 highs.
- **Weight:** 0.4
- **Change my mind:** weekly closes above 103 would confirm the recovery; below 94 would weaken it.

**70a1cdbabc (SOL)**
- **Read:** 2W −0.2%, 4W +7.5%, 8W −7%. The rebound peaked at 109 (day −23) and is now drifting sideways between 95 and 103. Short and long momentum disagree.
- **Weight:** 0.3
- **Change my mind:** above 105 would raise it; below 95 would lower it.

**f1337a0eec (DOT)**
- **Read:** 2W −1.9%, 4W +2.2%, 8W −30%. Sideways between 95 and 108 after a deep decline, with the average far above.
- **Weight:** 0.25
- **Change my mind:** weekly closes above 108 would raise it; below 95 would lower it.

**0474958fb5 (AVAX)**
- **Read:** 2W +5%, 4W +4.6%, 8W −25%. Choppy range between 91 and 105. The last day's +7.6% candle is noise, not a signal.
- **Weight:** 0.3
- **Change my mind:** weekly closes above 105 would raise it; below 91 would lower it.

**9458c41674 (LINK)**
- **Read:** 2W +10%, 4W +21%, 8W −3.6%. Higher lows (79 → 81 → 94); the close of 100 is above the recent high of 99.3. The long average is around 100 and only mildly falling. This is the closest of the ten to a regime turn.
- **Weight:** 0.45
- **Change my mind:** weekly closes above 104 (the pre-drop level) would raise it; below 93 would lower it.

**d21b69432f (XRP)**
- **Read:** 2W +2.6%, 4W +6.2%, 8W −16.5%. Range between 94 and 106 below a falling average, with no breakout.
- **Weight:** 0.3
- **Change my mind:** above 106 would raise it; below 93 would lower it.

## 3. Weights

{"6eda03c302 (DOGE)": 0.25, "4952e56f60 (BTC)": 0.35, "413cd707be (ADA)": 0.3, "2df4767e60 (LTC)": 0.4, "730ab8ca91 (ETH)": 0.4, "70a1cdbabc (SOL)": 0.3, "f1337a0eec (DOT)": 0.25, "0474958fb5 (AVAX)": 0.3, "9458c41674 (LINK)": 0.45, "d21b69432f (XRP)": 0.3}

## Entscheidung 2026-08-02

**Strategy:** Direction comes only from the weekly picture. I check the 2-, 4- and 8-week returns, and the position of price against the long averages of 100 to 180 days, which are falling in every window after the sell-off around day −60. If all momentum windows are negative and price sits below a falling long average, that is a downtrend regime and gets a reduced weight (about 0.2). If the momentum signals are mixed or the market is moving sideways, the weight stays in the middle-to-low range (0.3 to 0.45). Single strong days, range position and indicator distances do not change anything.

### 0c14e213fc (DOT)
- **Read:** Clean downtrend from about 190 down to 100.
  - 2-week return −2.5 %, 4-week −9 %, 8-week −18 %: all negative.
  - Price is far below the falling long average (about 140 to 150).
  - Lower highs at about 131, 112 and 108. Recent low 93.6.
  - The last two days are only a rebound inside a downtrend.
- **Weight 0.2:** Confirmed downtrend regime.
- **Change of mind:** Weekly closes above about 112 (last lower high), or a weekly close below 93 confirming further weakness.

### 21208dadc2 (SOL)
- **Read:** Crash to about 82, a rebound to 114 (day −30), then sliding back.
  - 2-week −3.6 %, 4-week −10 %, 8-week +11 %: mixed.
  - Price is below the falling long average (about 112).
  - Lows to watch: 99.7 and 95.9.
- **Weight 0.35:** Momentum contradicts itself, so the weight sits mid-to-low.
- **Change of mind:** Weekly close above about 114 (raise), or below about 95 (lower to about 0.2).

### 1b7a1b9355 (LINK)
- **Read:** Low at 83.6 on day −38, followed by a higher-low structure.
  - 2-week 0 %, 4-week +4 %, 8-week +6 %: weakly positive, z below 0.5, so no trend state.
  - Price is still below the long average (about 105).
  - Recent range is about 94 to 106.
- **Weight 0.4:** Sideways with a weak recovery.
- **Change of mind:** Weekly close above about 106 (raise toward 0.6), or below about 94 (cut to 0.25).

### 4334f389e7 (ADA)
- **Read:** Heavy decline from about 130 down to 73.
  - Spike to 105 on day −29, then it failed.
  - Today +8.7 % on high volume: a single extreme day, which counts as a reversal candidate rather than a signal.
  - 4-week return about 0 %, 8-week +15 %.
  - The long average is falling, at about 115.
- **Weight 0.35:** No trend state. I am not chasing the spike day.
- **Change of mind:** Weekly closes held above about 105 (raise), or a fall back below about 85 (cut).

### a60908cb8f (ETH)
- **Read:** Low at 80.2 on day −37, then higher lows at 90.9 and 96.6.
  - 2-week +0.7 %, 4-week +5.6 %, 8-week +11.5 %: all positive but weak, z_4W about 0.4.
  - Price is below the long average (about 108).
- **Weight 0.45:** Gentle recovery but no confirmed trend.
- **Change of mind:** Weekly close above about 105 (raise to about 0.6), or below 96 (lower to 0.3).

### fc25864ac6 (DOGE)
- **Read:** Downtrend.
  - 2-week −2 %, 4-week −9 %, 8-week −18 %: all negative.
  - Lower highs at about 130, 112 and 106. Price is far below the falling long average (about 130).
- **Weight 0.2:** Downtrend regime.
- **Change of mind:** Weekly close above about 106 to 110 (raise), or below 95.6 (stay low).

### 6e336f19e4 (AVAX)
- **Read:** Sideways range between about 87 and 108 since day −58, with many crossings.
  - 4-week −5 %, 8-week −4 %, 2-week +1 %.
  - The long average is falling, at about 125. Today's spike day is not a signal.
- **Weight 0.3:** Sideways under a downtrend regime.
- **Change of mind:** Weekly close above about 108 (raise), or below about 92 (cut).

### 408280d6a1 (LTC)
- **Read:** Low at 87.9 on day −38, a recovery to 108, and now a pullback.
  - 2-week −5 %, 4-week −2 %, 8-week +4 %: mixed.
  - The long average is falling, at about 115.
- **Weight 0.35:** Mixed signals, so the weight sits in the middle-low range.
- **Change of mind:** Weekly close above about 108 (raise), or below about 96 (cut).

### 9636c8da96 (XRP)
- **Read:** After the crash, the high at 119 failed, followed by a sideways-to-down drift.
  - 2-week −1 %, 4-week −6 %, 8-week −6 %: weak but uniformly negative.
  - Price is below the falling long average (about 118).
- **Weight 0.25:** Weak downtrend.
- **Change of mind:** Weekly close above about 107 (raise), or below about 93 (cut).

### a894fe13c3 (BTC)
- **Read:** Flat range of about 91 to 106 since day −58.
  - 2-, 4- and 8-week returns are all about 0 %, so this is a sideways regime.
  - Price is below the falling long average (about 110).
- **Weight 0.35:** Hold still because the market is sideways.
- **Change of mind:** Weekly close above about 106 (raise), or below about 93 (cut).

{"0c14e213fc (DOT)": 0.2, "21208dadc2 (SOL)": 0.35, "1b7a1b9355 (LINK)": 0.4, "4334f389e7 (ADA)": 0.35, "a60908cb8f (ETH)": 0.45, "fc25864ac6 (DOGE)": 0.2, "6e336f19e4 (AVAX)": 0.3, "408280d6a1 (LTC)": 0.35, "9636c8da96 (XRP)": 0.25, "a894fe13c3 (BTC)": 0.35}

## Entscheidung 2026-08-09

**Strategy:** Direction comes from the weekly view, using the 2-, 4- and 8-week returns, the slope of the long average (about 100 days) and the swing structure. The weight changes from a neutral 0.4–0.5 only when these agree. When they all point down below a falling long average, I reduce to about 0.2. When momentum is positive but sits under a falling long average (a rebound), I raise the weight only in steps. Mixed or sideways readings keep the weight in the middle, and position within a range is never a signal.

## 3437644ed3 (SOL)
- **Read:** The price was 105–127 before a crash on days −68 to −64 that bottomed near 79. It recovered to 110 by day −36, then drifted between 92 and 103. Returns: 2W ≈ 0 %, 4W ≈ −1 %, 8W ≈ +7 %, so momentum is mixed. The long average is around 103 and falling slightly, and volatility is low. This is a sideways regime.
- **Weight: 0.4.** There is no confirmed state, and the falling long average argues for a slight discount.
- **Change of mind:** Weekly closes above 108 would raise the weight. Closes below 92 would cut it to 0.25.

## dc1e6a4f24 (AVAX)
- **Read:** The price fell from 140–160 in a crash to 97, then made a further low at 88.5 on day −51. Since then it has ranged between 94 and 110. Returns: 2W −5 %, 4W ≈ 0, 8W −5 %. The long average is about 125 and falling, and the price sits well below it. This is a downtrend regime with a sideways base.
- **Weight: 0.3.**
- **Change of mind:** Weekly closes above 110 would raise the weight. A close below 94 would cut it to 0.2.

## 0c9a258e67 (DOT)
- **Read:** This is a persistent decline from about 200. Highs keep getting lower: 131 → 113 → 112 → 109. Lows are 100.6, then 93.6 on day −13. Returns: 2W −3.5 %, 4W −5 %, 8W −20 %. All three agree on a downtrend, and the long average is falling.
- **Weight: 0.2.**
- **Change of mind:** A weekly close above 110 would break the sequence of lower highs and justify going higher.

## 84dcb08d5c (XRP)
- **Read:** The price fell from 130–140 to a 102 crash low. The rebound high of 125.6 was followed by lower highs at 115 and 113, and a fresh low of 98.3 came on day −2. Returns: 2W −7.5 %, 4W −5 %, 8W −13 %. Momentum is aligned negative under a falling long average.
- **Weight: 0.2.**
- **Change of mind:** A weekly close above 111 would raise the weight.

## 4980158482 (DOGE)
- **Read:** The price fell from 140–170 to a 112 crash low. The rebound high of 133 was followed by lower highs at 114.5 and 108.7, with lows at 98–100. Returns: 2W −5.5 %, 4W −5 %, 8W −22 %. Momentum is aligned negative. Volatility is compressed, which says a bigger move is coming but not its direction.
- **Weight: 0.2.**
- **Change of mind:** A weekly close above 108 would raise the weight. A close below 97 would confirm the current low weight.

## 58e9a9c614 (LTC)
- **Read:** The price fell from 115–130 to an 86.5 crash low. Since then it has ranged between 95 and 106, with a top at 106.2 on day −14. Returns: 2W −5 %, 4W +3 %, 8W ≈ 0, so momentum is mixed. The long average is about 108 and falling. Trend efficiency is low, so this is sideways.
- **Weight: 0.4.**
- **Change of mind:** Weekly closes above 106 would raise the weight to 0.5. Closes below 94 would cut it to 0.25.

## 5b784f0a6d (ADA)
- **Read:** After the crash, lows came at 76, then 71 on day −45. A spike to 102.8 was followed by a pullback to 78.8. The price then rallied to 108.8 on day −3, a higher high above higher lows. Returns: 2W +17 %, 4W +20 %, 8W +6 %, all positive. However, the close of 100 is back below the old 103 high, so the breakout has not held. The long average is about 101 and falling, and volatility is high. This is a rebound inside a downtrend regime.
- **Weight: 0.5.** I am raising it one step, not to an extreme.
- **Change of mind:** Weekly closes above 104 would raise the weight to 0.65. A close below 89 would cut it to 0.3.

## 72246a0828 (LINK)
- **Read:** The price fell from 105–130 to an 85.5 crash low, retested it at 85.6, then recovered to 108 on day −14. Since then it has slipped to 100. Returns: 2W −7 %, 4W +2 %, 8W ≈ 0. This is a sideways range between 85 and 108, under a long average of about 106 that is falling slightly.
- **Weight: 0.4.**
- **Change of mind:** A weekly close above 108 would raise the weight. A close below 93 would cut it.

## 1576c1cdeb (BTC)
- **Read:** The price fell from 113–127 to a 91 crash low, then ranged between 89 and 103 with very low volatility. Returns: 2W −1 %, 4W +2 %, 8W −1 %. No trend state is present.
- **Weight: 0.4.**
- **Change of mind:** A weekly close above 103.5 would raise the weight. A close below 95 would cut it.

## 4abd4a5331 (ETH)
- **Read:** The price fell from 105–129 to a 78.8 crash low. Since then it has made higher lows (79 → 89.7 → 95.4) and higher highs (96.8 → 101.9 → 103.7). Returns: 2W −2 %, 4W +6 %, 8W +11 %. The long average is about 99 and flattening. The trend is recovering moderately, but it has not broken out of a range.
- **Weight: 0.5.**
- **Change of mind:** A weekly close above 104 would raise the weight to 0.6. A close below 95, which would break the higher-low sequence, would cut it to 0.35.

{"3437644ed3 (SOL)": 0.4, "dc1e6a4f24 (AVAX)": 0.3, "0c9a258e67 (DOT)": 0.2, "84dcb08d5c (XRP)": 0.2, "4980158482 (DOGE)": 0.2, "58e9a9c614 (LTC)": 0.4, "5b784f0a6d (ADA)": 0.5, "72246a0828 (LINK)": 0.4, "1576c1cdeb (BTC)": 0.4, "4abd4a5331 (ETH)": 0.5}

## Entscheidung 2026-08-16

**Strategy.** Direction comes only from the weekly level. A trend state requires the 2-, 4- and 8-week returns to share a sign, together with the position against a falling or rising long average (about 100 days). With a clear downtrend I hold a reduced 0.2–0.3. With a confirmed uptrend I hold about 0.6. Mixed or sideways windows stay near the middle at 0.35–0.45, discounted while price sits under a falling long average. Position in the range and single days or candles do not move the weight.

## 85e903ea76 (DOT)
- **Trend:** Persistent decline from about 219 to 100. The 2W, 4W and 8W returns are all negative (about −5%, −7%, −19%).
- **Structure:** Lower highs at 137, 119, 114.6 and 112.9. Price is far below a falling 100-day average of about 130.
- **Rally failure:** The rally from 100 to 113 (days −20 to −12) failed, and price is back at the 98.6–100 low.
- **Weight 0.2:** This is a clear downtrend regime.
- **Change my mind:** Weekly closes above 113.

## 0c1cf8495c (ADA)
- **Trend:** Crash from 135 to about 82 (day −50), then a recovery to 115 (day −10), now back at 100.
- **Momentum is mixed:** 2W about −8%, 4W about +5%, 8W about +12%.
- **Structure:** Higher lows at 79, 88 and 99.8. Price is still below a falling long average of about 120.
- **Weight 0.4:** Conflicting time frames call for a middle weight.
- **Change my mind:** A close below 88 means lower; weekly closes above 115 mean higher.

## 7c85cc1524 (LINK)
- **Trend:** Low of 74.7 (day −52), followed by a steady recovery.
- **Momentum:** 2W about +12%, 4W about +12%, 8W about +21%, all positive.
- **Structure:** Higher lows. Price broke out above the 95 range top, and the long average (about 93) is flattening, with price above it.
- **Caveat:** The last week alone was large (z about 2), so I take only a partial step.
- **Weight 0.6.**
- **Change my mind:** A close back below 93 (failed breakout).

## 2945ced6ee (AVAX)
- **Trend:** After the crash, a sideways range of 93–110 for about 50 days.
- **Momentum:** −3%, −2%, +3.5%, so no signal.
- **Long average:** About 125 and falling, above price.
- **Weight 0.35:** Sideways means hold still, with a slight discount for the falling long average.
- **Change my mind:** A close below 93 means lower; weekly closes above 110 mean higher.

## 20eb8250fe (SOL)
- **Trend:** Recovery to 110, then a range of 96–105.
- **Momentum:** +1%, −2%, +3%, mixed and flat. The long average of about 105–110 is falling.
- **Weight 0.4.**
- **Change my mind:** A close below 94.6 means lower; above 111 means higher.

## d099ef3f13 (LTC)
- **Trend:** Recovery from 89 to 108, now back at 100.
- **Momentum:** −1%, −6%, about 0. Mixed, and price is below the falling long average.
- **Weight 0.4.**
- **Change my mind:** Below 97 means lower; weekly closes above 108.5 mean higher.

## 970354f3fa (ETH)
- **Trend:** From the low of 80.6, price climbed to about 104, then went flat at 98–104 with compressed volatility.
- **Momentum:** −0.5%, +0.7%, +10%, so mixed.
- **Compression:** It signals a bigger coming move but gives no direction.
- **Weight 0.45.**
- **Change my mind:** A break below 97 means lower; weekly closes above 106 mean higher.

## a36ea00138 (XRP)
- **Trend:** Lower highs at 124.6, 119, 117, 115 and 112, now at 100.
- **Momentum:** 2W about −9%, 4W about −10%, 8W about −12%, all negative.
- **Long average:** Falling, around 125.
- **Weight 0.25:** This is a downtrend regime, with price testing the 99–101 lows.
- **Change my mind:** Weekly closes above 112.

## ee5812f0f4 (BTC)
- **Trend:** After the crash to 94, a flat range of about 99–106 for 6 weeks.
- **Momentum:** −1%, −3%, −0.7%, too small to be a trend state.
- **Long average:** Falling, around 115, above price.
- **Weight 0.4.**
- **Change my mind:** Below 97 means lower; weekly closes above 106.5 mean higher.

## aadd066216 (DOGE)
- **Trend:** Peak at 170, then a crash and a slide to about 100, followed by a 98–112 range on very low volume.
- **Momentum:** 2W −2%, 4W −4%, 8W −15%.
- **Long average:** About 130 and falling.
- **Weight 0.3:** This is a mild downtrend regime.
- **Change my mind:** Below 97 means lower; weekly closes above 112 mean higher.

{"85e903ea76 (DOT)": 0.2, "0c1cf8495c (ADA)": 0.4, "7c85cc1524 (LINK)": 0.6, "2945ced6ee (AVAX)": 0.35, "20eb8250fe (SOL)": 0.4, "d099ef3f13 (LTC)": 0.4, "970354f3fa (ETH)": 0.45, "a36ea00138 (XRP)": 0.25, "ee5812f0f4 (BTC)": 0.4, "aadd066216 (DOGE)": 0.3}

## Entscheidung 2026-08-23

**Strategy:** I start every window at a neutral 0.5 weight. I only raise it on a confirmed weekly trend state: 2, 4 and 8-week returns share a sign, the price is above a non-falling long average, and a multi-month range breakout holds on closes. I cut it when volatility spikes (σ20/σ90 well above 1.5) or the long average is falling. A single extreme week built from 2–3 giant candles, especially with a long upper wick, I treat as a reversal candidate and do not chase.

**Shared pattern:** every window shows the same sequence. There was a crash around day −82, then weeks of basing, then a +18–50 % spike over days −4 to −2. Day −1 printed a large upper wick, and day 0 consolidated at 100. In all of them, short-term volatility has exploded and the 2/4/8-week momentum is positive mainly because of this one week. So no window gets more than a modest weight.

## 8fffca08b0 (ADA)
- **Read:**
  - The long trend is down: 131 at the start, about 102 before the crash, low of 61. A base formed at 63–77, then the spike ran from 77 to 101.
  - Day −1 wicked to 113.8 and closed at 99.6, a rejection.
  - 2/4/8-week returns are +17/+37/+58 %, all positive, but driven by the extreme week. The window high of 138 is far above.
  - The long average is falling and sits around 95–100, so price is right at it.
- **Weight:** 0.4. Momentum is positive but rests on giant candles, volatility is extreme, and the long-term regime is not yet up.
- **Change my mind:** I would reduce on closes below 85 (the spike gave back). I would raise on weekly closes held above 114.

## be2be6876e (LINK)
- **Read:**
  - The base was 61–77; the old high zone before the crash was 89–94. Price closed above it at 100.
  - That makes 100 a multi-month high on a closing basis, with volume well above median.
  - The day −1 wick to 109 shows rejection. 2/4/8-week returns are about +41/+31/+59 %.
- **Weight:** 0.55. This is the cleanest breakout to the top of the range, but volatility is very high and the move is fresh.
- **Change my mind:** I would reduce on closes back below 93 (failed breakout). I would raise on a pullback that holds above 94, followed by a close above 109.

## ac0740e104 (ETH)
- **Read:**
  - The old high was about 98–100 (day −128). After the crash low of 61, price based at 72–79, then broke from 78 to 102.
  - Price is now at 100, right at the old high and not clearly above it.
  - 2/4/8-week returns are positive (+29/+31/+57 %).
- **Weight:** 0.5. Momentum is positive, but the breakout is unconfirmed and volatility is high.
- **Change my mind:** I would cut on closes below 90. I would add on weekly closes above 103.

## fcd083c3c0 (XRP)
- **Read:**
  - Before the spike, price was in a downtrend of lower highs (76 → 66).
  - The move ran from 66 to 112 intraday on 4–6× volume, then closed at 96 and 100. This looks like a blow-off.
  - Momentum before the spike was negative; the gains rest on a single week. The old high is 105.7.
- **Weight:** 0.3. There is no trend state beyond the one extreme week, the wick is climactic, and volatility is maximal.
- **Change my mind:** I would cut further on a close below 83. I would raise on weekly closes held above 106.

## 23e76c06df (DOT)
- **Read:**
  - The downtrend runs from 179 to 82 with lower highs (145, 109, 97, 93).
  - The long average is falling, roughly 105–120, and is overhead resistance.
  - The spike ran 81 → 101; day −1 wicked to 111 and was rejected.
  - 2/4/8-week returns are only about +12–16 %.
- **Weight:** 0.3. This looks like a rebound inside a downtrend, so I only add in steps.
- **Change my mind:** I would cut on closes below 86. I would raise on several weekly closes above 110.

## 276311511b (SOL)
- **Read:**
  - The old high was 102 (day −104). After the crash low of 63, price recovered to 86 by day −51, then based at 75–82.
  - The spike went to 100; day −1 wicked to 107.7.
  - 2/4/8-week returns are +25/+24/+34 %, and lows have been higher since day −60.
- **Weight:** 0.45. The structure is constructive, but this is an unconfirmed retest of the 102 high with high volatility.
- **Change my mind:** I would cut on closes below 88. I would raise on closes above 103 that hold.

## 8b0b65f261 (DOGE)
- **Read:**
  - Price peaked at 127 (day −101), then made lower highs (99, 85, 80) and based at 74–76.
  - The spike went to 101; day −1 wicked to 108 and was rejected.
  - The long-term regime is still down, with price at or below a falling long average (about 95–100).
- **Weight:** 0.35. This is a rebound against falling structure, and volatility is high.
- **Change my mind:** I would cut on closes below 85. I would raise on weekly closes above 108.

## b123bf3f46 (LTC)
- **Read:**
  - The crash from 115 to 75 was followed by a steadier recovery (higher lows at 75, 83 and 84), then a range of 84–91.
  - The spike was smaller, about +18 % (85 → 102).
  - 2/4/8-week returns are +15/+9/+23 %. The old range was 98–110.
- **Weight:** 0.45. Moderate momentum, a less extreme spike, and price back inside the old range.
- **Change my mind:** I would cut on closes below 89. I would raise on weekly closes above 106.

## fd9d29ad0d (AVAX)
- **Read:**
  - Price peaked at 138. There were two crashes (to 82, then 75), then a base at 80–91.
  - The spike went to 103; day −1 wicked to 109.
  - The long average is falling and well above price, around 105–110, and the old range was 115–135.
  - 2/4/8-week returns are about +13–18 %.
- **Weight:** 0.35. This is a rebound in a downtrend regime with high volatility.
- **Change my mind:** I would cut on closes below 88. I would raise on weekly closes above 110.

## 92dca21015 (BTC)
- **Read:**
  - Price rose to 106 by day −109, crashed to 75, then based at 77–86.
  - The spike went to 101 with no big rejection wick and comparatively moderate volume.
  - Price is now testing the old high zone of 100–106. The long average is about 90 and roughly flat.
  - 2/4/8-week returns are +20/+19/+31 %.
- **Weight:** 0.45. The structure is constructive with a lower spike risk, but it is still an unconfirmed test of resistance.
- **Change my mind:** I would cut on closes below 91. I would raise on weekly closes above 106.

```json
{"8fffca08b0 (ADA)": 0.4, "be2be6876e (LINK)": 0.55, "ac0740e104 (ETH)": 0.5, "fcd083c3c0 (XRP)": 0.3, "23e76c06df (DOT)": 0.3, "276311511b (SOL)": 0.45, "8b0b65f261 (DOGE)": 0.35, "b123bf3f46 (LTC)": 0.45, "fd9d29ad0d (AVAX)": 0.35, "92dca21015 (BTC)": 0.45}
```

## Entscheidung 2026-08-30

**Strategy.** I start each window at a neutral weight of about 0.5. I raise it only when the 2-, 4- and 8-week returns all agree in sign, the breakout above a multi-month range has held on closes, and the long trend is not falling. I lower it when price sits under a falling long average, when the momentum horizons disagree, or when a spike is fading back toward its base. Every window just had an extreme one-week spike, which counts as a reversal candidate rather than confirmed momentum. Volatility has jumped as a result (σ20/σ90 well above 1.5), so I keep every weight at or below about 0.6.

## 670bd73e62 (ETH)
- **Read:** The crash ran to 63, then a range of 65–80 held for about 75 days. The spike from 79 to 104 has held for 9 days between 99 and 104. The 2-, 4- and 8-week returns are all positive (+29%, +28%, +35%). Price is back at the old highs around 100–102 from day −135.
- **Weight: 0.55.** The breakout has held and momentum agrees across horizons. The size is held down because the move came from only 2–3 giant candles and volatility is high.
- **Change my mind:** Closes below 95 (back inside the spike base) would take me to about 0.4. Weekly closes above 106 would take me to about 0.65.

## b5724a6f66 (BTC)
- **Read:** The 77–86 range broke upward, and closes have held between 99 and 103 for 9 days. All momentum horizons are positive. The old high is 106 (day −116).
- **Weight: 0.55.** Same reasoning as the first window.
- **Change my mind:** Closes below 95 would lower it; holding above 106 would raise it.

## aeae3b222a (DOGE)
- **Read:** The longer-term trend is down, from a 140 high to an 83–91 base. The spike wicked to 123 but closes have fallen steadily (112 → 114 → 110 → 104 → 109 → 104 → 100). Price has given back about half of the spike, and the highs are getting lower.
- **Weight: 0.4.** The breakout is fading inside an overarching downtrend.
- **Change my mind:** A close below 96 would take me to about 0.3. A reclaim above 110 on closes would take me to about 0.5.

## a043fbbfa8 (LINK)
- **Read:** A broader advance started before the spike (73 → 85 from day −19 onward), so momentum is wider-based than in the other windows. Closes are holding 100–107, and the earlier high was 97. All horizons are positive.
- **Weight: 0.55.**
- **Change my mind:** Closes below 95 would lower it; closes above 108 would raise it.

## 1134e43f64 (DOT)
- **Read:** The long downtrend from 188 to 92 is intact, and the 100-day average (about 115) is falling and above price. The spike wicked to 126 and is fading to 100. The 8-week return is negative (−7%) while the 2-week is positive, so the horizons disagree.
- **Weight: 0.3.** This looks like a rally inside a downtrend.
- **Change my mind:** Weekly closes above 115 would take me to about 0.45. Closes below 92 would take me to about 0.2.

## 0b537a4524 (AVAX)
- **Read:** The downtrend runs from 140 to a base of 85–95. The spike wicked to 117 and has faded to 100. The 8-week return is only +3%, and price is below a falling long average (about 105–110).
- **Weight: 0.35.**
- **Change my mind:** Closes above 108 would raise it; closes below 92 would lower it to about 0.25.

## 4c48b3d5c2 (LTC)
- **Read:** After the crash to 85 there was a gradual recovery to a 92–99 range. The spike reached 116 and has faded to 100, which is just above the old range top of about 99. All horizons are positive but modest (+5% to +9%).
- **Weight: 0.45.** The trend is mildly positive but the breakout is weakly held.
- **Change my mind:** Closes below 95 would take me to about 0.35. Closes above 110 would take me to about 0.55.

## 8f7cad1a89 (XRP)
- **Read:** The base was drifting down from 85 to 73 before the event. The spike wicked to 125 on 6x volume, and closes have faded to 100. All horizons are positive only because of the spike, and volatility is extreme.
- **Weight: 0.4.** This is a one-week extreme with no prior trend behind it, so it is a reversal candidate.
- **Change my mind:** Closes below 94 would take me to about 0.3. Holding above 108 would take me to about 0.5.

## 7a9afb42cf (SOL)
- **Read:** This advance is the most orderly of the set. Closes climbed stepwise (84 → 92 → 97 → 100 → 107) instead of in one candle, and the higher high at 107 came on day −3. Price is above the earlier highs of 96, and all horizons are strongly positive.
- **Weight: 0.6.** Momentum is of better quality than elsewhere, still capped for volatility.
- **Change my mind:** Closes below 93 would take me to about 0.45. A weekly close above 108 would take me to about 0.65.

## a02b54a6fd (ADA)
- **Read:** The downtrend runs from 143 to 75. There have been repeated failed spikes (to 104 at day −57, 104 at day −24, and now 134), each faded afterwards. The 8-week return is only +2%, and the long average is falling.
- **Weight: 0.35.** The spikes are a pattern of failure, not a trend.
- **Change my mind:** Weekly closes above 112 would raise it; closes below 90 would lower it to about 0.25.

{"670bd73e62 (ETH)": 0.55, "b5724a6f66 (BTC)": 0.55, "aeae3b222a (DOGE)": 0.4, "a043fbbfa8 (LINK)": 0.55, "1134e43f64 (DOT)": 0.3, "0b537a4524 (AVAX)": 0.35, "4c48b3d5c2 (LTC)": 0.45, "8f7cad1a89 (XRP)": 0.4, "7a9afb42cf (SOL)": 0.6, "a02b54a6fd (ADA)": 0.35}

## Entscheidung 2026-09-06

**Strategy:** The direction comes from the weekly level. I use 2-, 4- and 8-week momentum, whether the post-breakout consolidation has held, and whether the close is above or below the falling long average. Elevated short-term volatility (σ20/σ90 well above 1.5 after the spike around day −17 to −15) caps the size. Single extreme days add nothing. I never weight by position in the range.

All windows share the same overall shape: a crash around day −96 to −93, a two-month base, a sharp breakout around day −17 to −15, then consolidation. They differ in how cleanly the breakout held and how heavy the overhead long-term downtrend is.

## f92b362c65 (LTC)
- **Read:** Momentum is positive across all three windows: 2 weeks about +5%, 4 weeks +21%, 8 weeks +25%.
  - The breakout from the 78–87 range held. The pullback low was 86–87, well above the old range.
  - Day −1 was a +8% candle, an extreme day, so I don't add because of it.
  - The 180-day high of 110 is overhead, and the long average is flat to falling but below price.
- **Weight: 0.6.** The trend state is up, and the size is reduced for volatility.
- **Change my mind:** a weekly close below 86.

## 2ffd5f5eaf (XRP)
- **Read:** The spike reached 119 intraday, then gave back. Momentum is mixed: 2 weeks −6%, while 4 and 8 weeks are +38% and +31%.
  - Price has been swinging in a 92–107 range for two weeks, with very high volatility.
  - Short and long momentum disagree, which points to a middle weight.
- **Weight: 0.45.**
- **Change my mind:** a close below 92 means lower; weekly closes above 107 mean higher.

## d0b25ede19 (DOGE)
- **Read:** The 180-day high is 130 and the long average is clearly falling.
  - The breakout from 75–80 held, with the low at 88.
  - Momentum is mixed: 2 weeks −3% (noise), 4 and 8 weeks about +30% and +25%.
  - Price oscillates between 88 and 104.
- **Weight: 0.45.** The overhead downtrend and high volatility keep it near the middle.
- **Change my mind:** below 88 means reduce; weekly closes above 104 mean raise.

## ba37f42311 (SOL)
- **Read:** This is the cleanest trend of the set. Momentum is +12% over 2 weeks, +40% over 4 and +38% over 8.
  - Price is at a new 180-day high, above the earlier 91–92 peak and the 102 intraday high around day −10.
  - Higher lows are in place, at 91 and 94.
- **Weight: 0.7.**
- **Change my mind:** a close below 91 (the last higher low).

## d5aab8ff96 (DOT)
- **Read:** The long-term downtrend runs from 155 to 77, and the long average is falling strongly.
  - Momentum is positive: +5.5% over 2 weeks, +22% over 4, +16% over 8.
  - Day 0 was a +7% candle up to the area of the spike high, about 96–105.
  - Price is only now testing the post-crash structure and is still far below the high.
- **Weight: 0.55.**
- **Change my mind:** a close below 85 means lower; a weekly close above 105 that holds means higher.

## fcd051cf16 (ETH)
- **Read:** The breakout from 74–77 has held for three weeks in a calmer band of 94–101.
  - Price is at a new 180-day closing high, above 96.
  - Momentum is positive: +2% over 2 weeks, +32% over 4, +39% over 8.
- **Weight: 0.65.**
- **Change my mind:** a close below 93.

## 99fb1c3a21 (ADA)
- **Read:** The long-term trend runs down from 130 and has been choppy, including a failed rally to 90 around day −31.
  - The 2-week change is −2% (noise), while 4 and 8 weeks are +15% and +38%.
  - Wide swings run from 85 to 102.
- **Weight: 0.5.**
- **Change my mind:** a close below 85 means lower; weekly closes above 103 mean higher.

## 4136c9b393 (BTC)
- **Read:** The breakout from the 78–81 range held, consolidating tightly at 96–101 with falling volatility and falling volume.
  - Momentum is positive: +3% over 2 weeks, +24% over 4, +26% over 8.
  - The old highs from around day −123 sit at 101–103.
- **Weight: 0.65.**
- **Change my mind:** a close below 95.

## ae67b18275 (AVAX)
- **Read:** The 180-day high is 133, and the long average is falling.
  - The breakout from 80–85 held, with the low at 89.
  - Momentum is positive: +4% over 2 weeks, +23% over 4, +23% over 8.
  - Price is at 100, just above the spike close.
- **Weight: 0.55.**
- **Change my mind:** a close below 89.

## 0ea9b085dc (LINK)
- **Read:** The uptrend has run since about day −26, with higher lows at 83–84.
  - Price is at a new 180-day high, far above the earlier peak of 82.
  - Momentum is +15% over 2 weeks, +61% over 4, +65% over 8.
  - Day 0 was a +10% candle, an extreme that is not a reason to add, and volatility is very high.
- **Weight: 0.65.**
- **Change my mind:** a close below 84.

{"f92b362c65 (LTC)": 0.6, "2ffd5f5eaf (XRP)": 0.45, "d0b25ede19 (DOGE)": 0.45, "ba37f42311 (SOL)": 0.7, "d5aab8ff96 (DOT)": 0.55, "fcd051cf16 (ETH)": 0.65, "99fb1c3a21 (ADA)": 0.5, "4136c9b393 (BTC)": 0.65, "ae67b18275 (AVAX)": 0.55, "0ea9b085dc (LINK)": 0.65}

## Entscheidung 2026-09-13

# Weekly Position Decisions: 10 Windows

## Strategy

I use the weekly regime first: do the 2-, 4- and 8-week returns agree in sign, and has a range breakout held on closing prices? I set the size from volatility. A recent large surge with σ20/σ90 well above 1.5 keeps the weight near the middle rather than at the extreme, and an extreme single week counts against continuation. Position in the range, single candles and indicator readings don't move the weight. I only change my view on a closing break of the post-breakout consolidation lows, or on a held close above the consolidation highs.

**Shared context.** All ten windows show the same pattern:
- a crash around day −100;
- a sideways base until about day −26;
- a jump of 20–50 % around days −25 to −22;
- three weeks of consolidation in a high-volatility regime.

The 4- and 8-week momentum is positive everywhere. The 2-week momentum is flat to mixed, and the last week was negative in most windows. So this reads as a correction inside a young weekly uptrend, with sharply higher volatility. The default is a medium weight.

## e298122e08 (AVAX)
- **Trend:** Down from 140 to 81, then a 85–95 range. The breakout at −24 is holding, and price now sits in a 96–112 consolidation.
- **Momentum:** 2W +2.5 %, 4W +15 %, 8W +13 %, all positive. The last week fell −8 % from the 112.5 high, which is a correction.
- **Long average:** The 180-day average sits above price at about 110 and is still falling, so the long-term picture is not yet repaired.
- **Weight: 0.45**
- **Change my mind:** Below 96 (consolidation lows), reduce. A held weekly close above 112.5, increase.

## 963802e133 (XRP)
- **Trend:** Steady decline from 109 to 74, then a +50 % surge to 126.7 (wick). Since then, consolidation at 98–110.
- **Momentum:** 4W +35 %, 8W +23 %, 2W about −1 %, so mixed in the short term.
- **Volatility:** Very high; the volume spike was 6×.
- **Breakout:** The prior range top at 86–88 is far below, so the breakout clearly held.
- **Weight: 0.5**
- **Change my mind:** A close below 97.5 is a warning, and below 92 I reduce. A weekly close above 110, increase.

## 1d553894ed (ETH)
- **Trend:** Crash to 61, a higher base at 70–78, then a breakout to 100+. Price is now at the top of the 180-day range (prior high 99.5).
- **Momentum:** 4W and 8W about +32 %, 2W +2.5 %, all aligned.
- **Structure:** Lows rise from 95.1 to 97.1, giving HH/HL. The trend is relatively smooth.
- **Weight: 0.6**
- **Change my mind:** A close below 95, reduce toward 0.4.

## e1b1605e50 (LTC)
- **Trend:** Base at 77–89, breakout to 103, a pullback to 88.2 (higher low), then a new high at 110.6. Price is now 100.
- **Momentum:** 2W +12 %, 4W +22 %, 8W +14 %, all positive.
- **Structure:** Intact HH/HL.
- **Weight: 0.6**
- **Change my mind:** Below 96, a warning. Below 88, the trend is broken and I reduce.

## af855f26f5 (BTC)
- **Trend:** Base at 76–87, breakout to 103, then a tight consolidation at 99–106. Price sits at the lower edge.
- **Momentum:** 4W +22 %, 8W +19 %, 2W −2 %.
- **Weight: 0.5**
- **Change my mind:** A close below 98.5 is a failing consolidation, so reduce to 0.35. Above 106, increase to 0.6.

## 5cfb6fc282 (DOGE)
- **Trend:** High at 143, crash to 84, then a spike to 122 (wick) and 115 (wick). Price has fallen back to 100.
- **Momentum:** 4W +18 %, 8W +14 %, 2W ±0.
- **Long average:** The 180-day average sits around 108 and is falling, and there are repeated long upper wicks.
- **Weight: 0.45**
- **Change my mind:** Below 97, reduce to 0.3. Above 111, increase.

## 5d967c67c0 (LINK)
- **Trend:** Crash to 63, then a gradual rise from day −33 and a breakout to 107. A spike to 122 at day −6 fully reversed back to 100.
- **Momentum:** 4W +19 %, 8W +34 %, 2W ±0. The last week was −15 %, an extreme week, which reads as a reversal of the spike rather than a trend break.
- **Weight: 0.5**
- **Change my mind:** Below 97, reduce. A weekly close above 112, increase.

## 9b0b05f5b3 (SOL)
- **Trend:** Crash to 61, recovery, a 72–79 range, then a breakout to 111.
- **Structure:** Since then, falling highs (111 → 108 → 106.5) against stable lows around 98–99, which is a contracting triangle.
- **Momentum:** 4W +33 %, 8W +30 %, 2W −2.5 %.
- **Weight: 0.5**
- **Change my mind:** A close below 98, reduce to 0.35. Above 108.5, increase to 0.6.

## ff7842a00b (ADA)
- **Trend:** High at 142, crash to 77, then repeated spikes to 98, 104 and 127 (wick), each followed by a reversal. The structure is choppy, with many crosses of the 50-day average.
- **Momentum:** 4W +16 %, 8W +22 %, 2W +5.6 %.
- **Long average:** About 108 and falling.
- **Volatility:** High, and trend quality (ER) is low.
- **Weight: 0.4**
- **Change my mind:** Below 93.5 (low at −14), reduce to 0.25. A held close above 111, increase.

## 9d8dd60946 (DOT)
- **Trend:** A long downtrend from 162 to 75, a breakout to 103 (wick), then a blow-off at day −5 to 128.5 that fully reversed to 100. This last move was a single extreme week with 4× volume.
- **Momentum:** 2W +22 %, 4W +32 %, 8W +21 %.
- **Long average:** Falling and above price, around 110+.
- **Volatility:** σ20/σ90 is clearly above 1.5, so the position should be smaller.
- **Weight: 0.4**
- **Change my mind:** Below 95, and especially back below 90 (old range top), reduce to 0.2. A weekly close above 112, increase.

## Weights

```json
{"e298122e08 (AVAX)": 0.45, "963802e133 (XRP)": 0.5, "1d553894ed (ETH)": 0.6, "e1b1605e50 (LTC)": 0.6, "af855f26f5 (BTC)": 0.5, "5cfb6fc282 (DOGE)": 0.45, "5d967c67c0 (LINK)": 0.5, "9b0b05f5b3 (SOL)": 0.5, "ff7842a00b (ADA)": 0.4, "9d8dd60946 (DOT)": 0.4}
```

## Entscheidung 2026-09-20

**Strategy:** The default weight is 0.5. I raise it only when the trend has a confirmed state: the 2-, 4- and 8-week returns all point the same way, the structure shows higher highs and higher lows, and a close holds above a multi-month range. I lower it when short and long momentum disagree, when the structure breaks, or when volatility is clearly elevated. Range position, oscillator levels and single extreme days or weeks count at most once, and an extreme week is a reason not to chase rather than a reason to buy.

---

### 46ba36175d (DOT)
- **Market:** The window fell from about 120 to 67 (day −55) and then rebounded hard. A spike to 109.8 at day −12 failed. Price fell to 83 at day −5 and has recovered to 100.
- **Momentum:** 2W about +14%, 4W about +22%, 8W about +37%. All three are positive.
- **Volatility:** Very high. σ20/σ90 is well above 1.5, with daily ranges of 6–10 and volume spikes of 2–4x.
- **Structure:** Choppy, with a lower high (109.8) after the spike. The long-term average is around 90–95 and roughly flat. Price sits only slightly above it.
- **Weight: 0.5.** Positive momentum is offset by extreme volatility and a failed spike, so I stay neutral.
- **Change mind:** A close below 83 means cutting toward 0.3. Weekly closes holding above 104 would justify about 0.65.

### 7c686ab687 (BTC)
- **Market:** The window traded in a 77–80 base for about two months. It broke out at day −32 to around 96. It has since consolidated at 93–101 for four weeks without losing the breakout, and closes at 100, near the 180-day high of 102.
- **Momentum:** 2W about +1%, 4W about +4%, 8W about +24%. All are positive, but the short-window z-score is modest.
- **Volatility:** Low to normal.
- **Structure:** The breakout held its retest. Higher lows are at 93.9 and 92.4.
- **Weight: 0.6.** The trend state is intact and volatility is calm.
- **Change mind:** A close below 92 means a failed consolidation, so I would go back to 0.45. A weekly close above 102.5 is a fresh multi-month high and would justify about 0.7.

### 4a8177812d (ADA)
- **Market:** The window crashed from 126 to 61 (day −87) and then rallied in spikes: 87 at day −78, 92 at day −45, and 113 intraday at day −29. Since then it has ranged between 84 and 101.
- **Momentum:** 2W about +2%, 4W about 0%, 8W about +37%. The short windows are flat, so this is not a trend state.
- **Volatility:** High. The rally came from a few giant candles.
- **Structure:** A sideways range of 84–103 over the last month.
- **Weight: 0.45.**
- **Change mind:** Weekly closes above 103 would justify 0.6. A close below 84 means 0.3.

### 8f688aa6f3 (XRP)
- **Market:** A blow-off spike took it from 71 to 120 intraday (day −29), on 4–6x volume. Since then it has made lower highs and traded choppily between 89 and 108. Day −5 printed a large outside-down candle (106 → 91).
- **Momentum:** 2W about −1%, 4W about −7%, 8W about +27%. Short and long momentum contradict each other, which suggests a possible turning point.
- **Volatility:** Very high.
- **Weight: 0.4.** I pull toward the middle because of the contradiction and the volatility.
- **Change mind:** A close below 88 means 0.25. A weekly close above 104 means 0.55.

### ea2d964971 (LTC)
- **Market:** A base at 75–80 broke out to around 90. Higher lows followed at 81.6 and 87.3, and price closes at 100, near the 180-day closing high of 102.9.
- **Momentum:** 2W about +7%, 4W about +12%, 8W about +23%. All three are positive.
- **Volatility:** Moderate.
- **Structure:** Higher highs and higher lows.
- **Weight: 0.65.**
- **Change mind:** A close below 87 (the last higher low) means 0.45. A weekly close above 103 would support about 0.75.

### 43f329a9b0 (SOL)
- **Market:** A base at 64–70 broke out to 98, consolidated at 87–96, and now closes at 100. That is above the 180-day high (the prior peaks were 98.2 in the last month and 87.6 at day −132), so this is a multi-month breakout.
- **Momentum:** 2W about +4%, 4W about +17%, 8W about +45%. This is a clear trend state.
- **Volatility:** Moderate.
- **Weight: 0.7.**
- **Change mind:** A close back below 92 means the breakout failed, so I would go to 0.45.

### 237758c7f4 (AVAX)
- **Market:** After a long base at 55–60 and a range at 63–71, price rose about 50% in three days (67 → 100) on 4–6x volume. The day-0 range was 83–101. Price closed above the 180-day high of about 92.7.
- **Momentum:** 4W and 8W are strongly positive, but the last week alone is extreme, with z well above 2.
- **Volatility:** Exploding.
- **Assessment:** This is a single extreme week, which is more often a reversal candidate than a continuation. Adding here would mean chasing.
- **Weight: 0.4.**
- **Change mind:** Two weekly closes holding above 92 (the breakout zone) would justify 0.55. A close below 83 (the day-0 low) means 0.25.

### cfa7ef0398 (ETH)
- **Market:** A gap breakout from 72 to 95 was followed by a tight month at 89–96. Lows held at 89.1 and 89.2. Price now closes at 100, a new 180-day closing high.
- **Momentum:** 2W about +5%, 4W about +7%, 8W about +35%. All three are positive.
- **Volatility:** Calmer than in the other windows.
- **Weight: 0.65.**
- **Change mind:** A close below 89 means 0.45. A weekly hold above 101 means about 0.75.

### 4cbec38df1 (DOGE)
- **Market:** The window peaked near 136 (day −129) and fell to 77.5. A spike reached 115 intraday at day −29. Since then it has made lower highs (109, 104.6) and chopped between 90 and 105. Price is still well below the earlier highs, and the long-term average is falling.
- **Momentum:** 2W about −4%, 4W about −7%, 8W about +19%. Short and long momentum disagree.
- **Weight: 0.4.**
- **Change mind:** A weekly close above 105 means 0.55. A close below 90 means 0.25.

### b1557662b1 (LINK)
- **Market:** Higher lows formed out of the 63–70 base. A breakout followed, then a spike to 109 at day −13, then a pullback to 85. Price is back at 100. The prior multi-month high of 86.8 has been held on closes.
- **Momentum:** 2W about −5%, 4W about +8%, 8W about +42%. The short-term reading is mixed.
- **Volatility:** Elevated.
- **Weight: 0.55.**
- **Change mind:** A close below 85 means 0.4. A weekly close above 106 means 0.7.

{"46ba36175d (DOT)": 0.5, "7c686ab687 (BTC)": 0.6, "4a8177812d (ADA)": 0.45, "8f688aa6f3 (XRP)": 0.4, "ea2d964971 (LTC)": 0.65, "43f329a9b0 (SOL)": 0.7, "237758c7f4 (AVAX)": 0.4, "cfa7ef0398 (ETH)": 0.65, "4cbec38df1 (DOGE)": 0.4, "b1557662b1 (LINK)": 0.55}

## Entscheidung 2026-09-27

**Strategy:** I start every window at a neutral 0.5. I raise the weight to about 0.7 only when 2-, 4- and 8-week momentum all point up, the move came from many orderly days rather than one or two giant candles, and price has broken a multi-month high on closes and held there. I cap the weight near 0.5 to 0.55 when short-term volatility is far above its 90-day level, the move rests on single spike candles, or price still sits below an older resistance zone.

All ten windows share the same market path: a crash around day −117, a base, a rally from day −39, and a push to new local highs in the last 9 days. So every coin has positive momentum, and ranking them against each other adds nothing. Each is judged on its own trend quality and volatility.

### da65538557 (LTC)
- **Read:** Price rose from a 62 base to 100. Momentum is strongly positive: about +59% over 8 weeks, +49% over 4 weeks and +33% over 2 weeks. It broke the old 180-day high of 85 and has held 4 closes above 98.
- **Caution:** Much of this came from one extreme candle on day −3 (+16%, volume 6.7). The last week is an extreme week, and short-term volatility is well above its 90-day level.
- **Weight:** 0.6. The trend is confirmed, but I cut it for the spike and the volatility.
- **Change my mind:** A close below 86 means the breakout failed (go to 0.35). Holding above 105 for a week would justify 0.7.

### 51a39980fd (ETH)
- **Read:** After the jump at day −39, price spent a month in an orderly range of about 88 to 95. It then broke out to 98–104 and is holding around 100. Momentum is about +43% over 8 weeks and +11% over 4 weeks.
- **Volatility:** Low, and the last few days are quiet. Structure shows higher highs and higher lows.
- **Weight:** 0.7.
- **Change my mind:** A close below 95 puts price back in the range; below 88 the trend is broken (go to 0.45).

### ab0efc1490 (DOGE)
- **Read:** The rally ran from 72 to 100, but it is very choppy. There was a spike to 109 and an immediate drop to 94, and daily ranges are often 10% or more.
- **Resistance:** Price is still below the older 107–122 zone from days −150 to −135.
- **Volatility:** Short-term volatility is far above its 90-day level. Momentum is positive (+37% over 8 weeks, +18% over 4 weeks) but of poor quality.
- **Weight:** 0.5.
- **Change my mind:** A close below 82 (the day −12 low) would take it to 0.3. Weekly closes above 110 would take it to 0.65.

### 36b31968c0 (LINK)
- **Read:** Clean higher highs and higher lows: 77.6 → 86 → 100+. Price broke the old high of 77.5 long ago.
- **Momentum:** About +67% over 8 weeks, +26% over 4 weeks and +25% over 2 weeks. The gains came from many days, not one candle.
- **Weight:** 0.7.
- **Change my mind:** A close below 86 is a warning (go to 0.5). Below 77.6 the structure is broken.

### 755c56a1ab (XRP)
- **Read:** A blow-off to 112 at day −36, then a wide range of 84 to 109 with heavy volume spikes. Price is in the middle-to-upper part of that range.
- **Momentum:** +43% over 8 weeks and +12% over 4 weeks. Volatility is very high, and there has been no clean breakout above 112.
- **Weight:** 0.55.
- **Change my mind:** A close below 84 would take it to 0.35. A weekly close above 112 would take it to 0.7.

### 688d838c7e (ADA)
- **Read:** The rally from 68 reached 101, fell back to 75, then climbed to 104. Price is still below the old 104–113 high zone.
- **Momentum:** Positive: +35% over 8 weeks and +32% over 4 weeks. Volatility is high.
- **Weight:** 0.55.
- **Change my mind:** A close below 91 would take it to 0.4. Weekly closes above 108 would take it to 0.7.

### c06f74bec2 (SOL)
- **Read:** A steady trend from 60 to 100, well above the prior 180-day high of 80.7. The last higher low is at 79.4.
- **Momentum:** About +69% over 8 weeks and +20% over 4 weeks. Volatility is moderate and the trend is orderly.
- **Weight:** 0.7.
- **Change my mind:** A close below 92 means 0.55; below 79 the trend is broken.

### 283c955218 (BTC)
- **Read:** The cleanest trend of the set. Price ran from 76 to 93, ranged between 89 and 97, broke out to 103, and is now holding at 100. It is above the old high of 98.
- **Momentum:** +33% over 8 weeks and +9% over 4 weeks, with low volatility.
- **Weight:** 0.7.
- **Change my mind:** A close below 95 puts price back in the range (go to 0.55). Below 89 the trend is broken.

### 515c2f799b (AVAX)
- **Read:** After two months flat at 57–62, almost the whole move (+60%) came from two candles on days −8 and −7, with peak volume of 5.7. This is an extreme week with a fragile structure.
- **Since then:** Price has stuck between about 92 and 108 for 6 days. Volatility is extreme. The 8-week return (+76%) is driven by the spike.
- **Weight:** 0.5.
- **Change my mind:** A close below 91 means the spike has failed (go to 0.3). Weekly closes above 108 would take it to 0.65.

### eae9f7477f (DOT)
- **Read:** A spike to 101 at day −19 crashed back to 74.5, and price has now recovered to 100. It is very volatile, with ±10% days.
- **Resistance:** Price is below the old 104–113 zone. Momentum is positive (+59% over 8 weeks, +55% over 4 weeks), but the path is erratic.
- **Weight:** 0.55.
- **Change my mind:** A close below 85 would take it to 0.35. Weekly closes above 105 would take it to 0.7.

{"da65538557 (LTC)": 0.6, "51a39980fd (ETH)": 0.7, "ab0efc1490 (DOGE)": 0.5, "36b31968c0 (LINK)": 0.7, "755c56a1ab (XRP)": 0.55, "688d838c7e (ADA)": 0.55, "c06f74bec2 (SOL)": 0.7, "283c955218 (BTC)": 0.7, "515c2f799b (AVAX)": 0.5, "eae9f7477f (DOT)": 0.55}
