#!/usr/bin/env python3
"""Cover and infographic for a pipeline article, rendered from its "## ИЗОБРАЖЕНИЯ" block.

    python3 render.py <article.md> <out_dir>

Writes to out_dir:
  <slug>-cover.jpg        1200x675, no text (brand palette, motif picked from the topic)
  <slug>-infographic.png  1200x900, the captions from "Подписи на картинке" as numbered cards
  <slug>-infographic-2.png, -3.png ...  one more per extra "### Инфографика N" / "### Схема N" block
  media.json              alt / title / caption / description / place for every image
                          ("images" list + legacy "cover"/"infographic" keys),
                          ready for wp_upload_media_from_url + wp_update_media

Every image block must have Alt, Caption and "Описание (медиатека WP)" (render refuses otherwise).

Needs Playwright with Chromium (PLAYWRIGHT_BROWSERS_PATH or executablePath /opt/pw-browsers/chromium)
and Pillow. Fonts (Manrope, OFL, Latin + Cyrillic) are in ./fonts.
"""
import asyncio, hashlib, html, json, os, random, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "fonts")

# ---------- parsing ----------

def field(text, name):
    m = re.search(r"\*\*" + re.escape(name) + r"[^*]*\*\*\s*(.+)", text)
    return m.group(1).strip() if m else ""

def section(text, title):
    m = re.search(r"^###\s*" + title + r"[^\n]*\n(.*?)(?=^###\s|\Z)", text, re.S | re.M)
    return m.group(1) if m else ""

def parse(md):
    # Drive's text export escapes markdown (\*\*, \#, \-, \_): undo it
    md = re.sub(r"\\([\\`*_{}\[\]()#+\-.!|<>~])", r"\1", md).replace("\r", "")
    head = md.split("\n---", 1)[0]
    slug = field(head, "Slug:") or "article"
    slug = re.sub(r"[^a-z0-9-]+", "-", slug.lower()).strip("-")
    lang = field(head, "Язык:") or "RU"
    topic = field(head, "Тема:")
    h1 = ""
    m = re.search(r"^#\s+(.+)$", md, re.M)
    if m:
        h1 = m.group(1).strip()
    block = md.split("## ИЗОБРАЖЕНИЯ", 1)[1] if "## ИЗОБРАЖЕНИЯ" in md else ""
    if not block:
        sys.exit("no '## ИЗОБРАЖЕНИЯ' block in the article")
    cov = section(block, "Обложка")
    extra = re.findall(r"^###\s*((?:Инфографика|Схема)[^\n]*)\n(.*?)(?=^###\s|\Z)", block, re.S | re.M)
    if not extra:
        sys.exit("no '### Инфографика' block in the article")

    def labels_of(sec, title):
        labels = []
        m = re.search(r"\*\*Подписи на картинке:\*\*(.*?)(?=\n\s*\*\*|\Z)", sec, re.S)
        if m:
            for line in m.group(1).splitlines():
                line = line.strip()
                if line.startswith(("- ", "• ", "* ")):
                    labels.append(line[2:].strip())
                elif line and not labels and not line.startswith("**"):
                    labels += [x.strip() for x in re.split(r";|\|", line) if x.strip()]
        labels = labels[:8]
        if len(labels) < 3:
            sys.exit(f"'{title}' needs at least 3 captions in 'Подписи на картинке'")
        return labels

    def meta(sec, fname, title):
        alt = field(sec, "Alt:")
        cap = field(sec, "Caption:")
        desc = field(sec, "Описание (медиатека WP):")
        miss = [n for n, v in (("Alt", alt), ("Caption", cap), ("Описание (медиатека WP)", desc)) if not v]
        if miss:
            sys.exit(f"'{title}': missing " + ", ".join(miss))
        return {"file": fname, "alt": alt, "caption": cap,
                "title": field(sec, "Заголовок (медиатека WP):") or alt, "description": desc}

    images = [dict(meta(cov, f"{slug}-cover.jpg", "Обложка"), kind="cover")]
    for n, (title, sec) in enumerate(extra, 1):
        fname = f"{slug}-infographic.png" if n == 1 else f"{slug}-infographic-{n}.png"
        img = dict(meta(sec, fname, title), kind="infographic")
        img["place_after"] = field(sec, "Место в статье:")
        img["labels"] = labels_of(sec, title)
        img["heading"] = field(sec, "Заголовок на картинке:") or ""
        images.append(img)
    out = {"slug": slug, "lang": lang, "topic": topic, "h1": h1, "images": images,
           "cover": images[0], "infographic": images[1]}
    return out

