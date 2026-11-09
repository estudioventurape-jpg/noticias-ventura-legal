#!/usr/bin/env python3
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps

W, H = 1600, 840

INTER_BOLD = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"
INTER_SEMIBOLD = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"
SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"


def wrap_text(draw, text, font, max_width):
    words = text.split()
    lines = []
    cur = ""
    for w in words:
        test = (cur + " " + w).strip()
        bbox = draw.textbbox((0, 0), test, font=font)
        if bbox[2] - bbox[0] <= max_width or not cur:
            cur = test
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def make(bg_path, out_path, category, headline, stat_num=None, stat_label=None):
    img = Image.open(bg_path).convert("RGB")
    img = ImageOps.fit(img, (W, H), method=Image.LANCZOS)

    # dark gradient overlay bottom-left for text legibility
    overlay = Image.new("L", (W, H), 0)
    odraw = ImageDraw.Draw(overlay)
    for y in range(H):
        # stronger darkness toward bottom
        alpha = int(190 * max(0, (y - H * 0.35) / (H * 0.65)))
        odraw.line([(0, y), (int(W * 0.95), y)], fill=min(alpha, 190))
    for x in range(W):
        pass
    black = Image.new("RGB", (W, H), (5, 8, 14))
    img = Image.composite(black, img, overlay)

    # slight top darkening for stat box legibility
    top_overlay = Image.new("L", (W, H), 0)
    tdraw = ImageDraw.Draw(top_overlay)
    for y in range(0, int(H * 0.3)):
        alpha = int(120 * (1 - y / (H * 0.3)))
        tdraw.line([(int(W * 0.5), y), (W, y)], fill=alpha)
    img = Image.composite(black, img, top_overlay)

    draw = ImageDraw.Draw(img)

    cat_font = ImageFont.truetype(INTER_BOLD, 22)
    headline_font = ImageFont.truetype(SERIF_BOLD, 56)
    stat_num_font = ImageFont.truetype(SERIF_BOLD, 70)
    stat_label_font = ImageFont.truetype(INTER_SEMIBOLD, 20)

    margin_x = 64
    # category caption
    cat_text = f"ESTUDIO VENTURA · {category.upper()}"
    draw.text((margin_x, H - 220), cat_text, font=cat_font, fill=(235, 238, 245))

    # headline, wrapped, up to 2 lines
    max_w = int(W * 0.72)
    lines = wrap_text(draw, headline, headline_font, max_w)
    y = H - 185
    for line in lines[:2]:
        draw.text((margin_x, y), line, font=headline_font, fill=(255, 255, 255))
        bbox = draw.textbbox((0, 0), line, font=headline_font)
        y += (bbox[3] - bbox[1]) + 18

    if stat_num:
        num_bbox = draw.textbbox((0, 0), stat_num, font=stat_num_font)
        num_w = num_bbox[2] - num_bbox[0]
        sx = W - margin_x - num_w
        draw.text((sx, 50), stat_num, font=stat_num_font, fill=(255, 255, 255))
        label_lines = wrap_text(draw, stat_label.upper(), stat_label_font, 420)
        ly = 50 + (num_bbox[3] - num_bbox[1]) + 10
        for ll in label_lines:
            lb = draw.textbbox((0, 0), ll, font=stat_label_font)
            lw = lb[2] - lb[0]
            draw.text((W - margin_x - lw, ly), ll, font=stat_label_font, fill=(200, 210, 230))
            ly += (lb[3] - lb[1]) + 6

    img.save(out_path)
    print("wrote", out_path)


if __name__ == "__main__":
    make(
        "/mnt/user-data/uploads/Downloads/reel_assets/sunafil-bg-raw.png",
        "/home/claude/noticias-ventura-legal/sunafil/sunafil-portada.png",
        "Laboral · Cumplimiento",
        "Sunafil ya puede multarte si no tienes el protocolo El Niño",
        "S/ 1M", "multa máxima que podría aplicar Sunafil por incumplir el protocolo"
    )
    make(
        "/mnt/user-data/uploads/Downloads/reel_assets/gmoney-bg-raw.png",
        "/home/claude/noticias-ventura-legal/gmoney/gmoney-portada.png",
        "Fintech · PLAFT",
        "GMoney mueve cripto entre países: lo que exige la SBS",
        None, None
    )
    make(
        "/mnt/user-data/uploads/Downloads/reel_assets/sandoval-bg-raw.png",
        "/home/claude/noticias-ventura-legal/sandoval/sandoval-portada.png",
        "Inmobiliario · Proyectos",
        "Coworking en el Jorge Chávez: el plan de Grupo Sandoval",
        "+12,000 m²", "de oficinas proyectadas junto al terminal de pasajeros"
    )
    make(
        "/mnt/user-data/uploads/Downloads/reel_assets/jne-bg-raw.png",
        "/home/claude/noticias-ventura-legal/jne/jne-portada.png",
        "Electoral · Municipal",
        "JNE vs López Aliaga: ¿le darán la credencial de regidor?",
        None, None
    )
