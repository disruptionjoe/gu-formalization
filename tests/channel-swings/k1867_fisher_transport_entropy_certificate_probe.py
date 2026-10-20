#!/usr/bin/env python3
"""Independent Fraction certificate reconstruction and Gaussian controls."""
import json,copy
from fractions import Fraction as F
from pathlib import Path
R=Path(__file__).resolve().parents[2];M=json.loads((R/'lab/process/k1867-fisher-transport-entropy-certificate.json').read_text())
def polynomial(cs,x):
 out=F(0)
 for a in reversed(cs):out=out*x+F(a)
 return out

def verify(m):
 c={k:F(v) for k,v in m['constants'].items()};n=0
 def ck(v):
  nonlocal n
  assert v
  n+=1
 ck(c['rho_squared_floor']<=F(1,2));ck(c['a_floor']==F(1,2))
 for sigma in [F(1,2),F(1),F(2)]:
  for mean in [F(0),F(1,3),F(2)]:
   v=sigma*sigma;raw=1/v-1;relative=v-2+1/v+mean*mean
   ck(raw+(v+mean*mean-1)==relative);ck(c['relative_information_factor']*(v*(1-1/v)**2+mean*mean)/4==relative)
   W2=mean*mean+(sigma-1)**2;ck(relative-W2==(sigma-1)**2*(2*sigma+1)/sigma**2)
 ck(c['transport_squared_factor']*F(1,2)>=1);ck(c['entropy_coefficient_squared']*F(1,2)>=F(1,4))
 for x,y in [(F(2),F(1)),(F(-3),F(-1)),(F(1),F(-1))]:ck(abs((x*x-y*y)/2)<=c['quadratic_loss_factor']*abs(x-y)*(abs(x)+abs(y))/2)
 data=json.loads((R/'lab/process/k1865-fisher-effective-trial-certificate.json').read_text())
 for s in [F(1,1000),F(1,200),F(1,10000)]:
  N=polynomial(['1','0','0','1/64','7991/331776'],s);B=polynomial(['1','0','0','13/576','93863/331776'],s)
  R2=s**6*polynomial(['18165763/124416','167987027/248832','202282679/147456'],s)
  ck(N==polynomial(data['polynomials']['N'],s));ck(B==polynomial(data['polynomials']['B'],s));ck(R2==polynomial(data['polynomials']['R2'],s))
  E=B*R2/(2*N*N)
  ck(2*E<(c['trial_transport_coefficient']*s**3)**2);ck(E*E/2<(c['trial_entropy_coefficient']*s**6)**2);ck(8*E<(c['trial_quadratic_coefficient']*s**3)**2)
  eps=F(1,1000);eta=eps**2/2-E;ck(eta>=0 and 2*(E+eta)==eps**2);ck(7*2*(E+eta)==7*eps**2)
 ck(m['scope']['exact_moments'] and m['scope']['forward_entropy']);ck(not m['scope']['reverse_entropy'] and not m['scope']['unbounded_sixth_moment_transfer'] and not m['scope']['gu_verdict'])
 return n
if __name__=='__main__':
 n=verify(M);faults=0
 for key,value in [('a_floor','1'),('rho_squared_floor','1'),('relative_information_factor','2'),('entropy_coefficient_squared','1/4'),('transport_squared_factor','1'),('quadratic_loss_factor','1/2'),('trial_transport_coefficient','1'),('trial_entropy_coefficient','1'),('trial_quadratic_coefficient','1')]:
  bad=copy.deepcopy(M);bad['constants'][key]=value
  try:verify(bad)
  except AssertionError:faults+=1
  else:raise AssertionError('undetected math/input fault '+key)
 sf=0
 for key in M['scope']:
  bad=copy.deepcopy(M);bad['scope'][key]=not bad['scope'][key]
  try:verify(bad)
  except AssertionError:sf+=1
  else:raise AssertionError('undetected scope fault '+key)
 print('PASS independent controls:',n,'math/input faults:',faults,'scope faults:',sf)
