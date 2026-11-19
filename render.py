#!/usr/bin/env python3
"""Render the 19 November 2026 front-page poster (1024x1024) to entry.png.

Run: python3 render.py  (writes entry.png next to this file)
Deterministic: fixed seed, fixed fonts, no timestamps, no network.
Fonts are vendored under fonts/ (DejaVu Sans, SIL OFL).
"""
import math
import random
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (246, 241, 231)
INK = (20, 20, 20)
RED = (192, 57, 43)
WHITE = (255, 255, 255)
GREY = (85, 85, 85)
CARD = (255, 255, 255)

F_B = "fonts/DejaVuSans-Bold.ttf"
F_R = "fonts/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def vgrad(draw, box, stops):
    """Vertical gradient across box from a list of (pos, color) stops."""
    x0, y0, x1, y1 = box
    n = y1 - y0
    for y in range(n):
        t = y / max(n - 1, 1)
        for i in range(len(stops) - 1):
            p0, c0 = stops[i]
            p1, c1 = stops[i + 1]
            if p0 <= t <= p1:
                f = 0 if p1 == p0 else (t - p0) / (p1 - p0)
                col = lerp(c0, c1, f)
                break
        else:
            col = stops[-1][1]
        draw.line([(x0, y0 + y), (x1, y0 + y)], fill=col)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, lines, fnt, fill, leading=None):
    if leading is None:
        leading = int(fnt.size * 1.22)
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def kicker(draw, x, y, label, fnt):
    tw = draw.textlength(label, font=fnt)
    pad = 10
    draw.rounded_rectangle([x, y, x + tw + pad * 2, y + fnt.size + 12],
                           radius=4, fill=RED)
    draw.text((x + pad, y + 5), label, font=fnt, fill=WHITE)
    return y + fnt.size + 12


# ---------------------------------------------------------------- icons
def icon_globe(d, cx, cy, r, col):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=col, width=4)
    d.ellipse([cx - r * 0.45, cy - r, cx + r * 0.45, cy + r],
              outline=col, width=3)
    d.line([(cx - r, cy), (cx + r, cy)], fill=col, width=3)
    d.arc([cx - r, cy - r * 0.55, cx + r, cy + r * 0.55],
          start=200, end=340, fill=col, width=3)
    d.arc([cx - r, cy - r * 0.55, cx + r, cy + r * 0.55],
          start=20, end=160, fill=col, width=3)


def icon_chart(d, x, y, s, col):
    pts = [(x, y + s * 0.75), (x + s * 0.3, y + s * 0.5),
           (x + s * 0.55, y + s * 0.62), (x + s, y + s * 0.15)]
    d.line(pts, fill=col, width=5, joint="curve")
    d.polygon([(x + s, y + s * 0.15), (x + s * 0.78, y + s * 0.15),
               (x + s, y + s * 0.38)], fill=col)
    d.line([(x, y + s), (x + s, y + s)], fill=col, width=4)


def icon_signal(d, cx, cy, r, col):
    """Radiating signal arcs from a dot: deep-space contact."""
    d.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=col)
    for rr, w in ((r * 0.55, 3), (r, 3)):
        d.arc([cx - rr, cy - rr, cx + rr, cy + rr],
              start=315, end=45, fill=col, width=w)


def icon_spiral(d, cx, cy, rmax, col):
    pts = []
    for a in range(0, 540, 6):
        rad = 2 + a * (rmax - 2) / 540.0
        th = math.radians(a)
        pts.append((cx + rad * math.cos(th), cy + rad * math.sin(th)))
    d.line(pts, fill=col, width=3, joint="curve")


def icon_flags(d, x, y, s, col):
    d.rectangle([x, y, x + s * 0.45, y + s], fill=col)
    d.rectangle([x + s * 0.55, y, x + s, y + s], outline=col, width=4)
    d.ellipse([x + s * 0.12, y + s * 0.32, x + s * 0.33, y + s * 0.53],
              fill=WHITE)
    d.ellipse([x + s * 0.67, y + s * 0.32, x + s * 0.88, y + s * 0.53],
              outline=col, width=3)


