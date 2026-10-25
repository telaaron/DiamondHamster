# E-035: was die KI gedacht hat (Set A)

Volle Antwort des Deciders pro Entscheidungswoche, unverändert. Er sah weder Datum noch Coin-Namen; die Namen in Klammern sind erst danach eingesetzt. Gesendeter Prompt und Daten: runs/<set>/<woche>/requests.json.

## Entscheidung 2026-07-05

## 1. Strategy

I size exposure by long-term trend structure first, using EMA200, the Gaussian midline slope and position in the 180-day range. Then I adjust by whether price has reclaimed EMA50.

- **Below EMA50 in a falling long-term trend:** a short-term bounce gets at most 0.1–0.2.
- **Near or reclaiming EMA50:** 0.25–0.3.
- **Above EMA20, EMA50 and the Gaussian midline:** up to 0.5.

Full exposure needs price back above EMA200 with a rising Gaussian midline.

## 2. Windows

### 2250407a4e (DOT)
- **Read:** Deep downtrend. Price is 42.7% under EMA200 (≈174.5) and sits at 6% of the 180-day range. The Gaussian midline (≈127) is falling fast, and ADX 36.7 says the downtrend is strong. The +8.8% week is a relief bounce that stalled just under EMA20 (≈101.6). EMA50 (≈114) is far overhead, and the 90-day low is ≈90.3.
- **Weight:** 0.1. This is counter-trend with stoch RSI already at 0.97, so there is little room left in the bounce.
- **Change my mind:** a close above 114 (EMA50 reclaimed) raises the weight; a break below 90 takes it to 0.

### ee74e2fb2c (XRP)
- **Read:** Long-term downtrend. EMA200 is ≈129.5 and the Gaussian midline (≈109) is falling. Short term has turned up: price is above EMA20 (≈96.4) and VWAP, MACD histogram is positive, and RSI is 55. Price is testing EMA50 (≈102.5) from below. ADX 22.5 means the trend is weak.
- **Weight:** 0.25. The bounce is constructive but hasn't cleared EMA50, and stoch RSI at 1.0 is stretched.
- **Change my mind:** above 102.5 I'd go to about 0.4; below 96 I'd go to 0.1.

### af09282c07 (BTC)
- **Read:** Downtrend. EMA200 is ≈118.9, the Gaussian midline ≈110.4 is falling, and ADX 31. Price has bounced above EMA20 (≈98) and is heading toward EMA50 (≈103.4). Bands are tighter (width 12.9%) and volatility is lower. The 90-day low is ≈90.8.
- **Weight:** 0.2. The strong ADX belongs to the prevailing downtrend, and price is still below EMA50.
- **Change my mind:** a close above 103.5 lifts the weight; below 98 cuts it to about 0.05.

### 88dc3ae0d9 (LINK)
- **Read:** Long-term down. EMA200 is ≈125.8 and the Gaussian midline ≈108.3 is falling. Price is up 9.5% over 30 days, above EMA20 (≈96.2) and VWAP, and only 1.5% under EMA50 (≈101.5). The 90-day low is ≈86.7.
- **Weight:** 0.3. This is a reasonable recovery attempt close to reclaiming EMA50.
- **Change my mind:** above 101.5 I'd go to 0.4; below 96 I'd go to 0.1.

### c1928011ff (ADA)
- **Read:** A violent +31.8% week. Price is above the upper Bollinger band (1.02), 13.7% over EMA20 (≈88) and just above EMA50 (≈98.3). It is still far below EMA200 (≈153.6) and the Gaussian midline (≈111), whose slope is steeply negative. ADX 39 shows a strong move, but price is very extended and 14.9% above VWAP. The 90-day low is ≈73.
- **Weight:** 0.25. Momentum is real, but chasing an upper-band blow-off inside a bear trend carries a poor risk/reward.
- **Change my mind:** if price consolidates and holds above 98 I'd add; a fall below 88 means the spike failed, and I'd go to 0.

### 6e321630d1 (LTC)
- **Read:** Downtrend structure. EMA200 is ≈128.5 and the Gaussian midline ≈107.9 is falling. Short term is firm: price is above EMA20 (≈95.9), bollinger_pos is 0.79, ADX 32 and RSI 57. Price is just under EMA50 (≈101.3).
- **Weight:** 0.3. The bounce is constructive and EMA50 is in reach, but this is still below long-term resistance.
- **Change my mind:** above 101.5 I'd go to 0.4; below 96 I'd go to 0.1.

### 74079e2872 (AVAX)
- **Read:** Strong downtrend. Price is 33% under EMA200 (≈150), the Gaussian midline (≈117) is falling at −3.8% per 5 days, and ADX 35.8. The bounce has carried price over EMA20 (≈97.4), but EMA50 (≈106) is still 6% away. The 90-day low is ≈82.
- **Weight:** 0.15. This is counter-trend, with significant overhead resistance.
- **Change my mind:** above 106 raises the weight; below 97 cuts it to 0.05.

### dbf46d879f (SOL)
- **Read:** The strongest of the set. Price is up 28% over 30 days and sits above EMA20 (≈92.3), EMA50 (≈93.5) and the Gaussian midline (≈95.5). The midline slope is still negative but shallow. EMA200 (≈118) and the 90-day high (≈120.6) are the next resistance. Price is somewhat extended, 14.6% above VWAP.
- **Weight:** 0.5. Structure is improving, but this isn't yet a confirmed long-term uptrend, and the extension argues for patience on size.
- **Change my mind:** a loss of 93.5 cuts the weight to 0.2; a close above 118–120 raises it to 0.75 or more.

### 5eb28a66a5 (ETH)
- **Read:** Long-term down. EMA200 is ≈126.6 and the Gaussian midline ≈108.8 is falling. Price is up 13.6% on the week, above EMA20 (≈95) and VWAP, and 1.2% under EMA50 (≈101.2). The 90-day low is ≈84.3.
- **Weight:** 0.3. This is a credible bounce at a key test, while the long-term trend is still negative.
- **Change my mind:** above 101.5 I'd go to 0.4; below 95 I'd go to 0.1.

### 68105f28cd (DOGE)
- **Read:** Strong downtrend. EMA200 is ≈140.4, the Gaussian midline ≈121.5 is falling, and ADX 36.4. The relief bounce is stuck just under EMA20 (≈100.9) and below VWAP. EMA50 (≈110.3) is well above, and the 90-day low is ≈89.3. Stoch RSI at 1.0 suggests the bounce is exhausted.
- **Weight:** 0.1.
- **Change my mind:** above 110 raises the weight; below 89 takes it to 0.

## 3. Weights

{"2250407a4e (DOT)": 0.1, "ee74e2fb2c (XRP)": 0.25, "af09282c07 (BTC)": 0.2, "88dc3ae0d9 (LINK)": 0.3, "c1928011ff (ADA)": 0.25, "6e321630d1 (LTC)": 0.3, "74079e2872 (AVAX)": 0.15, "dbf46d879f (SOL)": 0.5, "5eb28a66a5 (ETH)": 0.3, "68105f28cd (DOGE)": 0.1}

## Entscheidung 2026-07-12

**1. Strategy**

I only take meaningful long exposure when price is above the Gaussian channel midline and that midline is flattening or rising. Distance to the EMA200 serves as a check on the regime. When price is below a falling Gaussian midline and far below the EMA200, I stay flat or hold only a token position, however oversold it looks. Every window here is in a primary downtrend: all sit below the EMA200 and all have a negative Gaussian slope. So the weights stay low, and only the setups closest to reclaiming the midline get a small allocation.

**2. Windows**

**09faf902de (DOGE)**
- **Read:** Deep downtrend. Price is 32% below the EMA200 (≈147) and 20% below a steeply falling Gaussian midline (≈125). It sits at the bottom of its 180-day range, close to the 90-day low at ≈95.6. The EMA20 is at ≈104.6 and the EMA50 at ≈114. The positive MACD histogram is just a slower decline, not a reversal.
- **Weight:** 0.0. The trend is strong (ADX 34) and pointing down.
- **Change my mind:** A close above ≈114, reclaiming the EMA50. Losing ≈95.6 would confirm the downtrend continuing.

**19d4c6351d (ETH)**
- **Read:** A 30-day bounce has taken price back to the EMA50 (≈99.7). It is still below the falling Gaussian midline (≈103.5) and far below the EMA200 (≈123). Stoch RSI is pinned at 0.98 and there is a bearish RSI divergence, so the bounce looks extended into resistance.
- **Weight:** 0.1. This is a token position because momentum is real, but structure has not been reclaimed.
- **Change my mind:** A close above ≈104 (the Gaussian midline) would raise the weight. A close below ≈96 (the EMA20) would take it to flat.

**cdde591c21 (XRP)**
- **Read:** Weak downtrend with low ADX (15) and no clear impulse. Price is below the EMA20 (≈102), the EMA50 (≈107) and the falling Gaussian midline (≈113). The 90-day low is at ≈93.
- **Weight:** 0.0. There is no reclaim of any key level.
- **Change my mind:** A close above ≈107, the EMA50.

**f5b314ebd9 (AVAX)**
- **Read:** Bear trend. Price is 37% below the EMA200 and stoch RSI is at 0 after a 7.5% weekly drop. Resistance sits at the EMA20 (≈104), the EMA50 (≈112) and the Gaussian midline (≈120), and the midline is falling fast. The 90-day low is at ≈88.7.
- **Weight:** 0.0. Being oversold inside a strong downtrend is not a buy signal.
- **Change my mind:** A close above ≈112.

