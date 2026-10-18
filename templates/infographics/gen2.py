import os, subprocess, sys
from gen import page, COMMON, D

LIST_CSS = '''
.steps{display:grid;gap:14px}
.st2{display:flex;gap:20px;align-items:flex-start;background:var(--card);border:2px solid var(--line);border-radius:22px;padding:20px 26px}
.st2 .n{flex:none;width:52px;height:52px;border-radius:50%;background:var(--em);color:#0D1A2C;font-weight:800;font-size:26px;display:flex;align-items:center;justify-content:center}
.st2.y .n{background:var(--yel)}.st2.c .n{background:var(--cor)}
.st2 b{display:block;font-size:29px;font-weight:800}
.st2 span{display:block;color:var(--mut);font-size:22px;font-weight:600;margin-top:4px;line-height:1.3}
'''
COLS_CSS = '''
.cols{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.col{background:var(--card);border:2px solid var(--line);border-radius:22px;padding:24px 24px}
.col h3{font-size:24px;font-weight:800;text-transform:uppercase;letter-spacing:.05em;margin-bottom:12px}
.col.g{border-color:var(--em)}.col.g h3{color:var(--em)}
.col.r{border-color:var(--cor)}.col.r h3{color:var(--cor)}
.col li{list-style:none;font-size:23px;font-weight:600;line-height:1.3;padding:11px 0 11px 34px;position:relative;border-top:1px solid var(--line)}
.col li:before{position:absolute;left:0;top:10px;font-weight:800}
.col.g li:before{content:"✓";color:var(--em)}.col.r li:before{content:"✕";color:var(--cor)}
'''
POLL_CSS = '''
.opts{display:grid;gap:16px}
.op{display:flex;align-items:center;gap:22px;background:var(--card);border:2px solid var(--line);border-radius:24px;padding:24px 28px}
.op .e{font-size:50px;line-height:1}
.op .l{flex:none;width:56px;height:56px;border-radius:14px;background:var(--yel);color:#0D1A2C;font-weight:800;font-size:30px;display:flex;align-items:center;justify-content:center}
.op .t{font-size:31px;font-weight:700;line-height:1.25}
.op .t small{font-size:22px}
.how{margin-top:18px;text-align:center;color:var(--yel);font-weight:800;font-size:28px}
'''

def steps(rows):
    return '<div class="steps">' + ''.join(f'<div class="st2 {c}"><div class="n">{i}</div><div><b>{t}</b><span>{d}</span></div></div>' for i, (t, d, c) in enumerate(rows, 1)) + '</div>'
def cols(a, b):
    li = lambda xs: ''.join(f'<li>{x}</li>' for x in xs)
    return f'<div class="cols"><div class="col g"><h3>{a[0]}</h3><ul>{li(a[1])}</ul></div><div class="col r"><h3>{b[0]}</h3><ul>{li(b[1])}</ul></div></div>'
def poll(opts, how):
    return '<div class="opts">' + ''.join(f'<div class="op"><span class="e">{e}</span><span class="l">{l}</span><span class="t">{t}</span></div>' for e, l, t in opts) + f'</div><div class="how">{how}</div>'

I = {}
I['c_api'] = dict(
 head='<span class="pill">Google docs · Oct 16, 2026</span><div class="hook">The Indexing API is still <span class="c">not</span> a backlink indexer</div><div class="sub">What changed in the documentation, and what didn’t</div>',
 main=cols(('Changed', ['Default quota listed: 200 publish requests per day per project', 'An outdated form was removed']),
           ('Didn’t change', ['Only pages with JobPosting or BroadcastEvent in a VideoObject', 'Every submission goes through spam detection', 'Abuse, incl. multiple accounts, may get access revoked'])),
 extra='<div class="extra"><div class="warn"><b>Backlinks, blog posts, product pages</b> are not supported page types.</div></div>',
 foot='Source: Google Search Central, Indexing API docs (updated Oct 16, 2026)', css=COLS_CSS+'.col{padding:30px 28px}.col h3{font-size:28px}.col li{font-size:30px;padding:18px 0 18px 38px}.col li:before{top:17px}.main{margin-top:40px}.warn{font-size:30px;padding:28px 30px}', hs='84px')

