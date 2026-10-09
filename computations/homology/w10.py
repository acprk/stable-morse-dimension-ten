# M = Bl_{ union of S_i x L_i }(F x Y), L_i = proper transforms of the 4 coordinate lines (cycle E1-L1-E2-L2-E3-L3-E4-L4-E1)
from lam import *
import itertools
Ft={2:{2:1,3:1}}            # F: Tor H2=H3=Z/2
St=surf(5)                  # S: Z/5 in H1,H2
SP1=times_free(St,CP1)
def run(lines, qk=1):
    St_=surf(5,qk); SP1_=times_free(St_,CP1)
    MT=times_free(Ft,Y)
    for L in lines: MT=add(MT,shift(SP1_,2))            # codim-2 center S x P1 -> shift 2
    Cs=[times_free(Ft,CP1) for _ in range(4)]
    for L in lines:
        for e in (L, (L+1)%4):                          # line L joins E_L and E_{L+1}
            Cs[e]=add(Cs[e],shift(St_,2))               # S x pt codim 2 in C -> shift 2
    return 2*(tau(MT)-sum(tau(C) for C in Cs))
for r in range(0,5):
    for lines in itertools.combinations(range(4),r):
        for qk in (1,2):
            print(lines,'S torsion rank',qk,'gap(torsion part)=',run(lines,qk))
