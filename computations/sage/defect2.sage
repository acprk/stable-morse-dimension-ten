R.<x0,x1,x2,x3>=PolynomialRing(QQ, order='degrevlex')
X=[x0,x1,x2,x3]
M=matrix(R,[[6*x0,5*x1,4*x2,0],[5*x1,8*x2,0,4*x3],[4*x2,0,7*x3,6*x0],[0,4*x3,6*x0,5*x1]])
I2=R.ideal(M.minors(3)).saturation(R.ideal(X))[0]
print("radical == itself:", I2.radical()==I2, " degree:", I2.hilbert_polynomial())
hf=I2.hilbert_series()
S=PowerSeriesRing(QQ,'t',default_prec=6)
print("Hilbert function of R/I_Sigma in degrees 0..4:", list(S(hf))[:5])
h2=10-list(S(hf))[2]
print("h0(I_Sigma(2)) =",h2," => quadrics impose",10-h2,"conditions on the 10 nodes => defect =",10-(10-h2))
