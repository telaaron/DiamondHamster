# E-000: Referenz: T-001 (180 Tageskerzen, anonymisiert)

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

Answer with one JSON object only, mapping each window id to its weight, e.g. {"a1b2c3d4e5": 0.0, "f6a7b8c9d0": 1.0}.
```

## Bewertung gegen E-000

| Coins | Wochen | Entscheidungen | Timing-Wert/Woche | Basis | Differenz | t | ohne beste Woche | Wochen besser | Exposure | Rank-IC |
|---|---|---|---|---|---|---|---|---|---|---|
| A (10) | 13 | 130 | -0.235 % | -0.235 % | 0.0 % | None | 0.0 % (ohne 2026-07-05) | 0/13 | 0.453 (Basis 0.453) | -0.022 |
| B+C (20) | 13 | 260 | -0.304 % | -0.304 % | 0.0 % | None | 0.0 % (ohne 2026-07-05) | 0/13 | 0.373 (Basis 0.373) | -0.052 |

**Urteil: Referenz**

Verbrauch: 39 Claude-Aufrufe, 2338k Zeichen, Listenpreis 14.06 USD (zählt gegen Aarons Limit, keine Rechnung)

## Was die KI gedacht hat (Beispiel: Entscheidung 2026-07-05)

Alle Wochen: [denken.md](denken.md)

````
```json
{"ec366175cd (DOGE)": 0.2, "6199875174 (SOL)": 0.5, "32373eeb1b (AVAX)": 0.4, "251e6eb0a6 (BTC)": 0.25, "f4ad87f450 (XRP)": 0.25, "1b2036c6b8 (ETH)": 0.25, "e58dbc138e (LINK)": 0.25, "c2487af183 (LTC)": 0.3, "6f17a415c0 (DOT)": 0.2, "5f400e4073 (ADA)": 0.35}
```
````

## Notizen
Identisch mit dem Turnier-Prompt T-001 (Hash e41205856d85).
