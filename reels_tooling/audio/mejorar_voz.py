#!/usr/bin/env python3
"""Mejora de voz para reels de Víctor Ventura (receta igualada al audio de referencia de CapCut).

Uso: python3 mejorar_voz.py entrada.m4a salida.m4a [LUFS]
- Quita ruido de fondo, cierra las pausas con compuerta, copia la ecualización de la referencia
  (menos cuerpo en 350-500 Hz, más presencia en 900-1400 Hz y brillo sobre 4 kHz), comprime fuerte
  y normaliza (con -1 dB de ajuste final, porque la normalización queda ~1 dB alta) al estándar de los reels (-16 LUFS por defecto, pico máximo -1.5 dBFS).
Requiere ffmpeg. La ecualización es la que se midió en la prueba del 16-11-2026 (intensidad 80 %).
"""
import subprocess, sys

EQ = {100: 1.3, 112: 1.1, 125: 1.3, 141: 1.8, 158: 3.5, 178: 5.5, 200: 5.2, 224: 3.3, 251: 1.5, 282: -0.3,
      317: -2.2, 356: -3.4, 400: -4.3, 448: -4.8, 503: -3.6, 565: -1.3, 634: 0.6, 712: 1.8, 800: 2.8,
      897: 3.4, 1007: 3.6, 1131: 3.5, 1269: 3.4, 1425: 3.1, 1600: 1.9, 1795: 0.1, 2015: -1.2, 2262: -1.4,
      2539: -0.8, 2850: -0.5, 3200: -0.3, 3591: 1.0, 4031: 2.6, 4525: 3.1, 5079: 3.3, 5701: 3.3, 6400: 2.7,
      7183: 2.2, 8063: 2.4, 9050: 4.3, 10159: 6.9}


def cadena(lufs=-16.0, tp=-1.5, intensidad=0.8):
    ent = ";".join(f"entry({f},{g * intensidad:.2f})" for f, g in EQ.items())
    return (f"highpass=f=90,afftdn=nr=30:nf=-45:tn=1,"
            f"agate=threshold=0.01:ratio=6:attack=3:release=150:range=0.005,"
            f"firequalizer=gain_entry='{ent}':scale=linlog,"
            f"acompressor=threshold=-30dB:ratio=6:attack=5:release=120:makeup=4,"
            f"acompressor=threshold=-18dB:ratio=3:attack=3:release=80,"
            f"loudnorm=I={lufs}:TP={tp}:LRA=3:linear=false,"
            f"alimiter=limit=0.95:attack=2:release=40")


if __name__ == "__main__":
    entrada, salida = sys.argv[1], sys.argv[2]
    lufs = float(sys.argv[3]) if len(sys.argv) > 3 else -16.0
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", entrada, "-ac", "1", "-ar", "48000",
                    "-af", cadena(lufs) + ",volume=-1dB", "-c:a", "aac", "-b:a", "192k", salida], check=True)
    print("listo:", salida)
