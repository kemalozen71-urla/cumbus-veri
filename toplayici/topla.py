"""Cümbüş veri toplayıcı.

1. mekanlar.csv (ana mekân veritabanı) -> mekanlar.json
2. İzBB Kültür Sanat API -> etkinlikler.json (her etkinlik Mekân ID ile eşlenir)

Sadece standart kütüphane + requests kullanır. Çalıştırma:
    python toplayici/topla.py
"""
from __future__ import annotations

import csv
import html
import json
import re
import sys
import unicodedata
from datetime import datetime, timedelta, timezone
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
IZBB_API = "https://acikveriwapi.izmir.bel.tr/KulturSanat/EtkinlikleriGetir"
TR = timezone(timedelta(hours=3))

KATEGORILER = ["Kültür-Sanat", "Konser", "Sinema", "Spor", "Festival", "Fuar", "Çocuk"]


# ---------------------------------------------------------------- yardımcılar
def sadelestir(s: str) -> str:
    """Karşılaştırma için: küçük harf, Türkçe harfler sadeleşmiş, tek boşluk."""
    s = (s or "").replace("İ", "i").replace("I", "ı").lower()
    s = s.translate(str.maketrans("ışçğöüâî", "iscgouai"))
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return f" {s.strip()} "


def anahtar(k: str) -> str:
    return sadelestir(k).replace(" ", "")


def sec(kayit: dict, *adaylar: str):
    """Alan adı büyük/küçük harf ya da Türkçe karakter farkıyla gelse de bulur."""
    tablo = {anahtar(k): v for k, v in kayit.items()}
    for a in adaylar:
        v = tablo.get(anahtar(a))
        if v not in (None, "", []):
            return v
    return None


def adlar(v) -> str:
    """{'ad': ..} ya da [{'ad': ..}, ..] biçimindeki alanları metne çevirir."""
    if isinstance(v, dict):
        return str(v.get("ad") or v.get("adi") or "")
    if isinstance(v, list):
        return ", ".join(a for a in (adlar(x) for x in v) if a)
    return str(v or "")


MEKAN_KALIBI = re.compile(
    r"(?:Mekân|Mekan|YER|Yer)\s*:\s*([^\n]{3,80}?)(?=\s+(?:SAAT|Saat|Tarih|TARİH|Katılım|Etkinlik)\b|\n|$)")


def temiz_metin(s) -> str:
    if not s:
        return ""
    s = re.sub(r"<br\s*/?>|</p>", "\n", str(s), flags=re.I)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t\r\f\v]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n\n", s)
    return s.strip()


