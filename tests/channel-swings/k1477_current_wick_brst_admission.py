#!/usr/bin/env python3
"""Controls for K1477's protected admission replay."""
import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1477-current-wick-brst-admission.json').read_text()); n=0
def c(l,v):
 global n; assert v,l; n+=1; print(f'PASS {n:02d}: {l}')
for k,pin in D['pinned_inputs'].items(): c(f'{k} pin',hashlib.sha256((R/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
B,Q=D['bridge_census'],D['decision']; c('census sum',B['row_count']==B['satisfied_count']+B['conditional_count']+B['excluded_count']+B['missing_count']); c('five new satisfied',len(B['new_satisfied_rows'])==5); c('three new excluded',len(B['new_excluded_rows'])==3); c('four missing',len(B['missing_rows'])==4)
for k in ('current_conservation_transverse_boundary_closed','gaussian_entropy_localization_barrier_proved','unshifted_beta_one_resolvent_limit_excluded'): c(k,Q[k])
for k in ('ground_energy_recentered_limit_constructed','continuum_interacting_brst_closed','source_selected_reduction_constructed','k1145_k1150_candidate_counts_move','protected_status_change'): c(f'{k} fenced',not Q[k])
S=D['source_and_ledger_effect']; c('source unchanged','SOURCE_REGISTER_UNCHANGED' in S); c('ledger unchanged','33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED' in S); c('protected claims',all(x in S for x in ('SC-ACT-01/02/06 ASSERTS','SC-META-53 UNCERTAIN','K1145/K1150 0/7')))
print(f'RESULT: PASS {n}/{n}')
