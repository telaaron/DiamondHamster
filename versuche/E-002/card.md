# E-002: Ruhe als Standard: mittleres Gewicht (~0,5) halten, nur bei klarer Evidenz abweichen; jede Umschichtung kostet

- Achse: prompt
- Basis: E-000
- Daten: candles, 180 Tage
- Modell: claude-opus-5-5
- Thread: https://claude.ai/code/project/chan_01VH1Un8SQtbifKwzD9jDguD?thread=cmsg_01VH1Un8SQtbifKwzD9jDguDD3MYEvodR83Vg998zcfS9X

## Änderung zum Prompt der Basis
```diff
--- E-000
+++ E-002
@@ -2,6 +2,7 @@
 
 You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
 Horizon is weeks to months; you do not need to trade often.
+Calm is the default: hold a steady middle weight (around 0.5) and move away from it only on clear evidence. Every change in weight costs money, and small moves on weak signals lose more than they gain.
 
 Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
 Judge every window on its own. Do not compare windows with each other.
```

## Prompt
```
# T-001 baseline trader prompt

You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
Horizon is weeks to months; you do not need to trade often.
Calm is the default: hold a steady middle weight (around 0.5) and move away from it only on clear evidence. Every change in weight costs money, and small moves on weak signals lose more than they gain.

Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
Judge every window on its own. Do not compare windows with each other.

Answer with one JSON object only, mapping each window id to its weight, e.g. {"a1b2c3d4e5": 0.0, "f6a7b8c9d0": 1.0}.
```

## Bewertung gegen E-000

| Coins | Wochen | Entscheidungen | Timing-Wert/Woche | Basis | Differenz | t | ohne beste Woche | Wochen besser | Exposure | Rank-IC |
|---|---|---|---|---|---|---|---|---|---|---|
| A (10) | 13 | 130 | -0.181 % | -0.235 % | 0.055 % | 0.34 | -0.039 % (ohne 2026-08-16) | 8/13 | 0.503 (Basis 0.453) | 0.06 |

**Urteil: kein messbarer Unterschied**

Verbrauch: 13 Claude-Aufrufe, 783k Zeichen, Listenpreis 4.69 USD (zählt gegen Aarons Limit, keine Rechnung)

## Notizen
Hypothese: T-001 verliert durch Umschichten (Timing-Wert -0,24 %/Woche auf A). Ein ruhiger Standard senkt die Streuung der Gewichte und hebt den Timing-Wert Richtung 0 oder darüber. Umsetzung: Der Decider sieht sein Gewicht der Vorwoche nicht (jede Woche frisch). 'Nur bei klarer Evidenz ändern' braucht deshalb einen festen Anker; gewählt: 0,5. Falsifiziert, wenn die Differenz zu E-000 auf A nicht t >= 2 erreicht. Befund: Die Anweisung wirkt aufs Verhalten (Streuung der Gewichte 0,17 -> 0,08, Spanne 0,3 bis 0,7 statt 0,1 bis 0,85), aber die verbleibenden Abweichungen verlieren weiter (Timing-Wert -0,18 %/Woche). Der Vorsprung hängt an der Woche ab 2026-08-16. Ruhiger heißt also nur: weniger Verlust pro Woche, kein Timing-Können.
