# Araştırma raporu: 4. tur

- **Tarih:** 28 Kasım 2026 (Cumartesi), Europe/Istanbul
- **Aralık:** 28 Kasım – 11 Aralık 2026
- **Çıktı:** `arastirma/etkinlikler.json`, **157 kayıt** (önce 156; 9 geçmiş kayıt çıkarıldı, 10 yeni eklendi)
- Bu tur beş paralel araştırmacıyla yürütüldü (çocuk, spor, ilçeler+festival, söyleşi+sahne, fiyat avı). Önceki turların raporu git geçmişinde.

## Özet sayılar

| | Adet |
|---|---|
| Web araması (WebSearch) | ~155 |
| Açılan sayfa (WebFetch) | ~200 denendi |
| Doğrulanıp eklenen yeni kayıt | **10** |
| Elenen / doğrulanamayan aday | 47 (aşağıda) |
| Çıkarılan eski kayıt | 9 geçmiş (27 Kasım) |
| Fiyatı tamamlanan | 79 (araştırma kayıtları 70, İzBB 9) |
| Koordinat eklenen mekân | 8 |

## Yeni kayıtlar

| Kayıt | Tarih | Yer | Kategori |
|---|---|---|---|
| Küçük Prens (Baykuş Çocuk Tiyatrosu), 3+, 50 dk, 443–499 TL | 5 Ara 14:30 | Alsancak Gazi Ortaokulu, Konak | Çocuk |
| Karlar Ülkesi – Kar Partisi (Baykuş), 3+, 40 dk, 443–499 TL | 5 Ara 16:00 | Alsancak Gazi Ortaokulu, Konak | Çocuk |
| Duvarın Arkasındaki Ev (Savaş Tercan Çocuk Tiyatrosu), 2 seans | 30 Kas 11:00, 14:00 | Bergama KM | Çocuk |
| Göztepe Isonem – Yalova Haremspor (TBL basketbol) | 28 Kas 15:30 | Altındağ Atatürk Spor Kompleksi, Bornova | Spor |
| Blackbriar, 1.120 TL'den | 5 Ara 20:00 | SoldOut, Karşıyaka | Konser |
| Onurr "Methiyeler", 18+, 500–650 TL | 11 Ara 21:45 | Skaff PSM, Konak | Konser |
| 3'lü Stand Up Gecesi Falan, 378–432 TL | 11 Ara 20:30 | Sardunya Alsancak, Konak | Kültür-Sanat |
| "Sefa ve Cefa" imza günü (Osman Kanat) | 28 Kas 14:00 | Buca | Kültür-Sanat (İmza günü) |
| Bir Düş Gibi (İzmir DT) | 11 Ara 20:00 | DT Urla AKM Sahnesi | Kültür-Sanat |

Dağılım: Çocuk 4, Kültür-Sanat 3, Konser 2, Spor 1. İlçe: Konak 4, Bergama 2, Bornova 1, Buca 1, Karşıyaka 1, Urla 1.

- Tek kaynaklılar: Bergama oyunu (Yeni Bakış, belediyenin Kasım programını aktarıyor; yaş ve ücret yok) ve Buca imza günü (İlkses haberi). Notlarında belirtildi.
- İzDSO 11 Aralık konseri İzBB verisinde zaten vardı; yeni kayıt açılmadı, fiyatı (430 TL, indirimli 355 TL) `ucretler.json`'a yazıldı.

## Mevcut kayıtlarda değişiklik

- **Özel Bir Rica (6 Ara):** saat 20:30 → 20:00 (Biletix ve Biletinial 20:00, yalnız iTicket 20:30). Fiyat 1.413–2.084 TL.
- **Göztepe – Erciyes 38 (3 Ara):** stat TFF programından teyit edildi (Gürsel Aksel). **Göztepe – Trabzonspor (30 Kas):** 550–4.750 TL.
- **Bir Düş Gibi (28 Kas):** asıl kaynak Biletinial DT sayfasıyla teyit edildi, 200–450 TL.
- Yaş biçimi düzeltildi: Gümüş Patenler 7+, Arkas Kışın Renkleri 2-3. Böcek Oteli seanslarının tükendi bilgisi notlara işlendi.
- **Fiyat tutarlılığı:** Biletinial liste sayfası fiyatları detay sayfasından ~%10 düşük (büyük olasılıkla hizmet bedeli hariç). Liste fiyatı "…TL'den" olarak yazıldı; detay sayfası olan çocuk oyunlarında detay fiyatı kullanıldı. DT çocuk oyunlarının "145 TL'den" fiyatı öğrenci bileti olabileceği için yazılmadı.
- Selçuk Zeytin Festivali (28–29 Kas) bu tur da belediyeden teyit edilemedi; notuna eklendi, kendiliğinden düşecek.

