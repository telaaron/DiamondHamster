# E-019: was die KI gedacht hat (Set A)

Volle Antwort des Deciders pro Entscheidungswoche, unverändert. Er sah weder Datum noch Coin-Namen; die Namen in Klammern sind erst danach eingesetzt. Gesendeter Prompt und Daten: runs/<set>/<woche>/requests.json.

## Entscheidung 2026-07-05

# Wochenentscheidung: zehn Fenster

## 1. Strategie

Die Richtung kommt aus der Wochenebene. Ich prüfe die Vorzeichen von z_2W, z_4W und z_8W, den Abstand zur SMA100 und deren Steigung. Liegt der Kurs mehrere Wochen unter einem fallenden SMA100, gilt ein Abwärtsregime und ich setze ein reduziertes Gewicht (≈0,3). Haben alle drei Momentum-Fenster ein negatives Vorzeichen und liegt |z_4W| über 0,5, gehe ich tiefer (≈0,2).

Kurzfristige Erholungen ohne Wende der Wochenlinie erhöhen das Gewicht nicht, ebenso wenig einzelne Extremwochen oder die Lage in der Spanne. Hohe Volatilität (σ20/σ90 über 1,1) bei Abwärtsregime kürzt das Gewicht leicht.

Ausgangslage: Alle Fenster zeigen dasselbe Muster. Nach einem Crash bei etwa −150 Tagen folgte eine Seitwärtsphase, dann ein zweiter Einbruch bei etwa −33 bis −30 Tagen und zuletzt eine Erholung über 1 bis 2 Wochen bis 100.

## 2. Fenster

### e91b99f05f (LTC)
- **Lage:** Momentum gemischt (z_2W +0,3, z_4W +0,6, z_8W −1,4), also kein Trendzustand. ER 0,11, Volatilität normal.
- **Trend:** Kurs 10 % unter dem fallenden SMA100 (≈111). Seit −33 mehrere Wochenschlüsse darunter, also Abwärtsregime.
- **Struktur:** Tief 85,7 (−10), Erholung bis 100, darüber Widerstand bei 101 und 111.
- **Gewicht 0,3:** Die Erholung ist eine Rally im Abwärtstrend.
- **Umdenken:** Mehrere Wochenschlüsse über ≈111 mit abflachendem SMA. Ein Schluss unter 85 bestätigt den Abwärtstrend.

### 9b52b46ae2 (ADA)
- **Lage:** Sprung von 76 auf 101 in vier Tagen (z_2W +1,4), aber z_8W −1,1. Einzelne Extremwoche, also eher Umkehrkandidat als Fortsetzung.
- **Trend und Volatilität:** Kurs 14,5 % unter dem stark fallenden SMA100 (≈117). σ-Verhältnis 1,12 und große Tageskerzen.
- **Gewicht 0,25:** Abwärtsregime plus erhöhte Schwankung.
- **Umdenken:** Wochenschlüsse über 105,5 und anschließend gehaltener Rücklauf. Ein Fall unter 72,9 wäre ein neues Tief.

### 7487e413ba (XRP)
- **Lage:** ER 0,08, z_4W 0, Momentum neutral. Spanne 87,5 bis 111,8 seit −33.
- **Trend:** Kurs unter dem fallenden SMA100 (≈112).
- **Gewicht 0,3:** Abwärtsregime, innerhalb der Spanne kein Signal.
- **Umdenken:** Schluss über ≈112 über mehrere Wochen. Unter 87 wird das Gewicht weiter gesenkt.

### 4d8a21a4ae (SOL)
- **Lage:** Kurs knapp über dem SMA100 (≈99), der aber noch fällt. 5 Kreuzungen in 90 Tagen, die Linie hat damit wenig Bedeutung.
- **Momentum:** z_4W +1,4 und z_2W +1,1, z_8W aber −0,7. Kurzes und langes Momentum widersprechen sich, also möglicher Wendepunkt. ER 0,33 ist ordentlich.
- **Struktur:** Hoch 102,9, Tief 73,7.
- **Gewicht 0,4:** Gewicht zur Mitte, nicht voll umdrehen.
- **Umdenken:** Wochenschlüsse über 103 und z_8W positiv, dann stufenweise Richtung 0,55. Ein Schluss unter ≈83 senkt das Gewicht wieder auf 0,25.

### 08ca7defc1 (AVAX)
- **Lage:** ER 0,04 und 8 SMA-Kreuzungen, also unklar und seitwärts in einer übergeordneten Abwärtsbewegung.
- **Trend und Volatilität:** Kurs 17,7 % unter dem fallenden SMA100 (≈121). σ-Verhältnis 1,13.
- **Struktur:** Spanne 82 bis 102.
- **Gewicht 0,3.**
- **Umdenken:** Gehaltener Ausbruch über 102 mit Folgewoche. Ein Schluss unter 82 senkt auf 0,2.

### 3c89c6f11e (LINK)
- **Lage:** Momentum neutral (z_4W +0,1), Volatilität komprimiert (0,79): eine größere Bewegung steht an, die Richtung ist offen.
- **Trend:** Kurs 8,6 % unter dem fallenden SMA100 (≈109).
- **Struktur:** Spanne 86,9 bis 106,7.
- **Gewicht 0,3.**
- **Umdenken:** Wochenschluss über 107 und danach über dem SMA100. Ein Schluss unter 86,9 bestätigt den Abwärtstrend.

### fecb1f68ac (BTC)
- **Lage:** Momentum neutral, ER 0,09. Kurs 10,4 % unter dem fallenden SMA100 (≈112).
- **Struktur:** Spanne 90,8 bis 105,7.
- **Gewicht 0,3.**
- **Umdenken:** Über 106 und SMA-Rückeroberung über mehrere Wochen. Unter 90,8 wird gesenkt.

### e7732e1b04 (ETH)
- **Lage:** Momentum gemischt (z_4W +0,4, z_8W −1,2). Kurs 12 % unter dem fallenden SMA100 (≈114).
- **Struktur:** Tief 84,7, Zwischenhoch 103,6.
- **Gewicht 0,3.**
- **Umdenken:** Wochenschluss über 104 und Halt im Rücklauf. Ein Schluss unter 84,7 senkt das Gewicht.

### 2344e6c4bf (DOT)
- **Lage:** Alle Momentum-Fenster negativ (z_2W −0,6, z_4W −0,6, z_8W −1,7), also ein Abwärts-Trendzustand.
- **Trend:** Kurs 23 % unter dem stark fallenden SMA100 (≈130).
- **Struktur:** Tiefere Hochs bei 118,8 und 113, Tief 90,2. Die Erholung auf 100 ist eine Rally im Abwärtstrend.
- **Gewicht 0,2.**
- **Umdenken:** Schluss über ≈119 (tieferes Hoch gebrochen), danach Bestätigung. Unter 90 bleibt das Gewicht bei 0,2 oder tiefer.

### a45704c534 (DOGE)
- **Lage:** Alle Momentum-Fenster negativ, z_4W −0,7, also ein Abwärts-Trendzustand.
- **Trend:** Kurs 17 % unter dem fallenden SMA100 (≈121).
- **Struktur:** Tiefere Hochs bei 118,7 und 116,8, Tief 89,3.
- **Gewicht 0,2.**
- **Umdenken:** Wochenschlüsse über 117. Ein Schluss unter 89 bestätigt die Fortsetzung.

## 3. Gewichte

{"e91b99f05f (LTC)": 0.3, "9b52b46ae2 (ADA)": 0.25, "7487e413ba (XRP)": 0.3, "4d8a21a4ae (SOL)": 0.4, "08ca7defc1 (AVAX)": 0.3, "3c89c6f11e (LINK)": 0.3, "fecb1f68ac (BTC)": 0.3, "e7732e1b04 (ETH)": 0.3, "2344e6c4bf (DOT)": 0.2, "a45704c534 (DOGE)": 0.2}

## Entscheidung 2026-07-12

1. **Strategy**

Direction comes from the weekly regime. Every window here sits below a falling SMA100 after a crash about 37 days ago. A long-term downtrend with short-term momentum that disagrees calls for a reduced, mid-to-low weight, not an extreme one. I lower the weight further only where 2-, 4- and 8-week momentum all point down, and I raise it only after weekly closes hold above the recent rebound highs.

2. **Windows**

**be50010ca1 (LTC)**
- **Read:** Price is 12.7% below a falling SMA100 (about 114). Momentum is mixed: z_2W +0.4, z_8W −1.2. ER is 0.05, so the last 40 days are a range of roughly 89–105. The recovery since the low near 89 is still a rally inside a downtrend.
- **Weight:** 0.30. The downtrend justifies a reduced weight; the conflicting short momentum argues against going lower.
- **Change my mind:** weekly closes above about 105 → raise; a close below 89 → cut.

**7a95db2a2d (ETH)**
- **Read:** Strongest 2-week push in the set (z_2W +1.4), recovering from about 84 to about 100. The long trend is still down (SMA100 about 111 and falling, 4 crossings).
- **Weight:** 0.35. Mixed momentum points to a middle weight, but the regime caps it.
- **Change my mind:** weekly closes holding above 102.4 → raise; below 84 → cut.

**a18907d929 (DOGE)**
- **Read:** Cleanest downtrend in the set. ER is 0.36, and 2-, 4- and 8-week momentum are all negative (z_4W −1.4, z_8W −1.8). Price is 21.8% below a falling SMA100. Lower highs at 127, 122, 109 and 104.
- **Weight:** 0.15. Aligned negative momentum is a trend state, so a low weight is justified.
- **Change my mind:** a weekly close above about 109 (breaks the lower-high sequence) → raise; below 95 → toward 0.

