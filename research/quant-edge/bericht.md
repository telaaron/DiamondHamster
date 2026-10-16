# Quant-Edge: Woher Rendite kommt, wenn alle alles wissen

Stand 2026-10-16. Auftrag: Aarons Quant-Forscher-Prompt (Phasen 0 bis 5, Schluss a bis d). Gedankenexperiment für Märkte allgemein, Landung auf dem, was DiamondHamster wirklich betreiben kann.

**Kennzeichnung jeder Zahl:** (G) = gerechnet in dieser Arbeit, Code und Rohdaten unten verlinkt. (S) = geschätzt, mit Herleitung. (L) = Literatur, mit Quelle.

**Daten:** Binance Spot- und Perp-Tageskerzen plus jede einzelne Funding-Zahlung für 12 Coins (BTC, ETH, SOL, XRP, BNB, DOGE, ADA, LTC, LINK, AVAX, TRX, DOT), geladen auf Aarons Mac, weil die Cloud keine Börse erreicht. Der Regel-Holdout 2025-01-01 bis 2026-06-30 wurde **nicht heruntergeladen** (API-Zeitfenster schlossen ihn aus, jede Datei geprüft: 0 Zeilen im Holdout). Dazu Coinbase-Tageskerzen BTC/ETH aus dem Repo, Holdout beim Laden entfernt. Rohdaten mit sha256: `research/quant-edge/daten/`.

**Kill-Kriterien** wurden vor dem ersten Testlauf festgeschrieben: [00-killkriterien.md](/mnt/project-files/research/quant-edge/00-killkriterien.md).

---

## Die Antwort vorweg

Von vier Kandidaten überlebt genau einer: **Funding-Carry** (Coin kaufen, gleiche Menge als Perp leerverkaufen, die Gebühr kassieren, die gehebelte Käufer zahlen). BTC +8,4 % pro Jahr auf das eingesetzte Kapital, ETH +10,2 % (G, 2019 bis 2024, nach Kosten). Er braucht **keine Kursprognose**. Er scheitert nicht am Signal, sondern an drei Dingen außerhalb jedes Signals: Börsenausfall, schrumpfende Prämie (seit 2026-07 nur noch 5,9 % bzw. 4,5 % brutto pro Jahr, G) und Hedge-Brüche.

Alle drei Richtungs-Ideen auf Wochen bis Monate sind tot: Kaufen nach Zwangsverkäufen, Exposure-Senken bei Überhitzung, Trendfilter mit Volatilitätssteuerung. Das deckt sich mit den 37 KI-Versuchen: Auf diesem Horizont steckt in Signalen nichts Messbares. **Der Edge liegt in Bilanz, Kosten und Risikosteuerung, nicht in der Signalidee.**

---

## Begriffe (einmal, dann benutzt)

- **Perp (Perpetual Future):** Wette auf den Kurs ohne Ablaufdatum, mit Hebel. Software-Analogie: ein Termin-Kontrakt, der sich alle 8 Stunden selbst neu abrechnet.
- **Funding:** Die Zahlung, die den Perp-Kurs an den Spot-Kurs bindet. Sind mehr Leute gehebelt long, zahlen Longs alle 8 Stunden an Shorts. Ein Mietzins für Hebel.
- **Carry / Cash-and-Carry:** Coin halten und Perp leerverkaufen. Kursbewegung hebt sich auf, übrig bleibt das Funding. Du bist der Vermieter des Hebels.
- **Basis:** Abstand Perp-Kurs zu Spot-Kurs. Normal winzig. Springt sie, verliert der Hedge.
- **Liquidation:** Die Börse schließt eine gehebelte Position zwangsweise, wenn die Sicherheit (Margin) aufgebraucht ist. Ein Algorithmus, der zu jedem Preis verkauft.
- **Margin:** Sicherheitsleistung für die Hebelposition.
- **Sharpe:** Rendite pro Einheit Schwankung, auf ein Jahr hochgerechnet. Über 1 ist gut, über 3 bei echten Strategien verdächtig (meist versteckte Tail-Risiken).
- **Max Drawdown:** größter Verlust vom letzten Höchststand. **Calmar:** Jahresrendite geteilt durch Max Drawdown.
- **Tail-Ratio:** Größe der besten 5 % Wochen geteilt durch Größe der schlechtesten 5 %. Über 1 heißt: Ausreißer nach oben größer als nach unten.
- **Walk-Forward:** Parameter nur aus der Vergangenheit wählen, auf die Zukunft anwenden, Fenster weiterschieben. Wie ein Deployment, das nur die Logs von gestern kennt.
- **Timing-Wert:** Rendite der Strategie minus Rendite einer festen Position mit derselben mittleren Gewichtung. Misst, ob das *Wann* etwas bringt oder nur das *Wie viel*.

---

## Phase 0: Metaphysik des Edges

### Was bleibt, wenn alle alles sofort wissen?

Unter perfekter, symmetrischer Information ist jeder Preis die beste Schätzung des Wertes, gegeben das Risiko und die Zwänge aller Beteiligten. Informationsrendite ist null (Grossman-Stiglitz 1980 zeigen sogar: dann lohnt niemandem das Informieren, ein Gleichgewicht mit perfekter Information ist instabil, L). Was übrig bleibt, ist **keine Belohnung fürs Wissen, sondern eine Bezahlung fürs Tragen**: Risiko, Zeit, Bilanz, Lagerbestand, Unannehmlichkeit.

Ich leite aus einer Frage ab: *Was kostet etwas, auch wenn jeder den Preis kennt?*

