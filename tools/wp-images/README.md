# wp-images — images for pipeline articles on our WordPress sites

Used by the publisher runs for BLOG.SPEEDYINDEX.COM, INDEXPEDIA.RU, SPEEDYINDEX.RU (and for T1 posts on Mintlify / beehiiv when images help).

```
python3 tools/wp-images/render.py <article.md> <out_dir>
python3 tools/wp-images/upload.py <image> <init_upload.json> 272457/wp-media/<site>/<launch date>
```

`render.py` reads the article's `## ИЗОБРАЖЕНИЯ` block and writes:

- `<slug>-cover.jpg` — 1200×675, no text, brand palette (#0D1A2C, #00C696, #FFD23F); motif picked from the topic (robots.txt, sitemap, redirects, links, logs, index check).
- `<slug>-infographic.png` — 1200×900, the article H1 (or «Заголовок на картинке») and the captions from «Подписи на картинке» as numbered cards (3–8 captions, Latin and Cyrillic, font Manrope).
- `<slug>-infographic-2.png`, `-3.png`, … — one more image for every extra `### Инфографика N` or `### Схема N` block. Add them when the article's intent needs more visuals (step-by-step guides, comparisons, checklists, long how-tos).
- `media.json` — `images` list (file, alt, title, caption, description, place_after, labels) plus legacy `cover` / `infographic` keys.

Every image block must have **Alt:**, **Caption:** and **Описание (медиатека WP):** — `render.py` exits with an error otherwise.

Block format:

```
## ИЗОБРАЖЕНИЯ
### Обложка
**Alt:** …
**Caption:** …
**Заголовок (медиатека WP):** …
**Описание (медиатека WP):** …
### Инфографика
**Alt:** … / **Caption:** … / **Заголовок (медиатека WP):** … / **Описание (медиатека WP):** …
**Место в статье:** <exact H2 text — image goes after this section>
**Заголовок на картинке:** <optional, defaults to H1>
**Подписи на картинке:**
- …
### Инфографика 2
…same fields…
```

Public URL: GitHub push is blocked from cloud runs, so `upload.py` puts the file into the postmypost bucket. Get `init_upload.json` from the postmypost MCP tool `init_upload` (project_id=366895, name=<file name>, size=<bytes>) and save its JSON response to a file. Do not add a Content-Type field to the POST (the policy rejects it with 403). The script prints `https://postmypost-upload.storage.yandexcloud.net/272457/wp-media/...` and checks the file is readable.

Then: `wp_upload_media_from_url` (url, filename, alt_text, title, caption) → `wp_update_media` (description) → cover as `featured_media`, each infographic as a `<figure class="wp-block-image size-large"><img … class="wp-image-<id>" width="1200" height="900" loading="lazy"/><figcaption>…</figcaption></figure>` after its «Место в статье» section. Full steps: Drive «00а_публикатор_изображения_и_каннибализация.md».

Fonts: Manrope (SIL Open Font License, `fonts/OFL.txt`).
