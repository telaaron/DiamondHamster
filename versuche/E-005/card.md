# E-005: Renditen statt Preise: Tageszeilen als %-Änderung (Schluss zu Schluss) und Spanne (Hoch minus Tief in % des Vortagesschlusses) statt o/h/l/c; Kipp-Niveau in % vom letzten Schluss statt auf der 100-Skala

- Achse: format
- Basis: E-003
- Daten: custom, 180 Tage
- Modell: claude-opus-5-5
- Thread: https://claude.ai/code/project/chan_01VH1Un8SQtbifKwzD9jDguD?thread=cmsg_01VH1Un8SQtbifKwzD9jDguDLv8xzUuvaWVQcdnptRZr6x

## Änderung zum Prompt der Basis
```diff
--- E-003
+++ E-005
@@ -1,12 +1,12 @@
-# T-001 baseline trader prompt
+# E-005: returns instead of prices
 
 You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
 Horizon is weeks to months; you do not need to trade often.
 
-Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
+Each window is the last 180 days, one line per day: `day ret range v`. Day 0 is the decision day, -1 the day before; ret is the close-to-close change in % against the previous day; range is high minus low in % of the previous close; volume is relative to the window average. There are no price levels.
 Judge every window on its own. Do not compare windows with each other.
 
 Before the weights, write out your analysis:
 1. Strategy: in 2 to 3 sentences, the rule you will apply to every window.
-2. Then for each window, under its id: your read of the market (trend, structure, key levels as prices on the 100 scale), your weight and why, and the price on the 100 scale that would make you change your mind.
+2. Then for each window, under its id: your read of the market (trend, structure, key levels as % from the last close), your weight and why, and the move from the last close, in %, that would make you change your mind.
 3. End with one JSON object mapping each window id to its weight, e.g. {"a1b2c3d4e5": 0.0, "f6a7b8c9d0": 1.0}. Nothing after it.
```

## Prompt
```
# E-005: returns instead of prices

You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
Horizon is weeks to months; you do not need to trade often.

Each window is the last 180 days, one line per day: `day ret range v`. Day 0 is the decision day, -1 the day before; ret is the close-to-close change in % against the previous day; range is high minus low in % of the previous close; volume is relative to the window average. There are no price levels.
Judge every window on its own. Do not compare windows with each other.

Before the weights, write out your analysis:
1. Strategy: in 2 to 3 sentences, the rule you will apply to every window.
2. Then for each window, under its id: your read of the market (trend, structure, key levels as % from the last close), your weight and why, and the move from the last close, in %, that would make you change your mind.
3. End with one JSON object mapping each window id to its weight, e.g. {"a1b2c3d4e5": 0.0, "f6a7b8c9d0": 1.0}. Nothing after it.
```

## Datenaufbereitung (render.py)
```python
"""E-005: daily rows as returns and range instead of prices.

Same days and volume as the candle window, but no price level: per day the close-to-close change and the
high-low range, both in % of the previous close. One extra candle (day -lookback) is read only to get the
first day's previous close.
"""

import pandas as pd


def render(df: pd.DataFrame, lookback: int) -> str:
    w = df.tail(lookback + 1)
    prev = w["close"].shift(1)
    ret = 100 * (w["close"] / prev - 1)
    rng = 100 * (w["high"] - w["low"]) / prev
    vol = w["volume"] / w["volume"].iloc[1:].mean()
    rows = pd.DataFrame({"ret": ret, "range": rng, "v": vol}).iloc[1:]
    rows.index = pd.RangeIndex(-len(rows) + 1, 1)
    lines = [f"{d} {r.ret:+.1f} {r.range:.1f} {r.v:.2f}" for d, r in rows.iterrows()]
    return "day ret range v\n" + "\n".join(lines)
```

## Bewertung gegen E-003

| Coins | Wochen | Entscheidungen | Timing-Wert/Woche | Basis | Differenz | t | ohne beste Woche | Wochen besser | Exposure | Rank-IC |
|---|---|---|---|---|---|---|---|---|---|---|
| A (10) | 13 | 130 | -0.501 % | -0.151 % | -0.351 % | -1.3 | -0.454 % (ohne 2026-09-20) | 4/13 | 0.445 (Basis 0.457) | 0.017 |

**Urteil: kein messbarer Unterschied**

Verbrauch: 13 Claude-Aufrufe, 477k Zeichen, Listenpreis 5.48 USD (zählt gegen Aarons Limit, keine Rechnung)

## Was die KI gedacht hat (Beispiel: Entscheidung 2026-07-05)

Alle Wochen: [denken.md](denken.md)

````
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
````

## Notizen
Backlog #3. Hypothese: E-003 ordnet das Gewicht stark der Position in der 180-Tage-Spanne zu (Korrelation 0,79); ohne Preisniveau sieht die KI die Lage in der Spanne nicht direkt und muss aus Renditen und Spannweiten lesen (Momentum, Volatilitaet). Weniger Zahlen pro Zeile (3 statt 5). Erwartung: geringere Korrelation Gewicht zu Spannen-Position, Timing-Wert hoeher als E-003. Falsifiziert, wenn die Differenz zu E-003 auf A nicht t >= 2 erreicht. Bewusster Informationsverlust gegenueber o/h/l/c: Eroeffnung (bei Krypto ca. Vortagesschluss) und Lage des Schlusses in der Tagesspanne. Notwendige Folgeaenderung im Prompt: §4a-Vorlage nennt Niveaus 'auf der 100-Skala', die es hier nicht gibt; ersetzt durch '% vom letzten Schluss', sonst Wortlaut unveraendert.
