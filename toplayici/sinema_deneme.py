"""Beyazperde yapısını incelemek için geçici deneme betiği."""
import json, re, datetime, pathlib, requests
H = {"User-Agent": "Mozilla/5.0 (cumbus-veri; +https://github.com/kemalozen71-urla/cumbus-veri)",
     "Accept-Language": "tr-TR,tr;q=0.9"}
OUT = pathlib.Path("deneme"); OUT.mkdir(exist_ok=True)
rapor = {}
def al(url):
    try:
        r = requests.get(url, headers=H, timeout=30)
        return r.status_code, r.text
    except Exception as e:
        return -1, str(e)
linkler = {}
for sayfa in range(1, 6):
    url = "https://www.beyazperde.com/sinemalar/bolgeye/154190/" + (f"?page={sayfa}" if sayfa > 1 else "")
    kod, html = al(url)
    rapor[url] = kod
    if sayfa == 1:
        (OUT / "bolge.html").write_text(html[:400000])
    for m in re.finditer(r'href="(/sinemalar/sinema-[^"/]+/)"[^>]*>([^<]{0,120})', html):
        linkler.setdefault(m.group(1), m.group(2).strip())
    for m in re.finditer(r'(/sinemalar/sinema-[A-Za-z0-9]+/)', html):
        linkler.setdefault(m.group(1), "")
rapor["sinemalar"] = linkler
bugun = datetime.date.today().isoformat()
if linkler:
    ilk = sorted(linkler)[0]
    kod, html = al("https://www.beyazperde.com" + ilk)
    rapor["ilk_sinema"] = [ilk, kod]
    (OUT / "sinema.html").write_text(html[:600000])
    tid = re.search(r"sinema-([A-Za-z0-9]+)", ilk).group(1)
    for u in [f"https://www.beyazperde.com/_/showtimes/theater-{tid}/d-{bugun}/",
              f"https://www.beyazperde.com/_/showtimes/theater-{tid}/",
              f"https://www.beyazperde.com/sinemalar/sinema-{tid}/seanslar/d-{bugun}/"]:
        kod, txt = al(u)
        rapor[u] = kod
        (OUT / ("uc_" + re.sub(r"\W+", "_", u)[-60:] + ".txt")).write_text(txt[:300000])
(OUT / "rapor.json").write_text(json.dumps(rapor, ensure_ascii=False, indent=1))
