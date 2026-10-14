# H-004: SK-System (Stefan Kassing) mechanisch auf BTC/ETH

- Datum: 2026-10-15 (geschrieben, bevor ein Test lief)
- Autor: Fynn (Quelle: "SK-System ausführlich v1.02", Stefan Kassing, aufgeschrieben von Enrique Marin, Jan 2020), Testdesign Claude für Aaron
- Beobachtung: Das Dokument beschreibt "Sequenzen" (Punkte 0, A, B, Ziel C) an "Wendebereichen". Es behauptet
  reproduzierbare Einstiege, "pipgenaue" Reaktionen und dass Bewegungen zwischen Wendebereichen Zufall sind.
  Belege sind ausgewählte Forex-Charts (H1 bis M15), keine Statistik. Fynn: bei erfolgreicher Umsetzung
  "mit hoher Wahrscheinlichkeit" profitabel.
- Hypothese: Eine bullische Sequenz, die in einem übergeordneten Korrekturlevel startet, erreicht ihr Ziel
  (161,8-%-Extension) öfter, als es ihr Chance-Risiko-Verhältnis zum Ausgleich verlangt; der mittlere Ertrag
  pro Trade in R (Vielfachen des Risikos) ist nach Kosten positiv.
- Mechanismus laut Dokument: große Teilnehmer füllen Orders an Hochs/Tiefs ("Liquidität"), Korrekturlevel
  sind Zonen, in denen sich Käufer und Verkäufer einig werden. Unbelegt; die Wissensbasis
  (research/wissen/trader-wissen.md) führt Fibonacci und Elliott als nicht belegt.
- Daten: Binance Spot BTCUSDT, ETHUSDT Tageskerzen (data/raw, Hash in manifest.json).
  In-Sample 2017-08-17..2022-12-31. Validierung 2023-01-01..2024-12-31 getrennt berichtet.
  Holdout 2025-01..2026-06 wird nicht geöffnet.

## Mechanische Regeln (fest vor dem Test)

Wendepunkte: Fraktal mit k Kerzen je Seite. Ein Hoch bei Kerze i ist bekannt ab Kerze i+k (Bestätigung),
nie früher. Aufeinanderfolgende gleichartige Wendepunkte werden zum extremeren zusammengefasst
(Zickzack, abwechselnd Hoch/Tief).

Bullische Sequenz (Kassing-Begriffe in Klammern), geprüft bei jeder neuen Bestätigung eines Tiefs B:
- die letzten drei Wendepunkte sind Tief "0", Hoch "A", Tief "B";
- B > 0 (sonst ist die Sequenz ungültig, "der Markt darf nicht unter den 0-Punkt");
- Rücksetzer (A − B) / (A − 0) >= 0,382 ("erst ab dem 38,2er eine Sequenz").
- Ziel ("Sequenzziel", Zielzone): B + 1,618 · (A − 0) (Unterkante der Zone 161,8 bis 200).
- Stopp (Invalidierung): Kurs unter 0.
- Einstieg: Eröffnung der Kerze nach der Bestätigung von B, nur wenn der Schlusskurs bei Bestätigung
  noch unter A und über 0 liegt (sonst ist der Einstieg verpasst).
- Ausgang: das erste von Ziel (Hoch >= Ziel) oder Stopp (Tief <= 0). Treffen beide in derselben Kerze,
  zählt der Stopp (konservativ). Offene Trades am Periodenende werden zum Schlusskurs bewertet.
- Kosten: 0,2 % je Seite (wie COST_PER_SIDE).
- Bärische Sequenzen spiegelbildlich, nur für die Trefferstatistik (das Projekt ist long/flat).

Übergeordneter Filter ("Wendebereich", "Korrekturlevel", "Timeframepuzzeling"):
- Wochenkerzen (Sonntag-Schluss) aus denselben Tagesdaten, Wendepunkte k = 3 Wochen, gleiche Bestätigungsregel.
- Bullisches Korrekturlevel = 50 % bis 66,7 % Rücksetzer der letzten bestätigten Wochen-Aufwärtsbewegung
  (Tief → Hoch). Bärisch spiegelbildlich.
- F1 (primär): Punkt 0 der Tagessequenz liegt im zum Zeitpunkt der Bestätigung von B bekannten bullischen
  Wochen-Korrekturlevel.
- F0: kein Filter. F2 (BLASH): Schlusskurs bei Bestätigung in der unteren Hälfte der 52-Wochen-Spanne.

Primärer Test: Tageskerzen, k = 10, Filter F1, BTC und ETH gepoolt, long und short gepoolt für die
Trefferstatistik.

## Messgrößen

1. Mittleres R pro Trade nach Kosten, 95-%-Bootstrap-Intervall (10.000 Ziehungen).
2. Trefferquote gegen die Ausgleichsquote 1 / (1 + CRV) je Trade.
3. Fibonacci-Placebo: dieselben Trades mit Zielverhältnis ρ aus {1,0; 1,2; 1,4; 1,618; 1,8; 2,0; 2,2;
   2,6; 3,0} statt 1,618. Ist 1,618 etwas Besonderes, liegt sein mittleres R über dem Median der anderen.
4. Long/flat-Portfolio aus den bullischen Trades (Gewicht 1 vom Einstieg bis Ausgang): CAGR, Sharpe,
  Max Drawdown gegen Buy and Hold und 1.000 Zufallszeitpunkte gleicher Exposure und Haltedauer
  (baselines.random_timing).

## Widerlegt, wenn (fest vor dem Test)

- Primär: mittleres R nach Kosten <= 0 oder das 95-%-Intervall enthält 0. Eins reicht.
- Portfolio: Sharpe unter dem 95. Perzentil der Zufallszeitpunkte. Dann ist kein Timing-Vorteil gezeigt.
- Fibonacci: R bei 1,618 nicht über dem Median der anderen Zielverhältnisse. Dann ist das Fibonacci-Ziel
  austauschbar.
- Filter: F1 nicht besser als F0. Dann trägt der "Wendebereich" nichts.
- Nebenvarianten (k = 5, k = 20, F0, F2, je Coin, Sequenzen direkt auf Wochenkerzen mit k = 3 ohne Filter) zählen als weitere Tests; eine einzelne mit p < 0,05 ist kein Beleg
  (Bonferroni 0,05 / Zahl der Varianten).

## Was nicht getestet werden kann

- "Price Action", "allgemeines Marktverständnis", News-Bestätigung, diskretionäre Auswahl unter
  mehreren möglichen Sequenzen, Absicherung über korrelierte Paare (Forex-spezifisch). Ein Ergebnis
  gilt nur für diese mechanische Fassung. Ein Verfechter kann immer sagen, die Diskretion fehle;
  deshalb muss die diskretionäre Version sich im Forward-Test mit vorab notierten Setups beweisen.

## Ergebnis

(erst nach dem Test)
