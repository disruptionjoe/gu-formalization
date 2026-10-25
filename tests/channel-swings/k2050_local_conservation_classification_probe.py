"""Separate rational sparse-polynomial census and Gaussian-rational PDE jets."""
from fractions import Fraction as Q
from pathlib import Path
import json,hashlib,copy
from k2046_large_data_characteristic_reduction_probe import add,mul,scale,conj,power,norm
ROOT=Path(__file__).resolve().parents[2];I=(Q(0),Q(1))
def rank(rows):
 piv={}
 for row in rows:
  r={i:Q(v) for i,v in enumerate(row) if v}
  while r:
   j=min(r)
   if j not in piv:
    a=r[j];piv[j]={k:v/a for k,v in r.items()};break
   a=r[j]
   for k,v in piv[j].items():
    r[k]=r.get(k,Q(0))-a*v
    if not r[k]:r.pop(k,None)
 return len(piv)
def independent(degree,coeff,lam):
 # Each column is built directly by exponent shifts, no symbolic derivative or producer import.
 columns=[]
 for side in [0,1]:
  for i in range(degree+1):
   for j in range(degree+1-i):
    d={}
    def put(e,v):d[e]=d.get(e,Q(0))+v
    for k,c in enumerate(coeff):
     c=Q(c)
     if side==0:
      if i:put((i-1,j+1,k,0),i*c)
      if j:put((i+1,j-1,0,k),-j*c)
     elif k:
      if i:put((2,0,i-1,j+k-1),lam*k*c*i)
      if j:put((0,2,i+k-1,j-1),-lam*k*c*j)
    columns.append(d)
 exponents=set().union(*(set(c) for c in columns));return len(columns)-rank([[c.get(e,0) for c in columns] for e in sorted(exponents)])
def replay(r):
 polys={'w**4':[0,0,0,0,1],'(w-2)**3':[-8,12,-6,1],'w**4+w**2':[0,0,1,0,1],'w**2+1':[1,0,1],'w':[0,1]}
 for c in r['census']:assert independent(c['degree'],polys[c['F']],Q(c['lambda_value']))==c['nullity'],'exact coefficient rank'
 c=r['coefficients'];jets=0
 for k in range(1,9):
  z=(Q(k,3),Q(2-k,5));w=(Q(3-k,4),Q(k,7));v=(Q(k-2,5),Q(2*k,9));zv=mul(I,mul(conj(z),power(w,4)));wu=scale(-1,mul(I,mul(power(z,2),power(conj(w),3))))
  wuv=scale(-1,mul(I,add(scale(2,mul(mul(z,zv),power(conj(w),3))),scale(3,mul(power(z,2),mul(power(conj(w),2),conj(v)))))))
  ku=add(mul(conj(wu),v),mul(conj(w),wuv))[1]
  pv=add(scale(2,mul(mul(z,zv),power(conj(w),4))),scale(4,mul(power(z,2),mul(power(conj(w),3),conj(v)))))[0]
  assert ku+Q(c['derivative_current_potential'])*pv==0,'derivative current jet';jets+=1
  for n in range(1,7):
   lam=Q(2,7);zv=mul(I,mul(conj(z),power(w,n)));wu=scale(-lam*n,mul(I,mul(power(z,2),power(conj(w),n-1))))
   av=2*mul(conj(z),zv)[0];bu=2*mul(conj(w),wu)[0]
   assert av==Q(c['weighted_density_numerator'])*bu/(lam*n),'weighted density balance'
 # Real phase equations from the actual altered complex force; z=(1+i)r/sqrt2.
 # Use z=(1+i)*s, w=sqrt2*s; cancel irrational common factors algebraically.
 for n in range(1,9):
  for rr in [Q(1,2),Q(1),Q(3)]:
   lam=-Q(1,n);xdot=2*rr**(n+1);ydot=-2*lam*n*rr**(n+1)
   assert xdot==ydot==c['blowup_rate']*rr**(n+1),'bad sign force'
   inverse_power_derivative=-n*rr**(-n-1)*xdot
   assert inverse_power_derivative==-c['blowup_denominator_factor']*n,'blowup clock'
   assert 2*rr**2-2*(-lam*n)*rr**2==0,'signed density'
 for A in [Q(1),Q(2),Q(9)]:assert A*A/A**c['concentration_width_power']==1,'mass concentration scaling'
 # Higher even-power reciprocal identities and first-crossing barriers.
 barriers=0
 for m in range(2,7):
  for A,B,L,M,gamma in [(Q(1),Q(2),Q(3),Q(4),Q(1)),(Q(3,2),Q(1,3),Q(2),Q(1,5),Q(7,3))]:
   a,b=Q(2,3),Q(5,4);av=-2*a*b**m;bu=-2*gamma*a*b**m
   cu=(1-m)*b**(-m)*bu
   assert cu==c['reciprocal_factor']*gamma*(m-1)*a,'general reciprocal derivative'
   assert 2*gamma*(m-1)*av==c['repulsion_factor']*(m-1)*bu,'general repulsion derivative'
   h=B**(1-m)/2;C=2*gamma*(m-1)
   K=(m-1)*L*max(Q(1),h+C*M)**2+2*(m-1)*(gamma*A+B)
   eps=min(h,(Q(m-1)/(K+1))**(m-1))
   assert 0<eps<B**(1-m) and eps<= (Q(m-1)/(K+1))**(m-1),'positive crossing barrier'
   assert 2*(K+1)-K>0,'strict repulsion';barriers+=1
 # Mixed polynomial is a planted negative for density existence; real constants still allowed.
 assert independent(6,[0,0,1,0,1],Q(1,4))==2,'nonpower law exclusion'
 return dict(censuses=len(r['census'])+1,exact_jets=jets,weighted_balances=48,blowup_controls=24,scaling_controls=3,higher_power_barriers=barriers)
if __name__=='__main__':
 r=json.loads((ROOT/'lab/process/k2050-local-conservation-classification.json').read_text())
 for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 print('BASELINE',replay(r),flush=True);faults=[]
 for key,val in [('weighted_density_numerator',2),('derivative_current_potential','1/3'),('blowup_rate',1),('blowup_denominator_factor',1),('concentration_width_power',1),('reciprocal_factor',1),('repulsion_factor',1)]:
  bad=copy.deepcopy(r);bad['coefficients'][key]=val
  try:replay(bad)
  except AssertionError as e:assert str(e);faults.append([key,str(e)])
  else:raise AssertionError('missed '+key)
 print('PASS seven mathematical faults',faults)
