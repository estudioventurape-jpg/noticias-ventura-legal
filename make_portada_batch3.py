#!/usr/bin/env python3
import sys
sys.path.insert(0, "/home/claude/noticias-ventura-legal")
from make_portada import make
from PIL import Image
import os

jobs = [
    dict(
        bg="/home/claude/noticias-ventura-legal/reels_build/2026-11-11/r1_vivienda/images/img03.png",
        png_out="/home/claude/noticias-ventura-legal/alquileres-vivienda-bcr/alquileres-vivienda-bcr-portada.png",
        jpg_out="/home/claude/noticias-ventura-legal/alquileres-vivienda-bcr/alquileres-vivienda-bcr-portada.jpg",
        category="Inmobiliario · BCR",
        headline="El ratio precio/alquiler en Lima baja con fuerza, según el BCR",
        stat_num=None, stat_label=None,
    ),
    dict(
        bg="/home/claude/noticias-ventura-legal/reels_build/2026-11-11/r3_plaft/images/img01.png",
        png_out="/home/claude/noticias-ventura-legal/bancos-alemanes-plaft/bancos-alemanes-plaft-portada.png",
        jpg_out="/home/claude/noticias-ventura-legal/bancos-alemanes-plaft/bancos-alemanes-plaft-portada.jpg",
        category="PLAFT · Internacional",
        headline="Los bancos más grandes de Alemania se unen contra el lavado de dinero",
        stat_num=None, stat_label=None,
    ),
]

for j in jobs:
    os.makedirs(os.path.dirname(j["png_out"]), exist_ok=True)
    make(j["bg"], j["png_out"], j["category"], j["headline"], j["stat_num"], j["stat_label"])
    im = Image.open(j["png_out"]).convert("RGB")
    im = im.resize((1200, 630), Image.LANCZOS)
    im.save(j["jpg_out"], "JPEG", quality=78, optimize=True)
    print(j["jpg_out"], os.path.getsize(j["jpg_out"]), "bytes")
