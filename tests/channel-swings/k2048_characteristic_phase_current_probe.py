"""Gaussian-rational jet replay and polynomial coefficient classification controls."""
from fractions import Fraction as F
from pathlib import Path
import json,copy,hashlib
from k2046_large_data_characteristic_reduction_probe import add,mul,scale,conj,power,norm
ROOT=Path(__file__).resolve().parents[2];I=(F(0),F(1));Z=(F(0),F(0))
def poly(c,w):return tuple(sum((mul(x,power(w,j))[i] for j,x in enumerate(c)),F(0)) for i in range(2))
def real_product(a,b):
 n=max(len(a),len(b));a=a+[Z]*(n-len(a));b=b+[Z]*(n-len(b))
 return all(mul(a[j],b[k])==conj(mul(a[k],b[j])) for j in range(n) for k in range(n))
def replay(r):
 c=r['coefficients'];count=0
 fixtures=[((F(j,3),F(2-j,5)),(F(j-2,4),F(j+1,7)),(F(3-j,5),F(j,2))) for j in range(8)]
 for z,w,zu in fixtures:
  zv=mul(I,mul(conj(z),power(w,4)));wu=scale(-1,mul(I,mul(power(z,2),power(conj(w),3))))
  zuv=add(mul(I,mul(conj(zu),power(w,4))),scale(4,mul(I,mul(conj(z),mul(power(w,3),wu)))))
  J=mul(conj(z),zu)[1];jv=add(mul(conj(zv),zu),mul(conj(z),zuv))[1];assert jv==0,'current jet'
  a,b=norm(z),norm(w);au=2*mul(conj(z),zu)[0];av=2*mul(conj(z),zv)[0];auv=2*add(mul(conj(zu),zv),mul(conj(z),zuv))[0];C=mul(power(z,2),power(conj(w),4))
  assert a*auv-au*av==c['amplitude_current']*J*C[0]+c['amplitude_positive']*a**3*b**3,'amplitude jet'
  z0p=add(zu,zv);J0=mul(conj(z),z0p)[1]+c['initial_interaction']*C[0];assert J0==J,'initial diagonal current';count+=1
 # General F'/G mismatch is an actual PDE coefficient error, not a report flag.
 for z,w,zu in fixtures:
  fp=add(power(w,2),(F(2),F(1)));g=add(conj(fp),I);fv=add(power(w,3),w)
  zv=mul(I,mul(conj(z),fv));zuv=add(mul(I,mul(conj(zu),fv)),mul(mul(conj(z),power(z,2)),mul(fp,g)))
  jv=add(mul(conj(zv),zu),mul(conj(z),zuv))[1]
  assert jv==c['general_defect']*norm(z)**2*mul(fp,g)[1],'general polynomial defect'
 # Independently check the released full matched-polynomial amplitude law.
 for z,w,zu in fixtures:
  fp=add(power(w,2),(F(2),F(1)));fv=add(power(w,3),w);lam=F(3,7)
  zv=mul(I,mul(conj(z),fv));zuv=add(mul(I,mul(conj(zu),fv)),scale(lam*norm(fp)*norm(z),z))
  a=norm(z);J=mul(conj(z),zu)[1];au=2*mul(conj(z),zu)[0];av=2*mul(conj(z),zv)[0];auv=2*add(mul(conj(zu),zv),mul(conj(z),zuv))[0]
  assert a*auv-au*av==4*J*mul(power(z,2),conj(fv))[0]+c['general_amplitude']*lam*a**3*norm(fp),'matched amplitude law'
 # Actual coefficient matrices distinguish a real common multiplier from independent fits.
 for a in [[(F(1),F(2)),Z,(F(-3),F(1))],[(F(0),F(1))],[(F(2),F(0)),(F(1),F(-1))]]:
  for lam in [F(-2),F(0),F(3,7)]:
   b=[scale(lam,conj(x)) for x in a];assert real_product(a,b),'matched polynomial'
   b[0]=add(b[0],I if a[0][0] else (F(1),F(0)));assert not real_product(a,b),'unmatched polynomial control'
 # Initial flat Cauchy phase is NOT flat incoming phase when fields overlap.
 assert c['initial_interaction']==-1 and mul(conj((F(1),F(0))),Z)[1]-1==-1,'overlap correction'
 return {'exact_admissible_jet_fixtures':count,'general_defect_fixtures':8,'matched_and_unmatched_polynomial_pairs':9}
if __name__=='__main__':
 r=json.loads((ROOT/'lab/process/k2048-characteristic-phase-current.json').read_text())
 for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 print('BASELINE',replay(r));faults=[]
 for key,val in [('general_defect',2),('amplitude_current',2),('amplitude_positive',4),('initial_interaction',0),('general_amplitude',1)]:
  bad=copy.deepcopy(r);bad['coefficients'][key]=val
  try:replay(bad)
  except AssertionError as e:assert str(e);faults.append((key,str(e)))
  else:raise AssertionError('missed '+key)
 print('PASS five mathematical faults',faults)
