R.<x0,x1,x2,x3>=PolynomialRing(QQ)
X=[x0,x1,x2,x3]
M=matrix(R,[[6*x0,5*x1,4*x2,0],[5*x1,8*x2,0,4*x3],[4*x2,0,7*x3,6*x0],[0,4*x3,6*x0,5*x1]])
f=M.det()
# rank<=2 locus: 3x3 minors
I2=R.ideal(M.minors(3)).saturation(R.ideal(X))[0]
print("rank<=2 locus: dim",I2.dimension()-1,"degree",I2.hilbert_polynomial())
I1=R.ideal(M.minors(2)).saturation(R.ideal(X))[0]
print("rank<=1 members:", I1!=R.ideal(1) and I1.dimension()>0)
# condition (ii): exact over residue fields of the primary components of I2
ok=True
Iaff=I2+R.ideal([x0+2*x1+3*x2+5*x3-1])
allpts=Iaff.variety(QQbar)
if True:
    for pt in allpts:
        Mx=M.change_ring(QQbar).subs({X[i]:pt[X[i]] for i in range(4)}) if False else matrix(QQbar,4,4,lambda i,j: M[i,j](*[pt[v] for v in X]))
        K=Mx.right_kernel().basis()
        assert len(K)==2
        u,v=K
        # web quadrics q_k(y)=y^T A_k y ; A_k = coefficient matrices of x_k
        A=[matrix(QQ,4,4,lambda i,j: M[i,j].monomial_coefficient(X[k])) for k in range(4)]
        rows=[[ (u*A[k]*u), (u*A[k]*v), (v*A[k]*v)] for k in range(4)]
        C=matrix(QQbar,rows).transpose()   # 3x4: conditions for lambda
        r=C.rank()
        if r!=3: ok=False; print("violation at",pt,"rank",r)
print("Beauville (ii) holds:",ok, " (checked", len(allpts),"rank-2 points)")
# base points of web
Q=[vector(R,X)*matrix(QQ,4,4,lambda i,j: M[i,j].monomial_coefficient(X[k]))*vector(R,X) for k in range(4)]
print("web base point free:", R.ideal(Q).saturation(R.ideal(X))[0]==R.ideal(1))
