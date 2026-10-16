Du liest Dokumente, die öffentlich veröffentlicht wurden: Governance-Vorschläge von Krypto-Projekten oder Pflichtmeldungen (8-K) börsennotierter Firmen. Namen, Ticker, Daten, Links und Adressen sind durch Platzhalter wie [PROJECT], [TOKEN], [COMPANY], [DATE] ersetzt.

Aufgabe je Dokument: Beurteile allein aus dem Inhalt, ob das Beschriebene den wirtschaftlichen Wert für die Halter von [TOKEN] bzw. die Aktionäre von [COMPANY] in den nächsten Wochen eher erhöht oder senkt, verglichen mit ähnlichen Assets ohne diese Nachricht.

Regeln:
- Urteile nur über den Inhalt (Geldflüsse, Angebot, Gebühren, Rechte, Verwässerung, Kosten, Risiken, Verträge, Personal, Finanzierung), nicht über Tonfall oder Länge.
- Routine, Formalien, Abstimmungen ohne wirtschaftliche Wirkung, unklare Wirkung: 0.
- Versuche nicht herauszufinden, um welches Projekt, welche Firma oder welche Zeit es geht.
- Du siehst keine Kurse und sollst keine raten.

Antworte ausschließlich mit einer JSON-Liste, ein Objekt je Dokument, in der Reihenfolge der Eingabe:
[{"id": "<id>", "richtung": -1|0|1, "zuversicht": 1|2|3, "beleg": "<wörtliche Textstelle, max. 25 Wörter, die die Richtung trägt; leer bei 0>"}]
