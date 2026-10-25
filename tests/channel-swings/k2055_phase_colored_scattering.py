"""Exact phase lattice, reciprocal identities and rational conservative barriers."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,argparse
ROOT=Path(__file__).resolve().parents[2]
def produce():
 controls=[]
 for m in [2,3,4]:
  for gamma in [F(1,2),F(1),F(3,2)]:
   A=B=L=S=F(1);C=2*gamma*(m-1);h=F(1,2)
   # Rational overestimate of the fractional power, valid since exponent<=2.
   x=h+C*A*S;K=(m-1)*L*max(F(1),x*x)+2*(m-1)*B
   eps=min(h,(F(m-1)/(K+1))**(m-1))
   assert eps>0 and eps<=h and eps<=(F(m-1)/(K+1))**(m-1)
   for a,b in [(F(1),F(1)),(F(3,2),F(2,3)),(F(0),F(2))]:
    ar=-2*a*b**m;bs=2*gamma*a*b**m
    assert (1-m)*b**(-m)*bs==-C*a
    assert -C*ar==2*(m-1)*bs
   controls.append(dict(m=m,gamma=str(gamma),A='1',B='1',L='1',S='1',h=str(h),K_safe=str(K),epsilon=str(eps)))
 signs=[[(-1)**(n-k) for k in [0,1,2]] for n in [0,1]]
 order=sorted([(i,j) for i in range(2) for j in range(3)],key=lambda x:(sum(x),x))
 for idx,(i,j) in enumerate(order):
  assert i==0 or (i-1,j) in order[:idx];assert j==0 or (i,j-1) in order[:idx]
 paths=['explorations/conditional-build/k2050-local-conservation-classification-2026-10-25.md','explorations/conditional-build/k2052-ordered-collision-scattering-basin-2026-10-25.md']
 return dict(result_id='K2055',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',coefficients=dict(density_factor=2,reverse_u_sign=-1,reciprocal_shift=1),phase_signs=signs,grid_order=[list(x) for x in order],barrier_controls=controls,criterion_failure=dict(m=2,gamma='1/2',amplitude='2',bump_squared_integral='1',point_b_squared='1',eta_lower='16'),scope='Finite fully incoming phase-lattice trains. Exact algebra controls; universal continuation and openness use written proof.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths})
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();r=produce();out=ROOT/'lab/process/k2055-phase-colored-scattering.json'
 if a.write:out.write_text(json.dumps(r,indent=2)+'\n')
 else:assert r==json.loads(out.read_text())
 print('PASS K2055 nine rational barriers,27 reciprocal jets,2x3 grid')
