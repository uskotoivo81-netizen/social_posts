---
title: Claude için SpeedyIndex indeksleme MCP sunucusu: kurulum ve araçlar
seo_title: Claude için SpeedyIndex indeksleme MCP sunucusu
meta_description: SpeedyIndex indeksleme MCP sunucusu, Claude'da toplu indeksleme ve dizin kontrolü, backlink ve sıralama araçları sunar. Kurulum ve token modeli burada.
keyword: indeksleme mcp sunucusu (н.д. (tr))
tags: SEO, Artificial Intelligence, Marketing
cover: /home/claude/differ/tr_connector_cover.png
video: ebIvFIoc0js
---

# Claude için SpeedyIndex indeksleme MCP sunucusu: kurulum ve araçlar

SpeedyIndex indeksleme MCP sunucusu, Claude'un SpeedyIndex hesabınızdaki toplu indeksleme, dizin kontrolü, backlink ve sıralama araçlarını çağırmasını sağlayan bir MCP bağlayıcısıdır. Bağlayıcıyı Claude web veya masaüstüne ekledikten sonra, sohbet içinden Google ve Yandex için 10.000 URL'ye kadar indeksleme görevi oluşturabilir, Google, Yandex ve Bing dizin durumunu kontrol edebilir ve canlı backlinkleri veya Google sıralama pozisyonlarını okuyabilirsiniz. Sunucu ücretsizdir; görevler SpeedyIndex tokenlarıyla ödenir ve yeni hesaplar 100 token içerir.

MCP, Anthropic'in Kasım 2024'te tanıttığı açık bir standarttır ve Claude gibi bir asistana dış servislerin araçlarını çağırma olanağı verir. SpeedyIndex uzak sunucusu `mcp.speedyindex.com/mcp` adresinde Streamable HTTP olarak çalışır; OAuth ile SpeedyIndex oturum açma sayfası açılır, API anahtarınızı yapıştırırsınız. Anahtar sohbete yazılmaz. Yerel seçenek olarak `npx -y speedyindex-mcp` komutu da kullanılabilir; Node.js 18+ gerekir. Uzak sunucuda 22 araç bulunur: 15'i yalnızca veri okur ve ücretsizdir; 7'si hesabı değiştirir ve 5'i token harcar. Kısa video, Claude bağlantı adımlarını gösteriyor.

![SpeedyIndex + Claude — video](https://img.youtube.com/vi/ebIvFIoc0js/hqdefault.jpg)

## Claude'da Bağlanma

Claude web ve masaüstünde özel bağlayıcı şu adımlarla eklenir:

1. Claude'da Plugins → Add → Add custom connector yolunu izleyin.
2. Ad olarak "SpeedyIndex", URL olarak `mcp.speedyindex.com/mcp` girin → Continue → Connect.
3. SpeedyIndex oturum açma sayfasında API anahtarınızı yapıştırın → Connect.
4. Sohbette "+" → Connectors → SpeedyIndex'i açın.
5. Test: "What is my SpeedyIndex balance?" yazın; yanıt token ve kredi gösteriyorsa bağlantı çalışıyor.

Özel bağlayıcılar her Claude planında çalışır; Free plan tek özel bağlayıcıya izin verir. Team/Enterprise'da bir Owner, Organization settings → Connectors bölümünden bağlayıcıyı ekler; her üye kendi bağlantısını kurar. Claude araç çağrılarından önce onay ister; SpeedyIndex'in hesabı değiştiren 7 aracı — token harcayan 5'i dahil — Always allow yapılmadıkça onay ister. Claude, oturum açarken izin verdiğiniz verilere erişebilir; özel bağlayıcılar Anthropic tarafından doğrulanmaz. Tüm adımları ekran görüntüleriyle görmek için [SpeedyIndex MCP bağlayıcı kurulum rehberine](https://tr.speedyindex.com/mcp/) bakabilirsiniz.

## Araçlar ve Veriler

İndeksleme aracı Google ve Yandex için görev oluşturur; tek görevde 10.000 URL'ye kadar ekleyebilirsiniz. Google görevleri pay-per-indexed çalışır: dizine girmeyen URL'ler için tokenlar otomatik iade edilir. Drip feed ile bir Google görevini 2–30 güne yayabilirsiniz. Yandex görevleri ayrı çalışır.

Dizin kontrolü Google, Yandex ve Bing içindir; 10.000 URL'ye kadar listeler oluşturur ve dizine giren / girmeyen URL'leri ayırır. Google sonuçlarında sayfa başlıkları da görünür. Sayfaların Google dizininde olup olmadığını toplu kontrol etmek için [Google indeks kontrol sayfasını](https://tr.speedyindex.com/google-indeks-kontrol/) kullanabilirsiniz.

Backlink denetleyicisi sizin verdiğiniz donör sayfalarını açar ve hedef alan adlarınıza hâlâ bağlantı verip vermediklerini kontrol eder: HTTP durumu, çapa metni, nofollow işareti, Moz Domain Authority ve spam puanı. En fazla 50 hedef alan adı desteklenir. Bu araç bir alan adının backlinklerini keşfetmez; yalnızca sizin verdiğiniz yerleşimlerin canlı olup olmadığını doğrular.

Rank Tracker Google masaüstü sonuçlarını izler: proje başına 5 bölge ve 10 rakip, pozisyonlar ve son kontrole göre değişimler, 90 kontrole kadar trend geçmişi, ayrıca Google'ın AI Overview görünüp görünmediği ve sitenizi alıntılayıp alıntılamadığı.

Güvenlik tarafında sunucuda veritabanı yoktur; API anahtarı yalnızca şifreli bir token içinde saklanır. Erişim token'ı 1 saat yaşar, oturum açma 90 güne kadar yenilenir; hesapta anahtar değiştirilirse tüm oturumlar iptal olur. Bağlayıcı ödeme yapmaz, fatura oluşturmaz, proje veya görev silmez. Bağlayıcı ücretsizdir; görevler SpeedyIndex tokenlarıyla ödenir, abonelik yoktur. Yeni hesaplar 100 token içerir.

Bağlayıcı ayrıca Claude Code, Cursor ve VS Code ile de çalışır. Claude Code'da `claude mcp add` komutu kullanılır; `/mcp` içinden Authenticate seçilir. Cursor'da `.cursor/mcp.json`, VS Code'da `.mcp.json` dosyasına sunucu URL'si eklenir.

```bash
claude mcp add --transport http --scope user speedyindex https://mcp.speedyindex.com/mcp
```

## FAQ

### SpeedyIndex MCP bağlayıcısı ücretsiz mi?

Bağlayıcı ücretsizdir; görevler SpeedyIndex tokenlarıyla ödenir. 15 salt okunur araç ücretsiz çalışır, 7 hesabı değiştiren araçtan 5'i token harcar. Yeni hesaplar 100 token içerir.

### Claude'da özel bağlayıcıyı nasıl eklerim?

Claude'da Plugins → Add → Add custom connector yolunu izleyin, adı "SpeedyIndex" yapın, `mcp.speedyindex.com/mcp` URL'sini girin ve SpeedyIndex API anahtarınızla oturum açın. Sohbette bağlayıcıyı açtıktan sonra "What is my SpeedyIndex balance?" ile test edin.

### Hangi araçlar token harcar?

create_indexing_task, submit_single_url, create_index_check_task, create_backlink_check_task ve rank_tracker_start_check token harcar. Bakiye, görev listesi, görev raporu ve sıralama pozisyonu gibi salt okunur araçlar ücretsizdir.