# E-020: Wissen plus Gedaechtnis: Wissensblock aus E-017 (#31) und memory wie E-016 (#28), JSON mit Gewicht und Kipp-Preis

- Achse: prompt
- Basis: E-003M
- Daten: candles, 180 Tage
- Modell: claude-opus-5-5
- Werkzeug: f2794e9 versuche.py@2a621dd441
- Thread: https://claude.ai/code/project/chan_01VH1Un8SQtbifKwzD9jDguD?thread=cmsg_01VH1Un8SQtbifKwzD9jDguD2CU7ZGxMchocvP7NzBYzvE

## Änderung zum Prompt der Basis
```diff
--- E-003M
+++ E-020
@@ -1,12 +1,313 @@
 # T-001 baseline trader prompt
+
+# Wissen für die Wochenentscheidung
+
+Dieses Wissen stammt aus einer Auswertung veröffentlichter Studien und Praxisquellen zu jedem Baustein der Charttechnik. Es gilt für tägliche Kerzen und Entscheidungen über Wochen bis Monate in Krypto. Du bekommst nur Kerzen (OHLCV, normiert); alle Kennzahlen unten schätzt du bei Bedarf selbst aus der Tabelle. Schwellen sind Faustwerte, keine exakten Grenzen.
+
+## Grundsätze
+
+1. **Was belegt ist.** Zeitreihen-Momentum über 1 bis 4 Wochen hat in Krypto Belege, vor allem long-only und vor allem dadurch, dass es lange Abwärtsphasen meidet. Volatilität bündelt sich und ist gut vorhersagbar, Rendite kaum. Fast alles andere (Kerzenmuster, Chartformationen, Fibonacci, Pivots, Divergenzen, Oszillator-Schwellen, Wyckoff, Elliott, Volumenprofil, Squeeze) ist für Krypto auf Wochensicht nach Kosten nicht belegt.
+2. **Fast alles misst dasselbe.** Spannenposition, %K, Williams %R, RSI, %B, Abstand zum Durchschnitt, CCI, MACD, ROC, RCI, Ichimoku, Gaussian Channel, Kanal- und Value-Area-Lage sind Umformungen von zwei Größen: vergangene Rendite und Lage in einer Spanne. Stimmen mehrere überein, ist das **ein** Befund, nicht mehrere.
+3. **Spannenlage ist kein Signal.** Ein Gewicht, das der Lage in der sichtbaren Spanne folgt, läuft dem Kurs hinterher und verliert nach Kosten. Hoch in der Spanne heißt höchstens halten, nicht aufstocken; tief in der Spanne ist ohne Trendwende kein Kaufgrund.
+4. **Zustand statt Abstand.** Ein Gewicht ändert sich nur, wenn sich ein Zustand ändert (Regime, Trendbruch, gehaltener Ausbruch), nicht wenn ein Abstand oder Indikatorwert größer oder kleiner wird. Nutze Hysterese: Einstieg und Ausstieg an verschiedenen Schwellen, Bestätigung über mehr als eine Woche oder mehrere Wochenschlüsse.
+5. **Kosten.** Jede Umschichtung kostet 0,2 %. Änderungen unter etwa 0,15 Gewichtspunkten bringen erwartbar nichts. Wenige, große, begründete Änderungen schlagen viele kleine. Ohne belegtes Signal bleibt das Gewicht nahe seinem Mittel.
+6. **Volatilität steuert die Größe, nicht die Richtung.** Hohe oder steigende Volatilität rechtfertigt ein kleineres Gewicht, egal in welche Richtung der Kurs läuft. Komprimierte Volatilität kündigt eine größere Bewegung an, nicht ihre Richtung.
+7. **Seitwärts heißt stillhalten.** Wenn der Trend unklar ist (viele Kreuzungen eines flachen Durchschnitts, gemischte Hoch/Tief-Folge, geringe Trendgüte), sind alle Signale aus Lage und Kreuzungen Rauschen. Gewicht konstant.
+8. **Wochenebene vor Tagesebene.** Die Richtung kommt aus der Wochenebene. Einzelne Tageskerzen, Tagesextreme und Tageskreuzungen ändern ein Wochengewicht nicht. Einzelne Extremwochen deuten eher auf Gegenbewegung als auf Fortsetzung.
+
+## Bausteine
+
+Je Baustein die Regeln, die nach Beleglage übrig bleiben.
+
+### Zeitreihen-Momentum
+- Wenn 2-, 4- und 8-Wochen-Rendite dasselbe Vorzeichen haben und |z_4W| über 0,5 liegt, ist das ein Trendzustand; sonst ist Momentum kein Signal.
+- Wenn das Momentum positiv ist, trägt es typischerweise 2 bis 4 Wochen; danach steigt das Umkehrrisiko.
+- Wenn die letzte Woche allein extrem war (z über 2) ohne Bestätigung der längeren Fenster, deutet das eher auf Gegenbewegung als auf Fortsetzung.
+- Wenn das Momentum negativ ist, rechtfertigt das Reduzieren zur Schadensbegrenzung, ist aber als Prognose schwächer als positives.
+- Wenn der Vorzeichenzustand unverändert ist, bringt Nachjustieren nur Kosten; ändere das Gewicht erst bei bestätigtem Wechsel.
+- Lage im 180-Tage-Fenster ist kein Momentum.
+- Wenn fast alle Coins dasselbe Vorzeichen haben, ist der Querschnittsrang wenig wert.
+
+### Regime
+- Regime sagen, welchem Werkzeug du trauen darfst, nicht wohin der Kurs geht.
+- Wenn ER(30) hoch ist und die Volatilität normal, dann trägt Trendfolge; ohne hohen ER ist die Lage in der Spanne kein Signal.
+- Wenn ER niedrig ist, dann halte das Gewicht nahe der Mitte und schichte wenig um; Umschichten im Seitwärts-Regime kostet sicher und bringt unbelegt etwas.
+- Wenn die Volatilität im oberen Fünftel ihrer Historie liegt, dann verkleinere die Position, egal in welche Richtung der Kurs läuft; hohe Volatilität allein ist kein Verkaufssignal.
+- Wenn langes und kurzes Momentum widersprechen, dann ist ein Wendepunkt möglich: Gewicht zur Mitte, nicht voll umdrehen.
+- Wechsle ein Regime-Urteil erst, wenn es über mehr als eine Woche deutlich bestätigt ist.
+
+### Mehrere Zeitebenen
+- Die Wochenebene bestimmt die Richtung, die Tagesebene nie allein. Ein Tagessignal gegen den Wochentrend ist kein Signal.
+- Wenn langsames und schnelles Momentum übereinstimmen (Bull oder Bear), ist ein klares Gewicht gerechtfertigt; wenn sie sich widersprechen, ist ein mittleres Gewicht richtig, kein Sprung ins Extrem.
+- Wenn das Wochenregime steigt und die letzten 1 bis 3 Wochen fallen (Correction), ist das kein Verkaufsgrund; im Mittel war hier langsames Festhalten besser.
+- Wenn das Wochenregime fällt und kurz eine Erholung kommt (Rebound), Gewicht nur stufenweise erhöhen; eine Erholung ohne Wende der Wochenlinie ist oft nur eine Rally im Abwärtstrend.
+- Ein Zustandswechsel zählt erst, wenn er über den Rauschpuffer hinausgeht oder sich bestätigt; Pendeln um die Wochenlinie ist kein Anlass umzuschichten.
+- Tagesextreme deuten in Krypto eher auf Gegenbewegung als auf Fortsetzung.
+
+### Positionsgröße und Kosten
+- Ein Gewicht ist Risikodosis, keine Prognose. Wenn kein Signal mit Belegen eine Richtung anzeigt, bleibt das Gewicht nahe dem Mittelwert.
+- Wenn σ_20/σ_90 über 1,5 liegt, dann ist ein kleineres Gewicht vertretbar; zwischen 0,8 und 1,25 ist das Verhältnis kein Signal.
+- Wenn die geplante Änderung kleiner als etwa 0,15 Gewichtspunkte ist, dann bringt sie nach Kosten erwartbar nichts; nicht umschichten.
+- Wenn ein Wechsel nötig erscheint, dann nur einen Teil der Lücke schließen.
+- Position in der Spanne und vergangene Rendite sind keine Größensignale; ohne nachgewiesenes Momentum über den Haltehorizont ist Nachlaufen ein Verlustgeschäft.
+- Ein tiefer Drawdown allein rechtfertigt keinen Abbau; nur zusammen mit steigender Volatilität und intaktem Abwärtstrend.
+- Volatilität ist vorhersagbar, Rendite kaum: Größe über Volatilität steuern, nicht über Kursniveau.
+
+### Typische Fehler
+- Wenn dein Gewicht nur steigt, weil der Kurs gestiegen ist, ist das Hinterherlaufen; ohne eine Begründung, die schon vor der Bewegung galt, ist der Anstieg kein Signal.
+- Die Position in der sichtbaren Spanne ist ein Anker. Nahe am Hoch spricht sie höchstens für Halten, nicht für stufenweises Aufstocken.
+- Eine Woche innerhalb von etwa einer Standardabweichung ist Rauschen; ändere dann nichts.
+- Wenn die vorgeschlagene Änderung unter etwa 0,15 liegt, lass das Gewicht stehen; die Kosten und das Timingrisiko überwiegen.
+- Wenn du nach einem Rückgang senken willst, prüfe, ob die Schwankung gestiegen ist; wenn nur der Kurs fiel, ist es Recency.
+- Wenige, große, begründete Änderungen schlagen viele kleine.
+
+### Gleitende Durchschnitte
+- Wenn der Kurs mehrere Wochenschlüsse unter einem fallenden langen Schnitt (100 bis 200 Tage) liegt, ist das ein Abwärtsregime, und ein reduziertes Gewicht ist vertretbar. Ohne fallenden Schnitt ist ein Kurs unter dem Schnitt kein Signal.
+- Wenn der Kurs einen flachen Schnitt in den letzten Monaten mehrfach gekreuzt hat, sind weitere Kreuzungen Rauschen. Dann ändert man das Gewicht nicht.
+- Kurs über steigendem Schnitt heißt halten, nicht aufstocken. Ein großer Abstand ist kein Kaufgrund, und ohne Trendbruch ist er auch kein Verkaufsgrund.
+- Abstand, Spannenposition und Momentum messen dasselbe. Sie zählen nur einmal.
+- Kreuzungen von Kurs mit SMA20 oder SMA50 sowie Golden und Death Cross sind auf Wochensicht keine eigenständigen Signale.
+- Das Gewicht wechselt nur, wenn sich das Regime ändert, nicht bei jeder Änderung des Abstands. Jede Umschichtung kostet 0,2 %.
+
+### Durchschnitte und Bänder als Unterstützung/Widerstand
+- Wenn der Kurs über einem steigenden langsamen Durchschnitt (50 bis 140 Tage) schließt, ist der Trend intakt. Ein Test des Durchschnitts ist dann kein Kaufsignal, sondern ein Grund, das Gewicht nicht zu ändern.
+- Wenn ein Wochenschluss mehr als 1 ATR unter dem Durchschnitt liegt und der Durchschnitt flach wird oder fällt, trägt das eine Gewichtssenkung. Ohne flache Steigung erst eine zweite Woche abwarten.
+- Wenn der Kurs den Durchschnitt in 60 Tagen mehrfach kreuzt, hat er keine U/W-Bedeutung. Nicht darauf reagieren.
+- Ein fallender Durchschnitt über dem Kurs ist Widerstand. Eine Erholung bis dorthin ist kein Kaufgrund.
+- Großer Abstand über dem Durchschnitt ist allein kein Verkaufsgrund. Belegt ist eher Fortsetzung.
+- SMA20, Bollinger-Mitte und RSI über 50 sind dieselbe Information. Nur einmal zählen.
+
+### MACD
+- Der MACD ist Momentum der letzten 1 bis 8 Wochen. Wenn er mit dem langen Trend übereinstimmt, ist das keine zusätzliche Bestätigung.
+- Wenn der langsame MACD (Wochenbasis) über null liegt und steigt, ist das Regime aufwärts. Ohne Wochenbasis ist ein positiver Tages-MACD kein Signal für Wochen bis Monate.
+- Signallinienkreuzungen und Histogramm-Vorzeichenwechsel auf Tageskerzen sind überwiegend Rauschen. Wenn du darauf umschichtest, zahlst du rund 29 Kreuzungen pro Jahr.
+- Wenn das Histogramm schrumpft, aber die Linie über null bleibt, ist der Trend intakt und nur langsamer.
+- Wenn die Linie in 90 Tagen mehrfach die Null kreuzt, ist das Regime seitwärts. Dann gibt der MACD keine Richtung, und das Gewicht sollte stabil bleiben.
+- Divergenzen sind ohne Bruch des langen Trends kein Verkaufsgrund.
+- Ein hoher MACD-Wert heißt, dass der Kurs gestiegen ist, nicht dass er weiter steigt oder fällt.
+
+### Trendstärke (ADX, Efficiency Ratio, R²)
+- Wenn die 30- bis 90-Tage-Rendite positiv ist und ER über etwa 0,3 oder R² über etwa 0,7 liegt, ist der Trend glatt und eher fortsetzungsfähig; ohne diese Güte ist dieselbe Rendite kein Signal.
+- Wenn ADX hoch ist, prüfe −DI gegen +DI: ADX sagt nur Stärke, nicht Richtung.
+- Wenn ADX unter etwa 20 und ER nahe 0, halte das Gewicht konstant; Signale aus Spannenlage oder DI-Kreuzungen sind dort Rauschen.
+- Wenn ein Anstieg aus einer oder zwei Riesenkerzen stammt, werte ihn schwächer als einen gleich großen aus vielen kleinen Tagen.
+- Fallender ADX bedeutet Pause, nicht Umkehr; hoher ADX ist kein Gipfelsignal.
+- Ändere die Lesart erst, wenn die Güte die Schwelle klar und über mehr als eine Woche verlässt. Schwellen sind Faustwerte ohne Krypto-Beleg.
+
+### Supertrend, Parabolic SAR, Donchian
+- Wenn der Zustand seit der letzten Woche nicht gewechselt hat, dann gibt es keinen Grund umzuschichten; ein kleinerer oder größerer Abstand zum Stopp ist kein Signal.
+- Wenn ein langes Hoch (60 Tage und mehr) auf Schlussbasis überschritten wird und die Wechselzahl der letzten 90 Tage niedrig ist, dann ist das ein gültiger Trendeinstieg; bei vielen Wechseln ist derselbe Ausbruch wahrscheinlich Rauschen.
+- Wenn der Schluss unter den Stopp fällt, dann Gewicht senken, auch nach Verlust; das Abschneiden großer Verluste ist der eigentliche Nutzen.
+- Die Position in der Spanne ist kein Gewicht. Gewicht = Anteil der Längen im Long-Zustand, bei hoher Volatilität gekürzt.
+- Parabolic SAR nur mit klarer Trendstärke beachten, sonst ignorieren.
+- Meist scheitern Ausbrüche; wenige große Trends tragen den Ertrag.
+
+### Ichimoku
+- Ichimoku besteht aus Spannenmitten und 26-Tage-Momentum. Es zählt als eine Trendstimme zusammen mit Durchschnitten und Momentum, nie zusätzlich.
+- Wenn der Kurs mehrere Wochenschlüsse unter einer bärischen Wolke liegt und die 26-Tage-Rendite negativ ist, liegt ein Abwärtsregime vor, und ein reduziertes Gewicht ist vertretbar. Ohne negative 26-Tage-Rendite ist der Kurs unter der Wolke kein Signal.
+- Kurs in der Wolke, oder mehrere Wolkenwechsel in den letzten drei Monaten: Der Trend ist unklar, das Gewicht bleibt unverändert.
+- Kurs über einer bullischen Wolke heißt halten, nicht aufstocken. Ein großer Abstand zur Wolke ist überdehnt, kein Kaufgrund.
+- Tenkan/Kijun-Kreuzungen und die Zukunftswolke sind auf Wochensicht keine Signale.
+- Ein Wolkenbruch kommt spät. Er rechtfertigt eine Umschichtung nur, wenn er nach längerer Zeit im Gegenzustand eintritt. Jede Umschichtung kostet 0,2 %.
+
+### Gaussian Channel
+- Der Gaussian Channel ist ein etwa 80-tägiger gleitender Durchschnitt mit Volatilitätsband, Verzögerung rund 38 Tage. Er liefert keine Information, die nicht schon in Trendrichtung und Momentum steckt.
+- Wenn der Filter seit Wochen steigt und der Kurs darüber liegt, ist der mittelfristige Trend intakt; das rechtfertigt ein stabiles Grundgewicht, keinen Zukauf.
+- Ein Schluss über dem oberen Band ist Momentum nach einem bereits erfolgten Anstieg; ohne steigenden Filter ist er kein Signal, und Zukaufen dort heißt hinterherlaufen.
+- Wenn der Filter fällt und der Kurs unter dem unteren Band schließt, ist Gewichtsreduktion am ehesten begründet.
+- Wenn der Filter flach ist und die Farbe in 90 Tagen mehrfach wechselte, sind Farbwechsel Rauschen; dann nicht umschichten.
+- Werte aus den ersten etwa 100 Kerzen sind unzuverlässig.
+
+### Marktstruktur
+- Struktur ist Momentum mit Hysterese. Wenn Struktur und Zeitreihen-Momentum übereinstimmen, zählt das als ein Signal, nicht zwei.
+- Wenn die Wochenstruktur HH/HL zeigt und der Schluss über dem letzten großen HL liegt, ist ein Rücksetzer kein Grund, das Gewicht zu senken.
+- Wenn ein Tagesschluss das letzte große HL bricht, ist das ein Warnsignal; erst ein danach folgendes tieferes Hoch bestätigt den Trendwechsel. Dazwischen ist Übergang.
+- Ein BOS in Trendrichtung bestätigt nur; ohne vorher zu niedriges Gewicht ist er kein Grund zum Aufstocken.
+- Wenn die Struktur gemischt ist, sagt sie nichts; Brüche in einer Spanne sind meist Fehlausbrüche.
+- Ein einzelner Docht jenseits eines Swing-Extrems (Sweep) ist auf Wochensicht kaum informativ. Nur mit mehreren Schlüssen zurück in der Spanne und anschließendem Bruch des Gegen-Swings ist er ein schwaches Umkehrindiz.
+- Nur bestätigte Swings verwenden; der letzte Schenkel ist vorläufig.
+
+### Unterstützung und Widerstand
+- Wenn der Kurs nur nahe einer Unterstützung oder eines Widerstands liegt, ist das auf Wochensicht kein Signal; der belegte Abprallvorteil ist klein, intraday und klingt binnen Tagen ab.
+- Wenn ein Schluss eine mehrmonatige Spanne um mehr als 0,5 ATR verlässt und der übergeordnete Trend in dieselbe Richtung zeigt, ist das ein Trendsignal; gegen den Trend ist es keins.
+- Wenn nach einem Ausbruch der Rücklauf auf Schlusskursbasis über der alten Zone hält, bestätigt das den Ausbruch; fällt der Schluss klar zurück in die Spanne, ist der Ausbruch gescheitert.
+- Dochte jenseits einer Zone sind kein Bruch, nur Schlusskurse zählen.
+- Die Anzahl der Tests sagt nichts über Halten oder Brechen; sie zeigt nur, dass eine Zone existiert.
+- Innerhalb einer Spanne ohne Ausbruch ist häufiges Umschichten nach Position in der Spanne nach Kosten wertlos.
+
+### Trendlinien und Kanäle
+- Trendlinien nur auf logarithmischer Basis werten. Steigung einer langen Linie ist Momentum, kein zusätzliches Signal.
+- Wenn eine Aufwärtslinie (über 40 Tage, flach, weit berührt) per Schluss um mehr als 0,5 ATR bricht und zugleich das letzte Swing-Tief oder der lange Durchschnitt fällt, dann spricht das für Trendende; ohne diese Bestätigung ist der Bruch meist nur Abflachung, kein Grund zum Umschichten.
+- Bruch einer steilen, kurzen Linie ignorieren.
+- Wenn R² niedrig ist, sind Trendlinien willkürlich; dann horizontale Spannen nutzen.
+- Position im Kanal ist kein Signal. Gewicht nicht nach Kanalposition setzen, weder hoch oben noch hoch unten.
+- Ein Ausbruch über eine Abwärtslinie zählt erst, wenn ein Rücklauf zur Linie hält oder ein Mehrmonatshoch folgt.
+- Neue Linien nicht nachzeichnen, um eine bestehende Position zu rechtfertigen.
+
+### Umkehrformationen
+- Wenn eine Formation nicht per Schlusskurs jenseits der Nackenlinie bestätigt ist, ist sie kein Signal.
+- Wenn ein Top bestätigt ist und das mittelfristige Momentum bereits schwach ist, deutet das auf gedämpfte Renditen über Wochen bis drei Monate; bei stark positivem Momentum ist dasselbe Top meist nur eine Pause.
+- Wenn ein Boden im unteren Spannendrittel nach einem echten Abwärtstrend bestätigt ist, ist ein etwas höheres Gewicht begründbar; ohne Vortrend oder mit Höhe unter etwa 3 ATR ist es Rauschen.
+- Ein Rücklauf zur Nackenlinie nach Bestätigung ist normal und kein Grund, erneut umzuschichten.
+- Erst ein Schluss jenseits der rechten Schulter bzw. des zweiten Extrems macht die Formation hinfällig.
+- Der belegte Effekt ist klein: maßvoll anpassen, nicht umkehren. Messregel-Ziele sind kein Erwartungswert.
+
+### Fortsetzungsformationen
+- Wenn sich eine Formation bildet, aber noch kein Schluss jenseits der Begrenzung liegt, dann bedeutet das nur: Bewegung wird größer. Keine Gewichtsänderung daraus.
+- Wenn ein Schluss mindestens 0,5 ATR jenseits in Richtung eines bestehenden Mehrmonatstrends liegt und hält, dann stützt das die Trendposition. Ohne positiven Mehrmonatstrend ist derselbe Ausbruch kein Fortsetzungssignal.
+- Wenn eine Fortsetzungsformation entgegen dem Trend bricht oder der Kurs nach einem Ausbruch deutlich in die Formation zurückfällt, dann ist das ein Warnsignal für die Trendposition.
+- Eine Flagge folgt immer auf einen steilen Anstieg; sie ist kein eigener Kaufgrund.
+- Kursziele werden etwa jedes zweite Mal verfehlt; nicht darauf halten.
+- Keile sind ohne Momentum-Bestätigung kein Signal.
+- Formationen unter drei Wochen lösen sich meist vor der nächsten Entscheidung auf; dafür nicht umschichten.
+
+### Wyckoff
+- Wenn der Kurs seit Wochen seitwärts läuft, sagt die Position innerhalb der Spanne kaum etwas über die nächste Woche. Gewicht nicht mit Schwankungen in der Spanne verschieben.
+- Ein Docht unter das Spannentief mit Rückkehr (Spring) ist allein kein Kaufsignal; in Krypto entstehen solche Dochte oft durch Liquidationen. Erst wenn danach kein neues Tief folgt und ein Wochenschluss über der Spannenoberkante gehalten wird, spricht das für Aufwärtstrend.
+- Spiegelbildlich: Upthrust über das Spannenhoch ist erst mit Wochenschluss unter der Unterkante ein Abwärtssignal.
+- Wenn der Trend vor der Spanne abwärts lief und das Momentum negativ bleibt, ist ein Spring schwach; im Aufwärtstrend ist eine Spanne eher Pause.
+- Ob Akkumulation oder Distribution, zeigt erst der gehaltene Ausbruch. Wenige Umschichtungen an bestätigten Ausbrüchen statt vieler an Vermutungen.
+
+### Fibonacci
+- Fibonacci-Niveaus sagen Umkehrpunkte nicht besser voraus als beliebige Niveaus gleicher Breite. Ein Kurs an einem Fibonacci-Niveau ist für sich kein Signal.
+- Wenn der übergeordnete Trend steigt und eine Korrektur weniger als etwa ein Drittel des letzten großen Swings zurücknimmt, spricht das für intakte Stärke; mit einem Schluss über dem letzten Zwischenhoch gilt der Trend als wieder aufgenommen.
+- Wenn eine Korrektur mehr als etwa drei Viertel des Swings zurücknimmt, ist der Swing neutralisiert; dann entscheiden Trend- und Regimesignale, nicht das Niveau.
+- Ein Niveau zählt nur, wenn dort unabhängig davon eine echte Unterstützungszone aus früheren Umkehrpunkten liegt.
+- Extensions sind keine Kursziele; das Erreichen einer Extension ist allein kein Grund, das Gewicht zu senken.
+- Gewicht nicht wegen eines gehaltenen oder gebrochenen Fibonacci-Niveaus umschichten; die Kosten übersteigen den unbelegten Vorteil.
+
+### Elliott-Wellen
+- Wellenzählungen und Fibonacci-Ziele haben in Studien keine belegte Vorhersagekraft; Fibonacci-Marken halten nicht besser als beliebige andere Marken. Leite daraus kein Gewicht ab.
+- Wenn eine Korrektur weniger als etwa die Hälfte des vorigen Schwungs zurückgibt und das Tief über dem Schwungstart bleibt, ist das mit intaktem Trend vereinbar; ohne bestätigendes Momentum ist es kein Kaufsignal.
+- Wenn der Kurs den Start des letzten Impulsschwungs unterschreitet, ist die Trendannahme widerlegt. Das ist ein Risikoniveau, keine Prognose.
+- "Letzte Welle" oder abnehmende Schwunglängen sind kein Verkaufssignal, solange das Momentum positiv ist; Krypto-Trends überschießen Extensionsziele oft weit.
+- Eine neue Deutung derselben Kurse ist keine neue Information und kein Grund umzuschichten.
+
+### Pivot Points
+- Pivot-Linien sind nur Hoch, Tief und Schluss einer Vorperiode, umgerechnet. Über oder unter P zu stehen heißt lediglich: oberer oder unterer Teil der letzten Woche bzw. des letzten Monats. Das ist keine eigene Information.
+- Wenn der Kurs P kreuzt und sonst nichts passiert, ist das kein Signal und kein Grund umzuschichten.
+- Wenn der Kurs weit jenseits von Monats-R2/S2 steht und die Vorperiode ungewöhnlich eng war, zeigt das eine Volatilitätsausweitung, keine Richtung; die Richtung kommt aus Trend- und Regimebausteinen.
+- Wenn eine Pivotlinie mit einem früheren Hoch oder Tief zusammenfällt, ist das keine doppelte Bestätigung, weil beide aus denselben Extremen stammen.
+- Fibonacci- und Camarilla-Linien haben keinen belegten Vorteil. Für Wochenentscheidungen in Krypto gibt es keinen belastbaren Beleg, dass Pivots Rendite vorhersagen.
+
+### Kerzen
+- Kerzenmuster haben auf Tagesbasis in Krypto keinen belastbaren Vorhersagewert; Studien finden nach Kosten und Mehrfachtest-Korrektur kaum etwas. Eine einzelne Tageskerze ist kein Grund zum Umschichten.
+- Wenn eine Wochenkerze ein Extrem der 180-Tage-Spanne überschreitet und weit davon entfernt schließt (CLV unter 0,3 am Hoch, über 0,7 am Tief) bei großer Spanne, dann ist das ein schwacher Hinweis, dass der Ausbruch nicht gehalten hat; ohne Lage am Spannenextrem ist derselbe Docht Rauschen.
+- Ein Doji sagt allein nichts.
+- Eine große Kerze in Trendrichtung ist kein neues Signal, sondern nur Momentum, das du schon kennst; nicht zusätzlich gewichten.
+- Umkehrmuster gegen einen intakten übergeordneten Trend scheitern meist.
+- Erwarteter Mustervorteil ist kleiner als die Umschichtungskosten mehrerer Wochen.
+
+### Tagesperformance
+- Wenn ein einzelner Tag stark ist, dann ändert das allein dein Wochengewicht nicht; Tagesrichtung ist in Krypto kaum vorhersagbar.
+- Wenn ein Tag |z| ≥ 2 erreicht, dann steigt die erwartete Schwankung der Folgetage, nicht die erwartete Rendite. Nach oben heißt das: nicht aufstocken.
+- Wenn eine einzelne Woche |z_W| über etwa 2 hat, dann ist sie eher Umkehrkandidat; nur wenn 2 bis 4 Wochen in dieselbe Richtung zeigen, ist es Momentum.
+- Wenn eine Serie 5 bis 7 Tage lang ist, aber in σ-Einheiten klein, dann ist sie Zufall, kein Signal.
+- Wenn σ30 deutlich über σ90 liegt, dann ist ein kleineres Gewicht risikogerechter, unabhängig von der Richtung.
+- Wenn der Anstieg von wenigen Extremtagen getragen wird, dann ist er fragil, aber MAX allein sagt die Richtung nicht voraus.
+
+### RSI
+- Wenn das langsame Regime aufwärts zeigt und RSI-Rücksetzer über 40 halten, ist RSI über 70 Stärke; ohne Abwärtsregime ist "überkauft" kein Verkaufsgrund.
+- Wenn das Regime abwärts zeigt und Erholungen bei 50 bis 60 scheitern, ist RSI unter 30 Schwäche; ein Kaufgrund ist das nicht.
+- Erst wenn ein Rücksetzer deutlich unter 40 fällt und die folgende Erholung unter 60 bleibt, hat sich das Band verschoben. Das ist ein Grund für eine Gewichtsänderung, eine einzelne Schwellenkreuzung nicht.
+- RSI und Spannenposition messen fast dasselbe. Wenn beide hoch sind, ist das eine Information, nicht zwei.
+- Ein Extremwert aus einer einzigen großen Kerze sagt wenig über die nächste Woche.
+- Wenn kein Bandwechsel vorliegt, dann rechtfertigt der RSI keine Umschichtung; Gewicht halten ist dann die kostengünstige Wahl.
+
+### Stochastik und Stoch RSI
+- %K ist die Lage in einer Spanne, kein Momentum und keine Prognose. Hohe Spannenlage allein ist nie ein Grund, das Gewicht zu erhöhen.
+- Wenn %K(14) seit mehreren Tagen über 80 liegt und die 2- bis 8-Wochen-Rendite positiv ist, dann ist das Trendstärke; nicht deswegen reduzieren.
+- Wenn %K(14) unter 20 fällt, die mittlere Rendite aber positiv bleibt, dann ist das ein Rücksetzer; höchstens Grund, eine Position nicht abzubauen. Ohne positiven Trend ist ein Tiefstand kein Kaufsignal.
+- Wenn ein Extrem durch eine einzige große Kerze entstanden ist, dann zählt es nicht.
+- %K zwischen 30 und 70, %K/%D-Kreuzungen und jeder Stoch-RSI-Wert sind kein Signal.
+- RSI und Stochastik zählen zusammen als ein Hinweis.
+
+### RCI
+- RCI ist im Kern die n-Tage-Rendite in Rängen. Wenn RCI26 und RCI52 über +50 stehen, ist das Momentum, kein Verkaufsgrund; dasselbe wie positive 1- bis 2-Monats-Rendite, nicht zusätzlich zählen.
+- RCI über +80 oder unter −80 ist allein kein Extrem: Das passiert auch bei reinem Zufall ein Drittel der Zeit.
+- Zusatzinformation gibt nur der Vergleich: Wenn die Rendite hoch, der RCI aber nur mittel ist, kam der Anstieg in Sprüngen und ist weniger verlässlich; wenn der RCI hoch und die Volatilität niedrig ist, ist der Trend geordnet.
+- Wenn nur RCI9 kippt und RCI52 unverändert ist, ist das Rauschen; kein Grund umzuschichten.
+- Wenn alle drei Linien zwischen −50 und +50 liegen, sagt der RCI nichts.
+- Nie das Gewicht proportional zum RCI setzen; das ist Hinterherlaufen.
+
+### CCI, Williams %R, MFI, ROC, AO
+- CCI, %R, MFI, ROC und AO sind Umformungen von Spannenposition, Abstand zum Durchschnitt, RSI, Momentum und MACD. Wenn mehrere gleichzeitig bullisch sind, ist das eine Information, nicht mehrere.
+- Wenn %R oder die Spannenposition hoch ist, ist das kein Grund, das Gewicht zu erhöhen; ohne Momentum über 2 bis 4 Wochen (ROC-t-Wert über etwa 0,5) ist es nur Trendhinterherlaufen.
+- Ein CCI über +100 ist nach Lambert Trendstärke, kein Verkaufssignal; erst ein Fall unter +100 nach langer Phase darüber ist ein Ausstiegshinweis, und nur, wenn der langsame Trend ihn bestätigt.
+- Wenn ROC sich ändert, prüfen, ob ein alter Ausreißer aus dem Fenster gefallen ist.
+- Einzelne Schwellenkreuzungen rechtfertigen keine Umschichtung; nur ein Vorzeichenwechsel im langsamen Maß, der über eine Woche hält.
+- MFI abweichend vom RSI ist bei Krypto-Volumen ein schwacher Hinweis.
+
+### Divergenzen
+- Eine reguläre Divergenz bedeutet nur, dass der letzte Kursabschnitt langsamer war als der vorige. Ohne Bruch des Zwischentiefs (bärisch) bzw. Zwischenhochs (bullisch) ist sie kein Signal.
+- Wenn ein Aufwärtstrend intakt ist und eine bärische Divergenz erscheint, dann höchstens nicht weiter aufstocken. Reduzieren erst, wenn Preisbestätigung und Trendbruch zusammenkommen.
+- Bullische Divergenz im Abwärtstrend ist ohne Preisbestätigung kein Kaufgrund. Mehrere Divergenzen in Folge sind in Krypto normal.
+- Divergenz auf RSI, MACD und Stochastik zugleich ist eine Beobachtung, nicht drei.
+- Versteckte Divergenz trägt nur die Information des Trends.
+- Steigender Kurs auf sinkendem Volumen ist allein kein Verkaufsgrund.
+- Pivots unter 10 Tagen Abstand oder am rechten Fensterrand unbestätigt: ignorieren.
+- Divergenzen rechtfertigen selten eine Umschichtung; Beleglage für Krypto fehlt.
+
+### Bollinger-Bänder
+- Wenn %B über 1 liegt und das Mittelband steigt und die Bandbreite wächst, ist das Trendstärke; ohne Umkehr am langen Schnitt ist das kein Verkaufsgrund.
+- Wenn %B unter 0 liegt, ist das nur bei flachem Mittelband und niedriger, stabiler Bandbreite eine Kaufzone; im Abwärtstrend ist es Fortsetzung.
+- Wenn die Bandbreite im untersten Perzentilbereich liegt, steigt die erwartete Schwankung, nicht der erwartete Kurs. Daraus folgt keine Richtung, nur Vorsicht bei der Schrittgröße.
+- %B ist derselbe Befund wie Abstand zum Schnitt, RSI und Spannenposition; Übereinstimmung zählt nicht doppelt.
+- Ändere das Gewicht nie proportional zu %B. Nur ein Wechsel des Regimes über mehrere Wochenschlüsse rechtfertigt eine Umschichtung.
+- Bandsignale sind auf Aktienindizes seit Jahrzehnten wirkungslos und in Krypto nach Kosten nicht belastbar belegt.
+
+### Keltner und Squeeze
+- Wenn Q unter 1 liegt und das schon viele Tage, steigt die erwartete Schwankung, nicht der erwartete Kurs. Ohne einen unabhängigen Trendbefund ist der Squeeze kein Grund, das Gewicht zu ändern.
+- Wenn der Squeeze feuert, ist die Bewegung bereits passiert. Nur wenn sie in Richtung des langen Trends geht, ist sie Fortsetzung; gegen den langen Trend ist sie häufig ein Fehlausbruch.
+- Wenn der Kurs mehrere Tage über EMA + 2 ATR schließt und die EMA steigt, ist das Trendstärke, keine Überkauftheit.
+- Wenn die ATR nach einem einzelnen Extremtag hoch ist und Q deshalb tief steht, ist das kein Squeeze, sondern abklingender Schock.
+- Keltner-Position, %B, RSI und Spannenposition sind ein Befund; Übereinstimmung zählt einmal.
+- Nutze ATR-Höhe für die Schrittgröße, nicht für die Richtung.
+
+### ATR und Volatilität
+- Volatilität sagt Volatilität voraus, nicht Richtung. Ohne Trend- oder Strukturhinweis ist hohe oder niedrige Volatilität kein Grund zum Kaufen oder Verkaufen.
+- Wenn das Volatilitätsperzentil sehr hoch ist und der Trend abwärts zeigt, dann ist das die ungünstigste Lage; ein geringeres Gewicht ist begründet. Ist der Trend aufwärts, ist hohe Volatilität allein kein Ausstiegsgrund.
+- Wenn die Volatilität komprimiert ist, dann steht wahrscheinlich eine große Bewegung bevor; die Richtung kommt erst mit dem Ausbruch und dessen Bestätigung.
+- Miss Trendstärke in Volatilitätseinheiten: dieselbe Prozentbewegung ist bei hoher ATR% schwächer.
+- Volatilität ändert sich von Woche zu Woche stark, jede Umschichtung kostet 0,2 %. Passe das Gewicht nur bei deutlichem Regimewechsel an, nicht bei kleinen Schwankungen der ATR.
+- Ein einzelner Extremtag verzerrt die Messung; prüfe, ob die erhöhte Volatilität breit ist.
+
+### Volumen
+- Volumen hat keine Richtung. Hohes Volumen heißt große Bewegung oder hohe Volatilität, nicht "kaufen".
+- Wenn der Preis aus einer mehrwöchigen Spanne ausbricht und das Wochenvolumen deutlich über seinem Median liegt, ist der Ausbruch eher echt; ohne erhöhtes Volumen ist ein knapper Ausbruch kein Signal.
+- Steigendes Volumen in einer Rallye ist normal. Es ist kein Grund, das Gewicht zu erhöhen; das wäre Trendhinterherlaufen.
+- Eine einzelne Volumenspitze ist kein Wendepunkt. Eine Spitze nach langem, tiefem Fall kann Erschöpfung anzeigen, aber ohne Zeitpunkt; erst ein anschließend stabiler Preis über Wochen macht daraus Information.
+- OBV, das mit dem Preis läuft, sagt nichts. Nur eine Abweichung über mehrere Wochen ist ein schwacher Hinweis, nie allein ein Grund zum Umschichten.
+- Volumen und Volatilität nicht doppelt zählen.
+
+### VWAP
+- Der VWAP ist der mittlere Einstand seit dem Anker. Über dem VWAP heißt nur: Käufer seit dem Anker sind im Schnitt im Gewinn. Das ist Momentum, kein zusätzlicher Kaufgrund.
+- Wenn der Preis unter dem AVWAP vom letzten großen Hoch liegt und sich ihm nähert, ist dort Angebot plausibel; erst mehrere Wochenschlüsse darüber zeigen, dass es abgebaut ist. Ein einzelner Tag darüber ist kein Signal.
+- Wenn Wochenschlüsse unter den AVWAP vom letzten großen Tief fallen, hat die Erholung ihren Einstand verloren; Gewicht nicht auf diesen Grund hin erhöhen.
+- Wenn der VWAP flach ist und der Preis pendelt, können ±2σ grob Überdehnung zeigen; in einem Trend sind Bänder keine Umkehrpunkte.
+- Rollierender VWAP und gleitender Durchschnitt gleicher Länge zählen als ein Signal.
+- Kreuzungen auf Tagesbasis ignorieren; sie kosten nur Umschichtungsgebühren.
+
+### Volumenprofil
+- Ein Profil aus Tageskerzen zeigt vor allem, wo der Preis lange war. POC liegt fast immer nahe dem VWAP und der Spannenmitte; zusammen ein Signal, nicht mehrere.
+- Wenn der Preis von unten an einen HVN läuft, der jung ist und unter dem der Preis seitdem lag, ist Angebot plausibel; erst mehrere Wochenschlüsse darüber zeigen Abbau. Ein Tag darüber ist kein Signal.
+- Wenn mehrere Wochenschlüsse außerhalb der Value Area liegen, sucht der Markt neuen Wert. Das ist Momentum; es rechtfertigt kein höheres Gewicht, wenn du ohnehin schon der Spanne folgst.
+- Innerhalb der Value Area sind Bewegungen zwischen den Rändern normal; dort umzuschichten kostet Gebühren ohne belegten Ertrag.
+- Lücken (dünne Zonen) sind auf Tagesdaten meist nur große Tagesschritte; schnelles Durchlaufen ist nicht belegt.
+- POC als Magnet, 70-%- und 80-%-Regeln haben keinen Out-of-sample-Beleg.
+
+### Wochenrhythmus
+- Am Wochenende sind Volumen und Tagesspanne normal niedriger. Diesen 7-Tage-Rhythmus nicht als Divergenz, Kompression oder Ausbruchsbestätigung lesen. Kalendermuster in der Rendite sind nicht belegt.
 
 You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
 Horizon is weeks to months; you do not need to trade often.
 
 Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
 Judge every window on its own. Do not compare windows with each other.
+
+Each window starts with a line about your decision on this asset one week ago: `last week: weight W, flip price F on today's scale`, or `last week: no decision`. Keep last week's weight unless the close has broken the flip price since then; only then decide a new weight. With no decision last week, decide freely.
 
 Before the weights, write out your analysis:
 1. Strategy: in 2 to 3 sentences, the rule you will apply to every window.
 2. Then for each window, under its id: your read of the market (trend, structure, key levels as prices on the 100 scale), your weight and why, and the price on the 100 scale that would make you change your mind.
