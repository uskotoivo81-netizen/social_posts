import os, subprocess, sys
D = os.path.dirname(os.path.abspath(__file__))
FEAT = [
 ('01', 'Google link indexing', 'Pay per Indexed: links that don\'t get indexed are refunded in tokens, automatically.', 'yel'),
 ('02', 'Drip Feed', 'One task spread evenly over several days instead of one spike.', 'em'),
 ('03', 'Pre-indexing checks', '404, noindex, robots.txt and already-indexed URLs are caught before sending.', 'em'),
 ('04', 'Bulk index checker', 'Google, Bing and Yandex. Up to 100,000 URLs per check.', 'yel'),
 ('05', 'REST API + Telegram bot', 'Automate checks and indexing tasks from your own stack.', 'em'),
 ('06', '5 free SEO tools', 'Noindex, 404, 5xx and redirect checkers, sitemap URL extractor.', 'em'),
]
CHIPS = ['No Search Console access needed', 'Tokens never expire', 'Dashboard in 6 languages', 'No blackhat, no link schemes']

SIZES = {
 'sq': (1080, 1350, dict(pad='52px 60px', hook='78px', sub='26px', cols=2, ft='26px', fd='19px', chip='18px', gap='14px', fp='18px 22px')),
 'pin': (1000, 1500, dict(pad='52px 60px', hook='86px', sub='26px', cols=2, ft='26px', fd='20px', chip='18px', gap='14px', fp='20px 22px')),
 'x': (1600, 900, dict(pad='44px 60px', hook='78px', sub='24px', cols=3, ft='28px', fd='20px', chip='17px', gap='16px', fp='26px 24px')),
}

def html(fmt):
    w, h, c = SIZES[fmt]
    cards = ''.join(f'<div class="f {cl}"><span class="num">{n}</span><div class="ft">{t}</div><div class="fd">{d}</div></div>' for n, t, d, cl in FEAT)
    chips = ''.join(f'<span class="chip">✓ {x}</span>' for x in CHIPS)
    x = fmt == 'x'
    layout = """.wrap{display:grid;grid-template-columns:560px 1fr;column-gap:48px;align-items:start}.head{margin-top:70px}.grid{margin-top:96px}.f{min-height:330px}""" if x else ".head{margin-top:80px}.grid{margin-top:24px}"
    return f"""<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="base.css"><style>
:root{{--w:{w}px;--h:{h}px}}
.wrap{{position:absolute;inset:0;padding:{c['pad']}}}
.logo{{left:60px;top:{'44px' if x else '56px'};height:{'46px' if x else '52px'}}}
.hook{{font-size:{c['hook']};margin-top:20px}}
.sub{{font-size:{c['sub']};margin-top:16px}}
.grid{{display:grid;grid-template-columns:repeat({c['cols']},1fr);gap:{c['gap']}}}
.f{{position:relative;background:var(--card);border:2px solid var(--line);border-radius:22px;padding:{c['fp']};overflow:hidden}}
.f:before{{content:"";position:absolute;left:0;top:0;bottom:0;width:6px}}
.f.yel:before{{background:var(--yel)}}.f.em:before{{background:var(--em)}}
.num{{font-weight:800;font-size:18px;letter-spacing:.08em;color:var(--mut)}}
.f.yel .num{{color:var(--yel)}}.f.em .num{{color:var(--em)}}
.ft{{font-weight:800;font-size:{c['ft']};margin-top:6px}}
.fd{{color:var(--mut);font-weight:600;font-size:{c['fd']};margin-top:8px;line-height:1.35}}
.chips{{display:flex;flex-wrap:wrap;gap:10px;margin-top:{'22px' if x else '22px'}}}
.chip{{border:2px solid var(--em);color:#fff;font-weight:700;font-size:{c['chip']};border-radius:999px;padding:8px 16px}}
.cta{{margin-top:{'22px' if x else '22px'};display:flex;align-items:center;justify-content:space-between;background:var(--yel);color:#0D1A2C;border-radius:22px;padding:{'18px 24px' if x else '22px 28px'};font-weight:800;font-size:{'24px' if x else '28px'}}}
.cta span{{background:#0D1A2C;color:var(--yel);border-radius:999px;padding:8px 18px;font-size:{'20px' if x else '22px'}}}
.foot{{padding:0 60px {'26px' if x else '36px'};font-size:18px}}
{layout}
</style></head><body><div class="glow"></div><img class="logo" src="logo.png">
<div class="wrap"><div class="head"><span class="pill">Link indexing service</span>
<div class="hook">Get your links into Google. <span class="y">Pay only for indexed.</span></div>
<div class="sub">SpeedyIndex — indexing, index checks and free SEO tools in one dashboard</div>
{('<div class="chips">'+chips+'</div><div class="cta">Start free <span>app.speedyindex.com →</span></div>') if x else ''}</div>
<div><div class="grid">{cards}</div>
{'' if x else '<div class="chips">'+chips+'</div><div class="cta">Start free <span>app.speedyindex.com →</span></div>'}</div></div>
<div class="foot"><span>Results depend on the links; no service can promise 100% indexing</span><b>en.speedyindex.com</b></div>
</body></html>"""

if __name__ == '__main__':
    jobs = []
    for fmt, (w, h, _) in SIZES.items():
        p = os.path.join(D, f'svc_{fmt}.html'); open(p, 'w').write(html(fmt))
        jobs += [p, str(w), str(h), os.path.join(D, 'out', f'svc_{fmt}.png')]
    subprocess.run([sys.executable, os.path.join(D, 'render.py')] + jobs, check=True)