**d12067a8de (LTC)**
- **Read:** Consolidating near the EMA20 (≈100) and the 30-day VWAP. Price is below the EMA50 (≈104.3) and the Gaussian midline (≈108.6), and both are falling. The 90-day low is at ≈89.
- **Weight:** 0.05. The range is stable, but the trend is down.
- **Change my mind:** A close above ≈109 would raise the weight. A close below ≈89 would take it to flat.

**31b3a517e0 (ADA)**
- **Read:** A violent 14.5% drop in a week, with very wide Bollinger bands (39%) and high ATR. Price is 43% below the EMA200 and the Gaussian midline (≈122) has the steepest decline of any window. The EMA50 is at ≈112.4 and the 90-day low at ≈85.3.
- **Weight:** 0.0. Volatility is high and the downtrend is strong.
- **Change my mind:** A close above ≈112.

**c98cbd67dd (BTC)**
- **Read:** Flat over both 7 and 30 days. Price is just above the EMA20 (≈98.7) and below the EMA50 (≈102.4) and the Gaussian midline (≈106.8). The EMA200 is at ≈117 and the 90-day low at ≈90.7. Volatility is low and the market is basing.
- **Weight:** 0.1.
- **Change my mind:** A close above ≈107 would raise the weight. A close below ≈98.7 would take it to flat.

**60b37282c4 (SOL)**
- **Read:** This is the best structure in the set. A 15% rally over 30 days has carried price slightly above the Gaussian midline (≈99.1), and that midline has the flattest slope of any window. Price is also sitting on the EMA20 and EMA50 (≈99.8–99.9). The current move is a pullback from ≈106, and stoch RSI is reset to 0.02. The EMA200 is at ≈124.
- **Weight:** 0.25. This is a pullback-to-support entry within a possible trend change, kept modest because the regime is still bearish.
- **Change my mind:** A close below ≈97 would take it to flat. A close above ≈106 would raise the weight.

**d23f5ac689 (LINK)**
- **Read:** Similar to c98: price is above the EMA20 (≈97.8), just below the EMA50 (≈101.4), and below the Gaussian midline (≈105.8). ADX is low and the market is ranging. The EMA200 is at ≈125 and the 90-day low at ≈87.5.
- **Weight:** 0.1.
- **Change my mind:** A close above ≈106 would raise the weight. A close below ≈97.8 would take it to flat.

**7659de5cc5 (DOT)**
- **Read:** Deep bear. Price is 43% below the EMA200 and close to the 180-day low, with the 90-day low at ≈94.2. Resistance is at the EMA50 (≈114.4) and the steeply falling Gaussian midline (≈126).
- **Weight:** 0.0.
- **Change my mind:** A close above ≈114. Losing ≈94 would confirm the downtrend continuing.

**3. Weights**

{"09faf902de (DOGE)": 0.0, "19d4c6351d (ETH)": 0.1, "cdde591c21 (XRP)": 0.0, "f5b314ebd9 (AVAX)": 0.0, "d12067a8de (LTC)": 0.05, "31b3a517e0 (ADA)": 0.0, "c98cbd67dd (BTC)": 0.1, "60b37282c4 (SOL)": 0.25, "d23f5ac689 (LINK)": 0.1, "7659de5cc5 (DOT)": 0.0}

## Entscheidung 2026-07-19

## Strategy

All ten windows sit well below the 200-day EMA, with the Gaussian midline sloping down, so the default is defensive. I scale exposure up only when price has reclaimed both the 50-day EMA and the Gaussian midline with positive momentum. Windows below those levels get near-zero weight. Overstretched or ADX-confirmed downtrends get trimmed further.

## b01155f2bd (XRP)
- **Read:** Long-term downtrend near the bottom of the 180-day range (0.09). Price is at EMA20 (~100.3) but under EMA50 (~104.6), the Gaussian midline (~108.5) and EMA200 (~132). The 90-day low is ~91.9. ADX is 13, so there is no trend, only a weak bounce with a slightly positive MACD.
- **Weight:** 0.1. It hasn't reclaimed any meaningful resistance.
- **Change mind:** A close above ~105 (EMA50) would make me add. A close below ~92 would take me to flat.

## 91278f6cd9 (DOGE)
- **Read:** A strong downtrend (ADX 33), down 13% over 30 days, and 5% off the 180-day low. EMA20 is ~102.8, EMA50 ~111, the Gaussian midline ~120 and the 90-day low ~96. The positive MACD histogram only reflects slowing downside.
- **Weight:** 0.0. This is a confirmed bear trend.
- **Change mind:** A reclaim of ~111 (EMA50).

## 809cf88e9c (DOT)
- **Read:** The deepest decline in the set: 43% under EMA200, at 0.02 of the 180-day range, and still falling (-2.8% over 7 days). EMA20 is ~104.6, EMA50 ~114, the Gaussian midline ~124 and the 90-day low ~97.
- **Weight:** 0.0. There is no sign of a base.
- **Change mind:** A close above ~114. A loss of ~97 confirms the downtrend continues.

## 4f4856a40d (ADA)
- **Read:** Price has bounced 20% off the 90-day low (~83) and is back at EMA20 (~99.8). It remains below EMA50 (~107) and the Gaussian midline (~113). The very wide Bollinger bands (27%) point to a volatile regime, and the Gaussian slope is steeply negative.
- **Weight:** 0.1. A relief rally inside a downtrend.
- **Change mind:** Above ~107 I would raise it. Below ~95 I would go flat.

## 8e601ef4b7 (ETH)
- **Read:** Price is above EMA20 (~96.2), EMA50 (~97.0) and the Gaussian midline (~97.1). It is up 9.4% over 30 days, ADX is 22.5 and rising, and MACD is positive. It is still well below EMA200 (~118) and the 90-day high (~129.5), and is 8% above VWAP30, so it is somewhat extended.
- **Weight:** 0.5. This is the best structural reclaim in the set, capped by the long-term downtrend.
- **Change mind:** A close below ~96 (loss of EMA50 and the Gaussian midline) would cut it. Above ~118 (EMA200) would justify going heavier.

## 6017dda407 (AVAX)
- **Read:** Price is up 9.7% over 30 days but rolling over: stoch RSI is 0.23, it is below EMA20 (~102.5), EMA50 (~108.6) and the Gaussian midline (~114), and it sits in the lower half of the Bollinger band. The 90-day low is ~88.
- **Weight:** 0.05. The bounce is failing below resistance.
- **Change mind:** Above ~108.6 I would add. Below ~88 I would stay flat.

## 30fcb07d5c (BTC)
- **Read:** Price is coiling around EMA50 (~100.5) and above EMA20 (~98.3), but under the Gaussian midline (~102.7). Volatility is low (ATR 2.7%, Bollinger width 10%). Stoch RSI is high at 0.84. The 90-day low is ~89 and EMA200 is ~114.5.
- **Weight:** 0.25. The structure is neutral and improving, but the midline is not yet reclaimed.
- **Change mind:** Above ~103 I would raise to about 0.5. Below ~98 I would cut to near zero.

## ad60374ff3 (LINK)
- **Read:** Price is above EMA20 (~96.2), EMA50 (~97.3) and the Gaussian midline (~98.4), with a strong MACD and 4.9% gained over 7 days. ADX is low at 14, so the trend isn't established yet. EMA200 is ~118 and the 90-day high ~130.
- **Weight:** 0.45. The structure is constructive but the trend is unconfirmed.
- **Change mind:** A close below ~96 would cut it.

## 82b0f056f8 (LTC)
- **Read:** A sharp 7% weekly push into the upper Bollinger band (0.98), with stoch RSI pinned at 1.0 and RSI at 62. Price is above EMA20 (~95.3), EMA50 (~97.4) and the Gaussian midline (~98.9). EMA200 is ~121.
- **Weight:** 0.4. The reclaim is positive, but the short-term move is overextended and likely to pull back.
- **Change mind:** A close below ~97 would cut it. Holding above ~99 after a pullback would justify adding.

## 1ea589ebf7 (SOL)
- **Read:** Price is pulling back to sit right on EMA20 and EMA50 (~100.1 and ~100.3) and on the Gaussian midline (~99.0). The Gaussian slope is flattening (-0.51, the least negative in the set), and the window is up 9.5% over 30 days. The MACD histogram has turned negative and stoch RSI is low, so this is a test of support. The 90-day low is ~79 and EMA200 is ~123.
- **Weight:** 0.3. This is a retest of support in a market that is trying to base.
- **Change mind:** A close below ~99 (Gaussian midline) would cut it. Above ~104 with MACD turning back up would take it toward 0.5.

{"b01155f2bd (XRP)": 0.1, "91278f6cd9 (DOGE)": 0.0, "809cf88e9c (DOT)": 0.0, "4f4856a40d (ADA)": 0.1, "8e601ef4b7 (ETH)": 0.5, "6017dda407 (AVAX)": 0.05, "30fcb07d5c (BTC)": 0.25, "ad60374ff3 (LINK)": 0.45, "82b0f056f8 (LTC)": 0.4, "1ea589ebf7 (SOL)": 0.3}

## Entscheidung 2026-07-26

## Strategy

Every window sits below its 200-day EMA, so I treat each one as a long-term downtrend. Weight is capped around 0.4 until price reclaims the 200-day EMA. Within that cap, I add weight when price holds above the 20/50-day EMAs and the Gaussian midline. I cut weight when the Gaussian slope is steeply negative, when price is pinned near the 180-day low, or when a rally looks stretched (stoch_rsi near 1, bollinger_pos above 0.8, bearish RSI divergence).

