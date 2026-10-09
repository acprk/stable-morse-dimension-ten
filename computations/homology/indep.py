# Independent check: represent H_i(.;Z) as (rank, Counter of prime-power cyclic orders); Kunneth with torsion-free factor;
# then lambda = sum rank + 2*sum_i d(Tor H_i), d computed by grouping cyclic factors by prime.
from collections import Counter
def grp(rank=0,cyc=()): return [rank,Counter(cyc)]
def gadd(a,b): return [a[0]+b[0],a[1]+b[1]]
def gscale(a,k): return [a[0]*k,Counter({c:n*k for c,n in a[1].items()})]
def H_add(A,B):
    out={}
    for H in (A,B):
        for i,g in H.items(): out[i]=gadd(out.get(i,grp()),g)
    return out
def H_kunneth_free(A,F): # F torsion-free: dict deg->rank
    out={}
    for i,g in A.items():
        for j,r in F.items(): out[i+j]=gadd(out.get(i+j,grp()),gscale(g,r))
    return out
def H_shift(A,s): return {i+s:g for i,g in A.items()}
def d(c):
    byp=Counter()
    for order,n in c.items(): byp[min(p for p in range(2,order+1) if order%p==0)]+=n
    return max(byp.values(),default=0)
def lam(H): return sum(g[0] for g in H.values())+2*sum(d(g[1]) for g in H.values())
def blowup(A,Z,c):
    out=dict(A)
    for j in range(1,c): out=H_add(out,H_shift(Z,2*j))
    return out
biel=lambda T: {0:grp(1),1:grp(2,T),2:grp(2,T),3:grp(2),4:grp(1)}
S2=biel([2,2]); S3=biel([3])
P1={0:1,2:1}; Yf={0:1,2:6,4:1}
amb={0:grp(1),2:grp(2),4:grp(2),6:grp(2),8:grp(2),10:grp(2),12:grp(1)}
X=amb
for _ in range(3): X=blowup(X,S3,4)          # S3 x{t}, codim 4 in P1xP5
X=blowup(X,H_kunneth_free(S2,P1),3)         # S2 x P1, codim 3
C=H_kunneth_free(X,P1); M=H_kunneth_free(X,Yf)
print("lam(C)=",lam(C)," 4lam(C)=",4*lam(C)," lam(M)=",lam(M))
for i in sorted(M): print(i,M[i][0],dict(M[i][1]))

print("---- X8 = Bl_{2 S3}(AM x P1), M12 ----")
AM={0:grp(1),2:grp(11,[2]),3:grp(0,[2]),4:grp(11),6:grp(1)}   # b3=0, Tor H2=Tor H3=Z/2
A8=H_kunneth_free(AM,P1)
X=A8
for _ in range(2): X=blowup(X,S3,2)
C=H_kunneth_free(X,P1); M=H_kunneth_free(X,Yf)
print("lam(M)=",lam(M),"#Fix=4lam(C)=",4*lam(C))
print("---- X10 = Bl_{S3, 2 V5}(T4 x P1), M14 ; T4 free with betti t (param) ----")
V5={0:grp(1),1:grp(0,[5]),2:grp(1),3:grp(44),4:grp(1,[5]),6:grp(1)}
for name,T4 in [("T4 generic b",{0:grp(1),2:grp(1),4:grp(1),6:grp(1),8:grp(1)})]:
    A=H_kunneth_free({0:grp(1)},{0:1}); A={i:g for i,g in T4.items()}; A=H_kunneth_free(A,P1)
    X=blowup(A,S3,3)
    for _ in range(2): X=blowup(X,V5,2)
    C=H_kunneth_free(X,P1); M=H_kunneth_free(X,Yf)
    bA=sum(g[0] for g in A.values())
    print("with b(ambient)=",bA,": lam(M)=",lam(M),"#Fix=",4*lam(C),"gap=",lam(M)-4*lam(C), "(gap independent of ambient free part; lam(M) grows 8 per ambient Betti)")
