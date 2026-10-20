#!/usr/bin/env python3
"""Independent rational fixtures; not a numerical substitute for the weak-score proof."""
from fractions import Fraction as Q
from pathlib import Path
from copy import deepcopy
import json, math
ROOT=Path(__file__).resolve().parents[2]
def verify(d):
 n=0
 def ok(condition,why):
  nonlocal n
  assert condition,why;n+=1
 radius=Q(d['clip_radius'])
 for i in range(-48,49):
  x=Q(i,12);c=max(-radius,min(x,radius));f=(x*x-1)*c
  if abs(x)!=radius:
   # Numerical-free derivative of the piecewise polynomial defined by its input radius.
   actual=3*x*x-1 if abs(x)<radius else 2*x*c
   report=d['derivative_linear']*x*c+d['derivative_indicator']*(x*x-1)*(abs(x)<1)
   ok(actual==report,'piecewise derivative')
  ok(f*f<=(x*x-1)**2,'clipped fourth-moment bound')
  ok(x*c>=x*x-abs(x*x-1),'first derivative expectation premise')
  ok((abs(x)-1)**2<=(x*x-1)**2,'transport bound')
 ok(d['lower_error']==d['derivative_linear']+d['derivative_indicator'],'Cauchy error sum')
 for v in [Q(1,1000),Q(1,100),Q(1,4),Q(1,2),Q(3,4)]:
  a2=1-v
  actual=a2*a2+6*a2*v+3*v*v
  report=sum(Q(c)*v**j for j,c in enumerate(d['upper_moment_coefficients']))
  ok(actual==report,'Gaussian fourth moment')
  delta=actual-1
  ok(delta/v==4-2*v,'rationalized upper bound')
  ok(0<delta<2,'moment domain')
 for m in [2,3,5,10,100]:
  # B+1=m² makes both budget endpoints rational.
  B=Q(m*m-1);lo=Q(4,(m+3)**2);up=4/(B+1)-2/(B+1)**2
  ok(lo<=up,'budget bracket ordering')
  ok(Q(2)/Q(2,m+3)-d['lower_error']==m,'lower budget inversion')
 ok(d['leading_coefficient']==4,'endpoint coefficient from delta/v limit')
 for key in ['balanced_without_symmetry','tv_to_atomic','subleading_claim','novelty']:ok(d[key] is False,'scope '+key)
 return n
if __name__=='__main__':
 d=json.loads((ROOT/'lab/process/k1854-fisher-concentration-endpoint.json').read_text());print('K1854 independent rational checks PASS',verify(d))
 mathfaults={'clip_radius':Q(2),'derivative_linear':3,'derivative_indicator':2,'lower_error':2,'upper_moment_coefficients':[1,4,-1],'leading_coefficient':2}
 reporting={'balanced_without_symmetry':True,'tv_to_atomic':True,'subleading_claim':True,'novelty':True}
 for kind,changes in [('input',mathfaults),('reporting',reporting)]:
  for key,value in changes.items():
   mutant=deepcopy(d);mutant[key]=value
   try:verify(mutant)
   except AssertionError as err:print('[FAIL detected]',kind,key,str(err))
   else:raise AssertionError('undetected '+key)
 print('PASS 6 mathematical input faults and 4 reporting faults; crashes are not detections')
