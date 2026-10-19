# Indexing problems: diagnostic checklist (PDF)

Free printable checklist from [IndexFix Tools](https://indexfix-tools.lindabjorkvin.workers.dev): a step-by-step way to find out why a page is not in Google.

## Download

| Language | Title | Pages | On the site | On GitHub |
|---|---|---|---|---|
| English | Indexing problems: diagnostic checklist | 2 | [PDF](https://indexfix-tools.lindabjorkvin.workers.dev/downloads/indexing-diagnostics-checklist-en.pdf) | [view](https://github.com/uskotoivo81-netizen/social_posts/blob/main/indexfix/downloads/indexing-diagnostics-checklist-en.pdf) · [raw](https://raw.githubusercontent.com/uskotoivo81-netizen/social_posts/main/indexfix/downloads/indexing-diagnostics-checklist-en.pdf) |
| Русский | Проблемы с индексированием: чек-лист диагностики | 3 | [PDF](https://indexfix-tools.lindabjorkvin.workers.dev/downloads/indexing-diagnostics-checklist-ru.pdf) | [view](https://github.com/uskotoivo81-netizen/social_posts/blob/main/indexfix/downloads/indexing-diagnostics-checklist-ru.pdf) · [raw](https://raw.githubusercontent.com/uskotoivo81-netizen/social_posts/main/indexfix/downloads/indexing-diagnostics-checklist-ru.pdf) |
| Українська | Проблеми з індексуванням: чек-лист діагностики | 3 | [PDF](https://indexfix-tools.lindabjorkvin.workers.dev/downloads/indexing-diagnostics-checklist-uk.pdf) | [view](https://github.com/uskotoivo81-netizen/social_posts/blob/main/indexfix/downloads/indexing-diagnostics-checklist-uk.pdf) · [raw](https://raw.githubusercontent.com/uskotoivo81-netizen/social_posts/main/indexfix/downloads/indexing-diagnostics-checklist-uk.pdf) |
| Español | Problemas de indexación: checklist de diagnóstico | 3 | [PDF](https://indexfix-tools.lindabjorkvin.workers.dev/downloads/indexing-diagnostics-checklist-es.pdf) | [view](https://github.com/uskotoivo81-netizen/social_posts/blob/main/indexfix/downloads/indexing-diagnostics-checklist-es.pdf) · [raw](https://raw.githubusercontent.com/uskotoivo81-netizen/social_posts/main/indexfix/downloads/indexing-diagnostics-checklist-es.pdf) |
| Deutsch | Indexierungsprobleme: Diagnose-Checkliste | 3 | [PDF](https://indexfix-tools.lindabjorkvin.workers.dev/downloads/indexing-diagnostics-checklist-de.pdf) | [view](https://github.com/uskotoivo81-netizen/social_posts/blob/main/indexfix/downloads/indexing-diagnostics-checklist-de.pdf) · [raw](https://raw.githubusercontent.com/uskotoivo81-netizen/social_posts/main/indexfix/downloads/indexing-diagnostics-checklist-de.pdf) |
| Français | Problèmes d’indexation : checklist de diagnostic | 3 | [PDF](https://indexfix-tools.lindabjorkvin.workers.dev/downloads/indexing-diagnostics-checklist-fr.pdf) | [view](https://github.com/uskotoivo81-netizen/social_posts/blob/main/indexfix/downloads/indexing-diagnostics-checklist-fr.pdf) · [raw](https://raw.githubusercontent.com/uskotoivo81-netizen/social_posts/main/indexfix/downloads/indexing-diagnostics-checklist-fr.pdf) |
| Tiếng Việt | Sự cố lập chỉ mục: danh sách kiểm tra chẩn đoán | 3 | [PDF](https://indexfix-tools.lindabjorkvin.workers.dev/downloads/indexing-diagnostics-checklist-vi.pdf) | [view](https://github.com/uskotoivo81-netizen/social_posts/blob/main/indexfix/downloads/indexing-diagnostics-checklist-vi.pdf) · [raw](https://raw.githubusercontent.com/uskotoivo81-netizen/social_posts/main/indexfix/downloads/indexing-diagnostics-checklist-vi.pdf) |

A4, ready to print. Checks link to the matching free IndexFix tool where there is one; the Google documentation used is listed at the end.

## What's inside

1. Find out what Google reports
2. Can Google fetch the page?
3. Is Google allowed to crawl and index it?
4. Is this the URL Google should index?
5. Can Google discover it?
6. What the Page indexing status means
7. Backlinks on sites you don't own
8. What does not help

## How to use it

1. Take one URL that should be in Google but isn't.
2. Go from top to bottom. The first check that fails is usually the cause, so fix it before moving on.
3. Where a check names a tool (URL Inspection decoder, robots.txt tester, log analyzer and others), open it from the link: the tools are free and run in the browser.
4. Section 7 covers backlinks on sites you don't control.
5. Section 8 lists what does not help, so you don't lose time on it.

## Как пользоваться (RU)

**Проблемы с индексированием: чек-лист диагностики** — [скачать PDF](https://indexfix-tools.lindabjorkvin.workers.dev/downloads/indexing-diagnostics-checklist-ru.pdf).

1. Возьмите один URL, который должен быть в Google, но его там нет.
2. Проверяйте сверху вниз. Первая непройденная проверка обычно и есть причина — исправьте её, прежде чем идти дальше.
3. Если в проверке указан инструмент, откройте его по ссылке из чек-листа — инструменты бесплатные и работают в браузере.
4. Обратные ссылки на чужих сайтах — раздел 7.
5. Раздел 8 — что не помогает, чтобы не тратить на это время.

Разделы: 1. Узнайте, что сообщает Google; 2. Может ли Google получить страницу?; 3. Разрешено ли Google сканировать и индексировать страницу?; 4. Тот ли это URL, который должен индексировать Google?; 5. Может ли Google найти страницу?; 6. Что означает статус Page indexing; 7. Обратные ссылки на чужих сайтах; 8. Что не помогает.

## Source and updates

- Texts: [`../checklist-src/<lang>.json`](../checklist-src/). Generator: [`../checklist-src/make_pdf.py`](../checklist-src/make_pdf.py) (Playwright → A4 PDF).
- The IndexFix Tools site downloads these files on every build (`DOWNLOADS_SRC` in the site's `build.py`). To update the PDFs on the site: replace the file here, keeping the name, then redeploy the site.
- File names must stay `indexing-diagnostics-checklist-<lang>.pdf`. If a language file is missing, the site hides the download block for that language.

Edition: October 2026. Made by the SpeedyIndex team.
