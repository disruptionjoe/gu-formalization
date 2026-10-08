#!/usr/bin/env python3
"""Controls for K1444's joint admission boundary."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1444-form-phase-admission.json').read_text()); n=0
def check(label,value):
 global n
 assert value,label; n+=1; print(f'PASS {n:02d}: {label}')
for key,pin in D['pinned_inputs'].items(): check(f'{key} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
C,Q=D['bridge_census'],D['decision']
check('census total',C['row_count']==C['satisfied_count']+C['conditional_count']+C['excluded_count']+C['missing_count'])
check('census values',(C['row_count'],C['satisfied_count'],C['conditional_count'],C['excluded_count'],C['missing_count'])==(113,76,9,24,4))
check('four new satisfied',len(C['new_satisfied_rows'])==4)
check('one new conditional',len(C['new_conditional_rows'])==1)
check('two new excluded',len(C['new_excluded_rows'])==2)
check('four missing preserved',len(C['missing_rows'])==4)
check('higher-tier scalar consequence',Q['higher_tier_scalar_cauchy_consequence_constructed'])
for key in ('fixed_free_domain_interacting_form_constructed','all_interacting_resolvent_routes_excluded','strict_zero_harmonic_exact_resonance_present','same_tier_zero_harmonic_normal_form_constructed','completed_full_pde_global_flow_constructed','source_selected_reduction_constructed','k1145_k1150_candidate_counts_move','protected_status_change'): check(f'{key} fenced',not Q[key])
check('ledger unchanged','LEDGER_UNCHANGED' in D['source_and_ledger_effect'])
check('counts unchanged','K1145/K1150 0/7' in D['source_and_ledger_effect'])
print(f'RESULT: PASS {n}/{n}')