I['c_prompts'] = dict(
 head='<span class="pill">Save this · thread</span><div class="hook">7 copy-paste AI prompts for an <span class="y">indexing audit</span></div><div class="sub">Paste a Search Console export, get a fix list. Works with ChatGPT, Claude or Gemini.</div>',
 main=steps([('Triage the Page indexing export', 'Group URLs by reason, pick 3 to fix first', 'y'), ('Discovered vs Crawled', 'Likely causes and a checklist for each', ''), ('Noindex and robots.txt audit', 'Blocked pages that rely on noindex', ''), ('Sitemap sanity check', 'Non-200, redirects, noindex, canonicals', ''), ('Canonical conflicts', 'Declared vs Google-selected', ''), ('Backlink index check plan', 'Priority and a re-check schedule', ''), ('Client-ready summary', 'Plain language, no ranking promises', '')]),
 extra='', foot='Full prompts in the replies ↓', css=LIST_CSS + '.st2{padding:14px 22px}.st2 .n{width:44px;height:44px;font-size:22px}.st2 b{font-size:26px}.st2 span{font-size:20px}.steps{gap:10px}', hs='76px')

I['c_5reasons'] = dict(
 head='<span class="pill">Before you blame the indexer</span><div class="hook">Paid for 100 links, <span class="c">0 indexed?</span></div><div class="sub">5 reasons a linking page never makes it into Google</div>',
 main=steps([('The page doesn’t return 200', 'A 404 or 5xx error: there is nothing to index', 'c'), ('It sends noindex', 'In a meta tag or an X-Robots-Tag header', 'c'), ('robots.txt blocks crawling', 'Google never sees the page or the link on it', 'c'), ('Canonical points elsewhere', 'Google may index the other URL instead', 'y'), ('Orphan or thin page', 'Nothing links to it, little unique value', 'y')]),
 extra='<div class="extra"><div class="cta">Free checks: noindex · 404 · 5xx · redirects → SpeedyIndex</div></div>',
 foot='Source: Google Search Central, indexing documentation', css=LIST_CSS, hs='86px')

I['c_5steps'] = dict(
 head='<span class="pill">How it works</span><div class="hook">A Google indexing task in <span class="y">5 steps</span></div><div class="sub">Pre-checks first, then a steady pace</div>',
 main=steps([('Create a task', 'Indexing links → Google', ''), ('Paste your links', 'One per line', ''), ('Turn on the pre-checks', 'URL availability and Google index status: 404s, noindex, robots.txt blocks and already-indexed URLs are caught before sending', 'y'), ('Drip Feed', 'Spread the links evenly over several days', ''), ('Review and create', 'Pay per Indexed: URLs that don’t get indexed are refunded in tokens automatically', 'y')]),
 extra='<div class="extra"><div class="cta">Try it on your own list → app.speedyindex.com</div></div>',
 foot='SpeedyIndex dashboard', css=LIST_CSS, hs='86px')

I['c_poll_pain'] = dict(
 head='<span class="pill">Poll · vote with a reaction</span><div class="hook">Your biggest <span class="y">indexing pain</span> in 2026?</div>',
 main=poll([('👍', 'A', 'Bought links that never got indexed'), ('🔥', 'B', 'Stuck in “Discovered” or “Crawled – not indexed”'), ('🤔', 'C', 'Pages that were indexed, then dropped out'), ('😢', 'D', 'Not sure what to check first')], 'Tap the reaction of your answer ↓'),
 extra='', foot='SpeedyIndex poll', css=POLL_CSS+'.main{margin-top:36px}.op{padding:28px 30px}.op .t{font-size:36px}.op .e{font-size:60px}.how{font-size:34px;margin-top:30px}.opts{gap:22px}', hs='104px')

