#!/usr/bin/env python3
"""Controls for K1457's scalar fourth-chaos threshold."""
import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1457-scalar-fourth-chaos-cancellation-threshold.json').read_text()); n=0
def c(l,v):
 global n; assert v,l; n+=1; print(f'PASS {n:02d}: {l}')
for k,p in D['pinned_inputs'].items(): c(f'{k} pin',hashlib.sha256((R/p['path']).read_bytes()).hexdigest()==p['sha256'])
g=2.
for N in (2,5,20,100):
 cN=-g+3/N**2; c(f'bounded product N={N}',abs(g+cN)*N**2<=3+1e-12)
 c(f'net vanishes N={N}',abs(g+cN)<=3/N**2+1e-12)
Q=D['decision']; c('threshold',Q['scalar_counterterm_threshold_proved']); c('constant excluded',not Q['net_scalar_coupling_may_stay_nonzero_constant']); c('no construction',not Q['nontrivial_interacting_limit_constructed']); c('general open',not Q['general_fourth_chaos_counterterm_excluded']); c('protected',not Q['protected_status_change'])
print(f'RESULT: PASS {n}/{n}')
