"""İzmir sinema seansları -> seanslar.json

Kaynak: Beyazperde. Sinema listesi bölge sayfasından (data-theater etiketleri),
seanslar her sinemanın günlük JSON ucundan (/_/showtimes/theater-ID/d-TARIH/).
Bugün + 3 gün toplanır. Çalıştırma:  python toplayici/seanslar.py
"""
from __future__ import annotations

import csv
import html
import json
import re
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
from topla import sadelestir  # noqa: E402

KOK = Path(__file__).resolve().parent.parent
TR = timezone(timedelta(hours=3))
SITE = "https://www.beyazperde.com"
BOLGE = SITE + "/sinemalar/bolgeye/154190/"
GUN_SAYISI = 4
H = {
    "User-Agent": "Mozilla/5.0 (cumbus-veri; +https://github.com/kemalozen71-urla/cumbus-veri)",
    "Accept-Language": "tr-TR,tr;q=0.9",
}

# İlçe merkezleri (yaklaşık). Sinemanın kendi konumu yoksa mesafe buradan hesaplanır.
ILCE_MERKEZ = {
    "Aliağa": (38.800, 26.972), "Balçova": (38.389, 27.050), "Bayındır": (38.218, 27.648),
    "Bayraklı": (38.462, 27.165), "Bergama": (39.120, 27.180), "Beydağ": (38.085, 28.210),
    "Bornova": (38.466, 27.220), "Buca": (38.388, 27.175), "Çeşme": (38.324, 26.304),
    "Çiğli": (38.495, 27.070), "Dikili": (39.070, 26.890), "Foça": (38.670, 26.757),
    "Gaziemir": (38.320, 27.130), "Güzelbahçe": (38.370, 26.890), "Karabağlar": (38.370, 27.120),
    "Karaburun": (38.640, 26.510), "Karşıyaka": (38.460, 27.110), "Kemalpaşa": (38.430, 27.420),
    "Kınık": (39.087, 27.380), "Kiraz": (38.230, 28.205), "Konak": (38.418, 27.129),
    "Menderes": (38.250, 27.130), "Menemen": (38.610, 27.070), "Narlıdere": (38.395, 26.990),
    "Ödemiş": (38.230, 27.970), "Seferihisar": (38.197, 26.840), "Selçuk": (37.950, 27.370),
    "Tire": (38.090, 27.730), "Torbalı": (38.150, 27.360), "Urla": (38.320, 26.765),
}
SEMT_ILCE = {"alsancak": "Konak", "mavisehir": "Karşıyaka", "tinaztepe": "Buca", "bostanli": "Karşıyaka"}
# Bölge listesinde çıkmayan ama Beyazperde'de seans yayımlayan sinemalar
EK_SINEMALAR = [
    {"id": "T0582", "ad": "Paribu Cineverse MaviBahçe",
     "adres": "Mavişehir Mah. Caher Dudayev Blv. (MaviBahçe AVM) Karşıyaka", "ilce": "Karşıyaka"},
    {"id": "T2911", "ad": "Paribu Cineverse Karşıyaka Hilltown",
     "adres": "Yalı Mah. 6522 Sk. No:3 (Hilltown AVM) Karşıyaka", "ilce": "Karşıyaka"},
]
COCUK_TURLERI = {"ANIMATION", "FAMILY"}
TUR_TR = {
    "ACTION": "Aksiyon", "ADVENTURE": "Macera", "ANIMATION": "Animasyon", "BIOPIC": "Biyografi",
    "COMEDY": "Komedi", "DRAMA": "Dram", "FAMILY": "Aile", "FANTASY": "Fantastik", "HORROR": "Korku",
    "THRILLER": "Gerilim", "SCIENCE_FICTION": "Bilim kurgu", "ROMANCE": "Romantik",
    "DOCUMENTARY": "Belgesel", "MUSICAL": "Müzikal", "CRIME": "Suç", "WAR": "Savaş",
    "HISTORICAL": "Tarih", "MYSTERY": "Gizem", "WESTERN": "Western",
}
SURUM = {"LOCAL": "Türkçe", "DUBBED": "Dublaj", "DUBBED_ST": "Dublaj", "ORIGINAL": "Altyazılı"}