-3. End with one JSON object mapping each window id to its weight, e.g. {"a1b2c3d4e5": 0.0, "f6a7b8c9d0": 1.0}. Nothing after it.
+3. End with one JSON object mapping each window id to its weight and flip price, e.g. {"a1b2c3d4e5": {"weight": 0.0, "flip": 104.5}, "f6a7b8c9d0": {"weight": 1.0, "flip": 91.0}}. Nothing after it.
```

## Prompt
```
# T-001 baseline trader prompt

# Wissen für die Wochenentscheidung

Dieses Wissen stammt aus einer Auswertung veröffentlichter Studien und Praxisquellen zu jedem Baustein der Charttechnik. Es gilt für tägliche Kerzen und Entscheidungen über Wochen bis Monate in Krypto. Du bekommst nur Kerzen (OHLCV, normiert); alle Kennzahlen unten schätzt du bei Bedarf selbst aus der Tabelle. Schwellen sind Faustwerte, keine exakten Grenzen.

## Grundsätze

1. **Was belegt ist.** Zeitreihen-Momentum über 1 bis 4 Wochen hat in Krypto Belege, vor allem long-only und vor allem dadurch, dass es lange Abwärtsphasen meidet. Volatilität bündelt sich und ist gut vorhersagbar, Rendite kaum. Fast alles andere (Kerzenmuster, Chartformationen, Fibonacci, Pivots, Divergenzen, Oszillator-Schwellen, Wyckoff, Elliott, Volumenprofil, Squeeze) ist für Krypto auf Wochensicht nach Kosten nicht belegt.
2. **Fast alles misst dasselbe.** Spannenposition, %K, Williams %R, RSI, %B, Abstand zum Durchschnitt, CCI, MACD, ROC, RCI, Ichimoku, Gaussian Channel, Kanal- und Value-Area-Lage sind Umformungen von zwei Größen: vergangene Rendite und Lage in einer Spanne. Stimmen mehrere überein, ist das **ein** Befund, nicht mehrere.
3. **Spannenlage ist kein Signal.** Ein Gewicht, das der Lage in der sichtbaren Spanne folgt, läuft dem Kurs hinterher und verliert nach Kosten. Hoch in der Spanne heißt höchstens halten, nicht aufstocken; tief in der Spanne ist ohne Trendwende kein Kaufgrund.
4. **Zustand statt Abstand.** Ein Gewicht ändert sich nur, wenn sich ein Zustand ändert (Regime, Trendbruch, gehaltener Ausbruch), nicht wenn ein Abstand oder Indikatorwert größer oder kleiner wird. Nutze Hysterese: Einstieg und Ausstieg an verschiedenen Schwellen, Bestätigung über mehr als eine Woche oder mehrere Wochenschlüsse.
5. **Kosten.** Jede Umschichtung kostet 0,2 %. Änderungen unter etwa 0,15 Gewichtspunkten bringen erwartbar nichts. Wenige, große, begründete Änderungen schlagen viele kleine. Ohne belegtes Signal bleibt das Gewicht nahe seinem Mittel.
6. **Volatilität steuert die Größe, nicht die Richtung.** Hohe oder steigende Volatilität rechtfertigt ein kleineres Gewicht, egal in welche Richtung der Kurs läuft. Komprimierte Volatilität kündigt eine größere Bewegung an, nicht ihre Richtung.
7. **Seitwärts heißt stillhalten.** Wenn der Trend unklar ist (viele Kreuzungen eines flachen Durchschnitts, gemischte Hoch/Tief-Folge, geringe Trendgüte), sind alle Signale aus Lage und Kreuzungen Rauschen. Gewicht konstant.
8. **Wochenebene vor Tagesebene.** Die Richtung kommt aus der Wochenebene. Einzelne Tageskerzen, Tagesextreme und Tageskreuzungen ändern ein Wochengewicht nicht. Einzelne Extremwochen deuten eher auf Gegenbewegung als auf Fortsetzung.

