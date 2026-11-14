#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, "/home/claude/noticias-ventura-legal")
from build_notas import TEMPLATE, STYLE

NOTES = [
    dict(
        slug="alquileres-vivienda-bcr",
        title="Comprar departamento en Lima se paga más rápido con el alquiler, según el BCR | Estudio Ventura",
        description="El ratio entre el precio de venta y el alquiler en Lima bajó con fuerza este año, según el BCR: ya no toma tantos años de renta recuperar lo pagado por un departamento.",
        og_title="Comprar un departamento en Lima se paga más rápido con el alquiler",
        og_description="El ratio precio/alquiler bajó con fuerza según el BCR. Qué significa para quien compra para alquilar en Lima. Por Víctor Ventura.",
        lab="Inmobiliario · BCR",
        h1="Comprar un departamento en Lima se paga más rápido con el alquiler",
        sub="El ratio entre el precio de venta y el alquiler bajó con fuerza este año, según el Banco Central de Reserva",
        meta="11 de noviembre de 2026 · Victor Ventura, Director – Ventura Legal",
        stat_num="↓ ratio",
        stat_label="precio/alquiler en Lima: bajó con fuerza este año porque las rentas subieron más rápido que los precios, según el BCR",
        lead="Comprar un departamento en Lima hoy se paga con el alquiler mucho más rápido que hace unos años. El ratio entre el precio de venta y el alquiler bajó con fuerza este año, porque las rentas subieron más rápido que los precios, según el Banco Central de Reserva.",
        s1="En la práctica, ya no toma tantos años de renta recuperar lo que se pagó por el departamento. Hay distritos donde ese retorno es más veloz que en otros, así lo señala el propio BCR en sus reportes sobre el mercado inmobiliario.",
        s2="Para quien compra pensando en alquilar, el cambio es relevante: un ratio precio/alquiler más bajo suele indicar que, comparado con los últimos años, los alquileres rinden más en proporción al precio del inmueble. Pero el retorno varía mucho según la zona, así que no todos los distritos ofrecen la misma ventaja.",
        s3_suffix="",
        s3="Si piensas comprar para alquilar, revisa bien la zona y el contrato antes de firmar. Un contrato de arrendamiento formal y registrado te protege si el inquilino deja de pagar, y facilita cualquier proceso de cobro o desalojo si llega a ser necesario.",
        pull="“Ya no toma tantos años de renta recuperar lo que se pagó por el departamento.”",
        src="Fuente: Banco Central de Reserva del Perú (BCR). Información referencial; no constituye asesoría de inversión.",
    ),
    dict(
        slug="bancos-alemanes-plaft",
        title="Los bancos más grandes de Alemania se unen contra el lavado de dinero: el espejo PLAFT en el Perú | Estudio Ventura",
        description="Los principales bancos alemanes crearon una alianza para compartir datos y detectar operaciones sospechosas más rápido. En el Perú, la SBS y la UIF ya exigen algo parecido bajo el sistema PLAFT.",
        og_title="Los bancos más grandes de Alemania se unen contra el lavado de dinero",
        og_description="Una alianza bancaria alemana comparte datos para detectar lavado de activos. El espejo con el sistema PLAFT en el Perú. Por Víctor Ventura.",
        lab="PLAFT · Internacional",
        h1="Los bancos más grandes de Alemania se unen contra el lavado de dinero",
        sub="Crearon una alianza para compartir datos y detectar operaciones sospechosas más rápido, según Reuters",
        meta="11 de noviembre de 2026 · Victor Ventura, Director – Ventura Legal",
        stat_num="PLAFT",
        stat_label="sistema peruano de prevención del lavado de activos y financiamiento del terrorismo, con exigencias similares a las de la nueva alianza alemana",
        lead="Los bancos más grandes de Alemania se unieron para pelear juntos contra el lavado de dinero. Crearon una alianza para compartir datos y detectar operaciones sospechosas más rápido, según Reuters.",
        s1="La alianza busca cerrar un vacío conocido: cada banco veía solo una parte del movimiento de un cliente o de una red de cuentas, mientras que quienes lavan activos suelen repartir sus operaciones entre varias entidades para no llamar la atención. Compartir datos entre bancos permite detectar patrones que ningún banco vería solo.",
        s2="El modelo alemán anticipa hacia dónde va la supervisión antilavado en general: menos silos de información y más colaboración entre entidades obligadas, siempre dentro de reglas claras de protección de datos.",
        s3_suffix=" (PLAFT)",
        s3="En el Perú, la SBS y la UIF ya exigen a los sujetos obligados reportar este tipo de operaciones dentro del sistema de Prevención del Lavado de Activos y Financiamiento del Terrorismo (PLAFT). Si tu empresa es sujeto obligado, revisa tu oficial de cumplimiento y tus manuales PLAFT antes de que te caiga una supervisión: no basta con tenerlos, hay que aplicarlos y dejar evidencia de que se aplican.",
        pull="“Compartir datos entre bancos permite detectar patrones que ningún banco vería solo.”",
        src="Fuente: Reuters. Información referencial; no constituye asesoría legal.",
    ),
]

for n in NOTES:
    out = TEMPLATE.format(style=STYLE, **n)
    d = f"/home/claude/noticias-ventura-legal/{n['slug']}"
    os.makedirs(d, exist_ok=True)
    path = os.path.join(d, "index.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(out)
    print("wrote", path, len(out), "bytes")
