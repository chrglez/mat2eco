# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a **teaching materials repository** for "Matemáticas para la Economía II" (Mathematics for Economics II), a course in the Economics degree program at Universidad de Las Palmas de Gran Canaria (ULPGC). The repository contains LaTeX documents for course materials organized by topics (Temas), including lecture slides (Transparencias), exercises (Ejercicios), practice sessions (Prácticas), and exams (examenes_pruebas).

## Repository Structure

The repository is organized by **functionality** (not by topics):

```
mat2eco/
├── transparencias/      # Lecture slides (PUBLIC on GitHub)
│   ├── tema0/
│   ├── tema1/          # R Markdown (xaringan) slides
│   ├── tema2/
│   ├── tema3/
│   └── tema4/
├── ejercicios/         # Exercise sheets (PRIVATE - .gitignore)
│   ├── tema0/
│   ├── tema1/
│   ├── tema2/
│   ├── tema3/
│   └── tema4/
├── practicas/          # Practice sessions (PRIVATE - .gitignore)
│   ├── tema0/
│   ├── tema1/
│   ├── tema2/
│   ├── tema3/
│   └── tema4/
├── pruebas_examenes/   # Exams and tests (PRIVATE - .gitignore)
├── old/                # Archived old materials (PRIVATE - .gitignore)
└── images/             # Shared images (logo.png, ulpgc.png)
```

**Privacy Note**: Only `transparencias/` and `images/` are public on GitHub. All other folders are excluded via `.gitignore`.

## LaTeX Build System

### Compilation Commands

Most LaTeX documents require **LuaLaTeX** compilation:

```bash
# For standard documents (prácticas, ejercicios)
lualatex filename.tex

# Using latexmk (recommended, handles multiple passes automatically)
latexmk -lualatex filename.tex

# For exams with latexmk configuration
cd pruebas_examenes
latexmk filename.tex  # Uses .latexmkrc configuration
```

### LaTeX Configuration Notes

- **Engine**: Documents use LuaLaTeX (`% !TeX program = lualatex`)
- **Font System**: Uses `fontspec` and `unicode-math` packages
  - Prácticas: Latin Modern Roman/Math
  - Exámenes: Libertinus Serif/Math
- **Language**: Spanish with babel (`es-tabla`, `es-nodecimaldot`)
- **Exam Class**: Tests use the `exam` document class with grading tables
- **Shared Resources**:
  - Images in root `images/` folder (logo.png, ulpgc.png)
  - May reference `../images/` from subdirectories
- **Academic Year**: Automatic calculation based on current month (September cutoff)

### latexmk Configuration

The `pruebas_examenes/.latexmkrc` file configures:
```perl
$pdf_mode = 4;                    # Use lualatex
$interaction = 'nonstopmode';     # Don't stop on errors
$synctex = 1;                     # Enable SyncTeX
```

## R Markdown Slides (tema1)

Tema1 uses **xaringan** (R Markdown) for HTML slides:

```bash
# In transparencias/tema1/
# Open Trans_tema1.Rmd in RStudio and knit, or use R:
Rscript -e "rmarkdown::render('Trans_tema1.Rmd')"
```

- **Output**: HTML slides with custom CSS (`css/custom.css`)
- **Dependencies**: `xaringan`, `fontawesome` packages
- **Configuration**: 16:9 ratio, GitHub highlighting style
- **.gitignore**: Excludes R project files (.Rproj.user, .RData, etc.)

## Document Types

### 1. Prácticas (Practice Sessions)
- Format: A4, 11pt article class
- Naming: `practica_temaN_sesionX.tex`
- Header: Course name, academic year
- Packages: enumitem, graphicx, amsmath/amssymb

### 2. Ejercicios (Exercises)
- Format: A4, 10pt report class
- Often includes test questions (tipo test)
- Uses multicol for columned layouts
- Title page with university logos

### 3. Exámenes (Exams)
- Format: A4, 10pt exam class
- Naming: `YYMMDD_description_grupoXX.tex`
- Features: Point tracking, grading tables, answer toggles
- Commands: `\printanswers` / `\noprintanswers`
- Time limit and metadata in header

## Common Patterns

### Standard Header Block
```latex
% !TeX program = lualatex
\documentclass[options]{class}
\usepackage{fontspec}
\usepackage{unicode-math}
\usepackage[spanish,es-tabla,es-nodecimaldot]{babel}
```

### Academic Year Calculation
```latex
\newcommand{\academicYear}{%
    \ifnum\month>7
        \the\numexpr\year-2000\relax/\the\numexpr\year+1-2000\relax
    \else
        \the\numexpr\year-1-2000\relax/\the\numexpr\year-2000\relax
    \fi
}
```

### Image References
Always use relative paths from document location:
- From root: `images/logo.png`
- From functionality folders (transparencias/tema1/, ejercicios/tema2/, etc.): `../../images/logo.png`

## File Management

### LaTeX Auxiliary Files
Generated files (not tracked in git):
- `.aux`, `.log`, `.fls`, `.fdb_latexmk`
- `.synctex.gz`
- `.out`, `.toc`

### What to Commit (Public Repository)
- **transparencias/**: All source files (`.tex`, `.Rmd`) and PDFs
- **images/**: Shared assets (logo.png, ulpgc.png)
- Configuration files: `.gitignore`, `CLAUDE.md`
- CSS, custom headers, and other assets for slides

### What NOT to Commit (via .gitignore)
- **ejercicios/**: Exercise materials (private)
- **practicas/**: Practice session materials (private)
- **pruebas_examenes/**: Exams and tests (private)
- **old/**: Archived materials (private)
- LaTeX auxiliary files (`.aux`, `.log`, `.fls`, `.fdb_latexmk`, `.synctex.gz`)
- R temporary files (`.Rhistory`, `.RData`, `.Rproj.user`)
- System files (`.DS_Store`, `Thumbs.db`)

## Course Context

**Course**: Matemáticas para la Economía II (40706)
**Degree**: Grado en Economía, ULPGC
**Instructor**: Christian González (chrglez)
**Topics Covered**:
- Tema 1: Functions of several real variables (domains, level curves, limits, continuity)
- Tema 2: Calculus of functions of several variables
- Additional topics in Tema 3-4

When creating new materials, maintain consistency with existing document structure, fonts, and naming conventions.
