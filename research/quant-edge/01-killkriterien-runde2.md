# Kill-Kriterien Runde 2, vorab festgelegt (2026-10-16, vor jedem Testlauf)

Geschrieben, bevor die Runde-2-Daten angekommen sind und bevor eine Zeile Testcode lief. Abweichungen nur als datierter Nachtrag am Ende. Regeln aus Runde 1 ([00-killkriterien.md](00-killkriterien.md)) gelten unverändert.

## Gemeinsam
- Entwicklung: Beginn der Reihe bis 2024-12-31. Regel-Holdout 2025-01-01..2026-06-30: nicht geladen, nicht getestet. 2026-07-01..heute: Dev-Nachschau, nie Beweis.
- Kosten 0,2 % pro Seite und Bein. Funding Zahlung für Zahlung. Signal am Schluss t, Ausführung frühestens am nächsten Bar.
- Carry-Kapital 1,5 je Einheit Nominal (1,0 Spot + 0,5 Margin), Hedge-Pflege wie Runde 1.
- **Signifikanz:** Bonferroni α = 0,05 / N_kum. N_kum = 66 (Runde 1) + 53 (diese Runde, unten aufgezählt) = **119**, α = **0,00042**. "Bestätigt" nur unter α. "Hinweis" bei p < 0,05. Sharpe-Aussagen zusätzlich mit Deflated Sharpe Ratio (Bailey/López de Prado 2014), N = 119; "bestätigt" erst bei DSR > 0,95.
- Nachträgliche Varianten erhöhen N_kum, zählen nie als Bestätigung.
- Zu jedem Ergebnis eine Gegenhypothese (Messfehler) und ein Test dagegen. Sharpe > 3: zuerst Tail und Datenfehler suchen.

## Q1 Regimewechsel Carry (8 Tests)
- Q1-a (BTC, ETH): Bruchpunkt im Monatsmittel des Fundings 2019-09..2024-12. sup-F (Andrews, 15 % Trimmung) auf Mittelwertsprung, p per AR(1)-Bootstrap unter H0. Dazu OLS-CUSUM (deskriptiv).
- Q1-b (BTC, ETH): Marktzustands-Modell auf Tagesbasis 2019-09..2024-12, Ziel = 30-Tage-Mittel des Fundings annualisiert, Regressoren 30-Tage-Rendite, 90-Tage-Rendite, 30-Tage-Volatilität (alles bis t bekannt). Prognose 2026-07..heute. Mittleres Residuum mit Newey-West-t (Lag 30).
  - "Strukturell niedriger bestätigt": Residuum < −3 Prozentpunkte p.a. und p < α.
  - "Hinweis auf Regime": Residuum < −3 pp und p < 0,05.
  - Sonst: "durch Marktlage erklärt" (zyklisch).
- Q1-c (BTC, ETH): Ablation Q1-b mit Open-Interest-Änderung 30 Tage als Zusatzregressor (Fit 2022-01..2024-12).
- Q1-d (BTC, ETH): USDe-Umlauf (30-Tage-Änderung) gegen Q1-b-Residuum, 2024-02..2024-12 plus 2026-07+. Wird als Korrelation mit Newey-West-t berichtet; bei < 12 unabhängigen Monaten nie "bestätigt".
- **Folge für K1:** Ist das niedrige Funding zyklisch, lebt K1 als "an, wenn Markt heiß"-Strategie (Runde-1-Variante war schlechter, also nur Hinweis). Ist es strukturell, gilt Break-even ≈ 8 % als dauerhaft unterschritten und K1 auf Binance-Perps ist für die nächste Runde tot.
- Deskriptiv, kein Test: Anteil der Zahlungen exakt auf dem Basiszins 0,01 %/8 h je Jahr.

