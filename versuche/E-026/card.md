# E-026: E-003M plus eine zweite Tabelle je Fenster: die Tagesschlusskurse des Gesamtmarkts (BTC, anonym) ueber dieselben 180 Tage, gleicher Stichtag wie das Coin-Fenster, auf 100 normiert; prompt.md erklaert die Tabelle in einem Satz ohne Handelsregel

- Achse: daten
- Basis: E-003M
- Daten: custom, 180 Tage
- Modell: claude-opus-5-5
- Werkzeug: f2794e9 versuche.py@764f343a01
- Thread: https://claude.ai/code/project/chan_01VH1Un8SQtbifKwzD9jDguD?thread=cmsg_01VH1Un8SQtbifKwzD9jDguDCYHL1TSFUYiXgnmMXqAkoN

## Änderung zum Prompt der Basis
```diff
--- E-003M
+++ E-026
@@ -4,6 +4,7 @@
 Horizon is weeks to months; you do not need to trade often.
 
 Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
+Below each window follows a second table `market: day c` with the daily close of the overall crypto market (its largest coin) over the same days, scaled the same way so its last close is 100.
 Judge every window on its own. Do not compare windows with each other.
 
 Before the weights, write out your analysis:
```

## Prompt
```
# T-001 baseline trader prompt

You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
Horizon is weeks to months; you do not need to trade often.

Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
Below each window follows a second table `market: day c` with the daily close of the overall crypto market (its largest coin) over the same days, scaled the same way so its last close is 100.
Judge every window on its own. Do not compare windows with each other.

Before the weights, write out your analysis:
1. Strategy: in 2 to 3 sentences, the rule you will apply to every window.
2. Then for each window, under its id: your read of the market (trend, structure, key levels as prices on the 100 scale), your weight and why, and the price on the 100 scale that would make you change your mind.
3. End with one JSON object mapping each window id to its weight, e.g. {"a1b2c3d4e5": 0.0, "f6a7b8c9d0": 1.0}. Nothing after it.
```

## Datenaufbereitung (render.py)
```python
"""E-026: the champion's 180-day daily table plus a second table with the overall market (backlog #7).

The market is BTC (tournament/candles/BTC.csv, frozen TradingView Binance spot candles, the same file the
bench scores with; no new fetch). It is shown anonymously as daily closes over exactly the same days as the
coin window, cut off at the same decision day, scaled so its last close is 100. Never a ticker, date or level.
For BTC's own window the second table is identical to the first table's closes, which can reveal that window.
If any day of the window has no market close: "market not available".
"""

import pandas as pd

from diamondhamster import ai, tournament

BTC = tournament.read_candles("BTC", tournament.CANDLES)["close"]


def market(days: pd.DatetimeIndex) -> str:
    c = BTC.reindex(days)
    if c.isna().any() or len(c) == 0:
        return "market not available"
    c = c * (100 / c.iloc[-1])
    lines = [f"{d} {v:.1f}" for d, v in zip(range(-len(c) + 1, 1), c)]
    return "market: day c\n" + "\n".join(lines)


def render(df: pd.DataFrame, lookback: int) -> str:
    w = df.loc[: df.index[-1]].tail(lookback)
    return ai.compact(ai.window(df, df.index[-1], lookback)) + "\n" + market(w.index)
```

## Bewertung gegen E-003M

| Coins | Wochen | Entscheidungen | Timing-Wert/Woche | Basis | Differenz | t | ohne beste Woche | Wochen besser | Exposure | Rank-IC |
|---|---|---|---|---|---|---|---|---|---|---|
| A (10) | 13 | 130 | -0.373 % | -0.244 % | -0.129 % | -1.12 | -0.171 % (ohne 2026-07-26) | 4/13 | 0.413 (Basis 0.463) | 0.064 |

**Urteil: kein messbarer Unterschied**

Verbrauch: 13 Claude-Aufrufe, 1043k Zeichen, Listenpreis 6.75 USD (zählt gegen Aarons Limit, keine Rechnung)

## Was die KI gedacht hat (Beispiel: Entscheidung 2026-07-05)

Alle Wochen: [denken.md](denken.md)

````
**Strategy:** Trend-following with a market filter. I hold full size only when an asset is above its medium-term structure and making higher highs and higher lows while the market is not in a downtrend. In a falling market I go flat to small, and I add exposure only for clear relative strength, such as reclaiming the pre-crash level or breaking a base on volume.

