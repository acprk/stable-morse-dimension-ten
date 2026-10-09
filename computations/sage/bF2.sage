def lattice_cone(t):
    B=matrix(QQ,[[1,0,0],[0,1,0],[0,0,1],[t[0]/5,t[1]/5,t[2]/5]])
    H=(5*B).change_ring(ZZ).hermite_form()[:3]/5
    T=H.inverse()
    return [ (vector(QQ,r)*T).change_ring(ZZ) for r in identity_matrix(3)]
def resolve_count(t):
    F=Fan([Cone(lattice_cone(t))])
    while not F.is_smooth():
        bad=[c for c in F.cones(3) if not c.is_smooth()][0]
        # pick a nonzero lattice point in the half-open fundamental parallelepiped of bad
        R=matrix(ZZ,[list(r) for r in bad.rays()])
        Ri=R.inverse()
        best=None
        for p in Polyhedron(vertices=[vector(ZZ,[0,0,0])]+[sum(S) for k in range(1,4) for S in Combinations(list(bad.rays()),k)]).integral_points():
            p=vector(ZZ,p)
            if p==0: continue
            co=p*Ri
            if all(0<=c<1 for c in co):
                best=p; break
        F=F.subdivide(new_rays=[best])
    return len(F.cones(3)), len(F.rays())-3
tot=0
for t in [(1,1,4)]:
    c,e=resolve_count(t); print("1/5",t,": smooth resolution with",c,"maximal cones,",e,"exceptional divisors")
print("chi(F) =", (24+16)/5 - 4 + 4*c)