| # | Quelle | Wer zahlt | Warum sie unter perfekter Information NICHT verschwindet |
|---|---|---|---|
| R1 | **Risikoprämie** (Halten von etwas, das in schlechten Zeiten fällt) | Alle Risikoscheuen, über einen niedrigeren Einstiegspreis | Information beseitigt Unwissen über die Verteilung, nicht das Risiko selbst. Wer Crash-Risiko nicht tragen will, zahlt dafür, es loszuwerden. Präferenz, kein Wissensdefizit. |
| R2 | **Sofortigkeitsprämie** (Spread, Market Making) | Wer *jetzt* handeln will | Inventarrisiko und Kapitalbindung des Market Makers bleiben. Unter perfekter Information fällt nur der Teil weg, der vor Informierten schützt (adverse Selektion), der Lagerhaltungsteil bleibt (Stoll 1978, L). |
| R3 | **Versicherungsprämie** (Optionen, Crash-Schutz verkaufen) | Hedger mit Mandat, Verlustlimit, Verbindlichkeiten | Der Bedarf entsteht aus Regeln (Value-at-Risk, Solvenz), nicht aus Unwissen. Implizite Volatilität liegt im Mittel über realisierter (Volatilitäts-Risikoprämie, Carr/Wu 2009, L). |
| R4 | **Hebel-/Finanzierungsprämie** (Carry, Funding, Basis) | Wer Hebel will, aber keinen billigen Kredit bekommt | Die Einschränkung ist die Bilanz, nicht das Wissen. Frazzini/Pedersen 2014 (L): Hebelbeschränkte Investoren überzahlen für eingebauten Hebel. Krypto-Perps sind genau das. |
| R5 | **Zwangsfluss-Prämie** (Margin Calls, Liquidationen, Rücknahmen, Indexregeln) | Wer zu jedem Preis handeln *muss* | Jeder kennt den Fluss, aber das Kapital zum Auffangen ist im Moment des Stresses knapp, weil alle Auffänger selbst unter Stress stehen. "Limits to Arbitrage" (Shleifer/Vishny 1997, L), Fire Sales bei Fonds (Coval/Stafford 2007, L). |
| R6 | **Nicht-Rendite-Motive** (Lotterie-Vorliebe, Steuer, Regulierung, Ideologie) | Wer etwas anderes als Rendite optimiert | Präferenzen sind kein Informationsproblem. Der Lotteriekäufer weiß, dass sein Los im Mittel verliert. |
| R7 | **Struktur-Renten** (Warteschlangen-Priorität, Maker-Rebates, Tick-Größe, Listing-Zugang) | Alle, die über die Struktur handeln | Wird durch Regeln vergeben, nicht durch Wissen. Fließt aber fast ganz an den Eigentümer der Struktur (die Börse). Für uns unerreichbar. |

**Nicht in der Liste, bewusst:** Informations-Edge (per Axiom null) und Latenz-Edge (wenn alle 0 ms haben, null; bleibt nur Losglück bei Gleichstand).

**Synthese:** Rendite unter perfekter Information ist **Miete für Bilanz und Nerven**. Wer etwas trägt, das ein anderer nicht tragen kann oder will, wird bezahlt. Das ist der ganze Rest.

### "Jeder Edge ist die Zwangsjacke von jemand anderem", Segment für Segment

| Segment | Stimmt? | Begründung |
|---|---|---|
| Perp-Funding / Basis | **ja** | Gegenseite ist hebelbeschränkt (kein Zugang zu USD-Kredit, will Hebel ohne Bankkonto). |
| Liquidationen | **ja, am stärksten** | Die Zwangsjacke ist wörtlich ein Algorithmus. Preis ist ihm egal. |
| Optionen / Volatilitätsprämie | überwiegend | Hedge-Mandate ja; Privatkäufer von Calls sind aber freiwillig (R6, Lotterie). |
| Market Making | teils | Ungeduld ist oft Vorliebe, nicht Zwang. |
| Index-/ETF-Rebalancing | ja, aber dünn | Regeln sind öffentlich, wird vorweggenommen, Restprämie klein. |
| BTC halten / Aktien halten | **nein, bricht** | Gegenseite ist der *künftige Käufer*, nicht ein Gezwungener. Rendite ist Risikoprämie (R1) bzw. bei Aktien Wachstum der Cashflows. Bei BTC ohne Cashflows: Rendite = neue Nachfrage. Freiwillig. |
| Insider / Information | **nein, bricht** | Gegenseite ist uninformiert, nicht gezwungen. Unter dem Axiom weg. |
| Überteuerte Lotterie-Altcoins | **bricht interessant** | Käufer zahlen freiwillig. Die Zwangsjacke sitzt bei *dir*: Leerverkauf ist teuer oder unmöglich (Leihe, Funding negativ). Der Edge existiert, weil der Arbitrageur gefesselt ist. |

**Urteil:** Der Satz stimmt für alle Prämien aus R2 bis R5. Er bricht bei R1 und R6: Dort zahlt jemand freiwillig, aus Präferenz. Genauer wäre: *Jeder Edge ist entweder die Zwangsjacke oder die Vorliebe von jemand anderem, und er überlebt nur, solange die Zwangsjacke des Arbitrageurs ihn schützt.*

### Was zerstört sich selbst, wenn es groß wird?

Alles aus R2 bis R5. Mechanismus jedes Mal derselbe: Du wirst selbst Teil des Angebots, das die Prämie drückt.
- **Carry (R4):** Jeder zusätzliche Short senkt das Funding. Sichtbar in unseren Daten: Funding BTC annualisiert 30,6 % (2021), 11,9 % (2024), 5,9 % (seit 2026-07) (G). Plausibler Treiber: industrielle Carry-Produkte wie Ethena (USDe) seit 2024 (S, Kausalität nicht geprüft).
- **Zwangsfluss (R5):** Wer kauft, wenn andere müssen, verkleinert den Preisdruck, also seine eigene Rendite. Und er wird selbst zur Liquidität, die beim nächsten Mal jeder sein will.
- **Market Making (R2):** Eigene Inventargröße wird zum Risiko, Spread verengt sich durch Wettbewerb.
- **Risikoprämie (R1)** skaliert am besten: Halten drückt die Prämie kaum, solange man nicht den Markt dominiert.

**Wo der eigene Fußabdruck bindend wird:** sobald die eigene Order einen merklichen Anteil am Zwangsfluss oder am Tagesvolumen hat. Faustregel Marktimpact (Wurzelgesetz, Tóth et al. 2011, L): Impact ≈ σ_Tag × √(Q / Tagesvolumen). BTC-Perp 2024: σ_Tag 2,8 %, Median-Tagesvolumen 16,2 Mrd USD (G). Bei 1 % des Volumens (≈ 160 Mio USD) wären das ≈ 0,28 % Impact pro Seite (S, Formel mit Vorfaktor 1), also schon mehr als unsere 0,2 % Kostenannahme.

