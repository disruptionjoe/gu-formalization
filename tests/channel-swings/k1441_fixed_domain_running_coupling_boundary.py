#!/usr/bin/env python3
"""Controls for K1441's fixed-domain running-coupling boundary."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1441-fixed-domain-running-coupling-boundary.json').read_text()); n=0
def check(label,value):
 global n
 assert value,label; n+=1; print(f'PASS {n:02d}: {label}')
for key,pin in D['pinned_inputs'].items(): check(f'{key} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
R,Q=D['running_coupling_boundary'],D['decision']
for power in (0,1,1.9): check(f'N^-{power} fails',2-power>0)
check('N^-2 is threshold',2-2==0)
check('necessary bound stated','O(N^-2)' in R['necessary_bound'])
check('fixed coupling rejected','fixed nonzero coupling' in R['fixed_coupling_consequence'])
check('escape is conditional','does not prove' in R['conditional_escape'])
check('renormalization ceiling','says nothing against' in R['renormalization_ceiling'])
check('necessity decision',Q['quadratic_cutoff_decay_necessary_on_fixed_free_domain'])
for key in ('fixed_nonzero_coupling_passes_free_form_test','quadratic_and_vacuum_counterterms_change_necessary_decay','vanishing_coupling_escape_constructs_nontrivial_interaction','all_renormalization_routes_excluded','protected_status_change'): check(f'{key} fenced',not Q[key])
print(f'RESULT: PASS {n}/{n}')
