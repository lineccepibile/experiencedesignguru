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

## Search and AI discovery

What is already in the code:

- `robots.txt`: welcomes search engines and AI assistants by name (ChatGPT, Claude, Perplexity, Gemini, Apple, Bing), with a Content-Signal line (search yes, AI answers yes, AI training yes: change `ai-train` to `no` to opt out of training only).
- `sitemap.xml`: every public page. Add each new page here.
- `llms.txt`: a plain summary of ExperienceDesignGuru, the courses, the free guides and Linda, written for AI assistants.
- Structured data (JSON-LD): the home page describes the organisation, the website, Linda and the courses; the About page is a ProfilePage for Linda. Keep the course list in step with the store.
- Every page has a title, a description, a canonical link and a social share preview (`assets/about/og-my-story.jpg`).
- The About book's full story is written into the page (`#srstory`), so crawlers that do not run JavaScript can still read it.

At launch (in this order):

1. **Cloudflare: let AI crawlers in.** Cloudflare blocks AI crawlers by default on new domains. In the dashboard for experiencedesignguru.com, under AI Crawl Control, allow the search and assistant crawlers, and turn off Cloudflare's managed robots.txt so it does not replace ours. Then open https://experiencedesignguru.com/robots.txt and check it shows our file.
2. **Google Search Console:** add the domain, submit `sitemap.xml`.
3. **Bing Webmaster Tools:** import from Search Console and submit the sitemap. Bing's index feeds ChatGPT search and Copilot.
4. Check the structured data with Google's Rich Results Test on `/` and `/about/`.

Content that helps most (to add in the design):

- One page per course, with its own clear heading, who it is for, what you learn and a link to the store. AI assistants recommend pages that answer one question well.
- A short FAQ on the home page, in the words owners use ("How do I get more direct bookings for my B&B?", "How do I make guests remember my tour?").
- Descriptive alt text on every image, and real text instead of text inside images.
- Link the site from Instagram, Stan, The Visualler and LinkedIn, and keep the name "ExperienceDesignGuru" and "Linda Covino" written the same way everywhere.

## Still to do

- Caorle photo with the coloured houses (current one is the bell tower)
- Linda to rewrite the draft copy in each chapter
- Link target for "Get in touch" (`#contact`)

## FAQ page (hidden)

`/faq/` is not in the menu on purpose. It answers owners' questions in their own words for search engines and AI assistants (FAQPage structured data) and is listed in sitemap.xml and llms.txt. Edit the questions in `scripts/faq_data.py`, then run `python3 scripts/build-faq.py`.
