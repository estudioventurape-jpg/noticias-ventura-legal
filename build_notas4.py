#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "/home/claude/noticias-ventura-legal")
from build_notas import STYLE, TEMPLATE
import os

NOTES = [
    dict(
        slug="extincion-dominio",
        title="El Congreso le devuelve autonomía a la extinción de dominio | Estudio Ventura",
        description="La Cámara de Diputados aprobó restablecer la autonomía de la extinción de dominio, sin esperar sentencia penal firme. El ángulo PLAFT para el Perú.",
        og_title="Extinción de dominio: el Congreso le devuelve autonomía al proceso",
        og_description="La Cámara de Diputados aprobó restablecer la autonomía de la extinción de dominio. El ángulo PLAFT para el Perú. Por Víctor Ventura.",
        lab="PLAFT · Penal",
        h1="El Congreso le devuelve autonomía a la extinción de dominio",
        sub="La Cámara de Diputados aprobó, el 10 de noviembre, que el Estado ya no tenga que esperar una sentencia penal firme para recuperar bienes de origen ilícito",
        meta="12 de noviembre de 2026 · Victor Ventura, Director – Ventura Legal",
        stat_num="US$50M",
        stat_label="lo que el Estado dejó de recuperar en bienes ilícitos, según el Congreso, mientras rigió la norma que ahora se corrige",
        lead="El diez de noviembre, la Cámara de Diputados aprobó, con 66 votos a favor, un dictamen que le devuelve autonomía al proceso de extinción de dominio: el Estado ya no tendrá que esperar una sentencia penal firme para recuperar un bien de origen ilícito, según Gestión y El Comercio.",
        s1="La norma, que modifica el Decreto Legislativo 1373, corrige los efectos de la llamada Ley Soto (Ley N.° 32104), que había condicionado la extinción de dominio a que termine todo el proceso penal. Según la presidenta de la Comisión de Justicia, Catherin Palomino, esa traba le costó al Estado unos cincuenta millones de dólares en bienes que dejó de recuperar. El texto todavía debe pasar por el Senado antes de convertirse en ley.",
        s2="Con el cambio, la Fiscalía podrá iniciar el proceso de extinción de dominio en paralelo al proceso penal, sin esperar su resultado, sobre inmuebles, vehículos o cuentas vinculados a narcotráfico, lavado de activos, corrupción o minería ilegal. El Ministerio Público mantiene la carga de probar el origen ilícito del bien, y quien compró de buena fe y puede probarlo puede pedir que lo excluyan del proceso.",
        s3_suffix=" (PLAFT)",
        s3="Para empresas y personas con activos de procedencia dudosa, la ventana para regularizar se estrecha: ya no alcanza con que el proceso penal se demore. Para sujetos obligados ante la UIF, la norma es una señal más de que el Estado está afinando sus herramientas de recuperación de activos.",
        pull="“El Estado ya no tendrá que esperar una sentencia penal firme para recuperar un bien de origen ilícito.”",
        src="Fuentes: Gestión, El Comercio y La República. Información referencial; no constituye asesoría legal.",
    ),
    dict(
        slug="banco-supervisor",
        title="Por qué quebró el banco Ueno en Paraguay (y no fue por ser digital) | Estudio Ventura",
        description="Solvencia de 5.56% frente a un mínimo legal de 12%, préstamos vinculados por US$146 millones y un supervisor con conflicto de interés. La lección para el Perú.",
        og_title="El banco Ueno no quebró por ser digital: quebró por fallas clásicas de supervisión",
        og_description="Solvencia de 5.56%, préstamos vinculados excesivos y un regulador sin independencia real. La lección para el Perú. Por Víctor Ventura.",
        lab="PLAFT · Banca",
        h1="El banco Ueno no quebró por ser digital",
        sub="Quebró por fallas clásicas de supervisión: préstamos vinculados excesivos y un regulador sin independencia real",
        meta="12 de noviembre de 2026 · Victor Ventura, Director – Ventura Legal",
        stat_num="5.56%",
        stat_label="la solvencia con la que colapsó el banco Ueno en Paraguay; la ley exige un mínimo de 12%",
        lead="El banco digital paraguayo Ueno colapsó con una solvencia de apenas 5.56%, muy por debajo del mínimo legal de 12%, y arrastró consigo la renuncia del presidente Santiago Peña. Pero, según la abogada Ljubica Vodanovic en Gestión, el problema no fue que el banco fuera digital.",
        s1="Ueno tenía más de ciento cuarenta y seis millones de dólares prestados a empresas relacionadas, algunos por encima del límite legal, y los fondos públicos llegaban al 29% de sus depósitos. El golpe final fue de supervisión: el jefe del banco central que debía vigilarlo había presidido antes ese mismo banco.",
        s2="En el Perú, la SBS limita los préstamos a empresas vinculadas al 25% del capital de nivel 1, exige que se aprueben antes por el directorio y en condiciones de mercado, y tiene autonomía constitucional frente al Gobierno. Son, justamente, las tres reglas de Basilea que Paraguay no aplicó: control de conflictos de interés, diversificación del riesgo y un supervisor independiente.",
        s3_suffix=" (cumplimiento)",
        s3="Si eres parte de un directorio, de un área de riesgos o de cumplimiento, el caso Ueno es un recordatorio concreto: revisa tus límites de crédito a partes vinculadas, la concentración de tus fuentes de fondeo y qué tan independiente es, en la práctica, quien te supervisa. La tecnología nunca es la excusa.",
        pull="“El banco Ueno no quebró por ser digital: quebró por fallas clásicas de supervisión.”",
        src="Fuente: columna de Ljubica Vodanovic en Gestión. Información referencial; no constituye asesoría legal.",
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