## Bausteine

Je Baustein die Regeln, die nach Beleglage übrig bleiben.

### Zeitreihen-Momentum
- Wenn 2-, 4- und 8-Wochen-Rendite dasselbe Vorzeichen haben und |z_4W| über 0,5 liegt, ist das ein Trendzustand; sonst ist Momentum kein Signal.
- Wenn das Momentum positiv ist, trägt es typischerweise 2 bis 4 Wochen; danach steigt das Umkehrrisiko.
- Wenn die letzte Woche allein extrem war (z über 2) ohne Bestätigung der längeren Fenster, deutet das eher auf Gegenbewegung als auf Fortsetzung.
- Wenn das Momentum negativ ist, rechtfertigt das Reduzieren zur Schadensbegrenzung, ist aber als Prognose schwächer als positives.
- Wenn der Vorzeichenzustand unverändert ist, bringt Nachjustieren nur Kosten; ändere das Gewicht erst bei bestätigtem Wechsel.
- Lage im 180-Tage-Fenster ist kein Momentum.
- Wenn fast alle Coins dasselbe Vorzeichen haben, ist der Querschnittsrang wenig wert.

### Regime
- Regime sagen, welchem Werkzeug du trauen darfst, nicht wohin der Kurs geht.
- Wenn ER(30) hoch ist und die Volatilität normal, dann trägt Trendfolge; ohne hohen ER ist die Lage in der Spanne kein Signal.
- Wenn ER niedrig ist, dann halte das Gewicht nahe der Mitte und schichte wenig um; Umschichten im Seitwärts-Regime kostet sicher und bringt unbelegt etwas.
- Wenn die Volatilität im oberen Fünftel ihrer Historie liegt, dann verkleinere die Position, egal in welche Richtung der Kurs läuft; hohe Volatilität allein ist kein Verkaufssignal.
- Wenn langes und kurzes Momentum widersprechen, dann ist ein Wendepunkt möglich: Gewicht zur Mitte, nicht voll umdrehen.
- Wechsle ein Regime-Urteil erst, wenn es über mehr als eine Woche deutlich bestätigt ist.

