import numpy as np, sys
from scipy.optimize import milp, LinearConstraint, Bounds
def search(n, K=2, verbose=True, forbid_C_sc=False):
    D=2*n
    pieces=[]
    for pr in (0,1):
      for f in range(2,n):
        for a in range(1,f):
          b=2*f-1-a
          if not (a<b<=2*f-2): continue
          for c in range(f,n):
            for j in range(K):
              for nu in range(0,c-f+1):
                for eps in range(0,n-c+1):
                  pieces.append((pr,f,a,b,c,j,nu,eps))
    P=len(pieces)
    Cl=[(c,j) for c in range(2,n) for j in range(K)]
    # selector binaries: for each C label, min-type (f,eps), max-type (f,eps)
    sel=[]
    for ci,(c,j) in enumerate(Cl):
        for kind in ('min','max'):
            for f in range(2,c+1):
                for eps in range(0,n-c+1):
                    sel.append((ci,kind,f,eps))
    # global min/max binaries per C label
    gsel=[(ci,kind) for ci in range(len(Cl)) for kind in ('gmin','gmax')]
    S=len(sel); G=len(gsel)
    nz=len(Cl)*D
    nv=P+D+nz+D+S+G
    iy=lambda k:P+k; iz=lambda ci,k:P+D+ci*D+k; iw=lambda k:P+D+nz+k
    isel={s:P+D+nz+D+t for t,s in enumerate(sel)}
    igs={s:P+D+nz+D+S+t for t,s in enumerate(gsel)}
    rows=[];lo=[];hi=[]
    def add(r,l,h): rows.append(r);lo.append(l);hi.append(h)
    def prof(pr,k,where,ci=None):
        v=np.zeros(nv)
        for i,(p_,f,a,b,c,j,nu,eps) in enumerate(pieces):
            if p_!=pr: continue
            if where=='C' and (c,j)!=Cl[ci]: continue
            s = nu+eps if where=='M' else nu
            if a+2*s==k: v[i]+=1
            if b+2*s==k: v[i]+=1
        return v
    for pr in (0,1):
        for k in range(D):
            add(prof(pr,k,'M')-prof(pr,D-1-k,'M'),0,0)
            if k<=1: add(prof(pr,k,'M'),0,0)
        for ci,(c,j) in enumerate(Cl):
            for k in range(2*c):
                add(prof(pr,k,'C',ci)-prof(pr,2*c-1-k,'C',ci),0,0)
            if forbid_C_sc:
                add(prof(pr,1,'C',ci),0,0)
    for ci,(c,j) in enumerate(Cl):
        for k in range(D):
            for pr in (0,1):
                r=-prof(pr,k,'C',ci); r[iz(ci,k)]=1; add(r,0,np.inf)
        # selectors: at most one min-type, one max-type
        for kind in ('min','max'):
            r=np.zeros(nv)
            for s in sel:
                if s[0]==ci and s[1]==kind: r[isel[s]]=1
            add(r,0,1)
    B=4.0
    for k in range(D):
        r=-prof(0,k,'M'); r[iw(k)]=1; r[iy(k)]=B; add(r,-np.inf,B)
        r=-prof(1,k,'M'); r[iw(k)]=1; r[iy(k)]=-B; add(r,-np.inf,0)
    # piece constraints
    for i,(pr,f,a,b,c,j,nu,eps) in enumerate(pieces):
        ci=Cl.index((c,j))
        if nu==0:   # in C's min component
            r=np.zeros(nv); r[i]=1; r[isel[(ci,'min',f,eps)]]=-1; add(r,-np.inf,0)
        if nu==c-f: # in C's max component
            r=np.zeros(nv); r[i]=1; r[isel[(ci,'max',f,eps)]]=-1; add(r,-np.inf,0)
        if f<c:     # if C's min is C itself (f=c), no other F
            for eps2 in range(0,n-c+1):
                r=np.zeros(nv); r[i]=1; r[isel[(ci,'min',c,eps2)]]=1; add(r,-np.inf,1)
        mu=nu+eps
        if mu==0:
            r=np.zeros(nv); r[i]=1; r[igs[(ci,'gmin')]]=-1; add(r,-np.inf,0)
        if mu==n-f:
            r=np.zeros(nv); r[i]=1; r[igs[(ci,'gmax')]]=-1; add(r,-np.inf,0)
    for kind in ('gmin','gmax'):
        r=np.zeros(nv)
        for ci in range(len(Cl)): r[igs[(ci,kind)]]=1
        add(r,0,1)
    r=np.zeros(nv); r[:P]=1; add(r,0,1)
    c_obj=np.zeros(nv)
    for k in range(D): c_obj[iw(k)]=-1
    for ci in range(len(Cl)):
        for k in range(D): c_obj[iz(ci,k)]=1
    integ=np.zeros(nv); integ[P:P+D]=1; integ[P+D+nz+D:]=1
    lb=np.zeros(nv); ub=np.full(nv,np.inf); ub[P:P+D]=1; ub[P+D+nz+D:]=1
    res=milp(c_obj,constraints=LinearConstraint(np.array(rows),lo,hi),integrality=integ,bounds=Bounds(lb,ub))
    gain=-res.fun
    if verbose:
        print(f"dim M={D} K={K}: max normalized gain={gain:.6f}  status={res.status}")
        if gain>1e-7:
            for i in np.nonzero(res.x[:P]>1e-7)[0]:
                pr,f,a,b,c,j,nu,eps=pieces[i]
                print(f"   x={res.x[i]:.4f} prime={'pq'[pr]} dimF={2*f} pair=({a},{b}) C=dim{2*c}#{j} nu={nu} eps={eps} mu={nu+eps}")
    return gain
if __name__=="__main__":
    K=int(sys.argv[1])
    for n in map(int,sys.argv[2:]): search(n,K)
