# E-007: Mehr Historie: 365 statt 180 Tage Tageskerzen pro Fenster; im Prompt nur die Angabe '180 days' auf '365 days' angepasst, damit sie zu den Daten passt

- Achse: daten
- Basis: E-003
- Daten: candles, 365 Tage
- Modell: claude-opus-5-5
- Thread: https://claude.ai/code/project/chan_01VH1Un8SQtbifKwzD9jDguD?thread=cmsg_01VH1Un8SQtbifKwzD9jDguDJx4EaKYCY4mXSJ3b6Y29fH

## Änderung zum Prompt der Basis
```diff
--- E-003
+++ E-007
@@ -3,7 +3,7 @@
 You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
 Horizon is weeks to months; you do not need to trade often.
 
-Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
+Each window is daily OHLCV for the last 365 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
 Judge every window on its own. Do not compare windows with each other.
 
 Before the weights, write out your analysis:
```

## Prompt
```
# T-001 baseline trader prompt

You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
Horizon is weeks to months; you do not need to trade often.

Each window is daily OHLCV for the last 365 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
Judge every window on its own. Do not compare windows with each other.

Before the weights, write out your analysis:
1. Strategy: in 2 to 3 sentences, the rule you will apply to every window.
2. Then for each window, under its id: your read of the market (trend, structure, key levels as prices on the 100 scale), your weight and why, and the price on the 100 scale that would make you change your mind.
3. End with one JSON object mapping each window id to its weight, e.g. {"a1b2c3d4e5": 0.0, "f6a7b8c9d0": 1.0}. Nothing after it.
```

## Bewertung gegen E-003

| Coins | Wochen | Entscheidungen | Timing-Wert/Woche | Basis | Differenz | t | ohne beste Woche | Wochen besser | Exposure | Rank-IC |
|---|---|---|---|---|---|---|---|---|---|---|
| A (10) | 13 | 130 | -0.191 % | -0.151 % | -0.04 % | -0.16 | -0.135 % (ohne 2026-07-05) | 8/13 | 0.367 (Basis 0.457) | 0.027 |

**Urteil: kein messbarer Unterschied**

Verbrauch: 13 Claude-Aufrufe, 1620k Zeichen, Listenpreis 9.79 USD (zählt gegen Aarons Limit, keine Rechnung)

## Was die KI gedacht hat (Beispiel: Entscheidung 2026-07-05)

Alle Wochen: [denken.md](denken.md)

````
**Strategy:** I follow the trend and only hold meaningful exposure when price is above its medium-term structure, meaning it has reclaimed the most recent breakdown level and is making higher lows. In a primary downtrend I hold at most a small starter position, and only when there is evidence of a base: a higher low, or a reclaimed breakdown level. Weight scales with how much of the broken structure has been recovered.

All ten windows have the same shape. There is a year-long decline from 2–4× current levels. A large crash near day −150 was followed by a 110–150 range, which broke down at day −33. Price has now bounced back to 100. Every window is below its 50-day and 200-day averages, so every weight starts low.

## c6b2c8e852 (LTC)
- **Read:** Primary downtrend. The 113–128 range broke at day −33. Lows were 88.4 (day −29) and 85.7 (day −10), roughly a double bottom. Price is now 100, just under the day −20 high of 101. Overhead resistance sits at 110–113, the old range floor.
- **Weight: 0.10.** The base is tentative and price remains below all the broken structure.
- **Change my mind:** a close above 113 would make me add. A break below 85.7 would take me flat.

## b039e8bff4 (XRP)
- **Read:** Same pattern. Lows were 90.7 (day −29) and 87.2 (day −10), a slightly lower low. Price is at 100 with resistance at 102.3 and the day −20 spike high of 111.8. The old floor is about 113.
- **Weight: 0.10.**
- **Change my mind:** above 112 would make me add. Below 87 would take me flat.

## 33ca11fe35 (DOGE)
- **Read:** A rally to 152 (day −52) failed. Price then fell from 129 to 99.7, bounced to 118.7, and made a lower low at 89.3 (day −5). That is a clean lower-high, lower-low sequence. The current bounce to 100 comes on fading volume (0.35–0.5). Resistance is 110–114.
- **Weight: 0.05.**
- **Change my mind:** a close above 114 would make me add. Below 89 would take me flat.

