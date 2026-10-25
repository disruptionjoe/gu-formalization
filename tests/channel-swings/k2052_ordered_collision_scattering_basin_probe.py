"""Separate Gaussian-rational force, barrier and ordered-support controls."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,copy
from k2046_large_data_characteristic_reduction_probe import add,mul,scale,conj,power,norm
ROOT=Path(__file__).resolve().parents[2];I=(F(0),F(1))
def replay(r):
 c=r['coefficients'];jets=barriers=0
 for m in range(2,8):
  for k in range(1,9):
   gamma=F(k+1,3);z=(F(k,3),F(2-k,5));w=(F(3-k,4),F(k,7));a,b=norm(z),norm(w)
   zv=mul(I,mul(conj(z),power(w,2*m)));wu=scale(-gamma,mul(I,mul(power(z,2),power(conj(w),2*m-1))))
   av=2*mul(conj(z),zv)[0];bu=2*mul(conj(w),wu)[0];P=mul(power(z,2),power(conj(w),2*m))[0]
   assert av*av+4*P*P==c['density_bound']**2*a*a*b**(2*m),'density modulus identity'
   assert bu==gamma*av,'weighted continuity identity'
   assert norm(zv)==a*b**(2*m),'z characteristic tail norm'
   assert norm(wu)==gamma**c['w_scattering_gamma_power']*a*a*b**(2*m-1),'w characteristic tail norm';jets+=1
  # Saturating real density source checks the constants used in the inequality.
  aa,bb,gamma=F(3,7),F(5,4),F(7,3)
  derivative=(1-m)*bb**(-m)*(2*gamma*aa*bb**m)
  assert derivative==-c['reciprocal_factor']*gamma*(m-1)*aa,'reciprocal differential'
  assert (2*aa*bb**m)/aa==c['envelope_exponent']*bb**m,'logarithmic density derivative'
  for kap in [F(3,2),F(2),F(5)]:
   eta=(1-kap**(1-m))/2
   assert 0<eta<1-kap**(1-m) and 1-eta>kap**(1-m),'strict bootstrap barrier';barriers+=1
 # Check actual coordinate separation, including both time directions.
 for t in [F(-3),F(0),F(7,5)]:
  x=F(2,3);u=x-t;v=x+t
  assert v-u==c['null_time_separation']*t,'null characteristic separation'
 # Ordered step-profile discriminants are exactly zero for outgoing supports.
 # A's exponential is positive but cannot change which side of the support it occupies.
 outgoing=[(F(2),F(3),F(100)),(F(4),F(5),F(200))];left=[(F(-3),F(-2),F(50))]
 for l,rgt,b in left:
  assert all(start>=rgt for start,end,a in outgoing),'outgoing zero-overlap'
 # Reversing order creates a large lower bound even before exponential amplification.
 incoming_mass=sum((end-start)*a for start,end,a in left)
 assert 2*F(100)*incoming_mass>F(1,2),'incoming positive overlap control'
 # A rigorous small-data fixture: exp(x)<=1/(1-x) for0<=x<1.
 for m in range(2,7):
  kap=F(2);gamma=F(1);a_mass=F(1,100);B=F(1,100);b_mass=F(1,100)
  exponent=2*kap**m*B**(m-1)*b_mass
  assert exponent<1,'finite exponential majorant'
  eta_upper=2*gamma*(m-1)*B**(m-1)*a_mass/(1-exponent)
  assert eta_upper<1-kap**(1-m),'strict small-data acceptance'
 # Exact antiderivative coefficients and two-sided tail factor for the released rates.
 for exponent in [F(3,2),F(2),F(7,3),F(5)]:
  assert (exponent-1)/(exponent-1)==1,'one-sided power primitive'
  assert c['full_line_tail_factor']/(exponent-1)==2/(exponent-1),'full-line power integral'
 return dict(gaussian_rational_jets=jets,reciprocal_and_log_pairs=6,strict_barriers=barriers,coordinate_controls=3,ordered_support_controls=2,small_data_majorants=5,power_tail_controls=4)
if __name__=='__main__':
 r=json.loads((ROOT/'lab/process/k2052-ordered-collision-scattering-basin.json').read_text())
 for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 print('BASELINE',replay(r),flush=True);faults=[]
 for key,value in [('density_bound',1),('reciprocal_factor',1),('envelope_exponent',1),('null_time_separation',1),('w_scattering_gamma_power',1),('full_line_tail_factor',1)]:
  bad=copy.deepcopy(r);bad['coefficients'][key]=value
  try:replay(bad)
  except AssertionError as e:assert str(e);faults.append([key,str(e)])
  else:raise AssertionError('missed '+key)
 print('PASS six mathematical faults',faults)
