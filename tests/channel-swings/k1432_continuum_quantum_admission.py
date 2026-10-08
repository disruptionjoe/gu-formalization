#!/usr/bin/env python3
"""Controls for K1432's continuum-quantum admission replay."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1432-continuum-quantum-admission.json').read_text()); n=0
def check(label,value):
 global n
 assert value,label; n+=1; print(f'PASS {n:02d}: {label}')
for key,pin in D['pinned_inputs'].items(): check(f'{key} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
B,Q=D['bridge_census'],D['decision']
check('census sum',B['row_count']==sum(B[k] for k in ('satisfied_count','conditional_count','excluded_count','missing_count')))
check('census exact',(B['row_count'],B['satisfied_count'],B['conditional_count'],B['excluded_count'],B['missing_count'])==(97,68,8,17,4))
check('three satisfied',len(B['new_satisfied_rows'])==3)
check('one conditional',len(B['new_conditional_rows'])==1)
check('one excluded',len(B['new_excluded_rows'])==1)
check('four missing',len(B['missing_rows'])==4)
for key in ('compatible_continuum_gaussian_representation_constructed','closed_refinement_stable_continuum_brst_cohomology_constructed','positive_free_continuum_hamiltonian_constructed','naive_quartic_cutoff_compatibility_excluded','wick_interaction_candidate_constructed'): check(key,Q[key])
for key in ('renormalized_interacting_hamiltonian_constructed','completed_full_pde_global_flow_constructed','source_selected_reduction_constructed','k1145_k1150_candidate_counts_move','protected_status_change'): check(f'{key} fenced',not Q[key])
check('ledger unchanged','LEDGER_UNCHANGED' in D['source_and_ledger_effect'])
print(f'RESULT: PASS {n}/{n}')
