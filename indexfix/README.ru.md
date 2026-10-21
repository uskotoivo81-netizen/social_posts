# IndexFix Tools

[English](README.md) · **Русский**

> IndexFix Tools — набор бесплатных браузерных инструментов для диагностики проблем со сканированием и индексацией в Google. Каждый инструмент решает одну задачу: расшифровывает отчёт URL Inspection, группирует URL из отчёта Page indexing, проверяет правила robots.txt или создаёт файл Sitemap. Всё работает в браузере: регистрация не нужна, а данные никуда не передаются.

**Сайт:** https://indexfixtools.com/ru/

Языки: [English](https://indexfixtools.com/) · [Русский](https://indexfixtools.com/ru/) · [Українська](https://indexfixtools.com/uk/) · [Español](https://indexfixtools.com/es/) · [Deutsch](https://indexfixtools.com/de/) · [Français](https://indexfixtools.com/fr/) · [Tiếng Việt](https://indexfixtools.com/vi/)

## Содержание

- [Как работают инструменты](#как-работают-инструменты)
- [Какой инструмент выбрать](#какой-инструмент-выбрать)
- [Инструменты: как пользоваться](#инструменты-как-пользоваться)
  - [1. Расшифровка отчёта URL Inspection](#url-inspection-decoder)
  - [2. Анализ отчёта Page indexing](#page-indexing-report-analyzer)
  - [3. Очистка списка URL](#url-list-cleaner)
  - [4. Приоритизация обратных ссылок](#backlink-list-prioritizer)
  - [5. Планировщик капельной индексации](#drip-feed-planner)
  - [6. Проверка robots.txt](#robots-txt-tester)
  - [7. Анализатор логов Googlebot](#googlebot-log-analyzer)
  - [8. Генератор Sitemap](#sitemap-generator)
  - [9. Генератор карты редиректов](#redirect-map-generator)
- [PDF чек-лист](#pdf-чек-лист)
- [Файлы в этой папке](#файлы-в-этой-папке)

## Как работают инструменты

- Бесплатно и без регистрации.
- Файлы и списки URL обрабатываются в браузере и не загружаются на сервер.
- Исключение — онлайн-проверки, которые вы запускаете сами: загрузка robots.txt по адресу сайта, импорт Sitemap по URL и проверка переадресаций. Подробнее — на странице [О проекте](https://indexfixtools.com/ru/about/).
- Результаты можно скопировать или скачать (TXT, CSV, XML — в зависимости от инструмента).
- Отчёты Search Console инструменты читают в английской формулировке: при необходимости откройте Search Console с параметром `?hl=en`.

## Какой инструмент выбрать

| Задача | Инструмент |
|---|---|
| Непонятный отчёт URL Inspection | [Расшифровка отчёта URL Inspection](#url-inspection-decoder) |
| Сотни URL в разделе «Why pages aren't indexed» | [Анализ отчёта Page indexing](#page-indexing-report-analyzer) |
| Хаотичный список ссылок перед проверкой или отправкой на индексацию | [Очистка списка URL](#url-list-cleaner) |
| Слишком много обратных ссылок при ограниченном бюджете | [Приоритизация обратных ссылок](#backlink-list-prioritizer) |
| Непонятно, с какой скоростью отправлять новые ссылки | [Планировщик капельной индексации](#drip-feed-planner) |
| Страницы, возможно, заблокированы в robots.txt | [Проверка robots.txt](#robots-txt-tester) |
| Нет уверенности, что Googlebot действительно заходит на сайт | [Анализатор логов Googlebot](#googlebot-log-analyzer) |
| Большой сайт без рабочего файла Sitemap | [Генератор Sitemap](#sitemap-generator) |
| Переезд сайта с сотнями старых URL | [Генератор карты редиректов](#redirect-map-generator) |

## Инструменты: как пользоваться

<a id="url-inspection-decoder"></a>

### 1. Расшифровка отчёта URL Inspection

Вставьте отчёт URL Inspection и узнайте, что означает каждое поле и что исправить в первую очередь.

**Открыть:** [indexfixtools.com/ru/url-inspection-decoder/](https://indexfixtools.com/ru/url-inspection-decoder/) · другие языки: [EN](https://indexfixtools.com/url-inspection-decoder/) · [RU](https://indexfixtools.com/ru/url-inspection-decoder/) · [UK](https://indexfixtools.com/uk/url-inspection-decoder/) · [ES](https://indexfixtools.com/es/url-inspection-decoder/) · [DE](https://indexfixtools.com/de/url-inspection-decoder/) · [FR](https://indexfixtools.com/fr/url-inspection-decoder/) · [VI](https://indexfixtools.com/vi/url-inspection-decoder/)

**Как пользоваться**

1. Откройте Search Console на английском: добавьте ?hl=en к адресу Search Console. Инструмент распознаёт именно английские формулировки отчёта.
2. Введите полный URL в строку проверки в верхней части любого экрана Search Console и нажмите Enter. URL должен относиться к открытому ресурсу.
3. Разверните раздел Page indexing, выделите текст от вердикта до конца раздела и скопируйте его.
4. Вставьте текст в поле и нажмите Прочитать вставленный текст. Проверьте поля и заполните вручную те, что остались пустыми.
5. Нажмите Расшифровать, чтобы узнать, что означает каждое значение, и получить следующие шаги по порядку.

**Полезно знать**

- Статус «URL is unknown to Google» означает, что Google раньше не встречал этот URL.
- Если robots.txt запрещает сканирование, в поле «Indexing allowed?» всегда стоит «Yes»: Google не может увидеть правило noindex на странице, которую ему не разрешено загружать.
- Успешная проверка в реальном времени лишь подтверждает, что Google-InspectionTool может получить доступ к странице. Статус дубликата, меры, принятые вручную, и удаления она не проверяет.

<a id="page-indexing-report-analyzer"></a>

### 2. Анализ отчёта Page indexing

Сгруппируйте выгруженные неиндексированные URL по причине, папке и шаблону адреса и получите список для повторной проверки.

**Открыть:** [indexfixtools.com/ru/page-indexing-report-analyzer/](https://indexfixtools.com/ru/page-indexing-report-analyzer/) · другие языки: [EN](https://indexfixtools.com/page-indexing-report-analyzer/) · [RU](https://indexfixtools.com/ru/page-indexing-report-analyzer/) · [UK](https://indexfixtools.com/uk/page-indexing-report-analyzer/) · [ES](https://indexfixtools.com/es/page-indexing-report-analyzer/) · [DE](https://indexfixtools.com/de/page-indexing-report-analyzer/) · [FR](https://indexfixtools.com/fr/page-indexing-report-analyzer/) · [VI](https://indexfixtools.com/vi/page-indexing-report-analyzer/)

**Как пользоваться**

1. Откройте отчёт Page indexing в Search Console и нажмите на причину в таблице «Why pages aren't indexed».
2. На странице причины экспортируйте примеры (проще всего в CSV).
3. Здесь выберите ту же причину, укажите файл или вставьте URL и нажмите Добавить в анализ.
4. Повторите для остальных причин, которые хотите сравнить.
5. Нажмите Анализировать, затем скачайте список URL для повторной проверки или полный анализ.

**Полезно знать**

- Отчёты Search Console экспортируются в форматах Google Таблиц, Excel или CSV.
- Экспорт ограничен 1000 строками типичных примеров; итоговые цифры в самом отчёте — реальные.
- «Crawled - currently not indexed» означает, что Google просканировал страницу, но не проиндексировал её; «Discovered - currently not indexed» — что страница обнаружена, но ещё не просканирована.

<a id="url-list-cleaner"></a>

### 3. Очистка списка URL

Удалите дубли и параметры отслеживания и приведите беспорядочный список ссылок к единому виду.

**Открыть:** [indexfixtools.com/ru/url-list-cleaner/](https://indexfixtools.com/ru/url-list-cleaner/) · другие языки: [EN](https://indexfixtools.com/url-list-cleaner/) · [RU](https://indexfixtools.com/ru/url-list-cleaner/) · [UK](https://indexfixtools.com/uk/url-list-cleaner/) · [ES](https://indexfixtools.com/es/url-list-cleaner/) · [DE](https://indexfixtools.com/de/url-list-cleaner/) · [FR](https://indexfixtools.com/fr/url-list-cleaner/) · [VI](https://indexfixtools.com/vi/url-list-cleaner/)

**Как пользоваться**

1. Вставьте ссылки или выберите файл (TXT, CSV или любую текстовую выгрузку).
2. Выберите настройки: параметры отслеживания, фрагменты, https, слеш в конце и при необходимости единственный домен, который нужно оставить.
3. Нажмите Очистить список.
4. Проверьте счётчики и таблицу по доменам.
5. Скопируйте результат или скачайте его в формате TXT или CSV.

**Полезно знать**

- URL с параметрами отслеживания (например, utm_source) и тот же URL без них — это разные адреса.
- http и https, с www и без www, со слешем в конце и без него — всё это разные URL.
- Часть URL после # (фрагмент) не передаётся на сервер.

<a id="backlink-list-prioritizer"></a>

### 4. Приоритизация обратных ссылок

Оставьте одну лучшую ссылку с каждого ссылающегося домена и отметьте ссылки, к которым стоит присмотреться.

**Открыть:** [indexfixtools.com/ru/backlink-list-prioritizer/](https://indexfixtools.com/ru/backlink-list-prioritizer/) · другие языки: [EN](https://indexfixtools.com/backlink-list-prioritizer/) · [RU](https://indexfixtools.com/ru/backlink-list-prioritizer/) · [UK](https://indexfixtools.com/uk/backlink-list-prioritizer/) · [ES](https://indexfixtools.com/es/backlink-list-prioritizer/) · [DE](https://indexfixtools.com/de/backlink-list-prioritizer/) · [FR](https://indexfixtools.com/fr/backlink-list-prioritizer/) · [VI](https://indexfixtools.com/vi/backlink-list-prioritizer/)

**Как пользоваться**

1. Экспортируйте обратные ссылки из своего сервиса в CSV (файлы Excel сначала сохраните как CSV).
2. Выберите файл или вставьте его содержимое.
3. Задайте настройки: одна ссылка с домена, пропуск ссылок nofollow, пропуск отмеченных URL.
4. Нажмите Расставить приоритеты и проверьте, какие столбцы найдены.
5. Скопируйте короткий список или скачайте его в формате TXT или CSV.

**Полезно знать**

- По ссылкам с rel=“nofollow”, “sponsored” или “ugc” Google, как правило, не переходит.
- Экспорт Search Console ограничен 1000 строками примеров.
- Рейтинги вроде Domain Rating или Authority Score — метрики сторонних сервисов, а не показатели Google; сравнивайте ссылки в пределах экспорта одного инструмента.

<a id="drip-feed-planner"></a>

### 5. Планировщик капельной индексации

Распределите новые ссылки по дням в ровном темпе и выгрузите график.

**Открыть:** [indexfixtools.com/ru/drip-feed-planner/](https://indexfixtools.com/ru/drip-feed-planner/) · другие языки: [EN](https://indexfixtools.com/drip-feed-planner/) · [RU](https://indexfixtools.com/ru/drip-feed-planner/) · [UK](https://indexfixtools.com/uk/drip-feed-planner/) · [ES](https://indexfixtools.com/es/drip-feed-planner/) · [DE](https://indexfixtools.com/de/drip-feed-planner/) · [FR](https://indexfixtools.com/fr/drip-feed-planner/) · [VI](https://indexfixtools.com/vi/drip-feed-planner/)

**Как пользоваться**

1. Введите количество ссылок или вставьте сами URL.
2. Выберите тип домена — поле «Ссылок в день» заполнится рекомендуемым темпом.
3. Скорректируйте количество ссылок в день и дату начала и решите, пропускать ли выходные.
4. Нажмите Составить график и проверьте итоги по неделям и последний день.
5. Скачайте CSV и работайте по нему или включите режим Drip-Feed, чтобы задача распределялась автоматически.

**Полезно знать**

- Для доменов моложе 6–12 месяцев SpeedyIndex рекомендует 1–2 ссылки в день (7–14 в неделю).
- Для доменов с историей рекомендуемый темп — 3–7 ссылок в день (20–50 в неделю).
- Для крупных авторитетных доменов — 10 и более в день (50–100+ в неделю).

<a id="robots-txt-tester"></a>

### 6. Проверка robots.txt

Узнайте, какие URL файл robots.txt закрывает для Googlebot и какая строка это определяет.

**Открыть:** [indexfixtools.com/ru/robots-txt-tester/](https://indexfixtools.com/ru/robots-txt-tester/) · другие языки: [EN](https://indexfixtools.com/robots-txt-tester/) · [RU](https://indexfixtools.com/ru/robots-txt-tester/) · [UK](https://indexfixtools.com/uk/robots-txt-tester/) · [ES](https://indexfixtools.com/es/robots-txt-tester/) · [DE](https://indexfixtools.com/de/robots-txt-tester/) · [FR](https://indexfixtools.com/fr/robots-txt-tester/) · [VI](https://indexfixtools.com/vi/robots-txt-tester/)

**Как пользоваться**

1. Откройте your-site/robots.txt в браузере и скопируйте весь файл (или вставьте черновик, который планируете опубликовать).
2. Вставьте его в первое поле.
3. Введите токен user-agent для проверки, например Googlebot.
4. Вставьте URL или пути для проверки, по одному в строке.
5. Нажмите Проверить URL и посмотрите результат и решающую строку для каждого URL.

**Полезно знать**

- Google поддерживает поля user-agent, allow, disallow и sitemap; другие поля, например crawl-delay, не поддерживаются.
- Google применяет самое конкретное правило, то есть правило с самым длинным путём; если правила противоречат друг другу, выбирается наименее строгое.
- Пути в правилах чувствительны к регистру, а содержимое после первых 500 КиБ файла Google игнорирует.

<a id="googlebot-log-analyzer"></a>

### 7. Анализатор логов Googlebot

Найдите в логах сервера настоящие визиты Googlebot и посмотрите, что он сканирует и какие URL отдают ошибки.

**Открыть:** [indexfixtools.com/ru/googlebot-log-analyzer/](https://indexfixtools.com/ru/googlebot-log-analyzer/) · другие языки: [EN](https://indexfixtools.com/googlebot-log-analyzer/) · [RU](https://indexfixtools.com/ru/googlebot-log-analyzer/) · [UK](https://indexfixtools.com/uk/googlebot-log-analyzer/) · [ES](https://indexfixtools.com/es/googlebot-log-analyzer/) · [DE](https://indexfixtools.com/de/googlebot-log-analyzer/) · [FR](https://indexfixtools.com/fr/googlebot-log-analyzer/) · [VI](https://indexfixtools.com/vi/googlebot-log-analyzer/)

**Как пользоваться**

1. Скачайте журналы доступа с сервера или из панели хостинга (Apache или Nginx, формат common или combined).
2. Выберите один или несколько файлов логов либо вставьте строки лога.
3. Нажмите Проанализировать лог.
4. Сначала посмотрите таблицу ошибок: это URL, на которых Google получил ответы 4xx или 5xx.
5. В таблице «IP вне диапазонов Google» найдите ботов, которые выдают себя за Googlebot, и скачайте CSV с подробностями.

**Полезно знать**

- Google рекомендует проверять Googlebot обратным DNS-запросом (имя хоста должно относиться к домену googlebot.com, google.com или googleusercontent.com) с последующим прямым DNS-запросом, который должен вернуть тот же IP-адрес, либо сверять IP-адрес с опубликованными диапазонами IP-адресов Google.
- Для Googlebot Smartphone и Googlebot Desktop в robots.txt действует один и тот же токен user-agent, а большую часть запросов Googlebot отправляет робот для мобильных устройств.
- Для большинства сайтов Googlebot в среднем не должен запрашивать страницы чаще, чем раз в несколько секунд.

<a id="sitemap-generator"></a>

### 8. Генератор Sitemap

Превратите список URL в корректные XML-файлы Sitemap, разбитые с учётом ограничений Google.

**Открыть:** [indexfixtools.com/ru/sitemap-generator/](https://indexfixtools.com/ru/sitemap-generator/) · другие языки: [EN](https://indexfixtools.com/sitemap-generator/) · [RU](https://indexfixtools.com/ru/sitemap-generator/) · [UK](https://indexfixtools.com/uk/sitemap-generator/) · [ES](https://indexfixtools.com/es/sitemap-generator/) · [DE](https://indexfixtools.com/de/sitemap-generator/) · [FR](https://indexfixtools.com/fr/sitemap-generator/) · [VI](https://indexfixtools.com/vi/sitemap-generator/)

**Как пользоваться**

1. Вставьте URL, которые должны появляться в результатах поиска, по одному на строку, или выберите файл.
2. Решите, добавлять ли lastmod: не добавлять, сегодняшняя дата или выбранная вами дата.
3. Если список может не поместиться в один файл, укажите базовый URL, по которому будут размещены файлы.
4. Нажмите Создать Sitemap и скачайте каждый файл.
5. Разместите файлы в корне сайта и отправьте Sitemap (или файл индекса) в Search Console либо укажите его в robots.txt.

**Полезно знать**

- Размер одного файла Sitemap ограничен 50 МБ (без сжатия) или 50 000 URL; более длинные списки нужно разбивать.
- Файлы Sitemap должны быть в кодировке UTF-8 и содержать полные абсолютные URL и экранированные значения.
- Google игнорирует значения priority и changefreq; lastmod учитывается, если он стабильно точен.

<a id="redirect-map-generator"></a>

### 9. Генератор карты редиректов

Превратите пары старый→новый URL в правила переадресации для Apache или Nginx с исправленными цепочками.

**Открыть:** [indexfixtools.com/ru/redirect-map-generator/](https://indexfixtools.com/ru/redirect-map-generator/) · другие языки: [EN](https://indexfixtools.com/redirect-map-generator/) · [RU](https://indexfixtools.com/ru/redirect-map-generator/) · [UK](https://indexfixtools.com/uk/redirect-map-generator/) · [ES](https://indexfixtools.com/es/redirect-map-generator/) · [DE](https://indexfixtools.com/de/redirect-map-generator/) · [FR](https://indexfixtools.com/fr/redirect-map-generator/) · [VI](https://indexfixtools.com/vi/redirect-map-generator/)

**Как пользоваться**

1. Подготовьте таблицу соответствий: в каждой строке старый URL и его новый URL, разделённые запятой, табуляцией или стрелкой.
2. Вставьте её или выберите CSV-файл и, если старые URL записаны полными адресами, укажите хост сайта.
3. Выберите сервер (Apache, Nginx или оба) и код статуса.
4. Нажмите Создать правила и исправьте всё, что попало в раздел «Что проверить в первую очередь».
5. Скопируйте или скачайте правила, проверьте их на тестовом сервере и только потом разверните.

**Полезно знать**

- При смене URL Google рекомендует постоянные серверные переадресации, например 301 и 308.
- Перенаправляйте сразу на конечный адрес; если без цепочек не обойтись, в идеале делайте их не длиннее 3 переходов и не допускайте 5 и более.
- Поисковые роботы Google проходят до 10 переходов переадресации; 301 и 308 — сильные сигналы, 302 и 307 — слабые.

## PDF чек-лист

**Проблемы с индексированием: чек-лист диагностики** — Пошаговая проверка: статус в Search Console, доступность страницы, robots.txt, noindex, канонический URL, переадресации, файл Sitemap и обратные ссылки — и что делать в каждом случае.

Скачать: [EN](https://indexfixtools.com/downloads/indexing-diagnostics-checklist-en.pdf) · [RU](https://indexfixtools.com/downloads/indexing-diagnostics-checklist-ru.pdf) · [UK](https://indexfixtools.com/downloads/indexing-diagnostics-checklist-uk.pdf) · [ES](https://indexfixtools.com/downloads/indexing-diagnostics-checklist-es.pdf) · [DE](https://indexfixtools.com/downloads/indexing-diagnostics-checklist-de.pdf) · [FR](https://indexfixtools.com/downloads/indexing-diagnostics-checklist-fr.pdf) · [VI](https://indexfixtools.com/downloads/indexing-diagnostics-checklist-vi.pdf)

Подробнее: [downloads/README.md](downloads/README.md).

## Файлы в этой папке

| Путь | Что это |
|---|---|
| `downloads/` | PDF чек-листы на 7 языках. Сайт копирует их в `/downloads/` при каждой сборке. |
| `checklist-src/` | Тексты чек-листа по языкам (`<lang>.json`) и генератор `make_pdf.py`. |
| `README.md`, `README.ru.md` | Эта документация. |

---

Сайт создан командой [SpeedyIndex](https://speedyindex.com/) · Telegram: https://t.me/speedyindex_seo_ru

Промокод **INDEX10**: +10% бонусными токенами при пополнении баланса SpeedyIndex.
