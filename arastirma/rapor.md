# Araştırma raporu: 3. tur

- **Tarih:** 27 Kasım 2026 (Cuma), Europe/Istanbul
- **Aralık:** 27 Kasım – 10 Aralık 2026
- **Çıktı:** `arastirma/etkinlikler.json`, **150 kayıt** (önce 84; 4 geçmiş + 1 iptal çıkarıldı, 71 yeni eklendi)
- Önceki turların ayrıntılı raporu git geçmişinde (`git log -p arastirma/rapor.md`).

## Özet sayılar

| | Adet |
|---|---|
| Web araması (WebSearch) | ~185 (turun ortak 200 arama sınırı doldu) |
| Açılan sayfa (WebFetch) | ~200 denendi |
| Doğrulanıp eklenen yeni kayıt | **71** (seans bazında) |
| Elenen / doğrulanamayan aday | ~50 (aşağıda) |
| Çıkarılan eski kayıt | 4 geçmiş (26 Kasım) + 1 iptal (Uzi, 27 Kasım, Ooze: Biletix iptal gösteriyor) |

## Yeni kayıtların dağılımı

| Kategori | Yeni |
|---|---|
| Kültür-Sanat (tiyatro, stand-up, opera) | 49 |
| Konser | 14 |
| Çocuk | 7 |
| Spor | 1 |

| İlçe | Yeni |
|---|---|
| Konak | 23 |
| Bornova | 21 |
| Karşıyaka | 17 |
| Balçova | 5 |
| Urla | 4 |
| Bayraklı | 1 |

## Başlıklara göre

