"""Exact resource controls; continuum proofs are in the accompanying note."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,argparse
ROOT=Path(__file__).resolve().parents[2]
def produce():
 refs=['lab/process/k2067-sector-preserving-pointer-control.json','lab/process/k2069-causal-budget-pointer.json']
 eta=F(1,100);L=F(2400);T=F(30);rho=F(1);visibility=F(183,200)
 assert F(51,4)<16 and F(20)+4==24
 count=2
 for chi in [F(i,12) for i in range(13)]:
  a=1-chi/3;b=chi/3
  for n in [F(j,7) for j in range(-7,8)]:
   assert max(abs(s*a+t*b*n) for s in [-1,1] for t in [-1,1])<=1
   assert min(abs(s*a+t*b*n) for s in [-1,1] for t in [-1,1])>=F(1,3)
   count+=2
 assert 24/L==eta
 lower=2*F(7,5)*visibility**2-32*eta-16*eta**2
 assert F(7,5)**2<2 and lower>2;count+=3
 return dict(id='K2071',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in refs},eta=str(eta),initial_radius=str(L),duration=str(T),ramp_width=str(rho),control_radius=str(L+T+2*rho),detector_radius=str(L+T),strict_center_separation=str(2*(L+T+2*rho)+T),state_error=str(2*eta),sector_leakage_probability=str(4*eta**2),no_click_probability=str(eta**2),bell_rational_lower=str(lower),finite_exact_controls=count,scope='prepared-subspace approximation only; no exact sector or source detector field')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();d=produce();dest=ROOT/'lab/process/k2071-confined-pointer-control.json'
 if a.write:dest.write_text(json.dumps(d,indent=2)+'\n')
 else:assert json.loads(dest.read_text())==d
 print('PASS',d['finite_exact_controls'],'finite resource controls; Bell rational lower',d['bell_rational_lower'])
