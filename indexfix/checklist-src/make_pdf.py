import asyncio, json, os, sys, html, re
from playwright.async_api import async_playwright
H = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(H, '..', 'site2', 'src')
sys.argv = ['x', '/tmp/x', 'https://indexfix-tools.lindabjorkvin.workers.dev']
HOST = 'https://indexfixtools.com'
FONT = os.path.join(H, '..', 'ig', 'node_modules', '@fontsource', 'inter', 'files')
e = html.escape
SI_HOST = {"en": "https://en.speedyindex.com", "ru": "https://speedyindex.com", "fr": "https://fr.speedyindex.com", "es": "https://es.speedyindex.com", "uk": "https://ua.speedyindex.com"}
SVC = {"checker": {"ru": "proverka-indeksatsii-sayta-google", "en": "google-index-checker", "fr": "verificateur-index-google", "es": "comprobador-indice-google", "uk": "perevirka-indeksu-google"},
       "noindex": {"en": "noindex-tag-checker", "fr": "verificateur-noindex", "es": "comprobador-noindex", "uk": "perevirka-noindex"}}
SI_NAME = {"checker": "SpeedyIndex Google Index Checker", "noindex": "SpeedyIndex Noindex Checker"}
def svc(key, lang):
    l = lang if lang in SI_HOST and lang in SVC[key] else "en"
    return SI_HOST[l] + "/" + SVC[key][l] + "/"
def pre(l): return "" if l == "en" else "/" + l
SOURCES = [("URL Inspection tool — Search Console Help", "https://support.google.com/webmasters/answer/9012289"),
           ("Page indexing report — Search Console Help", "https://support.google.com/webmasters/answer/7440203"),
           ("Introduction to robots.txt — Google Search Central", "https://developers.google.com/search/docs/crawling-indexing/robots/intro"),
           ("Block Search indexing with noindex — Google Search Central", "https://developers.google.com/search/docs/crawling-indexing/block-indexing"),
           ("How to specify a canonical URL — Google Search Central", "https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls"),
           ("Build and submit a sitemap — Google Search Central", "https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap"),
           ("Ask Google to recrawl your URLs — Google Search Central", "https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl"),
           ("Indexing API quickstart — Google for Developers", "https://developers.google.com/search/apis/indexing-api/v3/quickstart")]
LOGO = ('<svg class="logo" viewBox="0 0 32 32"><rect width="32" height="32" rx="8" fill="#2d2a6e"/>'
        '<circle cx="14" cy="14" r="7" fill="none" stroke="#ffc94d" stroke-width="3"/><path d="M19 19l6 6" stroke="#ffc94d" stroke-width="3.4" stroke-linecap="round"/>'
        '<path d="M10.5 14.2l2.4 2.4 4.3-4.6" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>')
def fonts():
    css = ''
    for w in (400, 600, 700, 800):
        for sub in ('cyrillic', 'vietnamese', 'latin-ext', 'latin'):
            css += "@font-face{font-family:Inter;font-weight:%d;src:url(file://%s/inter-%s-%d-normal.woff2)}\n" % (w, FONT, sub, w)
    return css
def tools_names(lang):
    import gzip
    p = os.path.join(SITE, 'i18n', lang + '.json')
    L = json.load(open(p, encoding='utf-8'))
    return {k: v['name'] for k, v in L['tools'].items()}
def link(ref, lang, C, names):
    if not ref: return ''
    if ref.startswith('SI:'):
        k = ref[3:]; return '<a class="tl" href="%s">%s</a>' % (svc(k, lang), e(SI_NAME[k]))
    return '<a class="tl" href="%s%s/%s/">%s: %s</a>' % (HOST, pre(lang), ref, e(C['tool_word']), e(names[ref]))