# ---------------------------------------------------------------- build
def build():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # --- masthead
    f_title = font(F_B, 64)
    f_date = font(F_B, 27)
    title = "THE WORLD TODAY"
    tw = d.textlength(title, font=f_title)
    d.text(((W - tw) / 2, 16), title, font=f_title, fill=INK)
    d.rectangle([36, 96, 988, 128], fill=INK)
    date = "THURSDAY 19 NOVEMBER 2026"
    dw = d.textlength(date, font=f_date)
    d.text(((W - dw) / 2, 99), date, font=f_date, fill=WHITE)
    d.rectangle([36, 136, 988, 140], fill=RED)

    # --- lead panel: Vice City dusk
    x0, y0, x1, y1 = 36, 148, 988, 548
    vgrad(d, (x0, y0, x1, y1), [
        (0.0, (27, 11, 56)), (0.45, (123, 45, 139)),
        (0.75, (232, 93, 61)), (1.0, (245, 166, 35))])
    # lead text scrim: full-width dusk band behind the fact lines,
    # drawn BEFORE sun + skyline so both stay bright over it
    scrim = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(scrim)
    sd.rectangle([x0, 340, x1, 452], fill=(23, 10, 43, 110))
    img = Image.alpha_composite(img.convert("RGBA"), scrim).convert("RGB")
    d = ImageDraw.Draw(img)
    # sun
    sx, sy, sr = 800, 392, 64
    d.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=(255, 209, 102))
    d.ellipse([sx - sr + 14, sy - sr + 14, sx + sr - 14, sy + sr - 14],
              fill=(255, 224, 138))
    # skyline
    rng = random.Random(19)
    bx = x0
    while bx < x1:
        bw = rng.randint(34, 74)
        bh = rng.randint(56, 150)
        by = y1 - bh
        d.rectangle([bx, by, bx + bw, y1], fill=(23, 10, 43))
        for wy in range(by + 12, y1 - 10, 18):
            for wx in range(bx + 8, bx + bw - 8, 16):
                if rng.random() < 0.45:
                    d.rectangle([wx, wy, wx + 6, wy + 8],
                                fill=(255, 209, 102))
        bx += bw + rng.randint(2, 10)
    # lead text (left, over sky, above skyline)
    f_kick = font(F_B, 20)
    f_head = font(F_B, 74)
    f_sub = font(F_B, 34)
    f_fact = font(F_R, 24)
    kicker(d, 56, 168, "LEAD  •  CULTURE", f_kick)
    d.text((56, 208), "GTA VI IS HERE", font=f_head, fill=WHITE,
           stroke_width=2, stroke_fill=(23, 10, 43))
    d.text((56, 296), "Vice City opens worldwide", font=f_sub, fill=WHITE,
           stroke_width=1, stroke_fill=(23, 10, 43))
    y = 352
    for ln in ["After 13 years, Rockstar's sequel rolls out",
               "at midnight, country by country — PS5 & Xbox.",
               "Pre-orders: 15.9m copies, about $1.5bn."]:
        d.text((56, y), ln, font=f_fact, fill=WHITE,
               stroke_width=1, stroke_fill=(23, 10, 43))
        y += 32

    # --- story cards
    f_ck = font(F_B, 18)
    f_ch = font(F_B, 27)
    f_cb = font(F_R, 20)
    f_ch3 = font(F_B, 26)
    f_cb3 = font(F_R, 19)

    def card(xa, ya, xb, yb, kick, head, body, icon, small=False):
        d.rounded_rectangle([xa, ya, xb, yb], radius=6, fill=CARD,
                            outline=INK, width=2)
        # icon inline at the left of the kicker line (never over headline)
        icon(d, xa + 16, ya + 13, 24, RED)
        d.text((xa + 48, ya + 12), kick, font=f_ck, fill=RED)
        f_h = f_ch3 if small else f_ch
        f_b = f_cb3 if small else f_cb
        lh = 31 if small else 32
        lb = 23 if small else 24
        hl = wrap(d, head, f_h, (xb - xa) - 32)
        yy = text_block(d, xa + 16, ya + 40, hl, f_h, INK, leading=lh)
        bl = wrap(d, body, f_b, (xb - xa) - 32)
        # mechanical overflow guard: never draw past the card's bottom
        max_lines = max(0, (yb - 10 - (yy + 6)) // lb)
        bl = bl[:max_lines]
        text_block(d, xa + 16, yy + 6, bl, f_b, INK, leading=lb)

    # row 2: two wide cards
    card(36, 562, 500, 756, "DIPLOMACY  •  SHENZHEN",
         "Trump, Xi and Putin meet — a first",
         "First-ever three-way talks at APEC. Nuclear arms cuts "
         "and Iran on the agenda; no deal expected.",
         lambda dd, x, y, s, c: icon_globe(dd, x + s // 2, y + s // 2,
                                           s // 2, c))
    card(524, 562, 988, 756, "MARKETS  •  NASDAQ",
         "Anthropic debuts as ANT",
         "Priced at $83, above its $70–$78 range. 980m shares, "
         "about $81bn; valued near $1.5tn.",
         lambda dd, x, y, s, c: icon_chart(dd, x, y, s, c))

    # row 3: three cards
    card(36, 770, 345, 962, "SPACE  •  NASA",
         "Voyager 1, a light-day away",
         "NASA briefs today at noon ET. First object 16bn miles "
         "out — a signal takes a day.",         lambda dd, x, y, s, c: icon_signal(dd, x + s // 2, y + s // 2,
                                          s // 2, c),
         small=True)
    card(357, 770, 666, 962, "WEATHER  •  INDIA",
         "Cyclone Akvan nears coast",
         "Red alerts; schools shut. Landfall due by noon "
         "tomorrow, Narsapur–Puri.",
         lambda dd, x, y, s, c: icon_spiral(dd, x + s // 2, y + s // 2,
                                          s // 2, c),
         small=True)
    card(678, 770, 988, 962, "DEFENCE  •  TOKYO",
         "India–Japan 2+2 talks",
         "Fourth ministerial dialogue. Rajnath & Jaishankar meet "
         "Koizumi & Motegi.",
         lambda dd, x, y, s, c: icon_flags(dd, x, y, s, c),
         small=True)

    # --- footer
    f_ft = font(F_R, 17)
    foot = "Thursday 19 November 2026  •  Sources: AP, Reuters, NASA, IMD, PIB, Rockstar Games"
    fw = d.textlength(foot, font=f_ft)
    d.text(((W - fw) / 2, 972), foot, font=f_ft, fill=GREY)

    img.save("entry.png", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    build()