## d4b423c315 (LINK)
- **Market read:** A sharp counter-trend rally: +20% over 30 days, price above EMA20 (~94.3) and EMA50 (~93.5). The Gaussian slope is still negative, and price remains well below EMA200 (~110.9) and the 90-day high (~123). ADX of 15 means the trend is weak. Short-term it is stretched: stoch_rsi 1.00, bollinger_pos 0.85, 10% above the 30-day VWAP.
- **Weight: 0.35.** Momentum is real, but this is likely a bear-market rally into resistance, and a pullback is likely.
- **Change my mind:** below ~93.5, cut to 0. Above ~111 (EMA200 reclaimed), raise to 0.7 or more.

## ce75c35c93 (DOGE)
- **Market read:** A downtrend with ADX 31. Price is 28% under EMA200 and below EMA50 (~106.7), the Gaussian slope is -2.8%, and price sits near the 180-day low (90-day low ~92.9). The bounce to EMA20 is minor.
- **Weight: 0.05.** The trend is firmly down, and there is no reversal structure.
- **Change my mind:** a reclaim of ~107 (EMA50) would lift the weight to around 0.3.

## 3b2af95b31 (SOL)
- **Market read:** Neutral consolidation. Price is flat against EMA20/50 (~99.4/99.7), slightly above a flat Gaussian midline, and ADX is 12. Price is well off the 90-day low (~78) but far below EMA200 (~121). The MACD histogram is slightly negative.
- **Weight: 0.3.** The base is stabilizing, but there is no trend.
- **Change my mind:** below ~97, cut to 0.1. A push above ~105 with rising ADX would justify 0.5.

## c4eb36ab2a (LTC)
- **Market read:** A rally of +14% over 30 days, with price above EMA20 (~96) and EMA50 (~96.3). There is bearish RSI divergence, stoch_rsi is 0.98, and the Gaussian slope is -1.1%. EMA200 is around 117.8.
- **Weight: 0.25.** The divergence and the stretched reading argue for less exposure than the trend alone suggests.
- **Change my mind:** below ~96, cut to 0. Above ~108 with the divergence cleared, raise to 0.45.

## 59d570873d (AVAX)
- **Market read:** A bounce of +4% over 7 days, still below EMA50 (~102.5) and the Gaussian midline. The Gaussian slope is -2.3%, and EMA200 is far overhead (~143). Volatility is high (ATR 4.5%).
- **Weight: 0.1.** This is a bounce inside a downtrend.
- **Change my mind:** a close above ~103 (EMA50) would justify around 0.3. Below ~95, go to 0.

## 0929734703 (DOT)
- **Market read:** A deep downtrend. Price is 41% under EMA200, below EMA50 (~109.8), and 14.5% below a steeply falling Gaussian midline. It sits at 0.04 of the 180-day range, just above the 90-day low (~95.1).
- **Weight: 0.0.** There are no signs of a reversal.
- **Change my mind:** a reclaim of ~110 would justify 0.2. If price holds above ~95 and a bullish divergence forms, consider 0.1.

## 2afbbfde7d (XRP)
- **Market read:** A low-volatility drift (bollinger_width 6.6%, ADX 10). Price sits just above EMA20 but below EMA50 (~102.4) and the falling Gaussian midline. It is near the bottom of the 180-day range, with the 90-day low around 90.7.
- **Weight: 0.1.** The tape is quiet inside a downtrend.
- **Change my mind:** above ~102.5, raise to 0.3. Below ~91, go to 0.

## fcd40c93da (ETH)
- **Market read:** A strong rally of +24% over 30 days, with price above EMA20 (~94.8) and EMA50 (~94). There is bearish RSI divergence, price is 9% over the 30-day VWAP, and the Gaussian slope is negative. Price is below EMA200 (~111.7) and the 90-day high (~124).
- **Weight: 0.3.** The momentum is good, but the divergence and overextension inside a larger downtrend argue for caution.
- **Change my mind:** below ~94, cut to 0. Above ~112, raise to 0.6.

## 8679b1f567 (BTC)
- **Market read:** Orderly. Price is modestly above EMA20 (~98.5) and EMA50 (~99.5), sitting on the Gaussian midline. RSI is 55, ADX is 23, ATR is a low 2.6%, and nothing is overextended. EMA200 is around 112.5.
- **Weight: 0.35.** This is the healthiest structure in the set, though it is still below the long-term trend.
- **Change my mind:** below ~98, cut to 0.1. Above ~112.5, raise to 0.7.

## 980607ef44 (ADA)
- **Market read:** A 30-day bounce of +12% that has stalled. Price is back below EMA20, below EMA50 (~105.7), and 38% under EMA200. The Gaussian slope is -2.7%, and volatility is high (ATR 5.1%).
- **Weight: 0.05.** The bounce is fading inside a steep downtrend.
- **Change my mind:** above ~106, raise to 0.25. Below ~90, stay at 0.

{"d4b423c315 (LINK)": 0.35, "ce75c35c93 (DOGE)": 0.05, "3b2af95b31 (SOL)": 0.3, "c4eb36ab2a (LTC)": 0.25, "59d570873d (AVAX)": 0.1, "0929734703 (DOT)": 0.0, "2afbbfde7d (XRP)": 0.1, "fcd40c93da (ETH)": 0.3, "8679b1f567 (BTC)": 0.35, "980607ef44 (ADA)": 0.05}

## Entscheidung 2026-08-02

**1. Strategy**

Every window trades below its 200-day EMA, so I treat each one as a long-term downtrend and cap exposure at about 0.5. Within that cap, I add weight when price holds above the 50-day EMA and the Gaussian midline is flat or rising. I cut to near zero when the midline slope is steeply negative, price sits near the 180-day lows, or a move is a stretched bear-market rally.

**2. Windows**

**8de6271142 (BTC)**
- **Read:** Price is mildly below the EMA20 (100.7) and EMA50 (101.8), and far below the EMA200 (114.7). The Gaussian slope is negative (−0.63), the 90-day low is 90.9 and the 90-day high is 130.4. Momentum is soft (stoch 0.21, negative MACD), but ADX of 22 shows no strong trend. This looks like a drift lower inside a downtrend.
- **Weight: 0.15.** A small toe-hold, because the structure isn't collapsing.
- **Change my mind:** A close above 102 (reclaiming the EMA50) raises the weight. A break below 91 goes flat.

**d479d70c51 (LINK)**
- **Read:** Price is above the EMA20 and the EMA50 (98.6), and above the Gaussian midline (+3.5) with only a slightly negative slope. The 30-day return is +5%. The 7-day pullback (−5%) looks like a retest of support, and ADX is low. The EMA200 is far above at 115.5, and the 90-day low is 83.5.
- **Weight: 0.35.** Medium-term structure is constructive, but the long-term trend is still down.
- **Change my mind:** A close below 98.5 (losing the EMA50) cuts the weight.

**090a52c74e (ADA)**
- **Read:** Price spiked 14% in a week to 1.58 on the Bollinger scale, 12% above the EMA20 (89.1). The midline slope is steeply negative (−1.89), and the EMA200 is far above at 137.7. Price is only at 0.29 of its 180-day range. This is a stretched relief rally in a bear trend and is prone to fade back toward 89–92.
- **Weight: 0.15.**
- **Change my mind:** Holding above 105 with follow-through raises the weight. A close below 92 (the EMA50) goes flat.

**b4798f6564 (SOL)**
- **Read:** Price is below all EMAs (EMA50 at 103.0, EMA200 at 124.4), and the 30-day return is −10.6%. The midline slope is just turning positive (+0.13), and ADX of 13 shows no trend. This is a weak range in a downtrend, with the 90-day low at 81.6.
- **Weight: 0.15.**
- **Change my mind:** A close above 103 raises the weight. Below 95 goes flat.

**fb1c3ee84c (LTC)**
- **Read:** Price is below all EMAs (EMA50 at 102.7), the 7-day return is −6.6%, and it is near the lower Bollinger band. The midline slope is negative and price sits at 0.25 of its 180-day range. The 90-day low is 87.9.
- **Weight: 0.10.**
- **Change my mind:** A close above 102.7 raises the weight. Below 88 goes flat.

**18b563b0ea (DOT)**
- **Read:** This is a deep downtrend: 41% below the EMA200, with a Gaussian midline at 116.4 sloping −2.78. Price is at 0.06 of its 180-day range, and the 90-day low is 93.0. The stoch reading of 0.99 is only a dead-cat bounce inside the trend.
- **Weight: 0.0.**
- **Change my mind:** A reclaim of 109.5 (the EMA50) would bring it back into consideration.

**4b70936fea (XRP)**
- **Read:** Price is below the EMA50 (103.3), and the midline slope is negative (−1.2). ADX of 10.8 shows a directionless grind near the lows (0.12 of the 180-day range). The 90-day low is 92.9.
- **Weight: 0.05.**
- **Change my mind:** A close above 103.3 raises the weight. Below 93 goes flat.

**397760a5e7 (DOGE)**
- **Read:** This is a strong downtrend (ADX 29.6) with a midline slope of −2.54. Price is 7% below the EMA50 (107.8) and only 4.7% above the 90-day low (95.5). The positive MACD histogram reflects a small bounce, not a reversal.
- **Weight: 0.0.**
- **Change my mind:** Reclaiming 107.8 would reopen the long side.