### Was bricht zuerst bei unendlichem Kapital?

**Die Prämie selbst.** Jeder Edge aus R2 bis R5 ist der Preis knappen Kapitals. Unendliches Kapital heißt Kapitalkosten null, du lieferst Hebel, Liquidität und Versicherung, bis die Prämie auf deine Grenzkosten (null) fällt. Du konkurrierst dann nur noch mit dir selbst. Danach brechen, in dieser Reihenfolge: (1) Gegenpartei-Kapazität (Börsen-Positionslimits, Versicherungsfonds, Auto-Deleveraging), (2) Konzentration auf wenige Börsen (ein Ausfall vernichtet einen großen Teil), (3) Regulierung. Übrig bliebe allein R1, die Risikoprämie, und auch die schrumpft, weil du zum dominanten Käufer wirst.

---

## Phase 1: Der Gegner

Wer sitzt am anderen Ende, und welche Regel zwingt ihn, unabhängig vom Preis zu handeln?

| Agent | Zwang (Regel) | Preisunabhängig? | Zeitpunkt vorhersehbar? | Zählt für "keine Gegenpartei ohne Zwang"? |
|---|---|---|---|---|
| Gehebelte Perp-Trader (privat) | Margin: unter Wartungsmarge Liquidation | **vollständig** | teils (Liquidationsniveaus schätzbar, unser Hyblock-Nachbau) | ja |
| Liquidations-Engine, Versicherungsfonds, Auto-Deleveraging | Börsenregel | vollständig | nein, ereignisgetrieben | ja |
| Perp-Longs, die Hebel wollen | kein Zugang zu billigem USD-Kredit | gegenüber Funding fast unelastisch in Euphorie | Funding ist öffentlich | ja (Präferenz plus Bilanzgrenze) |
| Carry-Fonds, Ethena | Rücknahmen, Margin auf der Short-Seite | bei Rücknahmen ja | nein | ja |
| Miner | Strom in Fiat, Hashpreis, Halving | teils | Halving ja, Kapitulation nein | ja |
| Staaten, Insolvenzmassen (Mt.Gox 2024, FTX-Masse, deutscher Staat 2024) | Gerichtsbeschluss, Zeitplan | ja | **ja, Termine öffentlich** | ja |
| Teams und VCs mit Token-Unlocks | Vesting-Plan | teils (hedgen vorab per Perp) | ja | ja |
| Dealer mit Short-Gamma (Options-Market-Maker) | Delta-neutral-Mandat: müssen in Bewegungen hinterher handeln | ja | teils (Optionspositionen schätzbar) | ja |
| ETF-Anleger, Treasury-Firmen | Mandat, Benchmark, Kapitalerhöhung nur bei Prämie zum Buchwert | teils | nein | teils |
| Market Maker selbst | Risikolimits: im Crash weiten oder ziehen sie sich zurück | ja, im Stress | nein | ja |
| Panische Privatanleger | **kein Zwang, nur Gefühl** | nein | nein | **nein**, scheidet nach Regel aus |

### These prüfen: "Ein Bot gegen jemanden, der nicht Nein sagen kann, braucht keine Prognose"

**Halb wahr. Du tauschst Prognose-Risiko gegen Bilanz-Risiko.** Drei Prognosen bleiben auch gegen einen Gezwungenen:
1. **Ist der Druck vorübergehend oder ist er Information?** Wer bei FTX im November 2022 den gezwungenen Verkäufern Solana abkaufte, kaufte gleichzeitig eine echte Verschlechterung. Zwang und schlechte Nachricht kommen oft zusammen.
2. **Ist der Zwangsfluss größer als mein Kapital?** Kaskaden füttern sich selbst. Wer zu früh auffängt, wird selbst liquidiert.
3. **Wer fängt außer mir noch auf?** Die Prämie ist, was nach dem Wettbewerb übrig bleibt.

Die These gilt rein nur dort, wo der Zwang **vertraglich, wiederkehrend und klein gegenüber dem auffangenden Kapital** ist. In unserem Suchraum ist das genau einer: Funding. Dort prognostizierst du keinen Kurs, du trägst Ausfall- und Basisrisiko. Unsere Tests bestätigen das (Phase 3).

---

## Phase 2: Der Edge, konkret

Suchraum ohne MA-Crossover, RSI, Bollinger. Eine Ausnahme mit Begründung: K4 enthält einen gleitenden Durchschnitt, **nicht als Signal, sondern als Kontrollarm**, weil er die Latte ist, die jeder Profi-Vorschlag im Projekt bisher aufgestellt hat (Dokument Profi-Trader, Kontrollarm "Trendregel plus Volatilitätssteuerung"). Er soll zeigen, ob irgendetwas Timing-artiges besser ist als feste Positionsgröße.

| | K1 Funding-Carry | K2 Zwangsverkäufer-Reversal | K3 Überhitzungsfilter | K4 Trend plus Vol-Steuerung (Kontrolle) | K5 Volatilität verkaufen | K6 Termin-Zwangsverkäufer |
|---|---|---|---|---|---|---|
| **Was** | Spot long, Perp short, Funding kassieren | Nach extrem negativem Funding (bzw. Absturz) Spot kaufen, 4 oder 8 Wochen halten | Exposure halbieren, wenn Funding extrem hoch | Long nur über gleitendem Schnitt, Größe nach Volatilität | Optionen verkaufen (Deribit) | Vor bekannten Großverkäufen (Mt.Gox, Staaten, Unlocks) nicht kaufen bzw. danach kaufen |
| **Warum existiert er** | R4 Hebelmiete | R5 Zwangsfluss | R5 gespiegelt: Überhebelte werden später zu Zwangsverkäufern | schwach: langsames Kapital, Risiko-Abbau-Flüsse | R3 Versicherung | R5 mit bekanntem Termin |
| **Wer zahlt** | gehebelte Longs | Liquidierte, die zu jedem Preis verkaufen | gehebelte Longs am Ende einer Euphorie | Rebalancer, Mittelwert-Wetter; Zwang unklar | Hedger, Lotteriekäufer | Gerichte, Staaten, VCs |
| **Warum nicht wegarbitriert** | braucht Bilanz, Börsenrisiko, Stablecoin-Risiko | im Stress fehlt Kapital zum Auffangen | wenige trauen sich gegen den Trend | Crowding unvollständig | Tail-Risiko, Margin | öffentliche Termine, teils eingepreist |
| **Kapazität** | groß, aber selbstdämpfend (eigener Short senkt Funding) | klein (Ereignisse selten, Impact im Stress hoch) | groß (nur Exposure-Steuerung) | groß | mittel | klein |
| **Halbwertszeit** | sichtbar kürzer werdend: Funding BTC 30,6 % → 11,9 % → 5,9 % (2021 → 2024 → 2026 H2, G) | auf Tages-/Stundenebene vermutlich längst von schnellen Akteuren abgeerntet (Phase 3) | n/a | Jahrzehnte in klassischen Märkten (Moskowitz/Ooi/Pedersen 2012, L) | lang (L, Carr/Wu) | einmalig je Ereignis |
| **Testbar hier?** | **ja** | **ja** | **ja** | **ja** | nein (keine Optionsdaten) | nein (zu wenige Ereignisse, keine Termindaten) |

