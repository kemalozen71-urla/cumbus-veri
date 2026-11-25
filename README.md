# cumbus-veri

Cümbüş uygulamasının okuduğu herkese açık veri deposu. Sunucu yok; uygulama dosyaları doğrudan buradan okur.

| Dosya | Ne |
|---|---|
| `mekanlar.csv` | **Ana mekân veritabanı**: mekân, ilçe, açık/kapalı, adres, telefon, nasıl giderim, harita bağlantıları. Elle düzenlenir; yeni mekânlar en alta, yeni `IZM-xxxx` numarasıyla eklenir. |
| `mekan_adlari.json` | Etkinlik metinlerinde mekânı tanımak için her Mekân ID'nin farklı yazılışları |
| `mekanlar.json` | `mekanlar.csv`'den üretilir (elle düzenlenmez) |
| `etkinlikler.json` | Toplayıcının ürettiği etkinlikler; her biri `mekanId` ile mekâna bağlı |
| `eslesmeyen_mekanlar.json` | Mekâna eşlenemeyen etkinlik yerleri: veritabanına eklenecek adaylar |

GitHub Actions toplayıcıyı günde üç kez çalıştırır (`.github/workflows/topla.yml`).

Kaynak: İzmir Büyükşehir Belediyesi Açık Veri Portalı, CC BY 4.0.