**821973dbfa (AVAX)**
- **Read:** Price sits just above the EMA20 but below the EMA50 (103.6) and 30% below the EMA200. The midline slope is negative (−1.74) with moderate ADX. Price is at 0.18 of its 180-day range, and the 90-day low is 86.7.
- **Weight: 0.05.**
- **Change my mind:** A close above 103.6 raises the weight. Below 94 goes flat.

**885905eb8c (ETH)**
- **Read:** Price is above the EMA20 and the EMA50 (98.1), and 5.4% above a flat Gaussian midline (slope +0.01). The 30-day return is +7.2%, and the 7-day dip of −3.5% looks like a pullback to support. The EMA200 is at 114.8, and the 90-day low is 79.9. This is the most constructive structure of the set, still capped by the long-term downtrend.
- **Weight: 0.4.**
- **Change my mind:** A close below 98 cuts the weight. Above 115 (the EMA200) raises it substantially.

{"8de6271142 (BTC)": 0.15, "d479d70c51 (LINK)": 0.35, "090a52c74e (ADA)": 0.15, "b4798f6564 (SOL)": 0.15, "fb1c3ee84c (LTC)": 0.1, "18b563b0ea (DOT)": 0.0, "4b70936fea (XRP)": 0.05, "397760a5e7 (DOGE)": 0.0, "821973dbfa (AVAX)": 0.05, "885905eb8c (ETH)": 0.4}

## Entscheidung 2026-08-09

## 1. Strategy

Every window trades below its 200-day EMA, so all of them are in a long-term bear regime. My rule is to follow the medium-term trend and cap exposure. I own nothing unless price is above the 50-day EMA and the Gaussian midline is flat or rising. I scale up only when momentum (30-day return, MACD) confirms. Strong downtrends sitting near their 180-day lows get 0, and nothing gets more than about 0.6 while price is below the 200-day EMA.

## 2. Windows

### 8b97fd0f38 (AVAX)
- **Read:** Downtrend. Price is below EMA20 (≈101.4), EMA50 (≈104.7) and the Gaussian midline (≈106.0). The midline is falling at −1.33% per 5 days. EMA200 is far above at ≈144. The 90-day low is ≈88.5. ADX of 16 shows a weak trend, and the slightly positive MACD only shows the decline slowing.
- **Weight: 0.1.** There is no trend support, so this is only a token position on the stalled decline.
- **Change my mind:** A close above 105 (reclaiming EMA50) would make me add. A close below 88.5 would take me to 0.

### 0b54f4268c (XRP)
- **Read:** Price is pinned near the bottom of its range (pos 0.03, only 2% above the 90-day low at ≈97.9). It is below EMA20 (≈103.6), EMA50 (≈107.3) and the Gaussian midline (≈109.4, falling). MACD is negative.
- **Weight: 0.0.** The trend is down, price sits at its lows, and nothing shows a turn.
- **Change my mind:** A close above 107.3 (EMA50).

### 1be95e5e19 (SOL)
- **Read:** Recovery attempt. Price is above EMA20 (≈97.9), EMA50 (≈98.9) and the Gaussian midline (≈99.2), and the midline has flattened. MACD is positive. However, stoch RSI is pinned at 1.0 and ADX is only 13. Overhead resistance is EMA200 at ≈118.5 and the 90-day high at ≈128.
- **Weight: 0.4.** The structure has improved, but the trend is unconfirmed and short-term momentum is stretched.
- **Change my mind:** A close below 98 (losing EMA50 and the midline).

### f801df940e (DOGE)
- **Read:** Strong downtrend: ADX 28.5 and the Gaussian slope is −2.23. Price is below EMA50 (≈107.8) and the Gaussian midline (≈112.6), only 2.5% above the 90-day low (≈97.6). The mildly positive MACD is just a pause.
- **Weight: 0.0.**
- **Change my mind:** A close above 108 (EMA50).

### b2dd668505 (LTC)
- **Read:** Neutral and range-bound. Price sits on EMA20 (≈100) and just under EMA50 (≈100.6), with the Gaussian midline (≈99.7) nearly flat and drifting down. ADX of 12.8 means there is no trend. The 90-day low is ≈86.4.
- **Weight: 0.25.** Partial exposure fits a basing market that has not turned yet.
- **Change my mind:** A close above 101 would make me add. A close below 97 would take me to 0.

### 2ed7a3eaa6 (BTC)
- **Read:** Price is above EMA20 (≈99.1), EMA50 (≈99.7) and the Gaussian midline (≈99.1), with narrow bands (5.9%) suggesting a coming breakout. The midline is still sloping slightly down (−0.32). EMA200 is at ≈111.4.
- **Weight: 0.35.** The structure is positive but unconfirmed, with stoch RSI near 1.
- **Change my mind:** A close below 99 (losing EMA50 and the midline).

### 85a48a6979 (ADA)
- **Read:** Sharp bounce: +16.7% over 30 days, MACD strongly positive, ADX 25. Price is above EMA20 (≈94.0) and EMA50 (≈92.3). It is extended, though: 9.9% above the 30-day VWAP and 13% above a Gaussian midline (≈88.5) that is still falling. EMA200 sits well overhead at ≈132, and volatility is high (ATR 5.2%).
- **Weight: 0.4.** I respect the momentum but stay sized down for the extension and the bear regime.
- **Change my mind:** A close below 94 (EMA20).

### 734d26b024 (DOT)
- **Read:** Deep downtrend: 40% below EMA200 and a Gaussian slope of −2.48. Price is below EMA50 (≈108) and the midline (≈112.4), near its range lows. The 90-day low is ≈93.
- **Weight: 0.0.**
- **Change my mind:** A close above 108 (EMA50).

### f646457166 (LINK)
- **Read:** Flat. Price is slightly below EMA20 and EMA50 (both ≈100.8) but above a Gaussian midline (≈99.2) that is rising slightly (+0.23). The 30-day return is positive, but ADX of 12 shows no trend, and MACD is mildly negative after a pullback.
- **Weight: 0.3.** The midline's slope supports some exposure, but I'm waiting for EMA reclaim.
- **Change my mind:** A close above 101 would make me add. A close below 99 would take me to 0.

### 7b9e8ebda6 (ETH)
- **Read:** This is the best structure of the set. Price is above EMA20 (≈98.7), EMA50 (≈97.5) and the Gaussian midline (≈94.3), and the midline is rising (+0.53). The 30-day return is +6.3% and ADX is building at 19. Resistance is EMA200 at ≈112.4 and the 90-day high at ≈122.5. The MACD histogram is slightly negative, which is a minor consolidation.
- **Weight: 0.55.** The trend is intact, with exposure capped because price is still below EMA200.
- **Change my mind:** A close below 97.5 (EMA50).

{"8b97fd0f38 (AVAX)": 0.1, "0b54f4268c (XRP)": 0.0, "1be95e5e19 (SOL)": 0.4, "f801df940e (DOGE)": 0.0, "b2dd668505 (LTC)": 0.25, "2ed7a3eaa6 (BTC)": 0.35, "85a48a6979 (ADA)": 0.4, "734d26b024 (DOT)": 0.0, "f646457166 (LINK)": 0.3, "7b9e8ebda6 (ETH)": 0.55}

## Entscheidung 2026-08-16

# Analysis

## 1. Strategy

Price is above or below the 200-day EMA and the Gaussian-channel slope tells me the primary trend, and I only take meaningful exposure when the structure is constructive (price above a rising Gaussian midline, or a confirmed breakout toward the EMA200). Below the EMA200 with a falling Gaussian slope, I stay near flat even when the market is oversold, because oversold readings in downtrends tend to persist. Each window gets a level that would upgrade it (reclaiming a key moving average) or invalidate it (losing the nearest support).

## 2. Windows

### e025a6fcaf (XRP)
**Read:** This is an established downtrend. Price sits at the 180-day low (pos 0.01), 26.5% below the EMA200 (~136), and the Gaussian slope is falling at -0.94. RSI is 34 and stoch RSI is 0, which is oversold, but there is no divergence. The 90-day low at ~99.2 is right under price. EMA20 is ~104.3 and EMA50 ~108.7.

**Weight: 0.05.** I see no sign of a reversal. A bounce is possible from oversold, but the trend argues against owning it.

**Change of mind:** A close above ~104.3 (EMA20) would justify a small long. A break below ~99.2 confirms I should stay flat.

### 812f8f29a9 (AVAX)
**Read:** The longer-term downtrend is intact: 30% below the EMA200 (~143) and the Gaussian slope is -1.01. Price has bounced 11% off the 90-day low (~89.8). ADX of 15 and narrow Bollinger bands point to consolidation. EMA50 is ~104.9.

**Weight: 0.10.** This is basing, but it is still below every key average.

**Change of mind:** A reclaim of ~104.9 (EMA50) would move me toward 0.3. A drop below ~95 means the base failed.

### 46d1834492 (ETH)
**Read:** The structure is neutral to positive. Price is above the EMA50 (~99.5) and above a rising Gaussian midline (~96.9, slope +0.72), but 11.8% below the EMA200 (~113.4). The weekly dip has stoch RSI at 0 while RSI is near 50, which looks like a pullback inside a recovery. The 90-day high is ~114.9.

**Weight: 0.40.** The intermediate trend is constructive, but the EMA200 overhead caps conviction.

**Change of mind:** A break below ~96.9 (Gaussian midline) would cut me to 0.1. A push through ~105 toward the EMA200 would raise me to 0.6.

