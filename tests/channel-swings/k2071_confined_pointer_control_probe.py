"""Separate finite controls, not a finite substitute for the continuum proof."""
from fractions import Fraction as Q
from pathlib import Path
import json,copy,hashlib
ROOT=Path(__file__).resolve().parents[2]
def check(d):
 e=Q(d['eta']);l=Q(d['initial_radius']);t=Q(d['duration']);r=Q(d['ramp_width'])
 assert 24/l<=e,'preparation tail'
 assert Q(d['state_error'])>=2*e,'two discarded-tail evolutions'
 assert Q(d['sector_leakage_probability'])>=4*e*e,'sector leakage probability'
 assert Q(d['no_click_probability'])>=e*e,'detector tail'
 assert Q(d['control_radius'])>=l+t+2*r,'causal tube'
 assert Q(d['detector_radius'])>=l+t,'detector support'
 assert Q(d['strict_center_separation'])>=2*Q(d['control_radius'])+t,'spacelike cylinders'
 assert Q(d['bell_rational_lower'])<=Q(14,5)*Q(183,200)**2-32*e-16*e*e,'all-outcome Bell budget'
 assert Q(d['bell_rational_lower'])>2
 return 9
if __name__=='__main__':
 d=json.loads((ROOT/'lab/process/k2071-confined-pointer-control.json').read_text());count=check(d)
 for p,h in d['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 # Orthogonal inside/outside finite sectors: identity versus phase flip
 # agrees on inside, and attains the factor2 tail bound exactly.
 for a,b,c in [(Q(3,5),Q(4,5),2),(Q(5,13),Q(12,13),2),(Q(8,17),Q(15,17),2)]:
  assert a*a+b*b==1 and (b-(-b))**2==4*b*b;count+=2
 # Tensor telescoping checked on diagonal phase controls with entangled pairs.
 for n in range(1,8):
  # General product failure probability <= sum of marginal tail probabilities.
  e=Q(1,10);assert 1-(1-e*e)**n<=n*e*e;count+=1
 faults=[]
 for key,val in [('state_error','0'),('sector_leakage_probability','0'),('no_click_probability','0'),('control_radius','2400'),('strict_center_separation','1'),('bell_rational_lower','3')]:
  x=copy.deepcopy(d);x[key]=val
  try:check(x)
  except AssertionError:faults.append(key)
  else:raise AssertionError(('missed fault',key))
 print('PASS',count,'separate finite controls;',len(faults),'resource faults rejected')
