# -*- coding: utf-8 -*-
"""Extrae las figuras TikZ/pgfplots de Trans_tema2.qmd y las compila a SVG.

Cada \\begin{tikzpicture}...\\end{tikzpicture} del .qmd se compila suelta con la misma
preambula que el PDF (paquetes de ../tema1/partials/packages.tex y los \\tikzset del
encabezado del .qmd) y se convierte a SVG con pdftocairo (poppler). Genera figuras/figNN.svg y
figuras/indice.json (numero de figura -> texto original, para sustituirlas luego).

Uso:  python3 extraer_figuras.py [--solo N ...] [--salida DIR]
Requiere lualatex y pdftocairo.
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

AQUI = Path(__file__).resolve().parent
TEMA = AQUI.parent
QMD = TEMA / "Trans_tema2.qmd"
PAQUETES = TEMA.parent / "tema1" / "partials" / "packages.tex"


def figuras(texto):
    """[(inicio, fin, codigo)] de cada tikzpicture."""
    return [(m.start(), m.end(), m.group(0)) for m in
            re.finditer(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}", texto, re.S)]


def estilos(texto):
    """Bloque \\tikzset{...} del encabezado YAML del qmd."""
    cab = texto.split("\n---\n", 1)[0]
    m = re.search(r"\\tikzset\{.*?\n          \}", cab, re.S)
    return re.sub(r"^          ", "", m.group(0), flags=re.M) if m else ""


def documento(codigo, tikzset):
    return "\n".join([
        r"\documentclass[border=4pt]{standalone}",
        r"\usepackage{fontspec}\usepackage{unicode-math}",
        r"\input{" + PAQUETES.as_posix() + "}",
        r"\definecolor{maincolor}{RGB}{23, 44, 73}",
        tikzset,
        r"\begin{document}", codigo, r"\end{document}", ""])


def compilar(n, codigo, tikzset, salida, mantener_log):
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        (td / "f.tex").write_text(documento(codigo, tikzset), encoding="utf-8")
        r = subprocess.run(["lualatex", "-interaction=nonstopmode", "-halt-on-error",
                            "-shell-escape", "f.tex"], cwd=td, capture_output=True,
                           text=True, timeout=180)
        if r.returncode != 0 or not (td / "f.pdf").exists():
            if mantener_log:
                (salida / f"fig{n:02d}.log").write_text(r.stdout[-3000:], encoding="utf-8")
            return False
        d = subprocess.run(["pdftocairo", "-svg", "f.pdf", str(salida / f"fig{n:02d}.svg")],
                           cwd=td, capture_output=True, text=True, timeout=120)
        return d.returncode == 0 and (salida / f"fig{n:02d}.svg").exists()


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--solo", type=int, nargs="*", help="numeros de figura (desde 1)")
    ap.add_argument("--salida", type=Path, default=AQUI / "figuras")
    ap.add_argument("--logs", action="store_true", help="guarda el log de las que fallan")
    a = ap.parse_args()
    a.salida = a.salida.resolve()
    for exe in ("lualatex", "pdftocairo"):
        if not shutil.which(exe):
            sys.exit(f"Falta {exe} en el PATH.")
    texto = QMD.read_text(encoding="utf-8")
    figs, tikzset = figuras(texto), estilos(texto)
    a.salida.mkdir(parents=True, exist_ok=True)
    print(f"{len(figs)} figuras; tikzset: {'si' if tikzset else 'NO'}")
    ok, mal = [], []
    for n, (_, _, cod) in enumerate(figs, 1):
        if a.solo and n not in a.solo:
            continue
        bien = compilar(n, cod, tikzset, a.salida, a.logs)
        (ok if bien else mal).append(n)
        print(f"  fig{n:02d}  {'OK' if bien else 'FALLA'}", flush=True)
    (a.salida / "indice.json").write_text(
        json.dumps({f"{n:02d}": cod for n, (_, _, cod) in enumerate(figs, 1)},
                   ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\n{len(ok)} compiladas, {len(mal)} con error: {mal}")
    sys.exit(1 if mal else 0)


if __name__ == "__main__":
    main()
