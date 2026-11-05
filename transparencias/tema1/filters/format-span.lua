--- format-span.lua
--- Filtro Pandoc para convertir spans y divs con clases Quarto
--- a comandos/entornos LaTeX definidos en los partials del tema.
---
--- === Spans (inline) ===
---
--- Uso en Quarto Markdown:
---   [texto]{.primary}   → \primary{texto}      (negrita maincolor)
---   [texto]{.secondary}  → \secondary{texto}    (negrita airforceblue)
---   [texto]{.ctextbf}   → \ctextbf{texto}      (negrita maincolor)
---   [texto]{.btextbf}   → \btextbf{texto}      (negrita airforceblue)
---   [texto]{.ctextsl}   → \ctextsl{texto}       (cursiva maincolor)
---   [texto]{.btextsl}   → \btextsl{texto}       (cursiva airforceblue)
---   [texto]{.cemph}     → \cemph{texto}          (énfasis maincolor)
---   [texto]{.bemph}     → \bemph{texto}          (énfasis airforceblue)
---   [texto]{.ctexttt}   → \ctexttt{texto}       (monoespaciado maincolor)
---   [texto]{.btexttt}   → \btexttt{texto}       (monoespaciado airforceblue)
---   [texto]{.tbf}       → \tbf{texto}            (monoespaciado [texto] azul)
---   [texto]{.source}    → \vfill{\tiny\color{gray} texto}  (fuente al pie)
---
--- === Divs (bloques) ===
---
--- ::: {.block}              → \begin{block}{}...\end{block}
--- ### Título                   (con título si hay heading)
--- contenido
--- :::
---
--- ::: {.alertblock}         → \begin{alertblock}{}...\end{alertblock}
--- ::: {.exampleblock}       → \begin{exampleblock}{}...\end{exampleblock}

-- Clases que se mapean directamente a comandos LaTeX del mismo nombre
local span_commands = {
  "primary",
  "secondary",
  "ctextbf",
  "btextbf",
  "ctextsl",
  "btextsl",
  "cemph",
  "bemph",
  "ctexttt",
  "btexttt",
  "tbf",
}

function Span(el)
  -- Clase especial: fuente/referencia al pie de la slide
  if el.classes:includes("source") then
    return {
      pandoc.RawInline("latex", "\\vfill{\\tiny\\color{gray} "),
      el,
      pandoc.RawInline("latex", "}"),
    }
  end

  for _, cmd in ipairs(span_commands) do
    if el.classes:includes(cmd) then
      return {
        pandoc.RawInline("latex", "\\" .. cmd .. "{"),
        el,
        pandoc.RawInline("latex", "}"),
      }
    end
  end
end

-- Entornos Beamer block soportados
local block_envs = {
  "block",
  "alertblock",
  "exampleblock",
}

-- Convierte inlines de Pandoc a LaTeX preservando math, spans, etc.
local function inlines_to_latex(inlines)
  local doc = pandoc.Pandoc({pandoc.Para(inlines)})
  local latex = pandoc.write(doc, "latex")
  -- pandoc.write añade \n al final, lo quitamos
  return latex:gsub("\n$", "")
end

function Div(el)
  for _, env in ipairs(block_envs) do
    if el.classes:includes(env) then
      -- Extraer título del primer Header si existe
      local title_latex = ""
      local content = {}
      for _, block in ipairs(el.content) do
        if block.t == "Header" and title_latex == "" then
          title_latex = inlines_to_latex(block.content)
        else
          table.insert(content, block)
        end
      end

      -- Construir el bloque LaTeX
      local result = pandoc.List({})
      result:insert(pandoc.RawBlock("latex", "\\begin{" .. env .. "}{" .. title_latex .. "}"))
      for _, block in ipairs(content) do
        result:insert(block)
      end
      result:insert(pandoc.RawBlock("latex", "\\end{" .. env .. "}"))
      return result
    end
  end
end
