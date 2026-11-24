#!/usr/bin/env python3
"""Exact controls for moving metric variation, dual descent and density domains.
No source action, physical quotient or Fredholm domain is constructed.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('VECLIB_MAXIMUM_THREADS','1')
import sympy as S
import json
checks=[]
def ck(name,value):
    assert bool(value),name
    checks.append(name)
def zero(x):return S.simplify(x)==0
x,u,v,w=S.symbols('x u v w',real=True)
b=S.diag(-2,3,4,5)
h=S.Matrix([[1,1,0,0],[1,2,1,0],[0,1,-1,1],[0,0,1,3]])
k=S.Matrix([[2,0,1,0],[0,-1,0,1],[1,0,2,1],[0,1,1,-2]])
ck('noncommuting metric variations',h*k!=k*h)
B=b+x*h+u*k;Y=b+v*h+w*k
fb=S.log(-B.det())/2;fy=-S.log(-Y.det())/2
at0={x:0,u:0,v:0,w:0};trh=S.trace(b.inv()*h);trk=S.trace(b.inv()*k)
ck('actual determinant first b derivative',zero(S.diff(fb,x).subs(at0)-trh/2))
ck('actual determinant first y derivative',zero(S.diff(fy,v).subs(at0)+trh/2))
ck('actual noncommuting b Hessian',zero(S.diff(fb,x,u).subs(at0)+S.trace(b.inv()*h*b.inv()*k)/2))
ck('actual noncommuting y Hessian',zero(S.diff(fy,v,w).subs(at0)-S.trace(b.inv()*h*b.inv()*k)/2))
f=fb+fy;rho=S.sqrt(B.det()/Y.det())
ck('log mixed Hessian zero',zero(S.diff(f,x,w)))
ck('density mixed Hessian nonzero',zero(S.diff(rho,x,w).subs(at0)+trh*trk/4) and trh*trk!=0)
ck('moving section log identically zero',zero(f.subs({v:x,w:u})))
ck('moving section weight identically one',zero(rho.subs({v:x,w:u})-1))
ck('full first weight derivative cancels',zero((S.diff(rho,x)+S.diff(rho,v)).subs(at0)))
ck('full mixed second weight derivative cancels',zero((S.diff(rho,x,u)+S.diff(rho,x,w)+S.diff(rho,v,u)+S.diff(rho,v,w)).subs(at0)))
ck('frozen-y derivative would give false moving response',S.diff(rho,x).subs(at0)!=0)
# Actual four-dimensional trace reversal, with off-diagonal test h.
K=lambda a,c:S.trace(b.inv()*a*b.inv()*c)-S.trace(b.inv()*a)*S.trace(b.inv()*c)/2
ck('Euler norm minus four',K(b,b)==-4)
ck('gradient half Euler',zero(K(b/2,h)+trh/2))
ck('mean norm minus one',K(b/2,b/2)==-1)
s,a=S.symbols('s a',real=True)
for name,F in [('linear',s),('bounded',S.tanh(s)),('free_second_jet',S.tanh(s)+a*S.tanh(s)**2)]:
 ck(name+' value zero',F.subs(s,0)==0)
 ck(name+' first jet one',S.diff(F,s).subs(s,0)==1)
ck('bounded profile adjustable second jet',S.diff(S.tanh(s)+a*S.tanh(s)**2,s,2).subs(s,0)==2*a)
ck('bounded profile differs globally',S.diff(S.tanh(s),s)!=1)
# Held ambient fields and moving point: direct chain rule, not row rescaling.
t=S.symbols('t',real=True);y0,y1=S.symbols('y0 y1',real=True)
b0,b1=2+3*t,5-2*t;z0=1+y0*y1;z1=3+y0**2;bn=2+y1
Q=bn*(y0*z0+y1*z1)/2;curve={y0:b0,y1:b1}
ck('moving Euler evaluation includes field jets',zero(S.diff(Q.subs(curve),t)-(3*S.diff(Q,y0)-2*S.diff(Q,y1)).subs(curve)))
ck('held-field Euler factor response nonzero',S.diff(((2+3*t)*7+(5-2*t)*11)/2,t)!=0)
m=S.exp(t);ck('density variation chain',zero(S.diff(m*Q.subs(curve),t)-m*S.diff(Q.subs(curve),t)-m*Q.subs(curve)))
# Differentiate the COMPLETE moving quotient, with frozen-map contrary control.
U=S.Matrix([[1,t],[t,1+t*t]]);D0=S.Matrix([[2,3],[0,5]])
Dt=U*D0*U.inv();qt=S.Matrix([[0,1]])*U.inv();kt=U*S.Matrix([1,0])
ck('moving quotient identity',S.simplify(qt*Dt-5*qt)==S.zeros(1,2))
ck('complete moving hidden response cancels',S.simplify(S.diff(qt,t)*Dt*kt+qt*S.diff(Dt,t)*kt+qt*Dt*S.diff(kt,t))==S.zeros(1,1))
ck('frozen quotient would falsely break repaired family',(qt*S.diff(Dt,t)*kt)[0].subs(t,0)!=0)
# Full profile gradient, frozen base versus moving diagonal.
xi,yi=S.symbols('xi yi',real=True)
F=S.tanh(s)+a*S.tanh(s)**2
V=S.diff(F,s).subs(s,2*xi-2*yi)*S.exp(yi)/2
ck('primitive metric response retains free second jet',zero(S.diff(V,xi).subs({xi:0,yi:0})-2*a))
ck('moving response independent of second jet',zero(S.diff(V.subs(yi,xi),xi).subs(xi,0)-S.Rational(1,2)))
# Density-valued two-sided variational blocks: direct differentiation of bilinear.
A,Bc,C=S.symbols('A B C');hh,oo,bh,bo=S.symbols('hidden observed barhidden barobserved')
D=S.Matrix([[A,Bc],[0,C]]);col=S.Matrix([hh,oo]);row=S.Matrix([[bh,bo]]);bil=(row*D*col)[0]
ck('unbar observed quotient closes',S.diff(bil,bo)==C*oo)
ck('bar observed equation retains hidden input',S.diff(bil,oo)==Bc*bh+C*bo)
ck('two cross blocks zero suffice',S.diff(bil,oo).subs(Bc,0)==C*bo)
ck('annihilator restriction removes barhidden term',S.diff(bil,oo).subs(bh,0)==C*bo)
Ds=S.Matrix([[A,Bc],[Bc,C]])
ck('self-dual control links both cross blocks',Ds==Ds.T and Ds[0,1]==Ds[1,0])
# Exact kernel projector and reciprocal rank using a 10D complex Clifford module.
from pathlib import Path
import sys,numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'channel-swings'))
from actual_sym2_c14_orbit_probe import native_gammas
gam,metric=native_gammas();normal=[gam[j] for j in range(14) if j not in [9,0,1,2]];d=gam[0].shape[0];Id=np.eye(d,dtype=np.complex128)
# Signed-monomial integer arrays, no approximate tolerances or numerical ranks.
eta=[int((g@g)[0,0].real) for g in normal]
ck('native normal dimensions and Clifford signs',len(normal)==10 and d==128 and all(np.array_equal(g@g,e*Id) for g,e in zip(normal,eta)))
idx=eta.index(-1);H=[int(j==idx) for j in range(10)];cH=normal[idx]
# Ten times P_K(Hflat psi) avoids fractions: 10 H_r Id - gamma_r c(H).
Z=[10*eta[j]*H[j]*Id-normal[j]@cH for j in range(10)]
ck('actual projected normal field gamma kernel',np.array_equal(sum(e*g@z for e,g,z in zip(eta,normal,Z)),np.zeros((d,d))))
ck('actual hidden readout minus9 identity',np.array_equal(Z[idx],-9*Id))
ck('dual kernel injection rank128 witnessed by left inverse',np.array_equal(-Z[idx],9*Id))
# Exact formal-dual and unitary conjugation formulas on nonconstant coefficient P.
afun=1+t*t;ufun=2+t+t**3;f=t*t+t
P=lambda z:afun*S.diff(z,t)
Padj=lambda z:-S.diff(afun*z,t)
ck('weighted adjoint differentiates measure',zero(S.exp(-f)*Padj(S.exp(f)*ufun)-Padj(ufun)+afun*S.diff(f,t)*ufun))
ck('unitary conjugation half drift',zero(S.exp(f/2)*P(S.exp(-f/2)*ufun)-P(ufun)+afun*S.diff(f,t)*ufun/2))
bvar=S.symbols('bvar',real=True);bar=S.symbols('bar');q=S.exp(bvar);E=q*bar*oo
ck('bar density coordinate metric chain',S.diff(E,bvar)==q*bar*oo)
# Different L2 spaces for canonical weight along scaling, not an index test.
ck('canonical conformal determinant drift',zero(S.log(S.exp(4*s))/(-2)+2*s))
ck('weighted ambient scale measure cancels',S.exp(-2*s)*S.exp(2*s)==1)
ck('tail weighted finite unweighted infinite',S.integrate(S.exp(-2*s),(s,0,S.oo))==S.Rational(1,2) and S.integrate(S.Integer(1),(s,0,S.oo))==S.oo)
ck('opposite tail unweighted finite weighted infinite',S.integrate(S.exp(2*s),(s,-S.oo,0))==S.Rational(1,2) and S.integrate(S.Integer(1),(s,-S.oo,0))==S.oo)
ck('bounded profile limits finite',S.limit(S.exp(S.tanh(s)),s,S.oo)==S.E and S.limit(S.exp(S.tanh(s)),s,-S.oo)==1/S.E)
print(json.dumps({'status':'PASS','check_count':len(checks),'checks':checks},indent=2))