### Mehrere Zeitebenen
- Die Wochenebene bestimmt die Richtung, die Tagesebene nie allein. Ein Tagessignal gegen den Wochentrend ist kein Signal.
- Wenn langsames und schnelles Momentum übereinstimmen (Bull oder Bear), ist ein klares Gewicht gerechtfertigt; wenn sie sich widersprechen, ist ein mittleres Gewicht richtig, kein Sprung ins Extrem.
- Wenn das Wochenregime steigt und die letzten 1 bis 3 Wochen fallen (Correction), ist das kein Verkaufsgrund; im Mittel war hier langsames Festhalten besser.
- Wenn das Wochenregime fällt und kurz eine Erholung kommt (Rebound), Gewicht nur stufenweise erhöhen; eine Erholung ohne Wende der Wochenlinie ist oft nur eine Rally im Abwärtstrend.
- Ein Zustandswechsel zählt erst, wenn er über den Rauschpuffer hinausgeht oder sich bestätigt; Pendeln um die Wochenlinie ist kein Anlass umzuschichten.
- Tagesextreme deuten in Krypto eher auf Gegenbewegung als auf Fortsetzung.

### Positionsgröße und Kosten
- Ein Gewicht ist Risikodosis, keine Prognose. Wenn kein Signal mit Belegen eine Richtung anzeigt, bleibt das Gewicht nahe dem Mittelwert.
- Wenn σ_20/σ_90 über 1,5 liegt, dann ist ein kleineres Gewicht vertretbar; zwischen 0,8 und 1,25 ist das Verhältnis kein Signal.
- Wenn die geplante Änderung kleiner als etwa 0,15 Gewichtspunkte ist, dann bringt sie nach Kosten erwartbar nichts; nicht umschichten.
- Wenn ein Wechsel nötig erscheint, dann nur einen Teil der Lücke schließen.
- Position in der Spanne und vergangene Rendite sind keine Größensignale; ohne nachgewiesenes Momentum über den Haltehorizont ist Nachlaufen ein Verlustgeschäft.
- Ein tiefer Drawdown allein rechtfertigt keinen Abbau; nur zusammen mit steigender Volatilität und intaktem Abwärtstrend.
- Volatilität ist vorhersagbar, Rendite kaum: Größe über Volatilität steuern, nicht über Kursniveau.

