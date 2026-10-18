import os, subprocess, sys
D = os.path.dirname(os.path.abspath(__file__))

LAYOUT = {
 'P': (1000, 1500, """
.wrap{position:absolute;inset:0;padding:56px 64px}
.logo{left:64px;top:56px}
.head{margin-top:92px}
.hook{font-size:var(--hp,92px);margin-top:22px}
.sub{font-size:30px;margin-top:20px}
.main{margin-top:30px}
.extra{margin-top:22px}
.foot{padding:0 64px 44px;font-size:20px}
"""),
 'S': (1080, 1350, """
.wrap{position:absolute;inset:0;padding:52px 60px}
.logo{left:60px;top:52px;height:50px}
.head{margin-top:80px}
.hook{font-size:var(--hs,78px);margin-top:18px}
.sub{font-size:26px;margin-top:14px}
.main{margin-top:24px}
.extra{margin-top:16px}
.foot{padding:0 60px 34px;font-size:18px}
.card{padding:24px 30px}
"""),
 'X': (1600, 900, """
.wrap{position:absolute;inset:0;padding:48px 64px;display:grid;grid-template-columns:600px 1fr;column-gap:56px;grid-template-rows:auto 1fr}
.logo{left:64px;top:44px;height:46px}
.head{grid-column:1;grid-row:1 / span 2;margin-top:92px}
.hook{font-size:var(--hx,74px);margin-top:20px}
.sub{font-size:24px;margin-top:16px}
.main{grid-column:2;grid-row:1 / span 2;align-self:center}
.extra{margin-top:26px}
.foot{padding:0 64px 32px;font-size:18px}
"""),
}

def page(name, fmt, head, main, extra, foot_l, css=''):
    w, h, lay = LAYOUT[fmt]
    html = f"""<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="base.css">
<style>:root{{--w:{w}px;--h:{h}px}}{lay}{css}</style></head><body class="{fmt}"><div class="glow"></div>
<img class="logo" src="logo.png">
<div class="wrap"><div class="head">{head}{extra if fmt=='X' else ''}</div><div class="main">{main}{extra if fmt in ('P','S') else ''}</div></div>
<div class="foot"><span>{foot_l}</span><b>en.speedyindex.com</b></div></body></html>"""
    p = os.path.join(D, f'{name}_{fmt}.html'); open(p, 'w').write(html)
    return p, w, h

COMMON = """
.card{padding:30px 34px}
.warn{border-radius:22px;background:rgba(255,92,122,.12);border:2px solid var(--cor);padding:22px 28px;font-size:26px;font-weight:700}
.warn b{color:var(--cor)}
.cta{margin-top:16px;border-radius:22px;background:var(--em);color:#0D1A2C;padding:22px 28px;font-size:26px;font-weight:800}
.X .warn,.X .cta{font-size:22px;padding:18px 22px}
table{width:100%;border-collapse:separate;border-spacing:0 12px}
th{text-align:left;color:var(--mut);font-size:20px;font-weight:700;text-transform:uppercase;letter-spacing:.05em;padding:0 14px}
td{background:#0B1626;border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:22px 14px;font-size:26px;font-weight:700;vertical-align:middle}
td:first-child{border-left:1px solid var(--line);border-radius:14px 0 0 14px;color:#fff}
td:last-child{border-right:1px solid var(--line);border-radius:0 14px 14px 0}
.yes{color:var(--em);font-weight:800}.no{color:var(--cor);font-weight:800}.mid{color:var(--yel);font-weight:800}
.ic{display:inline-block;width:38px;height:38px;border-radius:50%;text-align:center;line-height:38px;font-size:24px;font-weight:800;margin-right:10px;color:#0D1A2C}
.ic.y{background:var(--em)}.ic.n{background:var(--cor)}.ic.m{background:var(--yel)}
small{display:block;color:var(--mut);font-size:18px;font-weight:600;margin-top:6px}
"""

ITEMS = {}

