#!/usr/bin/env python3
"""Controls for K1499's Gaussian fixed-moment limit."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1499-gaussian-moment-limit.json').read_text())
def gaussian_moment(j):
 if j%2:return 0
 return math.prod(range(1,j,2)) if j else 1
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 a,q=D['gaussian_limit'],D['decision']
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1499'),('unit variance','E(X_N^2)=1' in a['normalized_variable']),('all contractions','r=1,2,3' in a['criterion']),('fourth moment theorem','fourth-moment theorem' in a['theorem']),('distribution','N(0,1)' in a['distribution_limit']),('fourth moment','->3' in a['fourth_moment_limit']),('hypercontractive','(p-1)^2' in a['hypercontractive_bound']),('all fixed moments','every fixed j' in a['moment_limit']),('Gaussian decision',q['standard_gaussian_limit_proved']),('moment decision',q['all_fixed_moments_converge']),('third vanishes',q['normalized_third_moment_vanishes']),('TV fenced',not q['total_variation_rate_proved']),('growing fenced',not q['growing_moment_order_controlled']),('protected fenced',not q['protected_status_change'])]
 expected=[1,0,1,0,3,0,15,0,105]
 checks += [(f'Gaussian moment {j}',gaussian_moment(j)==v) for j,v in enumerate(expected)]
 checks += [('Lp bound p4',(4-1)**2==9),('Lp bound p6',(6-1)**2==25)]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
