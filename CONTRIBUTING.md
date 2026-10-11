# Ideen beitragen

Danke, dass du mitdenkst. Das Projekt lebt von Ideen, die wir selbst nicht hatten. Gleichzeitig gilt: Jede Idee wird gleich hart getestet, und eine widerlegte Idee ist genauso ein Ergebnis wie eine bestätigte.

## Was gesucht wird

| Art | Beispiel |
|---|---|
| **Prompt** | "Lass die KI zuerst das Regime benennen", "verbiete Kursziele", "lass sie wie ein Risk-Manager denken" |
| **Daten** | eine zusätzliche Zeile (Funding, Open Interest, M2, On-Chain), weniger Historie, Gesamtmarkt als Vergleich |
| **Format** | Renditen statt Preise, Wochenkerzen, nur Kennzahlen, Tabelle anders aufbauen |
| **Regel-Hypothese** | eine Beobachtung aus der Praxis, die man als feste Regel testen kann (ohne KI) |
| **Kritik an der Methode** | ein Leak, eine unfaire Baseline, eine Metrik, die sich austricksen lässt |

## So reichst du eine Idee ein

1. [Neues Issue → "Idee für einen Versuch"](../../issues/new/choose) und das Formular ausfüllen.
2. Wichtig sind drei Dinge:
   - **Genau eine Änderung.** "Mehr Indikatoren und anderer Prompt" sind zwei Versuche.
   - **Warum** es helfen sollte (der Mechanismus, nicht nur "ist bekannt").
   - **Woran man sieht, dass es nicht klappt.** Was müsste herauskommen, damit du sagst: war nichts?
3. Schau vorher in [docs/VERSUCHE.md](docs/VERSUCHE.md), ob es schon getestet wurde oder im Backlog steht.

## Was danach passiert

1. Die Idee kommt in den Backlog (Label `idee`), mit Verweis auf dein Issue.
2. Sie läuft als Versuch E-NNN im Spielplatz: eine Änderung gegen den aktuellen Champion, 13 feste Wochen, 30 Coins, automatisches Urteil (`schlechter` / `kein messbarer Unterschied` / `Kandidat` / `neuer Dev-Champion` / `verworfen`).
3. Ergebnis, voller Prompt und die komplette Überlegung der KI werden im Issue verlinkt. Das Issue wird mit dem Urteil geschlossen.
4. Ein Dev-Champion kann samstags ins Zukunfts-Turnier (höchstens einer pro Woche). Erst dort zählt er.

Regelbasierte Hypothesen (ohne KI) laufen über eine Hypothesen-Karte ([hypotheses/TEMPLATE.md](hypotheses/TEMPLATE.md)): erst Karte, dann Test auf Historie bis 2024, Holdout erst ganz am Ende.

## Was nicht angenommen wird

- Ideen, die Daten aus der Zukunft brauchen oder das Datum bzw. den Coin verraten (z. B. Mondphase mit echtem Datum, solange das nicht anonym geht).
- "Teste 20 Parameter und nimm den besten." Jede Variante zählt als eigener Versuch.
- Kaufsignale, Kursziele, Coin-Tipps. Das Projekt gibt keine.

## Code-Beiträge

Pull Requests sind willkommen, wenn sie zu einem Issue gehören. `pytest -q` muss grün sein. Prompts mit geloggten Läufen werden nie geändert, nur als neue ID kopiert. Regeln: [docs/PROTOKOLL.md](docs/PROTOKOLL.md).