### Typische Fehler
- Wenn dein Gewicht nur steigt, weil der Kurs gestiegen ist, ist das Hinterherlaufen; ohne eine Begründung, die schon vor der Bewegung galt, ist der Anstieg kein Signal.
- Die Position in der sichtbaren Spanne ist ein Anker. Nahe am Hoch spricht sie höchstens für Halten, nicht für stufenweises Aufstocken.
- Eine Woche innerhalb von etwa einer Standardabweichung ist Rauschen; ändere dann nichts.
- Wenn die vorgeschlagene Änderung unter etwa 0,15 liegt, lass das Gewicht stehen; die Kosten und das Timingrisiko überwiegen.
- Wenn du nach einem Rückgang senken willst, prüfe, ob die Schwankung gestiegen ist; wenn nur der Kurs fiel, ist es Recency.
- Wenige, große, begründete Änderungen schlagen viele kleine.

### Gleitende Durchschnitte
- Wenn der Kurs mehrere Wochenschlüsse unter einem fallenden langen Schnitt (100 bis 200 Tage) liegt, ist das ein Abwärtsregime, und ein reduziertes Gewicht ist vertretbar. Ohne fallenden Schnitt ist ein Kurs unter dem Schnitt kein Signal.
- Wenn der Kurs einen flachen Schnitt in den letzten Monaten mehrfach gekreuzt hat, sind weitere Kreuzungen Rauschen. Dann ändert man das Gewicht nicht.
- Kurs über steigendem Schnitt heißt halten, nicht aufstocken. Ein großer Abstand ist kein Kaufgrund, und ohne Trendbruch ist er auch kein Verkaufsgrund.
- Abstand, Spannenposition und Momentum messen dasselbe. Sie zählen nur einmal.
- Kreuzungen von Kurs mit SMA20 oder SMA50 sowie Golden und Death Cross sind auf Wochensicht keine eigenständigen Signale.
- Das Gewicht wechselt nur, wenn sich das Regime ändert, nicht bei jeder Änderung des Abstands. Jede Umschichtung kostet 0,2 %.

### Durchschnitte und Bänder als Unterstützung/Widerstand
- Wenn der Kurs über einem steigenden langsamen Durchschnitt (50 bis 140 Tage) schließt, ist der Trend intakt. Ein Test des Durchschnitts ist dann kein Kaufsignal, sondern ein Grund, das Gewicht nicht zu ändern.
- Wenn ein Wochenschluss mehr als 1 ATR unter dem Durchschnitt liegt und der Durchschnitt flach wird oder fällt, trägt das eine Gewichtssenkung. Ohne flache Steigung erst eine zweite Woche abwarten.
- Wenn der Kurs den Durchschnitt in 60 Tagen mehrfach kreuzt, hat er keine U/W-Bedeutung. Nicht darauf reagieren.
- Ein fallender Durchschnitt über dem Kurs ist Widerstand. Eine Erholung bis dorthin ist kein Kaufgrund.
- Großer Abstand über dem Durchschnitt ist allein kein Verkaufsgrund. Belegt ist eher Fortsetzung.
- SMA20, Bollinger-Mitte und RSI über 50 sind dieselbe Information. Nur einmal zählen.

### MACD
- Der MACD ist Momentum der letzten 1 bis 8 Wochen. Wenn er mit dem langen Trend übereinstimmt, ist das keine zusätzliche Bestätigung.
- Wenn der langsame MACD (Wochenbasis) über null liegt und steigt, ist das Regime aufwärts. Ohne Wochenbasis ist ein positiver Tages-MACD kein Signal für Wochen bis Monate.
- Signallinienkreuzungen und Histogramm-Vorzeichenwechsel auf Tageskerzen sind überwiegend Rauschen. Wenn du darauf umschichtest, zahlst du rund 29 Kreuzungen pro Jahr.
- Wenn das Histogramm schrumpft, aber die Linie über null bleibt, ist der Trend intakt und nur langsamer.
- Wenn die Linie in 90 Tagen mehrfach die Null kreuzt, ist das Regime seitwärts. Dann gibt der MACD keine Richtung, und das Gewicht sollte stabil bleiben.
- Divergenzen sind ohne Bruch des langen Trends kein Verkaufsgrund.
- Ein hoher MACD-Wert heißt, dass der Kurs gestiegen ist, nicht dass er weiter steigt oder fällt.

### Trendstärke (ADX, Efficiency Ratio, R²)
- Wenn die 30- bis 90-Tage-Rendite positiv ist und ER über etwa 0,3 oder R² über etwa 0,7 liegt, ist der Trend glatt und eher fortsetzungsfähig; ohne diese Güte ist dieselbe Rendite kein Signal.
- Wenn ADX hoch ist, prüfe −DI gegen +DI: ADX sagt nur Stärke, nicht Richtung.
- Wenn ADX unter etwa 20 und ER nahe 0, halte das Gewicht konstant; Signale aus Spannenlage oder DI-Kreuzungen sind dort Rauschen.
- Wenn ein Anstieg aus einer oder zwei Riesenkerzen stammt, werte ihn schwächer als einen gleich großen aus vielen kleinen Tagen.
- Fallender ADX bedeutet Pause, nicht Umkehr; hoher ADX ist kein Gipfelsignal.
- Ändere die Lesart erst, wenn die Güte die Schwelle klar und über mehr als eine Woche verlässt. Schwellen sind Faustwerte ohne Krypto-Beleg.

### Supertrend, Parabolic SAR, Donchian
- Wenn der Zustand seit der letzten Woche nicht gewechselt hat, dann gibt es keinen Grund umzuschichten; ein kleinerer oder größerer Abstand zum Stopp ist kein Signal.
- Wenn ein langes Hoch (60 Tage und mehr) auf Schlussbasis überschritten wird und die Wechselzahl der letzten 90 Tage niedrig ist, dann ist das ein gültiger Trendeinstieg; bei vielen Wechseln ist derselbe Ausbruch wahrscheinlich Rauschen.
- Wenn der Schluss unter den Stopp fällt, dann Gewicht senken, auch nach Verlust; das Abschneiden großer Verluste ist der eigentliche Nutzen.
- Die Position in der Spanne ist kein Gewicht. Gewicht = Anteil der Längen im Long-Zustand, bei hoher Volatilität gekürzt.
- Parabolic SAR nur mit klarer Trendstärke beachten, sonst ignorieren.
- Meist scheitern Ausbrüche; wenige große Trends tragen den Ertrag.

