#!/usr/bin/env python3
"""Independent rational spectral controls and assertion-based faults."""
from fractions import Fraction as F
from pathlib import Path
import json,copy
R=Path(__file__).resolve().parents[2];M=json.loads((R/'lab/process/k1866-positive-scalar-screening-window.json').read_text())
def verify(m):
 c={k:F(v) for k,v in m['constants'].items()};n=0
 def ck(v):
  nonlocal n
  assert v
  n+=1
 gamma=lambda f:(1-c['slip_scalar_factor']*f)/(1+c['slip_scalar_factor']*f)
 for f in [F(0),F(1,3),F(2,5)]:
  T=[F(2),F(3),F(5),F(0)];sgn=[-1,1,1,1];tr=sum(a*b for a,b in zip(T,sgn));h=[2*T[i]-(1-f)*sgn[i]*tr for i in range(4)]
  ck(sum(h[i]*sgn[i] for i in range(4))-h[3]==-(1-c['trace_scalar_factor']*f)*tr)
 for masses,weights in [([0],[F(1,3)]),([0,1,4],[F(1,7),F(2,5),F(1,11)]),([1,9],[F(1,3),F(2,3)])]:
  response=lambda z:sum(w*z/(z+F(l)) for l,w in zip(masses,weights))
  for x,y in [(F(1,100),F(1)),(F(1,3),F(4)),(F(2),F(8))]:
   fx,fy=response(x),response(y)
   ck(fx<=fy);ck(fy<=y*fx/x);ck(response((x+y)/2)>=(fx+fy)/2);ck(gamma(fy)<=gamma(fx))
 for delta in [F(0),F(1,100),F(1,2),F(9,10)]:
  f=(1-delta)/3;ck(1-c['trace_scalar_factor']*f==delta);ck(gamma(f)==(2+delta)/(4-delta))
 ck(c['example_delta_lower']==1-3*c['example_epsilon']/(2-c['example_epsilon']))
 for z in [F(1,100),F(1),F(100)]:
  m2=F(4);diag=[1/z,1/(z+m2)];cross=diag[0]-diag[1]
  ck(z*cross==m2/(z+m2));ck(diag[0]>0 and diag[1]>0);ck(sum(diag)**2-cross**2==4*diag[0]*diag[1]>0)
 ck(m['scope']['positive_diagonal_measure'] and m['scope']['fixed_massless_tensor']);ck(m['scope']['universal_metric'] and not m['scope']['contacts']);ck(not m['scope']['gu_verdict'] and not m['scope']['empirical_ppn'])
 return n
if __name__=='__main__':
 n=verify(M);faults=0
 for key,value in [('trace_scalar_factor','2'),('slip_scalar_factor','2'),('example_epsilon','1/10'),('example_delta_lower','195/199')]:
  bad=copy.deepcopy(M);bad['constants'][key]=value
  try:verify(bad)
  except AssertionError:faults+=1
  else:raise AssertionError('undetected math fault '+key)
 sf=0
 for key in M['scope']:
  bad=copy.deepcopy(M);bad['scope'][key]=not bad['scope'][key]
  try:verify(bad)
  except AssertionError:sf+=1
  else:raise AssertionError('undetected scope fault '+key)
 print('PASS independent controls:',n,'math faults:',faults,'scope faults:',sf)
