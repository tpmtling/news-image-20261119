"""Render news_image.png — a newspaper front page for 19 Nov 2026.

Run with Pillow available:  python3 make_image.py
Output is a deterministic 1024 x 1024 PNG beside this file.
"""

import os
import textwrap

from PIL import Image, ImageDraw, ImageFont

from news_data import BRIEFS, STORIES

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "news_image.png")

W = H = 1024
PAPER = (248, 244, 233)
INK = (28, 26, 23)
MUTED = (96, 90, 80)
RED = (155, 27, 27)
RULE = (70, 64, 56)
HAIR = (196, 188, 168)

SERIF = "/usr/share/fonts/truetype/noto/NotoSerif-Regular.ttf"
SERIF_B = "/usr/share/fonts/truetype/noto/NotoSerif-Bold.ttf"
SERIF_I = "/usr/share/fonts/truetype/noto/NotoSerif-Italic.ttf"
DISPLAY = "/usr/share/fonts/truetype/noto/NotoSerifDisplay-Black.ttf"
SANS = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap measured in pixels."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_block(draw, x, y, width, lines, fnt, fill, leading):
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def centred(draw, y, text, fnt, fill):
    w = draw.textlength(text, font=fnt)
    draw.text(((W - w) / 2, y), text, font=fnt, fill=fill)
    return y + fnt.size


def main():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    margin = 46
    right = W - margin
    width = right - margin

    # --- masthead -------------------------------------------------
    y = 18
    centred(draw, y, "THE  WORLD  TODAY", font(DISPLAY, 68), INK)
    y += 82
    draw.line([(margin, y), (right, y)], fill=RULE, width=1)
    y += 6
    centred(
        draw, y,
        "Thursday, 19 November 2026  ·  Shenzhen  ·  The Hague  ·  Gaza  ·  Deep Space",
        font(SANS, 15), MUTED,
    )
    y += 24
    draw.rectangle([(margin, y), (right, y + 6)], fill=RED)
    y += 18

    lead = [s for s in STORIES if s["lead"]][0]
    rest = [s for s in STORIES if not s["lead"]]

    # --- lead story -----------------------------------------------
    draw.text((margin, y), lead["kicker"], font=font(SANS_B, 16), fill=RED)
    y += 24
    hf = font(SERIF_B, 40)
    lines = wrap(draw, lead["headline"], hf, width)
    y = draw_block(draw, margin, y, width, lines, hf, INK, 46)
    y += 3
    df = font(SERIF, 18)
    lines = wrap(draw, lead["deck"], df, width)
    y = draw_block(draw, margin, y, width, lines, df, (52, 48, 42), 24)
    y += 4
    draw.text(
        (margin, y),
        "Sources: " + lead["source"],
        font=font(SERIF_I, 13), fill=MUTED,
    )
    y += 22
    draw.line([(margin, y), (right, y)], fill=RULE, width=2)
    y += 14

    # --- two columns ----------------------------------------------
    gap = 30
    col_w = (width - gap) // 2
    col_x = [margin, margin + col_w + gap]
    columns = [rest[:3], rest[3:]]
    col_y = [y, y]
    for ci, stories in enumerate(columns):
        x, cy = col_x[ci], col_y[ci]
        for si, story in enumerate(stories):
            draw.text((x, cy), story["kicker"], font=font(SANS_B, 13), fill=RED)
            cy += 19
            hf = font(SERIF_B, 21)
            lines = wrap(draw, story["headline"], hf, col_w)
            cy = draw_block(draw, x, cy, col_w, lines, hf, INK, 25)
            cy += 2
            df = font(SANS, 14)
            lines = wrap(draw, story["deck"], df, col_w)
            cy = draw_block(draw, x, cy, col_w, lines, df, (58, 54, 47), 18)
            cy += 7
            if si < len(stories) - 1:
                draw.line([(x, cy), (x + col_w, cy)], fill=HAIR, width=1)
                cy += 9
        col_y[ci] = cy
    # centre rule between the columns
    bottom_cols = max(col_y)
    mid = margin + col_w + gap // 2
    draw.line([(mid, y), (mid, bottom_cols - 6)], fill=HAIR, width=1)
    y = bottom_cols + 2

    # --- briefs strip ---------------------------------------------
    draw.line([(margin, y), (right, y)], fill=RULE, width=2)
    y += 10
    draw.text((margin, y), "IN BRIEF", font=font(SANS_B, 15), fill=RED)
    y += 22
    bf = font(SANS, 14)
    for brief in BRIEFS:
        lines = wrap(draw, "•  " + brief, bf, width)
        y = draw_block(draw, margin, y, width, lines, bf, (52, 48, 42), 18)
        y += 2
    y += 4
    draw.line([(margin, y), (right, y)], fill=RED, width=3)
    y += 8
    centred(
        draw, y,
        "One page, one day: the world on Thursday, 19 November 2026.",
        font(SERIF_I, 13), MUTED,
    )

    img.save(OUT, format="PNG", optimize=True)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