**Auswahl:** K1 bis K4 werden gerechnet. K1 ist der stärkste Mechanismus (Zwang vertraglich, Gegenpartei eindeutig). K2 und K3 sind die Richtungsvarianten, die DiamondHamster als Analyse-Hinweis nutzen könnte (Hypothesen H-A und H-B aus dem Gewinner-Dokument). K4 ist die Latte.

---

## Phase 3: Simulation ohne Gnade

### Aufbau
- **Walk-Forward:** K4 wählt seine Länge jedes Jahr nur aus Vorjahren. K1 hat keinen Parameter. K2/K3 nutzen nur gleitende Perzentile der jeweils letzten 365 Tage. Kein K-Fold.
- **Kosten:** 0,2 % pro Seite und pro Bein (Protokoll §1.5). Carry zusätzlich Hedge-Pflege (täglich die Hälfte der Kursbewegung umschichten, beide Beine; konservativ, kostet 1,65 bzw. 2,2 Prozentpunkte des Nominals pro Jahr, G) und 1,5-faches Kapital je Einheit (1,0 Spot plus 0,5 Margin). Funding echt, Zahlung für Zahlung. **Nicht modelliert:** Steuern (für Aarons OÜ unbekannt), Kapitalkosten über die 4-%-Hürde hinaus, Teilausführungen, Queue-Position (bei Tageshorizont irrelevant gegenüber 0,2 %).
- **Look-ahead-Audit:** Jede Datei beginnt mit dem Audit der Referenzen. Kernregel: Signal am Schluss von Tag t, Handel zum Open t+1 (`backtest.run` verschiebt um einen Tag). Funding eines Tages (00/08/16 UTC) ist am Tagesschluss bekannt. Perzentile laufen über t−364 bis t. Nichts nach t.

### K1 Funding-Carry: lebt

| | BTC | ETH | Quelle |
|---|---|---|---|
| Fenster | 2019-09-10 bis 2024-12-31 | 2019-11-27 bis 2024-12-31 | G |
| Rendite auf Kapital p.a. | **+8,4 %** | **+10,2 %** | G |
| Sharpe | 6,6 | 7,1 | G (siehe Warnung) |
| Max Drawdown | −1,8 % | −1,8 % | G |
| Anteil negativer 30-Tage-Fenster | 9,9 % | 12,0 % | G |
| Schlechtestes 30-Tage-Fenster | −1,6 % | −1,3 % | G |
| Tage mit negativem Funding | 11,8 % | 9,3 % | G |
| Längste Strecke negatives Funding | 9 Tage | 13 Tage | G |
| Rendite je Jahr 2019/20/21/22/23/24 | 1,4 / 10,2 / 20,8 / 1,6 / 4,5 / 7,0 % | 0,4 / 17,1 / 25,6 / −1,1 / 4,7 / 7,5 % | G (2019 Teiljahr) |
| **mit einem Börsenausfall (50 % Kapital weg)** | **−4,9 % p.a.** | **−3,8 % p.a.** | G |
| Funding brutto annualisiert seit 2026-07 (Dev-Nachschau) | 5,9 % | 4,5 % | G |

**Kill-Kriterien (vorab):** Rendite > 4 % ✓, negative 30-Tage-Fenster < 25 % ✓, Drawdown < 10 % ✓, für beide Coins. **K1 besteht die Entwicklungsphase.**

**Warnung zur Sharpe von 6 bis 7:** Das ist kein Wunder, sondern ein Messfehler-Kandidat. Die Rechnung enthält das größte Risiko nicht, weil es in den Daten nie eintrat: Ausfall der Börse, Einfrieren von Auszahlungen, Stablecoin-Entkopplung. Der Drawdown von 1,8 % ist der Drawdown *gegeben, dass Binance überlebt*. Eine einzige FTX-artige Pleite dreht fünf Jahre Gewinn ins Minus (Zeile oben).

**Breite (12 Coins, nicht vorab als Test angemeldet, nur Robustheit):** Gleichgewichtetes Portfolio +6,5 % p.a., Sharpe 3,5, Max Drawdown −6,6 % (G). Aber SOL −5,6 % p.a. mit −38 % Drawdown, BNB −1,6 % (G). Ursache SOL: FTX-Woche November 2022, Carry −31 % in rund zwei Wochen (G), weil alle gleichzeitig SOL leerverkaufen wollten: Funding drehte tief negativ (schlechteste 30 Tage −36 %, G) und die Basis riss. **Der Hedge ist nur so gut wie die Annahme, dass die Masse nicht dieselbe Seite will wie du.**

**Stressfenster (Carry-Ergebnis in der Woche):**

| Ereignis | BTC | ETH | SOL |
|---|---|---|---|
| Covid 2020-03-12 | −0,9 % | −0,6 % | n/a |
| Mai-Crash 2021 | +0,4 % | +0,3 % | +0,05 % |
| LUNA 2022-05 | 0,0 % | −0,1 % | −0,9 % |
| Celsius/3AC 2022-06 | 0,0 % | −0,3 % | −0,4 % |
| FTX 2022-11 | −0,3 % | −0,3 % | **−30,9 %** |
| Yen-Carry 2024-08-05 | +0,05 % | 0,0 % | 0,0 % |

