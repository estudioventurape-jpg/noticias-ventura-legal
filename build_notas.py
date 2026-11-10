#!/usr/bin/env python3
# -*- coding: utf-8 -*-

STYLE = """
:root{--ink:#0E1216;--blue:#2A4A9C;--dblue:#20397A;--lblue:#8FA4D8;--soft:#E5EAF6;--soft2:#F2F5FB;--g1:#444C55;--g2:#5A6470;--l1:#C3C9D4;--l2:#DFE3EA;--bg:#fff}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);font-family:Inter,system-ui,sans-serif;color:var(--ink);line-height:1.5;font-size:15px}
.w{max-width:760px;margin:0 auto;padding-left:16px;padding-right:16px}
header.top{border-bottom:1px solid var(--l1)}
header .w{display:flex;justify-content:space-between;align-items:center;padding-block:14px}
.brand{font-family:Newsreader,Georgia,serif;font-size:20px;font-weight:500}
.brand i{color:var(--g2);font-weight:400;font-size:17px}
.brand small{font-family:Inter,sans-serif;font-size:10px;letter-spacing:1.4px;color:var(--g2);text-transform:uppercase;margin-left:10px}
main.w{padding-top:28px;padding-bottom:40px}
.lab{font-size:11px;letter-spacing:1.4px;text-transform:uppercase;color:var(--blue);font-weight:600}
h1{font-family:Newsreader,Georgia,serif;font-weight:500;font-size:clamp(30px,6vw,44px);line-height:1.08;margin:8px 0 10px;letter-spacing:-.3px;text-wrap:balance}
.sub{font-family:Newsreader,Georgia,serif;font-style:italic;color:var(--g2);font-size:18px;margin-bottom:4px}
.meta{font-size:13px;color:var(--g2);margin-top:10px}
.cover{width:100%;aspect-ratio:1200/630;object-fit:cover;display:block;margin-top:18px}
.cta{display:flex;flex-wrap:wrap;gap:10px;margin:22px 0 8px}
.btn{display:inline-block;padding:13px 20px;font-weight:600;font-size:14px;text-decoration:none;border:1px solid var(--ink);color:var(--ink);background:#fff;cursor:pointer}
.btn.p{background:var(--ink);color:#fff}
.btn.g{background:#25a244;border-color:#25a244;color:#fff}
.stat{background:var(--soft);padding:18px 20px;margin:28px 0;display:flex;align-items:baseline;gap:14px;flex-wrap:wrap}
.stat b{font-family:Newsreader,Georgia,serif;font-size:40px;color:var(--dblue);font-weight:500;font-variant-numeric:tabular-nums}
.stat span{font-size:14px;color:var(--g1);max-width:420px}
h2.s{font-family:Newsreader,Georgia,serif;font-weight:500;font-size:24px;border-top:2px solid var(--ink);padding-top:10px;margin:34px 0 12px}
h2.s span{color:var(--blue);margin-right:10px}
p{color:var(--g1);margin:0 0 14px;max-width:65ch}
p.lead{color:var(--ink);font-size:16px}
.src{font-size:12.5px;color:var(--g2);border-left:2px solid var(--l1);padding-left:10px;margin:10px 0 0}
footer{border-top:1px solid var(--l1);margin-top:40px;padding-block:22px 40px;font-size:13px;color:var(--g2)}
footer .nm{font-family:Newsreader,Georgia,serif;font-size:18px;color:var(--ink)}
.note{color:var(--g2);font-size:13px;margin-top:4px}
@media(max-width:640px){.brand small{display:none}}
""".strip()

