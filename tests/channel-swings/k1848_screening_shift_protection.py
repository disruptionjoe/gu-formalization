#!/usr/bin/env python3
"""Exact algebra for affine source shift; continuum proofs live in the note."""
from pathlib import Path
import json,hashlib
import sympy as s
R=Path(__file__).resolve().parents[2];p=R/'lab/process/k1848-screening-shift-protection.json';r=json.loads(p.read_text());checks={}
def ck(k,v):
 assert bool(v),k
 checks[k]=True
x,y,J,e,lam,z,Z,C=s.symbols('x y J e lam z Z C',real=True)
phi=s.Matrix([x,y]);v=s.Matrix(list(map(s.Rational,r['fixture']['v'])));A=s.Matrix([[s.Rational(x) for x in row] for row in r['fixture']['A']]);c=s.Matrix(list(map(s.Rational,r['fixture']['c'])));h=s.Rational(r['fixture']['h'])
chi=phi-J*v;U=(chi.T*A*chi)[0]/2+lam*(chi.dot(chi))**2/4
ck('source coefficient',c==A*v);ck('contact coefficient',h==v.dot(A*v));ck('positive mass',A[0,0]>0 and A.det()>0)
ck('nonlinear affine invariance',s.expand(U.subs({x:x+e*v[0],y:y+e*v[1],J:J+e},simultaneous=True)-U)==0)
O=-s.diff(U,J);grad=s.Matrix([s.diff(U,x),s.diff(U,y)])
ck('same action readout',s.expand(O-v.dot(grad))==0)
ck('full stationary solution',all(s.expand(t.subs({x:J*v[0],y:J*v[1]},simultaneous=True))==0 for t in grad))
H=s.hessian(U,(x,y));ck('positive Hessian decomposition',s.simplify(H-(A+lam*(chi.dot(chi)*s.eye(2)+2*chi*chi.T)))==s.zeros(2))
ck('minimum linearization',H.subs({x:J*v[0],y:J*v[1]},simultaneous=True)==A)
response=c.dot((z*s.eye(2)+A).inv()*c)-h
ck('protected resolvent',s.factor(response+z*v.dot(A*(z*s.eye(2)+A).inv()*v))==0)
ck('zero static',response.subs(z,0)==0);ck('nonzero response',s.factor(response)!=0)
ck('low frequency inertia',s.limit(response/z,z,0)==-v.dot(v))
M=A.row_join(-A*v).col_join((-v.T*A).row_join(s.Matrix([[h]])))
ck('one dynamical flat mode',M.rank()==2 and M*s.Matrix([*v,1])==s.zeros(3,1))
w=s.Matrix([x,y,J]);ck('positive potential square',s.expand(w.dot(M*w)-chi.dot(A*chi))==0)
Keff=Z*z+h-c.dot((z*s.eye(2)+A).inv()*c)
ck('Schur kernel',s.factor(Keff-z*(Z+v.dot(A*(z*s.eye(2)+A).inv()*v)))==0)
ck('Schur inertial coefficient',s.limit(Keff/z,z,0)==Z+v.dot(v))
ck('generalized mass determinant',s.factor((z*s.diag(1,1,Z)+M).det()-(z*s.eye(2)+A).det()*Keff)==0)
w1,w2,eta=s.symbols('w1 w2 eta');wvec=s.Matrix([w1,w2]);cp=c+e*wvec
ck('broken symmetry static residual',s.expand(cp.dot(A.inv()*cp)-(h+eta)-(2*e*v.dot(wvec)+e**2*wvec.dot(A.inv()*wvec)-eta))==0)
ck('constant potential leaves response',s.diff(U+C,J)==s.diff(U,J))
ck('constant potential changes vacuum energy',(U+C-U)==C)
omega,t=s.symbols('omega t',positive=True)
primitive=omega**2*s.sin(omega*t)/t+2*omega*s.cos(omega*t)/t**2-2*s.sin(omega*t)/t**3
ck('continuum oscillatory primitive',s.simplify(s.diff(primitive,omega)-omega**2*s.cos(omega*t))==0)
ck('continuum boundary variation bound',1+4+s.integrate(2*omega,(omega,1,2))==s.Rational(r['continuum']['late_bound_coefficient']))
ck('continuum energy',s.integrate(omega**2/2,(omega,1,2))==s.Rational(r['continuum']['energy_coefficient']))
P=s.diag(1,0);ds=s.Matrix([0,1]);cs=s.Matrix([1,0]);ck('internal sector commutation',P*A==A*P);ck('internal all-frequency silence',ds.dot((z*s.eye(2)+A).inv()*cs)==0)
for d in r['dependencies']:ck('dependency '+d['path'],hashlib.sha256((R/d['path']).read_bytes()).hexdigest()==d['sha256'])
r['exact_algebra_checks']=checks;p.write_text(json.dumps(r,indent=2)+'\n');print('K1848 exact algebra groups',len(checks))
