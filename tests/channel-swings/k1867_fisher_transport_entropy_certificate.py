#!/usr/bin/env python3
"""Symbolic transform and exact budgets; analytic proof is in the note."""
import json,hashlib
from pathlib import Path
import sympy as S
R=Path(__file__).resolve().parents[2];M=json.loads((R/'lab/process/k1867-fisher-transport-entropy-certificate.json').read_text())
def verify(m):
 c={k:S.Rational(v) for k,v in m['constants'].items()};n=0
 def ck(v):
  nonlocal n
  assert v
  n+=1
 x=S.symbols('x',real=True);w=S.Function('w')(x);V=S.Function('V')(x);ric=4*S.diff(w,x,2)-4*S.diff(w,x)**2+V
 ck(S.expand(S.diff(ric,x,2)-(4*S.diff(w,x,4)-8*S.diff(w,x)*S.diff(w,x,3)-8*S.diff(w,x,2)**2+S.diff(V,x,2)))==0)
 ck(c['rho_squared_floor']<=S.Rational(1,2));ck(c['a_floor']==S.Rational(1,2))
 v,t=S.symbols('v t',positive=True);relative=(1-1/v)**2*v+t*t;corrected=1/v+v+t*t-2
 ck(S.expand(relative-corrected)==0);ck(S.expand(c['relative_information_factor']*relative/4-corrected)==0)
 scale=S.symbols('scale',positive=True)
 ck(S.simplify((relative-(t*t+(S.sqrt(v)-1)**2)).subs(v,scale**2)-(scale-1)**2*(2*scale+1)/scale**2)==0)
 ck(c['transport_squared_factor']*c['rho_squared_floor']>=1);ck(c['entropy_coefficient_squared']*4*c['rho_squared_floor']>=1);ck(c['quadratic_loss_factor']>=1)
 s=S.Rational(1,1000);N=1+s**3/64+S.Rational(7991,331776)*s**4;B=1+S.Rational(13,576)*s**3+S.Rational(93863,331776)*s**4
 R2=S.Rational(18165763,124416)*s**6+S.Rational(167987027,248832)*s**7+S.Rational(202282679,147456)*s**8;E=B*R2/(2*N*N)
 ck(2*E<(c['trial_transport_coefficient']*s**3)**2);ck(E*E/2<(c['trial_entropy_coefficient']*s**6)**2);ck(8*E<(c['trial_quadratic_coefficient']*s**3)**2)
 ck(2*S.Rational(384,5)<c['trial_transport_coefficient']**2);ck(S.Rational(384,5)**2/2<c['trial_entropy_coefficient']**2);ck(8*S.Rational(384,5)<c['trial_quadratic_coefficient']**2)
 for p,digest in m['dependencies'].items():assert hashlib.sha256((R/p).read_bytes()).hexdigest()==digest
 return n,len(m['dependencies'])
if __name__=='__main__':print('PASS math, dependency controls:',verify(M))
