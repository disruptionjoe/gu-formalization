#!/usr/bin/env python3
"""Exact finite identities; continuum theorem is proved in K1854."""
from pathlib import Path
import json, hashlib
import sympy as S
ROOT=Path(__file__).resolve().parents[2]
def verify(d):
 x,v,b=S.symbols('x v b',real=True); checks=0
 def eq(a,z=0):
  nonlocal checks
  assert S.simplify(a-z)==0,(a,z);checks+=1
 assert d['clip_radius']==1
 for clip,indicator in [(-1,0),(x,1),(1,0)]:
  f=(x*x-1)*clip
  eq(S.diff(f,x),d['derivative_linear']*x*clip+d['derivative_indicator']*(x*x-1)*indicator)
 # All three polynomial regions and continuity at the corners.
 eq((x*x-1)**2-((x*x-1)*x)**2,(1-x*x)**3)
 for at in [-1,1]: eq(((x*x-1)*x).subs(x,at),0)
 eq(sum(S.Integer(c)*v**i for i,c in enumerate(d['upper_moment_coefficients'])),(1-v)**2+6*(1-v)*v+3*v*v)
 eq(d['leading_coefficient'],4)
 eq(d['lower_error'],d['derivative_linear']+d['derivative_indicator'])
 eq(4/(b+1)-2/(b+1)**2,4*(1/(b+1))-2*(1/(b+1))**2)
 for delta in [S.Rational(1,100),S.Rational(1,4),S.Rational(1,2),S.Integer(1)]:
  vv=1-S.sqrt(1-delta/2)
  eq(4*vv-2*vv*vv,delta)
  eq(1/vv,2*(1+S.sqrt(1-delta/2))/delta)
 assert not any(d[k] for k in ['balanced_without_symmetry','tv_to_atomic','subleading_claim','novelty'])
 for dep in d['dependencies']:assert hashlib.sha256((ROOT/dep['path']).read_bytes()).hexdigest()==dep['sha256']
 return checks
if __name__=='__main__':
 d=json.loads((ROOT/'lab/process/k1854-fisher-concentration-endpoint.json').read_text())
 print('K1854 exact algebra groups PASS',verify(d))
