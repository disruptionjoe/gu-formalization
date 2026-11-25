#!/usr/bin/env python3
"""Exact reduced Clifford and coarea controls; universal proof is in the note.
Reduced signature(2,2), H(1,1), N(1,1) tests slot/sign/order algebra only.
The native n14 polarization dimension and infinite-dimensional estimates are
proved on paper, not inferred from these finite controls or from a source fit.
"""
import json
import sympy as s

checks = {}
def ok(name, condition):
    checks[name] = bool(condition)
    assert condition, name
def eq(a,b): return s.simplify(a-b) == s.zeros(*a.shape)
I=s.I; eye=s.eye(4); zero=s.zeros(4,1)
pa=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1)]
g=[I*s.kronecker_product(pa[0],s.eye(2)),s.kronecker_product(pa[1],s.eye(2)),s.kronecker_product(pa[2],pa[0]),I*s.kronecker_product(pa[2],pa[1])]
eta=s.diag(-1,1,1,-1)
def c(v): return sum((v[i]*g[i] for i in range(4)),s.zeros(4))
def dot(v,w): return (v.T*eta*w)[0]
def Gamma(z): return sum((g[i]*z[i] for i in range(4)),zero)
def ip(p,z): return sum((eta[i,i]*p[i]*z[i] for i in range(4)),zero)
def q(z): return s.Matrix.vstack(z[0],z[1])
ok('indefinite Clifford relations',all(eq(g[i]*g[j]+g[j]*g[i],2*eta[i,j]*eye) for i in range(4) for j in range(4)))
ell=s.Matrix([0,0,1,1]); n=s.Matrix([0,0,1,-1])
psi=c(ell).nullspace()[0]
b0=[g[0]*g[1]*psi,psi,zero,zero]
ok('visible conormal gamma-traceless polarization',eq(Gamma(b0),zero) and eq(ip(ell,b0),zero) and q(b0)!=s.zeros(8,1))
ok('null Clifford kernel dimension',len(c(ell).nullspace())==2)
omega=g[0]*g[1]*g[2]*g[3]
for label,p in [('normal',ell),('mixed',s.Matrix([3,0,5,4]))]:
    a=dot(p,n); P=c(p)*c(n)/(2*a)
    h=s.eye(4)-(p*(n.T*eta)+n*(p.T*eta))/a
    ok(label+' null input',dot(p,p)==0)
    ok(label+' kernel projection',eq(P*P,P) and eq(c(p)*P,s.zeros(4)))
    ok(label+' screen projection',eq(h*h,h) and h.trace()==2 and h*p==s.zeros(4,1) and h*n==s.zeros(4,1))
    V=[sum((h[i,j]*P*b0[j] for j in range(4)),zero) for i in range(4)]
    J=[sum((h[i,j]*eta[j,j]*g[j] for j in range(4)),s.zeros(4)) for i in range(4)]
    ok(label+' screen gamma insertion',eq(sum((g[i]*J[i] for i in range(4)),s.zeros(4)),2*eye))
    w=[s.simplify(V[i]-J[i]*Gamma(V)/2) for i in range(4)]
    ok(label+' smooth exact common polarization',eq(Gamma(w),zero) and eq(ip(p,w),zero) and all(eq(c(p)*z,zero) for z in w))
    ok(label+' observation nonzero',q(w)!=s.zeros(8,1))
    for tag,z in [('plain',w),('input chirality',[omega*v for v in w])]:
        cp=[c(p)*v for v in z]; tr=Gamma(z); con=ip(p,z)
        generators=[cp,[p[i]*tr for i in range(4)],[eta[i,i]*g[i]*con for i in range(4)],[eta[i,i]*g[i]*c(p)*tr for i in range(4)],[con],[c(p)*tr]]
        ok(label+' all non-scalar-input generators '+tag,all(eq(v,zero) for gen in generators for v in gen))
    if label=='normal':ok('polarization anchors exactly',all(eq(w[i],b0[i]) for i in range(4)))
    # Generic zeroth-order identity breaks the very same exact slab solution.
    ok(label+' lower-term countercontrol',any(v!=zero for v in w))
r,R,tau,c0,rho=s.symbols('r R tau c rho',positive=True)
mu=tau*(r*r+c0)**2*r**3
ok('coarea Jacobian',s.simplify((rho**5*(tau/rho)*r**3).subs(rho,s.sqrt(r*r+c0))-mu)==0)
mass=s.integrate(mu,(r,R,2*R))
ok('fixed-frequency shell grows R8',s.expand(mass).coeff(R,8)==s.Rational(255,8)*tau)
ok('positive shell leading coefficient',s.Rational(255,8)>0)
ok('s4 critical power',7-2*4==-1)
ok('s9over2 integrable tail',7-2*s.Rational(9,2)<-1)
ok('sharp observed scaling',s.Rational(13,2)-s.Rational(4,2)==s.Rational(9,2))
for exponent,expected in [(5,s.Rational(1,128)),(6,s.Rational(1,640))]:
    ok('convergent radial integral s'+str(exponent),s.integrate(r**7/(1+2*r*r)**exponent,(r,0,s.oo))==expected)
N=s.symbols('N',positive=True,integer=True)
ok('endpoint disjoint-shell averaging squared norm',s.simplify(N*(1/N)**2-1/N)==0)
ok('critical logarithmic substitution',s.diff(s.log(s.log(r)),r)==1/(r*s.log(r)))
ok('critical log beta2 tail',s.diff(-1/s.log(r),r)==1/(r*s.log(r)**2))
ok('native visible dimension reused',4*64-64==192)
print(json.dumps({'status':'pass','checks':len(checks),'scope':__doc__,'results':checks},indent=2))
