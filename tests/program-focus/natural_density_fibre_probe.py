#!/usr/bin/env python3
"""Exact controls for natural full-fibre density proofs, not physical selection.
The universal invariant-measure and integrability arguments remain written proofs.
"""
import json
import sympy as s
checks={}
def ok(name,value):checks[name]=bool(value);assert value,name
g=s.Matrix([[0,1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,1]])
A=s.diag(2,s.Rational(1,2),1,1)
ok('Lorentz boost preserves g',A.T*g*A==g)
ok('boost determinant one',A.det()==1)
eps=s.symbols('eps',positive=True);y=g.copy();y[0,0]=eps
ok('same-signature null perturbation determinant',y.det()==g.det()==-1)
ok('boost null evaluation scales four',s.expand((A.T*y*A)[0,0])==4*eps)
ok('relative determinant cannot damp this orbit',(g.inv()*y).det()==1)
for j in range(5):ok('disjoint boost interval '+str(j),2*4**j<4**(j+1))
d=s.symbols('d0:4',positive=True);weights=[d[i]*d[j] for i in range(4) for j in range(i,4)]
ok('Sym2 congruence determinant exponent five',s.prod(weights)==s.prod(d)**5)
ok('vertical density covariance',s.simplify((s.prod(d)**2)**(-s.Rational(5,2))*s.prod(d)**5)==1)
lam=s.symbols('lambda');v=s.diag(*s.symbols('v0:4'));gd=s.diag(-1,1,1,1);tr=s.trace(gd*v)
K=s.trace(gd*gd*gd*v)-lam*s.trace(gd*gd)*tr
ok('trace-reversed Euler pairing',s.expand(K-(1-4*lam)*tr)==0)
ok('native raised H coefficient',-s.Rational(1,2)/(1-4*s.Rational(1,2))==s.Rational(1,2))
ok('lambda-one coefficient differs',-s.Rational(1,2)/(1-4)==s.Rational(1,6))
ok('degenerate trace reversal excluded',1-4*s.Rational(1,4)==0)
x,z=s.symbols('x z',real=True)
ok('polynomial profile violates extra cocycle',s.expand((x+z)+(x+z)**2-(x+x*x)-(z+z*z))==2*x*z)
t=s.symbols('t');V=s.Matrix(4,4,lambda i,j:s.Symbol('v'+str(min(i,j))+str(max(i,j))))
rem=s.trace((gd*(gd+t*V)-s.eye(4))**2)
ok('higher natural jet zero at diagonal',rem.subs(t,0)==0 and s.diff(rem,t).subs(t,0)==0)
u=s.Matrix([1,0,0,0]);uf=gd*u;h=gd+2*uf*uf.T
ok('extra timelike clock gives positive metric',h==s.eye(4))
B=s.eye(4);B[0:2,0:2]=s.Matrix([[s.Rational(5,4),s.Rational(3,4)],[s.Rational(3,4),s.Rational(5,4)]])
ok('clock data breaks full Lorentz stabilizer',B.T*gd*B==gd and B*u!=u)
ok('determinant inverse power for density control',-s.Rational(1,2)-s.Rational(5,2)==-3)
ok('Gaussian absorbs polynomial inverse degree',4*3==12)
print(json.dumps({'status':'pass','checks':len(checks),'scope':__doc__,'results':checks},indent=2))
