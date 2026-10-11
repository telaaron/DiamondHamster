# Versuche: Übersicht

Dev-Champion: **E-003**
Varianten bisher getestet: **4**. Je mehr Varianten, desto sicherer ist die beste davon auch Glück: ein Dev-Sieg ist nur ein Filter, zählen tut das Turnier.
Verbrauch gesamt: 55 USD Listenpreis (gegen Aarons Claude-Limit)

| ID | Achse | Änderung | Basis | Diff/Woche A | t | ohne beste Woche | B+C | Urteil | Thread |
|---|---|---|---|---|---|---|---|---|---|
| [E-000](E-000/card.md) | prompt | Referenz: T-001 (180 Tageskerzen, anonymisiert) | - | eigener Wert -0.235 | -0.8 | | eigener Wert -0.304 | Referenz |  |
| [E-001](E-001/card.md) | daten | T-002: plus eine Zeile mit 19 Indikatoren | E-000 | 0.116 | 1.69 | 0.083 | -0.063 | kein messbarer Unterschied |  |
| [E-002](E-002/card.md) | prompt | Ruhe als Standard: mittleres Gewicht (~0,5) halten, nur bei klarer Evidenz abweichen; jede Umschichtung kostet | E-000 | 0.055 | 0.34 | -0.039 |  | kein messbarer Unterschied | [Thread](https://claude.ai/code/project/chan_01VH1Un8SQtbifKwzD9jDguD?thread=cmsg_01VH1Un8SQtbifKwzD9jDguDD3MYEvodR83Vg998zcfS9X) |
| [E-003](E-003/card.md) | prompt | Sichtbares Denken: erst Strategie, dann pro Fenster Marktlesart, Gewicht mit Begründung und Kipp-Preis, zuletzt das JSON | E-000 | 0.084 | 1.04 | 0.049 | -0.262 | kein messbarer Unterschied | [Thread](https://claude.ai/code/project/chan_01VH1Un8SQtbifKwzD9jDguD?thread=cmsg_01VH1Un8SQtbifKwzD9jDguDPqfqsXbf1uUjcQYGgzfjDy) |
| [E-004](E-004/card.md) | prompt | Relativ statt absolut: Fenster sind verschiedene Märkte derselben Woche; vergleichen, mehr Gewicht auf die stärksten, weniger auf die schwächsten (ersetzt 'Judge every window on its own') | E-003 | -0.487 | -2.16 | -0.557 |  | schlechter | [Thread](https://claude.ai/code/project/chan_01VH1Un8SQtbifKwzD9jDguD?thread=cmsg_01VH1Un8SQtbifKwzD9jDguD4mK27Xxe67JynWUkCdjmgV) |
