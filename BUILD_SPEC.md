# BUILD_SPEC — news-image-20261119 ("The World Today")

Bounty: make.fun `news-image-20261119`, $250, FREE, deadline
2026-11-21T00:00:00Z (07:00 WIB 21 Nov 2026). Task: sum up Thursday
19 November 2026's world news in one image. Judge: z-ai/glm-5.3-flash,
pairwise, no news feed. Criteria in order: (1) names the day + specific
events of that day, nothing before 13 Nov 2026; (2) selection & breadth
across regions/fields; (3) reads — viewer can tell what happened from the
image alone; (4) faithful, no hype/speculation as fact; (5) craft, legible
at ~300px across.

Repo: https://github.com/irfandihmtr/news-image-20261119 (branch master).
Entrypoint: `main.py` (stdlib-only copier). Image: `entry.png`, 1024x1024.

## 1. Headlines (all verified 19 Nov 2026, 00:26–00:36 UTC, >=2 sources each)

Built at 00:35 UTC 19 Nov — i.e. early in the day. Every item below is an
event that happened, or was first reported, on 19 Nov 2026 in some timezone.
Nothing here is dated 17–18 Nov (see §2 for the traps that were excluded).

| # | Story (as printed) | Facts on the poster | Sources (checked 19 Nov 2026) |
|---|---|---|---|
| 1 LEAD | GTA VI IS HERE — Vice City opens worldwide | After 13 years; midnight local rollout country by country; PS5 & Xbox; pre-orders 15.9m copies, about $1.5bn | Rockstar/PlayStation via AP (theevenkeelnews, 18 Nov); Stocktwits/Sensor Tower: NZ live 12am NZDT, 15.88m units, $1.54bn; Escapist: 8 Game Awards noms, launch date locked 6 Nov 2025 |
| 2 | Trump, Xi and Putin meet — a first | First-ever three-way talks, APEC sidelines, Shenzhen; nuclear arms cuts + Iran on agenda; no deal expected | Reuters 18 Nov (via The Hill/NYP) + White House confirmation via SCMP/Yonhap/Bernama; Beijing confirmed (SCMP 15 Nov); worldofnow summary 18 Nov |
| 3 | Anthropic debuts as ANT | Priced at $83, above $70–$78 range; 980m shares, about $81bn; valued near $1.5tn; trading starts 19 Nov Nasdaq | The Desk 18 Nov 19:06 EST (price $83, 980m shares, $81.3bn, trading 19 Nov); TechCrunch via unite.ai (reported $83, $1.5tn fully diluted); CNBC/Reuters via AI Morning Brief |
| 4 | Voyager 1, a light-day away | NASA briefs today at noon ET (JPL); first human-made object 16bn miles out; a signal takes a day | NASA science.nasa.gov (briefing Thu 19 Nov 12pm EST); NASA JPL invite; PopSci (crossed 18 Nov 05:16:07 ET, ~16.09bn miles, confirm at 19 Nov conference) |
| 5 | Cyclone Akvan nears coast | Red alerts; schools shut; landfall due by noon tomorrow, Narsapur–Puri | IMD bulletin 27, 02:30 19 Nov via transclew (landfall by noon 20 Nov, 90–100 km/h gusting 110); The Hindu live (19 Nov 01:27 IST); Daily Jagran (red alert, schools shut 19–21 Nov in 6 Odisha districts) |
| 6 | India–Japan 2+2 talks | Fourth ministerial dialogue, Tokyo; Rajnath & Jaishankar meet Koizumi & Motegi | PIB press release (visit 18–19 Nov, dialogue 19 Nov); Hindu BusinessLine 18 Nov; ANI via alojapan (dialogue Thu 19 Nov) |

Wording discipline (judge checks facts): the trilateral is "meet" (planned/
scheduled — outcome NOT claimed); Voyager "briefs today" (crossing was 18 Nov
05:16 ET, confirmation is the 19 Nov event); Akvan "landfall due by noon
tomorrow" (landfall is 20 Nov, NOT 19 Nov); Anthropic "debuts" (pricing was
18 Nov evening, first trade is 19 Nov); GTA "rolls out at midnight, country
by country" (NZ first at 19 Nov local).

## 2. EXCLUDED — verified real stories with the WRONG date (do NOT add)

These appear in 19-Nov roundups but happened/were first reported 17–18 Nov.
Adding any as "19 November news" risks the judge's criterion 1/3 penalty.