# 1 link velocity
ITEMS['ig01_velocity'] = dict(
 head='<span class="pill">Drip-Feed pace</span><div class="hook">How many links a day should you <span class="y">send?</span></div><div class="sub">Recommended Drip-Feed pace by site authority</div>',
 main='''<div class="card vel">
 <div class="row"><div class="lab"><span class="n">New site</span><span class="a">under 6 months, limited history</span></div>
  <div class="track"><div class="seg" style="left:3.33%;width:6.67%;background:var(--yel)"></div><div class="seg" style="left:12%;width:30%;color:var(--yel);justify-content:flex-start">5–15/day</div></div>
  <div class="wk">Start at the minimum · ≈ 35–105 URLs per week</div></div>
 <div class="row"><div class="lab"><span class="n">Medium-authority site</span><span class="a"></span></div>
  <div class="track"><div class="seg" style="left:13.33%;width:20%;background:var(--em2)"></div><div class="seg" style="left:35%;width:30%;color:var(--em2);justify-content:flex-start">20–50/day</div></div>
  <div class="wk">≈ 140–350 URLs per week</div></div>
 <div class="row" style="margin-bottom:14px"><div class="lab"><span class="n">High-authority site</span><span class="a"></span></div>
  <div class="track"><div class="seg" style="left:33.33%;width:66.67%;background:var(--em)">50–150/day</div></div>
  <div class="wk">≈ 350–1,050 URLs per week</div></div>
 <div class="axis"><span>0</span><span>50</span><span>100</span><span>150 URLs/day</span></div></div>''',
 extra='<div class="extra"><div class="warn"><b>Everything on day one</b> = one giant spike. Drip Feed spreads the same batch evenly over several days.</div><div class="cta">One task, spread over N days → Drip Feed in SpeedyIndex</div></div>',
 foot='Pace: SpeedyIndex Drip-Feed recommendations',
 css='''.vel .row{margin-bottom:18px}.vel .lab{display:flex;justify-content:space-between;align-items:baseline}.vel .lab .n{font-size:30px;font-weight:800}.vel .lab .a{font-size:21px;color:var(--mut);font-weight:600}
.vel .track{position:relative;height:56px;margin-top:12px;border-radius:14px;background:#0B1626;border:1px solid var(--line)}
.vel .seg{position:absolute;top:0;bottom:0;border-radius:14px;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:28px;color:#0D1A2C}
.vel .wk{font-size:21px;color:var(--mut);margin-top:8px;font-weight:600}.vel .wk b{color:#fff}
.vel .axis{display:flex;justify-content:space-between;color:var(--mut);font-size:18px;font-weight:600}
.X .vel .row{margin-bottom:16px}.X .vel .track{height:48px}.X .vel .lab .n{font-size:26px}''',
 hp='96px', hx='76px')

# 2 robots vs noindex
ITEMS['ig02_robots'] = dict(
 head='<span class="pill">Indexing myths</span><div class="hook">robots.txt is <span class="c">not</span> a delete button</div><div class="sub">Disallow and noindex do different jobs. Mixing them up keeps pages in Google.</div>',
 main='''<div class="card"><table>
<tr><th></th><th>robots.txt Disallow</th><th>noindex</th></tr>
<tr><td>Stops Google crawling the page</td><td><span class="ic y">✓</span><span class="yes">Yes</span></td><td><span class="ic n">✕</span><span class="no">No</span></td></tr>
<tr><td>Keeps the URL out of search results</td><td><span class="ic n">✕</span><span class="no">No</span><small>can still show, without a description</small></td><td><span class="ic y">✓</span><span class="yes">Yes</span><small>once Google crawls the page</small></td></tr>
<tr><td>Google must crawl the page to see it</td><td>—</td><td><span class="ic m">!</span><span class="mid">Yes</span><small>don't block it in robots.txt</small></td></tr>
<tr><td>Works as a line inside robots.txt</td><td><span class="ic y">✓</span><span class="yes">Yes</span></td><td><span class="ic n">✕</span><span class="no">Not supported</span></td></tr>
</table></div>''',
 extra='<div class="extra"><div class="cta">Check which pages send noindex → free Noindex Checker in SpeedyIndex</div></div>',
 foot='Source: Google Search Central, robots.txt and noindex documentation',
 css='.X td{font-size:21px;padding:14px 12px}.X th{font-size:17px}.X table{border-spacing:0 8px}', hp='112px', hx='80px')