## 46b394aa0b (BTC)
- **Read:** A lower-volatility version. Lows were 92.9 (day −30) and 90.8 (day −4), a slightly lower low. Price is at 100 against resistance at 104–106 (day −20). The old range floor is about 115.
- **Weight: 0.10.**
- **Change my mind:** above 106 would make me add. Below 90.8 would take me flat.

## df2fedf2ed (ETH)
- **Read:** Lows were 84.3 (day −29) and 84.7 (day −9), a near-equal double bottom. Price is at 100 just under the day −20 high of 103.6. The old floor is about 112.
- **Weight: 0.10.**
- **Change my mind:** above 104 with follow-through would make me add. Below 84 would take me flat.

## 8d7a1d4851 (LINK)
- **Read:** Lows were 86.8 (day −29) and 86.9 (day −10), a double bottom. Price is at 100 against resistance at 106.7 (day −20) and the 111–114 old floor. Volume on the bounce is thin (0.26).
- **Weight: 0.10.**
- **Change my mind:** above 107 would make me add. Below 86.8 would take me flat.

## 1b3b921066 (SOL)
- **Read:** The prior range was lower here, at 100–110. The breakdown went to 73.7 (day −29). The retest held at 78.5 (day −10), a clear higher low. Price is now 100, back inside the old 99–107 range, so the breakdown has been reclaimed. This is the most constructive structure of the set.
- **Weight: 0.25.**
- **Change my mind:** a hold above 103–107 would make me add. Below 90 means the reclaim failed, and below 78.5 I go flat.

## 3d4bbff6f1 (AVAX)
- **Read:** Price broke from the 125–145 range to 89.9 (day −29), then made a lower low at 82.0 (day −16) on high volume. It has recovered to 100 with resistance at 102 and then 116–129. The bottom is unconfirmed.
- **Weight: 0.10.**
- **Change my mind:** above 103 would make me add. Below 85 would take me flat.

## 04184de6b0 (DOT)
- **Read:** The 135–155 range broke down. The low of 100.3 (day −29) was followed by a lower low at 90.2 (day −7). Price is back at 100, which is only a retest of the prior low as resistance, with heavier supply at 113–118. The trend structure is still lower lows.
- **Weight: 0.05.**
- **Change my mind:** above 115 would make me add. Below 90 would take me flat.

## 520bf26d11 (ADA)
- **Read:** The deepest breakdown of the set, from the 125–140 range to 78.4, then a lower low at 72.9 (day −10). This was followed by a violent V-reversal from 76 to 105.5 in four days on 2× volume, which could be capitulation followed by short covering. Price is still well under the 112–124 breakdown zone. The move is extended short-term and gap-fill pullbacks toward 85–90 are common.
- **Weight: 0.15.** Momentum is real, but the primary trend is still down.
- **Change my mind:** a close above 112 would make me add. Below 85 would take me flat.

{"c6b2c8e852 (LTC)": 0.1, "b039e8bff4 (XRP)": 0.1, "33ca11fe35 (DOGE)": 0.05, "46b394aa0b (BTC)": 0.1, "df2fedf2ed (ETH)": 0.1, "8d7a1d4851 (LINK)": 0.1, "1b3b921066 (SOL)": 0.25, "3d4bbff6f1 (AVAX)": 0.1, "04184de6b0 (DOT)": 0.05, "520bf26d11 (ADA)": 0.15}
````

## Notizen
Backlog #5, Gegenprobe zu E-006 (60 Tage). Hypothese: Die KI ankert das Gewicht an der Position in der sichtbaren Spanne (E-003: Korrelation 0,79 zur 180-Tage-Spanne). Mit 365 Tagen sieht sie den laengeren Zyklus; die Spanne wird breiter und traeger, das koennte Umschichtung senken. Erwartung: Timing-Wert hoeher als E-003. Falsifiziert, wenn die Differenz zu E-003 auf A nicht t >= 2 erreicht. Datenpruefung vorab: alle 30 Coins haben fuer alle 13 Entscheidungstage 365 lueckenlose Tageskerzen (Kerzen ab 2024-01-16). Nebeneffekt: Volumen ist relativ zum Fensterschnitt, also jetzt zum 365-Tage-Schnitt; Prompt etwa doppelt so lang, Kosten etwa doppelt.
