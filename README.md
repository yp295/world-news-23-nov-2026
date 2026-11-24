[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/yp295/world-news-23-nov-2026/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/yp295/world-news-23-nov-2026/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

# World News 23 November 2026 in One Image

Entry for the make.fun bounty [Sum up 23 November's world news in one image](https://make.fun/bounty/news-image-20261123) ($100).

## The image

`news.png` — a 1024 x 1024 newspaper front page summing up Monday 23 November 2026: 13 main stories with real photos, a UTC timeline, a numbers strip, a region bar, a world map with numbered pins, and 24 more one-line items — 37 stories in total. A DATE CHECK in the footer excludes stories from 19, 20, 21 and 22 November.

**13 main stories (all first reported 23 November 2026):**

1. **HUANG RETURNS AS NVIDIA CEO** — board unanimously reinstates Jensen Huang 11 days after he quit; shares +31%, Nasdaq +6.5%. (Reuters · CNN)
2. **IRGC CLAIMS 3 TANKERS HIT MINES** — Revolutionary Guards say three "violating" tankers caught fire after hitting naval mines in Hormuz; unverified, CENTCOM silent. (Reuters · Press TV)
3. **UNRWA WORKER KILLED IN GAZA** — Adel Al-Helo, 35, killed near a water well in Jabalia camp; at least 3 killed in Gaza that day. (Reuters)
4. **'SPUTNIK-S': NUCLEAR SATELLITE READY** — Western intel: Moscow built a nuclear-armed satellite, launchable in 60 days; NATO will defend space. (NDR · WDR · SZ)
5. **~700,000 RUSSIAN SOLDIERS KILLED** — leaked Rosstat data: 490,000 deaths recorded to Sep 2026, est. over 700,000 in 200 Russians. (Mediazona · Meduza)
6. **UK RECOGNISES ROHINGYA GENOCIDE** — Milibrand tells MPs: Britain formally recognises the genocide, sanctions 5 generals. (FCDO · Reuters)
7. **FIFA NAMES WOMEN'S WORLD CUP HOSTS** — 2031: US, Mexico, Costa Rica, Jamaica — first 48-team edition; 2035: England. (FIFA · Reuters)
8. **EU PROPOSES 22ND SANCTIONS PACKAGE** — Commission proposes banning Russian teams under their flag, visa bans for propagandists, curbs on crypto schemes. (EU Commission)
9. **US SANCTIONS IRAN SHADOW BANKS** — Treasury sanctions 8 people, 22 entities moving money for Tehran; DOJ moves to seize $1bn+ crypto stolen from Binance. (US Treasury · Reuters)
10. **SPAIN FREES PUIGDEMONT TO RETURN** — Supreme Court archives the case against the ex-Catalan leader, clearing his return after nearly a decade in exile. (Reuters)
11. **BOMB THREATS HIT ~450 GERMAN SCHOOLS** — emailed threats reach about 450 schools Monday morning; police call them not credible and classes go on. (Reuters · Bild)
12. **UPDATE — DYMER TOLL 11; TWO PULLED ALIVE** — Monday toll 11; Davyd, 7, and Valentyna, 79, pulled alive after ~22 hours. Kyiv region in mourning. (Reuters)
13. **DEEP M6.5 QUAKE OFF VANUATU** — M6.5 at ~598 km depth at 02:40 UTC; USGS green alert, no tsunami threat, no damage reported. (USGS)

**DATE CHECK** (printed in the footer): strictly 23 November 2026 coverage. Excluded: 19 Nov — Shenzhen summit, ICJ ruling; 20 Nov — El Chapo capture, Nigeria boat, Peru quake; 21 Nov — BepiColombo orbit capture, Cikande fire, EU-Indonesia deal; 22 Nov — Alcaraz, Márquez, COP31 collapse, Merkury sinking, Dymer strike, Khartoum drones, Skubal deal, Democrats' 258 seats. Monday updates only: Dymer toll, Merkury confirmation, Cikande toll. Not yet: Nepal quake and a Hamas official killed were 24 Nov.

Photo sources and honest caveats (some photos are representative, not exact-event) are in `PHOTO_CREDITS.md`. Sources for every story (date + outlet) are in the build notes (`SOURCES.md`, kept with the build scripts).

## The program

`main.py` (Python 3.13, standard library only) copies the bundled `news.png` to `/output/entry.png` byte-for-byte and verifies the sha256 before and after copying. No network, no randomness, fully deterministic — two runs produce identical bytes.

Run it:

```sh
python3 main.py
```

## License

MIT — see `LICENSE`.
