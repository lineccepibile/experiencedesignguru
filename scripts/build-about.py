"""Build about/index.html from src/about/index.src.html.

Run from the repo root:  python3 scripts/build-about.py

Placeholders in the source:
  {{IMG:name}}   -> /assets/about/name.webp
  {{FONT}}       -> /assets/fonts/the-youngest-script.woff2 (licensed, not committed)
  {{ICON:name}}  -> the Lucide SVG from src/icons/name.svg, inlined
"""
import re
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
src = (ROOT / 'src/about/index.src.html').read_text()

src = src.replace('{{FONT}}', '/assets/fonts/the-youngest-script.woff2')


def img(m):
    name = m.group(1)
    path = ROOT / f'assets/about/{name}.webp'
    assert path.exists(), f'missing image {path}'
    return f'/assets/about/{name}.webp'


src = re.sub(r'\{\{IMG:(\w+)\}\}', img, src)


def icon(m):
    s = (ROOT / f'src/icons/{m.group(1)}.svg').read_text()
    s = re.sub(r'<!--.*?-->', '', s, flags=re.S).strip()
    s = re.sub(r'\s(width|height)="24"', '', s).replace('stroke-width="2"', 'stroke-width="1.8"')
    return s.replace('\n', '').replace('`', '')


src = re.sub(r'\{\{ICON:([\w-]+)\}\}', icon, src)

assert '{{' not in src, 'unfilled placeholder'
out = ROOT / 'about/index.html'
out.write_text(src)
print(f'{out.relative_to(ROOT)}  {len(src) // 1024} KB')