# 3 sitemap tags
ITEMS['ig03_sitemap'] = dict(
 head='<span class="pill">XML sitemaps</span><div class="hook">2 of 3 optional sitemap tags are <span class="y">ignored</span></div><div class="sub">What Google actually does with priority, changefreq and lastmod</div>',
 main='''<div class="tags">
<div class="tag"><code>&lt;priority&gt;</code><span class="st n">IGNORED</span><p>No effect on how Google crawls or ranks the URL.</p></div>
<div class="tag"><code>&lt;changefreq&gt;</code><span class="st n">IGNORED</span><p>Google does not use the declared frequency.</p></div>
<div class="tag ok"><code>&lt;lastmod&gt;</code><span class="st y">USED*</span><p>*Only if it is consistently and verifiably accurate: the date of the last significant update.</p></div>
</div>''',
 extra='<div class="extra"><div class="warn"><b>Bumping lastmod on every deploy</b> teaches Google to ignore it.</div><div class="cta">Pull a clean URL list from any sitemap → free Sitemap URL Extractor</div></div>',
 foot='Source: Google Search Central, "Build and submit a sitemap"',
 css='''.tags{display:grid;gap:18px}.tag{position:relative;background:var(--card);border:2px solid var(--line);border-radius:24px;padding:26px 30px}
.tag.ok{border-color:var(--em);box-shadow:0 0 40px rgba(0,198,150,.25)}
.tag code{font-family:PJS;font-weight:800;font-size:46px;color:#fff}
.tag .st{position:absolute;right:28px;top:28px;border-radius:999px;padding:8px 18px;font-weight:800;font-size:22px;color:#0D1A2C}
.st.n{background:var(--cor)}.st.y{background:var(--em)}
.tag p{color:var(--mut);font-size:25px;font-weight:600;margin-top:10px}
.X .tag{padding:20px 24px}.X .tag code{font-size:32px}.X .tag p{font-size:20px}''', hp='96px', hx='74px')

# 4 discovered vs crawled pipeline
ITEMS['ig04_pipeline'] = dict(
 head='<span class="pill">Search Console</span><div class="hook">"Not indexed" has <span class="y">two</span> very different meanings</div><div class="sub">Where each status stops on the way into Google</div>',
 main='''<div class="card pipe">
<div class="stages"><div class="sg">1 · Discovered</div><div class="ar">→</div><div class="sg">2 · Crawled</div><div class="ar">→</div><div class="sg">3 · Indexed</div></div>
<div class="lane"><div class="bar" style="width:33%;background:var(--yel)"></div><div class="stop" style="left:33%">✕</div></div>
<div class="st"><b class="mid">Discovered – currently not indexed</b><br>Google knows the URL but has not crawled it yet; the crawl was rescheduled so the site would not be overloaded. Last crawl date: empty.
<div class="fix">Check: server capacity, internal links from pages Google already visits, sitemap.</div></div>
<div class="lane"><div class="bar" style="width:66%;background:var(--cor)"></div><div class="stop" style="left:66%">✕</div></div>
<div class="st"><b class="no">Crawled – currently not indexed</b><br>Google fetched the page and chose not to index it for now. It may be indexed later; no need to resubmit.
<div class="fix">Check: does the page add something other indexed pages don't?</div></div>
</div>''',
 extra='<div class="extra"><div class="cta">Check index status of any URL list in bulk → SpeedyIndex</div></div>',
 foot='Source: Search Console Help, Page indexing report',
 css='''.pipe{padding:30px 34px}.stages{display:flex;align-items:center;gap:10px}.sg{flex:1;text-align:center;background:#0B1626;border:1px solid var(--line);border-radius:14px;padding:14px 6px;font-weight:800;font-size:24px}
.ar{color:var(--em);font-weight:800;font-size:30px}
.lane{position:relative;height:22px;border-radius:11px;background:#0B1626;border:1px solid var(--line);margin:26px 0 14px}
.bar{position:absolute;left:0;top:0;bottom:0;border-radius:11px}
.stop{position:absolute;top:50%;transform:translate(-50%,-50%);width:44px;height:44px;border-radius:50%;background:#fff;color:#0D1A2C;font-weight:800;text-align:center;line-height:44px;font-size:24px}
.st{font-size:24px;color:var(--mut);font-weight:600;line-height:1.35}.st b{font-size:28px}
.fix{margin-top:10px;color:#fff;font-weight:700;font-size:21px;border-left:4px solid var(--em);padding-left:12px}
.X .st{font-size:19px}.X .st b{font-size:22px}.X .fix{font-size:18px}.X .lane{margin:18px 0 10px}.X .sg{font-size:20px}''', hp='96px', hx='70px')

if __name__ == '__main__':
    base_css = open(os.path.join(D, 'base.css')).read()
    jobs = []
    for name, it in ITEMS.items():
        for fmt in ('P', 'X', 'S'):
            css = COMMON + it['css'] + f":root{{--hp:{it['hp']};--hx:{it['hx']}}}"
            p, w, h = page(name, fmt, it['head'], it['main'], it['extra'], it['foot'], css)
            jobs += [p, str(w), str(h), os.path.join(D, 'out', f'{name}_{fmt}.png')]
    os.makedirs(os.path.join(D, 'out'), exist_ok=True)
    subprocess.run([sys.executable, os.path.join(D, 'render.py')] + jobs, check=True)
