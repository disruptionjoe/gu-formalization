"""Exact Gaussian-rational force and null-jet checks, independent of producer."""
from fractions import Fraction as F
from pathlib import Path
import json,copy,hashlib
ROOT=Path(__file__).resolve().parents[2]
def add(z,w):return z[0]+w[0],z[1]+w[1]
def mul(z,w):return z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0]
def scale(k,z):return k*z[0],k*z[1]
def conj(z):return z[0],-z[1]
def power(z,n):
 r=(F(1),F(0))
 for _ in range(n):r=mul(r,z)
 return r
def norm(z):return z[0]**2+z[1]**2
def replay(r):
 q=r['coefficients'];count=0
 for sig in [-1,1]:
  for x,y in [(F(1),F(1)),(F(2,3),F(5,7)),(F(-3),F(2)),(F(0),F(3)),(F(2),F(0))]:
   z=(x,sig*x);w=(y,F(0));zp=scale(2,mul((0,1),mul(conj(z),power(w,4))));wm=scale(2,mul((0,1),mul(power(z,2),power(conj(w),3))))
   a,b=norm(z),norm(w);ap=2*mul(conj(z),zp)[0];bm=2*mul(conj(w),wm)[0]
   assert ap==4*sig*a*b*b and bm==-ap,'original force'
   if sig==-1 and b:
    av=ap/2;bu=-bm/2;cu=-bu/(b*b);cuv=2*av
    assert av==q['density']*a*b*b and cu==q['reciprocal_u']*a,'null reduction'
    assert cuv==-q['repulsion']*cu*b*b,'repulsive scalar ODE'
   count+=1
 for a0,b0,bp in [(F(3),F(2),F(-7)),(F(2,3),F(5,7),F(1,2)),(F(1),F(1),F(0))]:
  cx=-bp/b0**2;cu=2*a0;cv=cx-cu
  candidate=q['repulsion']*b0+cx+q['initial_density']*(a0+b0)
  assert candidate==cv,'initial diagonal'
 for A,B,L,M in [(F(1),F(2),F(3),F(10)),(F(8),F(5),F(0),F(2)),(F(1,3),F(1,2),F(5,7),F(40))]:
  H=1/(2*B);K=L*(H+2*M)**2+2*(A+B);m=1/(2*B+K)
  assert m<1/B and m<=H,'barrier entry'
  assert q['repulsion']/m-K==4*B+K>0,'barrier crossing sign'
 # Genuine admissible first/second jets of the original complex equations.
 z=w=(F(1),F(0));zu=wv=(F(0),F(0));zv=(F(0),F(1));wu=(F(0),F(-1))
 wuv=scale(-1,mul((0,1),add(scale(2,mul(z,zv)),scale(3,conj(wv)))))
 bu=2*mul(conj(w),wu)[0];bv=2*mul(conj(w),wv)[0];buv=2*(mul(conj(wv),wu)[0]+mul(conj(w),wuv)[0]);cuv=2*bu*bv-buv
 du=2*zu[1]-4*wu[1];dv=2*zv[1]-4*wv[1];scalar_u=-2*du
 assert cuv-scalar_u==q['phase_defect']*(du-dv)==4,'phase curvature defect'
 # At z=w=1, the real simultaneous direction (1,1) has force derivative10i.
 # The candidate Lipschitz constant must dominate it, and telescoping supplies equality.
 derivative=scale(2,mul((0,1),add((F(1),F(0)),scale(4,(F(1),F(0))))))
 assert derivative==(0,10) and q['complex_lipschitz']==derivative[1],'complex force Lipschitz'
 return dict(force_fixtures=count,initial_diagonals=3,barrier_controls=3,admissible_complex_jet=1)
if __name__=='__main__':
 r=json.loads((ROOT/'lab/process/k2046-large-data-characteristic-reduction.json').read_text())
 for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 print('BASELINE',replay(r))
 faults=[]
 for key,val in [('reciprocal_u',1),('repulsion',-2),('initial_density',2),('phase_defect',1),('complex_lipschitz',8)]:
  z=copy.deepcopy(r);z['coefficients'][key]=val
  try:replay(z)
  except AssertionError as e:assert str(e);faults.append([key,str(e)])
  else:raise AssertionError('missed '+key)
 print('PASS five mathematical coefficient faults',faults)
