set table "3dplot.surf.table"; set format "%.5f"
set format "%.7e";;set parametric; splot[-5:5][-5:5] v,1/v*cos(u),1/v*sin(u)