I['c_poll_check'] = dict(
 head='<span class="pill">Poll · react or reply with a letter</span><div class="hook">How do you check if new backlinks are <span class="y">indexed?</span></div>',
 main=poll([('👍', 'A', 'site: search, one URL at a time'), ('🔥', 'B', 'Search Console <small>(only for sites you own)</small>'), ('🤔', 'C', 'A bulk index checker'), ('😢', 'D', 'I don’t check')], 'Pick one ↓'),
 extra='', foot='SpeedyIndex poll', css=POLL_CSS+'.main{margin-top:40px}.op{padding:32px 30px}.op .t{font-size:36px}.op .t small{font-size:26px}.op .e{font-size:60px}.how{font-size:34px;margin-top:28px}.opts{gap:20px}', hs='96px')

I['c_recrawl'] = dict(
 head='<span class="pill">FAQ</span><div class="hook">How long does Google take to index a <span class="y">backlink?</span></div><div class="sub">There’s no fixed number. Google’s own docs: crawling “can take anywhere from a few days to a few weeks.”</div>',
 main=cols(('Helps discovery', ['Links from pages Google already crawls', 'An accurate sitemap (sites you control)', 'A fast server without errors', 'A steady pace instead of one giant batch']),
           ('Doesn’t help', ['Requesting a recrawl of the same URL again and again', 'Resubmitting “Crawled – currently not indexed” URLs', 'The Indexing API for regular pages: not supported'])),
 extra='<div class="extra"><div class="cta">Spread one batch over several days → Drip Feed</div></div>',
 foot='Source: Google Search Central, “Ask Google to recrawl your URLs”', css=COLS_CSS+'.col{padding:28px 26px}.col h3{font-size:26px}.col li{font-size:27px;padding:16px 0 16px 34px}.col li:before{top:15px}.sub{font-size:30px}.main{margin-top:32px}.cta{font-size:30px;padding:26px 30px}', hs='84px')

I['c_ugc'] = dict(
 head='<span class="pill">New from Google · Oct 8, 2026</span><div class="hook">Google opened a fast lane. <span class="c">Backlinks aren’t on it.</span></div><div class="sub">UGC Fresh Data Program: a separate pipeline for user-generated content</div>',
 main=cols(('Who it’s for', ['Platforms built on user posts and forum threads', 'Stable post URLs, not feeds or profiles', 'Public pages, no login or paywall', 'Structured data: SocialMediaPosting, DiscussionForumPosting', 'Active moderation and user reporting']),
           ('What it isn’t', ['Not the Indexing API', 'Not for regular sites or backlinks', 'No guarantee of appearing in Search', 'Not every application is accepted'])),
 extra='', foot='Source: Google Search Central; Search Engine Roundtable, Oct 8, 2026', css=COLS_CSS + '.col{padding:28px 26px}.col h3{font-size:26px}.col li{font-size:26px;padding:16px 0 16px 34px}.col li:before{top:15px}.main{margin-top:36px}', hs='76px')

I['c_triage'] = dict(
 head='<span class="pill">Diagnosis</span><div class="hook">Only your homepage is indexed? <span class="y">6-step triage</span></div>',
 main=steps([('URL Inspection on an inner page', 'What exactly does Google report?', ''), ('robots.txt', 'Is a whole section disallowed?', ''), ('noindex', 'In the page template or an HTTP header?', 'y'), ('Canonical', 'Do inner pages point to the homepage?', 'y'), ('Links', 'Reachable through plain HTML links, not only scripts?', ''), ('Sitemap', 'Inner URLs listed and returning 200?', '')]),
 extra='<div class="extra"><div class="cta">Free checks: noindex · 404 · redirects → SpeedyIndex</div></div>',
 foot='Based on Google Search Central documentation', css=LIST_CSS + '.st2{padding:16px 24px}.steps{gap:12px}', hs='84px')