### e829345203 (LTC)
**Read:** The market is drifting sideways. The Gaussian slope is flat (+0.01), ADX is 11.8 (no trend), and price is 18.6% below the EMA200 (~123). It sits just under the EMA20 (~101.8) and EMA50 (~103.0). The 90-day low is ~89.0.

**Weight: 0.20.** There is no trend to ride, and the market sits below the long-term average.

**Change of mind:** A close above ~103 (EMA50) would raise me to 0.4. Losing ~95 would take me flat.

### f3ab2a70f7 (DOT)
**Read:** This is a steep downtrend. Price is 41% below the EMA200 (~170), the Gaussian slope is -2.05, and price is at the 180-day low, with the 90-day low at ~97.8. There is a bullish RSI divergence with stoch RSI at 0, an early exhaustion hint. EMA20 is ~104.6 and the Gaussian midline ~114.8.

**Weight: 0.10.** The divergence earns a token position, but the trend is strongly negative.

**Change of mind:** A reclaim of ~104.6 (EMA20) would confirm the divergence and raise me to 0.3. A close below ~97.8 would take me flat.

### d2b20b4511 (SOL)
**Read:** The market is range-bound in the middle of its 180-day range (0.38). MACD histogram has turned positive, ADX is 9.4 (no trend), and the Gaussian slope is slightly negative (-0.13). Price hugs the EMA20 (~100.7) and EMA50 (~101.2) and is well below the EMA200 (~119.8).

**Weight: 0.30.** Momentum is improving, but the trend is weak overall.

**Change of mind:** A close above ~101.2 with a rising Gaussian slope would raise me to 0.5. A break below ~96 would cut me to 0.1.

### c1fd5a8fe6 (BTC)
**Read:** This is a mild downtrend. Price is below the EMA20 (~101.4), EMA50 (~102.4), and EMA200 (~114), and the Gaussian slope is slightly negative. Stoch RSI is 0 near the lower band, and the 90-day low is ~91.9. Volatility is low (ATR 1.95%).

**Weight: 0.15.** The trend is bearish with no reversal signal.

**Change of mind:** A reclaim of ~102.4 would raise me to 0.35. A break below ~95 would take me flat.

### 54c2fb58f3 (DOGE)
**Read:** This is a downtrend with a strongly falling Gaussian slope (-1.90). Price sits near the 180-day low (0.04) with the 90-day low at ~97.2. There is a small MACD uptick and a tight Bollinger squeeze, so a move is coming, but the bias is down. EMA50 is ~105.7 and EMA200 ~138.

**Weight: 0.05.** A squeeze inside a downtrend more often resolves lower.

**Change of mind:** A close above ~105.7 (EMA50) would raise me to 0.3. A close below ~97.2 confirms flat.

### a7a6f940f5 (LINK)
**Read:** This is a strong breakout: +14.7% in 7 days, above the EMA50 (~89.7) and the Gaussian midline (~86.9, rising), and testing the EMA200 at ~101.6. ADX is 25 and rising. The market is overbought (RSI 69, above the upper band), so a pullback is likely. The 90-day high is ~106.8.

**Weight: 0.60.** Momentum and the trend shift are real, but price is stretched short term and the EMA200 is resistance.

**Change of mind:** A weekly close above ~101.6 and then ~106.8 would raise me to 0.8. A drop below ~92 (EMA20) would cut me to 0.25.

### fb40c6529e (ADA)
**Read:** The market fell sharply this week (-10.1%) after a 30-day rally, and volatility is very wide (Bollinger width 26.9%). Price is still just above a flat Gaussian midline (~98.3) but 30% below the EMA200 (~144). MACD has rolled over hard. EMA20 is ~104.1.

**Weight: 0.15.** Momentum is broken, and the rally looks like a counter-trend bounce.

**Change of mind:** A loss of ~98.3 (Gaussian midline) would take me flat. A reclaim of ~104.1 would raise me to 0.35.

{"e025a6fcaf (XRP)": 0.05, "812f8f29a9 (AVAX)": 0.1, "46d1834492 (ETH)": 0.4, "e829345203 (LTC)": 0.2, "f3ab2a70f7 (DOT)": 0.1, "d2b20b4511 (SOL)": 0.3, "c1fd5a8fe6 (BTC)": 0.15, "54c2fb58f3 (DOGE)": 0.05, "a7a6f940f5 (LINK)": 0.6, "fb40c6529e (ADA)": 0.15}

## Entscheidung 2026-08-23

## 1. Strategy

Every window is a sharp short-term rally, so the question is whether it is a **trend continuation or a relief rally inside a downtrend**. I size up when price is above the 200-EMA and the Gaussian midline is rising. I size down when price is below the 200-EMA or the midline is falling. I also trim when the move is a vertical blow-off (RSI > 84, close above the upper Bollinger band), because a pullback toward the 20-EMA is then likely before any continuation.

## 2. Windows

### dd2449eb15 (LTC)
- **Read:** +18% in a week, pushing into the 200-EMA at ~103 from below. The Gaussian midline is flat, so the regime is neutral. Overhead resistance is the 200-EMA at ~103 and the 90-day high at ~106. Support is the 20-EMA at ~90.
- **Weight: 0.4.** The rally is constructive but runs straight into the major moving average.
- **Change my mind:** a close above 106 would justify more weight; a close below 90 would take me flat.

### db38ef2395 (LINK)
- **Read:** A strong established uptrend, about 20% above the 200-EMA (~83). The midline is rising (+0.81) and ADX is 47. It is stretched at 40% above the Gaussian, but trend strength is the dominant feature. The 90-day high is at ~109 and the 20-EMA at ~85.
- **Weight: 0.7.** This is a high-quality trend; I hold back a little for the extension.
- **Change my mind:** below 85.

### 43f7b751e6 (AVAX)
- **Read:** A relief rally in a downtrend. Price is 15% below the 200-EMA (~117), the midline is falling (−0.76) and the asset sits at 0.40 of its 180-day range. Overhead levels are ~117 and the 90-day high at ~125.
- **Weight: 0.2.** Counter-trend bounces like this usually fade.
- **Change my mind:** reclaiming 117 would make it more bullish; a close below 90 (20-EMA) would take me flat.

### c56fc6fbcd (DOT)
- **Read:** A classic bear-market rally. Price is 26% below the 200-EMA (~136), the midline is falling steeply (−1.72) and the asset is near the bottom of its 180-day range (0.20). The 20-EMA is at ~89.
- **Weight: 0.1.**
- **Change my mind:** only a sustained move above ~115 would change the structure; below 89, flat.

### 5a8f86e33b (ADA)
- **Read:** A recovery in progress: +38% over 30 days and the midline has turned up (+0.75). Price is still 9% below the 200-EMA (~109), so the major trend has not flipped yet. The 90-day high is at ~114 and the 20-EMA at ~86.
- **Weight: 0.45.** The regime is improving, but resistance sits just overhead.
- **Change my mind:** above 110 I would go higher; below 86, cut.

### fcac1927e7 (DOGE)
- **Read:** A vertical blow-off: +34% in a week, RSI 85, close well above the upper band (1.17). This is happening while the midline is still falling (−1.49), with price just under the 200-EMA (~102). The 20-EMA is far below at ~82.5.
- **Weight: 0.3.** Mean-reversion risk is high and the trend is unconfirmed.
- **Change my mind:** holding above 102 with the midline turning up would raise the weight; below 88, flat.

### 8e55a1da11 (XRP)
- **Read:** An extreme move: +53% in a week, RSI 87, 30% above the 20-EMA (~77). Price is above the 200-EMA (~89), but the midline is still declining (−0.98). The 90-day high is at ~112.
- **Weight: 0.4.** Momentum is real, but giving back a large part of the move is likely.
- **Change my mind:** below 89 (the 200-EMA), flat; consolidation above 100 with the midline turning up would lift the weight.

### b8e237b90f (ETH)
- **Read:** A clean uptrend. Price is above the 200-EMA (~87), the midline is rising (+0.81), the asset sits at 0.92 of its 180-day range and the 90-day high at ~103 is close. Volatility is moderate (ATR 3.9%).
- **Weight: 0.75.** The structure is best-in-class; I trim only for overbought readings.
- **Change my mind:** below 85 (20-EMA).

### ec4f33eaec (BTC)
- **Read:** Price is above the 200-EMA (~92), near the top of its range and just under the 90-day high (~102). The midline is flat. Volatility is low (ATR 2.8%) but RSI is 81 and price is above the upper band.
- **Weight: 0.55.** A breakout setup, but overbought.
- **Change my mind:** a close above 102.5 would justify more; below 92, flat.

### 727211dcd0 (SOL)
- **Read:** Price is above the 200-EMA (~93.5) at 0.83 of its 180-day range, with the midline flat. It is very overbought (RSI 84, stoch 1.0, above the upper band). The 90-day high is at ~108 and the 20-EMA at ~86.
- **Weight: 0.5.**
- **Change my mind:** below 93.5, flat; a breakout above 108 would justify more.

## 3. Weights

{"dd2449eb15 (LTC)": 0.4, "db38ef2395 (LINK)": 0.7, "43f7b751e6 (AVAX)": 0.2, "c56fc6fbcd (DOT)": 0.1, "5a8f86e33b (ADA)": 0.45, "fcac1927e7 (DOGE)": 0.3, "8e55a1da11 (XRP)": 0.4, "b8e237b90f (ETH)": 0.75, "ec4f33eaec (BTC)": 0.55, "727211dcd0 (SOL)": 0.5}

