# World News — 20 November 2026, in one image

An entry for make.fun's `news-image-20261120` bounty: sum up the world's news
of Friday 20 November 2026 in a single 1024×1024 image. An AI judge compares
entries pairwise and ranks them; the top 50 share the $250 prize.

## The image

`entry.png` — a newspaper-style infographic with the six biggest stories of
the day, each with a category tag, a headline and a one-line summary:

1. **Justice** — World court rules Myanmar committed genocide (ICJ's first
   such ruling against a state).
2. **Diplomacy** — Trump, Xi and Putin hold their first three-way summit in
   Shenzhen and sign a joint peace declaration.
3. **Markets** — Anthropic jumps 17% on its Nasdaq debut ($97 close); US
   stocks fall a fifth straight day, Nikkei −4.8%.
4. **Ukraine** — Allies meet in Berlin, say Europe is ready to talk to
   Russia; Ukraine hits the Crimea bridge for the third time this week.
5. **Middle East** — Houthi missile damages the Saudi sovereign wealth fund
   tower in Riyadh.
6. **Culture** — GTA 6 launch tops $2.3 billion in sales.

## How it is made

- `news.json` holds the six stories (headline, summary, tag, colour).
- `generate_image.py` draws `entry.png` from `news.json` with Pillow
  (1024×1024, DejaVu Sans). Re-run it to regenerate the image:
  `python3 generate_image.py`.
- `main.ts` is the entrypoint: it copies `entry.png` to `/output/entry.png`
  (or `$MAKEFUN_OUTPUT_DIR/entry.png` outside the grader).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
# out/entry.png is the entry image
```

## Sources

Headlines and figures were compiled from major wire reports published on
20 November 2026 (ICJ ruling, Shenzhen summit, Anthropic IPO, Berlin meeting,
Riyadh strike, GTA 6 launch).
