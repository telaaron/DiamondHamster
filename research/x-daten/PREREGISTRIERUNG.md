# Vorab-Festlegung X-Sentiment-Score (H-X1)

Status: **ENTWURF**, wird mit Aarons OK eingefroren (Datum + Commit-Hash unten). Danach keine Änderung mehr, nur neue Versionen mit neuem Namen, die als neuer Versuch in N_kum zählen.
Anlass: Methodik-Befund B-24 (research/methodik/befunde.md). Gilt vor dem ersten Datenpunkt.

Warum: Kostenlose X-Historie gibt es nicht, also ist nur ein Vorwärtstest möglich. Wer erst Daten sammelt und dann die Formel wählt, tunt den Score auf genau diese Daten (wie Tests schreiben, nachdem man den Output gesehen hat).

## 1. Hypothese

H-X1 (konträr, zweiseitig getestet): Der tägliche Score S korreliert mit der BTC-Rendite der folgenden 28 Tage.
Erwartung: negativ (Euphorie vor schwachen Wochen, Angst vor starken). Ein positiver Zusammenhang zählt ebenfalls als Befund, aber nur, wenn er das Kill-Kriterium besteht.

## 2. Accountliste

- Auswahlregel statt Bauchgefühl: 50 Accounts, die Aaron und Fynn **vor Start** nach dieser Regel wählen: englisch- oder deutschsprachig, Krypto-Marktkommentar als Hauptthema, > 100k Follower am Stichtag, mindestens 3 Posts pro Woche im Oktober 2026.
- Liste als `accounts-v1.csv` (Handle, X-User-ID, Follower am Stichtag, Begründung) mit Datum eingefroren. Gespeichert wird die **User-ID**, weil Handles sich ändern.
- Kein Nachtragen, kein Austausch. Wer gesperrt wird oder aufhört, bleibt als "fehlt" in den Daten (gegen Survivorship: sonst misst man nur die, die überlebt haben).
- Bekannte Verzerrung: "heute groß" heißt "lag zuletzt richtig oder laut". Wird nicht korrigiert, nur benannt.

## 3. Score-Formel (fest)

Klassifizierung je Text durch einen Claude-Subagenten mit eingefrorenem Prompt (`klassifizierer-v1.md`, sha256 hier eintragen), kein Zugriff auf Preise:
- Post: Haltung zu BTC/Gesamtmarkt ∈ {bullisch, bärisch, keine}.
- Reply: Haltung ∈ {bullisch, bärisch, keine} plus Ton ∈ {Zustimmung, Widerspruch, Hass, Unsicherheit} (Ton fließt **nicht** in S ein, nur als Zusatzinfo, damit S einfach bleibt).

Tageswert um 00:00 UTC über ein rollierendes 7-Tage-Fenster:
- P = bullisch / (bullisch + bärisch) über alle Posts; jeder Account höchstens 5 Posts pro Fenster (damit Vielposter nicht dominieren).
- R = dasselbe über Replies; je Post genau ein Abruf 3-24 h nach Erscheinen, höchstens 40 Replies in der Reihenfolge, die X dabei anzeigt (X sortiert nach eigener Relevanz, nicht nach Zeit; das ist Teil der Messung).
- S = 100 × (0,5·P + 0,5·R). Fehlt P oder R (keine Haltung), zählt der vorhandene Teil allein; fehlen beide, S = 50.

## 4. Horizont, Baseline, Test

- Ziel: BTC-Rendite (Binance BTCUSDT Close 00:00 UTC) von Tag t bis t+28.
- Maß: Spearman-Rang-Korrelation (IC) zwischen S_t und Rendite t→t+28, t-Wert mit Newey-West (Lag 28), weil sich die Fenster überlappen.
- Baselines: (a) Zufalls-Score: 1.000 Permutationen in 28-Tage-Blöcken, IC muss ins äußere 5 % fallen; (b) Halten: eine Regel "Exposure = 1 − S/100" muss Halten nach 0,1 % Kosten je Umschichtung schlagen.
- Ehrliche Grenze: Bei 26 Wochen Laufzeit sind es nur ~6 unabhängige 28-Tage-Fenster. Erkennbar ist nur ein großer Effekt (|IC| ~0,4+). Kleine Effekte bleiben unsichtbar.

## 5. Kill-Kriterium und Stoppdatum

- Start: Tag des ersten Datenpunkts (eintragen). Stopp: **Start + 26 Wochen**, erste Auswertung erst dann. Kein Zwischen-Blick auf IC (Zwischenblicke sind verdecktes Tuning).
- Kill: |t_NW| < 2 **oder** Permutationstest nicht im äußeren 5 % **oder** Regel schlägt Halten nicht → Score wird nicht als Signal genutzt, höchstens als Info-Anzeige ohne Handlungsbezug.
- Betriebs-Kill vorab: Datenabdeckung < 80 % der Tage (Bann, Ausfall) → Test ungültig, nicht verlängern, neu vorab-festlegen.
- Zählt als **1** Versuch in N_kum (Wissensbasis/Methodik).

## 6. Rohdaten (ab Tag 1, Geist von B-19)

- Jede Antwort roh speichern: `daten/raw/YYYY-MM-DD/HHMMSS_<endpoint>_<user_id>.json.gz` plus `request.json` (Endpoint, Parameter, Zeitstempel UTC, Route, twscrape-Version).
- Täglich `daten/raw/YYYY-MM-DD/sha256.txt`; Dateien nie überschreiben oder nachträglich bearbeiten.
- Klassifizierungs-Ergebnisse getrennt, je Zeile mit Prompt-sha256, damit eine neue Prompt-Version nie alte Werte überschreibt.
- Technik-Tests vor dem Einfrieren landen in `TEST-unfrozen/` und zählen nie für H-X1 (Collector erzwingt das).
- Rohdaten bleiben auf dem Mac (später Mac Mini), nicht im Repo (Größe, fremde Inhalte); im Repo nur Manifeste und Hashes.

## 7. Offen (Aaron entscheidet vor dem Einfrieren)

- Route (Entscheidungskarte im Thread): twscrape mit Burner oder bezahlte API.
- Horizont 28 Tage passt zu "Wochen bis Monate". Alternative: 56 Tage, dann aber nur ~3 unabhängige Fenster in 26 Wochen.
- Die 50 Accounts nach Regel in §2 (Fynn kennt die Szene).

Eingefroren am: ____ · Commit: ____ · Start erster Datenpunkt: ____