**06436a9cf4 (DOT)**
- **Read:** Price is 24.8% below SMA100, which is falling steeply (−8.7% in 20 days). Range of about 95–107. z_4W −1.0, z_8W −1.5. Six SMA crossings earlier show a choppy history, but the current regime is clearly down.
- **Weight:** 0.20.
- **Change my mind:** weekly closes above about 107.6 → raise; below 94 → cut.

**9f817b615b (SOL)**
- **Read:** Only 4.3% below SMA100. 2- and 4-week momentum are positive; 8-week is mildly negative. Higher lows since the low near 78 (78 → 83 → 98). Possibly an early turn, but SMA100 is still falling and the 109 high has not been taken out.
- **Weight:** 0.40.
- **Change my mind:** weekly closes above about 109.2 → raise toward 0.55; below 98 → back to 0.30.

**c99da955a9 (XRP)**
- **Read:** 15% below a falling SMA100. ER is 0.08, so this is sideways after the crash, in a range of about 93–109. Momentum is mixed.
- **Weight:** 0.30.
- **Change my mind:** above 109 holding → raise; below 93 → cut.

**1862deca9e (LINK)**
- **Read:** z_2W +1.0, but ER is 0.03 (sideways). 8.8% below a falling SMA100. Range of about 88–102.
- **Weight:** 0.35.
- **Change my mind:** weekly closes above 102.3 → raise; below 87.7 → cut.

**ebaf0bf3f3 (AVAX)**
- **Read:** 22.4% below a falling SMA100. Eight crossings and ER 0.03 mean the short term is noise. Range of about 89–111. Momentum is flat to negative.
- **Weight:** 0.25.
- **Change my mind:** above 111 holding → raise; below 88.7 → cut.

**01b537d1d2 (ADA)**
- **Read:** 25% below SMA100, which is falling steeply (−8.2% in 20 days). A spike to 123 has been fully given back, so the rally failed. Volatility is elevated (sigma20/sigma90 1.19).
- **Weight:** 0.20.
- **Change my mind:** weekly closes above about 118.6 → raise; below 85 → cut.

**faa9f23357 (BTC)**
- **Read:** ER is 0.01 (pure sideways). 9.9% below a gently falling SMA100. Range of about 90.6–105.5.
- **Weight:** 0.35.
- **Change my mind:** weekly closes above 105.5 → raise; below 90.6 → cut.

```json
{"be50010ca1 (LTC)": 0.30, "7a95db2a2d (ETH)": 0.35, "a18907d929 (DOGE)": 0.15, "06436a9cf4 (DOT)": 0.20, "9f817b615b (SOL)": 0.40, "c99da955a9 (XRP)": 0.30, "1862deca9e (LINK)": 0.35, "ebaf0bf3f3 (AVAX)": 0.25, "01b537d1d2 (ADA)": 0.20, "faa9f23357 (BTC)": 0.35}
```

## Entscheidung 2026-07-19

**Strategie:** Die Richtung kommt aus der Wochenebene. Kurs unter einem fallenden SMA100 mit negativem 8‑Wochen‑Momentum gilt als Abwärtsregime und spricht für ein reduziertes Gewicht. Widersprechen sich kurzes (2W/4W) und langes Momentum, bleibt das Gewicht im unteren Mittelfeld statt ins Extrem zu gehen. Bei niedrigem ER und vielen SMA‑Kreuzungen wird nicht nachjustiert. Nur wenn alle Fenster negativ sind und der Trend vergleichsweise glatt läuft (ER um 0,3), gehe ich deutlich unter die Mitte.

## 6f4f29aa48 (LTC)
- **Markt:** Zwei Crashs (Tief 86 bei −43, Retest 83,5 bei −25), seitdem höhere Tiefs und ein langsamer Anstieg auf 100. Der SMA100 liegt bei etwa 106 und fällt.
- **Momentum:** 2W/4W leicht positiv, 8W negativ. Das ist ein Widerspruch, also ein möglicher Wendepunkt, aber unbestätigt. ER 0,15, Volatilität normal.
- **Gewicht 0,40:** Abwärtsregime, aber eine beginnende Erholung. Deshalb Mitte minus.
- **Umdenken:** Mehrere Wochenschlüsse über 106 sprechen für mehr. Ein Schluss unter 86 spricht für weniger.

## bbada168ad (LINK)
- **Markt:** Doppeltief bei 83,4/83,6, dann Erholung bis 103 und jetzt 100. Der SMA100 liegt bei etwa 104 und fällt, 4 Kreuzungen in 90 Tagen deuten auf Seitwärtsphase.
- **Momentum:** Kurz positiv, lang negativ, ER 0,10. Kein Trendzustand.
- **Gewicht 0,40:** Stillhalten nahe dem unteren Mittel.
- **Umdenken:** Wochenschlüsse über 104–105 sprechen für mehr. Unter 83 für weniger.

## 9eb17dc197 (SOL)
- **Markt:** Tiefs bei 78,7 und 83,8. Die Erholung bis 108 (−17) ist zurückgelaufen, jetzt 100. Der SMA100 liegt bei etwa 104,6 und fällt, 6 Kreuzungen.
- **Momentum:** z_2W −0,6, ER 0,15. Seitwärts mit gescheitertem Vorstoß.
- **Gewicht 0,35.**
- **Umdenken:** Ein gehaltener Schluss über 108 spricht für mehr. Unter 84 für weniger.

## 2e36d1344d (ETH)
- **Markt:** Tiefs bei 80,4 und 81,9, Erholung bis 102,4, jetzt 100. Der SMA100 liegt bei etwa 106 und fällt.
- **Momentum:** Kurz positiv (z_4W +0,6), lang negativ, ER 0,16.
- **Gewicht 0,40:** Konflikt, also ein mittleres bis reduziertes Gewicht.
- **Umdenken:** Wochenschlüsse über 106 sprechen für mehr. Unter 81 für weniger.

## 7a1a744bc6 (BTC)
- **Markt:** Tiefs bei 91,4 und 89,8, enge Seitwärtsphase zwischen 92 und 101. Der Kurs liegt 8 % unter dem fallenden SMA100 (etwa 108,7).
- **Momentum:** ER 0,05, also reines Rauschen. 8W bei −1,1.
- **Gewicht 0,35:** Abwärtsregime ohne Trendgüte.
- **Umdenken:** Ein Schluss über 102 mit Folgewoche spricht für mehr. Unter 89,5 für weniger.

## 4f845a72e4 (DOGE)
- **Markt:** Lange Abwärtsfolge vom Hoch 163 (−66) mit tieferen Hochs (127,7, dann 109,6). Tiefs bei 98,6 und 96. Der Kurs liegt rund 21 % unter dem fallenden SMA100 (etwa 126).
- **Momentum:** 2W, 4W und 8W alle negativ, ER 0,32. Ein glatter Abwärtstrend.
- **Gewicht 0,20:** Zur Schadensbegrenzung reduziert.
- **Umdenken:** Ein Wochenschluss über 110 (tieferes Hoch gebrochen) spricht für mehr. Unter 96 bestätigt das niedrige Gewicht.

## 12336bfb0a (ADA)
- **Markt:** Crash auf 89 (−44), dann ein Spike auf 120 (−15), der komplett zurückgegeben wurde. Das ist ein gescheiterter Ausbruch. Der SMA100 liegt bei etwa 126 und fällt steil (−7,3 % in 20 Tagen).
- **Volatilität:** σ20/σ90 bei 1,18, also leicht erhöht. ER 0,03.
- **Gewicht 0,25:** Abwärtsregime mit hoher Schwankung.
- **Umdenken:** Wochenschlüsse über 115 sprechen für mehr. Unter 83 für weniger.

## fe5638aa62 (XRP)
- **Markt:** Tiefs bei 95,7 und 92,2, Hoch 107,9 bei −15, jetzt 100. Der Kurs liegt 13 % unter dem fallenden SMA100 (etwa 115).
- **Momentum:** Durchweg leicht negativ, ER 0,08.
- **Gewicht 0,30.**
- **Umdenken:** Wochenschlüsse über 108 sprechen für mehr. Unter 92 für weniger.

## 998417226f (AVAX)
- **Markt:** Tief bei 87,9 (−30), Erholung bis 110, jetzt 100. Der Kurs liegt rund 20 % unter dem fallenden SMA100 (etwa 125).
- **Volatilität und Momentum:** σ20/σ90 bei 0,75, also komprimiert. Das kündigt Bewegung an, aber keine Richtung. 8W bei −1,2.
- **Gewicht 0,25.**
- **Umdenken:** Ein gehaltener Schluss über 110 spricht für mehr. Unter 88 für weniger.

## 8a66aaf69f (DOT)
- **Markt:** Stufenweiser Abwärtstrend mit tieferen Hochs (127,7, dann 110,7, dann 109,1) und Tiefs bei 97–98. Der Tag 0 schließt schwach mit einem Low von 98,3. Der Kurs liegt rund 25 % unter dem SMA100 (etwa 133), der mit −7,5 % in 20 Tagen deutlich fällt.
- **Momentum:** Alle Fenster negativ, ER 0,28.
- **Gewicht 0,15:** Das klarste Abwärtsregime unter den Fenstern.
- **Umdenken:** Wochenschlüsse über 110 sprechen für mehr. Unter 97 bestätigt das niedrige Gewicht.

{"6f4f29aa48 (LTC)": 0.40, "bbada168ad (LINK)": 0.40, "9eb17dc197 (SOL)": 0.35, "2e36d1344d (ETH)": 0.40, "7a1a744bc6 (BTC)": 0.35, "4f845a72e4 (DOGE)": 0.20, "12336bfb0a (ADA)": 0.25, "fe5638aa62 (XRP)": 0.30, "998417226f (AVAX)": 0.25, "8a66aaf69f (DOT)": 0.15}

