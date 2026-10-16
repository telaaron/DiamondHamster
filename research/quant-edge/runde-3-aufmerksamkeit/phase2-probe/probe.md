# Runde 3 · Phase 2 · Datenprobe (2026-10-16, 16:34–16:38 UTC)

Gemessen von Aarons Mac, ohne API-Keys und ohne Konto. 61 Requests, alle in `requests.log` (Datei, HTTP-Code, Bytes, Zeit). Roh-Antworten in `raw/`, Hashes in `sha256.txt`.
SEC mit User-Agent `DiamondHamster research admin@must-seen.com`, ~3 req/s.

## Tabelle

| Quelle | erreichbar | HTTP | PIT-Zeitstempel-Feld | Historie ab | Delistete/Gelöschte drin? | Limits | Lücken |
|---|---|---|---|---|---|---|---|
| SEC submissions (data.sec.gov) | ja | 200 | `acceptanceDateTime` (UTC, sekundengenau) = Annahme durch EDGAR; `filingDate` nur Tag | AAPL: recent ab 2015-09 (1002 Filings), ältere in `submissions-001.json` ab 1994-01-26 | ja, EDGAR löscht praktisch nie | 10 req/s, UA Pflicht | Uhrzeit in den alten Zusatzdateien nicht geprüft |
| SEC daily-index | ja | 200 | nur Datum im Dateinamen (`company.YYYYMMDD.idx`), keine Uhrzeit | 1994 Q3 | ja | 10 req/s | keine Uhrzeit, für Uhrzeit Submissions-API nehmen |
| SEC Full-Text-Suche (efts) | ja | 200 | `file_date` (nur Tag) | 2001 (Jan 2001 „internet": 4552 Treffer) | ja | 10 req/s | nur Tag; Uhrzeit per `adsh` aus Submissions nachschlagen |
| GitHub REST commits | ja | 200 | **keins**: `author.date` und `committer.date` sind vom Client gesetzt (Beispiel: beide identisch, beliebig fälschbar) | ganze Repo-Historie | gelöschte Repos/force-pushes weg | 60 req/h ohne Token (`x-ratelimit-limit: 60`), GraphQL ohne Token 0 | Commit-Datum nicht PIT-tauglich |
| GH Archive | ja | 206 (Range) | `created_at` = GitHub-Server-Zeit des Events (PushEvent 2023-03-01T12:00:00Z) | 2011-02-12 (Datei existiert) | ja, Stundendateien sind unveränderlich, auch Events später gelöschter Repos | keins bekannt; Dateien groß (Stunde ≈ 100 MB+ entpackt) | Commit-SHA im PushEvent → Verknüpfung mit Repo-Inhalt möglich |
| Discourse gov.uniswap.org | ja | 200 | `created_at` je Topic/Post (Server); `bumped_at`/`updated_at` daneben getrennt | 2020-09-08 (`?order=created&ascending=true`) | gelöschte Posts fehlen; editierte Posts haben `version`>1, Ursprungstext nur über `/posts/{id}/revisions` | ungetestet, Discourse-Default ~60 req/min anonym | `?page=50&order=created` leer (Paging endet früh) → Topic-IDs `/t/{id}.json` direkt laufen |
| Discourse forum.arbitrum.foundation | ja | 200 | `created_at` (Server) | Seite 80 → Okt 2023; frühestes gesehen 2022-10-04 | wie oben | wie oben | wie oben |
| Snapshot hub GraphQL | ja | 200 | `created` (Unix, Hub-Server bei Einreichung), dazu `start`/`end` | 2020-07-18 (balancer.eth); Uniswap ab 2020-09-22 | gelöschte Proposals fehlen (Spaces können löschen) | ungetestet; Hub erlaubt ohne Key ~60 req/min | `start` kann vor `created` liegen (Uniswap #1: start < created) |
| Tally API | nein | 401 | – | – | – | API-Key nötig (= Kontoanlage, nicht gemacht) | ausgefallen |
| DefiLlama Emissions | nein | 402 | – | – | – | `/emissions` und `/emission/{id}` nur Bezahlplan; `defillama-datasets.llamao.fi` löst nicht auf; Repo `DefiLlama/emissions-adapters` 404 (privat/umbenannt) | ausgefallen |
| token.unlocks.app (Tokenomist) | nein | 403 | – | – | – | „automated_access_not_allowed", nur Bezahl-API | Wayback-CDX hat Snapshots ab 2023-03-20 (`token.unlocks.app/arbitrum`) → das einzige freie „was war am Tag X bekannt" |
| CryptoRank Vesting | nein | 403 | – | – | – | Cloudflare-Block | ausgefallen |
| Ethereum RPC publicnode | ja (nur aktuell) | 200 / 403 | Blockzeit on-chain (unveränderlich) | `eth_blockNumber` ok; Archivabfrage (Block 13.000.000) 403 „personal token" | n/a | Archiv nur mit Token | eth.drpc.org lieferte die Archivabfrage frei (200); eth.llamarpc.com 525 |
| Binance CMS „New Listing" (catalogId 48) | ja | 200 | `releaseDate` (ms, Server); Titel ohne Inhalt | 2283 Artikel, 115 Seiten à 20, älteste 2017-07-21 | Delisting-Katalog 161 (441 Artikel) erreichbar; ob zurückgezogene Artikel fehlen, unbekannt | ungetestet | `releaseDate` kann bei Neuveröffentlichung wechseln, nicht geprüft; Wayback hat die Übersichtsseite ab 2020-05 |
| Upbit Notices | ja (neuer Pfad) | 200 (alter Pfad 404) | `first_listed_at` (KST) = erste Veröffentlichung; `listed_at` = letzte Änderung (Beispiel ZIL: first 2026-07-20, listed 2026-10-16) | 5904 Notices, 296 Seiten, älteste 2017-10-24 | unbekannt | ungetestet | Pfad: `/api/v1/announcements?os=web&page=N&per_page=20&category=all` |
| Coinbase Assets / Blog | nein (direkt) | 403 | – | – | – | Blog 403; X-Konto ohne freie API | Wayback hat `x.com/CoinbaseAssets` ab 2024-05, aber Profilseiten ohne Tweet-Liste → praktisch keine zeitgestempelte Quelle |
| Wayback CDX | ja | 200 | `timestamp` = Crawlzeit (PIT im strengen Sinn: „spätestens bekannt um") | binance announcement ab 2020-05-26 | ja (Archiv) | langsam (6–25 s pro Abfrage) | Abdeckung zufällig, Lücken von Wochen |
| data.binance.vision Klines 1h | ja | 200 | `open_time`/`close_time` (ms), Daten nachträglich erzeugt | FTTUSDT ab 2019-12; Verzeichnis ~1000 Spot-Symbole | **ja**: SRMUSDT bis 2022-11, BTCSTUSDT bis 2022-11 noch vorhanden | keins bekannt; `.CHECKSUM` je Datei (FTT 2024-03 stimmt) | Spot hat **kein** bookTicker-Archiv (nur aggTrades/klines/trades) |
| Binance Futures bookTicker-Archiv | ja | 200 | Tick-Zeit | 2023-05-16 | – | – | endet vor 2024-04 (keine Datei ab 2024-04) → Spread historisch nur 2023-05 bis 2024-03, sonst nur live |
| Binance REST bookTicker / exchangeInfo | ja | 200 | nur live | – | exchangeInfo führt SRMUSDT noch mit Status `BREAK` | Gewichtslimit | Spread nur live messbar (außer Futures-Fenster oben) |
| CoinGecko free | teilweise | 401 (`days=max`) / 200 (`days=90`) | Tagespunkte 00:00 UTC, Werte nachträglich berechnet | **nur letzte 365 Tage** ohne Bezahlplan (error_code 10012) | unbekannt | Public-Limit ~30 req/min | Volumen pro Tag vorhanden (`total_volumes`), aber keine lange Historie |

## Kurz-Urteil

- **PIT-tauglich und frei:** SEC (Submissions mit Uhrzeit), GH Archive, Discourse `created_at`, Snapshot `created`, Binance CMS `releaseDate`, Upbit `first_listed_at`, Wayback-Crawlzeit.
- **Nicht PIT:** GitHub-Commit-Datum (fälschbar), Token-Unlock-Kalender (alle freien Wege zu; nur Wayback-Schnappschüsse von token.unlocks.app als Ersatz).
- **Kurse:** data.binance.vision ist frei, mit Delisteten, ohne Survivorship-Lücke bei Binance. Spread historisch nur über Futures-bookTicker 2023-05 bis 2024-03.
- **Ausgefallen:** Tally, DefiLlama Emissions, Tokenomist, CryptoRank, Coinbase.

## Holdout-Protokoll (2025-01-01 bis 2026-06-30)

Keine Kursdaten aus dem Fenster geladen. Kursdateien dieser Probe: FTTUSDT-1h-2024-03 (März 2024), Binance bookTicker live (2026-10-16), CoinGecko ARB 90 Tage (2026-07-19 bis 2026-10-16, vollständig nach dem Fenster). Die Anfrage `coingecko_arb_max.json` (days=max) hätte das Fenster berührt, wurde aber mit 401 abgelehnt; es kamen keine Kurse.

Antworten ohne Kurse, deren Inhalt ins Fenster fällt:
- `sec_submissions_aapl.json`: Filing-Liste enthält 2025/2026-Einträge (Metadaten).
- `gh_commits.json`: ein Commit vom 2026-04-30.
- `uni_latest.json`, `uni_latest_asc.json`, `uni_topic_first.json`, `arb_latest.json`: `bumped_at`/`last_posted_at` im Fenster.
- `upbit_announcements*.json`: gepinnte Notice vom 2025-10-29 („불공정거래 예방조치 제도 안내").
- `bv_s3_ftt.xml`: Dateinamen und LastModified 2025/2026 (nur Listing, keine Kurse).