## Çocuk görselleri

- Yeni 4 çocuk kaydından 1'inde (Küçük Prens) `gorselAday` var; hiçbiri `gorsel`e taşınmadı.
- Görsel sunucuları (merlincdn.net, arkassanat) hem WebFetch'te hem proxy'de engelli; Music for Babies dahil eski adaylar da kontrol edilemedi. Dosyada 30 çocuk kaydında `gorselAday` bekliyor, elle bakılmalı.

## Elenenler ve nedenleri

| Neden | Örnekler |
|---|---|
| Saat/stat henüz kesin değil | Karşıyaka – Eskişehirspor (6 Ara), Menemen FK – Kastamonuspor (6 Ara), Gaziemir – Bigaspor (5 Ara), Aras Kargo – Beşiktaş (7 Ara 16:00, yalnız Spor Ekranı), Aliağa Petkimspor – Bahçeşehir (5 Ara), Şirinyer hipodrom programı |
| Asıl bilet sayfası yok (izmirmag tek kaynak) | Birsen Tezer, JOKER (Ooze); Mavi Gri, KILLOKI, Sezer Sarıgöz, Kerimcan Durmaz (Hayal Kahvesi); Candlelight Dilek Türkan, Mustafa Keser (Bostanlı); İzmir Tango Masalı; Cathedra Noel konserleri; Artemis Kitap Kulübü; 2 Yaka film gösterimi; 2 Aile Arasında gösterimi; Doğaçlama Tiyatro Festivali (Han); Christmas Town, Dam'da Dem, Angara Gecesi |
| Mekân adresi doğrulanamadı | Bora Gencer (5 Ara 20:30, Penguen Kültür Sanat Bistro; Biletinial tarih/saati teyit ediyor ama mekân adresi yok), Deli Cihan |
| Çelişki | Candles and Echoes (izmirmag 8/10 Ara St. John; AASSM 12 Ara), Deli Cihan (3 Ara mı 23 Kas mı), Bora Gencer Güzelbahçe kaydı |
| Saat/seans yok | GITFEST (2–6 Ara Fuar İzmir; saat ve ücret yok), PAW Patrol Festival Macerası 5 Ara, Etekler ve Pantolonlar (Çeşme, "çok yakında"), Kovacs (11 Ara, mekân yok), Çocuk Yılbaşı Partisi (Tiyatro Durağı) |
| Sayfa açılmadı | Vivaldi çocuk konseri (kultursanat.izmir.bel.tr), Bubilet çocuk atölyeleri, Arkas hafta içi program listesi |
| Eski yıl / aralık dışı | Kültürpark Yeni Yıl Festivali (2025), İzDSO 6 Ara (2024 sayfası), Melike Koçak/APİKAM söyleşileri, Hilltown LEGO ağacı, İçimizdeki Şeytan (17 Ara), Sermet Erkin (13/19 Ara), Bornova Yeni Yıl Festivali (12 Ara) |
| Halka kapalı / İzmir dışı | TTI İzmir turizm fuarı, AB İnsan Hakları Film Günleri (Ankara) |

## Mekân ve konum

