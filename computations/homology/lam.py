# torsion profiles: dict prime -> dict degree -> rank ; free: dict degree->rank
from collections import defaultdict
def shift(T,s):
    return {p:{d+s:r for d,r in D.items()} for p,D in T.items()}
def add(*Ts):
    out=defaultdict(lambda: defaultdict(int))
    for T in Ts:
        for p,D in T.items():
            for d,r in D.items(): out[p][d]+=r
    return {p:dict(D) for p,D in out.items()}
def times_free(T,e):  # e: dict degree->rank of torsion-free even factor
    return add(*[ {p:{d:r*k for d,r in D.items()} for p,D in shift(T,s).items()} for s,k in e.items()])
def tau(T):  # sum_i d(Tor H_i)
    degs=set(d for D in T.values() for d in D)
    return sum(max(T[p].get(d,0) for p in T) for d in degs)
def tau_cyc(T,N):  # generator count with grading mod 2N
    cls=defaultdict(lambda: defaultdict(int))
    for p,D in T.items():
        for d,r in D.items(): cls[d%(2*N)][p]+=r
    return sum(max(v.values()) for v in cls.values())
def surf(p,k=1): return {p:{1:k,2:k}}            # surface with (Z/p)^k in H1,H2
def brauer3(p,k=1): return {p:{2:k,3:k}}         # simply conn 3-fold, Tor H2=H3
def blowup_add(T,codim):  # complex codim c: shifts 2,4,..,2(c-1)
    return add(*[shift(T,2*j) for j in range(1,codim)])
CP1={0:1,2:1}; Y={0:1,2:6,4:1}
def gap(TX):
    tC=tau(times_free(TX,CP1)); tM=tau(times_free(TX,Y))
    return 2*(tM-4*tC)   # lambda(M)-4lambda(C); free parts cancel
