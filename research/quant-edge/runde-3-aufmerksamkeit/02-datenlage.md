# Runde 3, Phase 2: Datenlage (2026-10-16)

Frage: Gibt es kostenlose Quellen mit Zeitstempel der **erstmaligen öffentlichen Verfügbarkeit** (Point-in-Time, kurz PIT) und Kurse mindestens in Stundenauflösung?

Software-Analogie für PIT: Wir brauchen das `created_at` eines Datensatzes, nicht sein `updated_at`. Ein Archiv, das nur den heutigen Stand kennt, ist wie eine Datenbank ohne Historie: Man kann nicht rekonstruieren, was am Tag X sichtbar war.

Messung: 61 Requests von Aarons Mac (Container ist für alle Quellen außer GitHub-Repo und PyPI gesperrt, HTTP 403 am Proxy, (G)). Roh-Antworten, Log und sha256 in `phase2-probe/` (65 Dateien, Prüfsummen nachgerechnet: alle OK (G)).

## Urteil vorweg

Die Runde **kann laufen**, aber nicht für alle Kandidaten:

| Kandidat | Dokument-/Ereignisquelle PIT | Kurse ≥ 1h | Urteil |
|---|---|---|---|
| A1 Token-Unlocks | **nein, frei nicht verfügbar** (Kalender-Anbieter 402/403; nur Wayback-Schnappschüsse oder eigener On-Chain-Parser) | ja | **bedingt**: nur mit eigenem Vesting-Vertrags-Leser oder bezahltem Kalender |
| A2 Schwer lesbare Dokumente | ja: SEC (`acceptanceDateTime`, sekundengenau), Snapshot (`created`), Discourse (`created_at`) | Krypto ja (Binance-Archiv); US-Aktien nur Tageskerzen voll, Stunden ab 2023 (TradingView) | **lauffähig**, saubere KI-Messung nur ab 2026-07 |
| A3 Querverbindungen | Ereignisse ja (wie A2); der Graph selbst ist nicht PIT (heutige Partnerschaften ≠ damalige) | wie A2 | **bedingt**: Graph muss aus PIT-Dokumenten gebaut werden |

Was A2/A3 trotzdem stark begrenzt, ist nicht die Datenquelle, sondern der Leser: Das Modell kennt alles bis ca. Juni 2026 (Phase 0). Sauberes Testfenster = 2026-07-01 bis heute, ~15 Wochen.

## Quellen im Detail (G = gemessen per Request, Rohdatei in phase2-probe/raw/)

