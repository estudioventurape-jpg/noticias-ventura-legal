# Estilo explicativo animado (flujo por defecto de los reels)

Capa animada de Remotion (etiqueta superior, íconos, sellos, diagramas, paneles con marcas, subtítulos con palabra clave)
que se superpone sobre las imágenes de Higgsfield con Ken Burns. No consume créditos de Higgsfield: se renderiza con Remotion y ffmpeg.

Pasos:
1. Voz sin silencios + `guion.txt` + alineación (`scripts/alinear_subtitulos.py`, de la skill crea-un-reel) para obtener `props.json` con los tiempos de cada frase.
2. Copiar `Explainer.tsx`, `Icons.tsx` y `Root.tsx` a `remotion/src/` (junto a Overlay, Subtitle y TextCard de la skill).
3. Definir las escenas en `Explainer.tsx`: cada elemento entra con `<Pop at={segundos}>` o `<Stamp at={segundos}>` en el segundo en que se dice su frase (los tiempos incluyen el offset de 0.4 s de la miniatura).
4. Render con fondo transparente: `props.transparent = true` y `npx remotion render src/index.ts Explainer seqtr --props=props.json --sequence --image-format=png --concurrency=2`.
5. Componer sobre `bg_reel.mp4` (Ken Burns, oscurecido con `eq=brightness=-0.2:saturation=0.9`) con `overlay=0:0:eof_action=pass`, miniatura de 0.4 s al inicio, voz, música y acentos.

Referencia: reel «cargo de confianza» (14-11-2026). Las escenas del ejemplo son específicas de ese guion y se rehacen por reel.