Alles G. Nicht in Krypto-Daten vorhanden: 2008, Flash Crash 2010, CHF 2015. Krypto-Analogon zum CHF-Peg-Bruch ist die Stablecoin-Entkopplung: USDC fiel im März 2023 kurz auf rund 0,88 USD (L, Circle/SVB). Wer USDC als Margin hält, verliert im Carry genau dann.

**Ausfall-Verhalten (Börse 3 Tage nicht erreichbar):** Der Short-Perp kann dann nicht mit Margin nachgefüttert werden. Größter Perp-Anstieg (Tageshoch) in 3 Tagen: BTC +43 %, ETH +203 % (Covid-Wick 2020-03-13), SOL +105 % (G, auf Last-Price-Hochs; Liquidationen laufen über den geglätteten Mark-Price, echtes Risiko also kleiner, S). Mit 0,5 Margin (2-facher Hebel auf der Short-Seite) liegt die Liquidation grob bei +45 bis +50 % (S). **Bei ETH hätte ein dreitägiger Ausfall im März 2020 das Short-Bein liquidiert, während das Spot-Bein woanders lag.** Folge: mehr Margin (Kapital 2,0 statt 1,5 senkt die Rendite um ein Viertel, auf ≈ 6,3 % BTC bzw. 7,7 % ETH, S aus G×0,75) oder beide Beine auf derselben Börse mit Portfolio-Margin (dann volles Börsenrisiko an einem Ort).

**Signal-Ausfall:** K1 hat kein Signal. Ausfall der Datenquelle ändert nichts. Das ist ein Qualitätsmerkmal.

### K2 Zwangsverkäufer-Reversal: tot

Mittlere Überrendite der Ereignisse gegenüber der unbedingten Rendite gleicher Haltedauer, nach 0,4 % Kosten. p = Anteil zufälliger Einstiegsdaten mit mindestens so gutem Mittel (10 000 Ziehungen).

| Coin | Auslöser | Haltedauer | Ereignisse | EV je Trade | Basis | Überrendite | p | Treffer | Hälfte 1 / 2 |
|---|---|---|---|---|---|---|---|---|---|
| BTC | Funding | 4 Wo | 11 | +4,8 % | +5,5 % | −0,7 % | 0,52 | 55 % | −1,9 / +0,8 % |
| BTC | Funding | 8 Wo | 8 | +13,2 % | +12,2 % | +1,0 % | 0,44 | 50 % | +2,0 / −0,7 % |
| BTC | Preis | 4 Wo | 26 | +1,2 % | +4,9 % | −3,6 % | 0,82 | 58 % | −3,7 / −3,6 % |
| BTC | Preis | 8 Wo | 19 | +7,8 % | +11,1 % | −3,3 % | 0,65 | 53 % | −1,5 / −5,3 % |
| ETH | Funding | 4 Wo | 11 | −5,5 % | +5,8 % | −11,3 % | 0,94 | 27 % | −12,7 / −4,7 % |
| ETH | Funding | 8 Wo | 8 | +8,5 % | +11,1 % | −2,5 % | 0,53 | 38 % | +0,5 / −23,9 % |
| ETH | Preis | 4 Wo | 23 | −5,2 % | +6,1 % | −11,3 % | 0,99 | 35 % | −14,2 / −8,6 % |
| ETH | Preis | 8 Wo | 18 | +0,2 % | +13,1 % | −12,8 % | 0,92 | 44 % | −8,6 / −18,2 % |

Alles G. **Keine der 8 Varianten** besteht. Bei ETH ist "kaufen nach dem Absturz" sogar deutlich schlechter als zufälliges Kaufen (fallendes Messer). Die 10 weiteren Coins (nur Funding-Auslöser, Robustheit): 10 von 20 Varianten positiv, also Münzwurf, keine mit p < 0,05, bestes LINK 4 Wo +12 % bei p 0,09 (G). Monte Carlo über die Reihenfolge der Trades: 95-%-Schlechtfall-Drawdown beim Hintereinander-Ausführen der BTC-Ereignisse −47 % (4 Wo) bis −69 % (G). Nicht tragbar.

**Wo die Zwangsverkaufs-Prämie wirklich lebt (Diagnose, nachträglich, kein Test):** Gepoolt über 12 Coins, 178 Ereignisse, Überrendite nach Haltedauer: 1 Tag +0,20 %, 3 Tage −0,04 %, 7 Tage +0,35 %, 14 Tage +0,66 %, 28 Tage −2,6 %, 56 Tage −5,0 % (G, vor Kosten von 0,4 %). Auf Tageskerzen ist nach Kosten nichts übrig. **Die Prämie aus Zwangsverkäufen wird innerhalb von Minuten bis Stunden geerntet, von denen, die im Moment der Liquidation Liquidität stellen.** Auf Wochen-Horizont ist sie weg. Das ist die wichtigste Einzelaussage für den Liquidations-Engine-Thread: Die Engine kann einen Edge nur intraday haben, nicht für DiamondHamsters Horizont.

### K3 Überhitzungsfilter: tot

| | BTC | ETH | Quelle |
|---|---|---|---|
| Fenster | 2020-09-20 bis 2024-12 | 2020-12-06 bis 2024-12 | G |
| Anteil "heißer" Wochen | 11,6 % | 12,7 % | G |
| Timing-Wert pro Woche | −0,02 % | −0,07 % | G |
| t (wöchentlich) | −0,18 | −0,60 | G |
| Jahre negativ | 2 von 5 | 3 von 5 | G |
| Mit 3 Tagen Signal-Verspätung | −0,04 %, t −0,34 | −0,03 %, t −0,28 | G |
| Mit 10 % fehlenden Funding-Daten | −0,04 %, t −0,38 | −0,08 %, t −0,67 | G |

Kill-Kriterium t > 2 klar verfehlt. Auf 12 Coins: 10 von 12 negativ (G). Bestätigt E-023 (Perp-Basis als KI-Zeile: +0,01, nichts). Hohes Funding warnt vor Crashs (BIS-Papier, L), aber nicht so, dass Exposure-Senken sich nach Kosten lohnt: Die Euphorie läuft oft noch weiter.

### K4 Trend plus Vol-Steuerung (Kontrollarm): tot als Edge