TEMPLATE = """<html lang="es"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta property="og:type" content="article">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{og_description}">
<meta property="og:image" content="https://venturalegal.pe/noticias/{slug}/{slug}-portada.jpg">
<meta property="og:url" content="https://venturalegal.pe/noticias/{slug}/">
<meta name="twitter:card" content="summary_large_image">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Newsreader:ital,wght@0,400;0,500;1,400&display=swap" rel="stylesheet">
<style>
{style}
</style>
</head>
<body>
<header class="top"><div class="w"><div class="brand">Estudio Ventura <i>abogados</i><small>Noticias</small></div></div></header>
<main class="w">
<div class="lab">{lab}</div>
<h1>{h1}</h1>
<div class="sub">{sub}</div>
<div class="meta">{meta}</div>
<img class="cover" src="{slug}-portada.jpg" alt="{h1}">

<div class="cta">
<a class="btn p" href="https://www.tiktok.com/@victorventura.legal" target="_blank" rel="noopener">Ver el video en TikTok</a>
<a class="btn g" href="https://wa.me/51927995630?text=Hola%20V%C3%ADctor%2C%20quiero%20una%20consulta%20legal" target="_blank" rel="noopener">Escríbeme por WhatsApp</a>
</div>

<div class="stat"><b>{stat_num}</b><span>{stat_label}</span></div>

<p class="lead">{lead}</p>

<h2 class="s"><span>01</span>Qué pasó</h2>
<p>{s1}</p>

<h2 class="s"><span>02</span>Ángulo Perú</h2>
<p>{s2}</p>

<h2 class="s"><span>03</span>Ángulo legal{s3_suffix}</h2>
<p>{s3}</p>

<p class="src">{src}</p>
</main>
<footer><div class="w">
<div class="nm">Víctor Ventura</div>
<div class="note">Director – Ventura Legal · Contenido legal y financiero para el Perú</div>
</div></footer>


</body></html>
"""