| Story | True date | Evidence |
|---|---|---|
| Hakeem Jeffries nominated House Speaker (251–11) | Wed 18 Nov | AP + WaPo + NPR, 18 Nov 15:30Z; full House vote 3 Jan 2027 |
| Pew: Islam largest religion by 2035 (2.57bn vs 2.52bn) | 18 Nov 09:48 ET | pewresearch.org published 2026-11-18T09:48-05:00; AP 18 Nov |
| EU proposes €45bn Ukraine loan | Wed 18 Nov | Reuters Brussels 18 Nov; Agence Europe 18 Nov |
| Nvidia Q3: $115.8bn revenue; board rules out Huang return | 17 Nov (earnings); resignation 12 Nov | NVIDIA release 17 Nov; CNBC interview 17 Nov |
| Iran strikes US bases in Gulf / Kuwait Ali Al Salem | 18 Nov | Reuters 18 Nov (Enas Alashray) |
| England beat Australia, 3rd ODI, Duckett 133, series 2–1 | Wed 18 Nov | cricket.com.au + ESPNcricinfo, 18 Nov 11:25Z |
| Modi meets Prince & Princess of Wales, Delhi | Wed 18 Nov | IANS/BBC, 18 Nov |
| Great Unconformity / missing billion years (Nature) | Paper 4 Nov, coverage 11–16 Nov | Nature 4 Nov; Smithsonian 16 Nov |

## 3. Layout spec (1024x1024, exact)

- Canvas: RGB, paper `#F6F1E7` (246,241,231). Outer margin 36.
- Masthead: `THE WORLD TODAY`, DejaVu Sans Bold 64, ink `#141414`,
  centred, y=16. Date bar: black rect x36–988, y96–128; text
  `THURSDAY 19 NOVEMBER 2026`, DejaVu Sans Bold 27, white, centred, y=99.
  Red rule `#C0392B`, x36–988, y136–140.
- Lead panel: x36–988, y148–548. Vertical gradient stops:
  0.00 `#1B0B38`, 0.45 `#7B2D8B`, 0.75 `#E85D3D`, 1.00 `#F5A623`.
  Scrim band (drawn BEFORE sun/skyline): full panel width, y340–452,
  fill `(23,10,43)` alpha 110. Sun: centre (800,392), r=64,
  `#FFD166`, inner disc r=50 `#FFE08A`. Skyline: seeded
  `random.Random(19)`; buildings width 34–74, height 56–150, gap 2–10,
  fill `#170A2B`, from bottom y=548; windows 6x8 `#FFD166`, grid 16x18,
  probability 0.45, offset (8,12). (Palms were REMOVED — v1 rendered as
  spiky artefacts over the text.)
  - Kicker tag: red rounded rect, text `LEAD  •  CULTURE`, Bold 20,
    white, at (56,168). Headline `GTA VI IS HERE`, Bold 74, white,
    stroke 2 `#170A2B`, at (56,208). Sub `Vice City opens worldwide`,
    Bold 34, white, stroke 1, at (56,296). Fact lines, Regular 24,
    white, stroke 1, y=352,384,416:
    `After 13 years, Rockstar's sequel rolls out` /
    `at midnight, country by country — PS5 & Xbox.` /
    `Pre-orders: 15.9m copies, about $1.5bn.`
- Cards: white `#FFFFFF`, rounded radius 6, 2px ink outline. Kicker:
  24px icon (red) at (x+16, y+13), kicker text Bold 18 red at (x+48, y+12).
  Headline Bold 27 (row 2) / 26 (row 3), ink, at (x+16, y+40), leading
  32/31. Body Regular 20 (row 2, leading 24) / 19 (row 3, leading 23),
  ink, 6px below headline. Overflow guard in `card()`: body lines are
  truncated to `max(0, (yb-10-(yy+6)) // leading)` — never draw past the
  card bottom; if a body is cut, SHORTEN the copy, do not widen the card.
- Row 2, y562–756: card A x36–500 `DIPLOMACY  •  SHENZHEN` (globe icon),
  headline `Trump, Xi and Putin meet — a first`, body `First-ever
  three-way talks at APEC. Nuclear arms cuts and Iran on the agenda; no
  deal expected.` Card B x524–988 `MARKETS  •  NASDAQ` (chart icon),
  headline `Anthropic debuts as ANT`, body `Priced at $83, above its
  $70–$78 range. 980m shares, about $81bn; valued near $1.5tn.`
- Row 3, y770–962: card A x36–345 `SPACE  •  NASA` (signal icon),
  headline `Voyager 1, a light-day away`, body `NASA briefs today at
  noon ET. First object 16bn miles out — a signal takes a day.`
  Card B x357–666 `WEATHER  •  INDIA` (spiral icon), headline `Cyclone
  Akvan nears coast`, body `Red alerts; schools shut. Landfall due by
  noon tomorrow, Narsapur–Puri.` Card C x678–988 `DEFENCE  •  TOKYO`
  (flags icon), headline `India–Japan 2+2 talks`, body `Fourth
  ministerial dialogue. Rajnath & Jaishankar meet Koizumi & Motegi.`
