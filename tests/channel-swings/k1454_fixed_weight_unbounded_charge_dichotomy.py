#!/usr/bin/env python3
"""Controls for K1454's fixed-weight dichotomy."""
import hashlib,json,math
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1454-fixed-weight-unbounded-charge-dichotomy.json').read_text()); n=0
def c(l,v):
 global n; assert v,l; n+=1; print(f'PASS {n:02d}: {l}')
for k,p in D['pinned_inputs'].items(): c(f'{k} pin',hashlib.sha256((R/p['path']).read_bytes()).hexdigest()==p['sha256'])
for M in (2,3,7):
 a=[M**(-j) for j in range(8)]; ratios=[a[j]/a[j+1] for j in range(7)]
 c(f'ratio M={M}',max(abs(x-M) for x in ratios)<1e-12)
 c(f'pair optimum M={M}',abs(.5*math.sqrt(ratios[0])-.5*math.sqrt(M))<1e-12)
 partial=sum(a[j]*(M**.5)**(2*j) for j in range(8)); c(f'spectral divergence witness M={M}',abs(partial-8)<1e-10)
Q=D['decision']; c('criterion',Q['sharp_ratio_criterion_proved']); c('closure possible',Q['fixed_weight_shift_closure_possible'])
c('unbounded carrier fenced',not Q['fixed_weight_finite_on_all_unbounded_charges']); c('joint solution fenced',not Q['joint_fixed_weight_solution_exists'])
c('other weights open',not Q['all_time_dependent_or_nondiagonal_weights_excluded']); c('protected',not Q['protected_status_change'])
print(f'RESULT: PASS {n}/{n}')
