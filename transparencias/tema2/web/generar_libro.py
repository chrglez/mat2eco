# -*- coding: utf-8 -*-
"""Genera capitulos/tema2.qmd (capitulo del libro) a partir de Trans_tema2.qmd.

BORRADOR DE PARTIDA: vuelca definiciones, formulas y figuras de las diapositivas como
secciones de un capitulo. La explicacion (el texto que hace de esto un libro) se escribe
a mano; cuando se empiece a editar capitulos/tema2.qmd hay que dejar de regenerarlo.

Uso:  python3 generar_libro.py            (no sobrescribe si el capitulo ya es una edicion)
      python3 generar_libro.py --forzar
"""
import argparse
import re
import sys
from pathlib import Path

from generar_web import ORIGEN, convertir

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[2]
DESTINO = RAIZ / "capitulos" / "tema2.qmd"
MARCA = "<!-- BORRADOR GENERADO: generar_libro.py -->"

CABECERA = f"""---
title: "Cálculo de funciones de varias variables"
---

{MARCA}

::: {{.callout-note appearance="simple" icon=false}}
**Borrador.** Este capítulo se ha generado a partir de las transparencias del tema 2:
conserva definiciones, fórmulas y figuras, pero aún falta el texto explicativo.
Mientras tanto, la [presentación](../transparencias/tema2/web/tema2.html) y el
[PDF](../transparencias/tema2/Trans_tema2.pdf) están disponibles.
:::

"""


def bajar_niveles(texto):
    """# -> ##, ## -> ### (fuera de bloques de codigo)."""
    fuera, salida = True, []
    for l in texto.splitlines():
        if l.startswith("```"):
            fuera = not fuera
        if fuera and re.match(r"^#{1,5} ", l):
            l = "#" + l
        salida.append(l)
    return "\n".join(salida) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--forzar", action="store_true")
    a = ap.parse_args()
    if DESTINO.exists() and MARCA not in DESTINO.read_text(encoding="utf-8") and not a.forzar:
        sys.exit(f"{DESTINO} ya no es un borrador generado (se ha editado). "
                 "Usa --forzar si de verdad quieres sobrescribirlo.")
    cuerpo = ORIGEN.read_text(encoding="utf-8").split("\n---\n", 1)[1]
    cuerpo, n = convertir(cuerpo, ruta_figuras="../transparencias/tema2/web/figuras",
                          raiz_img="../transparencias/tema2/")
    cuerpo = re.sub(r"^<!--\s*Referencia:.*?-->\s*\n", "", cuerpo, flags=re.M)
    DESTINO.parent.mkdir(exist_ok=True)
    DESTINO.write_text(CABECERA + bajar_niveles(cuerpo), encoding="utf-8")
    print(f"{DESTINO.relative_to(RAIZ)}: {n} figuras.")


if __name__ == "__main__":
    main()
