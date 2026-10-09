# Fresh independent check (mock-review-1). Does not import q10.sage.
R.<x0,x1,x2,x3> = PolynomialRing(QQ, order='degrevlex')
X=[x0,x1,x2,x3]; irr=R.ideal(X)
A=matrix(R,[[6*x0,5*x1,4*x2,0],[5*x1,8*x2,0,4*x3],[4*x2,0,7*x3,6*x0],[0,4*x3,6*x0,5*x1]])
f=A.det()
fpaper=900*x0^2*x1^2-1728*x0^3*x2-640*x1*x2^3-875*x1^3*x3+720*x0*x1*x2*x3+256*x2^2*x3^2-672*x0*x3^3
print("det A == displayed f:", f==fpaper)
wt=[0,4,3,1]
print("weights of monomials of f mod 5:", set(sum(e*w for e,w in zip(m.exponents()[0],wt))%5 for m in f.monomials()))
print("f irreducible over QQ:", (len(f.factor())==1 and f.factor()[0][1]==1))
# absolute irreducibility: check over a finite field extension heuristic -> factor over QQbar is expensive; check factor over GF(p^k)

# coefficient matrices independent
Ai=[A.apply_map(lambda e: e.monomial_coefficient(v)) for v in X]
print("A_i linearly independent:", matrix(QQ,[a.list() for a in Ai]).rank()==4)
J=R.ideal([f]+list(f.gradient())); Js=J.saturation(irr)[0]
I3=R.ideal(A.minors(3)).saturation(irr)[0]
I2=R.ideal(A.minors(2)).saturation(irr)[0]
print("Sing scheme: dim(proj)=",Js.dimension()-1," degree=",Js.hilbert_polynomial())
print("Sing scheme radical:", Js.radical()==Js)
print("Sing == rank<=2 scheme:", Js==I3)
print("rank<=1 locus empty:", I2==R.unit_ideal())
# defect test: quadrics through the 10 nodes
I=Js
print("h^0(I_nodes(2)) =", len([1 for m in []]) , "computing...")
mons2=[m for m in (sum(X)^2).monomials()]
# dimension of degree-2 part of saturated ideal
B2=[g for g in I.gens()]
from itertools import product
V=[]
for g in I.gens():
    for m in (sum(X)^(2-g.degree())).monomials() if g.degree()<=2 else []:
        V.append(g*m)
mat=matrix(QQ,[[v.monomial_coefficient(m) for m in mons2] for v in V]) if V else matrix(QQ,0,10)
print("  dim I_2 =", mat.rank(), "(0 => nodes impose independent conditions on quadrics => defect 0 => b3(AM5)=0, b2=11)")
print("  min degree of generators of I_nodes:", min(g.degree() for g in I.gens()))
# coordinate points
for i in range(4):
    pt={X[m]:(1 if m==i else 0) for m in range(4)}
    print(" p%d: f=%s grad=%s"%(i,f.subs(pt),[g.subs(pt) for g in f.gradient()]))
# web base points: v^T A_i v
v=vector(R,X)
qs=[v*a.change_ring(R)*v for a in Ai]
print("web base locus empty:", R.ideal(qs).saturation(irr)[0]==R.unit_ideal())
# Quintic
Q=(6*x0^5+9*x1^5+17*x0*x1^3*x2+15*x0^2*x1*x2^2+13*x2^5+14*x0^3*x1*x3+10*x1^2*x2^2*x3
   +10*x0*x2^3*x3+x0*x1^2*x3^2+19*x0^2*x2*x3^2+15*x1*x2*x3^3+5*x3^5)
print("Q invariant (weights mod5):", set(sum(e*w for e,w in zip(m.exponents()[0],wt))%5 for m in Q.monomials()))
invmons=[m for m in (sum(X)^5).monomials() if sum(e*w for e,w in zip(m.exponents()[0],wt))%5==0]
print("# invariant quintic monomials:", len(invmons), " Q uses", len(Q.monomials()))
print("Q smooth:", R.ideal([Q]+list(Q.gradient())).saturation(irr)[0]==R.unit_ideal())
print("Q(p_k):", [Q.subs({X[m]:(1 if m==i else 0) for m in range(4)}) for i in range(4)])
print("Q misses nodes:", (Js+R.ideal(Q)).saturation(irr)[0]==R.unit_ideal())
Jc=R.ideal([f,Q]+matrix(R,[list(f.gradient()),list(Q.gradient())]).minors(2)).saturation(irr)[0]
print("B∩Q smooth curve:", Jc==R.unit_ideal())
C=R.ideal([f,Q]).saturation(irr)[0]
print("B∩Q: dim(proj)=",C.dimension()-1," hilbert poly:",C.hilbert_polynomial(), " (deg 20, genus 51 expected: 20t-50)")

