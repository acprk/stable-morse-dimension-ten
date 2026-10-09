import itertools, random
set_random_seed(1)
K=QQ
R.<x0,x1,x2,x3>=PolynomialRing(K)
X=[x0,x1,x2,x3]
def test(a, classes, trials=3):
    q=5
    pos=[(i,j) for i in range(4) for j in range(i,4)]
    char={p:(a[p[0]]+a[p[1]])%q for p in pos}
    res=[]
    for t in range(trials):
        M=matrix(R,4,4)
        for k,c in enumerate(classes):
            for (i,j) in pos:
                if char[(i,j)]==c:
                    co=K(ZZ.random_element(-9,10) or 1)
                    M[i,j]+=co*X[k]; 
                    if i!=j: M[j,i]+=co*X[k]
        f=M.det()
        if f==0: res.append('det0'); continue
        J=R.ideal([f]+f.gradient())
        sing=J.radical() if False else J
        d=sing.dimension()
        if d!=1: res.append(('singdim',d-1)); continue
        deg=R.ideal(f.gradient()+[f]).vector_space_dimension() if False else None
        # count singular points with multiplicity via Hilbert polynomial of saturated ideal
        P=ProjectiveSpace(K,3,names='x0,x1,x2,x3')
        npts=J.saturation(R.ideal(X))[0].hilbert_polynomial()
        # Milnor/Tjurina total; ordinary nodes => tjurina 1 each; also count reduced points
        nred=J.radical().saturation(R.ideal(X))[0].hilbert_polynomial()
        coordpts=[f.subs({X[m]:(1 if m==i else 0) for m in range(4)}) for i in range(4)]
        res.append((npts,nred,[c==0 for c in coordpts], f.factor().__len__()))
    return res
q=5
for a in [(0,1,2,3),(0,1,2,4),(0,1,3,4),(0,2,3,4),(1,2,3,4)]:
    pos=[(i,j) for i in range(4) for j in range(i,4)]
    chars=sorted(set((a[i]+a[j])%5 for (i,j) in pos))
    for classes in itertools.combinations(chars,4):
        # x_k weights must be distinct: classes distinct automatically
        print(a,classes,test(a,classes))