## Entscheidung 2026-07-26

## Strategie

Die Richtung kommt aus dem Wochenregime: dem langen Durchschnitt (SMA100 mit Steigung), dem 2-, 4- und 8-Wochen-Momentum und der Trendgüte (ER). Spannenlage und Oszillatoren zählen dabei nicht. Wenn alle drei Momentumfenster positiv sind und der Kurs über einem steigenden SMA100 liegt, gibt es ein klares Gewicht. Ein fallender SMA100 zusammen mit negativem 8W-Momentum ergibt ein reduziertes Gewicht (≈0,25). Widersprechen sich kurzes und langes Momentum bei brauchbarer Trendgüte, liegt das Gewicht in der Mitte (0,4–0,5). Im Seitwärtsmarkt (niedriger ER, viele Kreuzungen) bleibt das Gewicht stabil, und geändert wird nur bei bestätigten Wochenschlüssen.

Gemeinsamer Hintergrund aller Fenster: Etwa bei Tag −54 bis −51 gab es einen Einbruch um 15–30 %, danach folgte eine Erholung. Der SMA100 fällt überall, und das 8W-Momentum ist überall negativ. Ein bestätigter Aufwärtstrend liegt in keinem Fenster vor.

---

### 91b9b0398c (XRP)
- **Lage:** Abwärtsregime. Der Kurs liegt 10 % unter dem fallenden SMA100, ER 0,14, und es gab 4 Kreuzungen in 90 Tagen.
- **Struktur:** Die Hochs fallen: 116 (−41), 106 (−22), 104,6 (−5). Seit etwa 30 Tagen pendelt der Kurs zwischen 91 und 106.
- **Momentum:** z_4W +0,5 ist knapp, z_8W −0,9. Die Vorzeichen sind gemischt, also gibt es kein Trendsignal.
- **Gewicht 0,3:** reduziert, weil der Abwärtsregime-Befund besteht.
- **Umdenken:** Wochenschlüsse über 106,5 sprechen für 0,45. Unter 93 bleibt es reduziert.

### b08cc8b5d8 (LTC)
- **Lage:** Der Kurs liegt 2,9 % unter dem fallenden SMA100, ER 0,32 (Güte grenzwertig).
- **Struktur:** Die Tiefs steigen: 82 → 86 → 89,7 → 95,6. Ein neues Hoch bei 100,9 bildet kurzfristig HH/HL.
- **Momentum:** z_2W und z_4W liegen bei +1,0, z_8W bei −0,5. Kurzes und langes Momentum widersprechen sich, also mittleres Gewicht.
- **Gewicht 0,45**
- **Umdenken:** Wochenschlüsse über etwa 103 (SMA100) bei abflachendem Durchschnitt sprechen für 0,6. Ein Schluss unter 89,7 spricht für 0,25.

### e4d1a405e7 (DOT)
- **Lage:** Klarer Abwärtsregime-Befund. Der Kurs liegt 22 % unter dem SMA100, und der SMA100 fiel in 20 Tagen um 7,3 %. ER 0,05, z_8W −1,5.
- **Struktur:** Seit 30 Tagen seitwärts zwischen 95 und 109.
- **Gewicht 0,25:** reduziert, und Seitwärts heißt stillhalten.
- **Umdenken:** Wochenschlüsse über 109 sprechen für 0,4. Unter 95 bleibt es bei 0,25.

### 4ea7b90132 (SOL)
- **Lage:** Der Kurs liegt 3,2 % unter einem nur leicht fallenden SMA100. Es gab 6 Kreuzungen, ER 0,12. Das ist ein Seitwärtsregime.
- **Struktur:** Spanne 95–109. Der Rebound von 80 ist zum Stillstand gekommen.
- **Momentum:** Die Vorzeichen sind gemischt.
- **Gewicht 0,4:** nahe der Mitte, mit leichtem Abschlag wegen des fallenden Durchschnitts.
- **Umdenken:** Wochenschlüsse über 109,5 sprechen für 0,55. Unter 95 spricht für 0,25.

### 15e1d69cae (BTC)
- **Lage:** Der Kurs liegt 6 % unter dem SMA100. Seit dem Bruch gab es keine Rückkreuzung (1 Kreuzung). ER 0,22.
- **Struktur:** Die Tiefs steigen: 89 → 94,5 → 97,5. Das Hoch liegt bei 102,4.
- **Momentum:** z_4W +0,9 gegen z_8W −0,8. Das ist ein Widerspruch.
- **Gewicht 0,4**
- **Umdenken:** Ein gehaltener Wochenschluss über 102,5 bzw. über dem SMA100 (etwa 106,5) spricht für 0,55. Unter 94,5 spricht für 0,25.

### e123d90fdc (ETH)
- **Lage:** Der Kurs liegt am fallenden SMA100 (−0,4 %). ER 0,39, das ist die beste Güte im Satz.
- **Struktur:** Erholung von 77 auf 100 mit steigenden Tiefs (78 → 87,7 → 94,5). Heute ein knappes neues Hoch bei 100,6.
- **Momentum:** z_4W +1,6, z_8W −0,1. Die langen Fenster bestätigen noch nicht, und der SMA fällt weiter.
- **Gewicht 0,5:** mittleres Gewicht, kein Sprung.
- **Umdenken:** Mehrere Wochenschlüsse über 102 mit abflachendem SMA sprechen für 0,65. Unter 94 spricht für 0,3.

### ee28ae3639 (DOGE)
- **Lage:** Der Kurs liegt 18 % unter dem fallenden SMA100. ER 0,07, z_8W −1,4.
- **Struktur:** Seitwärts zwischen 93 und 108. Der Rücksetzer auf 93,2 an Tag −3 wurde wieder aufgeholt, ist aber ohne Bedeutung.
- **Gewicht 0,25:** Abwärtsregime, stillhalten.
- **Umdenken:** Wochenschlüsse über 108 sprechen für 0,4. Unter 93 bleibt es reduziert.

### b880ed00a5 (ADA)
- **Lage:** Der Kurs liegt 19 % unter dem SMA100, der in 20 Tagen um 7,4 % gefallen ist.
- **Struktur:** Der Spike auf 120 (−22) ist vollständig gescheitert, danach läuft der Kurs seitwärts zwischen 94 und 109. ER 0,14.
- **Gewicht 0,25**
- **Umdenken:** Wochenschlüsse über 109 sprechen für 0,4. Unter 94 bleibt es bei 0,25.

### 89ad278a82 (AVAX)
- **Lage:** ER 0,03 und 8 Kreuzungen, also reines Rauschen. Der Kurs liegt 14 % unter dem fallenden SMA100.
- **Struktur:** Spanne 84–105. Die Tageskerze bei −1 (+7,6 %) ist ein Tagesextrem und zählt nicht.
- **Gewicht 0,25**
- **Umdenken:** Wochenschlüsse über 105,5 sprechen für 0,4. Unter 91 bleibt es reduziert.

### e968d21d8c (LINK)
- **Lage:** Der Kurs liegt 1,7 % über einem leicht fallenden SMA100. ER 0,34.
- **Struktur:** Erholung von 79 auf 100 mit steigenden Tiefs (79,4 → 85 → 93,7). Heute ein Schluss am Hoch der Erholung.
- **Momentum:** z_2W +1,0 und z_4W +1,5, aber z_8W −0,2. Die Bestätigung durch das lange Fenster fehlt.
- **Gewicht 0,5**
- **Umdenken:** Wochenschlüsse über 102 bei flach werdendem oder steigendem SMA100 sprechen für 0,65. Unter 93,7 spricht für 0,3.

```json
{"91b9b0398c (XRP)": 0.3, "b08cc8b5d8 (LTC)": 0.45, "e4d1a405e7 (DOT)": 0.25, "4ea7b90132 (SOL)": 0.4, "15e1d69cae (BTC)": 0.4, "e123d90fdc (ETH)": 0.5, "ee28ae3639 (DOGE)": 0.25, "b880ed00a5 (ADA)": 0.25, "89ad278a82 (AVAX)": 0.25, "e968d21d8c (LINK)": 0.5}
```

## Entscheidung 2026-08-02

## Strategy
I start from a neutral weight of about 0.45. I cut to about 0.2 only when two things hold together: the 2-, 4- and 8-week momentum all point down with |z_4W| ≥ 0.5, and price sits clearly below a falling SMA100 with lower highs. Mixed momentum or a sideways range (low ER) means I hold near the middle. A single daily spike or the position within the range never raises the weight.

## 1bb562fa14 (LINK)
- **Read:** Sideways. Momentum is slightly positive but weak (z_4W 0.3) and ER is 0.09. Price is just below a mildly falling SMA100, which it has crossed 3 times. Since the low at about 84 (day −38) it has recovered into a 94–105 range. Higher lows at 94 and 96, but no breakout.
- **Weight:** 0.45. There is no signal, so I stay neutral.
- **Change mind:**
  - Weekly close below 94: lower the weight.
  - Weekly close above 106 while the SMA flattens: raise it.

## 1b681943d9 (BTC)
- **Read:** Flat. All z are about 0 and ER is 0.04. Price is 7.6% below a falling SMA100. It has traded in a tight 98–105 range for 4 weeks, above the 91 low.
- **Weight:** 0.4. This is a sideways regime with a mild downward tilt from the long average.
- **Change mind:** Weekly close below 97 (lower) or above 106 (higher).