## Entscheidung 2026-08-30

**1. Strategy**

I follow the trend, using the 200-day EMA as the regime filter. Above it, with EMA20 > EMA50 structure and a rising Gaussian midline, I hold 0.6–0.8. I trim for overextension or a fading pullback. Below the 200-EMA I stay small, 0–0.3, even on strong 30-day bounces, because those are counter-trend rallies until the 200-EMA is reclaimed.

**2. Windows**

**2b34d4af44 (AVAX)**
- **Read:** Bear regime: EMA200 sits at ~123.8, 19% overhead. A 30-day bounce stalled at the EMA20 (~99.7), with the EMA50 at ~97.1 just below. Gauss slope is turning down, and the 90d high (~125.8) is far away.
- **Weight: 0.2.** This is a counter-trend bounce losing steam (stoch_rsi 0.25).
- **Change my mind:** below 97 I go flat; a close above ~110 would make me raise the weight.

**a6ae68c4d3 (ADA)**
- **Read:** Bear regime, with EMA200 ~127.4. Price fell 15% this week and lost the EMA20 (~104). It is sitting on the EMA50 (~99.2). Gauss slope is still positive, and the 90d low is far below at ~71.7.
- **Weight: 0.15.** Momentum has broken (negative MACD, below VWAP) inside a downtrend.
- **Change my mind:** below 99 I go flat; reclaiming 104 would lift me to ~0.3.

**880429751a (DOGE)**
- **Read:** Bear regime, with EMA200 ~115.5. Price is holding the EMA20 (~99.5) after a -12% week. EMA50 is at ~95.5, and the gauss slope is negative. Upside is capped near the 90d high of ~123.5.
- **Weight: 0.25.** The structure is holding, but the bigger trend is down.
- **Change my mind:** below 95.5 I go to 0; above ~108 I add.

**f11b04b29f (XRP)**
- **Read:** Price just reclaimed the EMA200 (~99.5) after a +28% month. EMA20 is ~95.1 and EMA50 ~88.3, and ADX 45 shows a strong trend. This week pulled back 10.7%, and the gauss slope is flat. The 90d high is at ~125.
- **Weight: 0.5.** Regime is turning positive but has not been confirmed.
- **Change my mind:** below 95 I cut to 0.2; above ~108 I go to 0.75.

**248b72051a (SOL)**
- **Read:** Strong uptrend. EMA20 is ~90.9, EMA200 ~88.6, and EMA50 ~82.9. ADX is 47 and the gauss slope is rising. Price is close to the 90d high (~108.7) but extended: +12% vs VWAP and +10% vs EMA20.
- **Weight: 0.7.** The trend is intact, trimmed for extension.
- **Change my mind:** below ~91 (EMA20) I drop to 0.4.

**841806dc63 (LINK)**
- **Read:** Uptrend with ADX near 60 and a steep gauss slope. EMA20 is ~95.5, EMA200 ~87.5, and EMA50 ~86.4. Stoch_rsi is 0, so this is a shallow pullback. The 90d high is ~113.
- **Weight: 0.7.** It is a dip within a strong trend, but momentum has flattened (MACD hist ~0).
- **Change my mind:** below 95.5 I reduce to 0.4; below 87 I go flat.

**d29524354d (BTC)**
- **Read:** A clean, low-volatility uptrend (ATR 3%). EMA20 is ~94.7, EMA200 ~92.9, and EMA50 ~89.3. Price is consolidating just under the 90d high of ~104.9.
- **Weight: 0.8.** It is an orderly trend near its highs.
- **Change my mind:** below 94.7 I reduce to 0.5; a breakout above 105 confirms the position.

**03e8056d3f (LTC)**
- **Read:** Bear regime, with EMA200 ~111.7. Price sits between the EMA50 (~98.3) and EMA20 (~100.9), and momentum is fading. The 90d high is ~115.6 and the 90d low ~82.
- **Weight: 0.25.** It is a neutral pullback inside a downtrend.
- **Change my mind:** below 98 I go to 0; above 111.7 I go to 0.5.

**01cf6d8206 (ETH)**
- **Read:** Strong uptrend. EMA20 is ~94.3, EMA200 ~89.4, and EMA50 ~86.4. The gauss slope is rising, price is close to the 90d high (~106.2), and pos_in_180d is 0.86.
- **Weight: 0.8.** Trend and structure are healthy, and the pullback is mild.
- **Change my mind:** below 94.3 I cut to 0.5.

**35c7800a9a (DOT)**
- **Read:** Deep downtrend. EMA200 is ~150, 33% overhead. Price is below the EMA20 (~102.9), EMA50 (~103.5), and the falling gauss midline (~102). It is near the 180d low (pos 0.10), with the 90d low at ~88.3.
- **Weight: 0.0.** There is no long setup.
- **Change my mind:** a reclaim above ~104 would justify 0.15; below 88 confirms staying flat.

```json
{"2b34d4af44 (AVAX)": 0.2, "a6ae68c4d3 (ADA)": 0.15, "880429751a (DOGE)": 0.25, "f11b04b29f (XRP)": 0.5, "248b72051a (SOL)": 0.7, "841806dc63 (LINK)": 0.7, "d29524354d (BTC)": 0.8, "03e8056d3f (LTC)": 0.25, "01cf6d8206 (ETH)": 0.8, "35c7800a9a (DOT)": 0.0}
```

## Entscheidung 2026-09-06

**1. Strategy**

I follow the trend. I stay mostly long when price is above the EMA50 and EMA200 and the Gaussian midline is rising. I cut the position when price is below the EMA200, which acts as overhead resistance, or when a short-term spike is stretched and shows bearish RSI divergence. I size by how well trend strength (ADX, slope) holds up against overextension.

**2. Windows**

## 4ba4cb22f8 (XRP)
- **Read:** Strong uptrend. Price is above EMA20 (94.5), EMA50 (87.6) and EMA200 (95.1), and the Gaussian slope is +1.76. ADX is 43, so the trend is strong.
- **Momentum:** Short-term momentum is cooling, with MACD histogram negative and stoch RSI at 0.15. This is a pause, not a reversal.
- **Levels:** The 90-day high is about 119.5, which leaves room to run.
- **Weight: 0.7.** The trend is intact and the pullback is digesting gains.
- **Change mind:** a close below 94, which would lose both EMA20 and EMA200.

## ce01140c68 (DOT)
- **Read:** Price jumped 19.5% in a week but sits well below the EMA200 (123.5). The Gaussian slope is negative (-0.34) and ADX is weak at 21.
- **Momentum:** Price is at the upper Bollinger band, stoch RSI is 1.0, and there is bearish divergence. This looks like a bear-market rally into resistance.
- **Levels:** The 90-day high is about 107.
- **Weight: 0.3.**
- **Change mind:** a close above 107 would make me add. A close below 89 (EMA20) would take me to flat.

## 363b3ecbea (DOGE)
- **Read:** A recovery trend with ADX at 39 and a rising Gaussian midline. Price is above EMA20 (92.3) and EMA50 (88.2).
- **Levels:** The EMA200 (103.5) is just overhead, and the 90-day high is about 111.
- **Momentum:** Neutral, with stoch RSI at 0.5 and MACD histogram flat.
- **Weight: 0.5.** Constructive, but price has not yet reclaimed the EMA200.
- **Change mind:** a close above 103.5 would make me add. A close below 92 would make me reduce.

## cd6a808bc4 (BTC)
- **Read:** A clean, low-volatility uptrend. ADX is 48, ATR is 2.9%, and price is above all EMAs (EMA20 at 95.2, EMA200 at 90.5).
- **Levels:** Price is at the 90th percentile of its 180-day range. The 90-day high is about 102.5.
- **Momentum:** A mild pullback in momentum, which is healthy.
- **Weight: 0.85.**
- **Change mind:** a close below 95 (EMA20).

## fa0b8c2625 (ETH)
- **Read:** A strong uptrend. ADX is 49 and the Gaussian slope is +2.77. Price is above EMA20 (94.4), EMA50 (86.7) and EMA200 (86.7).
- **Levels:** Price is near the 90-day high of 102. Stoch RSI has reset, so price is consolidating near highs.
- **Weight: 0.85.**
- **Change mind:** a close below 94.

## 1ec41d8ea7 (SOL)
- **Read:** A powerful trend. ADX is 51, the 30-day gain is 45%, and price is 36% above the Gaussian midline. That makes it extended.
- **Momentum:** Momentum is cooling without divergence.
- **Levels:** EMA20 is 91.7 and the 90-day high is 103.8.
- **Weight: 0.75.** The trend is intact; the stretch keeps the weight slightly lower.
- **Change mind:** a close below 92.

## 92c82f6efc (LTC)
- **Read:** A breakout attempt. Price is pressing the 90-day high (100.9) and is above EMA200 (97.2) and EMA20 (91.2). ADX is 33.
- **Momentum:** RSI is 71, stoch RSI is 1.0, and there is bearish divergence, so price is short-term overbought into resistance.
- **Weight: 0.6.**
- **Change mind:** a sustained move above 101 would make me add. A close below 97 (EMA200) would make me reduce sharply.

## 6b1f40e398 (ADA)
- **Read:** A rebound with a rising Gaussian slope (+1.97). Price is above EMA20 (92.3) and EMA50 (87.7).
- **Levels:** Price is still below EMA200 (108.8), and the 90-day high is about 115.6.
- **Volatility:** High, with ATR at 6.2%.
- **Weight: 0.45.**
- **Change mind:** a close above 109 would make me add. A close below 92 would make me reduce.

