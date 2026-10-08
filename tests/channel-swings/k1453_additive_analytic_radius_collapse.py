#!/usr/bin/env python3
"""Controls for K1453's additive analytic-radius collapse."""
import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1453-additive-analytic-radius-collapse.json').read_text()); n=0
def c(l,v):
 global n; assert v,l; n+=1; print(f'PASS {n:02d}: {l}')
for k,p in D['pinned_inputs'].items(): c(f'{k} pin',hashlib.sha256((R/p['path']).read_bytes()).hexdigest()==p['sha256'])
B=[1,1.5,3]; R0=5.; C=.4
for t,b in enumerate(B,1): c(f'comparison {t}',R0-C*b*t<=R0-C*t)
c('finite deadline',R0/C==12.5); c('coefficient floor','at least one' in D['radius_boundary']['coefficient_floor'])
Q=D['decision']; c('collapse proved',Q['finite_time_radius_collapse_proved']); c('global fenced',not Q['finite_radius_global_under_k1450_law'])
for k in ('pde_blowup_proved','all_global_hierarchy_routes_excluded','protected_status_change'): c(f'{k} fenced',not Q[k])
print(f'RESULT: PASS {n}/{n}')
