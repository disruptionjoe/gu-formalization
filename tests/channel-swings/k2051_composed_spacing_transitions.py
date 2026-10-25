"""Exact composition of existing half, wide and superunit spacing results."""
from fractions import Fraction as Q
from pathlib import Path
import json,hashlib,argparse
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k2051-composed-spacing-transitions.json'
def produce():
 old=json.loads((ROOT/'lab/process/k2049-wide-spacing-packing.json').read_text());pieces=[]
 for p in old['pieces']:
  a,s=map(Q,p['line']);pieces.append(dict(name=p['name'],interval=p['interval'],jump_at_one=[str(Q(1,2)-a),str(-s)]))
 a,b,c=Q(21,88),Q(67,280),Q(1,2);assert b-a==Q(1,1540) and c-b==Q(73,280)
 refs=['explorations/conditional-build/k1981-wide-spacing-thermal-frontier-2026-10-23.md','explorations/conditional-build/k2010-countable-thermal-attainment-2026-10-24.md','explorations/conditional-build/k2047-fifth-thermal-spacing-phase-2026-10-25.md','lab/process/k2049-wide-spacing-packing.json']
 return dict(result_id='K2051',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',energy='7/2',regimes=[dict(spacing='delta=1/2',value=str(a),minimum_physical_levels=14),dict(spacing='1/2<delta<=1',value=str(b),minimum_physical_levels=7),dict(spacing='1<delta<=2',value=str(c),minimum_physical_levels=3),dict(spacing='delta>2',value=None,minimum_physical_levels=None)],jumps={'half':str(b-a),'one':str(c-b)},high_energy_jump_at_one=pieces,provenance='Regime theorems reused from K2047,K2049,K1981,K2010; new composition/custody correction, not newly proved wide-spacing optimum.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in refs})
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();r=produce()
 if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
 else:assert r==json.loads(OUT.read_text())
 print('PASS K2051 inherited regime composition, two exact jumps, three full energy formulas')
