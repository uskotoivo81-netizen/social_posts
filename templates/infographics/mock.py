import os, sys, asyncio, html as H, re
from playwright.async_api import async_playwright
D = os.path.dirname(os.path.abspath(__file__))

FONTS = """
<style>
@font-face{font-family:Inter;src:url(node_modules/@fontsource/inter/files/inter-latin-400-normal.woff2);font-weight:400}
@font-face{font-family:Inter;src:url(node_modules/@fontsource/inter/files/inter-latin-600-normal.woff2);font-weight:600}
@font-face{font-family:Inter;src:url(node_modules/@fontsource/inter/files/inter-latin-700-normal.woff2);font-weight:700}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Inter,'Noto Color Emoji',sans-serif;-webkit-font-smoothing:antialiased}
</style>"""

def linkify(t, color):
    t = H.escape(t)
    return re.sub(r'((?:en\.speedyindex\.com|t\.me)/[^\s]*)', rf'<span style="color:{color}">\1</span>', t).replace('\n', '<br>')

def tg(text, img, out, time='13:00'):
    body = linkify(text, '#6AB3F3')
    return f"""<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>
body{{width:480px;background:#0E1621;color:#fff}}
.hdr{{display:flex;align-items:center;gap:12px;padding:12px 16px;background:#17212B;border-bottom:1px solid #0B121A}}
.av{{width:40px;height:40px;border-radius:50%;background:#0D1A2C url(logo.png) center/80% no-repeat;border:1px solid #1F3A5C}}
.nm{{font-weight:600;font-size:16px}} .sb{{color:#7F91A4;font-size:13px;margin-top:2px}}
.wrap{{padding:18px 12px 22px;background:#0E1621}}
.bub{{background:#182533;border-radius:14px;overflow:hidden;max-width:420px}}
.bub img{{display:block;width:100%}}
.ch{{color:#6AB3F3;font-weight:600;font-size:14px;padding:8px 12px 0}}
.tx{{padding:6px 12px 4px;font-size:15px;line-height:1.38}}
.ft{{display:flex;justify-content:flex-end;gap:6px;color:#6D7F8F;font-size:12px;padding:2px 10px 8px}}
.note{{color:#7F91A4;font-size:12px;text-align:center;margin-top:10px}}
</style></head><body>
<div class="hdr"><div class="av"></div><div><div class="nm">SpeedyIndex</div><div class="sb">channel</div></div></div>
<div class="wrap"><div class="bub"><img src="{img}"><div class="ch">SpeedyIndex</div><div class="tx">{body}</div><div class="ft">{time}</div></div>
<div class="note">Mockup · Telegram EN · {len(text)} chars (caption limit 1024)</div></div>
</body></html>"""

ICONS = '''<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#F3F5F7" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8L12 21.2l8.8-8.8a5.5 5.5 0 0 0 0-7.8z"/></svg>
<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#F3F5F7" stroke-width="1.8" stroke-linejoin="round"><path d="M21 12a8.5 8.5 0 0 1-12.6 7.4L3 21l1.6-5.2A8.5 8.5 0 1 1 21 12z"/></svg>
<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#F3F5F7" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M17 2l4 4-4 4"/><path d="M3 11V9a3 3 0 0 1 3-3h15"/><path d="M7 22l-4-4 4-4"/><path d="M21 13v2a3 3 0 0 1-3 3H3"/></svg>
<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#F3F5F7" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 2L11 13"/><path d="M22 2l-7 20-4-9-9-4 20-7z"/></svg>'''

def th(text, img, out, when='17:00'):
    lines = text.split('\n')
    hook, rest = H.escape(lines[0]), '\n'.join(lines[1:])
    body = linkify(rest, '#5EA9F5')
    return f"""<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>
body{{width:480px;background:#101010;color:#F3F5F7}}
.p{{display:flex;gap:12px;padding:18px 16px 16px}}
.av{{flex:none;width:40px;height:40px;border-radius:50%;background:#0D1A2C url(logo.png) center/80% no-repeat;border:1px solid #333}}
.top{{display:flex;gap:8px;align-items:baseline;font-size:15px}} .top b{{font-weight:600}} .top span{{color:#777}}
.tx{{font-size:15px;line-height:1.4;margin-top:4px}} .hk{{font-weight:400}}
.im{{margin-top:12px;border-radius:12px;overflow:hidden;border:1px solid #2A2A2A;width:300px}} .im img{{display:block;width:100%}}
.ac{{display:flex;gap:22px;margin-top:12px}}
.note{{color:#777;font-size:12px;text-align:center;padding:0 0 14px}}
</style></head><body>
<div class="p"><div class="av"></div><div style="flex:1;min-width:0">
<div class="top"><b>speedyindex_seo</b><span>{when}</span></div>
<div class="tx"><span class="hk">{hook}</span><br>{body}</div>
<div class="im"><img src="{img}"></div>
<div class="ac">{ICONS}</div></div></div>
<div class="note">Mockup · Threads · {len(text)} chars (limit 500) · line 1 = hook</div>
</body></html>"""

TG1 = """🧹 Spam update is over. Now check your links.

Google's September 2026 spam update finished rolling out on October 8 — about two weeks after it started on September 24. It ran globally, in all languages, and Google said it brought no new policies.

If your traffic moved in that window, don't rewrite half the site yet. Five checks first:

1️⃣ Line up Sep 24 – Oct 8 against your Search Console performance data
2️⃣ Open the Manual actions report
3️⃣ Find pages that exist to rank rather than to help
4️⃣ Audit new links: are the linking pages live — and indexed?
5️⃣ Pause bulk link pushes until the data settles

A link on a page Google never indexed doesn't show up anywhere in your data. You can check those pages in bulk 👉 en.speedyindex.com/google-index-checker/

Did your rankings move during the rollout? 👇"""

TH1 = """robots.txt is not a delete button.

It stops crawling. A disallowed URL can still show up in Google, just without a description.

Want a page out of search? Let Google crawl it and add noindex. And no, noindex inside robots.txt isn't supported.

Check which pages send the tag 👉 en.speedyindex.com/noindex-tag-checker/

Ever blocked a page and found it in Google anyway?"""

async def main():
    jobs = [(tg(TG1, 'out/tg01_spam.png', 'x'), 'mock_tg01.png'), (th(TH1, 'out/ig02_robots_S.png', 'x', 'Sat 24.10'), 'mock_threads_robots.png')]
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for htm, out in jobs:
            f = os.path.join(D, out.replace('.png', '.html')); open(f, 'w').write(htm)
            pg = await b.new_page(viewport={'width': 480, 'height': 800}, device_scale_factor=2)
            await pg.goto('file://' + f); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(2500)
            await pg.screenshot(path=os.path.join(D, 'out', out), full_page=True); print(out)
        await b.close()
    print(len(TG1), len(TH1))
asyncio.run(main())