- Footer: Regular 17, grey `#555555`, centred, y=972:
  `Thursday 19 November 2026  •  Sources: AP, Reuters, NASA, IMD, PIB, Rockstar Games`

## 4. Rendering recipe (reproduce byte-identically)

1. `python3 render.py` in the repo root (needs PIL locally; grader does
   NOT run this). Uses only `fonts/DejaVuSans.ttf` and
   `fonts/DejaVuSans-Bold.ttf` (vendored DejaVu, OFL). Deterministic:
   fixed seed 19, no timestamps, no network, no randomness besides the
   seeded skyline. `entry.png` is saved with `optimize=True`.
2. `main.py` is STDLIB-ONLY (imports `os`, `shutil`, `pathlib` only) and
   copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default
   `/output/entry.png`). It must NEVER import PIL — the grader runs
   `python3 -P -s /bot/main.py` in a pinned image without third-party
   packages (this exact failure rejected news-image-20261117 round 1).
3. Expected output: 1024x1024 RGB PNG, 142,627 bytes,
   sha256 `12fa345345b27e8dd4283f316d51e0df6b99c81d02119c6534827ca37a2cf748`
   (build 19 Nov 2026 ~00:35 UTC). Re-rendering from this spec must
   reproduce these bytes; if it does not, diff the render (do not edit
   the PNG by hand).

## 5. Verification commands (all run, all passed 19 Nov 2026 ~00:36 UTC)

```sh
# two clean-env runs + one as nobody from a read-only copy: all identical
rm -rf /tmp/out1 /tmp/out2 /tmp/out3 && mkdir -p /tmp/out3 && chmod 777 /tmp/out3
env -i MAKEFUN_OUTPUT_DIR=/tmp/out1 /usr/bin/python3 -P -s main.py
env -i MAKEFUN_OUTPUT_DIR=/tmp/out2 /usr/bin/python3 -P -s main.py
cp -r . /tmp/rotest/ && chmod 755 /tmp/rotest /tmp/rotest/fonts && chmod 644 /tmp/rotest/* /tmp/rotest/fonts/*
setpriv --reuid=65534 --regid=65534 --clear-groups env MAKEFUN_OUTPUT_DIR=/tmp/out3 /usr/bin/python3 -P -s /tmp/rotest/main.py
sha256sum /tmp/out1/entry.png /tmp/out2/entry.png /tmp/out3/entry.png entry.png
# -> 12fa345345b27e8dd4283f316d51e0df6b99c81d02119c6534827ca37a2cf748 (x4)
python3 -c "from PIL import Image; im=Image.open('entry.png'); im.verify(); print(Image.open('entry.png').size)"
# -> verified PNG (1024, 1024); bytes 142627 <= 1048576; IHDR 1024x1024
git ls-remote https://github.com/irfandihmtr/news-image-20261119.git HEAD
```

## 6. Final rebuild checklist (for the submit chat, before 21 Nov 07:00 WIB)

The day is only ~35 minutes old at build time. Before the final submit,
re-verify every headline and REPLACE any that a bigger 19-Nov story
displaces — the final poster must be the best summary of the FULL day:

1. Trilateral outcome (Shenzhen): did they meet? Any joint statement /
   nuclear or Iran announcement? If a deal or a walkout happened, it
   becomes story #2 with the outcome stated; if the meeting was cancelled,
   drop it and promote another story.
2. Anthropic first trade (Nasdaq, 09:30 ET 19 Nov): opening price / first-day
   move. Add the close only if it is verified from Reuters/Bloomberg/CNBC.
3. Voyager briefing (JPL, noon ET 19 Nov): confirmation signal received?
   Update the line only from NASA's own briefing.
4. Cyclone Akvan: landfall timing/place may shift (forecast: by noon 20 Nov,
   Narsapur–Puri). Update only from IMD bulletins; never state a landfall
   that has not happened.
5. Look for genuinely NEW 19-Nov stories that broke after 00:35 UTC
   (US markets close, Europe evening news, sport results played 19 Nov,
   any breaking news). Candidates must pass the §1 test: happened or first
   reported 19 Nov, >=2 independent sources.
6. NEVER promote a §2 story: Jeffries, Pew, EU loan, Nvidia, Iran–Gulf,
   ODI, Modi–Wales all stay excluded — their dates cannot change.
7. After any headline change: re-render (`python3 render.py`), re-check
   the image visually (no overflow, no icon/text collisions, legible at
   300px), re-run §5 verification, commit + push, and only then bundle/
   submit from the user-typed chat.
8. Do NOT bundle/submit from a handed-off side chat: the server's
   parent-chain gate refuses bundles from sessions the user did not open
   with their own typed prompt (proven twice). Build here; submit from the
   user-typed chat.