Walk-Forward 2017 bis 2024, Coinbase-Kerzen, wöchentlich, nach Kosten.

| | BTC Strategie | BTC Buy & Hold | BTC feste Position gleiche Ø-Gewichtung | ETH Strategie | ETH Buy & Hold | ETH feste Position |
|---|---|---|---|---|---|---|
| CAGR | 51,0 % | 76,2 % | 41,8 % | 84,5 % | 112,0 % | 71,2 % |
| Sharpe | 1,13 | 1,15 | 1,15 | 1,23 | 1,26 | 1,26 |
| Max Drawdown | −67,8 % | −83,8 % | −55,8 % | −77,2 % | −94,0 % | −76,9 % |
| Calmar | 0,75 | 0,91 | 0,75 | 1,09 | 1,19 | 0,93 |
| Längste Zeit im Drawdown | 1342 Tage | 1079 | 1039 | 1079 | 1148 | 1080 |
| Tail-Ratio | 1,33 | 1,31 | 1,26 | 1,41 | 1,25 | 1,18 |
| Ø Gewicht | 0,50 | 1,00 | 0,50 | 0,56 | 1,00 | 0,56 |
| Rang gegen 1000 Zufalls-Timings (gleiche Gewichte, Blöcke gemischt) | Sharpe 87 %, CAGR 85 % | | | Sharpe 86 %, CAGR 85 % | | |

Alles G. DCA (monatlich): IRR BTC 62 %, ETH 72 % (G). Gewählte Längen BTC: 200 Tage 2017 bis 2021, dann 50; ETH springt zwischen 50, 150 und 200 (G). Instabile Parameterwahl ist ein Warnzeichen für sich.

**Urteil nach Vorab-Kriterium:** Sharpe unter Buy & Hold, Rang unter 95 %. **Tot als Edge.** Und schlimmer für die Idee "Trendfilter als Risikomanagement": Eine **feste halbe Position** hat bei BTC dieselbe Sharpe, kleineren Drawdown (−56 % statt −68 %) und kürzere Durststrecke. **Positionsgröße schlägt Timing.** Das ist derselbe Befund wie bei allen 37 KI-Versuchen.

### Regime-Aufschlüsselung (K4, Jahresrenditen, G)

| Jahr | BTC Strat | BTC B&H | ETH Strat | ETH B&H |
|---|---|---|---|---|
| 2017 | +521 % | +1324 % | +3061 % | +8984 % |
| 2018 | −32 % | −73 % | −44 % | −82 % |
| 2019 | +42 % | +94 % | −16 % | −2 % |
| 2020 | +183 % | +305 % | +239 % | +474 % |
| 2021 | −15 % | +59 % | +209 % | +398 % |
| 2022 | −30 % | −64 % | −48 % | −67 % |
| 2023 | +90 % | +156 % | +34 % | +91 % |
| 2024 | +42 % | +121 % | +24 % | +46 % |

Der Trendfilter halbiert Bärenjahre und drittelt Bullenjahre. Netto ein Tausch, kein Gewinn.

---

## Phase 4: Falsifikation

### Kill-Kriterien gegen Ergebnisse

| Test | Kriterium (vorab) | Ergebnis | Urteil |
|---|---|---|---|
| K1 BTC | > 4 % p.a., < 25 % neg. 30-T, DD < 10 % | 8,4 %, 9,9 %, −1,8 % | **lebt** |
| K1 ETH | dito | 10,2 %, 12,0 %, −1,8 % | **lebt** |
| K2 (8 Varianten) | Überrendite > 0, p < 0,05, gleiches Vorzeichen in beiden Hälften | beste p 0,44 | **tot** |
| K3 BTC/ETH | t > 2, höchstens Hälfte der Jahre negativ | t −0,18 / −0,60 | **tot** |
| K4 BTC/ETH | Sharpe und CAGR über B&H und über 95 % Zufall | Sharpe unter B&H, Rang 86 % | **tot** |

14 Tests, Bonferroni-Schwelle p < 0,0036. K1 hat keinen p-Wert im klassischen Sinn (kein Signal, nur Mittelwert eines Zahlungsstroms): Sein t-Wert der Tagesrendite liegt bei Sharpe 6,6 über 5,3 Jahren grob bei 15 (S aus G, Sharpe × √Jahre). Statistisch eindeutig, ökonomisch hängt er an Annahmen außerhalb der Daten.

**Gezählte Varianten insgesamt:** 14 vorab + 1 nachträgliche Carry-Variante ("nur an, wenn letzte 7 Tage > 10 % p.a."), die schlechter war (BTC 4,5 %, ETH 6,7 %, G) + Robustheit auf 10 weiteren Coins. Nachträgliche Varianten zählen nicht als Bestätigung.

### Ablation: Wie viel trägt jede Annahme? (für K1, den Überlebenden)

| Annahme weggenommen | Wirkung | Quelle |
|---|---|---|
| **Perfekte Latenz** | Fast keine. Carry verdient alle 8 Stunden; ob die Order 1 s oder 1 min braucht, ist egal. | S |
| **10 % der Daten fehlen** | Keine, K1 nutzt kein Signal. (Bei K3: Timing-Wert von −0,02 auf −0,04 %/Woche, war ohnehin tot, G) | G |
| **Kosten verdoppelt (0,4 % pro Seite)** | Die Hedge-Pflege kostet heute 1,65 (BTC) bzw. 2,2 (ETH) Prozentpunkte des Nominals pro Jahr (G). Verdoppelt: Rendite auf Kapital ≈ 7,3 % BTC, ≈ 8,7 % ETH. Bleibt über Hürde. | S aus G |
| **Kapital 100× größer** | Funding fällt, weil der eigene Short es drückt. Elastizität unbekannt; Beobachtung: Mit dem Wachstum industrieller Carry-Produkte fiel BTC-Funding von 11,9 % (2024) auf 5,9 % (2026 H2) | G für Niveaus, S für Ursache |
| **Margin konservativer (Kapital 2,0 statt 1,5)** | Rendite × 0,75 → BTC ≈ 6,3 %, ETH ≈ 7,7 % | S aus G |
| **Börse fällt einmal aus (50 % Verlust)** | Von +8,4 % auf −4,9 % p.a. | G |
| **Ein Coin, auf den die Masse short will (SOL im FTX-Fall)** | −31 % in zwei Wochen | G |

