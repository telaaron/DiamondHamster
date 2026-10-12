# E-003M: Referenz: Mittel aus drei Läufen des E-003-Prompts (E-003, E-003-w2, E-003-w3)

- Achse: prompt
- Basis: (keine)
- Daten: candles, 180 Tage
- Modell: claude-opus-5-5

## Prompt
```
# T-001 baseline trader prompt

You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
Horizon is weeks to months; you do not need to trade often.

Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
Judge every window on its own. Do not compare windows with each other.

Before the weights, write out your analysis:
1. Strategy: in 2 to 3 sentences, the rule you will apply to every window.
2. Then for each window, under its id: your read of the market (trend, structure, key levels as prices on the 100 scale), your weight and why, and the price on the 100 scale that would make you change your mind.
3. End with one JSON object mapping each window id to its weight, e.g. {"a1b2c3d4e5": 0.0, "f6a7b8c9d0": 1.0}. Nothing after it.
```

## Bewertung gegen E-003M

| Coins | Wochen | Entscheidungen | Timing-Wert/Woche | Basis | Differenz | t | ohne beste Woche | Wochen besser | Exposure | Rank-IC |
|---|---|---|---|---|---|---|---|---|---|---|
| A (10) | 13 | 130 | -0.244 % | -0.244 % | 0.0 % | None | 0.0 % (ohne 2026-07-05) | 0/13 | 0.463 (Basis 0.463) | 0.059 |

**Urteil: Referenz**

Verbrauch: 0 Claude-Aufrufe, 0k Zeichen, Listenpreis 0.0 USD (zählt gegen Aarons Limit, keine Rechnung)

## Notizen
Wächter 2026-10-12: alle Versuche seit E-004 lagen unter E-003; die zwei Wiederholungen zeigen, dass der erste E-003-Lauf Glück hatte (Timing-Wert A: -0,15 / -0,26 / -0,32 %/Woche). Ab jetzt wird gegen das Mittel der drei Läufe gemessen. Auf B+C gibt es nur den ersten Lauf.