oturum = requests.Session()
oturum.headers.update(H)


def al(url: str):
    for deneme in range(3):
        try:
            r = oturum.get(url, timeout=30)
            if r.status_code == 200:
                return r
            if r.status_code == 404:
                return None
        except requests.RequestException:
            pass
        time.sleep(2 + deneme * 3)
    return None


def ilce_bul(adres: str, baslik: str) -> str:
    s = sadelestir(adres)
    for ilce in ILCE_MERKEZ:
        if sadelestir(ilce) in s:
            return ilce
    for semt, ilce in SEMT_ILCE.items():
        if f" {semt} " in s:
            return ilce
    return baslik if baslik in ILCE_MERKEZ else ""


def mekan_eslestir():
    """mekanlar.csv'deki sinemaları ad benzerliğiyle bulmak için."""
    yol = KOK / "mekanlar.csv"
    liste = []
    if yol.exists():
        for m in csv.DictReader(open(yol, encoding="utf-8")):
            if "sinema" in sadelestir(m.get("Tür", "") + " " + m.get("Kategori", "")):
                kelime = set(sadelestir(m["Mekân"]).split()) - {"izmir", "sinemasi", "sinema", "avm"}
                liste.append((m, kelime))

    def bul(ad: str, ilce: str):
        k = set(sadelestir(ad).split()) - {"izmir", "sinemasi", "sinema", "avm"}
        en, puan = None, 0.0
        for m, mk in liste:
            if not mk or not k:
                continue
            p = len(k & mk) / len(k | mk)
            if m.get("İlçe") == ilce:
                p += 0.15
            if p > puan:
                en, puan = m, p
        return en if puan >= 0.5 else None

    return bul


def sinemalari_topla():
    sinemalar, gorulen = [], set()
    bul = mekan_eslestir()
    for sayfa in range(1, 8):
        r = al(BOLGE + (f"?page={sayfa}" if sayfa > 1 else ""))
        if not r:
            break
        yeni = 0
        baslik = ""
        # Sırayla: ilçe başlığı, sinema kimliği, adres
        for m in re.finditer(
            r'href="/sinemalar/civarinda/\d+/">([^<]+)</a>'
            r'|data-theater="([^"]+)"'
            r'|<address class="address[^"]*">([^<]*)</address>',
            r.text,
        ):
            if m.group(1):
                baslik = html.unescape(m.group(1)).strip()
            elif m.group(2):
                bilgi = json.loads(html.unescape(m.group(2)))
                if bilgi["id"] in gorulen:
                    continue
                gorulen.add(bilgi["id"])
                sinemalar.append({"id": bilgi["id"], "ad": bilgi["name"].strip(), "adres": "", "ilce": baslik})
                yeni += 1
            elif m.group(3) is not None and sinemalar and sinemalar[-1]["adres"] == "":
                sinemalar[-1]["adres"] = re.sub(r"\s+", " ", html.unescape(m.group(3))).strip()
        if yeni == 0:
            break
    for ek in EK_SINEMALAR:
        if ek["id"] not in gorulen:
            gorulen.add(ek["id"])
            sinemalar.append(dict(ek))
    for s in sinemalar:
        s["ilce"] = ilce_bul(s["adres"], s["ilce"])
        mekan = bul(s["ad"], s["ilce"])
        enlem = boylam = None
        if mekan:
            s["mekanId"] = mekan["Mekân ID"]
            try:
                enlem, boylam = float(mekan["Enlem"]), float(mekan["Boylam"])
            except (ValueError, TypeError):
                pass
        if enlem is None and s["ilce"] in ILCE_MERKEZ:
            enlem, boylam = ILCE_MERKEZ[s["ilce"]]
            s["konumYaklasik"] = True
        s["enlem"], s["boylam"] = enlem, boylam
        s["url"] = f"{SITE}/sinemalar/sinema-{s['id']}/"
    return sinemalar