def tarih(s):
    if not s:
        return None
    s = str(s).strip()
    m = re.match(r"/Date\((\d+)", s)
    if m:
        return datetime.fromtimestamp(int(m.group(1)) / 1000, TR)
    for f in ("%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M:%S",
              "%d.%m.%Y %H:%M:%S", "%d.%m.%Y %H:%M", "%d.%m.%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(s[:19], f).replace(tzinfo=TR)
        except ValueError:
            pass
    try:
        t = datetime.fromisoformat(s.replace("Z", "+00:00"))
        return t if t.tzinfo else t.replace(tzinfo=TR)
    except ValueError:
        return None


def iso(t):
    return t.astimezone(TR).isoformat(timespec="minutes") if t else None


# ---------------------------------------------------------------- mekânlar
def mekanlari_oku():
    mekanlar = []
    with open(KOK / "mekanlar.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            ilce_ham = (r.get("İlçe") or "").strip()
            m = re.match(r"^(.*?)\s*\((.*)\)$", ilce_ham)
            ilce, semt = (m.group(1), m.group(2)) if m else (ilce_ham, "")
            semt = (r.get("Semt") or "").strip() or semt

            def sayi(x):
                try:
                    return round(float(x), 6)
                except (TypeError, ValueError):
                    return None

            mekanlar.append({
                "id": r["Mekân ID"],
                "ad": r["Mekân"].strip(),
                "ilce": "" if ilce in ("—", "-") else ilce,
                "semt": semt,
                "acikKapali": r.get("Açık / Kapalı") or "Kapalı",
                "kategori": r.get("Kategori") or "Kültür-Sanat",
                "tur": r.get("Tür") or "",
                "adres": r.get("Adres") or "",
                "telefon": r.get("Telefon") or "",
                "ulasim": r.get("Nasıl giderim") or "",
                "googleMaps": r.get("Google Maps") or "",
                "appleMaps": r.get("Apple Maps") or "",
                "web": r.get("Web sitesi") or "",
                "enlem": sayi(r.get("Enlem")),
                "boylam": sayi(r.get("Boylam")),
                "durum": r.get("Durum") or "",
            })
    return mekanlar


def eslestirici(mekanlar):
    """Açıklama/mekân metninde geçen en uzun mekân adını bulur."""
    adlar = json.loads((KOK / "mekan_adlari.json").read_text(encoding="utf-8"))
    for m in mekanlar:
        adlar.setdefault(m["id"], [m["ad"]])
    liste = sorted(
        ((sadelestir(a), mid) for mid, al in adlar.items() for a in al if len(a) >= 4),
        key=lambda x: -len(x[0]),
    )

    def bul(*metinler):
        for metin in metinler:
            s = sadelestir(metin)
            if len(s) < 4:
                continue
            for ad, mid in liste:
                if ad in s:
                    return mid
        return None

    return bul


# ---------------------------------------------------------------- kategori
KAT_KURALLARI = [
    ("Sinema", ("sinema", "sinematek", "film", "gosterim")),
    ("Konser", ("konser", "resital", "muzik", "senfoni", "orkestra", "koro", "caz", "jazz", "dinleti")),
    ("Çocuk", ("cocuk", "masal", "kukla")),
    ("Festival", ("festival", "senlik", "fest ")),
    ("Fuar", ("fuar", "expo")),
    ("Spor", ("spor", "kosu", "maraton", "turnuva", "yuruyus", "bisiklet", "mac ")),
]


def kategori_bul(tur: str, ad: str, yas: str) -> str:
    t = sadelestir(tur)
    for kat, kelimeler in KAT_KURALLARI:
        if any(f" {k.strip()}" in t for k in kelimeler):
            return kat
    a = sadelestir(ad)
    for kat, kelimeler in KAT_KURALLARI:
        if any(f" {k.strip()} " in a for k in kelimeler):
            return kat
    if yas and re.search(r"\b([3-9]|1[0-2])\s*[-+]", str(yas)):
        return "Çocuk"
    return "Kültür-Sanat"


# ---------------------------------------------------------------- İzBB
def izbb_etkinlikleri(bul, mekan_sozlugu):
    import requests

    yanit = requests.get(IZBB_API, timeout=60, headers={"User-Agent": "cumbus-veri/1.0"})
    yanit.raise_for_status()
    ham = yanit.json()
    if isinstance(ham, dict):
        ham = sec(ham, "onemliyerler", "etkinlikler", "data", "result", "items") or []

    # İlk çalıştırmada alan adlarını görmek için örnek kaydı saklarız.
    if ham:
        (KOK / "kaynak_ornegi.json").write_text(
            json.dumps(ham[0], ensure_ascii=False, indent=1), encoding="utf-8")

    simdi = datetime.now(TR)
    sinir = simdi - timedelta(hours=6)
    cikti, eslesmeyen = [], {}
    for r in ham:
        ad = temiz_metin(sec(r, "Adi", "Ad", "EtkinlikAdi", "Baslik", "Name"))
        if not ad:
            continue
        basla = tarih(sec(r, "SonrakiSeansBaslangic", "SonrakiSeansBaslangicTarihi",
                          "EtkinlikBaslamaTarihi", "BaslangicTarihi", "Baslangic", "Tarih"))
        bitis = tarih(sec(r, "SonrakiSeansBitis", "SonrakiSeansBitisTarihi",
                          "EtkinlikBitisTarihi", "BitisTarihi", "Bitis"))
        if (bitis or basla) and (bitis or basla) < sinir:
            continue
        aciklama = temiz_metin(sec(r, "Aciklama", "KisaAciklama", "Detay", "Icerik"))
        mekan_metni = temiz_metin(sec(r, "EtkinlikMerkezi", "EtkinlikMerkezAdi", "MekanAdi",
                                      "Mekan", "Yer", "SalonAdi") or "")
        tur = temiz_metin(adlar(sec(r, "kategoriler", "Tur", "Turu", "EtkinlikTuru", "Kategori")))
        alt_tur = temiz_metin(adlar(sec(r, "turler")))
        yas = temiz_metin(str(sec(r, "yasSiniriAdi", "YasSiniri", "YasSinir", "Yas") or ""))
        if yas in ("0", "Genel izleyici"):
            yas = ""
        if not mekan_metni:
            mm = MEKAN_KALIBI.search(aciklama)
            if mm:
                mekan_metni = mm.group(1).strip(" .,:;")
        mekan_id = bul(mekan_metni, ad, aciklama)
        if not mekan_id:
            k = mekan_metni or aciklama[:80]
            eslesmeyen[k] = eslesmeyen.get(k, 0) + 1
        mekan = mekan_sozlugu.get(mekan_id) or {}
        ucretsiz = sec(r, "UcretsizMi", "Ucretsiz", "Ucret")
        if ucretsiz is None and re.search(r"[üÜ]cretsiz|ÜCRETSİZ", aciklama):
            ucretsiz = True
        if isinstance(ucretsiz, str):
            u = sadelestir(ucretsiz)
            ucretsiz = True if ("ucretsiz" in u or u.strip() in ("true", "evet")) else (
                False if u.strip() else None)
        gorsel = sec(r, "gorselUrl", "Resim", "BuyukAfis", "KucukAfis", "Gorsel", "Afis", "ResimUrl")
        kid = sec(r, "Id", "EtkinlikId", "ID")
        cikti.append({
            "id": f"izbb-{kid}" if kid else "izbb-" + str(abs(hash(ad + str(basla))))[:10],
            "ad": ad,
            "aciklama": aciklama[:1500],
            "kategori": kategori_bul(f"{tur} {alt_tur}", ad, yas),
            "tur": ", ".join(x for x in (tur, alt_tur) if x),
            "baslangic": iso(basla),
            "bitis": iso(bitis),
            "ucretsiz": ucretsiz if isinstance(ucretsiz, bool) else None,
            "yasSiniri": yas,
            "gorsel": gorsel if isinstance(gorsel, str) and gorsel.startswith("http") else None,
            "biletUrl": sec(r, "BiletSatisLinki", "BiletLinki", "BiletUrl"),
            "kaynakUrl": sec(r, "EtkinlikUrl", "Url", "Link") or "https://kultursanat.izmir.bel.tr",
            "organizator": temiz_metin(adlar(sec(r, "organizator", "Duzenleyen", "Organizatoru"))),
            "mekanId": mekan_id,
            "mekanMetni": mekan_metni,
            "acikKapali": mekan.get("acikKapali"),
            "kaynak": "İzmir Büyükşehir Belediyesi açık veri (CC BY 4.0)",
        })
    return cikti, eslesmeyen


# ---------------------------------------------------------------- ana akış
def yaz(ad, veri):
    (KOK / ad).write_text(json.dumps(veri, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def arastirma_etkinlikleri(bul, mekan_sozlugu, mevcut):
    """Araştırmacı ajanın doğruladığı etkinlikler (arastirma/etkinlikler.json)."""
    yol = KOK / "arastirma" / "etkinlikler.json"
    if not yol.exists():
        return []
    try:
        liste = json.loads(yol.read_text(encoding="utf-8")).get("etkinlikler") or []
    except (ValueError, AttributeError):
        print("arastirma/etkinlikler.json okunamadı")
        return []
    dun = (datetime.now(TR) - timedelta(days=1)).isoformat()
    gorulen = {(sadelestir(e["ad"]), (e["baslangic"] or "")[:10]) for e in mevcut}
    cikti = []
    for e in liste:
        if not isinstance(e, dict) or not e.get("ad") or not e.get("baslangic"):
            continue
        son = e.get("bitis") or e["baslangic"]
        if son < dun[:len(son)]:
            continue
        anahtar = (sadelestir(e["ad"]), e["baslangic"][:10])
        if anahtar in gorulen:
            continue
        gorulen.add(anahtar)
        mekan_id = e.get("mekanId")
        if mekan_id not in mekan_sozlugu:
            mekan_id = bul(e.get("mekanMetni") or "") if e.get("mekanMetni") else None
        mekan = mekan_sozlugu.get(mekan_id) or {}
        kategori = e.get("kategori") if e.get("kategori") in KATEGORILER else "Kültür-Sanat"
        cikti.append({
            "id": str(e.get("id") or "ara-" + str(abs(hash(anahtar)))[:10]),
            "ad": e["ad"],
            "aciklama": (e.get("aciklama") or "")[:1500],
            "kategori": kategori,
            "tur": e.get("tur") or "",
            "baslangic": e["baslangic"],
            "bitis": e.get("bitis"),
            "ucretsiz": e.get("ucretsiz") if isinstance(e.get("ucretsiz"), bool) else None,
            "yasSiniri": e.get("yasSiniri") or "",
            "gorsel": e.get("gorsel"),
            "biletUrl": e.get("biletUrl"),
            "kaynakUrl": e.get("kaynakUrl"),
            "organizator": e.get("organizator") or "",
            "mekanId": mekan_id,
            "mekanMetni": "" if mekan_id else (e.get("mekanMetni") or ""),
            "acikKapali": e.get("acikKapali") or mekan.get("acikKapali"),
            "kaynak": e.get("kaynak") or "Cümbüş araştırması",
        })
    print(f"araştırma: {len(cikti)} etkinlik eklendi")
    return cikti


def main():
    mekanlar = mekanlari_oku()
    sozluk = {m["id"]: m for m in mekanlar}
    simdi = iso(datetime.now(TR))
    yaz("mekanlar.json", {"guncelleme": simdi, "sehir": "İzmir", "mekanlar": mekanlar})
    print(f"mekanlar.json: {len(mekanlar)} mekân")

    if "--sadece-mekan" in sys.argv:
        return
    bul = eslestirici(mekanlar)
    etkinlikler, eslesmeyen = izbb_etkinlikleri(bul, sozluk)
    etkinlikler += arastirma_etkinlikleri(bul, sozluk, etkinlikler)
    etkinlikler.sort(key=lambda e: e["baslangic"] or "9999")
    yaz("etkinlikler.json", {
        "guncelleme": simdi,
        "sehir": "İzmir",
        "kategoriler": KATEGORILER,
        "etkinlikler": etkinlikler,
    })
    eslesen = sum(1 for e in etkinlikler if e["mekanId"])
    print(f"etkinlikler.json: {len(etkinlikler)} etkinlik, {eslesen} tanesi mekâna eşlendi")
    # Eşleşmeyen mekân metinleri: mekanlar.csv'ye eklenecek adaylar
    yaz("eslesmeyen_mekanlar.json",
        sorted(({"metin": k, "adet": v} for k, v in eslesmeyen.items()), key=lambda x: -x["adet"]))


if __name__ == "__main__":
    main()
