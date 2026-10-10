# Forschungsprotokoll: eigene Trading-Methode

Stand: 2026-10-10 · Scope: nur Research, kein Live-Trading, keine Exchange-Keys · Assets: BTC, ETH (bis Aaron anderes sagt) · Horizont: Wochen bis Monate

## 1. Was "nicht auf Sand" konkret heißt

Die meisten selbstgebauten Strategien scheitern nicht an der Idee, sondern am Prozess: man testet 200 Varianten, nimmt die beste, und die "Edge" war Zufall. Fundament = ein Prozess, der genau das verhindert.

Regeln, die ab Tag 1 gelten:

1. **Holdout wird eingefroren.** Daten ab 2025-01-01 bis heute werden nicht angeschaut, nicht geplottet, nicht getestet. Einmaliger Test am Ende einer Methode. Wer einmal reinschaut, hat ihn verbrannt.
2. **Jeder Versuch wird geloggt, auch die gescheiterten.** Die Anzahl der Versuche ist Teil des Ergebnisses (Multiple-Testing-Korrektur, z. B. Deflated Sharpe Ratio). Ohne Log ist kein Ergebnis bewertbar.
3. **Hypothese vor Test.** Erst aufschreiben: Was erwarte ich, warum (Mechanismus), was würde es widerlegen. Dann testen. Nachträgliche Story-Erfindung zählt nicht.
4. **Immer gegen Baselines.** Buy & Hold, monatlicher DCA, zufälliges Timing mit gleicher Exposure. Eine Methode muss diese *nach Kosten* schlagen, sonst ist sie keine.
5. **Kosten und Realismus von Anfang an.** Gebühren + Slippage (konservativ 0,2 % pro Seite), Signal an Tag t, Ausführung frühestens Open t+1. Kein Lookahead.
6. **Regime-Abdeckung.** Ergebnis muss in Bull (2017, 2020/21), Bear (2018, 2022) und Seitwärts (2019, 2023 H1) einzeln betrachtet werden. Funktioniert nur in einem Regime = Regime-Wette, keine Methode.
7. **Einfach vor komplex.** Wenige Parameter. Jeder Parameter mehr = mehr Möglichkeiten, Rauschen zu fitten.

## 2. Ehrliche Einschränkung (wichtig)

Bei einem Horizont von Wochen bis Monaten gibt es wenig unabhängige Datenpunkte. BTC hat seit ~2013 brauchbare Daten, ETH seit 2015/2017. Das sind grob 130 bis 160 nicht-überlappende Monate. Daraus folgt:

- Statistische Signifikanz ist schwer zu erreichen. Eine Methode mit 20 Trades in 10 Jahren ist fast nicht von Glück unterscheidbar.
- Gegenmittel: Methode auf mehreren Assets testen (BTC, ETH, ggf. weitere Majors) und Robustheit über Parameter-Nachbarschaften prüfen statt eines Optimums.
- Annahme, die wir machen: dass Muster aus 2013 bis 2024 überhaupt noch gelten. Der Markt hat sich strukturell verändert (ETFs, Institutionelle, Derivate-Volumen). Das ist ein Bias-Risiko, das wir nur durch Forward-Testing auflösen.

"Neue Methode" heißt realistisch: eine eigene, verstandene Kombination aus Beobachtungen mit klarem Mechanismus, die den Prozess oben überlebt. Nicht ein Indikator, den noch nie jemand gesehen hat.

## 3. Pipeline einer Idee

| Stufe | Was | Abbruchkriterium |
|---|---|---|
| 0 Beobachtung | Aaron oder Daten zeigen ein Muster | keins, nur notieren |
| 1 Hypothese | Karte ausfüllen (siehe 5) | kein plausibler Mechanismus |
| 2 In-Sample-Test | 2013/2017 bis 2022-12 | schlägt Baselines nach Kosten nicht |
| 3 Walk-Forward | rollierend, Parameter nur aus Vergangenheit | bricht außerhalb des Fit-Fensters ein |
| 4 Validierung | 2023-01 bis 2024-12 | Performance-Kollaps vs. In-Sample |
| 5 Holdout | 2025-01 bis heute, **einmal** | verfehlt vorab definierte Schwelle |
| 6 Paper-Forward | live mitlaufen, ohne Geld, min. 3 bis 6 Monate | weicht deutlich vom Backtest ab |
| 7 Bot | erst danach | |

Die Erfolgsschwelle für Stufe 5 wird festgelegt, *bevor* Stufe 5 läuft.

## 4. Daten-Fundament

- Tageskerzen (OHLCV) BTC, ETH. Primär Binance Spot (ab 2017-08), für längere BTC-Historie zusätzlich Bitstamp/Coinbase (ab 2014/2015).
- Später, nur wenn eine Hypothese es braucht: Funding Rates, Open Interest, On-Chain (z. B. aktive Adressen, Exchange-Flows), Makro (DXY, Zinsen).
- Daten werden einmal gezogen, mit Hash versioniert, nie still überschrieben. Datenqualität prüfen: Lücken, Duplikate, Ausreißer, Börsen-Abweichungen.

**Blocker aktuell:** Der Cloud-Container erreicht keine Börsen-APIs (Binance, Coinbase, Kraken, CoinGecko geben Netzwerk-Policy-Ablehnung). GitHub und PyPI gehen.

## 5. Hypothesen-Karte (Vorlage)

```
ID: H-001
Datum:
Beobachtung: was habe ich gesehen?
Hypothese: wenn X, dann über Y Wochen Z (Richtung + Größenordnung)
Mechanismus: warum sollte das so sein? wer ist auf der anderen Seite?
Test: Daten, Zeitraum (nur In-Sample), Metrik
Widerlegt wenn: konkrete Schwelle
Parameter: Liste, mit vorab festgelegten Bereichen
Ergebnis: (erst nach Test)
Anzahl Varianten getestet:
Entscheidung: verwerfen / weiter zu Stufe N
```

## 6. Experiment-Log

Jede Ausführung eine Zeile, append-only: Datum, Hypothesen-ID, Code-Commit, Parameter, Zeitraum, Metriken (CAGR, Max Drawdown, Sharpe, Anzahl Trades, Exposure), Baseline-Vergleich, Notiz.

## 7. Erster konkreter Schritt

**Datenfundament + Baselines.** Bevor irgendeine eigene Idee getestet wird:

1. Saubere Tagesdaten BTC/ETH ziehen und versionieren, Qualitätsreport.
2. Holdout-Grenze im Code erzwingen (Loader gibt Daten ab 2025-01-01 nur mit explizitem Flag heraus).
3. Baselines berechnen: Buy & Hold, DCA, Random-Timing (1000 Läufe) inkl. Drawdowns pro Regime. Das ist die Latte, die jede Methode überspringen muss.

Parallel (Aarons Teil): 3 bis 5 eigene Beobachtungen als Hypothesen-Karten aufschreiben. Die Methode soll aus deinen Ideen kommen, nicht aus meinen.

Tech: Python, pandas, kein Backtest-Framework am Anfang (eigener, kleiner, vollständig verstandener Kern; Frameworks verstecken Lookahead- und Kostenannahmen).