## 24e3eba290 (DOT)
- **Read:** Downtrend. Momentum is negative across all windows (z_8W −0.9, z_4W −0.6). Price is 22% below an SMA100 that is falling steeply. Lower highs at 131, 112, 109 and 104; a fresh low at 93 on day −6. Today's bounce to 100 stays under the falling averages.
- **Weight:** 0.2. Confirmed downtrend state.
- **Change mind:** Weekly close above about 110 (prior lower high) would end the downtrend read.

## 67aa239fca (SOL)
- **Read:** Mixed. 8W momentum is positive (rebound from 82 to 114), but the 2W and 4W are negative. Highs have been lower since then: 114, 107, 105. Volatility is compressed (σ ratio 0.71), which signals a coming move but not its direction. Price is 6% below a falling SMA100.
- **Weight:** 0.4. Long and short momentum disagree, so I stay toward the middle.
- **Change mind:**
  - Weekly close below 96: about 0.25.
  - Above 107: about 0.5.

## 924ed13b67 (XRP)
- **Read:** Mild downtrend. All z are negative and z_4W is −0.5, right at the threshold. Price is 10.7% below a falling SMA100. Lower highs at 119, 109 and 107; lows near 93–96.
- **Weight:** 0.3. A weak but aligned negative state justifies a partial reduction.
- **Change mind:**
  - Weekly close below 95: 0.2.
  - Above 107: back to 0.45.

## 04d7ed9a42 (ETH)
- **Read:** Improving structure. Since the 80 low, lows have been rising (91, 95.6, 96.6) and highs too (98, 103, 105). All z are positive, but z_4W at 0.4 is below the trend threshold. Price is only 2.4% below a still-falling SMA100.
- **Weight:** 0.5. Higher lows support holding near neutral-plus, but this is not a confirmed trend.
- **Change mind:**
  - Weekly close below 96: 0.35.
  - Weekly close above 105.5 with the SMA flattening: 0.65.

## 1350eac60b (AVAX)
- **Read:** Choppy range, roughly 94–106 since day −40. Momentum signs are mixed and ER is 0.09. Price is 14.5% below a falling SMA100. Today's +5.8% candle on volume is a single day and does not count as a signal.
- **Weight:** 0.35. A sideways regime under a long-term downtrend.
- **Change mind:**
  - Weekly close above 106: 0.5.
  - Below 92: 0.2.

## db7c08df55 (LTC)
- **Read:** Sideways. ER is 0.01 and momentum signs are mixed (2W −0.6, 8W +0.3). Price is in a 97–108 range and 7.9% below a falling SMA100.
- **Weight:** 0.4. No trend state.
- **Change mind:** Weekly close below 96 (lower) or above 108 (higher).

## e58b0185d2 (ADA)
- **Read:** After the crash to 73, price spent three weeks basing between 82 and 95. Today it jumped 8.7% to 100 on high volume, which is a single-day extreme. Momentum signs are mixed (z_4W 0.0). The SMA100 is falling sharply (−7.6%), and the prior rebound high is at 105.5.
- **Weight:** 0.4. A daily extreme is not a reason to add, and the weekly trend is unconfirmed.
- **Change mind:**
  - Weekly close above 105.5 that holds: 0.55.
  - Close back below 85: 0.25.

## de57b1b271 (DOGE)
- **Read:** Downtrend. All z are negative (8W −1.0, 4W −0.7) and ER is 0.21. Price is 19.7% below a falling SMA100. Lower highs at 125, 112, 106.5 and 104.6.
- **Weight:** 0.2. Confirmed negative state.
- **Change mind:** Weekly close above about 110.

{"1bb562fa14 (LINK)": 0.45, "1b681943d9 (BTC)": 0.4, "24e3eba290 (DOT)": 0.2, "67aa239fca (SOL)": 0.4, "924ed13b67 (XRP)": 0.3, "04d7ed9a42 (ETH)": 0.5, "1350eac60b (AVAX)": 0.35, "db7c08df55 (LTC)": 0.4, "e58b0185d2 (ADA)": 0.4, "de57b1b271 (DOGE)": 0.2}

## Entscheidung 2026-08-09

**Strategy:** The weekly regime sets the direction, and volatility sets the size. A long average that is falling, combined with lower highs and negative 4–8-week momentum, justifies a reduced weight. Sideways markets with a low ER and mixed momentum stay near a middle weight of about 0.4. Only aligned positive momentum with higher lows justifies a mid weight. Position in the range, single days and indicator distances are not signals.

## 9b0ab58dab (LINK)
- **Read:** The crash around day −65 bottomed at 85.5. Since then price has moved sideways between about 96 and 108, and has spent the last four weeks pinned at 99–103.
- **Trend:** Price is 4% below a falling SMA100. ER is 0.05 and momentum is mixed, so this is a sideways regime inside a weak downtrend.
- **Weight: 0.40.** There is no confirmed trend, so I hold slightly below the middle because the long average is falling.
- **Change my mind:** Weekly closes above 108 would raise the weight. A close below 96 would lower it.

## 06492ae620 (LTC)
- **Read:** The low was 86.5 at day −46. The recovery peaked at 105.3, and price now sits in a 96–105 range.
- **Trend:** Price is 4.9% below a falling SMA100, and momentum is flat.
- **Weight: 0.40.** This is sideways, so there is nothing to act on.
- **Change my mind:** Weekly closes above 106 would raise the weight. A close below 96 would lower it.

## 85be2e980d (AVAX)
- **Read:** Price crashed from about 140 to 88.5. Since then it has ranged between 95 and 110 for seven weeks.
- **Trend:** Price is 14% below an SMA100 that is falling steeply (−7% in 20 days). That makes this a downtrend regime. Within the range, the action is noise.
- **Weight: 0.30.**
- **Change my mind:** A weekly close above 111 would raise the weight. A close below 94 would lower it.

## c55197cb4b (DOT)
- **Read:** Highs keep falling: 131, then 113.6, then 108.9. Lows fall too: 100.6, then 93.6.
- **Trend:** Price is 20% below a falling SMA100, and z_8W is −1.1. The downtrend is intact.
- **Weight: 0.20.** Damage control.
- **Change my mind:** A weekly close above 112 would end the lower-highs pattern and raise the weight. A close below 93.5 would confirm the downtrend and lower it.

## e73641fde5 (DOGE)
- **Read:** This is a steady grind lower. Highs: 133, 114.5, 108.7, 103.2. Lows: 103, 100.2, 97.6.
- **Trend:** Price is 19% below a falling SMA100, and z_8W is −1.5.
- **Weight: 0.20.**
- **Change my mind:** A close above 108 would raise the weight. A close below 97.5 would lower it.

## a68203feed (SOL)
- **Read:** Price crashed to 78.8, rebounded to 110, then drifted down to 92.5 and back to 100.
- **Trend:** Price is 2% below a falling SMA100. There were 5 crossings in 90 days and ER is 0.06, so this is chop.
- **Volatility:** Compressed (σ ratio 0.67). That tells me nothing about direction.
- **Weight: 0.45.**
- **Change my mind:** Held weekly closes above 110 would raise the weight. A close below 92 would lower it.

## e0bb40f206 (XRP)
- **Read:** Highs are falling (125.6, 115, 113.1, 106.2) while lows sit flat at about 98. That is a descending triangle.
- **Trend:** Price is 13.7% below a falling SMA100. z_2W is −1.0 and z_8W is −0.9.
- **Weight: 0.25.**
- **Change my mind:** A close below 98 would cut the weight toward 0.1. A close above 113 would raise it.

## ed3623b79c (BTC)
- **Read:** Price has been very flat at 96–103 for six weeks. The low was 89.5 at day −45.
- **Trend:** Price is 4.4% below a falling SMA100, ER is 0.04 and volatility is compressed.
- **Weight: 0.40.**
- **Change my mind:** A held breakout above 104 would raise the weight. A close below 96 would lower it.

## 60c1ba4ec3 (ADA)
- **Read:** The low was 71. A spike to 102.8 failed, then a higher low formed at 78.8 (day −12). The last rally reached 108.8, closed briefly at about 103 and is now back at 100.
- **Momentum:** Positive across 2, 4 and 8 weeks (+1.3, +1.1, +0.2), but the 8-week reading is weak.
- **Trend:** The SMA100 is still falling (−6.7%), so long and short momentum disagree.
- **Weight: 0.50.** The conflict points to a middle weight, not a jump to an extreme.
- **Change my mind:** A weekly close above 105 would take the weight to about 0.65. A close below 92 would take it to about 0.3.

## f035a7a477 (ETH)
- **Read:** Lows keep rising: 79.1, 89.7, 94.4, 95.4. Price has stalled below 103.7, and the current range is 95–104.
- **Trend:** Price is at a falling SMA100. Momentum is mixed (z_4W +0.5, z_8W +0.7, z_2W −0.3).
- **Weight: 0.50.**
- **Change my mind:** A weekly close above 104 would raise the weight to about 0.65. A close below 95 would lower it to about 0.35.

{"9b0ab58dab (LINK)": 0.4, "06492ae620 (LTC)": 0.4, "85be2e980d (AVAX)": 0.3, "c55197cb4b (DOT)": 0.2, "e73641fde5 (DOGE)": 0.2, "a68203feed (SOL)": 0.45, "e0bb40f206 (XRP)": 0.25, "ed3623b79c (BTC)": 0.4, "60c1ba4ec3 (ADA)": 0.5, "f035a7a477 (ETH)": 0.5}

## Entscheidung 2026-08-16

**Strategy:** The starting weight is a neutral 0.4–0.5. I lower it to about 0.15–0.25 only when two things hold together: the 2/4/8-week momentum is negative (with |z_4W| > 0.5), and the price has spent several weekly closes below a falling SMA100. I raise it only when momentum is positive and aligned across those windows. In sideways regimes (ER < 0.1, mixed momentum signs, the price swinging inside a range), the weight stays near the middle no matter where the price sits in the range. Compressed volatility (σ20/σ90 < 1) gives no direction in any window, so I never cut size for volatility here.

