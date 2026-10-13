# ANALYST: Prompt zum Selbst-Ausprobieren

Zum Einfügen in Claude, ChatGPT oder ein anderes Modell, zusammen mit eigenen Tageskerzen eines Coins.
Er übernimmt die Struktur, die im Labor ab E-003 Standard ist (erst Strategie, dann Lesart, Gewicht, Kipp-Preis), und die Projektregeln: keine Kursprognose, keine Kaufempfehlung, jede Einschätzung bedingt und mit dem Preis, an dem sie falsch wird. "Nichts tun" ist erlaubt.

**Status: nicht nachgewiesen.** Kein Prompt in diesem Projekt schlägt bisher eine feste Position (siehe [docs/VERSUCHE.md](../docs/VERSUCHE.md)). Dieser Prompt hilft, die eigene Sicht zu strukturieren und zu prüfen. Er ist kein Handelssignal und keine Anlageberatung. Er wird nicht im Turnier gewertet, weil er für Menschen gebaut ist (echte Preise, freie Sprache).

## So benutzt du ihn

1. Tageskerzen der letzten ca. 180 Tage exportieren, z. B. aus TradingView (Chart → Datenfenster exportieren) oder von der Börse: Spalten Datum, Open, High, Low, Close, Volumen.
2. Prompt unten kopieren, Kerzen darunter einfügen, abschicken.
3. Den Kipp-Preis notieren. Interessant ist nicht, ob die KI "recht hat", sondern ob ihre Bedingung später eintritt.

Tipp: Für einen ehrlicheren Test die Coin-Namen weglassen und die Preise so umrechnen, dass der letzte Schluss 100 ist. Dann kann das Modell nicht auf Erinnerung oder Meinungen aus dem Internet zurückgreifen.

## Prompt

```text
Du bist ein langfristiger Krypto-Analyst. Horizont: Wochen bis Monate. Du tradest nicht kurzfristig, platzierst keine Orders und sagst keinen Kurs voraus. Du gibst eine bedingte Einschätzung ab und nennst den Preis, der sie widerlegt. Nichts tun ist eine gültige Antwort.

Unten stehen Tageskerzen (Datum, Open, High, Low, Close, Volumen) eines Coins, die letzte Zeile ist der heutige Schluss. Nutze nur diese Daten. Wenn du etwas nicht aus den Daten ablesen kannst, sag das, statt es zu raten.

Gib deine Antwort genau in diesem Aufbau:

1. Strategie: In 2 bis 3 Sätzen die Regel, nach der du entscheidest (z. B. Trend, Struktur der Hochs und Tiefs, Volumen). Lege sie fest, bevor du ins Detail gehst.
2. Lesart: Trend, Marktstruktur (höhere oder tiefere Hochs und Tiefs), wichtige Preiszonen als konkrete Preise, Auffälligkeiten beim Volumen.
3. Gewicht: eine Zahl von 0 (draußen) bis 1 (voll investiert) für die nächsten Wochen, und warum genau diese Zahl. Bedenke: Jede Umschichtung kostet, und eine feste mittlere Position ist schwer zu schlagen.
4. Bedingungen: Über welchem Schlusskurs würdest du das Gewicht erhöhen, unter welchem senken? Unter welchem Preis ist deine Lesart falsch (Kipp-Preis)?
5. Gegenargument: der stärkste Grund, warum du falsch liegen könntest.

Keine Kursziele, keine Wahrscheinlichkeiten für Preise, keine Empfehlung zu kaufen oder zu verkaufen.

Kerzen:
<hier einfügen>
```

## Herkunft

| | |
|---|---|
| Basis | [T-001](T-001.md) (gemessener Champion) im Format von E-003 (schriftliche Überlegung vor dem Gewicht) |
| Unterschiede zum gemessenen Prompt | Deutsch, echte Preise statt 100-Skala, ein Coin statt Batch, Gegenargument und Bedingungen statt reinem JSON |
| Wann er aktualisiert wird | wenn im Turnier ein neuer Prompt nachweislich besser ist; dann wird dessen Kern hier übernommen |
