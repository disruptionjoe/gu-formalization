#!/usr/bin/env python3
"""Controls for K1467's joint admission boundary."""
import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1467-null-form-wick-domain-admission.json').read_text()); n=0
def c(l,v):
 global n; assert v,l; n+=1; print(f'PASS {n:02d}: {l}')
for k,p in D['pinned_inputs'].items(): c(f'{k} pin',hashlib.sha256((R/p['path']).read_bytes()).hexdigest()==p['sha256'])
C,Q=D['bridge_census'],D['decision']; c('census sum',C['row_count']==C['satisfied_count']+C['conditional_count']+C['excluded_count']+C['missing_count']); c('census values',(C['row_count'],C['satisfied_count'],C['conditional_count'],C['excluded_count'],C['missing_count'])==(137,85,10,38,4)); c('four satisfied',len(C['new_satisfied_rows'])==4); c('three excluded',len(C['new_excluded_rows'])==3); c('four missing',len(C['missing_rows'])==4)
for k in ('normalized_null_symbol_constructed','finite_cutoff_beta_one_hamiltonian_constructed'): c(k,Q[k])
for k in ('actual_lifted_current_null_closed','beta_one_continuum_hamiltonian_constructed','interacting_brst_closed','source_selected_reduction_constructed','k1145_k1150_candidate_counts_move','protected_status_change'): c(f'{k} fenced',not Q[k])
c('ledger unchanged','33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED' in D['source_and_ledger_effect']); c('counts unchanged','K1145/K1150 0/7' in D['source_and_ledger_effect'])
print(f'RESULT: PASS {n}/{n}')