NOTES = [
    dict(
        slug="extorsion",
        title="Prestar tu cuenta para una extorsión ya es delito: hasta 15 años de cárcel | Estudio Ventura",
        description="El Ejecutivo modificó el Código Penal: hasta 15 años de prisión a quien preste o venda su cuenta bancaria o billetera digital para que un extorsionador cobre el pago.",
        og_title="Prestar tu cuenta para una extorsión ya es delito: hasta 15 años de cárcel",
        og_description="Nueva modificación al Código Penal apunta a las cuentas mula que usan las bandas de extorsión en el Perú. Por Víctor Ventura.",
        lab="Penal · Cumplimiento",
        h1="Prestar tu cuenta para una extorsión ya es delito: hasta 15 años de cárcel",
        sub="El Ejecutivo modificó el Código Penal para golpear las cuentas mula que usan las bandas de extorsión",
        meta="10 de noviembre de 2026 · Victor Ventura, Director – Ventura Legal",
        stat_num="15 años",
        stat_label="pena máxima de prisión por prestar o vender tu cuenta bancaria o billetera digital a un extorsionador",
        lead="El Ejecutivo modificó el Código Penal: ahora castiga con hasta quince años de prisión a quien preste o venda su cuenta bancaria o su billetera digital para que un extorsionador cobre el pago, según Semana Económica.",
        s1="La norma apunta directo a las cuentas mula que usan las bandas de extorsión en el Perú, muchas veces a través de Yape o Plin. Hasta ahora, prestar una cuenta para que otro cobre un depósito se trataba casi como un favor; con el cambio, pasa a ser un delito con una pena muy alta.",
        s2="Las cuentas mula son el eslabón que permite a las bandas de extorsión cobrar sin exponer sus propias cuentas. Golpear ese eslabón es, junto con la persecución penal directa, una de las pocas palancas legales que el Estado tiene para frenar el cobro de extorsiones sin necesidad de capturar primero a toda la organización criminal.",
        s3_suffix=" (PLAFT)",
        s3="Para bancos y billeteras digitales, que son sujetos obligados ante la UIF, la norma eleva la presión para detectar y reportar estos movimientos a tiempo. Y para cualquier persona: si alguien te ofrece dinero fácil por prestar tu cuenta o tu DNI, ya no es solo un tema ético — es un delito con una pena muy alta.",
        src="Fuente: Semana Económica. Información referencial; no constituye asesoría legal.",
    ),
    dict(
        slug="nordea",
        title="Nordea pagó US$23 millones de multa por fallas en PLAFT: lo que exige la SBS en Perú | Estudio Ventura",
        description="Un tribunal de Copenhague multó al banco Nordea con US$23 millones por fallas en sus controles contra el lavado de activos entre 2012 y 2015. Qué exigen la SBS y la UIF en el Perú.",
        og_title="Nordea pagó US$23 millones de multa por fallas en PLAFT",
        og_description="Un tribunal de Copenhague sancionó a Nordea por fallas antilavado. Qué significa para la debida diligencia en el Perú. Por Víctor Ventura.",
        lab="PLAFT · Banca",
        h1="Nordea pagó US$23 millones de multa por fallas en PLAFT",
        sub="Un tribunal de Copenhague sancionó al banco por fallas en sus controles contra el lavado de activos entre 2012 y 2015",
        meta="10 de noviembre de 2026 · Victor Ventura, Director – Ventura Legal",
        stat_num="US$23M",
        stat_label="la multa que un tribunal de Copenhague impuso a Nordea por fallas en sus controles antilavado",
        lead="Un tribunal de Copenhague multó al banco Nordea con veintitrés millones de dólares por fallas en sus controles contra el lavado de activos entre 2012 y 2015, según Reuters.",
        s1="La sanción se centra en deficiencias de varios años en los controles antilavado de uno de los bancos nórdicos más grandes, que ya había enfrentado sanciones similares en otros países por el mismo tipo de fallas en la supervisión de sus clientes.",
        s2="El caso confirma que incluso bancos grandes y con sistemas de cumplimiento maduros pueden fallar durante años antes de que el regulador actúe, y que las multas por PLAFT pueden ser mucho mayores que el costo de mantener un programa de cumplimiento robusto.",
        s3_suffix=" (PLAFT)",
        s3="En el Perú, la SBS y la UIF exigen lo mismo a los bancos y a las empresas sujetas a PLAFT: conocer bien a sus clientes, vigilar movimientos raros y reportarlos a tiempo. Si tu empresa es sujeto obligado, no basta con tener un manual de prevención en un cajón: hay que aplicarlo, capacitar al personal y guardar la evidencia. Así es como se defiende un oficial de cumplimiento.",
        src="Fuente: Reuters. Información referencial; no constituye asesoría legal ni de inversión.",
    ),
    dict(
        slug="binance",
        title="Robaron US$6,300 millones a Binance y los lavaron con memecoins | Estudio Ventura",
        description="Hackers robaron US$6,300 millones a Binance y crearon al menos 6 criptomonedas tipo meme para lavar el dinero en días. Qué exigen la SBS y la UIF a los exchanges en el Perú.",
        og_title="Robaron US$6,300 millones a Binance y los lavaron con memecoins",
        og_description="Hackers señalados como norcoreanos lavaron US$6,300 millones robados a Binance con memecoins. El ángulo PLAFT para el Perú. Por Víctor Ventura.",
        lab="Cripto · PLAFT",
        h1="Le robaron US$6,300 millones a Binance y lo lavaron con memecoins",
        sub="Hackers señalados por Estados Unidos como norcoreanos crearon al menos 6 criptomonedas tipo meme para disfrazar el dinero",
        meta="10 de noviembre de 2026 · Victor Ventura, Director – Ventura Legal",
        stat_num="US$6,300M",
        stat_label="robados a Binance; los hackers crearon memecoins y usaron más de 20,000 billeteras en una semana para lavarlo",
        lead="A un exchange de criptomonedas le robaron seis mil trescientos millones de dólares, y para lavarlo inventaron monedas de broma. Hackers señalados por Estados Unidos como norcoreanos robaron ese monto a Binance y, según Bloomberg, crearon al menos seis criptomonedas tipo meme en pocos días para disfrazar el camino del dinero.",
        s1="En solo una semana, los atacantes usaron más de veinte mil billeteras digitales distintas para mover los fondos robados, repartiendo el rastro en miles de direcciones y dificultando el seguimiento.",
        s2="El caso confirma que el lavado con cripto ya no pasa solo por mezcladores o exchanges opacos: ahora incluye la creación de activos nuevos, diseñados para generar volumen y confundir el origen del dinero en horas.",
        s3_suffix=" (PLAFT)",
        s3="En el Perú, la SBS y la UIF ya piden a los exchanges y a las empresas que operan con criptoactivos que vigilen este tipo de movimientos. Si usas un exchange de criptomonedas, revisa que esté registrado y que reporte operaciones ante la UIF. Y si tu empresa acepta pagos en cripto, esa actividad ya debe estar en tu matriz de riesgo de PLAFT.",
        src="Fuente: Bloomberg. Información referencial; no constituye asesoría legal ni de inversión.",
    ),
]

import os

for n in NOTES:
    out = TEMPLATE.format(style=STYLE, **n)
    d = f"/home/claude/noticias-ventura-legal/{n['slug']}"
    os.makedirs(d, exist_ok=True)
    path = os.path.join(d, "index.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(out)
    print("wrote", path, len(out), "bytes")
