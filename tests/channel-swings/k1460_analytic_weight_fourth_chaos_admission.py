#!/usr/bin/env python3
"""Controls for K1460's joint admission boundary."""
import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1460-analytic-weight-fourth-chaos-admission.json').read_text()); n=0
def c(l,v):
 global n; assert v,l; n+=1; print(f'PASS {n:02d}: {l}')
for k,p in D['pinned_inputs'].items(): c(f'{k} pin',hashlib.sha256((R/p['path']).read_bytes()).hexdigest()==p['sha256'])
C,Q=D['bridge_census'],D['decision']; c('census sum',C['row_count']==C['satisfied_count']+C['conditional_count']+C['excluded_count']+C['missing_count'])
c('census values',(C['row_count'],C['satisfied_count'],C['conditional_count'],C['excluded_count'],C['missing_count'])==(130,81,10,35,4)); c('two satisfied',len(C['new_satisfied_rows'])==2); c('seven excluded',len(C['new_excluded_rows'])==7); c('four missing',len(C['missing_rows'])==4)
c('necessary conditions',Q['fourth_chaos_necessary_conditions_sharpened']); c('sector debt',Q['all_particle_sector_domain_debt_exposed'])
for k in ('k1450_prescription_globalized','fixed_entire_no_loss_weight_constructed','original_beta_one_hamiltonian_constructed','source_selected_reduction_constructed','k1145_k1150_candidate_counts_move','protected_status_change'): c(f'{k} fenced',not Q[k])
c('ledger unchanged','33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED' in D['source_and_ledger_effect']); c('counts unchanged','K1145/K1150 0/7' in D['source_and_ledger_effect'])
print(f'RESULT: PASS {n}/{n}')
