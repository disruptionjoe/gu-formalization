#!/usr/bin/env python3
"""Independent weighted projection and actual primitive controls with planted faults."""
import copy,hashlib,json
from fractions import Fraction as F
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
v=json.loads((ROOT/'lab/process/k1886-support-bounded-observation-approximation.json').read_text())

def formula_check(v):
 f=v['formula'];L=s.symbols('L',positive=True);a=s.symbols('a',positive=True)
 G=f['cube_gram_prefactor']*L**2*s.sinh(f['cube_gram_exponent']*a*L)/a
 assert s.limit(G,a,0)==8*L**3
 assert f['massless_volume_factor']==8
 inv=s.Rational(f['massive_squared_error_prefactor'])*a*s.exp(-2*a*L)/(L**2*(1-s.exp(-f['massive_tail_exponent']*a*L)))
 assert s.simplify((G*inv-1).rewrite(s.exp))==0
 # Integral check at exp(2aL)=2, using x1 integration and independent transverse area.
 assert f['cube_gram_prefactor']*(F(2)-F(1,2))/2==3
 assert f['optimal_squared_error']=='q^T G^-1 q'
 return 5

def report_check(v):
 assert v['scope']==dict(infimum_over_Cc_sources=True,nonzero_charge_smooth_target_attained=False,fixed_support_floor=True,source_energy_bound=False,native_GU=False,rotating_requires_repaired_map=True)
 for p,h in v['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 return 1+len(v['inputs'])
math_checks=formula_check(v);reports=report_check(v)
# Discrete quadrature-free Hilbert spaces independently certify projection algebra.
for n in [3,5,8]:
 weights=[F(i+1,n) for i in range(n)];h=[F(2)**(i-n//2) for i in range(n)]
 gram=sum(w*t*t for w,t in zip(weights,h))
 for seed in range(1,8):
  y=[F((i+1)**2-seed,seed+1) for i in range(n)]
  q=sum(w*t*z for w,t,z in zip(weights,h,y));r=[t*q/gram for t in h];z=[u-vv for u,vv in zip(y,r)]
  assert sum(w*t*zz for w,t,zz in zip(weights,h,z))==0;math_checks+=1
  assert sum(w*rr*rr for w,rr in zip(weights,r))==q*q/gram;math_checks+=1
  perturb=[F(i-seed) for i in range(n)];charge=sum(w*t*p for w,t,p in zip(weights,h,perturb))
  k=[p-t*charge/gram for p,t in zip(perturb,h)]
  assert sum(w*(yy-zz-kk)**2 for w,yy,zz,kk in zip(weights,y,z,k))==q*q/gram+sum(w*kk*kk for w,kk in zip(weights,k));math_checks+=1
  # Translate weight h by rational factor: charge and Gram must transform together.
  factor=F(seed+1,seed);q2=factor*q;g2=factor**2*gram
  assert q2*q2/g2==q*q/gram;math_checks+=1
# Actual compact C2 fixture; smooth continuum proof separately uses Cc-infinity bumps.
x,y,z=s.symbols('x y z');f=(1-x*x)**3*(1-y*y)**3*(1-z*z)**3
source=s.Matrix([f,0,0]);target=s.diff(f,x)
assert s.integrate(target,(x,-1,1))==0;math_checks+=1
assert s.integrate(s.diff(target,x),(x,-1,1))==0;math_checks+=1
for sign in [-1,1]:
 assert f.subs(x,sign)==0 and target.subs(x,sign)==0;math_checks+=1
# Positive bump is a nonzero-charge target and the projection loses compactness.
charge=s.integrate(f,(x,-1,1),(y,-1,1),(z,-1,1))
assert charge>0
projected=f-charge/8
assert projected.subs(x,1)==-charge/8!=0;math_checks+=2
actual_faults=0
for key,badval in [('cube_gram_prefactor',2),('cube_gram_exponent',1),('massless_volume_factor',4),('massive_squared_error_prefactor','2'),('massive_tail_exponent',2)]:
 bad=copy.deepcopy(v);bad['formula'][key]=badval
 try:formula_check(bad)
 except AssertionError:actual_faults+=1
 else:raise AssertionError('mathematical fault survived: '+key)
report_faults=0
for key in ['nonzero_charge_smooth_target_attained','source_energy_bound','native_GU','rotating_requires_repaired_map']:
 bad=copy.deepcopy(v);bad['scope'][key]=not bad['scope'][key]
 try:report_check(bad)
 except AssertionError:report_faults+=1
 else:raise AssertionError('report fault survived')
bad=copy.deepcopy(v);bad['inputs'][next(iter(bad['inputs']))]='0'*64
try:report_check(bad)
except AssertionError:report_faults+=1
else:raise AssertionError('pin fault survived')
print('PASS K1886 independent:',math_checks,'projection/primitive controls;',actual_faults,'actual formula faults;',reports,'report/pin checks;',report_faults,'report/pin faults')