1. **Çocuk (7 yeni; dosyada toplam çocuk kaydı 46):**
   - Şirin Mavişler "Zorlu Yarış" ve Hayalbazlar Düş Peşinde (Boyoz Akademi, 28–29 Kas, 2'şer seans, 3-10 yaş, 336–372 TL). Önceki turda tek kaynak diye elenmişti; bu tur Biletinial detay sayfalarıyla doğrulandı.
   - Gümüş Patenler (İzmir DT, 29 Kas 14:00, Bornova KSM; tükendi, fiyat yok, ~90 dk).
   - Arkas Sanat Göztepe atölyeleri (5 Ara): Kışın Renkleri (2-3 yaş, ebeveynli) ve Bir Manzaranın İçinde (8-12 yaş), 750 TL.
   - **Görsel:** 7 yeni kaydın 6'sında `gorselAday` var, hiçbiri `gorsel`e taşınmadı. Görsel sunucuları (merlincdn, arkassanat) bu oturumda açılamadı. Arkas görselleri çoğunlukla çocuk fotoğrafı; elle bakılmalı.
   - Böcek Oteli (4) ve Yuko kayıtlarındaki `gorselAday` temizlendi (26.11 elle kontrolde afişte ön planda gerçek çocuk fotoğrafı bulunmuştu).
   - Saat çelişkisi: Noel Baba'nın Geyikleri için Biletinial 13:30/15:30, Bubilet kaynaklı takvimler 14:00/16:00 diyor. Biletinial esas alındı.
2. **Spor (1 yeni):** Altay – Kepez Spor (29 Kas 15:00, Alsancak Mustafa Denizli). Göztepe'nin aralıkta başka iç saha maçı yok (sonraki 13 Ara Konyaspor). Karşıyaka'nın tek iç saha maçı 6 Ara Eskişehirspor; saat ve stat açıklanmadı.
3. **Karşıyaka ve ilçeler:** Karşıyaka'da 17 yeni kayıt (Kurtlar Sofrası 9 seans, SoldOut konserleri, Kardeş Türküler, Boyoz çocuk oyunları). Urla'da 4 (Rüstemoğlu Cemal, Kürk Mantolu Madonna, Napolitan Caz). Merkez dışı ilçelerde (Çeşme, Seferihisar, Menemen, Torbalı, Ödemiş, Tire, Bergama, Aliağa, Foça, Dikili) yeni doğrulanmış kayıt yok.
4. **Söyleşi, imza, kitap: boş.** Tek aday (Artemis Kitap Kulübü, 28 Kas) yalnızca izmirmag'e dayandığı için eklenmedi. Kitabevleri, üniversiteler, APİKAM ve Arkas'ta aralığa düşen duyuru bulunamadı.
5. **Konser ve sahne (63 yeni):** İzmir DT (Bağdat Rüzgarında Dokuz Kadın, Kurtlar Sofrası, Yalancının Resmi, Radyo-yu Hümayun, DT Mutfak), İzDOB Tosca (10 Ara), İstinyeArt (Ballı Süt, Sesler, Musti Kusti, Meksika Açmazı, Karşılıklı Ahkamlar), Nazım Hikmet KM (Boşanma Teklifi, Mefisto, Ay Carmela, Soytarı Kral Lear), Tiyatro Durağı (9 oyun), Maske (4 oyun), AASSM Aralık programı (Rammstein Symphonic, Cem Adrian, 7 ve 8 Ara ücretsiz konserler), Factory PSM, Hayal Kahvesi, Ooze, SoldOut.
6. **Festival:** yeni kayıt yok. Selçuk Zeytin Festivali belediyeden teyit edilemedi (site açılmadı); kayıt hâlâ yalnızca Yeni Bakış'a dayanıyor.

## Elenenler ve nedenleri

| Neden | Örnekler |
|---|---|
| Stat maç sayfasında yok | Menemen FK – Kastamonuspor (6 Ara 15:00; stat yalnızca ayrı bir haberde), Aliağa FK – Kastamonuspor (28 Kas) |
| Saat dilimi / saat belirsiz | Bucaspor 1928 – Bigaspor (28 Kas); voleybol: Göztepe – THY (29 Kas), Altekma – Sultanbeyli (5 Ara), Aras Kargo – Beşiktaş (7 Ara), Aras Kargo – ZAON Kifissia (CEV, 1–3 Ara). AA haftalık programı yayımlanınca eklenebilir. |
| Saat/stat açıklanmadı | Karşıyaka – Eskişehirspor (6 Ara), Gaziemir – Bigaspor |
| Tek aggregator (izmirmag), asıl kaynak açılmadı | Artemis Kitap Kulübü, Konser Adam, Christmas Town İzmir (4–13 Ara, Swissotel), Dam'da Dem (Urla), Angara Gecesi (Seferihisar), Birsen Tezer / Reckol / JOKER (Ooze), Mavi Gri / KILLOKI / Sezer Sarıgöz (Hayal Kahvesi), Blackbriar (SoldOut), Candlelight ve Mustafa Keser (Bostanlı), İzmir Tango Masalı, İsa Çulun, Sahne Tozu / Han Tiyatrosu / Pier Sahne oyunları |
| Çelişkili bilgi | Bora Gencer (5 Ara; Penguen mi Güzelbahçe AKM mi), Noel konserleri (St. John Kilisesi / AASSM tarih çelişkisi) |
| Mekân doğrulanamadı | Deli Cihan (Penguen Kültür Sanat Bistro adresi yok), 2 Yaka Mini Sinema Kulübü |
| Gün bazında teyit yok | Peter Pan (Karşıyaka; yalnızca Ekim haberinde "her pazar") |
| Yıl yok / eski kayıt | Karşıyaka Belediyesi /etkinlikler (Güzel ve Çirkin 4 Ara, Ay Dede, Ali Baba vb.; görsel yükleme tarihleri 2022), "İzmir Kültür Sanat Haftası 1–7 Aralık" haberleri (2025'e ait) |
| Aralık dışı / geçmiş | Çiğli Fakir Baykurt programı (24–26 Kas) |
| Kayıt yok | İzDSO 6 Aralık (Biletinial'de ve AASSM programında yok) |

## Mekân ve konum

- `mekanlar.csv`'ye eklenenler:
  - IZM-0177 Menemen İlçe Stadı (Kazımpaşa Mah. Atatürk Cad. No:154; koordinat Visit İzmir)
  - IZM-0178 Urla Hakan Çeken Kültür Merkezi (Yenikent, 75. Yıl Cumhuriyet Cd. 94 A)
  - IZM-0179 Avlu Urla (Yeni Mh. Zafer Cd. No:69)
  - Bu mekânlardaki mevcut kayıtlar (Ölü'n Bizi Ayırana Dek – Urla, Batu Mutlugil, Jarozzy → Bademler) mekân kimliğine bağlandı.
- **Koordinat eklenen 10 mekân:** 0004 Havagazı, 0009 Hikmet Şimşek, 0021 Tepekule (adres de eklendi), 0029 Han Tiyatrosu, 0034 Bostanlı Suat Taşer, 0117 Bornova KSM, 0128 Ooze, 0131 Cliff, 0154 Gürsel Aksel, 0165 Nazım Hikmet KM. Kaynaklar: iTicket mekân sayfaları, Visit İzmir, Wikipedia.
- **Koordinatı hâlâ eksik çocuk mekânları:** 0168 Alsancak Gazi Ortaokulu, 0171 Maske, 0172 Tiyatro Durağı, 0173 Boyoz Akademi, 0116 Ragıp Haykır; ayrıca 0110 Arkas Göztepe, 0125 İstinyeArt, 0174 Bademler, 0176 Canopy.
- IZM-0110 Arkas Sanat Göztepe'nin `Tür`üne "çocuk programı" eklendi; artık çocuk tablosunda.
- `sektorler.py` çalıştırıldı. `cocuk.csv` ek sütunları 6 mekân (0110, 0112, 0117, 0171, 0172, 0173), `spor.csv` ek sütunları 4 mekân (0154, 0155, 0159, 0177) için dolduruldu.
- Kontrol edilmeli: "DT Urla AKM Sahnesi" kayıtları IZM-0085 (Urla Atatürk KM) ile eşlendi; aynı bina olduğu teyit edilmeli.

## Kaynaklar

- Eklenenler: KYN-100 izmirmag konserler, KYN-101 Arkas merkez sayfaları, KYN-102 iTicket mekân sayfaları (koordinat), KYN-103 AA voleybol haftalık programı, KYN-104 TFF 2. Lig fikstürü. KYN-098'in notu güncellendi.
- Sorunlu: Bubilet (açılmıyor), görsel sunucuları (merlincdn, cdn.bubilet, biletix static; açılamadı), Biletix arama ve İzmir Arena sayfaları (dinamik, boş), tff.org maç detay sayfaları, Karşıyaka Belediyesi etkinlik listesi (yılsız, Ağustos'tan beri güncellenmemiş görünüyor), selcuk.bel.tr ve Gaziemir/Konak/Karabağlar belediye siteleri (açılmadı).
- **Sheets eşitlenmedi.** Bu oturumda "Cümbüş" çalışma kitabına yazacak araç kullanılmadı.

## Hâlâ boş kalan başlıklar

- Söyleşi, imza günü, kitap
- Festival ve fuar (İZFAŞ Aralık takvimi, yeni yıl pazarları)
- Merkez dışı ilçeler
- Spor: basketbol, hentbol, su topu, koşu, bisiklet, yelken, kite, hipodrom (arama sınırı nedeniyle taranamadı); voleybol saatleri
- Çocuk: 7–10 Aralık hafta içi, ücretsiz belediye/kütüphane etkinlikleri, AVM atölyeleri, çocuk konseri, çocuk sineması

## Sonraki tur için öneriler

1. **Spor önce:** AA "Voleybol: Haftanın programı" (Perşembe/Cuma) ile bekleyen 4 voleybol maçını; TFF 15. hafta programıyla Karşıyaka – Eskişehirspor ve Gaziemir – Bigaspor'u ekle. Basketbol ve diğer branşları baştan tara.
2. **Yeni Bakış 30 Kas – 6 Ara takvimi** (Pazartesi) ve Christmas Town İzmir festivalinin asıl kaynağı.
3. izmirmag'de tek kaynak kalan ~25 adayın bilet sayfalarını (Biletinial/Biletix) ara.
4. Çocuk görsel adaylarını (`gorselAday`) elle kontrol et; Music for Babies afişine bir kez daha bakılması önerildi.
5. Koordinatı eksik çocuk mekânları için resmi site / harita bağlantısı ara.
6. Arama bütçesi konulara daha dengeli dağıtılmalı: bu tur ilçe/söyleşi başlığı bütçenin büyük kısmını kullandı, spor ve sahne erken durdu.

---

## Ek: spor için kaynak zinciri taraması (27 Kasım 2026, akşam)

Saati ya da statı belli olmadığı için elenen maçlar zincirleme yeniden arandı. Sıra şöyleydi: önce ev sahibi kulüp, sonra federasyon (TFF, TVF, CEV), bilet satıcısı, maç merkezleri, yerel basın ve deplasman takımının basını, en son stat ya da salon. Bu turda yaklaşık 37 arama yapıldı ve 50 sayfa açıldı.

**Eklenen 6 maç (toplam kayıt 156):**

| Maç | Tarih ve saat | Yer | Kaynak |
|---|---|---|---|
| Bucaspor 1928 – Bigaspor (3. Lig) | 28 Kas 15:30 | Yeni Buca Stadı | AA haftalık program ve TFF canlı yayın listesi. Önceki 12:30, UTC saatiydi. |
| Aliağa FK – Kastamonuspor (2. Lig) | 28 Kas 15:30 | Aliağa Atatürk Stadı | AA (stat), TFF listesi ve Kastamonu basını (saat) |
| Altınordu – Bahçelievler (voleybol, Kadınlar 1. Lig) | 28 Kas 16:00 | TVF Atatürk Voleybol Salonu | Biletinial, 75 TL'den |
| Arkas Spor – TVF Spor Lisesi (voleybol, Erkekler 1. Lig) | 29 Kas 14:00 | TVF Atatürk Voleybol Salonu | Biletinial, 75 TL'den |
| Göztepe Yuppo – THY (Sultanlar Ligi) | 29 Kas 17:00 | TVF Atatürk Voleybol Salonu | Biletinial ve Voleybol Aktüel hakem listesi, 350–1.000 TL |
| Altekma – Sultanbeyli (Efeler Ligi) | 5 Ara 16:00 | TVF Atatürk Voleybol Salonu | Biletinial ve Spor Ekranı, 200 TL'den |

**Hâlâ eklenmeyenler:**
- **Aras Kargo – ZAON Kifissia (CEV):** İki maç da 2 ve 3 Aralık'ta Atina'da oynanacak (AA, Volleyweek). İzmir'de maç yok.
- **Aras Kargo – Beşiktaş:** Maç 6 Aralık'tan 7 Aralık'a alındı. Yeni saati (16:00) yalnızca Spor Ekranı veriyor. Biletinial ya da TVF yayımlayınca eklenecek.
- **Aras Kargo – Manisa (29 Kas):** Ertelendi.
- **Karşıyaka – Eskişehirspor, Menemen FK – Kastamonuspor (6 Ara) ve Gaziemir – Bigaspor (5 Ara):** Elde yalnızca sezon başındaki geçici fikstür saatleri var. Bu saatlerin değiştiği görüldü (ör. Eskişehirspor – Denizli maçı 15:00 görünüyordu, 15:30'da oynandı). AA'nın 15. hafta programı (4 Aralık civarı) yayımlanınca eklenmeli. Menemen'in iç sahası İlçe Stadı, Gaziemir'inki Bornova Aziz Kocaoğlu.

**Mekân:**
- Yeni Buca Stadı, Bornova Aziz Kocaoğlu Stadyumu ve Aliağa Atatürk Stadı `mekanlar.csv`'de yok. Sokak adresleri doğrulanamadığı için eklenmediler.
- Wikipedia koordinatları: Buca Arena 38.39500 / 27.19278, Aziz Kocaoğlu 38.44694 / 27.26222.
- Önceki notta Aziz Kocaoğlu için önerilen IZM-0156 aslında İzmir Atatürk Stadyumu'nun kimliği.

**En verimli kaynaklar (KYN-105 – KYN-108 eklendi):**
- AA'nın Cuma günü yayımlanan futbol programı: alt ligler için saati ve statı birlikte veriyor.
- TFF canlı yayın duyuruları.
- Biletinial Spor: voleybolda saat, salon ve fiyatı birlikte veriyor.
- Voleybol Aktüel: TVF programlarını ve hakem listelerini aktarıyor.

**Saat dilimi uyarısı:** Betexplorer, 365scores ve Sofascore saatleri UTC gösteriyor (Türkiye saatinden 3 saat geri). Bu sitelerden alınan saat mutlaka Türkçe bir kaynakla karşılaştırılmalı.