### Ichimoku
- Ichimoku besteht aus Spannenmitten und 26-Tage-Momentum. Es zählt als eine Trendstimme zusammen mit Durchschnitten und Momentum, nie zusätzlich.
- Wenn der Kurs mehrere Wochenschlüsse unter einer bärischen Wolke liegt und die 26-Tage-Rendite negativ ist, liegt ein Abwärtsregime vor, und ein reduziertes Gewicht ist vertretbar. Ohne negative 26-Tage-Rendite ist der Kurs unter der Wolke kein Signal.
- Kurs in der Wolke, oder mehrere Wolkenwechsel in den letzten drei Monaten: Der Trend ist unklar, das Gewicht bleibt unverändert.
- Kurs über einer bullischen Wolke heißt halten, nicht aufstocken. Ein großer Abstand zur Wolke ist überdehnt, kein Kaufgrund.
- Tenkan/Kijun-Kreuzungen und die Zukunftswolke sind auf Wochensicht keine Signale.
- Ein Wolkenbruch kommt spät. Er rechtfertigt eine Umschichtung nur, wenn er nach längerer Zeit im Gegenzustand eintritt. Jede Umschichtung kostet 0,2 %.

### Gaussian Channel
- Der Gaussian Channel ist ein etwa 80-tägiger gleitender Durchschnitt mit Volatilitätsband, Verzögerung rund 38 Tage. Er liefert keine Information, die nicht schon in Trendrichtung und Momentum steckt.
- Wenn der Filter seit Wochen steigt und der Kurs darüber liegt, ist der mittelfristige Trend intakt; das rechtfertigt ein stabiles Grundgewicht, keinen Zukauf.
- Ein Schluss über dem oberen Band ist Momentum nach einem bereits erfolgten Anstieg; ohne steigenden Filter ist er kein Signal, und Zukaufen dort heißt hinterherlaufen.
- Wenn der Filter fällt und der Kurs unter dem unteren Band schließt, ist Gewichtsreduktion am ehesten begründet.
- Wenn der Filter flach ist und die Farbe in 90 Tagen mehrfach wechselte, sind Farbwechsel Rauschen; dann nicht umschichten.
- Werte aus den ersten etwa 100 Kerzen sind unzuverlässig.

### Marktstruktur
- Struktur ist Momentum mit Hysterese. Wenn Struktur und Zeitreihen-Momentum übereinstimmen, zählt das als ein Signal, nicht zwei.
- Wenn die Wochenstruktur HH/HL zeigt und der Schluss über dem letzten großen HL liegt, ist ein Rücksetzer kein Grund, das Gewicht zu senken.
- Wenn ein Tagesschluss das letzte große HL bricht, ist das ein Warnsignal; erst ein danach folgendes tieferes Hoch bestätigt den Trendwechsel. Dazwischen ist Übergang.
- Ein BOS in Trendrichtung bestätigt nur; ohne vorher zu niedriges Gewicht ist er kein Grund zum Aufstocken.
- Wenn die Struktur gemischt ist, sagt sie nichts; Brüche in einer Spanne sind meist Fehlausbrüche.
- Ein einzelner Docht jenseits eines Swing-Extrems (Sweep) ist auf Wochensicht kaum informativ. Nur mit mehreren Schlüssen zurück in der Spanne und anschließendem Bruch des Gegen-Swings ist er ein schwaches Umkehrindiz.
- Nur bestätigte Swings verwenden; der letzte Schenkel ist vorläufig.

### Unterstützung und Widerstand
- Wenn der Kurs nur nahe einer Unterstützung oder eines Widerstands liegt, ist das auf Wochensicht kein Signal; der belegte Abprallvorteil ist klein, intraday und klingt binnen Tagen ab.
- Wenn ein Schluss eine mehrmonatige Spanne um mehr als 0,5 ATR verlässt und der übergeordnete Trend in dieselbe Richtung zeigt, ist das ein Trendsignal; gegen den Trend ist es keins.
- Wenn nach einem Ausbruch der Rücklauf auf Schlusskursbasis über der alten Zone hält, bestätigt das den Ausbruch; fällt der Schluss klar zurück in die Spanne, ist der Ausbruch gescheitert.
- Dochte jenseits einer Zone sind kein Bruch, nur Schlusskurse zählen.
- Die Anzahl der Tests sagt nichts über Halten oder Brechen; sie zeigt nur, dass eine Zone existiert.
- Innerhalb einer Spanne ohne Ausbruch ist häufiges Umschichten nach Position in der Spanne nach Kosten wertlos.

### Trendlinien und Kanäle
- Trendlinien nur auf logarithmischer Basis werten. Steigung einer langen Linie ist Momentum, kein zusätzliches Signal.
- Wenn eine Aufwärtslinie (über 40 Tage, flach, weit berührt) per Schluss um mehr als 0,5 ATR bricht und zugleich das letzte Swing-Tief oder der lange Durchschnitt fällt, dann spricht das für Trendende; ohne diese Bestätigung ist der Bruch meist nur Abflachung, kein Grund zum Umschichten.
- Bruch einer steilen, kurzen Linie ignorieren.
- Wenn R² niedrig ist, sind Trendlinien willkürlich; dann horizontale Spannen nutzen.
- Position im Kanal ist kein Signal. Gewicht nicht nach Kanalposition setzen, weder hoch oben noch hoch unten.
- Ein Ausbruch über eine Abwärtslinie zählt erst, wenn ein Rücklauf zur Linie hält oder ein Mehrmonatshoch folgt.
- Neue Linien nicht nachzeichnen, um eine bestehende Position zu rechtfertigen.

### Umkehrformationen
- Wenn eine Formation nicht per Schlusskurs jenseits der Nackenlinie bestätigt ist, ist sie kein Signal.
- Wenn ein Top bestätigt ist und das mittelfristige Momentum bereits schwach ist, deutet das auf gedämpfte Renditen über Wochen bis drei Monate; bei stark positivem Momentum ist dasselbe Top meist nur eine Pause.
- Wenn ein Boden im unteren Spannendrittel nach einem echten Abwärtstrend bestätigt ist, ist ein etwas höheres Gewicht begründbar; ohne Vortrend oder mit Höhe unter etwa 3 ATR ist es Rauschen.
- Ein Rücklauf zur Nackenlinie nach Bestätigung ist normal und kein Grund, erneut umzuschichten.
- Erst ein Schluss jenseits der rechten Schulter bzw. des zweiten Extrems macht die Formation hinfällig.
- Der belegte Effekt ist klein: maßvoll anpassen, nicht umkehren. Messregel-Ziele sind kein Erwartungswert.

### Fortsetzungsformationen
- Wenn sich eine Formation bildet, aber noch kein Schluss jenseits der Begrenzung liegt, dann bedeutet das nur: Bewegung wird größer. Keine Gewichtsänderung daraus.
- Wenn ein Schluss mindestens 0,5 ATR jenseits in Richtung eines bestehenden Mehrmonatstrends liegt und hält, dann stützt das die Trendposition. Ohne positiven Mehrmonatstrend ist derselbe Ausbruch kein Fortsetzungssignal.
- Wenn eine Fortsetzungsformation entgegen dem Trend bricht oder der Kurs nach einem Ausbruch deutlich in die Formation zurückfällt, dann ist das ein Warnsignal für die Trendposition.
- Eine Flagge folgt immer auf einen steilen Anstieg; sie ist kein eigener Kaufgrund.
- Kursziele werden etwa jedes zweite Mal verfehlt; nicht darauf halten.
- Keile sind ohne Momentum-Bestätigung kein Signal.
- Formationen unter drei Wochen lösen sich meist vor der nächsten Entscheidung auf; dafür nicht umschichten.

### Wyckoff
- Wenn der Kurs seit Wochen seitwärts läuft, sagt die Position innerhalb der Spanne kaum etwas über die nächste Woche. Gewicht nicht mit Schwankungen in der Spanne verschieben.
- Ein Docht unter das Spannentief mit Rückkehr (Spring) ist allein kein Kaufsignal; in Krypto entstehen solche Dochte oft durch Liquidationen. Erst wenn danach kein neues Tief folgt und ein Wochenschluss über der Spannenoberkante gehalten wird, spricht das für Aufwärtstrend.
- Spiegelbildlich: Upthrust über das Spannenhoch ist erst mit Wochenschluss unter der Unterkante ein Abwärtssignal.
- Wenn der Trend vor der Spanne abwärts lief und das Momentum negativ bleibt, ist ein Spring schwach; im Aufwärtstrend ist eine Spanne eher Pause.
- Ob Akkumulation oder Distribution, zeigt erst der gehaltene Ausbruch. Wenige Umschichtungen an bestätigten Ausbrüchen statt vieler an Vermutungen.

### Fibonacci
- Fibonacci-Niveaus sagen Umkehrpunkte nicht besser voraus als beliebige Niveaus gleicher Breite. Ein Kurs an einem Fibonacci-Niveau ist für sich kein Signal.
- Wenn der übergeordnete Trend steigt und eine Korrektur weniger als etwa ein Drittel des letzten großen Swings zurücknimmt, spricht das für intakte Stärke; mit einem Schluss über dem letzten Zwischenhoch gilt der Trend als wieder aufgenommen.
- Wenn eine Korrektur mehr als etwa drei Viertel des Swings zurücknimmt, ist der Swing neutralisiert; dann entscheiden Trend- und Regimesignale, nicht das Niveau.
- Ein Niveau zählt nur, wenn dort unabhängig davon eine echte Unterstützungszone aus früheren Umkehrpunkten liegt.
- Extensions sind keine Kursziele; das Erreichen einer Extension ist allein kein Grund, das Gewicht zu senken.
- Gewicht nicht wegen eines gehaltenen oder gebrochenen Fibonacci-Niveaus umschichten; die Kosten übersteigen den unbelegten Vorteil.

### Elliott-Wellen
- Wellenzählungen und Fibonacci-Ziele haben in Studien keine belegte Vorhersagekraft; Fibonacci-Marken halten nicht besser als beliebige andere Marken. Leite daraus kein Gewicht ab.
- Wenn eine Korrektur weniger als etwa die Hälfte des vorigen Schwungs zurückgibt und das Tief über dem Schwungstart bleibt, ist das mit intaktem Trend vereinbar; ohne bestätigendes Momentum ist es kein Kaufsignal.
- Wenn der Kurs den Start des letzten Impulsschwungs unterschreitet, ist die Trendannahme widerlegt. Das ist ein Risikoniveau, keine Prognose.
- "Letzte Welle" oder abnehmende Schwunglängen sind kein Verkaufssignal, solange das Momentum positiv ist; Krypto-Trends überschießen Extensionsziele oft weit.
- Eine neue Deutung derselben Kurse ist keine neue Information und kein Grund umzuschichten.

### Pivot Points
- Pivot-Linien sind nur Hoch, Tief und Schluss einer Vorperiode, umgerechnet. Über oder unter P zu stehen heißt lediglich: oberer oder unterer Teil der letzten Woche bzw. des letzten Monats. Das ist keine eigene Information.
- Wenn der Kurs P kreuzt und sonst nichts passiert, ist das kein Signal und kein Grund umzuschichten.
- Wenn der Kurs weit jenseits von Monats-R2/S2 steht und die Vorperiode ungewöhnlich eng war, zeigt das eine Volatilitätsausweitung, keine Richtung; die Richtung kommt aus Trend- und Regimebausteinen.
- Wenn eine Pivotlinie mit einem früheren Hoch oder Tief zusammenfällt, ist das keine doppelte Bestätigung, weil beide aus denselben Extremen stammen.
- Fibonacci- und Camarilla-Linien haben keinen belegten Vorteil. Für Wochenentscheidungen in Krypto gibt es keinen belastbaren Beleg, dass Pivots Rendite vorhersagen.

