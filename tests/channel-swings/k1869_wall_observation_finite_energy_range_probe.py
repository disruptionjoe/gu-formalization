#!/usr/bin/env python3
"""Independent frequency arithmetic; numerical integral comparisons are not rigorous bounds."""
from fractions import Fraction as F
from pathlib import Path
import json,copy
R=Path(__file__).resolve().parents[2];M=json.loads((R/'lab/process/k1869-wall-observation-finite-energy-range.json').read_text())
def verify(m):
 c={k:F(v) for k,v in m['constants'].items()};n=0
 def ck(v,msg):
  nonlocal n
  assert v,msg
  n+=1
 ck(c['speed_inverse']==24,'held target speed');ck(c['normal_factor']*2==24,'normalization at held kink scale')
 ck(c['mass_square_factor']==24**2,'held adjoint-square mass factor');ck(c['fourier_gaussian_norm_squared']==1,'radial probability integral')
 for b in [F(1,10),F(1),F(10)]:
  for t in [F(1,7),F(1),F(5)]:
   den=t+b
   # Integrand differences are exact derivatives with zero boundary integrals.
   budget_decl=c['budget_J_coefficient']*(1+b)/den+c['budget_constant']
   ck(t/den**2-budget_decl==t/den-b/den**2,'budget integration by parts')
   err_decl=c['error_linear']*b+c['error_J_coefficient']*b*b/den
   ck(b*b/den**2-err_decl==b*b/den**2+b*b/den-b,'error identity integrated J recurrence')
 for sig in [F(1,10),F(1),F(3)]:
  for tau in [F(1,7),F(2)]:
   for y in [F(-1),F(2,3)]:
    best=sig*y/(sig*sig+tau)
    for u in [F(0),F(1),best]:
     ck((sig*u-y)**2+tau*u*u-tau*y*y/(sig*sig+tau)==(sig*sig+tau)*(u-best)**2,'frequency optimality')
 for d in [1,2,3]:
  for ell in [0,1,2]:ck((d-3+2*ell>-1)==(d+2*ell>2),'radial integrability threshold')
 expected={'conditional_fixture':True,'dense_proper_massless_range':True,'gaussian_massless_finite_lift':False,'schwartz_zero_mean_criterion':True,'general_l2_zero_mean_sufficient':False,'native_gu_wall':False,'physical_chirality':False}
 for k,v in expected.items():ck(m['scope'][k]==v,'scope '+k)
 return n-len(expected),len(expected)
def numerical():
 import mpmath as mp
 mp.mp.dps=40;n=0
 for b in [mp.mpf('0.01'),mp.mpf('0.2'),mp.mpf('2')]:
  J=mp.quad(lambda t:mp.exp(-t)/(t+b),[0,1,mp.inf])
  B=mp.quad(lambda t:t*mp.exp(-t)/(t+b)**2,[0,1,mp.inf])
  E=mp.quad(lambda t:b*b*mp.exp(-t)/(t+b)**2,[0,1,mp.inf])
  assert abs(B-((1+b)*J-1))<mp.mpf('1e-30'),'numerical budget comparison'
  assert abs(E-(b-b*b*J))<mp.mpf('1e-30'),'numerical error comparison'
  n+=2
 return n
if __name__=='__main__':
 print('PASS independent exact math, scope checks:',verify(M));count=0
 for key,value in [('normal_factor','24'),('speed_inverse','12'),('mass_square_factor','24'),('fourier_gaussian_norm_squared','2'),('budget_J_coefficient','2'),('budget_constant','0'),('error_linear','2'),('error_J_coefficient','1')]:
  bad=copy.deepcopy(M);bad['constants'][key]=value
  try:verify(bad)
  except AssertionError as e:print('DETECTED mathematical input',key,':',e);count+=1
  else:raise AssertionError('undetected mathematical fault '+key)
 scopes=0
 for key in M['scope']:
  bad=copy.deepcopy(M);bad['scope'][key]=not bad['scope'][key]
  try:verify(bad)
  except AssertionError as e:print('DETECTED reporting',key,':',e);scopes+=1
  else:raise AssertionError('undetected scope fault '+key)
 print('PASS assertion-detected mathematical/reporting faults:',count,scopes)
 print('PASS numerical integral consistency only:',numerical())
