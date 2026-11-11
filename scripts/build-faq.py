#!/usr/bin/env python3
"""Builds faq/index.html (live site) and design/FAQ.dc.html (Claude Design board) from scripts/faq_data.py.
The FAQ page is deliberately not in the menu: it is for search engines and AI assistants (FAQPage structured data),
and is listed in sitemap.xml and llms.txt."""
import html, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from faq_data import FAQ
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E = html.escape
SITE = "https://experiencedesignguru.com"

def abs_url(u): return SITE + u if u.startswith("/") else u

ld = {"@context": "https://schema.org", "@graph": [
  {"@type": "FAQPage", "@id": SITE + "/faq/#faq", "url": SITE + "/faq/", "name": "Questions small travel business owners ask",
   "inLanguage": "en-GB", "isPartOf": {"@id": SITE + "/#website"}, "author": {"@id": SITE + "/about/#linda"},
   "mainEntity": [{"@type": "Question", "name": it["q"], "acceptedAnswer": {"@type": "Answer", "text": it["a"]}}
                  for g in FAQ for it in g["items"]]},
  {"@type": "BreadcrumbList", "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
    {"@type": "ListItem", "position": 2, "name": "FAQ", "item": SITE + "/faq/"}]}]}

def links_html(links):
    return " ".join(f'<a href="{E(u)}">{E(t)}</a>' for t, u in links)

groups = []
for g in FAQ:
    qs = "".join(f'''
<details>
<summary><span>{E(it["q"])}</span><svg aria-hidden="true" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 5v14M5 12h14"/></svg></summary>
<div class="ans"><p>{E(it["a"])}</p><p class="more">Go further: {links_html(it["links"])}</p></div>
</details>''' for it in g["items"])
    groups.append(f'<section><h2>{E(g["group"])}</h2>{qs}\n</section>')

page = f'''<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Guest experience questions from B&amp;B, tour and retreat owners · ExperienceDesignGuru</title>
<meta name="description" content="Straight answers to the questions small travel business owners ask: more direct bookings, five star reviews, standing out from other tours, filling a retreat, and getting AI assistants to recommend you. By Linda Covino, CCXP.">
<link rel="canonical" href="{SITE}/faq/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="ExperienceDesignGuru">
<meta property="og:url" content="{SITE}/faq/">
<meta property="og:title" content="Your guest experience questions, answered">
<meta property="og:description" content="How do I get more direct bookings for my B&amp;B? And other questions owners ask, answered by Linda Covino.">
<meta property="og:image" content="{SITE}/assets/about/og-my-story.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="alternate" type="text/plain" title="Summary for AI assistants" href="/llms.txt">
<script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False, indent=1)}
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Josefin+Sans:wght@600&family=Poppins:wght@400;500;600&display=swap" rel="stylesheet">
<style>
@font-face{{font-family:"YS";src:url(/assets/fonts/the-youngest-script.woff2) format("woff2");font-display:swap}}
*{{box-sizing:border-box}}
body{{margin:0;background:#EFEDE8;color:#1F1E1C;font-family:Poppins,system-ui,sans-serif;-webkit-font-smoothing:antialiased}}
a{{color:#1F1E1C}}a:hover{{color:#047A78}}
a:focus-visible,summary:focus-visible{{outline:3px solid #047A78;outline-offset:3px;border-radius:12px}}
.wrap{{max-width:860px;margin:0 auto;padding:0 clamp(20px,4vw,32px)}}
header{{max-width:1240px;margin:0 auto;padding:20px clamp(20px,4vw,32px);display:flex;align-items:center;justify-content:space-between;gap:12px}}
@media (max-width:480px){{header .btn{{padding:10px 14px;font-size:13px}}.logo b{{font-size:16px}}.logo span{{font-size:28px}}}}
.logo{{text-decoration:none;display:flex;align-items:baseline;gap:2px}}
.logo b{{font-weight:600;font-size:20px;letter-spacing:.02em}}
.logo span{{font-family:YS,cursive;font-size:34px;color:#C24F4F;line-height:1}}
.btn{{text-decoration:none;background:#047A78;color:#fff;padding:12px 22px;border-radius:999px;font-weight:500;font-size:15px}}
.btn:hover{{color:#fff}}
.eyebrow{{margin:0;font-family:"Josefin Sans",sans-serif;font-weight:600;font-size:14px;color:#55593E}}
h1{{margin:10px 0 14px;font-size:clamp(32px,5.4vw,48px);font-weight:600;line-height:1.15}}
h1 .s{{font-family:YS,cursive;font-weight:400;font-size:1.5em;color:#C24F4F}}
.lead{{margin:0;font-size:18px;line-height:1.6;color:#3A3934;max-width:640px}}
section{{margin-top:44px}}
h2{{margin:0 0 14px;font-size:15px;font-weight:600;color:#047A78}}
details{{background:#fff;border-radius:20px;margin-bottom:12px}}
summary{{list-style:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:16px;padding:20px 24px;font-size:18px;font-weight:500;line-height:1.4}}
summary::-webkit-details-marker{{display:none}}
summary svg{{flex:none;transition:transform 200ms cubic-bezier(.16,1,.3,1)}}
details[open] summary svg{{transform:rotate(45deg)}}
.ans{{padding:0 24px 22px}}
.ans p{{margin:0;font-size:16px;line-height:1.7;color:#3A3934}}
.ans .more{{margin-top:12px;font-size:14px;color:#4A4943}}
.ans .more a{{margin-right:10px}}
.cta{{margin:56px 0 72px;background:#1F1E1C;color:#EFEDE8;border-radius:28px;padding:clamp(28px,5vw,48px);display:flex;flex-wrap:wrap;gap:20px;align-items:center;justify-content:space-between}}
.cta p{{margin:0;font-size:20px;font-weight:500;max-width:460px;line-height:1.4}}
footer{{border-top:1px solid #D3CFC4}}
footer div{{max-width:1240px;margin:0 auto;padding:32px;display:flex;flex-wrap:wrap;justify-content:space-between;gap:16px;font-size:14px;color:#4A4943}}
@media (prefers-reduced-motion:reduce){{*{{transition:none !important}}}}
</style>
</head>
<body>
<header>
<a class="logo" href="/"><b>ExperienceDesign</b><span>Guru</span></a>
<a class="btn" href="https://stan.store/ExperienceDesignGuru">Browse courses</a>
</header>
<main class="wrap">
<p class="eyebrow">Questions owners ask me</p>
<h1>Your guest experience <span class="s">questions</span></h1>
<p class="lead">The questions B&amp;B owners, tour guides and retreat planners ask me most, in their own words, with the short answer. I'm Linda Covino, an experience designer and Certified Customer Experience Professional (CCXP).</p>
{"".join(groups)}
<div class="cta"><p>Got a question that isn't here? Ask me on Instagram.</p><a class="btn" href="https://www.instagram.com/experiencedesignguru/">Message @experiencedesignguru</a></div>
</main>
<footer><div><span>© 2026 Carmelinda Covino · ExperienceDesignGuru</span><span><a href="/">Home</a> · <a href="/about/">About</a> · <a href="https://stan.store/ExperienceDesignGuru">Store</a></span></div></footer>
</body>
</html>
'''
os.makedirs(os.path.join(ROOT, "faq"), exist_ok=True)
open(os.path.join(ROOT, "faq", "index.html"), "w").write(page)
print("faq/index.html", len(page), "questions:", sum(len(g["items"]) for g in FAQ))
