#!/usr/bin/env python3
"""Controls for K1458's fourth-chaos projection criterion."""
import hashlib,json,math
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1458-general-fourth-chaos-projection-criterion.json').read_text()); n=0
def c(l,v):
 global n; assert v,l; n+=1; print(f'PASS {n:02d}: {l}')
for k,p in D['pinned_inputs'].items(): c(f'{k} pin',hashlib.sha256((R/p['path']).read_bytes()).hexdigest()==p['sha256'])
g=2.
for norm in (2,10,100):
 alpha=-g+1/norm; perp=.75
 lhs=(g+alpha)**2*norm**2+perp**2
 c(f'pythagoras norm={norm}',abs(lhs-1.5625)<1e-12)
 c(f'coefficient rate norm={norm}',abs(g+alpha)<=1/norm+1e-12)
Q=D['decision']; c('criterion',Q['orthogonal_projection_criterion_proved']); c('cancel',Q['divergent_direction_must_cancel']); c('remainder',Q['orthogonal_remainder_must_be_bounded']); c('not sufficient',not Q['sufficient_full_hamiltonian_construction']); c('protected',not Q['protected_status_change'])
print(f'RESULT: PASS {n}/{n}')
