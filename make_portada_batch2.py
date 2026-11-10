#!/usr/bin/env python3
import sys
sys.path.insert(0, "/home/claude/noticias-ventura-legal")
from make_portada import make
from PIL import Image

jobs = [
    dict(
        bg="/home/claude/noticias-ventura-legal/reels_build/2026-11-10/img_1_extorsion/06.png",
        png_out="/home/claude/noticias-ventura-legal/extorsion/extorsion-portada.png",
        jpg_out="/home/claude/noticias-ventura-legal/extorsion/extorsion-portada.jpg",
        category="Penal · Cumplimiento",
        headline="Prestar tu cuenta para una extorsión ya es delito: hasta 15 años de cárcel",
        stat_num="15 años", stat_label="pena máxima de prisión por prestar o vender tu cuenta bancaria o billetera digital a un extorsionador",
    ),
    dict(
        bg="/home/claude/noticias-ventura-legal/reels_build/2026-11-10/img_2_nordea/01.png",
        png_out="/home/claude/noticias-ventura-legal/nordea/nordea-portada.png",
        jpg_out="/home/claude/noticias-ventura-legal/nordea/nordea-portada.jpg",
        category="PLAFT · Banca",
        headline="Nordea pagó US$23 millones de multa por fallas en PLAFT",
        stat_num="US$23M", stat_label="la multa que un tribunal de Copenhague impuso a Nordea por fallas en sus controles antilavado",
    ),
    dict(
        bg="/home/claude/noticias-ventura-legal/reels_build/2026-11-10/img_3_binance/02.png",
        png_out="/home/claude/noticias-ventura-legal/binance/binance-portada.png",
        jpg_out="/home/claude/noticias-ventura-legal/binance/binance-portada.jpg",
        category="Cripto · PLAFT",
        headline="Le robaron US$6,300 M a Binance y lo lavaron con memecoins",
        stat_num="US$6,300M", stat_label="robados a Binance; los hackers crearon memecoins y usaron más de 20,000 billeteras en una semana",
    ),
]

for j in jobs:
    make(j["bg"], j["png_out"], j["category"], j["headline"], j["stat_num"], j["stat_label"])
    im = Image.open(j["png_out"]).convert("RGB")
    im = im.resize((1200, 630), Image.LANCZOS)
    im.save(j["jpg_out"], "JPEG", quality=78, optimize=True)
    import os
    print(j["jpg_out"], os.path.getsize(j["jpg_out"]), "bytes")
