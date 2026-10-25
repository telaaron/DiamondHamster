# Runde 3, Phase 6: 20 Fälle von Hand geprüft (A2-S)

Frage aus dem Brief: Hat die KI die Richtung aus dem Inhalt gelesen oder aus dem Stil geraten?

Stichprobe: 20 der 159 A2-S-Dokumente mit Richtung ≠ 0, Zufall mit Seed 20261016, gezogen **vor** Ansicht der Renditen je Fall. Geprüft: (1) steht der zitierte Beleg wörtlich im pseudonymisierten Text, (2) trägt der Beleg die Richtung, (3) gibt der Leser mit nur den ersten 50 Wörtern dieselbe Richtung (Stil-/Kategorie-Kontrolle).

| ID | Richtung | Z | 50 W. | Beleg (gekürzt) | Inhalt trägt Richtung? |
|---|---|---|---|---|---|
| cb7a3788a4 | +1 | 3 | 0 | PFS 14,5 gegen 8,5 Monate, HR 0,50 | ja, nur aus dem Haupttext |
| ba9647648c | −1 | 3 | −1 | Wandlung zu 92 % des tiefsten VWAP | ja (Giftfinanzierung) |
| 4f287a8590 | −1 | 2 | 0 | Jury spricht 20 + 36 Mio USD zu | **unklar**: hängt davon ab, ob die Firma Klägerin oder Beklagte ist |
| e970fb64ac | +1 | 1 | 0 | Poison Pill läuft früher aus | ja, schwach |
| 2b4e82e29c | −1 | 2 | −1 | ATM-Programm erhöht | ja (Verwässerung) |
| 71b6ba990d | −1 | 2 | −1 | ATM bis 30 Mio USD | ja |
| 450afb3799 | +1 | 1 | 0 | Zinssatz der Kreditlinie gesenkt | ja, klein |
| 39248a31ac | +1 | 3 | +1 | Barabfindung 43 USD je Aktie | Inhalt ja, aber **schon per Pressemitteilung bekannt** (Fusionsarbitrage, keine Aufmerksamkeitslücke) |
| 4218ab8e81 | −1 | 2 | 0 | Sammelklage eingereicht | ja |
| 4dbff2d709 | −1 | 1 | 0 | Handel der Warrants ausgesetzt | ja; **Text enthält Rest-Leck** (XBRL-Kopf mit Datum, siehe unten) |
| 0e8bbead96 | −1 | 2 | −1 | ATM bis 150 Mio USD | ja |
| 9191c23b8c | −1 | 1 | 0 | EBITDA-Ausblick niedriger | ja |
| 1f6a2d9554 | −1 | 2 | −1 | Warrant-Ausübungspreis gesenkt | ja |
| 1ce511f623 | +1 | 1 | +1 | Fusion: 0,1 Aktien + 1,14 USD | **Schablone**: kein Aufschlag im Text erkennbar, "Fusion = gut" |
| 144295c9a2 | +1 | 3 | +1 | Barabfindung 127 USD | wie 39248a31ac |
| 0e97404c47 | −1 | 2 | 0 | 18,46 % neue Aktien | ja |
| 81fba282f3 | −1 | 1 | 0 | Vorzugsaktien + Warrants, 3,5 Mio USD | ja |
| 52675a0939 | +1 | 1 | 0 | Kreditmarge gesenkt | ja, klein |
| c23695cd6b | −1 | 2 | −1 | 214 Mio Aktien + 429 Mio Warrants | ja |
| 87ccd1bac5 | −1 | 2 | −1 | Angebot bis 50 Mio USD | ja |

Ergebnis (G, n = 20):
- Beleg wörtlich im Text: **20 von 20**. Keine erfundenen Zitate.
- Richtung folgt aus dem zitierten Inhalt: **17 von 20**. Ein Fall unklar (Gerichtsurteil ohne Parteirolle), ein Fall Schablone (Fusion ohne Preisinfo), zwei Fälle inhaltlich richtig, aber die Information war vorher schon öffentlich (Barabfindung).
- Gleiche Richtung schon aus 50 Wörtern: **10 von 20**. Die Hälfte der Urteile ist also eine Kategorie-Zuordnung ("ATM", "Fusion", "Warrant-Inducement"), die im ersten Satz steht. Echtes Tiefenlesen (Studiendaten, Kreditkonditionen, Auflagen) kam in der anderen Hälfte vor.

Gesamt über alle 159 (G, ergebnisse/extra.json): 50-Wörter-Leser gibt in 37 % dieselbe Richtung, in 0,6 % die Gegenrichtung, sonst 0. **Rendite-Split (deskriptiv, nicht vorab angemeldet):** Trades, bei denen schon 50 Wörter dieselbe Richtung gaben, netto +2,7 % (n 58, t 1,13); Trades, die nur aus dem Volltext kamen, netto −1,9 % (n 97, t −1,31). Das Tiefenlesen hat also nichts beigetragen, eher geschadet.

**Antwort auf die Brief-Frage:** Die KI liest den Inhalt korrekt und belegt ihn wörtlich. Sie rät nicht aus dem Tonfall. Aber der Teil ihrer Urteile, der Geld bringen müsste (die Information, die tief im Text steckt), bringt keins; der Teil, der aus der Überschrift kommt, ist bekannte Kategorie-Information (Verwässerung schlecht, Rückkauf gut).

## Nebenfund: Rest-Leck der Pseudonymisierung

10 von 499 A2-S-Texten (2 %) enthalten noch Jahr oder CIK aus einem XBRL-Kopf, weil dort kein "Item x.xx" vor dem Kopf stand und das Datums-Regex an zusammengeklebten Zeichen (`2026-08-132026-08-13`) nicht griff (G). Davon 2 Trades. Ohne diese 10: netto +0,04 % (n 154), Urteil unverändert. Fix für den Forward-Test: XBRL-Kopf (`dei:`, `us-gaap:`, 10-stellige CIK) immer entfernen, Datumsmuster ohne Wortgrenze.
