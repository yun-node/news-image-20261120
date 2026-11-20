#!/usr/bin/env python3
"""Generate the news-image entry: a 1024x1024 infographic summing up
Friday 20 November 2026 world news, from news.json. Run: python3 generate_image.py
Writes entry.png next to this file (at most 1024x1024, under 1 MiB)."""
import json
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 1024, 1024
BG = (253, 252, 248)
INK = (17, 17, 17)
MUTED = (63, 63, 70)
FAINT = (113, 113, 122)
RULE = (228, 228, 224)
RED = (185, 28, 28)
MARGIN = 44

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)

F_KICKER = font("DejaVuSans-Bold.ttf", 22)
F_TITLE = font("DejaVuSans-Bold.ttf", 64)
F_DATE = font("DejaVuSans-Bold.ttf", 26)
F_TAG = font("DejaVuSans-Bold.ttf", 19)
F_HEAD = font("DejaVuSans-Bold.ttf", 30)
F_BODY = font("DejaVuSans.ttf", 22)
F_FOOT = font("DejaVuSans.ttf", 20)

def wrap(draw, text, fnt, max_w):
    lines, cur = [], ""
    for word in text.split():
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines

def main():
    with open(os.path.join(HERE, "news.json"), encoding="utf-8") as fh:
        data = json.load(fh)
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    content_w = W - 2 * MARGIN
    y = 36
    # Kicker
    d.text((MARGIN, y), "THE DAY IN ONE IMAGE", font=F_KICKER, fill=RED)
    y += 30
    # Title
    d.text((MARGIN, y), data["title"], font=F_TITLE, fill=INK)
    y += 80
    # Date
    d.text((MARGIN, y), data["date"].upper(), font=F_DATE, fill=MUTED)
    y += 32
    # Rule
    d.line([(MARGIN, y), (W - MARGIN, y)], fill=INK, width=3)
    y += 16
    # Stories
    for i, s in enumerate(data["stories"]):
        # Tag chip
        tag = s["tag"]
        tw = d.textlength(tag, font=F_TAG)
        chip_w, chip_h = int(tw) + 26, 26
        d.rounded_rectangle([MARGIN, y, MARGIN + chip_w, y + chip_h],
                            radius=13, fill=s["color"])
        d.text((MARGIN + 13, y + 4), tag, font=F_TAG, fill=(255, 255, 255))
        y += chip_h + 5
        # Headline
        for line in wrap(d, s["headline"], F_HEAD, content_w):
            d.text((MARGIN, y), line, font=F_HEAD, fill=INK)
            y += 36
        y += 2
        # Summary
        for line in wrap(d, s["summary"], F_BODY, content_w):
            d.text((MARGIN, y), line, font=F_BODY, fill=MUTED)
            y += 28
        y += 6
        # Divider between stories
        if i < len(data["stories"]) - 1:
            d.line([(MARGIN, y), (W - MARGIN, y)], fill=RULE, width=1)
            y += 9
    # Footer
    foot = data["footer"]
    fw = d.textlength(foot, font=F_FOOT)
    d.text(((W - fw) / 2, H - 34), foot, font=F_FOOT, fill=FAINT)
    out = os.path.join(HERE, "entry.png")
    img.save(out, "PNG", optimize=True)
    print(f"wrote {out} size={img.size} bytes={os.path.getsize(out)} final_y={y}")

if __name__ == "__main__":
    main()
