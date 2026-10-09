# basis of N = Z^3 + Z(1,1,4)/5, express in coordinates *5
Nb=matrix(ZZ,[[5,0,0],[0,5,0],[0,0,5],[1,1,4]]).echelon_form()[:3]   # rows: basis of 5N
Bm=Nb.transpose()
def coords(v): return Bm.solve_right(vector(QQ,v))
rays=[(5,0,0),(0,5,0),(0,0,5)]
new=[(1,1,4),(2,2,3),(3,3,2),(4,4,1)]
F=Fan([Cone([coords(r) for r in rays])])
for v in new:
    F=F.subdivide(new_rays=[coords(v)])
print("rays",F.nrays()," max cones",len(F.cones(3))," smooth:",F.is_smooth(), " interior rays:",4)
print("b2 of resolution (#rays-3) =",F.nrays()-3, " chi = #max cones =",len(F.cones(3)))