def build(lang):
    C = json.load(open(os.path.join(H, lang + '.json'), encoding='utf-8'))
    names = tools_names(lang)
    secs = ''
    for s in C['sections']:
        items = ''.join('<li><span class="box"></span><div>%s %s</div></li>' % (e(t), link(r, lang, C, names)) for t, r in s['items'])
        secs += '<section><h2>%s</h2><ul class="ck">%s</ul></section>' % (e(s['h']), items)
    rows = ''.join('<tr><td class="st">%s</td><td>%s</td><td>%s</td></tr>' % tuple(e(x) for x in r) for r in C['statuses'])
    th = ''.join('<th>%s</th>' % e(x) for x in C['status_cols'])
    bl = ''.join('<li><span class="box"></span><div>%s %s</div></li>' % (e(t), link(r, lang, C, names)) for t, r in C['bl'])
    no = ''.join('<li><span class="x">✕</span><div>%s</div></li>' % e(t) for t in C['no'])
    src = ''.join('<li>%s — <a href="%s">%s</a></li>' % (e(n), u, e(u.replace('https://', ''))) for n, u in SOURCES)
    home = HOST + pre(lang) + '/'
    si = SI_HOST.get(lang, SI_HOST['en']) + '/'
    return f"""<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><title>{e(C['title'])}</title><style>
{fonts()}
@page{{size:A4;margin:14mm 13mm 16mm}}
*{{box-sizing:border-box}}
body{{font-family:Inter,sans-serif;color:#1b2031;font-size:9.6pt;line-height:1.42;margin:0}}
a{{color:#3b36a8;text-decoration:none}}
.top{{background:#2d2a6e;color:#fff;border-radius:12px;padding:16px 18px 14px;position:relative;overflow:hidden}}
.top:after{{content:"";position:absolute;right:-40px;top:-40px;width:170px;height:170px;border-radius:50%;background:radial-gradient(circle,rgba(255,201,77,.35),transparent 65%)}}
.brand{{display:flex;align-items:center;gap:8px;font-weight:800;font-size:10.5pt}}
.brand .logo{{width:22px;height:22px}}.brand span.m{{color:#c9c7f0;font-weight:600;font-size:8.6pt;margin-left:6px}}
h1{{font-size:21pt;line-height:1.12;margin:10px 0 6px;letter-spacing:-.01em}}
h1 b{{color:#ffc94d}}
.sub{{color:#e7e6fb;margin:0;font-size:10pt;max-width:150mm}}
.meta{{display:flex;justify-content:space-between;color:#c9c7f0;font-size:8.4pt;margin-top:8px}}
h2{{font-size:12pt;margin:12px 0 5px;color:#2d2a6e;border-bottom:2px solid #ffc94d;padding-bottom:3px;break-after:avoid}}
section{{break-inside:avoid}}
ul{{list-style:none;padding:0;margin:0}}
.ck li,.no li{{display:flex;gap:8px;align-items:flex-start;padding:4px 0;border-bottom:1px solid #ece9df}}
.box{{flex:none;width:12px;height:12px;border:1.6px solid #2d2a6e;border-radius:3px;margin-top:2px}}
.x{{flex:none;width:14px;color:#b3261e;font-weight:800;margin-top:-1px}}
.tl{{display:inline-block;background:#efedf9;border-radius:6px;padding:0 6px;font-size:8.4pt;font-weight:600;white-space:nowrap}}
table{{width:100%;border-collapse:collapse;font-size:8.6pt;break-inside:auto}}
th{{background:#2d2a6e;color:#fff;text-align:left;padding:5px 7px;font-weight:700}}
td{{padding:5px 7px;border-bottom:1px solid #e0ddd2;vertical-align:top}}
tr{{break-inside:avoid}}
td.st{{font-weight:700;width:30%;color:#2d2a6e}}
tr:nth-child(even) td{{background:#f6f5f1}}
.no li{{border-color:#f3d6d3}}
.promo{{margin-top:12px;background:#ffc94d;border-radius:10px;padding:9px 12px;font-weight:700;display:flex;justify-content:space-between;gap:10px;align-items:center;break-inside:avoid}}
.promo code{{background:#2d2a6e;color:#fff;border-radius:6px;padding:2px 8px;letter-spacing:.06em;font-family:Inter}}
.end{{margin-top:10px;display:flex;justify-content:space-between;align-items:center;font-size:8.6pt;color:#5a6175;break-inside:avoid}}
.src{{font-size:7.6pt;color:#5a6175;margin-top:8px;break-inside:avoid}}.src h2{{font-size:9.5pt;margin-top:8px}}.src li{{padding:1px 0}}
.legend{{font-size:8pt;color:#5a6175;margin:6px 0 0}}
</style></head><body>
<div class="top"><div class="brand">{LOGO}IndexFix Tools<span class="m">{e(C['brandline'])}</span></div>
<h1>{e(C['title'])}</h1><p class="sub">{e(C['sub'])}</p>
<div class="meta"><span>{e(C['made_by'])} · <a style="color:#ffc94d" href="{si}">SpeedyIndex</a></span><span>{e(C['date'])} · <a style="color:#fff" href="{home}">{e(home.replace('https://',''))}</a></span></div></div>
<p class="legend">{e(C['legend'])}</p>
{secs}
<section><h2>{e(C['status_h'])}</h2><table><thead><tr>{th}</tr></thead><tbody>{rows}</tbody></table></section>
<section><h2>{e(C['bl_h'])}</h2><ul class="ck">{bl}</ul></section>
<section><h2>{e(C['no_h'])}</h2><ul class="no">{no}</ul></section>
<div class="promo"><span>🎁 {e(C['promo'])}</span><code>INDEX10</code></div>
<div class="src"><h2>{e(C['sources_h'])}</h2><ul>{src}</ul></div>

</body></html>""", C
async def main(langs):
    async with async_playwright() as pw:
        b = await pw.chromium.launch()
        for lang in langs:
            h, C = build(lang)
            hp = os.path.join(H, 'ck_%s.html' % lang); open(hp, 'w', encoding='utf-8').write(h)
            p = await b.new_page(); await p.goto('file://' + hp); await p.wait_for_timeout(600)
            foot = '<div style="width:100%;font-family:sans-serif;font-size:7pt;color:#8a8fa0;padding:0 13mm;display:flex;justify-content:space-between"><span>IndexFix Tools · ' + e(C['title']) + '</span><span>' + e(C['page_word']) + ' <span class="pageNumber"></span>/<span class="totalPages"></span></span></div>'
            out = os.path.join(SITE, 'downloads', 'indexing-diagnostics-checklist-%s.pdf' % lang)
            os.makedirs(os.path.dirname(out), exist_ok=True)
            await p.pdf(path=out, format='A4', print_background=True, display_header_footer=True, header_template='<span></span>', footer_template=foot,
                        margin={'top': '14mm', 'bottom': '16mm', 'left': '13mm', 'right': '13mm'})
            print(lang, os.path.getsize(out))
        await b.close()
asyncio.run(main(sys.argv_langs if False else [a for a in os.environ.get('LANGS', 'en').split(',')]))
