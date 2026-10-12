# DiamondHamster 🐹💎

**Wir testen öffentlich, ob eine KI beim Krypto-Investieren wirklich hilft. Oder ob das nur gut klingt.**

> Labor statt Casino. Keine Anlageberatung, kein echtes Geld im Spiel, keine Kaufsignale.

---

## Worum geht's?

Viele behaupten, ihre KI oder ihr Bot schlägt den Markt. Fast keiner zeigt, wie er das gemessen hat.

Wir machen es andersherum: Eine KI bekommt jede Woche Kursdaten von 30 Coins und entscheidet, wie viel sie investiert hätte, zwischen 0 % und 100 %. Am Ende vergleichen wir mit der langweiligsten Strategie, die es gibt: **einfach eine feste Menge liegen lassen.** Nur wenn die KI das schlägt, hat sie etwas gekonnt.

Damit die KI nicht schummeln kann, sieht sie weder Datum noch Coin-Namen. Und gezählt werden nur Wochen, die sie nicht schon aus ihrem Training kennt.

## Wo stehen wir?

*Stand: 12. Oktober 2026*

- **Bisher schlägt die KI das "Liegenlassen" nicht.** In über 10 Versuchen mit verschiedenen Anleitungen und Daten war keiner messbar besser.
- **Was sie falsch macht:** Sie kauft, wenn der Kurs schon gestiegen ist, und steigt aus, wenn er schon gefallen ist. Sie läuft dem Markt hinterher.
- **Seit dem 11. Oktober läuft das Turnier:** Jede Woche treten die besten Anleitungen gegen echte, neue Kurswochen an. Das ist der einzige Test, der zählt. Erste Ergebnisse gibt es nach ein paar Wochen.

👉 Was wir bisher gelernt haben, in einfachen Worten: **[Versuche und Learnings](docs/VERSUCHE.md)**

## So verfolgst du das Projekt

| Wie | Was du bekommst |
|---|---|
| **Auf X: [@kryptofynn](https://x.com/kryptofynn)** | Die "Botupdates": was diese Woche getestet wurde und was rauskam. Am einfachsten. |
| **Hier vorbeischauen** | Diese Seite wird mit jedem Schritt aktualisiert. Ein Lesezeichen reicht. |
| **Mit GitHub-Konto: oben rechts auf "Watch" klicken** | Benachrichtigung per Mail, wenn sich etwas tut. |

## Selbst ausprobieren

Du willst sehen, wie die KI denkt? Hier ist eine Anleitung (ein "Prompt"), die du in ChatGPT oder Claude kopierst, zusammen mit Kursdaten eines Coins:

👉 **[Prompt zum Kopieren](prompts/ANALYST.md)**

Die KI sagt dir dann nicht "kaufen" oder "verkaufen", sondern: wie sie die Lage liest, wie viel sie investieren würde und **ab welchem Preis sie ihre Meinung ändert.** Wichtig: Auch dieser Prompt hat noch nicht bewiesen, dass er besser ist als Liegenlassen.

## Idee einbringen

Du hast eine Idee, wie die KI besser werden könnte? Ein Indikator, eine andere Anleitung, eine Datenquelle?

👉 **[Idee einreichen](../../issues/new?template=idee.yml)** (kostenloses GitHub-Konto nötig, ein kurzes Formular)

Jede Idee wird getestet, und das Ergebnis wird veröffentlicht, auch wenn sie nicht funktioniert. Wie das genau abläuft: [Mitmachen](CONTRIBUTING.md)

## Kleines Wörterbuch

| Begriff | Bedeutet |
|---|---|
| **Prompt** | Die Anleitung, die die KI bekommt. Wir testen, welche Anleitung am besten funktioniert. |
| **Liegenlassen** | Eine feste Menge investiert halten, ohne hin und her zu schieben. Unser Maßstab. |
| **Versuch** | Eine Anleitung oder Datenmenge wird auf 13 vergangenen Wochen getestet. Schnell, aber nur eine Vorauswahl. |
| **Turnier** | Die besten Anleitungen werden eingefroren und müssen sich Woche für Woche an der echten Zukunft beweisen. |
| **Kipp-Preis** | Der Preis, ab dem eine Einschätzung falsch ist. Jede Einschätzung hier hat einen. |

## Wer steckt dahinter?

Aaron ([@telaaron](https://github.com/telaaron)) baut das System, Fynn ([@kryptofynn](https://x.com/kryptofynn)) bringt die Trading-Praxis mit und teilt die Reise auf X. Die Forschungsarbeit läuft mit der KI Claude als Werkzeug.

---

<details>
<summary><b>Für Technik-Interessierte</b></summary>

- [Methode, Messung und Aufbau des Codes](docs/METHODE.md)
- [Alle Versuche als Tabelle, mit vollem Prompt und dem Denken der KI](versuche/UEBERSICHT.md)
- [Was als Nächstes getestet wird](versuche/backlog.md)
- [Turnier: Regeln und Runden](tournament/README.md)
- [Forschungsprotokoll mit allen Regeln](docs/PROTOKOLL.md)

</details>

*Keine Anlageberatung. Alle Zahlen sind Forschungsergebnisse auf kleinen Stichproben.*
