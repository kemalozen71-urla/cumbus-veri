"""mekanlar.csv'den sektör tablolarını üretir (sektorler/*.csv).

Temel sütunlar her seferinde mekanlar.csv'den yeniden yazılır; sektöre özgü
ek sütunlar (araştırmacının doldurdukları) Mekân ID'ye göre korunur.
Çalıştırma:  python toplayici/sektorler.py
"""
from __future__ import annotations

import csv
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from topla import sadelestir  # noqa: E402

KOK = Path(__file__).resolve().parent.parent
KLASOR = KOK / "sektorler"

TEMEL = ["Mekân ID", "Mekân", "İlçe", "Semt", "Tür", "Açık / Kapalı", "Adres", "Telefon",
         "Web sitesi", "Kapasite", "Google Maps"]


def _metin(m):
    return sadelestir(" ".join([m.get("Kategori", ""), m.get("Tür", ""), m.get("Mekân", ""), m.get("Salonlar", "")]))


def sinema(m):
    return m.get("Kategori") == "Sinema" or "sinema" in sadelestir(m.get("Tür", ""))


def konser(m):
    t = _metin(m)
    if spor(m) or sinema(m):
        return False
    return m.get("Kategori") == "Konser" or any(k in t for k in (
        "konser", "tiyatro", "sahne", "opera", "canli muzik", "salon"))


def spor(m):
    t = _metin(m)
    return m.get("Kategori") == "Spor" or any(k in t for k in ("stadyum", "spor salonu", "arena", "hipodrom", "velodrom"))


def cocuk(m):
    t = _metin(m)
    return m.get("Kategori") == "Çocuk" or any(k in t for k in ("cocuk", "kukla", "bilim merkezi", "oyun"))


def muze(m):
    t = _metin(m)
    return any(k in t for k in ("muze", "galeri", "sergi"))


def kultur(m):
    t = sadelestir(m.get("Tür", "") + " " + m.get("Mekân", ""))
    return "kultur merkezi" in t or "kultur sanat" in t or "kultur evi" in t


def acik(m):
    if m.get("Açık / Kapalı") == "Kapalı":
        return False
    t = sadelestir(m.get("Tür", ""))
    return m.get("Kategori") == "Açık alan" or any(k in t for k in ("meydan", "park", "acik alan", "tarihi alan", "antik", "acik hava"))


def fuar(m):
    t = _metin(m)
    return m.get("Kategori") == "Fuar" or any(k in t for k in ("fuar", "kongre"))


SEKTORLER = [
    # dosya, sekme adı, seçici, ek sütunlar
    ("sinemalar.csv", "Sinemalar", sinema, ["Beyazperde ID", "Bu hafta seans", "Salon sayısı", "Not (sektör)"]),
    ("konser_ve_sahne.csv", "Konser ve sahne", konser, ["Program sayfası", "Bilet sitesi", "Not (sektör)"]),
    ("spor.csv", "Spor", spor, ["Branş", "Ev sahibi takımlar", "Fikstür sayfası", "Not (sektör)"]),
    ("cocuk.csv", "Çocuk", cocuk, ["Yaş aralığı", "Program sayfası", "Fotoğraf", "Son doğrulama", "Not (sektör)"]),
    ("muze_ve_galeri.csv", "Müze ve galeri", muze, ["Açılış saatleri", "Ücret", "Not (sektör)"]),
    ("kultur_merkezleri.csv", "Kültür merkezleri", kultur, ["Program sayfası", "Not (sektör)"]),
    ("acik_alanlar.csv", "Açık alanlar", acik, ["Not (sektör)"]),
    ("fuar_ve_kongre.csv", "Fuar ve kongre", fuar, ["Program sayfası", "Not (sektör)"]),
]


def oku(yol: Path):
    if not yol.exists():
        return [], []
    with open(yol, encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        return list(r), r.fieldnames or []


def main():
    mekanlar, _ = oku(KOK / "mekanlar.csv")
    seans_say, bp_id = Counter(), {}
    yol = KOK / "seanslar.json"
    if yol.exists():
        s = json.loads(yol.read_text(encoding="utf-8"))
        for x in s.get("seanslar", []):
            seans_say[x["s"]] += 1
        for sin in s.get("sinemalar", []):
            if sin.get("mekanId"):
                bp_id[sin["mekanId"]] = sin["id"]
    KLASOR.mkdir(exist_ok=True)
    ozet = []
    for dosya, sekme, secici, ek in SEKTORLER:
        eski, eski_sutun = oku(KLASOR / dosya)
        eski_ek = {r["Mekân ID"]: r for r in eski if r.get("Mekân ID")}
        # Araştırmacının eklediği, mekanlar.csv'de olmayan ek sütunları da koru
        ek_tum = ek + [c for c in eski_sutun if c not in TEMEL and c not in ek]
        satirlar = []
        secilen = [m for m in mekanlar if secici(m) and m.get("Durum", "").lower() not in ("kapandı", "kapali", "kapalı (kalıcı)")]
        # Elle eklenmiş (mekanlar.csv'de olmayan) satırlar da kalsın
        idler = {m["Mekân ID"] for m in secilen}
        for m in secilen:
            satir = {c: m.get(c, "") for c in TEMEL}
            onceki = eski_ek.get(m["Mekân ID"], {})
            for c in ek_tum:
                satir[c] = onceki.get(c, "")
            if sekme == "Sinemalar":
                if m["Mekân ID"] in bp_id:
                    satir["Beyazperde ID"] = bp_id[m["Mekân ID"]]
                    satir["Bu hafta seans"] = str(seans_say.get(bp_id[m["Mekân ID"]], 0))
            satirlar.append(satir)
        for mid, r in eski_ek.items():
            if mid not in idler and not any(mid == m["Mekân ID"] for m in mekanlar):
                satirlar.append({c: r.get(c, "") for c in TEMEL + ek_tum})
        satirlar.sort(key=lambda r: (sadelestir(r["İlçe"]), sadelestir(r["Mekân"])))
        with open(KLASOR / dosya, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=TEMEL + ek_tum, lineterminator="\n")
            w.writeheader()
            w.writerows(satirlar)
        ozet.append(f"{sekme}: {len(satirlar)}")
    print(", ".join(ozet))


if __name__ == "__main__":
    main()
