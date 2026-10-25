"""Exact zero-loss approximation constants and a low-energy supporting certificate."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,argparse
from math import floor,ceil
from k2049_wide_spacing_packing import hull
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k2053-zero-loss-effective-thermal-brackets.json'
BANK='lab/process/k2045-third-thermal-spacing-phase.json';HASH='6641419ca109d3cbbcd21014913ed22a710f9b1c2249974ba0bb593b9591a637'
def produce():
 assert hashlib.sha256((ROOT/BANK).read_bytes()).hexdigest()==HASH
 bank=json.loads((ROOT/BANK).read_text())['bank'];vals=[[(F(v['energy']),F(v['value'])) for v in c['vertices']] for c in bank]
 high=hull([(e+1,r) for vs in vals for e,r in vs]+[(F(13),F(0))]);E=F(5,2);assignments=[]
 for vs in vals:
  h=hull(vs+high+[(F(12),F(0))]);candidates=[]
  for (x,y),(z,w) in zip(h,h[1:]):
   slope=(w-y)/(z-x);a=y-slope*x
   if slope<0:candidates.append((a+slope*E,a,slope))
  value,a,slope=max(candidates);assert all(r>=a+slope*e for e,r in vs);assert all(r>=a+slope*e for e,r in high);assert a+12*slope<=0
  assignments.append([str(a),str(slope)])
 lower=min(F(a)+F(s)*E for a,s in assignments);assert lower==F(124659,450796)
 pop=[F(x,13736) for x in [5052,7578,842,109,62,93]];upper=F(7671,27472)
 controls=[]
 for energy in [F(6,5),F(5,2),F(10)]:
  for eps in [F(1,10),F(1,100),F(1,1000)]:
   N=max(floor(energy)+1,ceil(1+(energy-1)/(2*eps)));Q=(energy-1)/(N-1)
   assert N>energy and Q/2<=eps
   controls.append(dict(E=str(energy),epsilon=str(eps),N=N,D=2*N+7,Q=str(Q),alpha=str(1-Q),error=str(Q/2)))
 interval=[F(2843,1165),F(1951423,716722)];line=[F(39366,112699),-F(6561,225398)]
 for a,sl in assignments:
  assert all(F(a)+F(sl)*x>=line[0]+line[1]*x for x in interval)
 endpoints=[dict(energy='2843/1165',value='651/2330',population=[str(F(x,1165)) for x in [432,648,72,8,2,3]]),dict(energy='789/275',value='153/550',population=[str(F(x,275)) for x in [96,144,16,4,6,9]])]
 upper_slope=(F(endpoints[1]['value'])-F(endpoints[0]['value']))/(F(endpoints[1]['energy'])-F(endpoints[0]['energy']));upper_intercept=F(endpoints[0]['value'])-upper_slope*F(endpoints[0]['energy'])
 inputs=[BANK,'explorations/conditional-build/k2008-effective-thermal-dimension-approximation-2026-10-24.md','explorations/conditional-build/k2010-countable-thermal-attainment-2026-10-24.md','explorations/conditional-build/k2020-posttransition-tail-and-resources-2026-10-24.md','explorations/conditional-build/k2049-wide-spacing-packing-2026-10-25.md']
 return dict(result_id='K2053',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',coefficients=dict(error_denominator_factor=2,dimension_factor=2,dimension_offset=7,tail_normalization_numerator=1),approximation_controls=controls,formula='((N-E)/(N-1))*F_(2N+7) <= F_infinity <= F_(2N+7); gap <= (E-1)/(2*(N-1))',bank_ref=BANK,bank_sha256=HASH,energy=str(E),spacing='1/2<delta<=1',lower=str(lower),upper=str(upper),width=str(upper-lower),low_cell_assignments=assignments,witness=dict(support=[1,3,5,7,9,11],population=list(map(str,pop)),physical_spectrum=list(range(13))),interval_bracket=dict(interval=list(map(str,interval)),lower_line=list(map(str,line)),upper_line=list(map(str,[upper_intercept,upper_slope])),endpoints=endpoints),scope='Finite/countable thermal model. Improved sufficient dimension, not necessity. Nonzero-width low-energy bracket, not exact optimum. Existing bank completeness and erasure proof reused.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs})
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();r=produce()
 if args.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
 else:assert r==json.loads(OUT.read_text())
 print('PASS K2053',len(r['low_cell_assignments']),'low-cell support lines; nine dimension/error controls; exact bracket',r['lower'],r['upper'])