## 705af8863e (DOGE)
- **Trend:** A clear downtrend from about 165 (day −94) to 100. The close is 16% below a steeply falling SMA100, and the 2/4/8-week momentum is all negative.
- **Last month:** A narrow band around 99–105 with ER 0.11, so the trend has paused but not turned. Momentum confirmation is weak (|z_4W| 0.4).
- **Regime:** The rule "several weekly closes below a falling long average" applies, so this is a downtrend regime. Volatility is compressed, which says nothing about direction.
- **Weight: 0.25.**
- **Change of mind:** Weekly closes above about 106.5 (the top of the band) → 0.4. Below 97 confirms the downtrend continuing.

## f2738596cd (LINK)
- **Momentum:** Positive across all windows (z_4W +1.0), so this counts as a trend state.
- **Structure:** Since the low at 74.5 (day −72), the higher lows run 76.7 → 84 → 85.9. The close at 100 breaks above the 4-week band of about 85–95.
- **Caveats:**
  - The SMA100 is still falling slightly.
  - There were 4 crossings in 90 days.
  - The last day was a single large candle (+5.6%).
  - Together these argue against a full position.
- **Resistance:** The zone of 104–115 from days −100 to −94.
- **Weight: 0.6.**
- **Change of mind:** A weekly close below about 92 means the breakout has failed → 0.4.

## fea1da2a4f (SOL)
- **Regime:** ER 0.02, momentum near zero with mixed signs, 4 crossings of the SMA100. This is a textbook sideways market.
- **Range:** About 97–106. The SMA100 is falling only gently.
- **Weight: 0.4.**
- **Change of mind:** A weekly close above about 106 → up; below 95 → about 0.25.

## e0340bd21c (XRP)
- **Momentum:** Negative and aligned (2W −1.3, 4W −1.0, 8W −0.9).
- **Price vs. average:** 14.7% below a falling SMA100, with no crossings at all in 90 days.
- **Structure:** Clean lower highs: 119.2 → 117.2 → 112.8 → 110 → 105.6, ending around 100.
- **Regime:** This is the unfavourable combination of a downtrend with no sign of a turn.
- **Weight: 0.15.**
- **Change of mind:** Weekly closes above about 110 (the last significant swing high), together with a higher low.

## 68af4e240b (ETH)
- **Price vs. average:** Exactly at the SMA100, which is falling, with 3 crossings.
- **Regime:** ER 0.05, momentum near zero. Sideways between about 97 and 105 after the recovery from 80.
- **Weight: 0.4.**
- **Change of mind:** Above 105 on a weekly close → 0.55. Below 96 → 0.25.

## f6568b8c66 (LTC)
- **Price vs. average:** 6% below a falling SMA100, with 0 crossings.
- **Momentum:** All negative (z_4W −0.7).
- **Regime:** ER 0.07 is low, so the trend is weak.
- **Recent action:** The rebound to 108.5 (day −28) failed and the price is drifting back to 100. Support sits at about 98.
- **Weight: 0.3.**
- **Change of mind:** A close above about 109 → 0.45. Below 97 → 0.2.

## cfb45acdaa (BTC)
- **Price vs. average:** 5.8% below a falling SMA100.
- **Momentum:** Weak and negative (z_4W −0.4).
- **Regime:** ER 0.06, sideways between 99 and 106 for 6 weeks.
- **Weight: 0.35.**
- **Change of mind:** Above 106.5 → 0.5. Below 98 → 0.2.

## 32caddde3c (DOT)
- **Price vs. average:** 21% below a steeply falling SMA100 (−8.8% in 20 days), with no crossings.
- **Momentum:** Negative and aligned (z_4W −0.6).
- **Structure:** Lower highs: 137.9 → 119.6 → 117.9 → 114.6. The latest rebound to 114.6 has been fully given back.
- **Weight: 0.15.**
- **Change of mind:** Weekly closes above about 115 (the last lower high).

## 865dfd1522 (ADA)
- **Momentum:** Contradictory: 2W −0.6, but 4W +0.3 and 8W +0.5. A turning point is possible, so the weight goes to the middle without a full flip.
- **Recent action:** A spike to 121 (day −10) was fully given back.
- **Price vs. average:** 8% below a falling SMA100.
- **Regime:** ER 0.07.
- **Weight: 0.35.**
- **Change of mind:** Above 116 → 0.5. Below about 88 (the swing low on day −20) → 0.15.

## 7008f8318d (AVAX)
- **Regime:** Sideways between 97 and 110 for 2 months. ER 0.08, mixed momentum, many crossings.
- **Price vs. average:** Below a falling SMA100.
- **Recent action:** The last day pushed up to 108.6 and was rejected. That is a single wick and is not informative.
- **Weight: 0.35.**
- **Change of mind:** A weekly close above 111 → 0.5. Below 95 → 0.2.

{"705af8863e (DOGE)": 0.25, "f2738596cd (LINK)": 0.6, "fea1da2a4f (SOL)": 0.4, "e0340bd21c (XRP)": 0.15, "68af4e240b (ETH)": 0.4, "f6568b8c66 (LTC)": 0.3, "cfb45acdaa (BTC)": 0.35, "32caddde3c (DOT)": 0.15, "865dfd1522 (ADA)": 0.35, "7008f8318d (AVAX)": 0.35}

## Entscheidung 2026-08-23

# Analysis

## 1. Strategy

All ten windows show the same pattern. There was a crash about 80 days ago, then a quiet drift, then a vertical 3–4 day spike that ended with a long upper wick on day −1. My rule:

- **Base weight is the mid (0.5).** The spike is one extreme week. The longer windows only partly confirm it, and the SMA100 is still falling. So the spike is a reversal candidate, not a trend state.
- **I don't add weight because the price rose.** Volatility expansion and a rejected wick at the top of the 180-day range push the weight down.
- **Only a held close above the multi-month range top counts as a confirmed breakout.** A close back inside the pre-spike base counts as failure.

## 2. Windows

**fa597abcfb (LINK)**
- **Read:** Price broke out of a 4-month range (old highs 91–94). Day −1 wicked to 109 and closed near 101. Momentum is aligned (2W, 4W and 8W all positive, 8W +2.6). The SMA100 is only slightly falling but has been crossed 4 times.
- **Weight:** 0.5. A new 180-day high on closing basis with volume is the strongest breakout in the set. The spike is still unconfirmed and the wick weighs against it.
- **Change my mind:** a close below 92 means the breakout failed (go to 0.3). Holding above 104 for a week would support a higher weight.

**cf60b907c5 (LTC)**
- **Read:** Price is still inside the broad 180-day range (highs 113–116). It is retesting the 97–100 breakdown zone from day −82. ER is low (0.27), z_4W is only +0.8, and the SMA100 is falling 4.3%.
- **Weight:** 0.4. This is a rally in a falling regime that has reached old resistance.
- **Change my mind:** below 90 → 0.25. Weekly closes above 106 → reconsider upward.

**147740b86f (ADA)**
- **Read:** A spike wick to 113.8 was rejected. Price is far below the old range (110–127). The SMA100 is falling 6.7%, and there are 3 SMA crossings in 90 days.
- **Weight:** 0.4. This looks like a rebound in a downtrend.
- **Change my mind:** below 85 → 0.25. Holding above 110 → upward.

**4ff9b9a966 (DOGE)**
- **Read:** z_2W is extreme (+3.4) and only weakly backed by z_8W (+1.4). The SMA100 is falling 7.8%, and old highs at 120–127 are far away. There was heavy volume on the wick day.
- **Weight:** 0.35.
- **Change my mind:** below 88 → 0.2. Weekly close above 108 → upward.

**ae9dc13fdd (BTC)**
- **Read:** This is the cleanest spike: little wick, and day −1 was a calm consolidation. ER is 0.48 and 8W momentum is positive. Price sits just under the old range top of 105–107.
- **Weight:** 0.5.
- **Change my mind:** a held close above 107 → 0.65. Below 92 → 0.3.

**bc79b9fb4e (AVAX)**
- **Read:** ER is low (0.28) and z_4W/z_8W are only +0.8. The SMA100 is falling 7.5%, and old highs at 130–138 are far away. The day −1 wick to 109 was rejected.
- **Weight:** 0.35.
- **Change my mind:** below 88 → 0.2. Above 110 held → upward.

**12b3af3acd (XRP)**
- **Read:** Price jumped from 66 to 100 in 4 days on huge volume, and σ20/σ90 is 1.53, which is high volatility. A wick to 111.8 went above the 180-day high (105.7) and closed back at 96. That is a weak failed-breakout signal at the range extreme.
- **Weight:** 0.3. Volatility cuts the position size.
- **Change my mind:** a close above 106 held → 0.5. Below 85 → 0.15.

**f041778259 (ETH)**
- **Read:** Price is at the 180-day range top (98–100). Day −2 closed at 102 and was not held. σ20/σ90 is 1.29, and 8W momentum is positive.
- **Weight:** 0.45. The breakout is unconfirmed.
- **Change my mind:** above 104 held → 0.6. Below 90 → 0.3.

**b20ef1ebeb (DOT)**
- **Read:** This is a long downtrend from 180. Price is sitting right at the SMA100, which is falling 9.2%. ER is 0.22.
- **Weight:** 0.3. This is a rally to falling resistance.
- **Change my mind:** below 88 → 0.15. Weekly closes above 112 → upward.

