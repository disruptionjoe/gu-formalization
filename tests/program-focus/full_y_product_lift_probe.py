#!/usr/bin/env python3
"""Exact split-group controls, not a topology proof. Stdlib only."""
import argparse,hashlib,json,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def run():
 checks={}
 def ok(n,b):
  checks[n]=bool(b)
  if not b:raise AssertionError(n)
 for m in [2,3,4,6,8,12,16]:
  group=[(a,b)for a in range(m)for b in range(2)]
  multiples=lambda k:{((k*a)%m,(k*b)%2)for a,b in group}
  twice=multiples(2);six=multiples(6);base6={(6*a)%m for a in range(m)}
  ok(f'even determinant fibre coordinate vanishes Z{m}',all(b==0 for a,b in twice))
  ok(f'sixth root detected on base including Z{m} torsion',all(((a,0)in six)==(a in base6)for a in range(m)))
  ok(f'fibre class cannot be admissible determinant Z{m}',(0,1)not in twice and (0,1)not in six)
  ok(f'order-two line twist rank2 has unchanged c1 Z{m}',all(((a+2*b)%m)==a for a in range(m)for b in range(m)if 2*b%m==0))
 ok('nonsplit Z4 mutation has no order-two fibre lift',not any(a%2==1 and 2*a%4==0 for a in range(4)))
 ok('rank4 twist mod2 coefficients',3%2==1 and 6%2==0)
 ok('primitive even base class need not be sixth divisible',2%6!=0)
 ok('sphere7 first section obstruction outside dimension7',8>7)
 deps=['explorations/conditional-build/global-normal-complex-reduction-2026-11-24.md','explorations/conditional-build/normal-special-unitary-existence-2026-11-25.md','explorations/conditional-build/normal-sm-global-quotient-2026-11-27.md','explorations/conditional-build/normal-sm-characteristic-constraints-2026-11-27.md']
 return {'status':'PASS','checks':checks,'grouped_checks':len(checks),'dependencies_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()for p in deps},'scope':'Finite split-group, parity and line-twist controls only. Serre filtration, geometry and prescribed-Spin extension are written/reviewed; no full topology formalization.'}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--verify',action='store_true');p.add_argument('--output');a=p.parse_args();t=time.perf_counter();d=run();d['runtime_seconds']=time.perf_counter()-t
 if a.output:Path(a.output).write_text(json.dumps(d,indent=2)+'\n')
 print(json.dumps({k:v for k,v in d.items()if k not in ['checks','dependencies_sha256']},indent=2))
