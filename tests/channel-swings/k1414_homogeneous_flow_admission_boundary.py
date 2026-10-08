#!/usr/bin/env python3
"""Controls for K1414's admission boundary."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1414-homogeneous-flow-admission-boundary.json').read_text()); n=0
def check(label,value):
 global n
 assert value,label; n+=1; print(f'PASS {n:02d}: {label}')
for key,pin in D['pinned_inputs'].items(): check(f'{key} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
B,U,Q=D['bridge_census'],D['distance_update'],D['decision']
check('census sum',B['row_count']==B['satisfied_count']+B['conditional_count']+B['excluded_count']+B['missing_count'])
check('census exact',(B['row_count'],B['satisfied_count'],B['conditional_count'],B['excluded_count'],B['missing_count'])==(81,56,6,15,4))
check('four new satisfied',len(B['new_satisfied_rows'])==4)
check('one new excluded',len(B['new_excluded_rows'])==1)
check('four missing',len(B['missing_rows'])==4)
check('homogeneous closure',any('homogeneous' in x for x in U['closed']))
check('PDE exclusion',any('full spatial' in x for x in U['excluded']))
check('defects sharpened',any('electric-current' in x for x in U['opened_or_sharpened']))
check('source unchanged',any('source selection' in x for x in U['unchanged']))
for key in ('homogeneous_completed_global_flow_constructed','nonlinear_time_dependent_mechanism_constructed','full_pde_leakage_classified'): check(key,Q[key])
for key in ('completed_full_pde_global_flow_constructed','full_bv_bfv_boundary_theory_constructed','positive_gu_physical_hilbert_cohomology_constructed','source_selected_reduction_constructed','k1145_k1150_candidate_counts_move','protected_status_change'): check(f'{key} fenced',not Q[key])
check('ledger unchanged','LEDGER_UNCHANGED' in D['source_and_ledger_effect'])
assert n==24,n
print('RESULT: PASS 24/24')
