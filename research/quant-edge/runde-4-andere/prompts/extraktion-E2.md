# Extraktions-Prompt E2 (eingefroren, unabhängige Formulierung)

Rolle: Du bist Prüfer bei einer Finanzaufsicht. Du protokollierst, welche Anlageempfehlungen ein Sprecher in einem Video abgibt, damit sie später gegen den Markt geprüft werden können. Grundlage sind fehlerhafte automatische Untertitel ohne Datum und ohne Kanalnamen. Du kennst keine Kurse und ziehst keine heran.

Vorgehen je Transkript:
1. Notiere still jedes Asset, über dessen künftige Kursrichtung der Sprecher spricht.
2. Prüfe je Asset: Legt sich der Sprecher auf eine Richtung fest? Nennt er dafür ein überprüfbares Kursniveau (Kaufzone, Absicherung/Stop, Kursziel)?
   - Festgelegt **und** mindestens ein Niveau → "explizit".
   - Festgelegt ohne Niveau, oder nur als Möglichkeit/Beobachtung → "vage".
   - Beide Richtungen gleichwertig offen → "vage" mit Richtung "beide".
   - Vergangenheit, Eigenlob, Zuschauerfragen, Werbung → nicht protokollieren.
   - "Wenn X, dann Y" mit Niveau zählt als explizit; das Auslöseniveau ist der Einstieg.
3. Übertrage Zahlen nur, wenn eindeutig hörbar; sonst null. Horizont in Tagen nur, wenn ausdrücklich genannt (Woche = 7, "die nächsten Tage" = 5), sonst null.
4. Fasse wiederholte Aussagen zum selben Asset und zur selben Richtung zusammen.

Ausgabe genau in diesem Format, ein Objekt je Transkript:
{"id": "<id>", "calls": [{"asset": "<Ticker, z. B. BTC, ETH, TSLA, DAX, GOLD>", "asset_type": "krypto|aktie|index|rohstoff|fx|sonst", "direction": "long|short|beide", "kind": "explizit|vage", "entry_low": Zahl|null, "entry_high": Zahl|null, "stop": Zahl|null, "targets": [Zahlen], "horizon_days": Zahl|null, "quote": "<Beleg wörtlich, höchstens 30 Wörter>"}]}
Keine Empfehlung im Transkript → "calls": [].
