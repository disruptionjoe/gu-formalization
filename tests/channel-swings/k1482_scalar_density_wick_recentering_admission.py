#!/usr/bin/env python3
"""Controls for K1482's protected admission replay."""
import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1482-scalar-density-wick-recentering-admission.json').read_text()); n=0
def c(l,v):
 global n; assert v,l; n+=1; print(f'PASS {n:02d}: {l}')
for key,pin in D['pinned_inputs'].items(): c(f'{key} pin',hashlib.sha256((R/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
B,Q=D['bridge_census'],D['decision']; c('census sum',B['row_count']==B['satisfied_count']+B['conditional_count']+B['excluded_count']+B['missing_count']); c('six new satisfied',len(B['new_satisfied_rows'])==6); c('four new excluded',len(B['new_excluded_rows'])==4); c('four missing',len(B['missing_rows'])==4)
for key in ('ultralocal_scalar_density_modified_energy_route_excluded','projective_wick_shift_ground_energy_tracking_excluded','projective_fixed_gaussian_mosco_route_excluded','projective_brst_mosco_route_excluded'): c(key,Q[key])
for key in ('full_spacetime_pde_repair_constructed','ground_energy_recentered_limit_constructed','source_selected_reduction_constructed','k1145_k1150_candidate_counts_move','protected_status_change'): c(f'{key} fenced',not Q[key])
S=D['source_and_ledger_effect']; c('source unchanged','SOURCE_REGISTER_UNCHANGED' in S); c('ledger unchanged','33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED' in S); c('protected claims',all(x in S for x in ('SC-ACT-01/02/06 ASSERTS','SC-META-53 UNCERTAIN','K1145/K1150 0/7')))
print(f'RESULT: PASS {n}/{n}')