**Wo der Edge wirklich sitzt:** nicht in Latenz, nicht in Daten, nicht im Signal. Er sitzt in **(1) wie viel Kapital man je Einheit bindet, (2) wo man es lagert, (3) welche Coins man meidet.** Reines Risikomanagement.

### Red Team: Wie würde ein Gegner den Carry-Bot ausnutzen?

1. **Funding-Squeeze:** Ein großer Akteur treibt den Perp kurz hoch (Wick), um überhebelte Shorts zu liquidieren. Bei 2-fachem Hebel auf dem Short-Bein ist der Carry-Bot so ein Short. Gegenmittel: niedriger Hebel, Mark-Price-Abstand überwachen.
2. **Crowding derselben Seite:** Wenn ein Coin stirbt (FTX/SOL), wollen alle short. Funding dreht negativ, Carry zahlt statt kassiert. Vorhersehbar, aber nicht vermeidbar, wenn man schon drin ist.
3. **Auto-Deleveraging:** Im Extremfall schließt die Börse gewinnende Positionen zwangsweise, um Verlierer zu decken. Dann ist das Short-Bein weg, das Spot-Bein nackt.
4. **Was ich vorhersehe und trotzdem nicht verhindern kann:** einen Börsenausfall. Ich sehe Warnsignale (Auszahlungsstopps, Gerüchte), aber Auszahlungen werden genau dann gestoppt, wenn ich sie brauche. Diversifikation über Börsen verkleinert das Risiko, beseitigt es nicht.

---

## Phase 5: Rückkehr zur Realität

### Was war live unmöglich (Axiom 6)?

| Axiom | Live? |
|---|---|
| 1. Jeder Tick, Level-3-Orderbuch | Für uns nein. Hätte aber den Überlebenden nicht verbessert. Wäre nur für die Intraday-Liquidationsprämie nötig (siehe K2-Diagnose), und dort konkurrieren wir mit Firmen, die co-located sind. |
| 2. Jede News mit 0 ms | Unmöglich. Für Carry irrelevant. |
| 3. Alle Fundamentaldaten, Satellitenbilder | Teils kaufbar. Für Krypto ohne Cashflows nahezu wertlos. |
| 4. Unendlich Compute | Unnötig. Der Überlebende ist eine Zeile Arithmetik. |
| 5./6. Unbegrenzte Forschungszeit, Unmögliches annehmen | Das einzig Unmögliche, das zählt: **Börsenausfall-Wahrscheinlichkeit kennen.** Sie steht in keinem Datensatz. |

**Ehrlich: Für den Erfolg nötig waren keine der Superkräfte.** Nötig war (a) eine Börse, die nicht pleitegeht, (b) dass die Gegenseite weiter Hebel will, (c) dass man nicht auf der Seite der Masse steht. Alle drei sind Annahmen über die Welt, nicht über unsere Fähigkeiten.

### 20 % Aufbau, 80 % Ergebnis

Der kleinste Bot, der den Kern enthält:
1. Spot BTC und ETH kaufen, gleiche Menge Perp leerverkaufen. Kein Signal.
2. Margin so, dass ein +60-%-Tag das Short-Bein nicht liquidiert. Täglich nachgleichen.
3. **Aus-Schalter (einziger Code, der zählt):** raus, wenn das 30-Tage-Funding unter die Kostenhürde fällt; raus, wenn Auszahlungen einer Börse stocken; nur Coins, bei denen Funding selten negativ ist (BTC, ETH; nicht SOL, BNB nach diesen Daten).
4. Über mindestens zwei Börsen verteilt.

Das ist, ehrlich gesagt, ein Kontoverwaltungsskript, keine KI. **Langweilig ist hier wirklich das Qualitätsmerkmal.**

### Der Edge liegt nicht in der Signalidee

Ja, das ist das Ergebnis, und es wird hiermit gesagt. Drei Richtungsideen mit sauberer Gegenpartei-Begründung sind auf Wochen-Horizont tot. Die einzige lebende Rendite kommt aus dem Tragen eines Risikos (Hebel vermieten), und ob sie sich lohnt, entscheiden Kosten, Kapitalbindung, Börsenwahl und Ausschalter.

### Was das konkret für DiamondHamster heißt

1. **Für die Analyse-Rolle (Wochen bis Monate):** Die richtige Ausgabe ist meistens "Positionsgröße nach Volatilität, kein Timing" plus "nichts tun". Das bestätigen jetzt K3, K4 und die 37 KI-Versuche aus drei Richtungen. Eine feste Position in der Größe, die man aushält, ist die Latte, und sie ist schwer zu schlagen.
2. **Funding als Thermometer, nicht als Signal:** Es zeigt, wie viel die Masse für Hebel zahlt. Das ist Kontext für eine bedingte Sicht ("die Euphorie ist teuer"), aber K3 zeigt: kein Handelssignal.
3. **Liquidations-Engine (Hyblock-Thread):** Ihr möglicher Wert liegt intraday (K2-Diagnose: Wochen-Horizont leer). Für DiamondHamsters Horizont sollte die Engine nicht als Signalquelle verkauft werden. Das ist eine Information für Aarons Entscheidung, ob er sie weiterbaut, keine Empfehlung zum Abbruch.
4. **Wenn irgendwann gehandelt wird:** zuerst K1, nicht eine Richtungsstrategie. Er hat die Entwicklungsphase bestanden. Nächster Schritt nach Protokoll wäre der einmalige Holdout-Test 2025-01 bis 2026-06 mit vorab festgelegter Schwelle. **Warnung vorab:** Die Dev-Nachschau ab 2026-07 zeigt BTC-Funding 5,9 % und ETH 4,5 % brutto (G); nach Hedge-Pflege auf 1,5-faches Kapital sind das ≈ 2,8 % bzw. 1,5 % (S aus G, Pflegekosten wie 2019 bis 2024 angenommen), also deutlich unter der 4-%-Hürde. Der Edge könnte gerade verschwinden.

---

## Schluss

### (a) Der Kern des Edges in einem Satz