## 5848e95e94 (LINK)
- **Read:** A parabolic trend. The 30-day gain is 62%, ADX is 61, and the Gaussian slope is +3.4.
- **Momentum:** Price is well outside the upper Bollinger band (1.25) with RSI at 75 and bearish divergence. Price sits 17% above EMA20 (85.2).
- **Weight: 0.6.** The trend is very strong, but mean-reversion risk is high.
- **Change mind:** a close below 90, which would be a sharp loss of momentum.

## 2864cb32db (AVAX)
- **Read:** A counter-trend rally below EMA200 (110.1). Price is at the upper band with stoch RSI at 1.0 and bearish divergence.
- **Levels:** Price is approaching the 90-day high (105.2). ADX is moderate at 33.
- **Weight: 0.35.**
- **Change mind:** a close above 105.2 would make me add. A close below 92 (EMA20) would take me to flat.

**3. Weights**

{"4ba4cb22f8 (XRP)": 0.7, "ce01140c68 (DOT)": 0.3, "363b3ecbea (DOGE)": 0.5, "cd6a808bc4 (BTC)": 0.85, "fa0b8c2625 (ETH)": 0.85, "1ec41d8ea7 (SOL)": 0.75, "92c82f6efc (LTC)": 0.6, "6b1f40e398 (ADA)": 0.45, "5848e95e94 (LINK)": 0.6, "2864cb32db (AVAX)": 0.35}

## Entscheidung 2026-09-13

**1. Strategy**

I set the weight mainly by the long-term trend: close versus EMA200, plus the slope of the Gaussian midline. When price is above a rising EMA200 and Gaussian line and is pulling back towards EMA20 or EMA50, I hold a high weight (0.6–0.8). When price is well below EMA200, I keep the weight small (0.15–0.3) even if the bounce off the lows is strong, and I go flat if it loses EMA50.

**2. Windows**

## 05cbd78bab (SOL)
- **Read:** A strong uptrend (ADX 47, Gaussian slope +3.45%/5d) is pulling back into EMA20 at about 100.3. Stoch RSI is at 0, so the pullback is stretched in the short term, while RSI at 53 shows momentum is intact.
- **Levels:** Support is the EMA50/EMA200 cluster at 92.3–92.6. Resistance is the 90-day high at 111.4.
- **Weight: 0.75.** This is a pullback inside a healthy trend; I hold a little back because the 7-day move was -6.8%.
- **Change my mind:** A close below 92 would mean the trend is breaking.

## 1380259be2 (ETH)
- **Read:** The strongest structure in this set. It is 12.6% above EMA200, ADX is 50.6, and the Bollinger bands are tight (6.1%). It is a shallow consolidation above EMA20 at 98.1.
- **Levels:** EMA50 is at 91.0 and EMA200 at 88.8. The 90-day high is 107.6.
- **Weight: 0.8.**
- **Change my mind:** Below 91 (EMA50).

## 922e56af0f (LTC)
- **Read:** Price has rallied 22.6% over 30 days but sits only just above EMA200 at 99.4. The MACD histogram is flat, the bands are wide (18.3%), and EMA20 is at 96.5. The longer-term trend is only now turning up.
- **Levels:** EMA50 is at 92.2. The 90-day high is 110.6.
- **Weight: 0.6.**
- **Change my mind:** Below 97, which would mean losing both EMA200 and EMA20.

## e647e0ffa5 (BTC)
- **Read:** An orderly uptrend with low volatility (ATR 2.75%). Price is testing EMA20 at about 100.2. EMA50 and EMA200 both sit near 95.1–95.2. Stoch RSI is close to 0.
- **Levels:** The 90-day high is 107.1.
- **Weight: 0.75.**
- **Change my mind:** Below 95.

## c2ce7b6cab (DOT)
- **Read:** A violent rebound (+30.6% in 30 days) from a crash. Price is still 16.8% below EMA200, which sits at about 120.2, and is only at 0.30 of its 180-day range. ATR is 7.4% and the Bollinger width is 49%, so this is a high-volatility recovery and not yet a confirmed trend.
- **Levels:** EMA20 is at 97.5 and EMA50 at 91.5. The 90-day high is 128.5.
- **Weight: 0.3.**
- **Change my mind:** Go flat below 91.5. Raise the weight on a reclaim of 120.

## f3cc254212 (XRP)
- **Read:** A pullback after a +34% month. Price is fractionally below both EMA200 (101.0) and EMA20 (101.2), and below the 30-day VWAP at 103.5. It sits mid-range at 0.50, and the Gaussian slope is still positive.
- **Levels:** EMA50 is at 95.2. The 90-day high is 126.7.
- **Weight: 0.4.**
- **Change my mind:** Raise the weight above 102 (reclaiming EMA200/EMA20). Go flat below 95.

## 1194f9fffb (AVAX)
- **Read:** A bear-market rally that is now rolling over. Price is 15.6% below EMA200, which sits at about 118.5. The 7-day move is -7.8%, and price is back under EMA20 at 102.0. It sits in the lower third of its range.
- **Levels:** EMA50 is at 98.5. The 90-day low is 77.9.
- **Weight: 0.2.**
- **Change my mind:** Go flat below 98.5. Raise the weight above 103.

## ccac44da8d (ADA)
- **Read:** The same setup as the previous window. Price is well below EMA200 at about 118.3, has dropped -8.9% over 7 days, and has lost EMA20 at 102.1. ATR is higher here at 6.3%.
- **Levels:** EMA50 is at 97.9. The 90-day high is 126.9.
- **Weight: 0.2.**
- **Change my mind:** Go flat below 97.9.

## a6aa431869 (LINK)
- **Read:** A sharp shakeout (-15.3% in a week) inside a strong uptrend. ADX is 53, the Gaussian slope is +4.1%, and price is 11.8% above EMA200 at about 89.4. It has dropped below EMA20 (102.7), so momentum is damaged, but the structure holds.
- **Levels:** EMA50 is at 94.3. The 90-day high is 122.1.
- **Weight: 0.6.**
- **Change my mind:** Below 94 (EMA50).

## 50d7d3759b (DOGE)
- **Read:** The weakest structure in this set. Price is 11.9% below EMA200, which sits at about 113.5. It is under EMA20 (102.8) and the 30-day VWAP (104.9), at 0.29 of its range, and only 21.8% above the 90-day low at 82.1.
- **Levels:** EMA50 is at 98.9.
- **Weight: 0.15.**
- **Change my mind:** Go flat below 98.9. Raise the weight above 103.

**3. Weights**

{"05cbd78bab (SOL)": 0.75, "1380259be2 (ETH)": 0.8, "922e56af0f (LTC)": 0.6, "e647e0ffa5 (BTC)": 0.75, "c2ce7b6cab (DOT)": 0.3, "f3cc254212 (XRP)": 0.4, "1194f9fffb (AVAX)": 0.2, "ccac44da8d (ADA)": 0.2, "a6aa431869 (LINK)": 0.6, "50d7d3759b (DOGE)": 0.15}

## Entscheidung 2026-09-20

## 1. Strategy

I follow the trend and size down when price is overextended. A window gets a high weight when price is above a rising EMA200 and Gaussian midline and ADX shows a trend. I cut the weight for blow-off extension (RSI above 80, price far outside the Bollinger bands), for bearish RSI divergence, and for being below the EMA200, where a rally is more likely a bounce into resistance than a new uptrend.

## 2. Windows

The levels below come from the indicators: a level = 100 / (1 + dist%).

### 2ddfbda76e (SOL)
- **Read:** Strong, mature uptrend (ADX 43, Gaussian slope +3.6%). Price is above every average: EMA20 about 92.4, EMA50 about 85.7, EMA200 about 83.3. It sits just under the 90-day high of about 102.9. RSI 64 is firm but not extreme, and there is no divergence.
- **Weight: 0.8.** The trend is intact. I don't go to full size because price is 8% above EMA20 near the top band.
- **Change my mind:** a close below about 92.4 (EMA20).

### bd5012d9ef (AVAX)
- **Read:** A parabolic blow-off: +55% in 7 days, RSI 84, Bollinger position 1.67, and 40% above EMA20 (about 71.6). The EMA50 (about 66.6) and EMA200 (about 76.3) are far below. The 30-day VWAP is about 74. The regime is bullish, but the odds of a sharp pullback over the coming week are high.
- **Weight: 0.3.** This is token participation only, because the risk/reward from here is poor.
- **Change my mind:** below about 88 I go flat. A tight consolidation that holds above about 95 would let me add.

### 60677e4c56 (ETH)
- **Read:** Strong trend (ADX 47) at a fresh high; the 90-day high is about 100.9. Levels: EMA20 about 94.0, EMA50 about 87.8, EMA200 about 84.0. Price is slightly outside the upper band, and there is a bearish RSI divergence. The MACD histogram is nearly flat, so momentum is fading.
- **Weight: 0.7.** The trend is still dominant, trimmed for the divergence.
- **Change my mind:** a close below about 94 (EMA20).

### ed10cf0049 (ADA)
- **Read:** A sharp week (+12%), but the 30-day return is flat and price is still below the EMA200 (about 104.8). The 90-day high is about 113.4. Support is at EMA20 (about 92.6) and EMA50 (about 88.9). There is a bearish divergence, and price is running into overhead resistance.
- **Weight: 0.35.** This looks like a bounce inside a weak higher-timeframe structure.
- **Change my mind:** a close above about 105 (reclaiming EMA200) raises the weight. A close below about 92.6 takes it to flat.

