"""Exact feasibility and three-level controls for the parametric thermal theorem."""
from fractions import Fraction as F
from pathlib import Path
from itertools import product,combinations
import argparse,json,hashlib
from k1981_wide_spacing_thermal_frontier import shell_rank
from k1950_global_catalyst_energy_certificates_probe import shell_return
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1987-thermal-spacing-parametric-frontier.json'
def feasible(d,delta,E):return d>=3 and delta>0 and delta<=2 and E>=(1 if delta<=1 else 2)
def produce():
 triples=[]
 for a,b in product(range(1,4),repeat=2):
  s=list(map(F,[0,a,a+b]));ok=shell_rank(s,[F(a)])
  assert ok==(a+b<=4)
  if ok:triples.append(dict(spectrum=list(map(str,s)),occupied=str(a),maximum_spacing=str(min(a,b)),minimum_budget=str(a)))
 assert len(triples)==6
 controls=[]
 for d in [1,2,3,4,5,10]:
  for delta in [F(1,10),F(1,2),F(1),F(1001,1000),F(3,2),F(2),F(2001,1000)]:
   for E in [F(9,10),F(1),F(3,2),F(1999,1000),F(2),F(10)]:
    ans=feasible(d,delta,E)
    actual=any(d>=3 and F(x['maximum_spacing'])>=delta and F(x['minimum_budget'])<=E for x in triples)
    assert ans==actual
    controls.append(dict(dimension=d,spacing=str(delta),budget=str(E),feasible=ans))
 returns=[]
 for t in [F(1,10),F(1,4),F(1,2),F(3,4),F(9,10)]:
  for row in triples:
   value=shell_return(t,[F(row['occupied'])],[F(1)]);assert value==F(1,2)
   returns.append(dict(t=str(t),spectrum=row['spectrum'],return_error=str(value)))
 return dict(result_id='K1987',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',three_level_spectra=triples,feasibility_controls=controls,three_level_returns=returns,scope='At fixed finite dimension, exact positive-spacing budget optimum is lower semicontinuous, left-continuous in spacing and right-continuous in budget on its feasible domain; semialgebraic with finitely many one-parameter jumps. Complete all-temperature feasibility domain and all three-level return1/2. No general higher-dimensional optimum, continuous-from-right spacing claim, rationality at arbitrary spacing, or uniform small-spacing modulus.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['explorations/conditional-build/k1978-thermal-spectral-spacing-2026-10-23.md','explorations/conditional-build/k1981-wide-spacing-thermal-frontier-2026-10-23.md','tests/channel-swings/k1981_wide_spacing_thermal_frontier.py']})
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();r=produce()
 if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
 else:assert r==json.loads(OUT.read_text())
 print('PASS K1987',len(r['three_level_spectra']),'complete three-level spectra;',len(r['feasibility_controls']),'parameter controls')
