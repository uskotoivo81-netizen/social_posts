# IndexFix Tools

**English** · [Русский](README.ru.md)

> IndexFix Tools is a set of free browser tools for Google crawling and indexing problems. Each tool solves one job, such as decoding a URL Inspection report, grouping URLs from the Page indexing report, testing robots.txt rules or building a sitemap. Everything runs in your browser: no sign-up, and your data is not uploaded.

**Site:** https://indexfix-tools.lindabjorkvin.workers.dev/

Languages: [English](https://indexfix-tools.lindabjorkvin.workers.dev/) · [Русский](https://indexfix-tools.lindabjorkvin.workers.dev/ru/) · [Українська](https://indexfix-tools.lindabjorkvin.workers.dev/uk/) · [Español](https://indexfix-tools.lindabjorkvin.workers.dev/es/) · [Deutsch](https://indexfix-tools.lindabjorkvin.workers.dev/de/) · [Français](https://indexfix-tools.lindabjorkvin.workers.dev/fr/) · [Tiếng Việt](https://indexfix-tools.lindabjorkvin.workers.dev/vi/)

## Contents

- [How the tools work](#how-the-tools-work)
- [Which tool to use](#which-tool-to-use)
- [Tools: how to use them](#tools-how-to-use-them)
  - [1. URL Inspection decoder](#url-inspection-decoder)
  - [2. Page indexing report analyzer](#page-indexing-report-analyzer)
  - [3. URL list cleaner](#url-list-cleaner)
  - [4. Backlink list prioritizer](#backlink-list-prioritizer)
  - [5. Drip-feed planner](#drip-feed-planner)
  - [6. Robots.txt tester](#robots-txt-tester)
  - [7. Googlebot log analyzer](#googlebot-log-analyzer)
  - [8. Sitemap generator](#sitemap-generator)
  - [9. Redirect map generator](#redirect-map-generator)
- [PDF checklist](#pdf-checklist)
- [Files in this folder](#files-in-this-folder)

## How the tools work

- Free, no sign-up.
- Files and URL lists are processed in your browser and are not uploaded.
- The exception is the online checks you start yourself: loading robots.txt from a site address, importing a sitemap by URL and checking redirects. See the [About page](https://indexfix-tools.lindabjorkvin.workers.dev/about/).
- Results can be copied or downloaded (TXT, CSV or XML, depending on the tool).
- Search Console reports are read in their English wording: open Search Console with `?hl=en` if needed.

## Which tool to use

| Task | Tool |
|---|---|
| A URL Inspection report you can't read | [URL Inspection decoder](#url-inspection-decoder) |
| Hundreds of URLs under “Why pages aren't indexed” | [Page indexing report analyzer](#page-indexing-report-analyzer) |
| A messy list of links before checking or indexing | [URL list cleaner](#url-list-cleaner) |
| Too many backlinks and a limited budget | [Backlink list prioritizer](#backlink-list-prioritizer) |
| Not sure how fast to send new links | [Drip-feed planner](#drip-feed-planner) |
| Pages may be blocked by robots.txt | [Robots.txt tester](#robots-txt-tester) |
| Not sure whether Googlebot really visits | [Googlebot log analyzer](#googlebot-log-analyzer) |
| A large site without a working sitemap | [Sitemap generator](#sitemap-generator) |
| A site move with hundreds of old URLs | [Redirect map generator](#redirect-map-generator) |

## Tools: how to use them

<a id="url-inspection-decoder"></a>

### 1. URL Inspection decoder

Paste a URL Inspection report and see what every field means and what to fix first.

**Open:** [indexfix-tools.lindabjorkvin.workers.dev/url-inspection-decoder/](https://indexfix-tools.lindabjorkvin.workers.dev/url-inspection-decoder/) · other languages: [EN](https://indexfix-tools.lindabjorkvin.workers.dev/url-inspection-decoder/) · [RU](https://indexfix-tools.lindabjorkvin.workers.dev/ru/url-inspection-decoder/) · [UK](https://indexfix-tools.lindabjorkvin.workers.dev/uk/url-inspection-decoder/) · [ES](https://indexfix-tools.lindabjorkvin.workers.dev/es/url-inspection-decoder/) · [DE](https://indexfix-tools.lindabjorkvin.workers.dev/de/url-inspection-decoder/) · [FR](https://indexfix-tools.lindabjorkvin.workers.dev/fr/url-inspection-decoder/) · [VI](https://indexfix-tools.lindabjorkvin.workers.dev/vi/url-inspection-decoder/)

**How to use**

1. Open Search Console in English: add ?hl=en to the Search Console address. The decoder reads the English wording of the report.
2. Type the full URL into the inspection bar at the top of any Search Console screen and press Enter. The URL must belong to the property that is open.
3. Expand the Page indexing section, select the text from the verdict to the end of the section and copy it.
4. Paste it into the box and click Read pasted text. Check the fields and fix any that stayed empty.
5. Click Decode to get what each value means and the next steps in order.

**Good to know**

- “URL is unknown to Google” means Google hasn't seen this URL before.
- When robots.txt blocks crawling, “Indexing allowed?” always shows “Yes”: Google can't see a noindex rule on a page it isn't allowed to fetch.
- A passing live test only confirms that Google-InspectionTool can reach the page. It doesn't check duplicate status, manual actions or removals.

<a id="page-indexing-report-analyzer"></a>

### 2. Page indexing report analyzer

Group exported “not indexed” URLs by reason, folder and URL pattern, and get a list worth rechecking.

**Open:** [indexfix-tools.lindabjorkvin.workers.dev/page-indexing-report-analyzer/](https://indexfix-tools.lindabjorkvin.workers.dev/page-indexing-report-analyzer/) · other languages: [EN](https://indexfix-tools.lindabjorkvin.workers.dev/page-indexing-report-analyzer/) · [RU](https://indexfix-tools.lindabjorkvin.workers.dev/ru/page-indexing-report-analyzer/) · [UK](https://indexfix-tools.lindabjorkvin.workers.dev/uk/page-indexing-report-analyzer/) · [ES](https://indexfix-tools.lindabjorkvin.workers.dev/es/page-indexing-report-analyzer/) · [DE](https://indexfix-tools.lindabjorkvin.workers.dev/de/page-indexing-report-analyzer/) · [FR](https://indexfix-tools.lindabjorkvin.workers.dev/fr/page-indexing-report-analyzer/) · [VI](https://indexfix-tools.lindabjorkvin.workers.dev/vi/page-indexing-report-analyzer/)

**How to use**

1. Open the Page indexing report in Search Console and click a reason in the “Why pages aren't indexed” table.
2. On the reason's page, export the examples (CSV is easiest).
3. Here, pick the same reason, choose the file or paste the URLs, and click Add to analysis.
4. Repeat for the other reasons you want to compare.
5. Click Analyze, then download the list of URLs to recheck or the full analysis.

**Good to know**

- Search Console reports export as Google Sheets, Excel or CSV.
- An export is truncated to 1,000 rows of representative examples; the totals shown in the report are actual totals.
- “Crawled - currently not indexed” means the page was crawled by Google but not indexed; “Discovered - currently not indexed” means it was found but not crawled yet.

<a id="url-list-cleaner"></a>

### 3. URL list cleaner

Remove duplicates and tracking parameters and normalise a messy list of links.

**Open:** [indexfix-tools.lindabjorkvin.workers.dev/url-list-cleaner/](https://indexfix-tools.lindabjorkvin.workers.dev/url-list-cleaner/) · other languages: [EN](https://indexfix-tools.lindabjorkvin.workers.dev/url-list-cleaner/) · [RU](https://indexfix-tools.lindabjorkvin.workers.dev/ru/url-list-cleaner/) · [UK](https://indexfix-tools.lindabjorkvin.workers.dev/uk/url-list-cleaner/) · [ES](https://indexfix-tools.lindabjorkvin.workers.dev/es/url-list-cleaner/) · [DE](https://indexfix-tools.lindabjorkvin.workers.dev/de/url-list-cleaner/) · [FR](https://indexfix-tools.lindabjorkvin.workers.dev/fr/url-list-cleaner/) · [VI](https://indexfix-tools.lindabjorkvin.workers.dev/vi/url-list-cleaner/)

**How to use**

1. Paste your links or choose a file (TXT, CSV or any text export).
2. Choose the options: tracking parameters, fragments, https, trailing slash and, if needed, a single domain to keep.
3. Click Clean list.
4. Check the counters and the per-domain table.
5. Copy the result or download it as TXT or CSV.

**Good to know**

- A URL with tracking parameters such as utm_source is a different address from the same URL without them.
- http and https, www and non-www, and a trailing slash each make a different URL.
- The #fragment part of a URL is not sent to the server.

<a id="backlink-list-prioritizer"></a>

### 4. Backlink list prioritizer

Keep one best link per referring domain and flag links worth a second look.

**Open:** [indexfix-tools.lindabjorkvin.workers.dev/backlink-list-prioritizer/](https://indexfix-tools.lindabjorkvin.workers.dev/backlink-list-prioritizer/) · other languages: [EN](https://indexfix-tools.lindabjorkvin.workers.dev/backlink-list-prioritizer/) · [RU](https://indexfix-tools.lindabjorkvin.workers.dev/ru/backlink-list-prioritizer/) · [UK](https://indexfix-tools.lindabjorkvin.workers.dev/uk/backlink-list-prioritizer/) · [ES](https://indexfix-tools.lindabjorkvin.workers.dev/es/backlink-list-prioritizer/) · [DE](https://indexfix-tools.lindabjorkvin.workers.dev/de/backlink-list-prioritizer/) · [FR](https://indexfix-tools.lindabjorkvin.workers.dev/fr/backlink-list-prioritizer/) · [VI](https://indexfix-tools.lindabjorkvin.workers.dev/vi/backlink-list-prioritizer/)

**How to use**

1. Export backlinks from your tool as CSV (Excel files: save as CSV first).
2. Choose the file or paste its content.
3. Pick the options: one link per domain, skip nofollow links, skip flagged URLs.
4. Click Prioritize and check which columns were found.
5. Copy the short list or download it as TXT or CSV.

**Good to know**

- Links marked rel=“nofollow”, “sponsored” or “ugc” will generally not be followed by Google.
- Search Console exports are truncated to 1,000 rows of examples.
- Ratings such as Domain Rating or Authority Score are third-party metrics, not Google values; compare links within one tool's export.

<a id="drip-feed-planner"></a>

### 5. Drip-feed planner

Spread new links over days at a steady pace and export the schedule.

**Open:** [indexfix-tools.lindabjorkvin.workers.dev/drip-feed-planner/](https://indexfix-tools.lindabjorkvin.workers.dev/drip-feed-planner/) · other languages: [EN](https://indexfix-tools.lindabjorkvin.workers.dev/drip-feed-planner/) · [RU](https://indexfix-tools.lindabjorkvin.workers.dev/ru/drip-feed-planner/) · [UK](https://indexfix-tools.lindabjorkvin.workers.dev/uk/drip-feed-planner/) · [ES](https://indexfix-tools.lindabjorkvin.workers.dev/es/drip-feed-planner/) · [DE](https://indexfix-tools.lindabjorkvin.workers.dev/de/drip-feed-planner/) · [FR](https://indexfix-tools.lindabjorkvin.workers.dev/fr/drip-feed-planner/) · [VI](https://indexfix-tools.lindabjorkvin.workers.dev/vi/drip-feed-planner/)

**How to use**

1. Enter the number of links, or paste the URLs themselves.
2. Choose the domain type; the links-per-day field fills with the recommended pace.
3. Adjust links per day and the start date, and choose whether to skip weekends.
4. Click Build schedule and check the weekly totals and the last day.
5. Download the CSV and follow it, or use Drip-Feed mode to spread a task automatically.

**Good to know**

- SpeedyIndex recommends 1–2 links a day (7–14 a week) for domains younger than 6–12 months.
- For established domains the recommended pace is 3–7 links a day (20–50 a week).
- For large trusted domains it is 10 or more a day (50–100+ a week).

<a id="robots-txt-tester"></a>

### 6. Robots.txt tester

Check which URLs a robots.txt file blocks for Googlebot and which line decides.

**Open:** [indexfix-tools.lindabjorkvin.workers.dev/robots-txt-tester/](https://indexfix-tools.lindabjorkvin.workers.dev/robots-txt-tester/) · other languages: [EN](https://indexfix-tools.lindabjorkvin.workers.dev/robots-txt-tester/) · [RU](https://indexfix-tools.lindabjorkvin.workers.dev/ru/robots-txt-tester/) · [UK](https://indexfix-tools.lindabjorkvin.workers.dev/uk/robots-txt-tester/) · [ES](https://indexfix-tools.lindabjorkvin.workers.dev/es/robots-txt-tester/) · [DE](https://indexfix-tools.lindabjorkvin.workers.dev/de/robots-txt-tester/) · [FR](https://indexfix-tools.lindabjorkvin.workers.dev/fr/robots-txt-tester/) · [VI](https://indexfix-tools.lindabjorkvin.workers.dev/vi/robots-txt-tester/)

**How to use**

1. Open your-site/robots.txt in the browser and copy the whole file (or paste a draft you plan to publish).
2. Paste it into the first box.
3. Enter the user-agent token to test, for example Googlebot.
4. Paste the URLs or paths to test, one per line.
5. Click Test URLs and read the result and the deciding line for each URL.

**Good to know**

- Google supports the user-agent, allow, disallow and sitemap fields; other fields such as crawl-delay aren't supported.
- Google uses the most specific rule based on the length of the rule path; with conflicting rules it uses the least restrictive one.
- Rule paths are case-sensitive, and Google ignores content after the first 500 KiB of the file.

<a id="googlebot-log-analyzer"></a>

### 7. Googlebot log analyzer

Find real Googlebot visits in server logs and see what it crawls and which URLs fail.

**Open:** [indexfix-tools.lindabjorkvin.workers.dev/googlebot-log-analyzer/](https://indexfix-tools.lindabjorkvin.workers.dev/googlebot-log-analyzer/) · other languages: [EN](https://indexfix-tools.lindabjorkvin.workers.dev/googlebot-log-analyzer/) · [RU](https://indexfix-tools.lindabjorkvin.workers.dev/ru/googlebot-log-analyzer/) · [UK](https://indexfix-tools.lindabjorkvin.workers.dev/uk/googlebot-log-analyzer/) · [ES](https://indexfix-tools.lindabjorkvin.workers.dev/es/googlebot-log-analyzer/) · [DE](https://indexfix-tools.lindabjorkvin.workers.dev/de/googlebot-log-analyzer/) · [FR](https://indexfix-tools.lindabjorkvin.workers.dev/fr/googlebot-log-analyzer/) · [VI](https://indexfix-tools.lindabjorkvin.workers.dev/vi/googlebot-log-analyzer/)

**How to use**

1. Download access logs from your server or hosting panel (Apache or Nginx, common or combined format).
2. Choose one or more log files, or paste log lines.
3. Click Analyze log.
4. Look at the error table first: these are URLs where Google got 4xx or 5xx responses.
5. Check the “not in Google ranges” table for bots pretending to be Googlebot, and download the CSV for details.

**Good to know**

- Google recommends verifying Googlebot with a reverse DNS lookup (the host name must be in googlebot.com, google.com or googleusercontent.com) followed by a forward DNS lookup that returns the same IP, or by matching the IP against Google's published IP ranges.
- Googlebot Smartphone and Googlebot Desktop obey the same user-agent token in robots.txt, and most Googlebot requests come from the mobile crawler.
- For most sites, Googlebot shouldn't request pages more often than once every few seconds on average.

<a id="sitemap-generator"></a>

### 8. Sitemap generator

Turn a list of URLs into valid XML sitemap files, split within Google's limits.

**Open:** [indexfix-tools.lindabjorkvin.workers.dev/sitemap-generator/](https://indexfix-tools.lindabjorkvin.workers.dev/sitemap-generator/) · other languages: [EN](https://indexfix-tools.lindabjorkvin.workers.dev/sitemap-generator/) · [RU](https://indexfix-tools.lindabjorkvin.workers.dev/ru/sitemap-generator/) · [UK](https://indexfix-tools.lindabjorkvin.workers.dev/uk/sitemap-generator/) · [ES](https://indexfix-tools.lindabjorkvin.workers.dev/es/sitemap-generator/) · [DE](https://indexfix-tools.lindabjorkvin.workers.dev/de/sitemap-generator/) · [FR](https://indexfix-tools.lindabjorkvin.workers.dev/fr/sitemap-generator/) · [VI](https://indexfix-tools.lindabjorkvin.workers.dev/vi/sitemap-generator/)

**How to use**

1. Paste the URLs you want in search results, one per line, or choose a file.
2. Choose whether to add lastmod: none, today or a date you pick.
3. If the list may exceed one file, enter the base URL where you'll upload the files.
4. Click Generate sitemap and download each file.
5. Upload the files to your site root and submit the sitemap (or the index) in Search Console or list it in robots.txt.

**Good to know**

- A single sitemap is limited to 50 MB (uncompressed) or 50,000 URLs; larger lists must be split.
- Sitemaps must be UTF-8 encoded, with fully qualified absolute URLs and entity-escaped values.
- Google ignores the priority and changefreq values; lastmod is used if it's consistently accurate.

<a id="redirect-map-generator"></a>

### 9. Redirect map generator

Turn old→new URL pairs into Apache or Nginx redirect rules, with chains fixed.

**Open:** [indexfix-tools.lindabjorkvin.workers.dev/redirect-map-generator/](https://indexfix-tools.lindabjorkvin.workers.dev/redirect-map-generator/) · other languages: [EN](https://indexfix-tools.lindabjorkvin.workers.dev/redirect-map-generator/) · [RU](https://indexfix-tools.lindabjorkvin.workers.dev/ru/redirect-map-generator/) · [UK](https://indexfix-tools.lindabjorkvin.workers.dev/uk/redirect-map-generator/) · [ES](https://indexfix-tools.lindabjorkvin.workers.dev/es/redirect-map-generator/) · [DE](https://indexfix-tools.lindabjorkvin.workers.dev/de/redirect-map-generator/) · [FR](https://indexfix-tools.lindabjorkvin.workers.dev/fr/redirect-map-generator/) · [VI](https://indexfix-tools.lindabjorkvin.workers.dev/vi/redirect-map-generator/)

**How to use**

1. Prepare the mapping: one old URL and its new URL per line, separated by a comma, tab or arrow.
2. Paste it or choose a CSV file, and enter the site host if the old URLs are full addresses.
3. Choose the server (Apache, Nginx or both) and the status code.
4. Click Generate rules and fix everything in “Check these first”.
5. Copy or download the rules, test them on a staging server, then deploy.

**Good to know**

- Google recommends permanent server-side redirects, such as 301 and 308, when URLs change.
- Redirect to the final destination directly; if chains can't be avoided, keep them ideally to no more than 3 and fewer than 5 hops.
- Google's crawlers follow up to 10 redirect hops; 301 and 308 are strong signals, 302 and 307 weak ones.

## PDF checklist

**Indexing problems: diagnostic checklist** — Step by step: status in Search Console, page availability, robots.txt, noindex, canonical URL, redirects, sitemap and backlinks, with what to do in each case.

Download: [EN](https://indexfix-tools.lindabjorkvin.workers.dev/downloads/indexing-diagnostics-checklist-en.pdf) · [RU](https://indexfix-tools.lindabjorkvin.workers.dev/downloads/indexing-diagnostics-checklist-ru.pdf) · [UK](https://indexfix-tools.lindabjorkvin.workers.dev/downloads/indexing-diagnostics-checklist-uk.pdf) · [ES](https://indexfix-tools.lindabjorkvin.workers.dev/downloads/indexing-diagnostics-checklist-es.pdf) · [DE](https://indexfix-tools.lindabjorkvin.workers.dev/downloads/indexing-diagnostics-checklist-de.pdf) · [FR](https://indexfix-tools.lindabjorkvin.workers.dev/downloads/indexing-diagnostics-checklist-fr.pdf) · [VI](https://indexfix-tools.lindabjorkvin.workers.dev/downloads/indexing-diagnostics-checklist-vi.pdf)

Details: [downloads/README.md](downloads/README.md).

## Files in this folder

| Path | What it is |
|---|---|
| `downloads/` | PDF checklists in 7 languages. The site copies them into `/downloads/` on every build. |
| `checklist-src/` | Checklist texts per language (`<lang>.json`) and the generator `make_pdf.py`. |
| `README.md`, `README.ru.md` | This documentation. |

---

Built by the [SpeedyIndex](https://en.speedyindex.com/) team · Telegram: https://t.me/SpeedyIndexOfficial

Promo code **INDEX10**: +10% bonus tokens when you top up your SpeedyIndex balance.