### Kerzen
- Kerzenmuster haben auf Tagesbasis in Krypto keinen belastbaren Vorhersagewert; Studien finden nach Kosten und Mehrfachtest-Korrektur kaum etwas. Eine einzelne Tageskerze ist kein Grund zum Umschichten.
- Wenn eine Wochenkerze ein Extrem der 180-Tage-Spanne überschreitet und weit davon entfernt schließt (CLV unter 0,3 am Hoch, über 0,7 am Tief) bei großer Spanne, dann ist das ein schwacher Hinweis, dass der Ausbruch nicht gehalten hat; ohne Lage am Spannenextrem ist derselbe Docht Rauschen.
- Ein Doji sagt allein nichts.
- Eine große Kerze in Trendrichtung ist kein neues Signal, sondern nur Momentum, das du schon kennst; nicht zusätzlich gewichten.
- Umkehrmuster gegen einen intakten übergeordneten Trend scheitern meist.
- Erwarteter Mustervorteil ist kleiner als die Umschichtungskosten mehrerer Wochen.

### Tagesperformance
- Wenn ein einzelner Tag stark ist, dann ändert das allein dein Wochengewicht nicht; Tagesrichtung ist in Krypto kaum vorhersagbar.
- Wenn ein Tag |z| ≥ 2 erreicht, dann steigt die erwartete Schwankung der Folgetage, nicht die erwartete Rendite. Nach oben heißt das: nicht aufstocken.
- Wenn eine einzelne Woche |z_W| über etwa 2 hat, dann ist sie eher Umkehrkandidat; nur wenn 2 bis 4 Wochen in dieselbe Richtung zeigen, ist es Momentum.
- Wenn eine Serie 5 bis 7 Tage lang ist, aber in σ-Einheiten klein, dann ist sie Zufall, kein Signal.
- Wenn σ30 deutlich über σ90 liegt, dann ist ein kleineres Gewicht risikogerechter, unabhängig von der Richtung.
- Wenn der Anstieg von wenigen Extremtagen getragen wird, dann ist er fragil, aber MAX allein sagt die Richtung nicht voraus.

### RSI
- Wenn das langsame Regime aufwärts zeigt und RSI-Rücksetzer über 40 halten, ist RSI über 70 Stärke; ohne Abwärtsregime ist "überkauft" kein Verkaufsgrund.
- Wenn das Regime abwärts zeigt und Erholungen bei 50 bis 60 scheitern, ist RSI unter 30 Schwäche; ein Kaufgrund ist das nicht.
- Erst wenn ein Rücksetzer deutlich unter 40 fällt und die folgende Erholung unter 60 bleibt, hat sich das Band verschoben. Das ist ein Grund für eine Gewichtsänderung, eine einzelne Schwellenkreuzung nicht.
- RSI und Spannenposition messen fast dasselbe. Wenn beide hoch sind, ist das eine Information, nicht zwei.
- Ein Extremwert aus einer einzigen großen Kerze sagt wenig über die nächste Woche.
- Wenn kein Bandwechsel vorliegt, dann rechtfertigt der RSI keine Umschichtung; Gewicht halten ist dann die kostengünstige Wahl.

### Stochastik und Stoch RSI
- %K ist die Lage in einer Spanne, kein Momentum und keine Prognose. Hohe Spannenlage allein ist nie ein Grund, das Gewicht zu erhöhen.
- Wenn %K(14) seit mehreren Tagen über 80 liegt und die 2- bis 8-Wochen-Rendite positiv ist, dann ist das Trendstärke; nicht deswegen reduzieren.
- Wenn %K(14) unter 20 fällt, die mittlere Rendite aber positiv bleibt, dann ist das ein Rücksetzer; höchstens Grund, eine Position nicht abzubauen. Ohne positiven Trend ist ein Tiefstand kein Kaufsignal.
- Wenn ein Extrem durch eine einzige große Kerze entstanden ist, dann zählt es nicht.
- %K zwischen 30 und 70, %K/%D-Kreuzungen und jeder Stoch-RSI-Wert sind kein Signal.
- RSI und Stochastik zählen zusammen als ein Hinweis.

### RCI
- RCI ist im Kern die n-Tage-Rendite in Rängen. Wenn RCI26 und RCI52 über +50 stehen, ist das Momentum, kein Verkaufsgrund; dasselbe wie positive 1- bis 2-Monats-Rendite, nicht zusätzlich zählen.
- RCI über +80 oder unter −80 ist allein kein Extrem: Das passiert auch bei reinem Zufall ein Drittel der Zeit.
- Zusatzinformation gibt nur der Vergleich: Wenn die Rendite hoch, der RCI aber nur mittel ist, kam der Anstieg in Sprüngen und ist weniger verlässlich; wenn der RCI hoch und die Volatilität niedrig ist, ist der Trend geordnet.
- Wenn nur RCI9 kippt und RCI52 unverändert ist, ist das Rauschen; kein Grund umzuschichten.
- Wenn alle drei Linien zwischen −50 und +50 liegen, sagt der RCI nichts.
- Nie das Gewicht proportional zum RCI setzen; das ist Hinterherlaufen.

### CCI, Williams %R, MFI, ROC, AO
- CCI, %R, MFI, ROC und AO sind Umformungen von Spannenposition, Abstand zum Durchschnitt, RSI, Momentum und MACD. Wenn mehrere gleichzeitig bullisch sind, ist das eine Information, nicht mehrere.
- Wenn %R oder die Spannenposition hoch ist, ist das kein Grund, das Gewicht zu erhöhen; ohne Momentum über 2 bis 4 Wochen (ROC-t-Wert über etwa 0,5) ist es nur Trendhinterherlaufen.
- Ein CCI über +100 ist nach Lambert Trendstärke, kein Verkaufssignal; erst ein Fall unter +100 nach langer Phase darüber ist ein Ausstiegshinweis, und nur, wenn der langsame Trend ihn bestätigt.
- Wenn ROC sich ändert, prüfen, ob ein alter Ausreißer aus dem Fenster gefallen ist.
- Einzelne Schwellenkreuzungen rechtfertigen keine Umschichtung; nur ein Vorzeichenwechsel im langsamen Maß, der über eine Woche hält.
- MFI abweichend vom RSI ist bei Krypto-Volumen ein schwacher Hinweis.

### Divergenzen
- Eine reguläre Divergenz bedeutet nur, dass der letzte Kursabschnitt langsamer war als der vorige. Ohne Bruch des Zwischentiefs (bärisch) bzw. Zwischenhochs (bullisch) ist sie kein Signal.
- Wenn ein Aufwärtstrend intakt ist und eine bärische Divergenz erscheint, dann höchstens nicht weiter aufstocken. Reduzieren erst, wenn Preisbestätigung und Trendbruch zusammenkommen.
- Bullische Divergenz im Abwärtstrend ist ohne Preisbestätigung kein Kaufgrund. Mehrere Divergenzen in Folge sind in Krypto normal.
- Divergenz auf RSI, MACD und Stochastik zugleich ist eine Beobachtung, nicht drei.
- Versteckte Divergenz trägt nur die Information des Trends.
- Steigender Kurs auf sinkendem Volumen ist allein kein Verkaufsgrund.
- Pivots unter 10 Tagen Abstand oder am rechten Fensterrand unbestätigt: ignorieren.
- Divergenzen rechtfertigen selten eine Umschichtung; Beleglage für Krypto fehlt.

### Bollinger-Bänder
- Wenn %B über 1 liegt und das Mittelband steigt und die Bandbreite wächst, ist das Trendstärke; ohne Umkehr am langen Schnitt ist das kein Verkaufsgrund.
- Wenn %B unter 0 liegt, ist das nur bei flachem Mittelband und niedriger, stabiler Bandbreite eine Kaufzone; im Abwärtstrend ist es Fortsetzung.
- Wenn die Bandbreite im untersten Perzentilbereich liegt, steigt die erwartete Schwankung, nicht der erwartete Kurs. Daraus folgt keine Richtung, nur Vorsicht bei der Schrittgröße.
- %B ist derselbe Befund wie Abstand zum Schnitt, RSI und Spannenposition; Übereinstimmung zählt nicht doppelt.
- Ändere das Gewicht nie proportional zu %B. Nur ein Wechsel des Regimes über mehrere Wochenschlüsse rechtfertigt eine Umschichtung.
- Bandsignale sind auf Aktienindizes seit Jahrzehnten wirkungslos und in Krypto nach Kosten nicht belastbar belegt.

### Keltner und Squeeze
- Wenn Q unter 1 liegt und das schon viele Tage, steigt die erwartete Schwankung, nicht der erwartete Kurs. Ohne einen unabhängigen Trendbefund ist der Squeeze kein Grund, das Gewicht zu ändern.
- Wenn der Squeeze feuert, ist die Bewegung bereits passiert. Nur wenn sie in Richtung des langen Trends geht, ist sie Fortsetzung; gegen den langen Trend ist sie häufig ein Fehlausbruch.
- Wenn der Kurs mehrere Tage über EMA + 2 ATR schließt und die EMA steigt, ist das Trendstärke, keine Überkauftheit.
- Wenn die ATR nach einem einzelnen Extremtag hoch ist und Q deshalb tief steht, ist das kein Squeeze, sondern abklingender Schock.
- Keltner-Position, %B, RSI und Spannenposition sind ein Befund; Übereinstimmung zählt einmal.
- Nutze ATR-Höhe für die Schrittgröße, nicht für die Richtung.

### ATR und Volatilität
- Volatilität sagt Volatilität voraus, nicht Richtung. Ohne Trend- oder Strukturhinweis ist hohe oder niedrige Volatilität kein Grund zum Kaufen oder Verkaufen.
- Wenn das Volatilitätsperzentil sehr hoch ist und der Trend abwärts zeigt, dann ist das die ungünstigste Lage; ein geringeres Gewicht ist begründet. Ist der Trend aufwärts, ist hohe Volatilität allein kein Ausstiegsgrund.
- Wenn die Volatilität komprimiert ist, dann steht wahrscheinlich eine große Bewegung bevor; die Richtung kommt erst mit dem Ausbruch und dessen Bestätigung.
- Miss Trendstärke in Volatilitätseinheiten: dieselbe Prozentbewegung ist bei hoher ATR% schwächer.
- Volatilität ändert sich von Woche zu Woche stark, jede Umschichtung kostet 0,2 %. Passe das Gewicht nur bei deutlichem Regimewechsel an, nicht bei kleinen Schwankungen der ATR.
- Ein einzelner Extremtag verzerrt die Messung; prüfe, ob die erhöhte Volatilität breit ist.

### Volumen
- Volumen hat keine Richtung. Hohes Volumen heißt große Bewegung oder hohe Volatilität, nicht "kaufen".
- Wenn der Preis aus einer mehrwöchigen Spanne ausbricht und das Wochenvolumen deutlich über seinem Median liegt, ist der Ausbruch eher echt; ohne erhöhtes Volumen ist ein knapper Ausbruch kein Signal.
- Steigendes Volumen in einer Rallye ist normal. Es ist kein Grund, das Gewicht zu erhöhen; das wäre Trendhinterherlaufen.
- Eine einzelne Volumenspitze ist kein Wendepunkt. Eine Spitze nach langem, tiefem Fall kann Erschöpfung anzeigen, aber ohne Zeitpunkt; erst ein anschließend stabiler Preis über Wochen macht daraus Information.
- OBV, das mit dem Preis läuft, sagt nichts. Nur eine Abweichung über mehrere Wochen ist ein schwacher Hinweis, nie allein ein Grund zum Umschichten.
- Volumen und Volatilität nicht doppelt zählen.