## Q2 Funding-Streuung über Coins und Börsen (7 Tests)
Benchmark: 12-Coin-Carry gleichgewichtet, immer an (B1-08). Regeln wöchentlich am Sonntagsschluss, wirksam ab Folgetag, ausgeschlossenes Kapital gleich auf die übrigen verteilt, Umschichtung kostet 2 Beine × 0,2 % je Seite.
- R1: Coin raus, wenn > 1/3 der Funding-Zahlungen der letzten 30 Tage negativ.
- R2: Coin raus, wenn 7-Tage-Mittel des Fundings < 0.
- R3: Coin raus, wenn Open-Interest-Wert 7 Tage > +30 % und 7-Tage-Funding < 0 (Short-Crowding; Fenster ab 2022-01).
- R4: Coin raus, wenn |Binance-7-Tage-Funding − Bybit-7-Tage-Funding| > 10 Prozentpunkte p.a.
- R5: Nur die 4 Coins mit dem höchsten 30-Tage-Funding halten.
- X1: Börsen-Spread-Carry Binance gegen Bybit, gepoolt 12 Coins: Perp long auf der Börse mit niedrigerem 7-Tage-Funding, short auf der höheren, nur wenn Spread > 4 Kostenbeine annualisiert über 30 Tage. Ohne Bybit-Kurse ist das Basisrisiko zwischen Börsen nicht messbar; Ergebnis gilt dann als Obergrenze.
- X2: wie X1 mit Hyperliquid statt Bybit (ab Hyperliquid-Datenbeginn).
- Urteil R1..R5: "lebt" nur wenn gegen Benchmark im selben Fenster (i) Max-DD mindestens 30 % kleiner, (ii) CAGR höchstens 1 pp niedriger, (iii) Sharpe-Differenz mit Block-Bootstrap (Blocklänge 30 Tage) p < α. (i)+(ii) ohne (iii) = "Hinweis". Zusätzlich berichtet: Hätte die Regel SOL vor dem 2022-11-09 ausgeschlossen? Fehlalarme pro Jahr.
- Urteil X1/X2: "lebt" wenn Rendite auf Kapital (2 × 0,5 Margin = 1,0) > 4 % p.a. nach Kosten, < 25 % negative 30-Tage-Fenster, DD < 10 %.

## Q3 Laufzeit-Futures statt Perp (6 Tests)
- D1 (BTC, ETH, USDT-margined Quartal): immer an. Einstieg am Schluss des Tages nach einem Quartalsverfall in den aktuellen Quartalskontrakt short, Spot long; Ausstieg am Schluss des Tages vor dessen Verfall; sofort neu. Kosten: Future-Bein 0,2 % je Öffnen und Schließen, Spot einmal plus Pflege wie K1.
- D2 (BTC, ETH, Coin-margined Quartal): dito, Inverse-Kontrakt linear angenähert (S).
- D3 (BTC, ETH, USDT-margined): nur einsteigen, wenn annualisierte Basis bei Einstieg > T-Bill + 2 pp; sonst Quartal in T-Bills.
- Hürde ist die **T-Bill-Rendite derselben Zeit** (FRED DTB3), nicht 4 % fix.
- Tot, wenn Überrendite über T-Bill ≤ 0, oder Max-DD > 10 %, oder > 25 % negative 30-Tage-Fenster. Vergleich mit K1 im selben Fenster deskriptiv.

## Q4 Börsenausfall-Basisrate (2 Rechnungen)
- Ergebnis: Spanne (niedrig/zentral/hoch) für jährliche Ausfallrate einer Top-10-Börse und Verlust bei Ausfall (LGD), jede Zahl (L) oder (S).
- K1-Erwartungswert BTC, ETH: E[r] = Carry-Rendite − p × LGD × (Anteil des Kapitals auf der Börse).
  - "K1 ökonomisch tot heute": E[r] mit zentralem p, LGD und Funding seit 2026-07 < T-Bill seit 2026-07.
  - "K1 tot in jeder Funding-Lage": E[r] mit zentralem p, LGD und Funding-Mittel 2019–2024 < T-Bill-Mittel 2019–2024.

