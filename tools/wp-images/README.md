# wp-images — cover and infographic for pipeline articles

Used by the weekly publisher run for BLOG.SPEEDYINDEX.COM, INDEXPEDIA.RU and SPEEDYINDEX.RU.

```
python3 tools/wp-images/render.py <article.md> wp-media/<launch date>/<site>/
```

Reads the article's `## ИЗОБРАЖЕНИЯ` block and writes:

- `<slug>-cover.jpg` — 1200×675, no text, brand palette (#0D1A2C, #00C696, #FFD23F); motif picked from the topic (robots.txt, sitemap, redirects, links, logs, index check).
- `<slug>-infographic.png` — 1200×900, the article H1 and the captions from «Подписи на картинке» as numbered cards (3–8 captions, Latin and Cyrillic, font Manrope).
- `media.json` — alt, title, caption, description and «Место в статье» for both images.

After `git push`, the images are served from
`https://raw.githubusercontent.com/uskotoivo81-netizen/social_posts/main/wp-media/...`
and go to WordPress with `wp_upload_media_from_url` (the steps are in «00_общие_правила.md», section 18).

Fonts: Manrope (SIL Open Font License, `fonts/OFL.txt`).
