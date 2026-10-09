set_random_seed(7)
R.<x0,x1,x2,x3>=PolynomialRing(QQ)
X=[x0,x1,x2,x3]
a=(0,1,2,3); classes=(0,1,2,4); q=5
pos=[(i,j) for i in range(4) for j in range(i,4)]
char={p:(a[p[0]]+a[p[1]])%q for p in pos}
M=matrix(R,4,4); coef={}
for k,c in enumerate(classes):
    for (i,j) in pos:
        if char[(i,j)]==c:
            co=QQ(ZZ.random_element(1,10)); coef[(i,j)]=(co,k)
            M[i,j]+=co*X[k]
            if i!=j: M[j,i]+=co*X[k]
print("web matrix:"); print(M)
f=M.det()
wts=[(-c)%q for c in classes]; print("weights on x_k:",wts)
# invariance check: f(g x) = chi f(x)
z=CyclotomicField(5).gen()
S5.<y0,y1,y2,y3>=PolynomialRing(CyclotomicField(5))
fg=S5(f)(*[z^wts[k]*S5.gen(k) for k in range(4)])
ratio=[ (fg.monomial_coefficient(m)/S5(f).monomial_coefficient(m)) for m in S5(f).monomials()]
print("f(gx)/f(x) constant:", len(set(ratio))==1, ratio[0])
J=R.ideal([f]+f.gradient())
Js=J.saturation(R.ideal(X))[0]
print("total Tjurina (=deg sing scheme):", Js.hilbert_polynomial(), " reduced points:", Js.radical().hilbert_polynomial())
print("coord points on B:", [f.subs({X[m]:(1 if m==i else 0) for m in range(4)})==0 for i in range(4)],
      " coord points singular:", [all(g.subs({X[m]:(1 if m==i else 0) for m in range(4)})==0 for g in f.gradient()) for i in range(4)])
print("f irreducible:", len(f.factor())==1 and f.factor()[0][1]==1)
# web base points
qs=[ (vector(R,X)*matrix(QQ,4,4,lambda i,j: (coef.get((min(i,j),max(i,j)),(0,-1))[0] if coef.get((min(i,j),max(i,j)),(0,-1))[1]==k else 0))*vector(R,X)) for k in range(4)]
print("web base locus dim (proj):", R.ideal(qs).saturation(R.ideal(X))[0].dimension()-1)
# generic (non-invariant) web Tjurina baseline
Mg=matrix(R,4,4); 
for k in range(4):
    A=random_matrix(ZZ,4,4,x=-5,y=6); A=A+A.transpose(); Mg+=A*X[k]
fgen=Mg.det(); Jg=R.ideal([fgen]+fgen.gradient()).saturation(R.ideal(X))[0]
print("generic web Tjurina:", Jg.hilbert_polynomial())
# invariant quintic G: monomials with weight sum == 0 mod 5
mons=[m for m in (sum(X)^5).monomials() if sum(m.degree(X[k])*wts[k] for k in range(4))%5==0]
print("invariant quintic monomials:", len(mons))
G=sum(QQ(ZZ.random_element(1,20))*m for m in mons)
print("G through coord pts:", [G.subs({X[m]:(1 if m==i else 0) for m in range(4)})==0 for i in range(4)])
IG=R.ideal([G]+G.gradient()).saturation(R.ideal(X))[0]
print("G smooth:", IG.dimension()==0 or IG==R.ideal(1))
# curve G∩B smooth: singular points of complete intersection
Jc=R.ideal([f,G]+ matrix(R,[f.gradient(),G.gradient()]).minors(2)).saturation(R.ideal(X))[0]
print("G∩B smooth curve:", Jc==R.ideal(1) or Jc.dimension()==0)
print("G meets nodes:", (Js.radical()+R.ideal(G)).saturation(R.ideal(X))[0]!=R.ideal(1))
save((M,G,wts),'q10_instance')
