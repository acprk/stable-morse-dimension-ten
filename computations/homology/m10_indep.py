import importlib.util, sys
spec=importlib.util.spec_from_file_location("ind","indep.py"); 
src=open('indep.py').read().split('S2=biel')[0]   # reuse only the generic helpers
exec(src)
P1={0:1,2:1}; Yf={0:1,2:6,4:1}
def tor_by_parity(H,par):
    from collections import Counter
    c=Counter()
    for i,g in H.items():
        if i%2==par: c+=g[1]
    return d(c)
for a,b2 in [(19,40),(3,9),(10,30)]:   # first: actual ranks b2(F)=19 (b(F)=40), b2(S)=40; others: gap independence
    F={0:grp(1),2:grp(a,[2]),3:grp(0,[2]),4:grp(a),6:grp(1)}
    S={0:grp(1),1:grp(0,[5]),2:grp(b2,[5]),4:grp(1)}
    W=H_kunneth_free(S,P1)
    M=H_add(H_kunneth_free(F,Yf),H_shift(W,2)); M=H_add(M,H_shift(W,2))   # two lines L0,L2
    C0=H_kunneth_free(F,P1)
    C1=H_add(C0,H_shift(S,2))     # each C_j gets exactly one S (lines 0,2 hit E0,E1 and E2,E3)
    lamM=lam(M); fix=4*lam(C1)
    bM=sum(g[0] for g in M.values())
    cyc=bM+2*(tor_by_parity(M,0)+tor_by_parity(M,1))
    print(f"b(F)={2+2*a} b2(S)={b2}: lam(M)={lamM}  #Fix=sum lam(C_j')={fix}  gap={lamM-fix}  cyclic Floer bound={cyc}  ok={fix>=cyc}")
    for i in sorted(M):
        if M[i][1]: print('   M deg',i,dict(M[i][1]))

