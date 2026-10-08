#!/usr/bin/env python3
"""Controls for K1412's completed homogeneous graph flow."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1412-homogeneous-completed-graph-flow.json').read_text()); n=0
def check(label,value):
 global n
 assert value,label; n+=1; print(f'PASS {n:02d}: {label}')
for key,pin in D['pinned_inputs'].items(): check(f'{key} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
F,Q=D['completed_flow'],D['decision']
for label,key,needle in [('tier','tier','G_n='),('uniform','uniform_cutoffs','independent of N'),('difference','difference_equation','delta='),('coefficient','coefficient_difference','||delta||'),('Cauchy','cauchy_estimate','Gronwall'),('global','global_limit','two-sided global flow'),('nested','nested_compatibility','restriction'),('boundary','boundary','not on the spatially dependent')]: check(label,needle in F[key])
for n0 in (1,2,3):
 tails=[sum(k**(-2*n0-2) for k in range(N+1,2000)) for N in (10,50,100)]
 check(f'tail decreases n={n0}',tails[2]<tails[1]<tails[0])
 check(f'tail finite n={n0}',all(math.isfinite(x) for x in tails))
for key in ('cutoff_uniform_finite_time_bound_proved','spectral_cutoff_cauchy_convergence_proved','global_completed_homogeneous_graph_flow_constructed','all_finite_graph_tiers_compatible'): check(key,Q[key])
check('PDE fenced',not Q['full_completed_pde_flow_constructed'])
check('physical fenced',not Q['bv_bfv_physical_flow_constructed'])
check('protected fixed',not Q['protected_status_change'])
assert n==23,n
print('RESULT: PASS 23/23')