**Wer Hebel vermietet statt Kurse vorherzusagen, wird von gehebelten Käufern bezahlt, die nicht Nein sagen können, und der ganze Rest des Edges ist, die Börse, die Margin und die Coins so zu wählen, dass man den Tag überlebt, an dem diese Zahlung umdreht.**

### (b) Die 5 Killer-Annahmen

1. **Die Börse bleibt zahlungsfähig und Auszahlungen laufen.** Ein FTX-artiger Ausfall mit 50 % Verlust dreht +8,4 % in −4,9 % p.a. (G).
2. **Die Masse will weiter gehebelt long sein.** Funding BTC 30,6 % (2021) → 11,9 % (2024) → 5,9 % (2026 H2) (G). Die Prämie schrumpft bereits.
3. **Der Hedge bleibt ein Hedge.** Basis und Funding bleiben eng, weil man nicht auf der Seite der Masse steht. SOL im FTX-Fall: −31 % in zwei Wochen (G).
4. **Das Short-Bein überlebt Kurssprünge.** Bei 2-fachem Hebel kann ein +45-%-Mark-Price-Sprung liquidieren; Tageshochs von +36 % (BTC, 1 Tag) und +203 % (ETH-Wick 2020) kamen vor (G, Last-Price).
5. **Collateral behält seinen Wert.** USDC-Entkopplung März 2023 auf ≈ 0,88 USD (L). Steuer nicht modelliert und für Aarons OÜ unbekannt.

### (c) Die 5 Zahlen, an denen der Bot scheitern wird

1. **Funding brutto < ≈ 8 % p.a.** Darunter liegt die Rendite auf 1,5-faches Kapital nach Kosten unter 4 % (S aus G: 4 % × 1,5 + Hedge-Pflege 1,65 bzw. 2,2 Prozentpunkte). **Heute schon unterschritten: 5,9 % BTC, 4,5 % ETH (G).**
2. **Börsenausfall-Wahrscheinlichkeit > ≈ 9 % pro Jahr.** Break-even: (8,4 % − 4 %) / 50 % Verlust (S aus G). Die echte Rate kenne ich nicht (siehe d).
3. **Mehr als 25 % negative 30-Tage-Fenster** (Vorab-Kriterium). Heute 9,9 % BTC, 12,0 % ETH (G).
4. **Ein Basis-/Funding-Schock > 10 % des Kapitals in zwei Wochen.** Ist bei SOL mit −31 % passiert (G); bei BTC/ETH bisher max. −0,9 % (G).
5. **Eigene Größe > ≈ 1 % des täglichen Perp-Volumens** (BTC 2024 ≈ 160 Mio USD, G für Volumen, S für Schwelle). Darüber frisst Marktimpact die Kostenannahme, und der eigene Short drückt das Funding.

### (d) Was ich selbst noch nicht weiß

- **Die echte Börsenausfall-Rate.** Sie ist die wichtigste Zahl des ganzen Bots und steht in keinem Datensatz.
- **Wie elastisch Funding auf die eigene Größe reagiert.** Ich sehe den Rückgang, kann ihn aber nicht sauber Ethena oder anderen Ursachen zuordnen.
- **Ob die Zwangsverkaufs-Prämie intraday groß genug ist**, um sie mit der eigenen Liquidations-Engine zu ernten. Tageskerzen sehen sie nicht, die Engine-Daten (Mac) könnten.
- **Wie K1 im Holdout 2025-01 bis 2026-06 aussah.** Absichtlich nicht angeschaut.
- **Ob 2026 H2 ein dauerhaft niedrigeres Funding-Regime ist** oder nur eine ruhige Phase. 108 Tage sind zu wenig.
- **Steuerliche Behandlung** von Funding-Einnahmen und Perp-Gewinnen für eine estnische OÜ.

---

## Worauf es wirklich ankommt (der Test des Prompts)

Nicht auf Daten, Latenz, Compute oder eine klügere Signalidee. Wir haben die Superkräfte ausgeschaltet und nichts verloren, was überlebt hatte. Es kommt darauf an, **wessen Risiko man trägt und ob man den Tag überlebt, an dem es eintritt.** Für DiamondHamster heißt das: Die Suche nach dem Timing-Signal auf Wochen-Horizont kann enden; die Arbeit verschiebt sich zu Positionsgröße, Kosten und, falls je gehandelt wird, zu Bilanzmiete mit einem guten Aus-Schalter.

---

## Anhang: Dateien und Reproduktion

- Kill-Kriterien vorab: `research/quant-edge/00-killkriterien.md`
- Code (Repo, Branch `claude/project-thread-lcuib5`, Ordner `research/quant-edge/`): `qe_common.py` (Laden, Holdout-Schnitt, Kennzahlen), `qe_binance.py`, `k4_trend_vol.py`, `k123_funding.py`, `diagnose.py`
- Ergebnisse als JSON: `research/quant-edge/ergebnisse/` (k4.json, k123.json, diagnose.json)
- Rohdaten mit sha256 und allen 161 Request-URLs: `research/quant-edge/daten/` (request.json, sha256.txt)
- Holdout: keine Zeile aus 2025-01-01 bis 2026-06-30 geladen oder verwendet. Die Coinbase-Dateien im Repo enthalten den Holdout; `qe_common.drop_holdout` entfernt ihn beim Laden und prüft per assert.

### Literatur
- Grossman, Stiglitz (1980): On the Impossibility of Informationally Efficient Markets. AER.
- Stoll (1978): The Supply of Dealer Services in Securities Markets. Journal of Finance.
- Shleifer, Vishny (1997): The Limits of Arbitrage. Journal of Finance.
- Coval, Stafford (2007): Asset Fire Sales (and Purchases) in Equity Markets. JFE.
- Carr, Wu (2009): Variance Risk Premiums. Review of Financial Studies.
- Moskowitz, Ooi, Pedersen (2012): Time Series Momentum. JFE.
- Frazzini, Pedersen (2014): Betting Against Beta. JFE.
- Tóth et al. (2011): Anomalous Price Impact and the Critical Nature of Liquidity in Financial Markets. Physical Review X.
- Schmeling, Schrimpf, Todorov (2023): Crypto Carry. BIS Working Paper 1087.
- USDC-Entkopplung März 2023 nach Silicon-Valley-Bank-Schließung (Circle-Mitteilungen, Presseberichte).
