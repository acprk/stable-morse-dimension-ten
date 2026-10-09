"""Necessity checks in real dimension 10 (Appendix A of the paper).
Re-solves the MILP of lpsearch2.py with families of fixed-point pieces removed;
a maximal normalized gain of 0 means the removed ingredient is necessary."""
src = open('lpsearch2.py').read()
src = src.replace("                  pieces.append((pr,f,a,b,c,j,nu,eps))",
                  "                  if FILT((pr,f,a,b,c,j,nu,eps)): pieces.append((pr,f,a,b,c,j,nu,eps))")
src = src.replace('if __name__=="__main__":', 'if False:')
# piece = (prime, f=dimF/2, a, b, c=dimC/2, label, nu, eps)
FILTERS = [
    ("no 6-dim fixed components",            lambda t: t[1] != 3),
    ("no Brauer-type (2,3) 6-dim components", lambda t: not (t[1] == 3 and t[2] == 2)),
    ("no torsion surfaces",                   lambda t: t[1] != 2),
    ("no 8-dim fixed components C",           lambda t: t[4] < 4),
    ("surfaces not inside an 8-dim C",        lambda t: not (t[1] == 2 and t[4] == 4)),
    ("surfaces only as their own component",  lambda t: not (t[1] == 2 and t[4] > 2)),
    ("8-dim C contains only 6-dim F",         lambda t: not (t[4] == 4 and t[1] != 3)),
]
for name, filt in FILTERS:
    ns = {'FILT': filt}
    exec(src, ns)
    print(name, ":", end=" ")
    ns['search'](5, 3, forbid_C_sc=True)