## Q5 Intraday-Zwangsfluss (30 Tests)
Daten: Binance-Perp 15-Minuten-Kerzen und 15-Minuten-Open-Interest BTC, ETH, 2022-01..2024-12.
- Ereignis Long-Kaskade: 15-min-Rendite < 0,2-%-Quantil der letzten 30 Tage (2880 Bars, ohne aktuellen Bar) UND Open-Interest-Änderung im Bar < 5-%-Quantil der letzten 30 Tage. Entclustert: nach Ereignis Sperre bis Haltedauer-Ende, mindestens 4 h.
- Handel: Perp kaufen zum Open von Bar t+1+L, halten H Bars, schließen zum Open danach.
- Hauptgitter: 2 Coins × H ∈ {1 h, 4 h, 24 h}, L = 0 (6 Tests).
- Spiegel Short-Squeeze (Rendite > 99,8-%-Quantil, OI-Drop), verkaufen: 6 Tests.
- Latenz-Ablation L ∈ {1 Bar = 15 min, 4 Bars = 1 h}: 12 Tests.
- Kontrolle nur Preis (ohne OI-Bedingung): 6 Tests.
- Statistik: Überrendite = Mittel nach Ereignis − Mittel aller Bars gleicher Haltedauer; p einseitig per Zufallszeitpunkten (10 000 Ziehungen).
- "Lebt": Überrendite nach 0,4 % Rundreise > 0, p < α, gleiches Vorzeichen 2022–23 und 2024, beide Coins.
- "Prämie existiert, für uns nicht erntbar": vor Kosten > 0 mit p < 0,05, nach Kosten ≤ 0. Zusatz-Ablation mit 0,05 % je Seite (Binance-Taker-Gebühr VIP0, L) nur deskriptiv.
- Hyperliquid-Collector-Daten (seit 2026-10-16 12:21 UTC): nur Datenstand berichten, zu kurz für einen Test.

## Zählung
Q1 8 + Q2 7 + Q3 6 + Q4 2 + Q5 30 = **53**. N_kum = 119.

## Nachträge
- **N1 (2026-10-16, vor dem Q1-Lauf, nach Blick nur auf Datumsbereiche):** Die Dev-Nachschau beginnt 2026-07-01 ohne Vorgeschichte (Holdout-Lücke). Eine 90-Tage-Rendite wäre erst ab 2026-09-29 berechenbar. Q1-b/Q1-c verwenden deshalb nur 30-Tage-Rendite und 30-Tage-Volatilität; Ziel bleibt das 30-Tage-Funding-Mittel. Prognosefenster damit ab 2026-07-31. Zusatzprüfung gegen die Gegenhypothese "Modell liegt außerhalb der Stichprobe immer daneben": gleiche Spezifikation, Fit bis 2022-12, Prognose 2023-01..2024-12 (zählt als 2 weitere Tests, N_kum = 121, α bleibt gerundet 0,00042 → exakt 0,000413).
- **N2 (2026-10-16, nach dem Q1-Lauf, nachträglich):** Newey-West-t ist bei ~80 überlappenden Tagen mit starker Persistenz überoptimistisch (Gegenhypothese). Gegentest: Leave-one-year-out-Fit in der Entwicklung, rollierende Residuen-Mittel gleicher Länge als empirische Nullverteilung, für Q1-b und Q1-c je Coin (4 Rechnungen). Kann ein Ergebnis nur entwerten, nie bestätigen.
- **N3 (nachträglich, nach dem Q5-Lauf):** Gegentest "Bid-Ask-Bounce" für die Preis-Kontrolle H = 4 h: Einstieg 1 und 4 Bars später (4 Rechnungen).
- **N4 (nachträglich, nach Blick auf Funding-Niveaus je Börse):** K1 mit Short-Bein auf Hyperliquid, BTC und ETH (2 Rechnungen). Ohne Hyperliquid-Kurse, Binance-Perp als Stellvertreter, also Obergrenze. Data Snooping: Idee entstand aus den Q2-Zahlen.
- **N5 (nachträglich, Diagnose):** Q2-Regeln und Benchmark ohne Umschichtungskosten (6 Rechnungen), um zu sehen, ob Signal oder Kosten entscheiden.
- **Zählung final Runde 2:** 53 vorab + 2 (N1) + 4 (N2) + 4 (N3) + 2 (N4) + 6 (N5) = **71**. N_kum = **137**, α = 0,05/137 = **0,000365**. Kein vorab angemeldetes Urteil ändert sich durch die strengere Schwelle.
