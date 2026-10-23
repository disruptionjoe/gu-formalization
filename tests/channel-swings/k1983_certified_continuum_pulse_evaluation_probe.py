"""Exact algebra plus a separate high-precision continuum reference.
High-precision spotchecks detect implementation errors; analytic Lipschitz bounds,
not numerical agreement, certify the continuum enclosure.
"""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
import sympy as s
import mpmath as mp
import k1983_certified_continuum_pulse_evaluation as e
ROOT=Path(__file__).resolve().parents[2]
def reference():
 mp.mp.dps=60;t=mp.findroot(lambda x:101*x**4-102*x**3-168*x*x+392*x-138,.45)
 lam=(-mp.mpf(7)/100+mp.mpf(69)*t/200-mp.mpf(77)*t*t/200)/(mp.mpf(1)/6-t*t/2+2*t**3/3-t**4/4)
 def ph(x):
  if x<0:return -ph(-x)
  if x<t:return -x+lam*(1-t)**2*x/2
  if x<1:return -x-lam*(x-1)*(x-t*t)/2
  if x<=2:return -mp.mpf(1)
  return x-3+lam*(x-2)*(3-x)/2
 # Independent definite integral via polynomial antiderivatives, in another numeric field.
 pieces=[(0,t,[0,-1+lam*(1-t)**2/2]),(t,1,[-lam*t*t/2,-1+lam*(1+t*t)/2,-lam/2]),(1,2,[-1]),(2,3,[-3-3*lam,1+5*lam/2,-lam/2])]
 def prim(x):
  x=abs(x);v=mp.mpf(0)
  for a,b,c in pieces:
   if x>a:
    v+=sum(cc*(min(x,b)**(i+1)-a**(i+1))/(i+1) for i,cc in enumerate(c))
  return v
 def av(z):
  a=max(-3,z-9);b=min(3,z)
  return 2*ph(a)/9 if a==b else 2*(prim(b)-prim(a))/(9*(b-a))
 def v3(u,z,eps):
  a=2+eps;knots=[u]+[v for v in [-3,-2,-1,-t,0,t,1,2,3,6,7,8,9-t,9,9+t,10,11,12] if u<v<u+9]+[u+9]
  integral=sum(mp.quad(av,[x,y]) for x,y in zip(knots,knots[1:]))/9
  raw=((a*a+a+1)*2*ph(u)/9+integral-(a+2)*av(z))/a**3
  return min(mp.mpf('0.23'),max(-mp.mpf('0.23'),raw))
 return v3
REF=None
def check(fault=None):
 global REF
 r=json.loads((ROOT/'lab/process/k1983-certified-continuum-pulse-evaluation.json').read_text());count=0
 x,t,l,a,gu,qg,pqg=s.symbols('x t l a gu qg pqg',real=True)
 pieces=[-x+l*(1-t)**2*x/2,-x-l*(x-1)*(x-t*t)/2,s.Integer(-1),x-3+l*(x-2)*(3-x)/2]
 assert s.simplify(pieces[0].subs(x,t)-pieces[1].subs(x,t))==0
 assert pieces[1].subs(x,1)==-1 and pieces[3].subs(x,2)==-1 and pieces[3].subs(x,3)==0
 v1=gu/a;v2=((a+1)*gu-qg)/a**2;pv2=((a+1)*gu-pqg)/a**2;qv2=qg/a
 assert s.simplify((2*v2-pv2-qv2+gu)/a-((a*a+a+1)*gu+pqg-(a+2)*qg)/a**3)==0;count+=5
 # Uniform derivative bound on every polynomial segment: affine derivatives attain extrema at endpoints.
 for lo,hi,c in e.PIECES:
  for endpoint in [lo,hi]:
   assert abs(sum(i*b*endpoint**(i-1) for i,b in enumerate(c) if i))<=F(207,200),'phase Lipschitz';count+=1
 assert e.phi(F(0))==0 and e.phi(F(3))==0 and e.phi(F(-1))==1
 if REF is None:REF=reference()
 oldavg,oldg=e.avg,e.g;e.evaluate.cache_clear()
 if fault=='column_sign':e.avg=lambda z:-oldavg(z)
 if fault=='forcing_sign':e.g=lambda u:-oldg(u)
 if fault=='column_length':e.avg=lambda z:oldavg(z)*F(3,2)
 try:
  for c in r['controls']:
   u,z,eps=map(F,[c['u'],c['z'],c['epsilon']]);v=e.evaluate(3,u,z,eps,128)
   if fault=='step':v*=2+eps
   cv=lambda f:mp.mpf(f.numerator)/f.denominator
   ref=REF(cv(u),cv(z),cv(eps));bound=F(c['absolute_error'])
   assert abs(cv(v)-ref)<cv(bound),'actual continuum third-iterate enclosure';count+=1
   assert abs(v)<=e.M,'amplitude'
 finally:e.avg,e.g=oldavg,oldg;e.evaluate.cache_clear()
 for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 return count
if __name__=='__main__':
 n=check();caught=[]
 for f in ['column_sign','forcing_sign','column_length','step']:
  try:check(f)
  except AssertionError as ex:caught.append((f,str(ex)))
  else:raise AssertionError('undetected mathematical fault '+f)
 print('PASS K1983 separate',n,'exact algebra/derivative and numerical continuum controls;',caught)