**Market context (identical in every window):** The market is in a downtrend, from about 143 to a low of 92 at day −5. It has bounced to 100 but is still below its ~50-day area (about 110) and below the breakdown level near 115. It is a short-term bounce inside a downtrend, so base weights stay low.

### c2e3254f16 (AVAX)
- **Read:** Long downtrend, from 210 to a low of 82 at day −16. Higher lows since then (82, 86, 92) and price is now 100, back at the top of its one-month range. Overhead is the 110–116 gap left by the −33/−30 breakdown.
- **Weight: 0.3.** It is improving, but it is still a bounce in a downtrend.
- **Change my mind:** Below 90 I go to 0. A close above 103 lets me add.

### 4d60bda5f8 (BTC)
- **Read:** This asset tracks the market. Lows at 92.9 and 90.8 and price now 100. Resistance is 104–106, from the day −20 high, and support is 91.
- **Weight: 0.25.** There is no edge beyond the market's own bounce.
- **Change my mind:** Below 91 I go to 0. Above 106 I go to 0.5.

### 0f5cd43f21 (ADA)
- **Read:** It crashed to 73 at day −10, then rose from 76 to 101 in four days on 1.8–2.2× volume. That breaks the 73–90 base and clears the day −20 bounce high of 100. It shows strong relative strength against the market, though it is far below the 50-day level (~120).
- **Weight: 0.5.** This is a momentum breakout, kept at half size because the move was vertical and the market is weak.
- **Change my mind:** Below 88 (losing the breakout) I go to 0. Holding above 103 lets me add.

### f6ee48f1a1 (LTC)
- **Read:** Low of 85.7 at day −10, followed by a steady grind to 100. Price is testing the 101 resistance from day −20. It fell less than the other assets and is making higher lows.
- **Weight: 0.35.**
- **Change my mind:** Below 90 I go to 0. A close above 102 takes me to 0.6.

### b4def9c423 (DOGE)
- **Read:** A rally to 152 at day −52 failed completely. Since the crash the highs keep falling (118.7, 109, now 101). The low was 89.3 at day −5 and resistance is 105–110.
- **Weight: 0.2.** The structure is still lower highs.
- **Change my mind:** Below 92 I go to 0. Above 110 I go to 0.5.

### 2132450ec6 (LINK)
- **Read:** Double bottom near 87 (days −29 and −10), with price now 100. Resistance is 101.5–106.7 and the trend is still down.
- **Weight: 0.25.**
- **Change my mind:** Below 88 I go to 0. Above 107 I go to 0.5.

### 727098e9dc (SOL)
- **Read:** Low of 73.7 at day −29, then a higher low at 78.5 (day −10). Price is now 100, above the day −20 high of 93.3 and back at the pre-crash level (~100 at day −34). The highs and lows are both rising, and it has recovered the entire crash, which the market has not.
- **Weight: 0.5.**
- **Change my mind:** Below 88 I go to 0. Holding above 103 lets me raise it.

### 303acee46a (XRP)
- **Read:** Low of 87.2 at day −9, with price now 100. The day −20 spike to 111.8 failed, so resistance sits at 102–112. The highs are still falling.
- **Weight: 0.2.**
- **Change my mind:** Below 88 I go to 0. Above 108 I go to 0.5.

### ae1a0b68e0 (ETH)
- **Read:** Double bottom at 84.3/84.7, with price now 100, just under the day −20 high of 103.6. Day 0 volume picked up, but price did not move.
- **Weight: 0.3.**
- **Change my mind:** Below 88 I go to 0. A close above 104 takes me to 0.5.

### 129d4c0ebd (DOT)
- **Read:** A persistent downtrend from 250, with every rally failing (188 → 151 → 157 → 118 → 101). The low was 90.2 at day −7 and price is now 100. Resistance is 102 and then 111–118.
- **Weight: 0.2.**
- **Change my mind:** Below 91 I go to 0. Above 112 I go to 0.5.

{"c2e3254f16 (AVAX)": 0.3, "4d60bda5f8 (BTC)": 0.25, "0f5cd43f21 (ADA)": 0.5, "f6ee48f1a1 (LTC)": 0.35, "b4def9c423 (DOGE)": 0.2, "2132450ec6 (LINK)": 0.25, "727098e9dc (SOL)": 0.5, "303acee46a (XRP)": 0.2, "ae1a0b68e0 (ETH)": 0.3, "129d4c0ebd (DOT)": 0.2}
````