**a42c10561f (SOL)**
- **Read:** A wick to 107.7 above the old highs (102–103) closed back at 98. ER is 0.53 and volatility is normal (σ20/σ90 0.96). Momentum is positive but the breakout has not held.
- **Weight:** 0.45.
- **Change my mind:** above 104 held → 0.6. Below 90 → 0.3.

## 3. Weights

{"fa597abcfb (LINK)": 0.5, "cf60b907c5 (LTC)": 0.4, "147740b86f (ADA)": 0.4, "4ff9b9a966 (DOGE)": 0.35, "ae9dc13fdd (BTC)": 0.5, "bc79b9fb4e (AVAX)": 0.35, "12b3af3acd (XRP)": 0.3, "f041778259 (ETH)": 0.45, "b20ef1ebeb (DOT)": 0.3, "a42c10561f (SOL)": 0.45}

## Entscheidung 2026-08-30

**Strategy:** The weekly state comes first. A trend state needs 2W, 4W and 8W momentum to share a sign with |z_4W| > 0.5, plus decent trend quality (ER ≥ ~0.3) and a long average that is not falling. Only then does the weight go clearly above the midpoint (~0.5). Where the long average is falling, ER is low, or a spike has already faded, the weight sits at or below the midpoint, and high σ20/σ90 trims the size. Every window here has the same recent shape: a sharp 3-day spike around day −10 to −8 that has since given back part of its gain. I treat that spike as momentum only where it caps an orderly, already-rising base.

### 18c8172d44 (LTC)
- **Read:** The range was 107–126 before the crash at day −89 to −86 took price to ~85. Recovery stalled in a flat 91–96 base. The spike reached 115.7 intraday (closing high 110.9) and has faded back to 100.
- **Momentum and regime:** 8W momentum is weak (+0.3), ER(30) is low at 0.17, and SMA100 is falling. That is not a trend state, and the faded spike reads more as a test than a breakout.
- **Weight: 0.40.** Close to the middle, slightly lower because of the falling long average.
- **Change mind:** A weekly close below 91 (back inside the old base) → 0.2. A weekly close above 111 → 0.5.

### dbe2a29433 (DOGE)
- **Read:** Price peaked at 140 (day −117), crashed, then based quietly at 84–90 for about 50 days. The spike hit a 122.9 wick and has faded to 100.
- **Breakout status:** Price is still above the base top (~91), so the breakout is technically holding. Against that, SMA100 is falling hard (−6.8% in 20 days), ER(30) is 0.23, z_8W is only +0.2, and σ20/σ90 is high at 1.45.
- **Weight: 0.40.**
- **Change mind:** A close below 92 means the breakout failed → 0.2. Weekly closes above 112 → 0.55.

### 03d0476306 (LINK)
- **Read:** Price bottomed at 63, then built higher lows: 65 → 70 → 73. It climbed steadily from day −19 and spiked to 107.6. It is now consolidating at 99–107.
- **Momentum and regime:** 2W/4W/8W are all positive (z_4W 2.0, z_8W 1.7), ER(30) is 0.40, and SMA100 is rising. This is a real trend state. Volatility is moderately elevated (1.32), which caps the size.
- **Weight: 0.65.**
- **Change mind:** A weekly close below 95 (under the consolidation and the −10 gap area) → 0.45.

### e355e5e90f (SOL)
- **Read:** A steady rise from 70 to 107.3, which took out the 180-day high near 96. Price is now holding about 100.
- **Momentum and regime:** Momentum is confirmed on every window (z 3.6 / 2.7 / 1.2), ER(30) is 0.47, and σ20/σ90 is near normal at 1.17. This is the cleanest trend in the set. The extreme 2W z suggests a pause, but the longer windows confirm it, so it is not a reversal signal.
- **Weight: 0.70.**
- **Change mind:** A weekly close below 92 (back under the old 96 high and the gap zone) → 0.45.

### 70afa2d237 (ADA)
- **Read:** The range was 120–150, then a crash to 72. Since then there have been repeated failed spikes: 104 at day −57, 109.9 at day −24, and a 134 wick at day −8. Each one faded.
- **Momentum and regime:** ER(30) is 0.15, z_4W is +0.1, there have been 3 SMA crossings, and SMA100 is falling. This is a choppy regime, and the bull spikes keep failing.
- **Weight: 0.30.**
- **Change mind:** A weekly close above 111 that then holds → 0.5. Below 88 → 0.15.

### 621e946976 (ETH)
- **Read:** Higher lows from 63 to 79, then a gap-up to 104. Price has held 99–106 for a week, and the prior range high is ~102.
- **Momentum and regime:** Momentum is aligned (z 2.6 / 1.8 / 1.6) and ER(30) is 0.44. SMA100 is essentially flat (−0.3%).
- **Weight: 0.60.**
- **Change mind:** A weekly close below 93 → 0.4.

### 71b112b0a0 (BTC)
- **Read:** An orderly climb from 77 to 100, followed by a tight hold at 99–104. The prior high was 106.7.
- **Momentum and regime:** Momentum is aligned (z 3.2 / 2.2 / 1.5) and ER(30) is 0.51, the best trend quality in the set. SMA100 is still falling slightly (−2.2%), which keeps me below full size.
- **Weight: 0.65.**
- **Change mind:** A weekly close below 95 → 0.45. A weekly close above 107 → hold, do not add.

### 9995dec536 (AVAX)
- **Read:** The range was 120–147, then a crash, then a two-month range of 83–98. The spike reached 116.9 and faded back to just above the range top.
- **Momentum and regime:** z_8W is +0.1, ER(30) is 0.16, and SMA100 is falling steeply (−6.9%). This is a sideways or down regime.
- **Weight: 0.35.**
- **Change mind:** Below 94 → 0.2. A weekly close above 108 → 0.5.

### abf48293ed (DOT)
- **Read:** A persistent downtrend from 200 to 92, with lower highs throughout. Price closes 9% below a falling SMA100. The spike to 126 faded fully.
- **Momentum and regime:** z_8W is negative and ER(30) is 0.10. The falling SMA100 sits overhead as resistance.
- **Weight: 0.15.**
- **Change mind:** Weekly closes above 115 with SMA100 flattening → 0.35.

### dd73e5c30f (XRP)
- **Read:** A grinding downtrend from 108 to 73, then a blow-off spike on very high volume (125 wick, 6× average). Price has faded to 100.
- **Momentum and regime:** 8W momentum is weak (+0.7), SMA100 is falling, and volatility is clearly elevated at 1.59. A single shock with no prior base is fragile, and the high volatility argues for a smaller size.
- **Weight: 0.35.**
- **Change mind:** Below 95 → 0.2. A weekly close above 112 → 0.5.

{"18c8172d44 (LTC)": 0.4, "dbe2a29433 (DOGE)": 0.4, "03d0476306 (LINK)": 0.65, "e355e5e90f (SOL)": 0.7, "70afa2d237 (ADA)": 0.3, "621e946976 (ETH)": 0.6, "71b112b0a0 (BTC)": 0.65, "9995dec536 (AVAX)": 0.35, "abf48293ed (DOT)": 0.15, "dd73e5c30f (XRP)": 0.35}

## Entscheidung 2026-09-06

## Strategy

I go long by trend state, not by where the price sits in its range. If the 2-, 4- and 8-week returns all have the same sign and z_4W is above 0.5, I set the weight above 0.5. If the signs disagree, or ER is low, the weight stays near the middle (0.4–0.5). When σ20/σ90 is above 1.5, or the SMA100 is still falling, I trim the size, because high volatility and an unconfirmed regime limit the dose regardless of direction.

All ten windows have the same shape: a crash around day −93, a base, a spike at days −17/−15, a consolidation, and now a retest of the spike high. That shape is one finding. What separates the windows is the quality of the trend in each.

## b61d94f669 (DOGE)
- **Read:** The 2-week return is negative (−0.2) while the 4- and 8-week returns are positive, so the momentum signs disagree. σ20/σ90 is high at 1.65. The SMA100 is falling (−5%).
  - Price is back at 100, below the spike high of 110.9 and the old resistance zone at 120–130.
  - Support is at about 88–90.
- **Weight:** 0.4. Mixed momentum with high volatility means a middle weight, slightly reduced.
- **Change of view:** Weekly closes above 105 would raise it; a close below 88 would lower it.

## c13033d5c4 (ETH)
- **Read:** All momentum signs are positive. ER is 0.41 and the SMA100 is rising.
  - The consolidation held between 94 and 102 after the breakout.
  - Volatility is high at 1.58.
- **Weight:** 0.6. It is a trend state, trimmed for volatility.
- **Change of view:** A close below 93.7 (the consolidation low) would break the trend.

## 776385078d (AVAX)
- **Read:** All momentum signs are positive and volatility is normal (1.16). The SMA100 is falling, so the long regime is not confirmed.
  - The last close is a new swing high, above the spike close of 99.1. The intraday high was 105.2.
  - Support is at 88.7–89.
- **Weight:** 0.55.
- **Change of view:** A close above 105 would raise it; a close below 88.7 would lower it.

## 392d0fd33b (BTC)
- **Read:** All momentum signs are positive and ER is 0.44.
  - The consolidation is tight (95–101) and sits above the breakout.
  - The SMA100 is flat and volatility is 1.47.
- **Weight:** 0.6.
- **Change of view:** A close below 94.9 would lower it.

## d5507c4cc2 (DOT)
- **Read:** The momentum signs are positive, but z_8W is only 0.7 and ER is low at 0.25. The SMA100 is falling sharply (−8.5%) and price crossed it 3 times in 90 days.
  - Price closed at 100 on a large day, slightly below the spike high of 105.4.
