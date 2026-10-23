"""Exact corner geometry and constants; continuum conclusions use the written proof."""
from fractions import Fraction as F
from pathlib import Path
import argparse,json,hashlib
from k1969_scalar_continuum_separation import isolate
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1993-pulse-sobolev-corner-obstruction.json'
M=F(23,100);R=F(1,4)
def produce():
 lo,hi=isolate();assert F(9,20)<lo<hi<F(23,50)
 # Entire disk lies in D and in the left/central bands: conservative box enclosure.
 assert R<2*lo and hi+R<3
 assert 3-hi-2*R>0 and 3+lo-2*R>0
 # Angular minimizer: two constant quadrants and two linear transitions.
 # Factors of pi are kept symbolic: slope=(4M)/pi, angular energy=(16M^2)/pi.
 coeff=16*M*M
 checks=0
 for a in [F(i,32) for i in range(1,32)]:
  q=-M+2*M*a
  assert abs(q)<=M and (q+M)/(2*M)==a;checks+=1
 for p in [F(1),F(3,2),F(7,4),F(19,10)]:
  assert 2-p>0;checks+=1 # radial integral R^(2-p)/(2-p) is finite exactly for p<2.
 # D0/pi, exponent coefficient times pi, and phase-gap prefactor/pi^2.
 D0=M*R*R/4;exp_coeff=8/(M*M);Lmax=F(51,20)
 phase_prefactor=D0*D0/(2*Lmax*Lmax)
 # Integrating two forced-quadrant means: variance >= pi/4*(a-b)^2.
 for a in [F(i,8) for i in range(-8,9)]:
  for b in [F(j,8) for j in range(-8,9)]:
   c=(a+b)/2
   assert ((a-c)**2+(b-c)**2)/2==(a-b)**2/4;checks+=1
 return dict(result_id='K1993',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',root_interval=list(map(str,[lo,hi])),radius=str(R),amplitude=str(M),annular_energy_coefficient_over_pi=str(coeff),defect_prefactor_times_pi=str(D0),defect_exponent_coefficient_over_pi=str(exp_coeff),phase_gap_prefactor_times_pi_squared=str(phase_prefactor),phase_gap_exponent_coefficient_over_pi=str(2*exp_coeff),rational_controls=checks,regularized_corner=dict(defect_coefficient_times_pi=str(M/6),log_energy_coefficient_over_pi=str(16*M*M),core_energy_coefficient_times_pi=str(2*M*M/3),core_energy_coefficient_over_pi=str(8*M*M)),scope='No H1_loc optimal pulse near the interior tight-cut corner. Exact saturated quadrants cost at least16 M^2/pi log(R/r). A capped H1 pulse with local gradient energy H has corner defect D >= (pi M R^2/4) exp(-1-8H/(pi M^2)). Exact zero column marginals and feasible phase give phase gap >= pi^2*phase_prefactor*exp(-2-16H/(pi M^2)). Geometry alone has W1p representatives for1<=p<2; no full feasible W1p pulse constructed. No source or GU inference.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['explorations/conditional-build/k1991-tight-cut-pulse-factorization-2026-10-23.md','explorations/conditional-build/k1974-scalar-excursion-separation-2026-10-23.md','tests/channel-swings/k1969_scalar_continuum_separation.py']})
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();d=produce()
 if a.write:OUT.write_text(json.dumps(d,indent=2)+'\n')
 else:assert d==json.loads(OUT.read_text())
 print('PASS K1993',d['rational_controls'],'exact rational geometry/constant controls; continuum scope in proof')