# ---------- drawing ----------

CSS_FONTS = "".join(
    f"@font-face{{font-family:M;src:url(file://{FONTS}/manrope-{sub}-{w}-normal.woff2);font-weight:{w}}}"
    for sub in ("latin", "cyrillic") for w in (500, 700, 800))
PAL = {"bg": "#0D1A2C", "card": "#132640", "line": "#1F3A5C", "em": "#00C696", "em2": "#5CF0C4",
       "yel": "#FFD23F", "txt": "#FFFFFF", "mut": "#9FB3C8"}

MOTIFS = [
    (r"robots|disallow|noindex|запрет", "doc_shield"),
    (r"sitemap|карт", "tree"),
    (r"redirect|редирект|переезд|migration|301", "arrows"),
    (r"backlink|link|ссылк|донор|anchor|анкор", "chain"),
    (r"log|googlebot|лог|бот", "bars"),
    (r"index|индекс|inspection|провер|verdict|вердикт|crawl|скан", "lens"),
]

def motif_svg(kind, rnd):
    e, e2, y, ln = PAL["em"], PAL["em2"], PAL["yel"], PAL["line"]
    if kind == "doc_shield":
        lines = "".join(f'<rect x="80" y="{90+i*42}" width="{rnd.randint(140,240)}" height="16" rx="8" fill="{ln}"/>' for i in range(6))
        return (f'<rect x="40" y="40" width="320" height="400" rx="26" fill="#132640" stroke="{ln}" stroke-width="4"/>{lines}'
                f'<path d="M300 250 l90 34 v70 c0 60 -40 96 -90 116 c-50 -20 -90 -56 -90 -116 v-70z" fill="{e}"/>'
                f'<path d="M262 352 l28 28 l52 -60" stroke="{PAL["bg"]}" stroke-width="16" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
    if kind == "tree":
        nodes = [(220, 70)] + [(90 + i * 130, 230) for i in range(3)] + [(50 + i * 85, 390) for i in range(5)]
        edges = "".join(f'<path d="M220 110 C220 170 {x} 160 {x} 200" stroke="{ln}" stroke-width="5" fill="none"/>' for x, _ in nodes[1:4])
        edges += "".join(f'<path d="M{nodes[1+i//2][0]} 260 C{nodes[1+i//2][0]} 320 {x} 320 {x} 360" stroke="{ln}" stroke-width="5" fill="none"/>' for i, (x, _) in enumerate(nodes[4:]))
        boxes = "".join(f'<rect x="{x-38}" y="{yy-30}" width="76" height="60" rx="14" fill="{e if i==0 else ("#132640" if i>3 else e2)}" stroke="{ln}" stroke-width="3"/>' for i, (x, yy) in enumerate(nodes))
        return edges + boxes
    if kind == "arrows":
        out = ""
        for i in range(3):
            yy = 90 + i * 140
            out += (f'<rect x="20" y="{yy}" width="130" height="80" rx="16" fill="#132640" stroke="{ln}" stroke-width="4"/>'
                    f'<path d="M165 {yy+40} H300" stroke="{e if i!=1 else y}" stroke-width="12" stroke-linecap="round"/>'
                    f'<path d="M285 {yy+18} L320 {yy+40} L285 {yy+62}" fill="none" stroke="{e if i!=1 else y}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>'
                    f'<rect x="335" y="{yy}" width="130" height="80" rx="16" fill="{e}"/>')
        return out
    if kind == "chain":
        out = ""
        for i in range(3):
            cx = 90 + i * 140
            out += f'<rect x="{cx-70}" y="{180+(i%2)*40}" width="160" height="90" rx="45" fill="none" stroke="{[e, e2, y][i]}" stroke-width="22"/>'
        return out + "".join(f'<circle cx="{rnd.randint(20,460)}" cy="{rnd.randint(30,450)}" r="{rnd.randint(4,9)}" fill="{e2}" opacity=".5"/>' for _ in range(10))
    if kind == "bars":
        out = f'<rect x="20" y="40" width="440" height="400" rx="24" fill="#132640" stroke="{ln}" stroke-width="4"/>'
        for i in range(8):
            h = rnd.randint(60, 300)
            out += f'<rect x="{50+i*50}" y="{410-h}" width="32" height="{h}" rx="8" fill="{y if i==5 else e}"/>'
        return out
    # lens / default
    lines = "".join(f'<rect x="70" y="{80+i*44}" width="{rnd.randint(150,260)}" height="16" rx="8" fill="{ln}"/>' for i in range(7))
    return (f'<rect x="30" y="30" width="330" height="410" rx="26" fill="#132640" stroke="{ln}" stroke-width="4"/>{lines}'
            f'<circle cx="300" cy="280" r="95" fill="rgba(0,198,150,.15)" stroke="{e}" stroke-width="22"/>'
            f'<path d="M368 348 L450 430" stroke="{e}" stroke-width="30" stroke-linecap="round"/>'
            f'<path d="M262 282 l26 26 l50 -56" stroke="{y}" stroke-width="14" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')

def cover_html(spec):
    seed = int(hashlib.sha1(spec["slug"].encode()).hexdigest()[:8], 16)
    rnd = random.Random(seed)
    hay = " ".join([spec["slug"], spec["topic"], spec["h1"]]).lower()
    kind = next((k for pat, k in MOTIFS if re.search(pat, hay)), "lens")
    side = rnd.choice([0, 1])
    dots = "".join(f'<circle cx="{rnd.randint(0,1200)}" cy="{rnd.randint(0,675)}" r="{rnd.choice([2,3,4])}" fill="#5CF0C4" opacity="{rnd.choice([.15,.25,.35])}"/>' for _ in range(70))
    gx = 300 if side else 900
    mx = 680 if side else 120
    return f"""<!doctype html><html><head><meta charset=utf-8><style>{CSS_FONTS}
html,body{{margin:0;width:1200px;height:675px;overflow:hidden;background:{PAL['bg']}}}</style></head><body>
<svg width="1200" height="675" viewBox="0 0 1200 675" xmlns="http://www.w3.org/2000/svg">
<defs><radialGradient id="g" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#00C696" stop-opacity=".30"/><stop offset="1" stop-color="#00C696" stop-opacity="0"/></radialGradient>
<pattern id="p" width="28" height="28" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.5" fill="#fff" opacity=".07"/></pattern></defs>
<rect width="1200" height="675" fill="url(#p)"/><circle cx="{gx}" cy="300" r="520" fill="url(#g)"/>{dots}
<rect x="{80 if side else 640}" y="250" width="{rnd.randint(260,380)}" height="18" rx="9" fill="#1F3A5C"/>
<rect x="{80 if side else 640}" y="290" width="{rnd.randint(180,300)}" height="18" rx="9" fill="#1F3A5C"/>
<rect x="{80 if side else 640}" y="330" width="120" height="18" rx="9" fill="#FFD23F" opacity=".8"/>
<g transform="translate({mx},100)">{motif_svg(kind, rnd)}</g></svg></body></html>"""

def infographic_html(spec, img):
    labels = img["labels"]
    n = len(labels)
    cols = 1 if n <= 3 else 2
    longest = max(len(x) for x in labels)
    fs = 34 if n <= 4 and longest < 60 else 30 if n <= 6 and longest < 80 else 26 if longest < 110 else 22
    title = img.get("heading") or spec["h1"] or spec["topic"]
    tfs = 46 if len(title) < 55 else 40 if len(title) < 80 else 34
    cards = "".join(f'<div class="c"><b>{i+1:02d}</b><span>{html.escape(t)}</span></div>' for i, t in enumerate(labels))
    return f"""<!doctype html><html><head><meta charset=utf-8><style>{CSS_FONTS}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1200px;height:900px;overflow:hidden}}
body{{font-family:M,sans-serif;color:#fff;background:{PAL['bg']};background-image:radial-gradient(rgba(255,255,255,.07) 1.5px,transparent 1.5px);background-size:28px 28px;padding:64px 70px;display:flex;flex-direction:column;gap:36px;position:relative}}
body:before{{content:"";position:absolute;width:800px;height:800px;border-radius:50%;background:radial-gradient(circle,rgba(0,198,150,.20),transparent 60%);right:-280px;top:-320px}}
h1{{font-weight:800;font-size:{tfs}px;line-height:1.12;letter-spacing:-.01em;max-width:1000px;position:relative}}
h1:after{{content:"";display:block;width:120px;height:8px;border-radius:4px;background:{PAL['em']};margin-top:22px}}
.g{{display:grid;grid-template-columns:repeat({cols},1fr);gap:20px;flex:1;align-content:center;position:relative}}
.c{{background:{PAL['card']};border:2px solid {PAL['line']};border-radius:22px;padding:22px 26px;display:flex;gap:20px;align-items:center;min-height:0}}
.c b{{font-weight:800;font-size:30px;color:{PAL['bg']};background:{PAL['em']};border-radius:14px;min-width:62px;height:62px;display:flex;align-items:center;justify-content:center}}
.c:nth-child(3n) b{{background:{PAL['yel']}}}
.c span{{font-weight:600;font-size:{fs}px;line-height:1.25}}
</style></head><body><h1>{html.escape(title)}</h1><div class="g">{cards}</div></body></html>"""

async def shoot(jobs):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        kw = {}
        exe = "/opt/pw-browsers/chromium"
        if os.path.exists(exe) and os.access(exe, os.X_OK):
            kw["executable_path"] = exe
        try:
            b = await p.chromium.launch(**kw)
        except Exception:
            b = await p.chromium.launch()
        for page_html, w, h, out in jobs:
            pg = await b.new_page(viewport={"width": w, "height": h})
            tmp = out + ".html"
            open(tmp, "w", encoding="utf-8").write(page_html)
            await pg.goto("file://" + os.path.abspath(tmp))
            await pg.evaluate("document.fonts.ready")
            await pg.wait_for_timeout(300)
            await pg.screenshot(path=out + ".raw.png")
            os.remove(tmp)
        await b.close()

def finish(raw, out, jpeg):
    from PIL import Image
    im = Image.open(raw).convert("RGB")
    if jpeg:
        im.save(out, "JPEG", quality=86, optimize=True, progressive=True)
    else:
        im.quantize(colors=128, method=Image.Quantize.MEDIANCUT).save(out, "PNG", optimize=True)
    os.remove(raw)

def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    md = open(sys.argv[1], encoding="utf-8").read()
    outdir = sys.argv[2]
    os.makedirs(outdir, exist_ok=True)
    spec = parse(md)
    c = os.path.join(outdir, spec["images"][0]["file"])
    jobs = [(cover_html(spec), 1200, 675, c)]
    infs = []
    for img in spec["images"][1:]:
        p = os.path.join(outdir, img["file"])
        jobs.append((infographic_html(spec, img), 1200, 900, p))
        infs.append(p)
    asyncio.run(shoot(jobs))
    finish(c + ".raw.png", c, True)
    for p in infs:
        finish(p + ".raw.png", p, False)
    json.dump(spec, open(os.path.join(outdir, "media.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    files = [c] + infs
    print(json.dumps({"files": files, "bytes": [os.path.getsize(f) for f in files]}, ensure_ascii=False))

if __name__ == "__main__":
    main()
