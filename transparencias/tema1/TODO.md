# TODO - Tema 1: Funciones reales de varias variables

## Tareas Pendientes
- [x] **Página final con fondo burdeos**: Resuelto usando TikZ overlay (`\fill[maincolor]` sobre `current page`) en lugar de `\setbeamercolor{background canvas}`, que no funciona en frames sueltos del documento por cómo Beamer procesa los backgrounds fuera de sus hooks nativos (`\AtBeginSection`, etc.).

## Completadas
- [x] **Página final**: Implementada con fondo burdeos y formato limpio
  - Slide final con `## {.plain}` y TikZ overlay para fondo `maincolor`
  - Título centrado con `\LARGE\bfseries` en blanco
  - Iconos CC en línea horizontal
- [x] Optimizar figuras TikZ con estilos globales
- [x] Añadir FontAwesome para iconos externos
- [x] Reorganizar figuras de bolas (R^1, R^2, R^3)
- [x] Añadir caption a figura de coordenadas polares
- [x] Añadir caption a figura de límites iterativos