I['c_killers'] = dict(
 head='<span class="pill">Silent link killers</span><div class="hook">3 things that quietly kill a <span class="c">backlink</span></div><div class="sub">And the free check for each</div>',
 main='''<div class="card"><table>
<tr><th>Symptom</th><th>What happens</th><th>Free check</th></tr>
<tr><td>noindex</td><td style="color:var(--mut);font-weight:600">The linking page can’t be indexed</td><td class="yes">Noindex Checker</td></tr>
<tr><td>404</td><td style="color:var(--mut);font-weight:600">The page is gone, and the link with it</td><td class="yes">404 Error Checker</td></tr>
<tr><td>Redirects</td><td style="color:var(--mut);font-weight:600">The URL now sends visitors elsewhere; the link may not be on the final page</td><td class="yes">Redirect Checker</td></tr>
</table></div>''',
 extra='<div class="extra"><div class="warn"><b>None of these show up</b> in a backlink report until you check.</div></div>',
 foot='SpeedyIndex free tools', css='td{font-size:30px;padding:34px 16px}th{font-size:22px}.sub{font-size:32px}.main{margin-top:40px}.warn{font-size:30px;padding:28px 30px}', hs='96px')

I['c_statuses'] = dict(
 head='<span class="pill">Save this · thread</span><div class="hook">Page indexing report, <span class="y">decoded</span></div><div class="sub">7 Search Console statuses, one line each</div>',
 main=steps([('Discovered – currently not indexed', 'Found, not crawled yet', 'y'), ('Crawled – currently not indexed', 'Crawled, left out for now', 'y'), ('Excluded by ‘noindex’ tag', 'Google saw the directive', 'c'), ('Blocked by robots.txt', 'Google can’t crawl the page', 'c'), ('Duplicate without user-selected canonical', 'Google picked another URL', ''), ('Page with redirect', 'Points somewhere else', ''), ('Soft 404', 'Looks like “not found”, returns 200', 'c')]),
 extra='', foot='Source: Search Console Help, Page indexing report', css=LIST_CSS + '.st2{padding:14px 22px}.st2 .n{width:44px;height:44px;font-size:22px}.st2 b{font-size:26px}.st2 span{font-size:20px}.steps{gap:10px}', hs='88px')

I['c_apiquote'] = dict(
 head='<span class="pill">FAQ</span><div class="hook">Is the Indexing API safe for <span class="c">backlinks?</span></div>',
 main='''<div class="card q"><div class="qm">“</div><div class="qt">Any attempts to abuse the Indexing API, including the use of multiple accounts or other means to exceed usage quotas, may result in access being revoked.</div><div class="qs">— Google Search Central, Indexing API quickstart (updated Oct 16, 2026)</div></div>
<div class="cols" style="margin-top:16px"><div class="col g"><h3>Supported</h3><ul><li>JobPosting pages</li><li>BroadcastEvent embedded in a VideoObject</li></ul></div><div class="col r"><h3>Not supported</h3><ul><li>Backlinks</li><li>Blog posts, product pages, everything else</li></ul></div></div>''',
 extra='<div class="extra"><div class="warn"><b>“All submissions</b> through the Indexing API undergo rigorous spam detection.”</div></div>',
 foot='Source: developers.google.com/search/apis/indexing-api', css=COLS_CSS + '''.col li{font-size:27px;padding:15px 0 15px 34px}.col h3{font-size:26px}.warn{font-size:28px;padding:26px 30px}.main{margin-top:34px}.q{padding:36px 40px;border-color:var(--yel)}.qm{font-size:110px;line-height:.6;color:var(--yel);font-weight:800;height:50px}
.qt{font-size:40px;font-weight:700;line-height:1.3}.qs{color:var(--mut);font-size:20px;font-weight:600;margin-top:14px}''', hs='88px')

if __name__ == '__main__':
    only = sys.argv[1:]
    jobs = []
    for name, it in I.items():
        if only and name not in only: continue
        css = COMMON + it['css'] + f":root{{--hs:{it['hs']}}}"
        p, w, h = page(name, 'S', it['head'], it['main'], it['extra'], it['foot'], css)
        jobs += [p, str(w), str(h), os.path.join(D, 'out', f'{name}_S.png')]
    subprocess.run([sys.executable, os.path.join(D, 'render.py')] + jobs, check=True)
