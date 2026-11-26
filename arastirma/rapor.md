# Araştırma raporu: 1. tur

- **Tarih:** 26 Kasım 2026 (Perşembe), Europe/Istanbul
- **Aralık:** 26 Kasım – 9 Aralık 2026
- **Çıktı:** `arastirma/etkinlikler.json`, 57 kayıt

## Özet sayılar

| | Adet |
|---|---|
| Web araması (WebSearch) | ~62 |
| Açılan sayfa (WebFetch) | ~85 (bunların ~12'si açılamadı) |
| Değerlendirilen aday (etkinlik/seans) | ~110 |
| Doğrulanıp kaydedilen | **57 kayıt** (43 ayrı yapım/etkinlik; çok seanslı oyunların her seansı ayrı kayıt) |
| Elenen / doğrulanamayan | ~53 (aşağıda) |

Her kayıt, en az bir sayfa açılarak doğrulandı: bilet sitesinin detay sayfası, kulüp fikstürü ya da haftalık takvim. Etkinliğin adı, günü, saati ve mekânı bu sayfada yazıyor. Tek kaynağa dayanan kayıtlarda bu durum `dogrulamaNotu` alanında belirtildi.

## Kategori dağılımı

| Kategori | Kayıt |
|---|---|
| Kültür-Sanat (tiyatro, stand-up, bale) | 25 |
| Konser | 17 |
| Çocuk | 12 |
| Spor | 2 |
| Festival | 1 |

## İlçe dağılımı

| İlçe | Kayıt |
|---|---|
| Konak | 24 |
| Karşıyaka | 16 |
| Bornova | 8 |
| Balçova | 3 |
| Urla | 3 |
| Bayraklı | 1 |
| Selçuk | 1 |
| Belirsiz (Arı Vız Vız, Maske Sanat Tiyatrosu) | 1 |

## Öncelik başlıklarına göre durum

1. **Spor (zayıf):**
   - Göztepe'nin iki iç saha maçı kaydedildi: 30 Kasım Trabzonspor, 3 Aralık Erciyes 38 (kupa).
   - Karşıyaka futbolun aralıkta iç saha maçı görünmüyor. Fotmob'a göre sıradaki maç 2 Aralık'ta Amed'e karşı deplasmanda (kupa). Karşıyaka Basket'in ilk maçı da 5 Aralık'ta Esenler deplasmanında.
   - Bucaspor 1928 – Bigaspor maçı (28 Kasım) betexplorer'da var. Ancak saat diliminin belirsiz olması ve ikinci kaynak bulunamaması yüzünden elendi.
   - Voleybol (Göztepe, Aras Kargo, Altekma) haftalık programları bulunamadı. Haftanın programı genelde Perşembe/Cuma yayımlanıyor.
   - Hentbol, su topu, koşu, su sporları ve hipodrom programları için bu aralıkta doğrulanabilir bir etkinlik bulunamadı.
2. **Çocuk:** 12 kayıt. İzmir Çocuk Tiyatrosu (Alsancak Gazi Ortaokulu salonu), Kemeraltı Nazım Hikmet KM'deki Kübik Prens ve Ringo'nun Dünyası, Devlet Tiyatrosu'nun Böcek Oteli (Karşıyaka) ve Arı Vız Vız. Çocuk atölyesi ve çocuk konseri bulunamadı. Music for Babies elendi (aşağıda).
3. **Karşıyaka:** 16 kayıt. Bostanlı Suat Taşer'de 9 oyun/gösteri, Hikmet Şimşek SM'de 1, Ragıp Haykır'da 6 seans (Bir Düş Gibi ve Böcek Oteli), SoldOut'ta Oi Va Voi.
4. **Söyleşi, imza, kitap (boş):** Aralıkta yeni ve doğrulanabilir bir söyleşi bulunamadı. 26 Kasım'daki Nazım Hikmet söyleşisi zaten İzBB verisinde var. İKSF'nin 26 Kasım söyleşilerinin saati yok.
5. **Diğer ilçeler, konser ve sahne:** Factory PSM (Havagazı), AASSM, Tepekule, Cliff, Ooze, Urla (Avlu, Bademler), İstinyeArt, Bornova KSM (Giselle) ve Selçuk Zeytin Festivali.

## Karşıyaka sinemaları

| Sinema | Beyazperde kimliği | Durum |
|---|---|---|
| Paribu Cineverse MaviBahçe | T0582 | Beyazperde'de **seans yayımlanıyor** (26 Kasım için dolu, tarih seçici 23 Aralık'a kadar). Toplayıcının okuduğu bölge sayfasında (154190, 1. sayfa) **listelenmiyor**, bu yüzden `seanslar.json`'da yok. |
| Paribu Cineverse Karşıyaka Hilltown | T2911 | Beyazperde'de **seans var**. "civarinda-154407" film sayfalarında 25 Kasım seansları görünüyor; sinema sayfası önbellekten 14 Kasım gösterdi. Bu sinema da bölge listesinde yok. |
| İzmir EgePark Cinema Pink | T0690 | Bölge listesinde var, ancak `seanslar.json`'da **0 seans**. Cinema Pink'in kendi sitesi bu turda açılamadı. Sinemanın çalışıp çalışmadığı doğrulanmalı. |

