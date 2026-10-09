# Fresh lambda bookkeeping for Theorem A (mock-review-1). Groups: deg -> (rank, {p: d_p})
from collections import defaultdict
def H(d): return {k:(v[0],dict(v[1])) for k,v in d.items()}
def kun(A,B):  # Kunneth; at least one factor free in all our uses -> no Tor terms needed except check
    out=defaultdict(lambda:[0,defaultdict(int)])
    for i,(ra,ta) in A.items():
        for j,(rb,tb) in B.items():
            out[i+j][0]+=ra*rb
            for p,m in ta.items(): out[i+j][1][p]+=m*rb
            for p,m in tb.items(): out[i+j][1][p]+=m*ra
            for p in set(ta)&set(tb): out[i+j][1][p]+=ta[p]*tb[p]; out[i+j+1][1][p]+=ta[p]*tb[p]  # Tor (elementary)
    return {k:(v[0],dict(v[1])) for k,v in out.items()}
def add(*Ls):
    out=defaultdict(lambda:[0,defaultdict(int)])
    for L in Ls:
        for i,(r,t) in L.items():
            out[i][0]+=r
            for p,m in t.items(): out[i][1][p]+=m
    return {k:(v[0],dict(v[1])) for k,v in out.items()}
def sh(L,s): return {i+s:v for i,v in L.items()}
def lam(L): return sum(r for r,t in L.values())+2*sum(max(t.values(),default=0) for r,t in L.values())
def lamN(L,N):
    b=sum(r for r,t in L.values()); cls=defaultdict(lambda:defaultdict(int))
    for i,(r,t) in L.items():
        for p,m in t.items(): cls[i%(2*N)][p]+=m
    return b+2*sum(max(c.values(),default=0) for c in cls.values())
def run(a,beta,t2F=1,t5F=0):
    F={0:(1,{}),2:(a,{2:t2F,**({5:t5F} if t5F else {})}),3:(0,{2:t2F,**({5:t5F} if t5F else {})}),4:(a,{}),6:(1,{})}
    S={0:(1,{}),1:(0,{5:1}),2:(beta,{5:1}),4:(1,{})}
    P1={0:(1,{}),2:(1,{})}; Y={0:(1,{}),2:(6,{}),4:(1,{})}
    M=add(kun(F,Y),sh(kun(S,P1),2),sh(kun(S,P1),2))
    C=add(kun(F,P1),sh(S,2))
    return lam(M),4*lam(C),lamN(M,1)
print("a=19,beta=40:",run(19,40))
for a,b in [(3,5),(19,40),(50,7)]: print(a,b,"gap",run(a,b)[0]-run(a,b)[1])
print("Tor H2(F)=(Z/2)^2:",run(19,40,t2F=2), "gap",run(19,40,2)[0]-run(19,40,2)[1])
print("F with extra Z/5:",run(19,40,1,1),"gap",run(19,40,1,1)[0]-run(19,40,1,1)[1])
