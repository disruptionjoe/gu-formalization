#!/usr/bin/env python3
"""Independent rational paired-density and barrier controls, with assertion faults."""
from fractions import Fraction as F
from pathlib import Path
import json,copy
R=Path(__file__).resolve().parents[2];M=json.loads((R/'lab/process/k1868-fisher-two-well-instability.json').read_text())
def verify(m):
 c={k:F(v) for k,v in m['constants'].items()};n=0
 def ck(v,msg):
  nonlocal n
  assert v,msg
  n+=1
 for theta in [F(0),F(1,3),F(-2,3),F(1),F(-1)]:
  for z in [F(0),F(1,4),F(3,4)]:
   for rho in [F(-3),F(2,5)]:
    # Rational df tests exact pointwise identity; then substitute sine df² relation.
    df=F(2,7);a=1+theta*z;b=1-theta*z
    actual=((a*rho+theta*df)**2/a+(-b*rho+theta*df)**2/b)/2-rho*rho
    ck(actual==theta**2*df**2/(1-theta**2*z*z),'paired Fisher subtraction')
    ck((1-z*z)/(1-theta*theta*z*z)<=1,'uniform endpoint tilt bound')
    for even in [F(1),F(9),F(81)]:ck((a*even+b*even)/2==even,'even observable invariance')
   ck(c['tv_factor']*(abs(theta*z)+abs(-theta*z))/2==abs(theta*z)/2,'paired TV mass')
 ck(c['half_width']==F(1,4),'chosen physical transition interval')
 ck(c['deficit_pi2_factor']*(2*c['half_width'])**2==1,'sine frequency square')
 ck(c['barrier_mass_factor']==8*c['half_width'],'integrating pointwise barrier')
 for x in [F(0),F(1,8),F(1,4)]:ck(F(1,2)-x>=c['barrier_exponent'],'uniform comparison exponent')
 ck(c['spectral_pi2_factor']==4*c['deficit_pi2_factor'],'Schrodinger versus diffusion')
 for mass in [F(1,1000),F(1,10)]:
  ck((1-mass)/(c['deficit_pi2_factor']*mass)*c['spectral_pi2_factor']*mass/(1-mass)==4,'reciprocal gap conventions')
  ck(c['mean_sign_factor']*mass==mass/2,'sign imbalance probability')
 for imbalance in [F(1,8),F(1,3),F(1)]:
  moved=imbalance/2
  ck(c['atom_transport_factor']*imbalance==moved*(1-(-1))**2,'optimal two-atom transport')
 ck(c['collapse_error_factor']==1+1,'two collapse errors')
 expected={'all_even_moments':True,'absolute_excess':True,'endpoint_theta_allowed':True,'effective_onset':False,'sharp_tunneling_exponent':False,'mean_zero_effective_tv_rate':False,'mean_zero_qualitative_tv':True,'gu_verdict':False}
 for k,v in expected.items():ck(m['scope'][k]==v,'scope '+k)
 return n-len(expected),len(expected)
if __name__=='__main__':
 print('PASS independent rational math, scope checks:',verify(M));count=0
 for key,value in [('half_width','1/2'),('barrier_mass_factor','1'),('barrier_exponent','1/3'),('deficit_pi2_factor','2'),('spectral_pi2_factor','4'),('tv_factor','1'),('mean_sign_factor','1'),('atom_transport_factor','1'),('collapse_error_factor','1')]:
  bad=copy.deepcopy(M);bad['constants'][key]=value
  try:verify(bad)
  except AssertionError as e: print('DETECTED mathematical input',key,':',e);count+=1
  else:raise AssertionError('undetected mathematical fault '+key)
 scopes=0
 for key in M['scope']:
  bad=copy.deepcopy(M);bad['scope'][key]=not bad['scope'][key]
  try:verify(bad)
  except AssertionError as e:print('DETECTED reporting',key,':',e);scopes+=1
  else:raise AssertionError('undetected scope fault '+key)
 print('PASS assertion-detected mathematical/reporting faults:',count,scopes)
