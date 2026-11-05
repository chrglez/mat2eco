function Span(el)
	if el.classes:includes("secondary") then
		return {
			pandoc.RawInline("latex", "\\secondary{"),
			el,
			pandoc.RawInline("latex", "}"),
		}
	end
	if el.classes:includes("primary") then
		return {
			pandoc.RawInline("latex", "\\primary{"),
			el,
			pandoc.RawInline("latex", "}"),
		}
	end
end