def yas_siniri(seans: dict) -> str:
    for t in seans.get("data", {}).get("ticketing", []) or []:
        for u in t.get("urls", []):
            m = re.search(r"(\d{1,2})\+", u)
            if m:
                return m.group(1) + "+"
            if "Genel" in u:
                return "Genel"
    return ""


def main():
    simdi = datetime.now(TR)
    sinemalar = sinemalari_topla()
    print(f"{len(sinemalar)} sinema bulundu")
    if not sinemalar:
        print("Sinema listesi alınamadı; eski seanslar.json korunuyor")
        return
    filmler, seanslar = {}, []
    for s in sinemalar:
        for g in range(GUN_SAYISI):
            gun = (simdi + timedelta(days=g)).date().isoformat()
            sayfa = 1
            while True:
                ek = f"p-{sayfa}/" if sayfa > 1 else ""
                r = al(f"{SITE}/_/showtimes/theater-{s['id']}/d-{gun}/{ek}")
                if not r:
                    break
                try:
                    veri = r.json()
                except ValueError:
                    break
                for sonuc in veri.get("results") or []:
                    film = sonuc.get("movie") or {}
                    fid = str(film.get("internalId") or film.get("id"))
                    if not fid or fid == "None":
                        continue
                    turler = [g2.get("tag") for g2 in film.get("genres") or []]
                    if fid not in filmler:
                        filmler[fid] = {
                            "id": fid,
                            "ad": film.get("title") or "",
                            "orijinalAd": film.get("originalTitle") or "",
                            "turler": [TUR_TR.get(t, (g2.get("translate") or t)) for t, g2 in zip(turler, film.get("genres") or [])],
                            "sure": film.get("runtime") or "",
                            "afis": (film.get("poster") or {}).get("url") or "",
                            "ozet": (film.get("synopsis") or "")[:400],
                            "cocuk": bool(COCUK_TURLERI & set(turler)),
                            "yas": "",
                            "url": f"{SITE}/filmler/film-{fid}/",
                            "yerli": (film.get("languages") or []) == ["TURKISH"],
                        }
                    for liste in (sonuc.get("showtimes") or {}).values():
                        for se in liste or []:
                            bas = se.get("startsAt")
                            if not bas:
                                continue
                            if not filmler[fid]["yas"]:
                                filmler[fid]["yas"] = yas_siniri(se)
                            ekstra = [x for x in (se.get("projection") or []) if x not in ("DIGITAL",)]
                            if se.get("experience"):
                                ekstra += se["experience"] if isinstance(se["experience"], list) else [se["experience"]]
                            surum = SURUM.get(se.get("diffusionVersion") or "", "")
                            if filmler[fid]["yerli"]:
                                surum = "Türkçe"  # Türk filmleri bazı salonlarda yanlışlıkla 'dublaj' görünüyor
                            seanslar.append({
                                "f": fid, "s": s["id"], "t": bas[:16],
                                "v": surum,
                                "x": " ".join(str(e) for e in ekstra),
                            })
                sayfalama = veri.get("pagination") or {}
                if sayfa >= int(sayfalama.get("totalPages") or 1):
                    break
                sayfa += 1
            time.sleep(0.4)
    # Yaş sınırı 7+ ve altıysa animasyon/aile olmasa da çocuk filmi kabul et
    for f in filmler.values():
        m = re.match(r"(\d+)\+", f["yas"])
        if f["yas"] == "Genel" or (m and int(m.group(1)) <= 7 and "Animasyon" in f["turler"]):
            f["cocuk"] = True
    seanslar.sort(key=lambda x: (x["t"], x["s"]))
    if not seanslar:
        print("Hiç seans gelmedi; eski seanslar.json korunuyor")
        return
    cikti = {
        "guncelleme": simdi.isoformat(timespec="minutes"),
        "kaynak": "Beyazperde",
        "sinemalar": sinemalar,
        "filmler": sorted(filmler.values(), key=lambda f: f["ad"]),
        "seanslar": seanslar,
    }
    (KOK / "seanslar.json").write_text(json.dumps(cikti, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"{len(filmler)} film, {len(seanslar)} seans yazıldı")


if __name__ == "__main__":
    main()