- Yeni mekân yok. Göztepe basketbolunun salonu (Altındağ Atatürk Spor Kompleksi) adresi doğrulanamadığı için eklenmedi; Visit İzmir'deki "Bornova Atatürk Spor Kompleksi" ile aynı olup olmadığı kontrol edilmeli.
- **Koordinat eklenen 8 mekân:** 0168 Alsancak Gazi, 0171 Maske, 0172 Tiyatro Durağı, 0173 Boyoz Akademi, 0125 İstinyeArt (Biletinial harita gömmesi); 0076 Çeşme Çakabey, 0038 Batı Sahne, 0011 Kültürpark Açıkhava (iTicket).
- Hâlâ eksik çocuk mekânları: 0116 Ragıp Haykır, 0110 Arkas Göztepe, 0174 Bademler. iTicket'ın Karşıyaka Yunus Emre KSM (0121) koordinatı Eskişehir'i gösteriyor, kullanılmadı.
- `sektorler.py` çalıştırıldı. `cocuk.csv` ek sütunları 5 mekân (0125, 0168, 0171, 0172, 0173), `spor.csv` 5 mekân (0154, 0155, 0157, 0160, 0181) için dolduruldu. Maske'nin çalışan Biletinial adresi `/tr-tr/mekan/maske-sanat-tiyatrosu`.

## Kaynaklar

- Eklenenler KYN-109 – KYN-121: Biletinial mekân sayfaları (Alsancak Gazi/Baykuş, İzDSO, İzDOB, DEÜ Sabancı), Biletix mekân takvimleri (SoldOut, Ooze/Hayal Kahvesi, Hikmet Şimşek), AASSM aylık program, AA basketbol haftalık programı, Spor Ekranı Sultanlar Ligi, Flashscore (yalnız gün/rakip), Paribu Pass, OpenVan (yalnız İZFAŞ ile birlikte).
- KYN-020 Bubilet: sağlıksız olarak işaretlendi.
- **Erişim sorunları:** kultursanat.izmir.bel.tr (robots.txt), acikveriwapi.izmir.bel.tr (403), bubilet, merlincdn görselleri, tff.org (curl 403), ilçe belediyesi takvimleri (Bornova, Gaziemir, Foça, Torbalı, Ödemiş) bu oturumda depo dosyasından gelen adresle açılamadı; yalnız arama sonucunda çıkan adresler açılabiliyor.
- **Sheets eşitlenmedi.**

## Hâlâ boş kalan başlıklar

- Söyleşi, imza, kitap (yalnız 1 kayıt), film gösterimi, dans, müzikal, atölye
- Festival ve fuar (GITFEST saati, yeni yıl pazarları için 2026 duyurusu yok)
- Merkez dışı ilçeler: Urla dışında Çeşme, Seferihisar, Menemen, Torbalı, Ödemiş, Tire, Aliağa, Foça, Dikili, Kemalpaşa, Selçuk; merkezde Buca, Çiğli, Gaziemir, Narlıdere, Güzelbahçe, Karabağlar, Bayraklı
- Spor: hentbol, su topu, koşu, bisiklet, yelken, kite; 5–7 Aralık maçlarının saatleri
- Çocuk: 7–11 Aralık hafta içi, ücretsiz belediye/kütüphane etkinlikleri, AVM atölyeleri, çocuk konseri, çocuk sineması

## Sonraki tur için öneriler

1. **Spor:** TFF canlı yayın duyurusu (1–2 Ara) ve AA haftalık programları (3–4 Ara) ile 5 bekleyen maçı ekle; Aras Kargo – Beşiktaş için Biletinial satışını kontrol et. Altay – Kepez (29 Kas) statı maç günü teyit edilmeli (Alsancak bakım haberi çelişkisi).
2. **Yeni Bakış 30 Kas – 6 Ara takvimi** (Pazartesi çıkar) ve ilçe belediyesi duyuruları; belediye siteleri doğrudan açılamıyor, aramayla ulaşılmalı.
3. **Çocuk:** İzDOB "Pamira ve Ağustos Böceği" (11 Ara'dan itibaren, 85 TL'den) saat ve yaşı; AASSM ücretsiz konserleri (7 Ara oda müziği, 8 Ara DEÜ öğrenci orkestrası) ve "Seramiğin Genç İzleri" sergisi (4–31 Ara).
4. Biletinial İzmir listelerinde detay sayfası açılmamış ~20 tiyatro/stand-up/konser.
5. Görsel adaylarını elle kontrol et (30 çocuk kaydı).
