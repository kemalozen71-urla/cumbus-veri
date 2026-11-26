"""Mekân koordinatlarını OpenStreetMap Nominatim ile bulur.

- mekanlar.csv'de Enlem/Boylam boş olan mekânlar için arar.
- Sonuçlar konum_onbellek.json'da tutulur (bulunamayanlar 14 gün sonra yeniden denenir).
- Nominatim kuralı: saniyede en fazla 1 istek, tanımlı User-Agent. Bir çalışmada en fazla 80 sorgu.
- Sonuç ancak İzmir il sınırları içindeyse ve (biliniyorsa) ilçe merkezine 30 km'den yakınsa kabul edilir.

Çalıştırma: python toplayici/konumla.py
"""
from __future__ import annotations

import csv
import json
import re
import time
from datetime import datetime, timedelta, timezone
from math import asin, cos, radians, sin, sqrt
from pathlib import Path

import requests

KOK = Path(__file__).resolve().parent.parent
ONBELLEK = KOK / "konum_onbellek.json"
TR = timezone(timedelta(hours=3))
URL = "https://nominatim.openstreetmap.org/search"
UA = "CumbusIzmir/1.0 (https://github.com/kemalozen71-urla/cumbus-veri)"
SINIR = (37.75, 39.45, 26.15, 28.55)  # enlem min/max, boylam min/max
EN_FAZLA_SORGU = 80

from ilceler import ILCE_MERKEZ  # noqa: E402


def mesafe(a, b, c, d):
    r = 6371.0
    x = sin(radians(c - a) / 2) ** 2 + cos(radians(a)) * cos(radians(c)) * sin(radians(d - b) / 2) ** 2
    return 2 * r * asin(sqrt(x))


def temiz_ad(ad: str) -> str:
    ad = re.sub(r"\(.*?\)", " ", ad)
    return re.sub(r"\s+", " ", ad).strip()


def ilce_ayir(ham: str) -> str:
    m = re.match(r"^(.*?)\s*\((.*)\)$", ham or "")
    return (m.group(1) if m else (ham or "")).strip()


def sorgula(oturum, q: str):
    r = oturum.get(URL, params={
        "q": q, "format": "jsonv2", "limit": 3, "countrycodes": "tr",
        "viewbox": f"{SINIR[2]},{SINIR[1]},{SINIR[3]},{SINIR[0]}", "bounded": 1,
        "accept-language": "tr",
    }, timeout=30)
    time.sleep(1.1)
    if r.status_code != 200:
        return []
    return r.json()


def uygun(sonuc, ilce):
    try:
        e, b = float(sonuc["lat"]), float(sonuc["lon"])
    except (KeyError, TypeError, ValueError):
        return None
    if not (SINIR[0] <= e <= SINIR[1] and SINIR[2] <= b <= SINIR[3]):
        return None
    merkez = ILCE_MERKEZ.get(ilce)
    if merkez and mesafe(e, b, *merkez) > 30:
        return None
    return round(e, 6), round(b, 6)


def main():
    onbellek = json.loads(ONBELLEK.read_text(encoding="utf-8")) if ONBELLEK.exists() else {}
    simdi = datetime.now(TR)
    oturum = requests.Session()
    oturum.headers.update({"User-Agent": UA})
    sorgu = bulunan = 0
    with open(KOK / "mekanlar.csv", encoding="utf-8") as f:
        satirlar = list(csv.DictReader(f))
    for r in satirlar:
        mid = r["Mekân ID"]
        if (r.get("Enlem") or "").strip():
            continue
        k = onbellek.get(mid)
        if k and k.get("enlem"):
            continue
        if k and k.get("denendi"):
            try:
                if simdi - datetime.fromisoformat(k["denendi"]) < timedelta(days=14):
                    continue
            except ValueError:
                pass
        if sorgu >= EN_FAZLA_SORGU:
            break
        ilce = ilce_ayir(r.get("İlçe", ""))
        if ilce in ("—", "-"):
            ilce = ""
        ad = temiz_ad(r["Mekân"])
        adres = (r.get("Adres") or "").strip()
        denemeler = [f"{ad}, {ilce}, İzmir" if ilce else f"{ad}, İzmir"]
        if adres:
            denemeler.append(adres if "izmir" in adres.lower() else f"{adres}, İzmir")
        konum = None
        for q in denemeler:
            sorgu += 1
            try:
                for s in sorgula(oturum, q):
                    konum = uygun(s, ilce)
                    if konum:
                        break
            except requests.RequestException as hata:
                print(f"  hata {mid}: {hata}")
            if konum or sorgu >= EN_FAZLA_SORGU:
                break
        if konum:
            bulunan += 1
            onbellek[mid] = {"enlem": konum[0], "boylam": konum[1], "kaynak": "OpenStreetMap",
                             "ad": r["Mekân"], "bulundu": simdi.isoformat(timespec="seconds")}
            print(f"  ✓ {mid} {r['Mekân']} → {konum}")
        else:
            onbellek[mid] = {"denendi": simdi.isoformat(timespec="seconds"), "ad": r["Mekân"]}
    ONBELLEK.write_text(json.dumps(onbellek, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(f"konumla: {sorgu} sorgu, {bulunan} yeni konum, önbellekte {sum(1 for v in onbellek.values() if v.get('enlem'))} konum")


if __name__ == "__main__":
    main()
