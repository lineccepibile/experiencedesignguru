# ExperienceDesignGuru website

Static site for experiencedesignguru.com. No framework and no build step on the server: every page is plain HTML.

## Pages

| Path | What it is |
|---|---|
| `/` | Holding page until the course pages exist, links to the About page |
| `/about/` | "My story" About page: a 3D pop-up book with seven chapters (Caorle, Milan, Logotel, Deloitte Digital, Dubai, The traveller, Now) |

## Editing the About page

Edit `src/about/index.src.html`, then rebuild:

```
python3 scripts/build-about.py
```

This writes `about/index.html`, filling in the image paths, the font path and the Lucide icons. Commit both files.

- **Chapters, wording, colours and pop-up pieces** live in the `spreads` array in the source. Each pop-up piece has a page side (`s:'l'` is the left page), a position and width in % of the page, a depth `z`, an optional tilt `r`, and a click reaction `act` (`jump`, `spin` or `ring`).
- **City photos** (full left page) are `assets/about/bg_*.webp`, already cropped to the page shape (0.875 wide to 1 tall). Never stretch a photo to fit: crop it.
- **Cut-outs** are `assets/about/*.webp` with a white paper edge, made from Unsplash photos (free licence, no credit needed).
- **Icons** are Lucide (`src/icons/`, ISC licence).

## The Youngest Script font

The script font is licensed, so it is **not** in this public repo (see `.gitignore`). The pages load it from `/assets/fonts/the-youngest-script.woff2` and fall back to Allura when it is missing. To use the real font, place the file in `assets/fonts/` before deploying, and check that the licence allows web embedding.

## Deploying

Cloudflare Pages, connected to this repo: framework preset "None", no build command, output directory `/`.

## Still to do

- Caorle photo with the coloured houses (current one is the bell tower)
- Linda to rewrite the draft copy in each chapter
- Link targets for "Explore the courses" (`#courses`) and "Get in touch" (`#contact`)
