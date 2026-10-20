#!/usr/bin/env python3
"""Exact algebra for K1844; continuum support/positivity proof is in the note."""
import sympy as s
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
z,t,a,b,eps=s.symbols('z t a b eps',positive=True)
checks={}
def ck(name,v):
    assert v,name
    checks[name]=True
K=s.Matrix([[2,1],[1,2]]);M=s.Matrix([[3,1],[1,1]]);c=s.Matrix([1,2]);d=s.Matrix([2,-1])
q=s.Matrix(s.symbols('q0:2'));vel=s.Matrix(s.symbols('v0:2'));J=s.symbols('J')
L=(vel.T*K*vel)[0]/2-(q.T*M*q)[0]/2+J*(c.T*q)[0]
ck('Euler kinetic Hessian',s.hessian(L,vel)==K)
ck('Euler mass Hessian',s.hessian(L,q)==-M)
ck('Euler source derivative',s.Matrix([s.diff(L,J,v) for v in q])==c)
ck('positive kinetic and mass minors',K.det()>0 and K[0,0]>0 and M.det()>0 and M[0,0]>0)
G=(z*K+M).inv();R=s.Matrix.hstack(c,d).T*G*s.Matrix.hstack(c,d)
ck('cross-response symmetry',R==R.T)
ck('positive matrix determinant',s.factor(R.det())==25/(3*z*z+6*z+2))
ck('conjugate DC', (c.T*M.inv()*c)[0]==s.Rational(9,2))
f=1/(z+1)-4/(z+4)
ck('two-field cancellation',s.factor(f)==-3*z/((z+1)*(z+4)))
ck('DC zero',f.subs(z,0)==0)
ck('nontrivial response',f.subs(z,1)==-s.Rational(3,10))
fg=1/(z+a)-(b/a)/(z+b)
ck('general cancellation',s.simplify(fg-(a-b)*z/(a*(z+a)*(z+b)))==0)
ck('equal mass triviality',fg.subs(b,a)==0)
ck('readout drift',s.simplify((1/(z+a)+(-b/a+eps)/(z+b)).subs(z,0))==eps/b)
p1=1-s.cos(t);p2=(1-s.cos(2*t))/4
ck('step equation one',s.simplify(s.diff(p1,t,2)+p1)==1)
ck('step equation two',s.simplify(s.diff(p2,t,2)+4*p2)==1)
ck('zero initial data',all(v.subs(t,0)==0 for v in [p1,p2,s.diff(p1,t),s.diff(p2,t)]))
ck('readout oscillation',s.simplify(p1-4*p2-(s.cos(2*t)-s.cos(t)))==0)
ck('nonconvergence subsequences',(s.cos(2*t)-s.cos(t)).subs(t,0)==0 and (s.cos(2*t)-s.cos(t)).subs(t,s.pi)==2)
ck('source contact derivative',s.diff(J*q[0]-J*J/(2*a),J)==q[0]-J/a)
ck('contact transfer',s.factor(1/(z+a)-1/a)==-z/(a*(z+a)))
ck('forcing versus field',s.cancel((z/(z+a))/z)==1/(z+a))
ck('derivative contact decomposition',s.cancel(z/(z+a)-(1-a/(z+a)))==0)
report=dict(artifact='K1844_POSITIVE_RESPONSE',scope='conditional_positive_quadratic_scalar_action',mathematical_checks=checks,conjugate_contact_free_DC_positive=True,cross_readout_fixture={'masses_squared':[1,4],'source':[1,1],'readout':[1,-4]},static_is_late_limit=False,signed_cross_residue_is_ghost=False,source_owned=False,all_screening_excluded=False,ledger_changes=False)
(ROOT/'lab/process/k1844-screening-positive-response.json').write_text(json.dumps(report,indent=2)+'\n')
print('K1844 exact algebra groups:',len(checks))
