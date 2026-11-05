# -*- coding: utf-8 -*-
"""Genera web/tema2.qmd (Reveal.js) a partir de Trans_tema2.qmd (Beamer).

El contenido se mantiene en un solo sitio, Trans_tema2.qmd. Este script:
  - cambia el encabezado YAML por el de Reveal.js;
  - sustituye cada tikzpicture por figuras/figNN.svg (ver extraer_figuras.py);
  - traduce los restos de LaTeX que Reveal no entiende (\\includegraphics, \\bhref,
    \\textcolor, \\begin{center}...).
No edites web/tema2.qmd a mano: se sobrescribe. Uso:  python3 generar_web.py
"""
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ORIGEN = AQUI.parent / "Trans_tema2.qmd"
DESTINO = AQUI / "tema2.qmd"
RAIZ_IMG = "../"            # img-png/... vive en tema2/, un nivel por encima de web/

CABECERA = """---
title: "Matemáticas para la Economía II"
subtitle: "Tema 2: Cálculo de funciones de varias variables"
author: "Christian González"
institute: "Universidad de Las Palmas de Gran Canaria · Curso 25/26"
lang: es
format:
  revealjs:
    theme: [simple, tema2.scss]
    width: 1600
    height: 900
    margin: 0.04
    slide-number: c/t
    hash: true
    controls: true
    progress: true
    transition: none
    math: mathjax
    pdf-separate-fragments: false
    embed-resources: true
    footer: "Matemáticas para la Economía II · ULPGC"
---
"""


def convertir(cuerpo, ruta_figuras="figuras", raiz_img="../"):
    """Cuerpo del .qmd Beamer -> markdown sin LaTeX de Beamer. Devuelve (texto, n_figuras)."""
    n = 0

    def figura(_):
        nonlocal n
        n += 1
        return f"![]({ruta_figuras}/fig{n:02d}.svg){{.figura}}"


    # 1. figuras TikZ/pgfplots -> SVG (mismo orden que extraer_figuras.py)
    cuerpo = re.sub(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}", figura, cuerpo, flags=re.S)
    # los contenedores {#fig-...} piden pie de figura: pasan a div normal
    cuerpo = re.sub(r"^(:::+) *\{#fig-[\w-]+\}", r"\1 {.contenedor}", cuerpo, flags=re.M)
    # 2. restos de LaTeX
    cuerpo = re.sub(r"^\\(?:begin|end)\{center\}\s*\n", "", cuerpo, flags=re.M)
    cuerpo = re.sub(r"\\includegraphics\[width=([\d.]*)\\textwidth\]\{([^}]+)\}",
                    lambda m: f"![]({raiz_img}{m.group(2)})"
                              f"{{width={int(float(m.group(1) or 1) * 100)}%}}", cuerpo)
    cuerpo = re.sub(r"\\bhref\{([^}]+)\}\{([^}]+)\}\s*\[\\faExternalLink\*\]\{\}",
                    lambda m: f"[{m.group(2)}]({m.group(1).replace(chr(92) + '%', '%')})",
                    cuerpo)
    cuerpo = re.sub(r"\\textcolor\{(\w+)\}\{([^}]*)\}",
                    r'<span style="color:\1">\2</span>', cuerpo)
    cuerpo = re.sub(r"^\\small ", "", cuerpo, flags=re.M)
    cuerpo = re.sub(r"\\textbf\{([^}]*)\}", r"**\1**", cuerpo)
    return cuerpo, n


def main():
    t = ORIGEN.read_text(encoding="utf-8")
    cuerpo = t.split("\n---\n", 1)[1]
    cuerpo, n = convertir(cuerpo)
    # 3. avisos de lo que queda
    resto = re.findall(r"^\s*\\(?:begin|end|small|tiny|vspace|centering|footnotesize)\b[^\n]*",
                       re.sub(r"\$\$.*?\$\$", "", cuerpo, flags=re.S), flags=re.M)
    DESTINO.write_text(CABECERA + cuerpo, encoding="utf-8")
    print(f"{DESTINO.name}: {n} figuras sustituidas.")
    if resto:
        print("Quedan lineas de LaTeX sin traducir:")
        for r in resto[:15]:
            print("  ", r.strip()[:90])


if __name__ == "__main__":
    main()