| Quelle | frei erreichbar | PIT-Feld | Historie ab | Gelöschte/Delistete drin? | Lücke |
|---|---|---|---|---|---|
| SEC EDGAR Submissions | ja (Mac) | `acceptanceDateTime` UTC, Sekunde | 1994 | ja | nur US-Firmen |
| SEC Volltextsuche | ja | `file_date` (nur Tag) | 2001 | ja | Uhrzeit per Akten-ID aus Submissions |
| GitHub Commits (REST) | ja, 60 req/h | **keins**: Commit-Datum setzt der Client | – | nein (Force-Push, Löschung) | **unbrauchbar als PIT** |
| GH Archive | ja | `created_at` = GitHub-Serverzeit des Push | 2011-02 | ja (unveränderliche Stundendateien) | groß (~100 MB/Stunde entpackt) |
| Discourse (Uniswap, Arbitrum) | ja | `created_at` (getrennt von `updated_at`) | 2020-09 / 2022-10 | gelöschte fehlen; Edits über `/revisions` rekonstruierbar | Paging endet früh, Topic-IDs iterieren |
| Snapshot (Abstimmungen) | ja | `created` (Hub-Serverzeit) | 2020-07 | gelöschte fehlen | `start` kann vor `created` liegen |
| Tally | nein (401, Konto) | – | – | – | – |
| Unlock-Kalender (DefiLlama, Tokenomist, CryptoRank) | **nein** (402/403) | – | – | – | einziger freier Ersatz: Wayback-Schnappschüsse ab 2023-03, lückenhaft |
| Ethereum Archiv-RPC | ja (eth.drpc.org frei; publicnode nur aktuell) | Blockzeit | Genesis | n/a | Vesting-Verträge pro Token selbst finden und dekodieren |
| Binance Listing-Ankündigungen | ja | `releaseDate` ms | 2017-07 (2283 Artikel) | Delisting-Katalog da | nur Titel; Neuveröffentlichung ändert evtl. Datum (ungeprüft) |
| Upbit Ankündigungen | ja | `first_listed_at` (Erstveröffentlichung, getrennt von `listed_at`) | 2017-10 (5904) | unbekannt | koreanisch |
| Coinbase Listings | nein (403) | – | – | – | keine freie zeitgestempelte Quelle |
| Wayback CDX | ja, langsam | Crawlzeit = "spätestens bekannt" | 2020-05 (Binance) | ja | zufällige Abdeckung |
| Kurse: data.binance.vision 1h | ja | Kerzen-Zeit | Listing jedes Symbols (~1000 Spot) | **ja**, delistete (SRM, BTCST) noch da | nur Binance-Volumen |
| Kurse: TradingView MCP 1h | ja (Container) | Kerzen-Zeit | Krypto erst ab 2026-01-01, US-Aktien ab 2023-01-03 | delistete fehlen | Krypto-Stunden fallen ins Holdout bzw. danach |
| Spread historisch | Futures-bookTicker 2023-05 bis 2024-03 | Tick | – | – | Spot: kein Archiv; sonst nur live |
| CoinGecko frei | teilweise | Tagespunkte, nachberechnet | nur letzte 365 Tage | – | zu kurz |

## Lücken und wie sie geschlossen würden

1. **Unlock-Kalender (A1):** frei nur über eigenen Leser für Vesting-Verträge (Archiv-RPC, Vertrag je Token manuell finden, Zeitplan aus dem Zustand zu einem früheren Block lesen). Aufwand (S): ~1 bis 2 Tage pro 10 Token; Auswahl der Token selbst ist eine Survivorship-Quelle. Alternative: Tokenomist-API (bezahlt), wenn Aaron das will.
2. **Spread:** für die Rückrechnung aus Stunden-Hoch/Tief schätzen (Corwin-Schultz-Schätzer, (S)) und gegen die Futures-bookTicker-Monate 2023-05 bis 2024-03 eichen; im Forward-Test live messen.
3. **Volumenschwelle:** aus Binance-`quote_volume` der 30 Tage vor dem Ereignis (PIT). Nur Binance unterschätzt das Weltvolumen, macht also mehr Assets "klein" als sie sind; als Nebentest Schwelle halbieren.
4. **Delistete Aktien:** TradingView führt sie nicht; Aktienvariante von A2 hätte Survivorship. Krypto-Variante (Binance-Archiv) nicht.
5. **Netzweg:** Alle Abrufe laufen über eine Remote-Control-Sitzung auf Aarons Mac; der Container erreicht keine dieser Quellen.

## Ersatzdaten, die bewusst **nicht** benutzt werden

- GitHub-Commit-Daten (fälschbar), heutige Unlock-Kalender (nachträglich korrigiert), CoinGecko-Historie (nachberechnet, zu kurz), Nachrichten-Feeds ohne Erstzeitstempel (TradingView-News: nur die letzten 200 Schlagzeilen je Symbol).

## Holdout-Protokoll

- Keine Kursdaten aus 2025-01-01 bis 2026-06-30 geladen (G, probe.md).
- Metadaten ohne Kurse mit Einträgen im Fenster: SEC-Filingliste AAPL, ein GitHub-Commit (2026-04-30), Forum-`bumped_at`-Felder, eine angepinnte Upbit-Mitteilung (2025-10-29), Dateinamen im Binance-S3-Listing. Für keinen Kandidaten relevant, aber hiermit geloggt (Wächter B-19/B-21).
- TradingView-Abfragen dieser Runde: nur `summary` bzw. Fehlerantworten; die beiden Krypto-1h-Abfragen (Fenster 2023 und bis 2025-12-31) lieferten 0 Bars.
