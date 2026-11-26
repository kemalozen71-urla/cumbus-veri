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

---

# 2. tur – çocuk

- **Tarih:** 26 Kasım 2026 (Perşembe), Europe/Istanbul. **Aralık:** 26 Kasım – 9 Aralık 2026.
- **Kapsam:** Yalnızca çocuk başlığı (tiyatro, kukla, atölye, çocuk konseri, şenlik, çocuk filmi) ve `sektorler/cocuk.csv`.

## Özet sayılar

| | Adet |
|---|---|
| Web araması (WebSearch) | ~45 |
| Açılan sayfa (WebFetch) | ~85 (bunların ~15'i açılamadı ya da onay bekledi) |
| Değerlendirilen çocuk adayı | ~75 (seans bazında) |
| **Yeni kaydedilen çocuk etkinliği** | **27 kayıt** (seans bazında; 18 ayrı yapım) |
| Güncellenen eski çocuk kaydı | 12 (mekân kimliği, yaş, bilet adresi, ikinci kaynak) |
| **Dosyadaki toplam çocuk kaydı** | **39** (toplam kayıt 84) |
| `cocuk.csv` mekân/topluluk satırı | **22** (önce 1) |

## Yeni çocuk etkinlikleri (27)

| Tarih | Etkinlik | Mekân | İlçe | Yaş | Ücret (TL'den) |
|---|---|---|---|---|---|
| 28 Kas 13:00 | Karlar Ülkesi – Kar Partisi | Alsancak Gazi Ortaokulu | Konak | 3+ | 443 |
| 28 Kas 13:30 / 29 Kas 15:30 | Noel Baba'nın Geyikleri (2 seans) | Tiyatro Durağı KSM | Konak | 2+ | 376 |
| 28 Kas 13:50 / 29 Kas 14:45 | Pijimaske İş Başına (2 seans) | Boyoz Akademi | Karşıyaka | 2-10 | 336 |
| 28 Kas 14:30 | Ters Yüz (Baykuş) | Alsancak Gazi Ortaokulu | Konak | 3-6 | 443 |
| 28 Kas 16:00 | Paw Patrol – Festival Macerası | Alsancak Gazi Ortaokulu | Konak | 3+ | 443 |
| 28 Kas 16:00 / 29 Kas 14:00 | Pink Pig – Yetenek Yarışması (2 seans) | Tiyatro Durağı KSM | Konak | 3-10 | 376 |
| 29 Kas 12:00 | Ayşin Koruk ile Çocuk Çini Etkinliği (atölye) | Bademler Sanat Köyü | Urla | – | 1.568 |
| 29 Kas 13:00 / 15:00 | Kuğu Gölü Çocuk Balesi (2 seans) | İstinyeArt | Balçova | sayfada "0-3" | 1.041 |
| 29 Kas 15:00 | Hansel ve Gretel – İçimizdeki Orman | Han Tiyatrosu | Konak | 3+ | 438 |
| 29 Kas 15:30 | Büyücüler Okulu | Maske Sanat Tiyatrosu | Bornova | 3-12 | 392 |
| 5 Ara 13:00 / 15:00 | 3D Hologram Sirki (2 seans) | Ege Ü. AKM Yunus Emre | Konak | 2-12 | 550 |
| 5 Ara 13:00 / 15:00 | Kübik Prens (2 seans) | Ahmet Piriştina KM | Karşıyaka | 4+ | 550 |
| 5 Ara 14:00 | Serhat Abi'nin Bilim Fabrikası | Bostanlı Suat Taşer | Karşıyaka | 2+ | 770 |
| 5 Ara 16:30 | Çilek ve Limon | Maske Sanat Tiyatrosu | Bornova | 3-11 | 280 |
| 6 Ara 11:00 / 14:00 | Böcek Oteli – İzmir DT (2 seans) | Bornova KSM Bozkurt Kuruç Fuaye | Bornova | 4-9 | 145 |
| 6 Ara 12:00 / 14:00 | Music for Babies (çocuk konseri, 2 seans) | Canopy by Hilton, Halkapınar | Konak | bebek-küçük çocuk | 896 |
| 6 Ara 13:00 | Tobi ve Lumi Ormanda (Ayvalık Bld. Tiyatrosu) | Dikili Delice | Dikili | 5+ | 300 |
| 6 Ara 14:00 | Yuko – İzmir DT | Ragıp Haykır Sahnesi | Karşıyaka | 5+ | 145 |
| 6 Ara 16:00 | Paw Patrol Kış Festivali | Alsancak Gazi Ortaokulu | Konak | 2+ | 392 |

Hepsi ücretli. Ücretsiz bir çocuk etkinliği bu aralıkta doğrulanamadı.

**Önceki turdan açılan Biletinial adayları:**
- Paw Patrol Kış Festivali: İzmir seansı (6 Aralık 16:00, Alsancak) netleşti ve eklendi.
- Music for Babies: mekân, İstanbul'daki Bomonti değil, Konak Halkapınar'daki Canopy by Hilton İzmir Bomonti çıktı (hilton.com ve Biletinial mekân sayfası). İki seansı eklendi.
- Böcek Oteli 29 Kasım: Biletinial İzmir DT sayfasında da teyit edildi. Önceden tek kaynaklıydı.
- Arı Vız Vız: mekânı bulundu (Maske Sanat Tiyatrosu, Bornova).
- Listede kalan diğer Biletinial adayları (Musti Kusti, Ballı Süt, Meksika Açmazı vb.) çocuk etkinliği değil. Bu turun kapsamı dışında kaldılar.

## Afiş görselleri (`gorsel`)

- **Hiçbir kayıtta `gorsel` dolu değil.** Afiş adresleri resmi bilet sayfalarının `og:image` alanından alındı ve **28 çocuk kaydında `gorselAday` alanına** yazıldı. Bunlar Biletinial'in merlincdn adresleri ve bir Biletix görseli.
- Görsel adreslerinin açılması bu oturumda denenemedi, çünkü WebFetch erişim onayı istedi ve onay gelmedi. Görsellerde çocuk yüzü olup olmadığı da kontrol edilemedi. Bu yüzden kural gereği `gorsel` boş bırakıldı.
- Sonraki turda (ya da insan kontrolüyle) her görsel açılmalı, yüz kontrolü yapılmalı, uygun olanlar `gorselAday`'dan `gorsel`'e taşınmalı.
- `cocuk.csv` Fotoğraf sütunu yalnızca logo olduğu belli olan 4 satırda dolu: İzmir Çocuk Tiyatrosu logo.png ve 3 Arkas mekânı için Arkas Sanat logosu (svg). Bu logolar da açılarak doğrulanmadı.

## İlçe dağılımı

| İlçe | Yeni kayıt | Toplam çocuk kaydı |
|---|---|---|
| Konak | 13 | 22 |
| Karşıyaka | 6 | 8 |
| Bornova | 4 | 5 |
| Balçova | 2 | 2 |
| Urla | 1 | 1 |
| Dikili | 1 | 1 |

`cocuk.csv` (22 satır) ilçe dağılımı: Konak 10, Karşıyaka 4, Bornova 3, Urla 2, Balçova 1, Buca 1, Karabağlar 1.

## Mekân ve topluluk tablosu

`mekanlar.csv`'ye eklenenler (IZM-0168 – IZM-0176), adresleri bilet sitesi ya da kurum sitesi mekân sayfasından alındı:
- 0168 Alsancak Gazi Ortaokulu Tiyatro Salonu (Talatpaşa Blv. 22, Konak)
- 0169 İzmir Çocuk Tiyatrosu (topluluk)
- 0170 Baykuş Çocuk Tiyatrosu (topluluk)
- 0171 Maske Sanat Tiyatrosu (Bornova)
- 0172 Tiyatro Durağı KSM (Kemeraltı)
- 0173 Boyoz Akademi Sanat Merkezi (Karşıyaka)
- 0174 Bademler Sanat Köyü (Urla). Kategori Kültür-Sanat bırakıldı.
- 0175 Buca Işılay Saygın Çocuk Kütüphanesi
- 0176 Canopy by Hilton İzmir Bomonti. Çocuk mekânı değil; yalnızca etkinliğin mekân kimliği için eklendi.

Mevcut 13 mekânın `Tür` alanına "çocuk programı" eklendi; böylece `sektorler.py` bunları çocuk tablosuna alıyor. Bu mekânların hepsinde bu turda doğrulanmış bir çocuk programı var:
- Ragıp Haykır, Bornova KSM, İstinyeArt, Kemeraltı Nazım Hikmet KM, Ahmet Piriştina KM, Ege Ü. AKM, Bostanlı Suat Taşer, Han Tiyatrosu
- APİKAM, Kültürpark Gençlik Tiyatrosu, Arkas Sanat Merkezi, Arkas Deniz Tarihi Merkezi, Arkas Sanat Urla

Düzeltmeler:
- IZM-0090 Ahmet Piriştina KM: ilçe "—" idi, adresle birlikte Karşıyaka Şemikler olarak düzeltildi. Eski "kültür mekânı değil" notu bu mekân için geçersiz görünüyor.
- IZM-0118 Ege Ü. AKM: adres Mithatpaşa Cd. No:92 olarak tamamlandı.
- IZM-0125 İstinyeArt: adres tamamlandı.

## Elenenler ve nedenleri

| Neden | Örnekler |
|---|---|
| Saat yok | Gümüş Patenler (İzmir DT, 29 Kasım; tükendi, seans saati sayfada yok) |
| Tek kaynak, bilet sayfası yok | Peter Pan (Hikmet Şimşek SM, Pazar 14:00, Karşıyaka Belediyesi). Yalnızca 24 Ekim tarihli haber var; Biletinial'deki Hikmet Şimşek listesinde de yok. |
| Mekân adresi yok, tek takvim | 2 Yaka Mini Sinema Kulübü (28 Kasım 15:00, "2 Yaka Kültür"). Çocuk sineması için tek aday buydu. |
| Yalnızca tek aggregator, bilet sayfası açılmadı | Şirin Mavişler "Zorlu Yarış", Hayalbazlar Düş Peşinde (Boyoz, 28-29 Kasım), Konser Adam Çocuk Konseri (Nazım Hikmet KM, 29 Kasım). Hepsi izmirmag'de var, bilettakvimi'nde ve Biletinial'de yok; Bubilet açılmadı. |
| Hizmet/kurs niteliğinde | Terapi Oyunu Alsancak/Bayraklı ücretli oyun grupları ve atölyeleri (her gün; ~849 TL). Etkinlik değil, düzenli kurs. |
| Aralık dışı | Maşa ile Koca Ayı, Şirinler Kayıp Reçete (13 Ara), Minecraft, Minyonlar, Kırmızı Kanatlı Baykuş (13 Ara), Arkas çocuk turları (12 Ara), Paw Patrol Kış Festivali Torbalı (15 Ara), Sermet Erkin illüzyon (19 Ara) |
| Yetişkinlere yönelik | Arkas "Kaşifler ve Maceracılar" turu (5 Ara). Sayfada "yetişkinlere yöneliktir" yazıyor. |
| Okul grubu programı | APİKAM çocuk eğitimleri (Salı/Perşembe, öğretmen kaydıyla). Mekân tablosuna not olarak işlendi. |
| Eski kayıt | Karşıyaka Belediyesi /etkinlikler (Pinokyo, Güzel ve Çirkin vb.; yıl yok, eski), Kadıköy "Mahallemde Çocuk Tiyatrosu" (İstanbul), ETİ Kırmızı Başlıklı Kız (2017), Kültürpark Çocuk Keşif Atölyeleri (2019 haberi; güncel durumu bilinmiyor) |
| Kalıcı mekân / gösterim değil | Funtastic Aquarium (iTicket "family") |

**Doğrulama notu:**
- Pijimaske ve Bademler çini atölyesi: asıl bilet sayfası (Bubilet) açılmadığı için iki bağımsız takvimin (izmirmag ve bilettakvimi) aynı gün ve saati vermesiyle kaydedildi; notta belirtildi.
- Tobi ve Lumi: yalnızca 24.11.2026 tarihli tek habere dayanıyor; notta belirtildi.
- Noel Baba'nın Geyikleri: takvim siteleri saati 30 dk geç gösteriyor, Biletinial esas alındı.

## Kaynak sağlığı (çocuk)

- **En verimli kaynaklar:**
  - izmirmag /cocuk ve bilettakvimi "Aile & Çocuk" haftalık takvimi
  - Biletinial mekân sayfaları (İzmir DT, Maske, Tiyatro Durağı, İstinyeArt, Alsancak Gazi)
  - izmircocuktiyatrosu.com
  - Biletix mekân sayfaları
  - Yeni kaynaklar `kaynaklar.csv`'ye KYN-090 – KYN-099 olarak eklendi.
- **Sorunlu kaynaklar:**
  - **Bubilet:** client_error vermeye devam ediyor (KYN-020 notu güncellendi).
  - **devtiyatro.gov.tr:** Genel program sayfası boş geliyor (KYN-011 notu güncellendi).
  - **Liste sayfaları dinamik yüklenenler:** bornova.bel.tr/etkinlikler, izmir.art ve arkassanat.com/program okunamadı.
  - **Karşıyaka Belediyesi /etkinlikler:** Hâlâ yıl göstermiyor.
- **Erişim kısıtı:** Görsel adresleri ve elle kurulan adresler WebFetch'te onay bekledi, onay gelmedi. Görsel doğrulaması bu yüzden yapılamadı.
- **Sheets eşitlenmedi.** Bu oturumda Claude Docs araçları ertelenmiş durumdaydı ve kullanılmadı.

## Sonraki tur için öneriler (çocuk)

1. `gorselAday` adreslerini açıp yüz kontrolü yap, uygun olanları `gorsel`e taşı.
2. Bubilet erişimi düzelirse şunları doğrula: Boyoz Akademi (Şirinler, Hayalbazlar), Konser Adam, 2 Yaka Mini Sinema Kulübü (mekân adresi), Pijimaske ve çini atölyesi.
3. Ücretsiz çocuk etkinlikleri için ilçe belediyelerinin çocuk tiyatrolarını ve kütüphane atölyelerini tara: Karşıyaka (Peter Pan), Bornova, Buca, Çiğli, İzBB kütüphaneleri. Liste sayfaları dinamik olduğundan haber ya da sosyal medya duyurularıyla eşleştir.
4. Çocuk sineması zayıf kaldı. Beyazperde seanslarından animasyon ve aile filmlerini Çocuk başlığına etiketleyen toplayıcı kuralı (KYN-078) uygulanmalı.
5. 7-9 Aralık hafta içi için okul dışı çocuk etkinliği bulunamadı. 12-13 Aralık hafta sonu yoğun (Arkas turları, Maşa ile Koca Ayı, Şirinler, Minecraft, Kırmızı Kanatlı Baykuş). Bir sonraki tur bu tarihleri kapsamalı.
