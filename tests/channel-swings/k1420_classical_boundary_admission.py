#!/usr/bin/env python3
"""Controls for K1420's classical-boundary admission replay."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1420-classical-boundary-admission.json').read_text()); n=0
def check(label,value):
 global n
 assert value,label; n+=1; print(f'PASS {n:02d}: {label}')
for key,pin in D['pinned_inputs'].items(): check(f'{key} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
B,U,Q=D['bridge_census'],D['distance_update'],D['decision']
check('census sum',B['row_count']==sum(B[k] for k in ('satisfied_count','conditional_count','excluded_count','missing_count')))
check('census exact',(B['row_count'],B['satisfied_count'],B['conditional_count'],B['excluded_count'],B['missing_count'])==(86,61,6,15,4))
check('five new satisfied',len(B['new_satisfied_rows'])==5)
check('four missing',len(B['missing_rows'])==4)
check('classical closure',any('classical boundary' in x for x in U['closed']))
check('quantum sharpened',any('quantization' in x for x in U['opened_or_sharpened']))
check('PDE unchanged',any('global unbounded-charge' in x for x in U['unchanged']))
for key in ('classical_bfv_boundary_exactness_constructed','proper_stratified_classical_quotient_constructed','positive_reduced_classical_hamiltonian_constructed'): check(key,Q[key])
for key in ('completed_full_pde_global_flow_constructed','positive_gu_physical_hilbert_cohomology_constructed','source_selected_reduction_constructed','k1145_k1150_candidate_counts_move','protected_status_change'): check(f'{key} fenced',not Q[key])
check('ledger unchanged','LEDGER_UNCHANGED' in D['source_and_ledger_effect'])
print(f'RESULT: PASS {n}/{n}')