### VWAP
- Der VWAP ist der mittlere Einstand seit dem Anker. Über dem VWAP heißt nur: Käufer seit dem Anker sind im Schnitt im Gewinn. Das ist Momentum, kein zusätzlicher Kaufgrund.
- Wenn der Preis unter dem AVWAP vom letzten großen Hoch liegt und sich ihm nähert, ist dort Angebot plausibel; erst mehrere Wochenschlüsse darüber zeigen, dass es abgebaut ist. Ein einzelner Tag darüber ist kein Signal.
- Wenn Wochenschlüsse unter den AVWAP vom letzten großen Tief fallen, hat die Erholung ihren Einstand verloren; Gewicht nicht auf diesen Grund hin erhöhen.
- Wenn der VWAP flach ist und der Preis pendelt, können ±2σ grob Überdehnung zeigen; in einem Trend sind Bänder keine Umkehrpunkte.
- Rollierender VWAP und gleitender Durchschnitt gleicher Länge zählen als ein Signal.
- Kreuzungen auf Tagesbasis ignorieren; sie kosten nur Umschichtungsgebühren.

### Volumenprofil
- Ein Profil aus Tageskerzen zeigt vor allem, wo der Preis lange war. POC liegt fast immer nahe dem VWAP und der Spannenmitte; zusammen ein Signal, nicht mehrere.
- Wenn der Preis von unten an einen HVN läuft, der jung ist und unter dem der Preis seitdem lag, ist Angebot plausibel; erst mehrere Wochenschlüsse darüber zeigen Abbau. Ein Tag darüber ist kein Signal.
- Wenn mehrere Wochenschlüsse außerhalb der Value Area liegen, sucht der Markt neuen Wert. Das ist Momentum; es rechtfertigt kein höheres Gewicht, wenn du ohnehin schon der Spanne folgst.
- Innerhalb der Value Area sind Bewegungen zwischen den Rändern normal; dort umzuschichten kostet Gebühren ohne belegten Ertrag.
- Lücken (dünne Zonen) sind auf Tagesdaten meist nur große Tagesschritte; schnelles Durchlaufen ist nicht belegt.
- POC als Magnet, 70-%- und 80-%-Regeln haben keinen Out-of-sample-Beleg.

### Wochenrhythmus
- Am Wochenende sind Volumen und Tagesspanne normal niedriger. Diesen 7-Tage-Rhythmus nicht als Divergenz, Kompression oder Ausbruchsbestätigung lesen. Kalendermuster in der Rendite sind nicht belegt.

You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
Horizon is weeks to months; you do not need to trade often.

Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
Judge every window on its own. Do not compare windows with each other.

Each window starts with a line about your decision on this asset one week ago: `last week: weight W, flip price F on today's scale`, or `last week: no decision`. Keep last week's weight unless the close has broken the flip price since then; only then decide a new weight. With no decision last week, decide freely.

Before the weights, write out your analysis:
1. Strategy: in 2 to 3 sentences, the rule you will apply to every window.
2. Then for each window, under its id: your read of the market (trend, structure, key levels as prices on the 100 scale), your weight and why, and the price on the 100 scale that would make you change your mind.
3. End with one JSON object mapping each window id to its weight and flip price, e.g. {"a1b2c3d4e5": {"weight": 0.0, "flip": 104.5}, "f6a7b8c9d0": {"weight": 1.0, "flip": 91.0}}. Nothing after it.
```

## Bewertung gegen E-003M

| Coins | Wochen | Entscheidungen | Timing-Wert/Woche | Basis | Differenz | t | ohne beste Woche | Wochen besser | Exposure | Rank-IC |
|---|---|---|---|---|---|---|---|---|---|---|
| A (10) | 13 | 130 | 0.005 % | -0.244 % | 0.249 % | 1.38 | 0.104 % (ohne 2026-08-16) | 9/13 | 0.288 (Basis 0.463) | 0.091 |

**Urteil: kein messbarer Unterschied**

Verbrauch: 13 Claude-Aufrufe, 1250k Zeichen, Listenpreis 7.1 USD (zählt gegen Aarons Limit, keine Rechnung)

## Was die KI gedacht hat (Beispiel: Entscheidung 2026-07-05)

Alle Wochen: [denken.md](denken.md)

````
**Strategy:** The weekly regime sets direction. Every window sits under a falling long average after a big decline and a sharp break about a month ago. I start from a low base weight of 0.1 to 0.2. I add a little only where the short rebound looks orderly and has a higher-low structure. I never chase a single extreme week. Each flip price is the level whose close would change the regime read: usually a hold above the post-crash range high, or a loss of the most recent higher low.

## 18e32e3f34 (LINK)
- **Read:** Long downtrend from 175 to 100, with a crash from 113 to 88 around day -30. Since then it has ranged between 87 and 107.
- **Momentum:** 8-week −25%, 4-week +2%, 2-week +4%. The signs are mixed, so there is no trend state.
- **Levels:** Price is below a falling 100-day average of about 110. Last week's +12% bounce is a rally inside a downtrend.
- **Weight:** 0.2, because the regime is down and volatility is high.
- **Flip:** A close above 107, the post-crash range high.

## e180ea7ec3 (ETH)
- **Read:** Same shape: 135 down to 85, then a rebound to 100.
- **Momentum:** 8-week −25%, 4-week +14%, 2-week +5%. Long and short momentum conflict.
- **Levels:** The long average is falling. Resistance is at 103.6 (the day -20 high), then about 113.
- **Weight:** 0.2.
- **Flip:** A close above 104.

## 3f78d4b448 (DOGE)
- **Read:** Peaked at 148 at day -52, then made lower highs at 118 and 107.
- **Momentum:** 2-, 4- and 8-week returns are all negative (−5%, −5%, −31%), which is a downtrend state. Last week's bounce from 92 to 100 does not change the weekly line.
- **Weight:** 0.1.
- **Flip:** A close above 108, the day -17 to -20 area.

## 55ac4942e5 (BTC)
- **Read:** Fell from 129 to 93, then went sideways between 91 and 105.
- **Momentum:** 8-week −23%. The 4- and 2-week returns are flat. The regime is down and short-term direction is unclear.
- **Weight:** 0.2.
- **Flip:** A close above 106, the range top.

## ed0b5479a3 (DOT)
- **Read:** Steady lower highs from 157 to 119 to 115, now at 100.
- **Momentum:** 2-, 4- and 8-week returns are all negative (−6%, −10%, −36%), with high ATR%. This is the clearest down regime of the set.
- **Weight:** 0.1.
- **Flip:** A close above 112, which would reclaim the day -17 to -13 shelf.

## 76ff955e0b (SOL)
- **Read:** Crashed to 74 at day -29, then made higher lows at 79 and 86–88 and higher highs. Price has reclaimed the pre-crash range of 100–105.
- **Momentum:** 4-week +23% and 2-week +13% against 8-week −15%. That conflict points to a possible turning point.
- **Weight:** 0.35, a middle weight rather than an extreme one.
- **Flip:** A close below 88, which would break the latest higher low.

## 4eb7875f84 (ADA)
- **Read:** Fell from 149 to 73, then jumped 32% in the last week on high volume.
- **Momentum:** The last week alone is extreme (z > 2). Longer windows do not confirm it: 8-week is −33%, while 4-week is +15%. A single extreme week is more likely a counter-move than a trend, and volatility is very high.
- **Weight:** 0.2.
- **Flip:** A close above 106, meaning the breakout above 100–105 holds.

## 8a3d60d1fa (XRP)
- **Read:** Fell from 128 to 87, then rebounded to 100.
- **Momentum:** 8-week −21%. The 4- and 2-week returns are flat to +3%, which is mixed.
- **Levels:** Below a falling long average. Range high is about 107 on a close basis (112 at the wick).
- **Weight:** 0.2.
- **Flip:** A close above 107.

## 2f156c8c12 (LTC)
- **Read:** Fell from 132 to 86, then rebounded. Today's close of 100 is a marginal new post-crash closing high, and volatility is somewhat lower than in its peers.
- **Momentum:** 8-week −24%, 4-week +7%, 2-week +3%. The weekly line has not turned.
- **Weight:** 0.25.
- **Flip:** A close above 103, which would confirm the range breakout.

## 4a2f95d7d6 (AVAX)
- **Read:** Fell from 148 to 82 (at day -16), then rebounded to 100.
- **Momentum:** 8-week −32%, 4-week +2%, 2-week +13%. The signs are mixed.
- **Levels:** Resistance is at 102 to 104.
- **Weight:** 0.2.
- **Flip:** A close above 104.

{"18e32e3f34 (LINK)": {"weight": 0.2, "flip": 107.0}, "e180ea7ec3 (ETH)": {"weight": 0.2, "flip": 104.0}, "3f78d4b448 (DOGE)": {"weight": 0.1, "flip": 108.0}, "55ac4942e5 (BTC)": {"weight": 0.2, "flip": 106.0}, "ed0b5479a3 (DOT)": {"weight": 0.1, "flip": 112.0}, "76ff955e0b (SOL)": {"weight": 0.35, "flip": 88.0}, "4eb7875f84 (ADA)": {"weight": 0.2, "flip": 106.0}, "8a3d60d1fa (XRP)": {"weight": 0.2, "flip": 107.0}, "2f156c8c12 (LTC)": {"weight": 0.25, "flip": 103.0}, "4a2f95d7d6 (AVAX)": {"weight": 0.2, "flip": 104.0}}
````

## Notizen
Backlog #35. dev-informiert (Auflagen Waechter B-18 wie #31): ein Sieg gilt hoechstens als Kandidat, zaehlt als eine Variante, bei Sieg folgen Ablationen, nur das Turnier beweist etwas. Prompt = E-017/prompt.md plus dieselbe Gedaechtnis-Aenderung wie E-016 gegenueber E-003M. Hypothese: beide zusammen senken Umschichtung und Spannen-Anker. Falsifiziert, wenn der partielle Ankerwert (werkzeuge/anker.py) ueber 0,2 oder die Umschichtung ueber 0,07 liegt. Vergleich: E-016 (+0,16 t 1,05, Umschichtung 0,04, partiell -0,15), E-017 (+0,30 t 1,57, 0,074, 0,43), E-019 (+0,19 t 1,70, 0,07, 0,41). Vorlage aus Paragraph 4a unveraendert bis auf das JSON-Format; versuche.py vom Branch claude/project-thread-lupsy0 (PR #6).

## Zusatzmetriken (Thread)
- dev-informiert (Wächter B-18): ein Sieg gälte höchstens als Kandidat; zählt als eine Variante.
- Umschichtung 0,025 je Coin und Woche (E-016 0,037, E-017 0,074, E-019 0,067); Gewicht in 103 von 120 Fällen unverändert, 17 Änderungen.
- Anteil der Gewichtsänderungen unter 0,15: 29 % (5 von 17); E-016 22 %, E-017 81 %, E-019 80 %.
- Spannen-Anker (werkzeuge/anker.py): einfache Korrelation 0,75, partiell 0,15 (E-003M 0,40, E-016 −0,15, E-017 0,43, E-019 0,41); Korrelation zu Momentum 0,65.
- Falsifikator #35 (partiell > 0,2 oder Umschichtung > 0,07): greift nicht, Hypothese überlebt.
- Exposure 0,29 (E-003M 0,46): mittleres Gewicht steigt von 0,20 in Woche 1 auf 0,38 in Woche 13, fast nur Aufstockungen.
