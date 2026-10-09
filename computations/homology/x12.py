from lam import *
from fractions import Fraction as Fr
def conv(a,b):
    out={}
    for i,x in a.items():
        for j,y in b.items(): out[i+j]=out.get(i+j,0)+x*y
    return out
def blow_free(F,c): return conv(F,{2*j:1 for j in range(1,c)})
# surfaces: (free poly, torsion)
S2=({0:1,1:2,2:2,3:2,4:1}, surf(2,2))     # bielliptic (Z/2)^2
S3=({0:1,1:2,2:2,3:2,4:1}, surf(3,1))     # bielliptic Z/3
EN=({0:1,2:10,4:1}, surf(2,1))            # Enriques
P1xP5={k:(2 if 0<k<12 and k%2==0 else 1) for k in range(0,13,2)}
P1xP5={0:1,2:2,4:2,6:2,8:2,10:2,12:1}
def X12(sa,ka,sb,kb):  # ka copies of surface sa (codim4), kb copies of sb x P1 (codim3)
    Fa,Ta=sa; Fb,Tb=sb
    Fb1=conv(Fb,CP1); Tb1=times_free(Tb,CP1)
    free=dict(P1xP5)
    for k,v in blow_free(Fa,4).items(): free[k]=free.get(k,0)+ka*v
    for k,v in blow_free(Fb1,3).items(): free[k]=free.get(k,0)+kb*v
    T=add(*([blowup_add(Ta,4)]*ka+[blowup_add(Tb1,3)]*kb))
    return free,T
def report(name,free,T):
    b=sum(free.values())
    lamC=2*b+2*tau(times_free(T,CP1)); lamM=8*b+2*tau(times_free(T,Y))
    fix=4*lamC
    # integral cyclic Floer bound for M (N=1) and field bounds
    cyc=8*b+2*tau_cyc(times_free(T,Y),1)
    TM=times_free(T,Y)
    fld={p:8*b+2*sum(D.values()) for p,D in TM.items()}
    print(f"{name}: dimX=12 b(X)={b} SM(M)=lam(M)={lamM} #Fix={fix} gap={lamM-fix} delta={Fr(lamM-fix,lamM)} cycFloer={cyc} fields={fld}")
for (na,sa),(nb,sb) in [(('S2',S2),('S3',S3)),(('S3',S3),('S2',S2)),(('EN',EN),('S3',S3)),(('S3',S3),('EN',EN))]:
    for ka in range(1,7):
        for kb in range(1,7):
            f,T=X12(sa,ka,sb,kb)
            b=sum(f.values())
            g=2*tau(times_free(T,Y))-8*tau(times_free(T,CP1))
            if g>0: report(f"{na}x{ka} + ({nb}xP1)x{kb}",f,T)