- **Weight:** 0.45. Trend quality is too weak for more than a middle weight.
- **Change of view:** A weekly close above 105.4 would raise it; a close below 82.5 would lower it.

## c0125f60bb (LTC)
- **Read:** All momentum signs are positive and ER is 0.34. Volatility is high at 1.52 and the SMA100 is falling slightly.
  - Price is back at the spike high of about 100.9.
  - The support zone is at 86–87.
- **Weight:** 0.55.
- **Change of view:** A close below 86 would lower it.

## ddf2d62da4 (XRP)
- **Read:** z_2W is negative, so the momentum signs disagree. Volatility is the highest of the set at 1.71.
  - The spike went up to 119.4 on extreme volume and was rejected.
  - Price is now at 100 inside the range of 92 to 107.
- **Weight:** 0.4.
- **Change of view:** A close above 107 would raise it; a close below 92 would lower it.

## 6e25c2a026 (SOL)
- **Read:** All momentum signs are positive (z_4W +2.8). ER is 0.47, the SMA100 is rising, and volatility is moderate at 1.37.
  - The breakout made higher lows: 91.4 and then 93.1.
  - The high is at 103.8.
- **Weight:** 0.7. This is the clearest trend state in the set.
- **Change of view:** A close below 91.4 would lower it.

## e9f99c53e1 (LINK)
- **Read:** This has the strongest momentum (z_4W +3.6) and the highest ER (0.52). The SMA100 is rising.
  - The last close is a new high at 100, but the last day alone was +9.9%, an extreme day that I do not add on.
  - Volatility is 1.51.
- **Weight:** 0.7. It is a trend state, held at the upper middle rather than chasing the move.
- **Change of view:** A close below 82.4 would lower it.

## e3a50d7bbd (ADA)
- **Read:** ER is very low at 0.12 and z_2W is negative. The SMA100 is falling and price crossed it 3 times.
  - There are repeated spikes that fade back: up to 89.5 and then 94.8 earlier, and 115.7 now.
- **Weight:** 0.4. This is a choppy regime, so the weight stays in the middle.
- **Change of view:** A close above 102 held for a week would raise it; a close below 85 would lower it.

{"b61d94f669 (DOGE)": 0.4, "c13033d5c4 (ETH)": 0.6, "776385078d (AVAX)": 0.55, "392d0fd33b (BTC)": 0.6, "d5507c4cc2 (DOT)": 0.45, "c0125f60bb (LTC)": 0.55, "ddf2d62da4 (XRP)": 0.4, "6e25c2a026 (SOL)": 0.7, "e9f99c53e1 (LINK)": 0.7, "e3a50d7bbd (ADA)": 0.4}

## Entscheidung 2026-09-13

**Strategy:** The base weight is a neutral 0.5. I raise it to about 0.6–0.65 only when there is a trend state: 2-, 4- and 8-week momentum share a sign, |z_4W| is above 0.5, SMA100 is rising and ER is at least about 0.3. A falling SMA100 with low ER means a sideways or downward regime, so the weight stays at the middle or slightly below. If σ20/σ90 is above 1.5, or a single extreme week has already reversed, I cut the size.

All ten windows look alike. Each had a crash around day −100, a breakout spike at days −25 to −22, and a consolidation since. Spike, momentum and range position are therefore one finding, counted once.

## 128e68e63d (ADA)
- **Read:** The long trend is down from 142, and SMA100 is falling. ER of 0.13 is low and there were 3 crossings, which points to a sideways or bearish regime. The spike to 127 was a wick. The latest high was 114, and the price has slipped from 110 to 100. Momentum is positive but weak (z_4W 0.8) and gets no confirmation from trend quality.
- **Weight:** 0.45.
- **Change my mind:** Weekly closes below 94 → 0.3. Weekly closes above 112 → 0.55.

## 24d5b92805 (SOL)
- **Read:** SMA100 is rising (+5.6%), ER is 0.30, and the structure is HH/HL since the low of 61. z_2W is −0.2, so this is a correction inside an uptrend, not a clean trend state. Support is at 98–99; the high is 111.4.
- **Weight:** 0.55, hold.
- **Change my mind:** A close below 95 (the last HL) → 0.4. A weekly close above 111 → 0.65.

## 206990aa98 (ETH)
- **Read:** All momentum signs are positive (z_4W 2.1), ER is 0.37, and σ20/σ90 is a calm 0.73. SMA100 is rising. The price is in a tight range of 95–103 above the breakout base at 77. This is a valid trend state.
- **Weight:** 0.65.
- **Change my mind:** A close below 95 → 0.5.

## ec31f95bed (AVAX)
- **Read:** SMA100 is falling (−3.9%) and ER is 0.15. The price is still well below the earlier range of 125–140. Momentum is positive but carries no quality. The recent high is 112.5 and the drop back to 100 ends in lower-high tendencies.
- **Weight:** 0.45.
- **Change my mind:** A close below 96 → 0.35. A weekly close above 112.5 → 0.55.

## 5cc037fe49 (DOGE)
- **Read:** SMA100 is falling, ER is 0.17, σ20/σ90 is 1.17, and z_2W is 0. The spike reached 122 as a wick, and the second attempt at 115 also failed. This is sideways with weak momentum.
- **Weight:** 0.45.
- **Change my mind:** A close below 97 → 0.35. A weekly close above 111 → 0.55.

## bdd6157ddf (LINK)
- **Read:** SMA100 is rising (+6.1%), but ER is only 0.21, σ20/σ90 is 1.21 and z_2W is 0. The push to 122 on day −6 was given back entirely, so the breakout did not hold. Support is at 98–100.
- **Weight:** 0.5, neutral.
- **Change my mind:** A close below 97 → 0.4. A weekly close above 110 → 0.6.

## b3ead30579 (DOT)
- **Read:** The long downtrend runs from 162, and SMA100 is falling (−5.3%). σ20/σ90 of 1.56 is above the threshold. The extreme spike to 128.5 on volume 4 was fully sold off within 4 days, a blow-off rather than momentum. z_2W of 1.5 comes from that single extreme week.
- **Weight:** 0.3. High volatility plus a falling trend is the least favourable combination.
- **Change my mind:** A close below 92 → 0.2. Stable weekly closes above 110 with falling volatility → 0.45.

## ed5a0a64ee (BTC)
- **Read:** ER is 0.37, σ20/σ90 is a calm 0.89, SMA100 is rising and there was only 1 crossing. The price is in a narrow consolidation of 99.5–106 above the breakout from about 84. z_2W of −0.1 is noise: the weekly regime is up and the correction is small.
- **Weight:** 0.6.
- **Change my mind:** A close below 98 → 0.45. A close above 106 → keep 0.6–0.65.

## 3481bbfbf4 (XRP)
- **Read:** SMA100 is rising, ER is 0.28 and σ20/σ90 is 0.91. The spike to 126.7 was a wick, and the range since is 98–110. z_2W of −0.1 marks a correction inside an uptrend.
- **Weight:** 0.55.
- **Change my mind:** A close below 97 → 0.45. A weekly close above 110 → 0.65.

## 523298ae93 (LTC)
- **Read:** All momentum signs are positive (z_2W 1.4, z_4W 1.7, z_8W 0.8), ER is 0.34 and σ20/σ90 is a normal 1.09. SMA100 is flat to slightly rising. The structure is an HL at 88, then a breakout over 100, with the 110.6 high only as a wick. Support is at 96.
- **Weight:** 0.6.
- **Change my mind:** A close below 96 → 0.45.

{"128e68e63d (ADA)": 0.45, "24d5b92805 (SOL)": 0.55, "206990aa98 (ETH)": 0.65, "ec31f95bed (AVAX)": 0.45, "5cc037fe49 (DOGE)": 0.45, "bdd6157ddf (LINK)": 0.5, "b3ead30579 (DOT)": 0.3, "ed5a0a64ee (BTC)": 0.6, "3481bbfbf4 (XRP)": 0.55, "523298ae93 (LTC)": 0.6}

## Entscheidung 2026-09-20

## Strategy

Each window starts at a neutral weight of 0.5. I only move above that when 2-, 4- and 8-week momentum all point up with |z_4W| ≥ 0.5 and price sits above a rising SMA100. I cut size when σ20/σ90 is above 1.5 or a move rests on a few giant candles. A low ER, mixed momentum signs or a range-bound structure keep the weight near the middle. Changes only happen on confirmed weekly closes beyond the levels named below.

## 64e882b2ae (ADA)
- **Read:** Price is above a rising SMA100, but momentum is flat (z_4W 0.0, z_2W +0.1) and ER(30) is 0.01, which means a sideways regime.
  - After the spike to 113 (wick) at day −29, it has ranged between about 84 and 103 for four weeks.
  - The jump at −2 just brings it back into the upper half of that range, and range position is not a signal.
- **Weight:** 0.5.
- **Change my mind:** a weekly close below 84 means reduce to about 0.3. Several closes above 103 make the breakout count, so 0.6.

## 061fa2d808 (XRP)
- **Read:** The post-spike range runs from about 88 to 108, with z_4W −0.3 and z_8W +0.9, so the signs are mixed.
  - ER is 0.04. The SMA100 is rising and price is above it, but there is no trend state.
  - Day −5 shows a large sell-off candle on high volume that was fully recovered, which is noise.
- **Weight:** 0.5.
- **Change my mind:** a close below 88 means 0.35. A weekly close above 108 means 0.6.

## b9134d7f14 (LINK)
- **Read:** The SMA100 is rising strongly (+7.7%) and z_8W is +1.6, but z_2W is −0.4, so the signs are mixed and ER is low.
  - Lows are roughly flat to rising (87.8 → 86.3), and the swing high is 109 (day −13).
  - This looks like a correction inside a weekly uptrend, which is no reason to sell.
