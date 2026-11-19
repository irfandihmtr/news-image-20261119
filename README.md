# news-image-20261119 — "The World Today"

Front-page poster summing up Thursday 19 November 2026 in one image
(1024×1024 PNG). Lead: GTA VI launches worldwide. Also: the first-ever
Trump–Xi–Putin trilateral in Shenzhen, Anthropic's Nasdaq debut as ANT,
NASA's Voyager 1 one-light-day briefing, Cyclone Akvan bearing down on
India's east coast, and the India–Japan 2+2 dialogue in Tokyo.

## Files

- `entry.png` — the image (1024×1024, rendered by `render.py`).
- `main.py` — stdlib-only entrypoint: copies `entry.png` to
  `/output/entry.png`. This is the file the grader runs.
- `render.py` — the PIL renderer that draws `entry.png` from scratch
  (deterministic, seeded; run `python3 render.py` to reproduce it).
- `fonts/` — vendored DejaVu Sans (regular + bold).
- `BUILD_SPEC.md` — the full rebuild spec: headlines, sources, layout,
  rendering recipe and verification commands.

## Verify

```sh
rm -rf /tmp/out1 /tmp/out2
env -i MAKEFUN_OUTPUT_DIR=/tmp/out1 /usr/bin/python3 -P -s main.py
env -i MAKEFUN_OUTPUT_DIR=/tmp/out2 /usr/bin/python3 -P -s main.py
sha256sum /tmp/out1/entry.png /tmp/out2/entry.png entry.png
```