### 14b22cc0ec (DOGE)
- **Read:** Below the EMA200 (about 106.5) and in the lower part of the 180-day range (0.39). The MACD histogram is negative, and price is roughly at the 30-day VWAP. Support is at EMA20 (about 97.0) and EMA50 (about 94.2). The 90-day high is about 115.5 and the 90-day low about 77.5. The Gaussian slope is still positive.
- **Weight: 0.25.** There is no confirmed uptrend.
- **Change my mind:** above about 106.5 I go long. Below about 94 I go flat.

### a0466b2cce (DOT)
- **Read:** A strong recovery rally (+20.7% over 30 days, ADX 35), but price is still under the EMA200 (about 104.9). Volatility is very high: band width 41% and ATR 6.8%. Support is at EMA20 (about 90.3) and EMA50 (about 83.8). The 90-day high is about 113.1.
- **Weight: 0.4.** The momentum is real, but price is under major resistance and volatility is high.
- **Change my mind:** a close above about 105 raises the weight to about 0.7. A close below about 90 cuts it to 0.1.

### 0113196557 (LTC)
- **Read:** An uptrend (ADX 40) pressing the 90-day high (about 101.2). RSI is 70.6 at the upper band, with a bearish divergence. EMA20 (about 91.5) and EMA200 (about 91.2) overlap, which makes that zone strong support. EMA50 is about 86.7.
- **Weight: 0.65.** The trend is good, trimmed for overbought conditions and the divergence.
- **Change my mind:** a close below about 91.5.

### c8c03409d2 (BTC)
- **Read:** A clean, low-volatility uptrend: ATR 2.7%, band width 9.4%, ADX 42. Price is near the 90-day high (about 101.4) with RSI 64 and no divergence. Levels: EMA20 about 96.1, EMA50 about 91.8, EMA200 about 90.4. It is only modestly extended.
- **Weight: 0.85.** This is the best-quality trend among the windows.
- **Change my mind:** a close below about 96 (EMA20).

### 7b9e6ef252 (LINK)
- **Read:** A powerful trend: Gaussian slope +4%, ADX 44, and 23.5% above the EMA200 (about 81.0). The recent pullback has left price 8.5% under the 90-day high (about 109.3). RSI 61.7 and Bollinger position 0.57 leave room to run. EMA20 is about 93.2 and EMA50 about 86.7.
- **Weight: 0.8.**
- **Change my mind:** a close below about 93 (EMA20).

### 08b9ec12d1 (XRP)
- **Read:** Barely above the EMA200 (about 96.1), with EMA20 (about 96.5) right next to it. The 30-day return is -3%, the MACD histogram is negative, and price is 17% under the 90-day high (about 120.5). The Gaussian slope is still positive, and price is at the 30-day VWAP. Structure is neutral to mildly bullish.
- **Weight: 0.5.**
- **Change my mind:** a close below about 96 (losing the EMA20/200 cluster) cuts the weight to 0.2. A close above about 105 raises it.

## 3. Weights

{"2ddfbda76e (SOL)": 0.8, "bd5012d9ef (AVAX)": 0.3, "60677e4c56 (ETH)": 0.7, "ed10cf0049 (ADA)": 0.35, "14b22cc0ec (DOGE)": 0.25, "a0466b2cce (DOT)": 0.4, "0113196557 (LTC)": 0.65, "c8c03409d2 (BTC)": 0.85, "7b9e6ef252 (LINK)": 0.8, "08b9ec12d1 (XRP)": 0.5}

## Entscheidung 2026-09-27

1. **Strategy**

I follow the trend and size down when price is stretched. I go long when price is above the 50- and 200-day EMAs and the Gaussian midline is rising. I size down when price is far above the EMA20 (more than ~10%), RSI is above ~75, RSI shows a bearish divergence, or price is more than ~40% above the Gaussian midline. I also size down when price has only just moved back above the EMA200. Each window's exit level sits roughly at the EMA20 or EMA200, whichever is the more important support.

2. **Windows**

## bef6633a1c (ETH)
- **Read:** Mature, strong uptrend (ADX 44). The averages are stacked: EMA20 ≈ 96.6, EMA50 ≈ 89.8, EMA200 ≈ 83.9. Price is 4% under the 90-day high of ~104.4. RSI 63 is not overheated, and price is mid-band. The midline is rising steeply.
- **Weight:** 0.85. A healthy trend that is not overextended.
- **Change my mind:** a close below ~93 (losing the EMA20 and heading toward the EMA50).

## 2b2f3b6227 (DOT)
- **Read:** Up 49% in 30 days, but only 6% above the EMA200 (~94). This looks like a sharp rebound out of a prior downtrend rather than a mature trend. Price is 13.6% above the EMA20 (~88) and 42.7% above the Gaussian midline. Stoch RSI is 0.89 and there is a bearish RSI divergence. Price is just under the 90-day high of ~103.
- **Weight:** 0.40. The trend points up, but the move is stretched and showing a warning sign.
- **Change my mind:** below ~94 (the EMA200) I go to zero. A close above ~103 with the divergence cleared would raise the weight.

## cd95d86e2b (XRP)
- **Read:** Strong trend (ADX 42). EMA20 ≈ 95.5, with EMA50 ≈ 89.4 and EMA200 ≈ 90.2 forming a support zone around 89–90. RSI is 59 and price is mid-band. There is room up to the 90-day high of ~112.
- **Weight:** 0.75. Moderately extended with space overhead.
- **Change my mind:** a close below ~89 (the EMA50/EMA200 cluster).

## 83bd500767 (ADA)
- **Read:** Up 26% in 30 days. EMA20 ≈ 90.7, EMA50 ≈ 84.0, and the EMA200 sits close below at ~94. Price is 10% above the EMA20 and the Bollinger bands are wide (38.9%). The 90-day high is ~104.
- **Weight:** 0.55. The breakout looks real, but it is extended and has only just cleared the long-term average.
- **Change my mind:** below ~94 (the EMA200).

## 047b8395a5 (BTC)
- **Read:** Clean, low-volatility trend (ATR 2.7%, ADX 44). EMA20 ≈ 96.3, EMA50 ≈ 91.2, EMA200 ≈ 87.8. Price is in the upper part of its 180-day range, 3% under the 90-day high of ~103.4. RSI 65 is not stretched.
- **Weight:** 0.90. The best-quality trend in the set.
- **Change my mind:** a close below ~95.

## aa8ab8a172 (SOL)
- **Read:** Very strong trend (ADX 46) with the midline rising steeply. Price is at the top of its 180-day range (0.95). EMA20 ≈ 91.2, EMA50 ≈ 82.9, EMA200 ≈ 77.4. Stoch RSI is 0.94, RSI 68.7, and price is 9.6% above the EMA20. The 90-day high is ~102.5.
- **Weight:** 0.65. Strong momentum, but short-term stretched.
- **Change my mind:** below ~91 (the EMA20).

## 5e4c391d65 (AVAX)
- **Read:** Up 49% in 30 days and down 3.6% this week, off the ~108 high. Price is still 15.5% above the EMA20 (~86.6) and 52.6% above the Gaussian midline. The Bollinger bands are extremely wide (74%). This looks like an extended move that has started to cool.
- **Weight:** 0.45. The trend is intact but over-stretched and losing momentum.
- **Change my mind:** below ~92 I go to zero. Reclaiming ~108 would raise the weight.

## 24b8d93e0c (LINK)
- **Read:** Strong trend; price has doubled off the 90-day low (~50.5). EMA20 ≈ 89.8, EMA50 ≈ 81.9, EMA200 ≈ 73.9. Price is near the upper band (0.85), stoch RSI is 0.93, and price is 11% above the EMA20. The 90-day high is ~103.4.
- **Weight:** 0.60. Strong but extended.
- **Change my mind:** a close below ~93.

## d8e17638ed (DOGE)
- **Read:** Price is 3.9% above the EMA200 (~96.2) and mid-range (0.57). The trend is recovering: EMA20 ≈ 93.9, EMA50 ≈ 88.7. RSI 61 leaves room to run, and the 90-day high is ~109.3.
- **Weight:** 0.60. Not overextended, but the long-term trend is not yet confirmed.
- **Change my mind:** below ~96 (losing the EMA200).

## 3b6c3128b0 (LTC)
- **Read:** Parabolic: up 21% in a week and 44.5% in 30 days, with RSI 78.7. Price is 16% above the EMA20 (~86.0); EMA50 ≈ 77.4, EMA200 ≈ 76.5. The trend is strong (ADX 50) but at a blow-off risk. The 90-day high is ~105.3.
- **Weight:** 0.40. I hold a partial position for the trend and stay reduced because of the overextension.
- **Change my mind:** a close below ~92 means cut. A pullback toward ~88–90 that holds would be a better entry.

3. **Weights**

{"bef6633a1c (ETH)": 0.85, "2b2f3b6227 (DOT)": 0.4, "cd95d86e2b (XRP)": 0.75, "83bd500767 (ADA)": 0.55, "047b8395a5 (BTC)": 0.9, "aa8ab8a172 (SOL)": 0.65, "5e4c391d65 (AVAX)": 0.45, "24b8d93e0c (LINK)": 0.6, "d8e17638ed (DOGE)": 0.6, "3b6c3128b0 (LTC)": 0.4}