## Notizen
Backlog #7 (Marktkontext). Basis E-003M (B-18: sauber, nicht dev-informiert). Daten: kein neuer Abruf, also keine B-19-Pflicht; BTC-Schluesse aus tournament/candles/BTC.csv (main 022ab32, TradingView BINANCE:BTCUSDT Spot, dieselbe Datei, mit der der Pruefstand wertet), sha256 3b72f3ca7cb95165f8b747f23f4d275ce4e27bd5bf9b0216054124d9d169680f. Darstellung (Standards, wo relative-staerke.md par. 7 mehr vorsieht): nur die Schlusskurse ('market: day c', eine Zeile pro Tag, gleiche Tagesnummern wie die Coin-Tabelle), keine Ratio, RS, Beta oder Residuen, damit genau eine Sache geaendert wird und die Eingabe nur um etwa ein Drittel waechst; derselbe Stichtag (Entscheidungstag) wie das Coin-Fenster, denn die Coin-Kerze des Entscheidungstags ist auch sichtbar. Fuer das BTC-Fenster selbst steht die identische zweite Tabelle da; damit ist dieses Fenster erkennbar (Karte vermerkt das). Fehlt ein Tag: 'market not available'. Hypothese: Mit dem Marktverlauf daneben gewichtet die KI Coins nach relativer Staerke zum Markt (Altcoins haengen am Gesamtmarkt), das verbessert die Verteilung quer ueber die Coins und den Timing-Wert. Falsifikator (vor dem Lauf festgelegt): falsifiziert, wenn der Timing-Wert gegenueber E-003M nicht steigt (Differenz <= 0) oder der Rank-IC nicht ueber dem von E-003M (0,059) liegt. Zusaetzlich berichtet: Nutzung = Rangkorrelation Gewicht zu relativer 30-Tage-Staerke (Coin-Rendite minus BTC-Rendite) je Woche quer ueber die 9 Altcoins, gemittelt; Signalwert = dieselbe Rangkorrelation der relativen Staerke mit der Rendite der Folgewoche. Champion-Regeln B-12/B-13/B-14: bei t >= 2 genau eine Wiederholung auf A, Urteil auf dem Mittel; B+C nur bei t >= 2. Karte nennt Anteil Gewichtsaenderungen unter 0,15, partiellen Anker (werkzeuge/anker.py), Rank-IC und Exposure. Vorlage aus par. 4a unveraendert. versuche.py vom Branch claude/project-thread-lupsy0 (README par. 4).

## Zusatz (Thread, nach dem Lauf)
- **Falsifikator: falsifiziert.** Timing-Wert gegenüber E-003M −0,13 %/Woche (t −1,12), also nicht gestiegen. Rank-IC 0,064 statt 0,059: praktisch gleich.
- **Umschichtung** 0,146 je Coin und Woche (E-003-Läufe 0,118 / 0,120 / 0,154); Gewicht in 10 von 120 Fällen unverändert. **Anteil der Gewichtsänderungen unter 0,15:** 53 % (E-003-Läufe 58 / 56 / 43 %).
- **Anker (werkzeuge/anker.py):** partiell 0,48 (E-003M 0,40), einfache Korrelation Gewicht zu Spannenlage 0,85, zu Momentum 0,73. Die zweite Tabelle bindet die KI eher stärker an die Spanne.
- **Nutzung:** Rangkorrelation Gewicht zu relativer 30-Tage-Stärke gegen BTC quer über die 9 Altcoins im Mittel 0,63 (E-003-Läufe ohne Tabelle 0,53 / 0,58 / 0,56). Die KI belohnt relative Stärke etwas mehr, tat das aber schon ohne Tabelle, weil relative Stärke im Querschnitt fast dasselbe ist wie eigenes Momentum.
- **Signalwert:** Rangkorrelation relative 30-Tage-Stärke zu Rendite der Folgewoche −0,11 (t −1,34): auf dem Prüfstand kehrte relative Stärke eher um, statt fortzulaufen.
- **Marktdeckel:** In allen Strategien steht ein Marktfilter („market not in a downtrend“); die Exposure sank auf 0,41 (Basis 0,46).
- **BTC-Fenster erkennbar:** Für BTC sind beide Tabellen identisch; der Decider schrieb in Woche 1 selbst „This asset tracks the market“. Das betrifft 1 von 10 Fenstern und verrät weder Woche noch Jahr; der Leak-Check (Jahreszahlen, Monatsnamen, Ticker in allen 130 Fenstern) fand nichts.
- Keine Wiederholung, kein B+C (t < 2). Champion bleibt E-003M.
