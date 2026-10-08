#!/usr/bin/env python3
"""Controls for K1452's joint admission boundary."""
import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1452-dressing-hierarchy-selector-admission.json').read_text()); n=0
def c(l,v):
 global n
 assert v,l; n+=1; print(f'PASS {n:02d}: {l}')
for k,p in D['pinned_inputs'].items(): c(f'{k} pin',hashlib.sha256((R/p['path']).read_bytes()).hexdigest()==p['sha256'])
C,Q=D['bridge_census'],D['decision']
c('census sum',C['row_count']==C['satisfied_count']+C['conditional_count']+C['excluded_count']+C['missing_count'])
c('census values',(C['row_count'],C['satisfied_count'],C['conditional_count'],C['excluded_count'],C['missing_count'])==(121,79,10,28,4))
c('three satisfied',len(C['new_satisfied_rows'])==3); c('one conditional',len(C['new_conditional_rows'])==1); c('four excluded',len(C['new_excluded_rows'])==4); c('four missing',len(C['missing_rows'])==4)
c('uv control',Q['uv_softened_interacting_control_constructed']); c('hierarchy',Q['conditional_full_pde_hierarchy_constructed']); c('dependency sharpened',Q['source_normalization_dependency_sharpened'])
for k in ('original_beta_one_interacting_hamiltonian_constructed','generic_zero_harmonic_sector_invariant','completed_global_full_pde_flow_constructed','source_selected_reduction_constructed','k1145_k1150_candidate_counts_move','protected_status_change'): c(f'{k} fenced',not Q[k])
c('ledger unchanged','LEDGER_UNCHANGED' in D['source_and_ledger_effect']); c('counts unchanged','K1145/K1150 0/7' in D['source_and_ledger_effect'])
print(f'RESULT: PASS {n}/{n}')