**Öneri:**
- `toplayici/seanslar.py`'ye T0582 ve T2911 sabit olarak eklenmeli ya da bölge sayfasının 2. sayfası da okunmalı. Bölge sayfasının 2 sayfa olduğu görüldü. Cinepoll Kemalpaşa da listede yok.
- MaviBahçe ve Hilltown `mekanlar.csv`'ye eklendi (IZM-0166, IZM-0167).

## Elenenler ve nedenleri

| Neden | Örnekler |
|---|---|
| Mekân çelişkili | Music for Babies (6 Aralık). "Canopy by Hilton İzmir Bomonti" adı İstanbul Bomonti'yi düşündürüyor; mekân teyit edilemedi. |
| Yıl yok | İzDSO 6 Aralık konseri (biletinial İngilizce sayfası yıl göstermiyor) |
| Saat dilimi ya da saat belirsiz | Bucaspor 1928 – Bigaspor (28 Kasım); Deniz Tekin, SoldOut (26 Kasım); İKSF söyleşileri (26 Kasım); Gediz Deltası kuş gözlemi (29 Kasım); Konak dijital şiddet paneli (26 Kasım) |
| Mekân belirsiz | Koudelka belgesel gösterimi ve söyleşisi (29 Kasım); Paw Patrol Kış Festivali (mekân "birden fazla", saat yok); Deli Cihan ve Bora Gencer (Penguen Bistro'nun yeri bulunamadı) |
| İzBB verisinde zaten var (tekrar) | Yenilmez, İzDSO 27 Kasım / 4 Aralık, İzmir Oda Orkestrası 28 Kasım, Trio Vecando, Geçmişten Bugüne Nazım Hikmet, Efes–Mimas fotoğraf sergisi |
| Eski kayıt | Karşıyaka Belediyesi /etkinlikler listesinde 26 Kasım – 10 Aralık aralığına düşen yaklaşık 12 etkinlik (Ay Dede'yi Kim Çaldı, Batakhane Güzeli, Film Buluşmaları vb.). Sayfa yıl göstermiyor; iç ipuçları 2019–2025'i işaret ediyor. Karşıyaka Belediyesi'nin "Yeni Yıl" haberi de 2025'e ait. |
| Detay sayfası açılamadı | Oradan Bakınca Mutluyuz (26 Kasım), Etekler ve Pantolonlar (26 Kasım, 5 Aralık) |
| Zaman yetmedi, detayı açılmadı | Biletinial listelerindeki Bağdat Rüzgarında Dokuz Kadın, Musti Kusti, Ballı Süt, Meksika Açmazı, Sesler, Mefisto, Ay Carmela, Soytarı Kral Lear. Hepsi sonraki tur için hazır aday. |
| Kapsam dışı ya da toplantı | BRIDGES paydaş toplantısı (27 Kasım) |

## Kaynak sağlığı

- **Çalışan ve verimli:**
  - Biletinial'ın İzmir liste sayfaları ve detay sayfaları (en iyi kaynak: tarih, saat, fiyat ve yaş sınırı veriyor)
  - iTicket'ın `/events/all/izmir` sayfası
  - Yeni Bakış'ın haftalık takvimi (Pazartesi yayımlanıyor)
  - Sporx'un Göztepe fikstürü
  - Beyazperde'nin sinema sayfaları
- **Sorunlu:**
  - **tff.org:** Fikstür sayfaları Süper Kupa sayfasına düşüyor.
  - **Bubilet:** Sayfalar `client_error` verdi.
  - **iTicket mekân sayfaları:** SoldOut, Hayal Kahvesi ve İzmir Arena sayfaları Nisan 2025'ten beri güncellenmemiş.
  - **Karşıyaka Belediyesi:** Liste yıl göstermiyor.
  - **BBŞT (Bornova Şehir Tiyatrosu):** Aralıkta programı yok.
  - **Sofascore:** Eski veri gösteriyor.
- **Erişim kısıtı:**
  - Bu turda yalnızca arama sonucunda çıkan bağlantılar açılabildi. Elle yazılan adresler onay bekledi ve onay gelmedi. Bu yüzden şu sayfalar doğrudan açılamadı: bornova.bel.tr/etkinlikler, Songkick metro sayfası, betexplorer Karşıyaka fikstürü ve Habertürk yerel haber yönlendirmesi.
  - Google Sheets'teki "İlçe kaynakları" listesine bu oturumdan erişilemedi.

`kaynaklar.csv`'ye eklenenler (KYN-081 – KYN-089):
- Biletinial çocuk, tiyatro, müzik ve opera-bale listeleri
- Biletinial'ın Kemeraltı Nazım Hikmet KM mekân sayfası
- iTicket İzmir listesi
- Beyazperde Karşıyaka sinemaları
- Sporx Göztepe fikstürü
- Betexplorer 3. Lig fikstürü

Sorunlu çıkan KYN-003, 020, 022, 044 ve 055'in `Not` sütununa açıklama, KYN-072'nin notuna da adres kalıbı eklendi.

`mekanlar.csv`'ye eklenenler:
- IZM-0165 Kemeraltı Nazım Hikmet Kültür Merkezi (Güzelyalı'daki IZM-0064'ten farklı)
- IZM-0166 Paribu Cineverse MaviBahçe
- IZM-0167 Paribu Cineverse Karşıyaka Hilltown

## Sonraki tur için öneriler

1. **Spor:** Perşembe ya da Cuma günü "Sultanlar Ligi/Efeler Ligi X. hafta programı" haberlerini, Yeni Asır'ın İzmir alt lig derlemesini ve Karşıyaka Basket'in 12 Aralık iç saha maçını tara. Karşıyaka futbolun iç saha maçları şu an Bornova Aziz Kocaoğlu'nda oynanıyor; Aziz Kocaoğlu Stadı mekân olarak eklenmeli.
2. **30 Kasım – 6 Aralık takvimi:** Yeni Bakış'ın 30 Kasım – 6 Aralık takvimi Pazartesi yayımlanınca Devlet Tiyatrosu, İzDOB ve İKSF etkinliklerini (saatleriyle) ekle.
3. **Kalan adaylar:** Biletinial listelerinde detayı açılmayan 10 kadar adayı doğrula.
4. **Söyleşi ve imza:** Kitabevlerinin (D&R, Remzi, Yakın) sosyal medya duyuruları ve Ege/DEÜ/Yaşar üniversitelerinin söyleşi takvimleri.
5. **Çocuk:** Arkas Sanat, İstinyePark ve AVM'lerin hafta sonu atölyeleri, Bilim Merkezi ve kütüphanelerin çocuk etkinlikleri. Bu tur bunlar için kaynak bulunamadı.
6. **Mekân doğrulama:**
   - Alsancak Gazi Ortaokulu Tiyatro Salonu, Maske Sanat Tiyatrosu, Avlu Urla, Bademler Sanat Köyü ve Urla Hakan Çeken KM'nin adresleri doğrulanıp mekân olarak eklenebilir.
   - Selçuk Zeytin Festivali tek kaynağa (Yeni Bakış) dayanıyor; belediyeden teyit edilmeli.
