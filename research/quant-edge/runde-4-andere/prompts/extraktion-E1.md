# Extraktions-Prompt E1 (eingefroren)

Du bekommst automatisch erzeugte Untertitel (Transkripte) von deutschsprachigen Trading-Videos. Ohne Satzzeichen, mit Hörfehlern (z. B. "bitcoin" als "bit coin", Zahlen ausgeschrieben oder als Ziffern). Datum und Kanal sind entfernt. Du hast keine Kursdaten und sollst keine verwenden oder erraten.

Aufgabe: Finde jede Handelsaussage des Sprechers zu einem konkreten handelbaren Asset (Coin, Aktie, Index, Rohstoff, Währungspaar) und ordne sie ein.

- **explizit**: Asset + Richtung (long = steigt/kaufen, short = fällt/verkaufen/shorten) + mindestens ein konkretes Kursniveau als Einstieg, Stop oder Ziel, als Empfehlung, Erwartung oder eigene Position des Sprechers ("ich gehe hier long", "Ziel 72.000", "Stop unter 65.000", "Einstieg zwischen 3.100 und 3.200").
- **vage**: Asset + Richtung ohne konkretes Niveau, oder nur im Konjunktiv/als Beobachtung ("könnte drehen", "würde ich beobachten", "bullish", "wenn ... dann ...", ohne eigenes Niveau).
- Keine Aussage: reine Rückblicke ("letzte Woche sind wir gestiegen"), Erfolgsmeldungen früherer Calls, Werbung, Fragen von Zuschauern, Aussagen ohne Richtung.
- Bedingte Szenarien mit Niveau ("wenn wir über 70.000 schließen, dann Ziel 75.000") sind explizit, mit dem Bedingungsniveau als Einstieg.
- Nennt der Sprecher zwei gegensätzliche Szenarien für dasselbe Asset ohne Präferenz, ist das **vage** (Richtung "beide").
- Mehrere Ziele: alle in "targets", aufsteigend nach Abstand vom Einstieg.
- Zahlen: als Zahl im Kurs des Assets ("zweiundsiebzig tausend" → 72000; "drei eins" bei ETH im Kontext 3.100 → 3100). Unsicher → null, nicht raten.
- Horizont in Tagen, nur wenn genannt ("diese Woche" → 7, "kurzfristig" → null, "bis Jahresende" → null, "in den nächsten Tagen" → 5).

Gib pro Transkript ein Objekt aus:
{"id": "<id>", "calls": [{"asset": "BTC", "asset_type": "krypto|aktie|index|rohstoff|fx|sonst", "direction": "long|short|beide", "kind": "explizit|vage", "entry_low": Zahl|null, "entry_high": Zahl|null, "stop": Zahl|null, "targets": [Zahlen], "horizon_days": Zahl|null, "quote": "<wörtlicher Ausschnitt, max. 30 Wörter, der den Call belegt>"}]}
Asset als üblicher Ticker (BTC, ETH, SOL, TSLA, NVDA, DAX, NDX, SPX, GOLD, SILVER). Dasselbe Asset mit derselben Richtung mehrfach im Video: zu einem Call zusammenfassen (die konkreteste Fassung). Transkript ohne Aussage: "calls": [].