- **Weight:** 0.55.
- **Change my mind:** a close below 85 (the last swing low) means 0.35. A weekly close above 106 means 0.65.

## 764e17151a (DOT)
- **Read:** All momentum windows are about +1, which counts as a trend state.
  - Against that, σ20/σ90 is 1.54, the SMA100 is falling, and the rise came in violent spikes: 113 at −12, down to 83, back to 100.
  - Volatility is high and the longer trend is still not confirmed as turned, so I size down to neutral rather than chase.
- **Weight:** 0.5.
- **Change my mind:** a close below 88 means 0.3. Holding above 105 for a week with volatility calming means 0.65.

## 54b1477da1 (DOGE)
- **Read:** The SMA100 is falling, z_2W and z_4W are negative, and ER is 0.07. The range is roughly 90 to 109, with price in the middle. There is no trend.
- **Weight:** 0.45.
- **Change my mind:** a weekly close below 89 means 0.3. A weekly close above 109 means 0.6.

## 90b93fd69b (SOL)
- **Read:** 2W, 4W and 8W momentum are all positive (z_4W +1.0), the SMA100 is rising +7.4%, ER is 0.20 and volatility is normal.
  - Price closed above the prior swing high of 99.5 (day −24) and the higher lows (86–88) are intact. This is a valid trend state.
- **Weight:** 0.65.
- **Change my mind:** a close below 86 (swing low) means 0.4. A failure back below 95 for a full week means 0.55.

## e6e47efc51 (ETH)
- **Read:** All momentum signs are positive (z_4W +0.5, at the threshold), the SMA100 is rising and volatility is calm (0.89).
  - ER is low (0.10), with consolidation between 89 and 101 since the gap-up at −32, so the trend is intact but slow.
- **Weight:** 0.6.
- **Change my mind:** a close below 89 means 0.4. A weekly close above 101 keeps 0.6 to 0.65.

## 749e039a02 (BTC)
- **Read:** All signs are positive, but z_4W is only +0.4 and ER is 0.09.
  - Price is ranging between 92.4 and 101.4 above a rising SMA100. This is hold territory, not an add.
- **Weight:** 0.55.
- **Change my mind:** a close below 92 means 0.4. A weekly close above 102 means 0.65.

## 050d558d6f (AVAX)
- **Read:** Momentum is strongly positive (z_2W +2.7), ER is 0.42 and price is 64% above the SMA100.
  - The last two days alone gave +23% and +12% on 4× to 6× volume, an extreme week that rests on a couple of giant candles.
  - σ20/σ90 is 1.53, the SMA100 is flat to falling, and the longer weeks were only modestly positive before this burst.
  - Rule: don't chase, and high volatility means a smaller size. The breakout above the multi-month range (about 73) still needs to hold.
- **Weight:** 0.5.
- **Change my mind:** a close back below 85 (the breakout fading toward 73) means 0.3. Holding above 90 for a week with volatility settling means 0.65.

## 6f7eed378f (LTC)
- **Read:** All momentum is positive (z_4W +0.9), the SMA100 is rising, ER is 0.19 and volatility is normal.
  - Lows are rising (80.7 → 85.5) and the close is near the 101 high. This is a trend state.
- **Weight:** 0.65.
- **Change my mind:** a close below 85 means 0.4. A weekly close above 101.5 confirms it, and I would keep 0.65.

{"64e882b2ae (ADA)": 0.5, "061fa2d808 (XRP)": 0.5, "b9134d7f14 (LINK)": 0.55, "764e17151a (DOT)": 0.5, "54b1477da1 (DOGE)": 0.45, "90b93fd69b (SOL)": 0.65, "e6e47efc51 (ETH)": 0.6, "749e039a02 (BTC)": 0.55, "050d558d6f (AVAX)": 0.5, "6f7eed378f (LTC)": 0.65}

## Entscheidung 2026-09-27

**Strategy:** Start every window from a neutral 0.5. Raise toward 0.7 only when there is a confirmed trend state. That means 2-, 4- and 8-week momentum share a sign, |z_4W| is above 0.5, price is above a rising SMA100 and the weekly structure shows higher highs. Size down for high volatility (σ20/σ90 near or above 1.5), for low trend quality (ER near 0.1) and for moves carried by one or two giant candles. Range position and distance to the average are not counted as signals.

All ten windows share the same shape: a crash around day -114, a drift lower until about day -40, a breakout at day -39, and a rally into the decision day. So every window is in an uptrend, and the differences come from trend quality, volatility and structure.

## b59326ea14 (DOT)
- **Read:** Strong trend state, with all z positive and z_4W at +2.3. ER is 0.31 and the SMA100 is rising. Price went from about 60 to 100 in six weeks with higher lows (74.5, then 85.0, then 89.2). The older range high is around 113.
- **Volatility:** σ20/σ90 is 1.57, which is in the high band, and the daily ranges are wide.
- **Weight 0.6:** The trend supports holding above neutral, but high volatility caps the size.
- **Change mind:** A close below 85.

## bee01bd424 (DOGE)
- **Read:** z_4W is only +0.9 and ER is 0.15, so the trend is weak. Since day -36 price has chopped between about 81 and 104. The spike to 109 at day -5 was given back right away, which looks like a failed breakout.
- **Volatility:** σ20/σ90 is 1.34.
- **Weight 0.5:** Trend quality is too low to justify anything above neutral.
- **Change mind:** Hold through weekly closes above about 104 for a higher weight. A close below 81 for a lower one.

## e07a4a79b4 (SOL)
- **Read:** Clean trend state, with z at +1.9, +1.2 and +2.7, and a strongly rising SMA100 (+9.8%). The structure shows higher highs (89.5, 92.4, 97.5, 100.1) and higher lows (78.5, then 92.2).
- **Volatility:** σ20/σ90 is 1.27, which is normal.
- **Weight 0.7.**
- **Change mind:** A close below 92 is a warning. A close below 78.5 means the trend is broken.

## 6e34b1c9de (LINK)
- **Read:** Essentially the same picture as e07a4a79b4 (SOL): z at +1.8, +1.3 and +2.4, SMA100 rising 9.5%, and a higher-high/higher-low sequence (lows 77.0 then 86.0).
- **Volatility:** σ20/σ90 is 1.16.
- **Weight 0.7.**
- **Change mind:** A close below 86 is a warning. Below 77 means the trend is broken.

## 94e9802dde (AVAX)
- **Read:** The 2-week z of +3.1 comes almost entirely from one burst, roughly 70 to 104 between days -9 and -6, on 5.7x volume. Since then price has moved sideways between 92 and 104. The longer windows do confirm the trend (z_4W +2.3).
- **Volatility:** σ20/σ90 is 1.64, which is high.
- **Weight 0.55:** The trend is real, but an extreme single week plus high volatility argues for holding near neutral.
- **Change mind:** A close below 91.4 (the day -3 low).

## 06c70b18a9 (ADA)
- **Read:** z at +1.7, +1.5 and +1.1, ER 0.25. The structure shows higher highs (89.8, 88.0, 99.7, 101.5) and higher lows (74.6, then 91.3).
- **Volatility:** σ20/σ90 is 1.05, which is normal.
- **Weight 0.7.**
- **Change mind:** A close below 91 is a warning. Below 74.6 means the trend is broken.

## 51c7df9945 (BTC)
- **Read:** A smooth staircase: a breakout over 96 at day -6, then a tight consolidation around 100 with very small recent ranges. z_8W is +2.0 but z_4W is only +0.7.
- **Volatility:** σ20/σ90 is 1.12, which is low and stable.
- **Weight 0.65.**
- **Change mind:** A close back below 96 means the breakout failed. A close below 88.7 means the trend is broken.

## d2ecefaaa4 (LTC)
- **Read:** The strongest trend statistics in the set: z at +2.7, +2.9 and +2.5, and ER at 0.52. However, a large part of the move is one candle on day -3 (+16% on 6.7x volume), and gains carried by a single candle are more fragile.
- **Volatility:** σ20/σ90 is 1.49, close to the high band.
- **Weight 0.65.**
- **Change mind:** A close below 86.5 (the base of the gap candle) undoes the move. Below 82.5 the trend is in question.

## 1b7c9fef21 (ETH)
- **Read:** z at +0.8, +0.7 and +1.9, and the SMA100 is rising strongly (+8.7%). Higher lows at 87.7 and then 96.7, with a calm consolidation just under the 104 high.
- **Volatility:** σ20/σ90 is 0.88, the lowest in the set.
- **Weight 0.65.**
- **Change mind:** A close below 96.7 is a warning. Below 87.7 means the trend is broken.

## 2601b565a6 (XRP)
- **Read:** z_4W is +0.5, right on the threshold, and ER is 0.11, the lowest in the set. Price has whipsawed between about 83 and 112 since day -36, with big wicks both ways and repeated high-volume spikes. That is a range, not a trend.
- **Volatility:** σ20/σ90 is 1.21.
- **Weight 0.5:** There is no trend signal, so stay at neutral.
- **Change mind:** Weekly closes above 110 for a higher weight. A close below 82 for a lower one.

{"b59326ea14 (DOT)": 0.6, "bee01bd424 (DOGE)": 0.5, "e07a4a79b4 (SOL)": 0.7, "6e34b1c9de (LINK)": 0.7, "94e9802dde (AVAX)": 0.55, "06c70b18a9 (ADA)": 0.7, "51c7df9945 (BTC)": 0.65, "d2ecefaaa4 (LTC)": 0.65, "1b7c9fef21 (ETH)": 0.65, "2601b565a6 (XRP)": 0.5}
