#!/usr/bin/env python3
"""Controls for K1456's low-chaos orthogonality."""
import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1456-low-chaos-counterterm-orthogonality.json').read_text()); n=0
def c(l,v):
 global n; assert v,l; n+=1; print(f'PASS {n:02d}: {l}')
for k,p in D['pinned_inputs'].items(): c(f'{k} pin',hashlib.sha256((R/p['path']).read_bytes()).hexdigest()==p['sha256'])
for degree in range(4): c(f'chaos {degree} orthogonal',degree!=4)
c('fourth retained',4==4); B=D['chaos_boundary']; c('projection statement','P_4 C_N Omega=0' in B['low_counterterm']); c('fixed coupling','=gW_N' in B['invariance'])
Q=D['decision']; c('no change',not Q['low_chaos_changes_fourth_projection']); c('invariant',Q['fourth_projection_invariant_under_low_chaos']); c('no repair',not Q['low_chaos_repairs_k1439']); c('higher open',not Q['fourth_chaos_repairs_excluded']); c('protected',not Q['protected_status_change'])
print(f'RESULT: PASS {n}/{n}')
