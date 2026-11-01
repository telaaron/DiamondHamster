# X-Daten kostenlos und nahe Echtzeit

Ziel: Posts der ~50 wichtigsten Krypto-Accounts auf X plus die Replies darunter,
als Rohstoff für einen Sentiment-Score (0 = alle bärisch, 50 = gemischt, 100 = alle bullisch).
Stand: 2026-11-01. Läuft nur auf Aarons Mac (aus der Cloud blockt X mit 403).

## Bedarf (grob gerechnet)

- 50 Accounts × ~5 Posts/Tag = ~250 Posts/Tag.
- Replies: 1-2 Seiten pro Post (~40-80 Replies) → ~10.000-20.000 Replies/Tag.
- Polling alle 15-30 min reicht für "nahe Echtzeit". Sentiment über Wochen braucht keine Sekunden-Latenz.
- Requests: ~50 Timeline-Abrufe pro Runde + ~250-500 Reply-Abrufe/Tag. Das ist klein.

## Routen im Vergleich

Getestet am 2026-11-01 auf dem MacBook mit `x_probe.py` (3 Accounts: APompliano, woonomic, CryptoHayes).

| Route | Posts | Replies | Zuverlässigkeit | Limits | Bann-Risiko | ToS | Kosten |
|---|---|---|---|---|---|---|---|
| **Nitter/xcancel RSS** (öffentliche Instanzen) | ja, 1 von 7 Instanzen lief (nitter.kareem.one, 39 Posts) | **nein** (Statusseiten 403) | schlecht: Nitter-Repo seit 11.09.2026 archiviert, xcancel 451, Rest 403/Challenge | Instanz-abhängig, unbekannt | keins für uns (fremde Instanz) | Graubereich, Risiko trägt der Betreiber | 0 |
| **Syndication/Embed** (`syndication.twitter.com`, `cdn.syndication.twimg.com`) | nicht testbar: DNS-Filter auf dem Mac (Tailscale/Pi-hole) blockt die Hosts | nein (nur Reply-Zahl je Post) | von X seit 2023 stark eingeschränkt | unbekannt | keins | Embed-Nutzung, eher ok | 0 |
| **fxtwitter/vxtwitter API** | einzelne Posts per ID, kein Timeline-Feed | nein | Drittdienst, kann jederzeit weg | unbekannt | keins | Graubereich | 0 |
| **X API offiziell** | ja | ja (Suche `conversation_id:`) | sehr gut | Pay-per-use, **kein Gratis-Lesetier mehr**: 0,005 USD pro gelesenem Post | keins | sauber | ~20k Replies/Tag ≈ 100 USD/Tag. Startguthaben bis 70 USD einmalig |
| **twscrape + Burner-Account** (Cookies `auth_token`, `ct0`) | ja | **ja** (`tweet_replies`) | gut, Lib aktiv gepflegt (0.20.1, Aug 2026); bricht, wenn X GraphQL ändert | pro Account+Endpoint ~50-500 Req/15 min; reicht für 50 Accounts | **mittel bis hoch**: Burner kann gesperrt werden, dann neuer Burner | **Verstoß** (Scraping ohne Erlaubnis; ToS nennen 15.000 USD je 1 Mio. Posts in 24 h als Schadenersatz, wir lägen bei ~20k/Tag) | 0 |
| **Playwright, eingeloggter Browser** | ja | ja | mittel: langsam, UI-Änderungen brechen Selektoren | menschliches Tempo nötig | mittel (Browser wirkt echter als API-Calls) | **Verstoß** wie twscrape | 0 |
| **Bluesky / Telegram** | ja, offiziell und frei | ja (Bluesky-API, Telegram-Kommentare) | sehr gut | großzügig | keins | sauber | 0, aber **andere Leute**: viele Top-Krypto-Accounts posten dort kaum |

Software-Analogie: Nitter und Syndication sind wie ein inoffizieller Mirror einer API, der jederzeit offline geht.
twscrape ist der Client, der die interne GraphQL-API der X-Web-App nachbaut, mit einem Login-Cookie als Session.

## Ergebnis der Probe

- **Ohne Login gibt es keine Replies.** Posts gehen noch über eine einzige Nitter-Instanz, das ist kein Fundament.
- Replies sind der Kern von Aarons Score (Zustimmung, Hass, Unsicherheit in den Kommentaren). Dafür braucht es einen eingeloggten Account oder Geld.
- Also bleiben zwei echte Wege: **twscrape mit Burner** (gratis, ToS-Verstoß, Bann-Risiko) oder **offizielle API** (sauber, ~3.000 USD/Monat bei voller Reply-Menge).
- Billige Mischform: offizielle API nur für Posts (250/Tag ≈ 1,25 USD/Tag), Replies nur als Stichprobe. Nicht "for free", aber legal.

## Empfehlung

twscrape mit **einem** Burner-Account auf dem Mac, Polling alle 30 min, nur die ~50 Ziel-Accounts, max. 40 Replies je Post.
Nitter-RSS als Fallback für Posts. Bei Bann: neuer Burner, nicht mehr Accounts parallel.

Nicht machen: Hauptaccount, gekaufte Accounts, Account-Pools, Proxys zur Tarnung. Das erhöht Bann- und Rechtsrisiko und ist für 50 Accounts unnötig.

## Burner einrichten (Aaron, ~10 min)

1. Neuen X-Account mit eigener E-Mail anlegen (nicht der Hauptaccount, nicht mit ihm verknüpfen). Ein paar Tage normal benutzen, den ~50 Ziel-Accounts folgen.
2. Im Browser eingeloggt: DevTools → Application → Cookies → `x.com` → Werte von `auth_token` und `ct0` kopieren.
3. Auf dem Mac:
   ```bash
   python3 -m venv ~/.diamondhamster/xvenv && ~/.diamondhamster/xvenv/bin/pip install twscrape
   mkdir -p ~/.diamondhamster
   TWS_TELEMETRY=0 ~/.diamondhamster/xvenv/bin/twscrape --db ~/.diamondhamster/x-accounts.db add_cookie burner1
   # fragt nach dem Cookie-String: auth_token=...; ct0=...
   ```
4. Test: `TWS_TELEMETRY=0 ~/.diamondhamster/xvenv/bin/python research/x-daten/x_probe.py --skip-nitter --twscrape`

Cookies bleiben auf dem Mac. Nie ins Repo, nie in den Chat.

## Offene Punkte

- DNS-Filter auf dem Mac (Resolver Tailscale 100.100.100.100 bzw. 192.168.178.120) blockt `syndication.twitter.com`, `cdn.syndication.twimg.com`, `nitter.poast.org`. Wahrscheinlich Pi-hole-Blockliste. Für die Empfehlung egal.
- woonomic lieferte 0 RSS-Posts: Handle geändert oder Instanzfehler, ungeprüft.

## Quellen

- Nitter-Instanzen, Repo archiviert 11.09.2026: https://github.com/zedeus/nitter/wiki/Instances
- X API Preise (Stand 10.10.2026): https://opentweet.io/x-api-pricing
- twscrape: https://pypi.org/project/twscrape/
- ToS-Schadenersatzklausel: https://conductatlas.com/platform/x/x-terms-of-service/liquidated-damages-for-bulk-post-access/
