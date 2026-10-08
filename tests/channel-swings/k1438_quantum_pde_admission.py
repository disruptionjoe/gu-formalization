#!/usr/bin/env python3
"""Controls for K1438's quantum/PDE admission replay."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1438-quantum-pde-admission.json').read_text()); n=0
def check(label,value):
 global n
 assert value,label; n+=1; print(f'PASS {n:02d}: {label}')
for key,pin in D['pinned_inputs'].items(): check(f'{key} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
B,Q=D['bridge_census'],D['decision']
check('census sum',B['row_count']==sum(B[k] for k in ('satisfied_count','conditional_count','excluded_count','missing_count')))
check('census exact',(B['row_count'],B['satisfied_count'],B['conditional_count'],B['excluded_count'],B['missing_count'])==(106,72,8,22,4))
check('four new satisfied',len(B['new_satisfied_rows'])==4)
check('five new excluded',len(B['new_excluded_rows'])==5)
check('four missing',len(B['missing_rows'])==4)
for key in ('three_dimensional_wick_L2_multiplication_limit_constructed','renormalized_interacting_form_or_resolvent_constructed','bounded_same_tier_normal_form_closes_full_pde','completed_full_pde_global_flow_constructed','source_selected_reduction_constructed','k1145_k1150_candidate_counts_move','protected_status_change'): check(f'{key} fenced',not Q[key])
check('surviving routes',Q['zero_harmonic_spacetime_and_hierarchy_routes_remain_open'])
check('ledger unchanged','LEDGER_UNCHANGED' in D['source_and_ledger_effect'])
check('protected rows retained','SC-META-53 UNCERTAIN' in D['source_and_ledger_effect'])
print(f'RESULT: PASS {n}/{n}')
