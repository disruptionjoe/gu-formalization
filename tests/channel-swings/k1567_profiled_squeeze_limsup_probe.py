#!/usr/bin/env python3
"""Hostile mutations for K1567."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1567-profiled-squeeze-limsup.json').read_text())
def valid(x):
 q,d=x['profiled_upper'],x['decision'];return all([x['claim_id']=='K1567','J_g(A)=F_*(A)+6gA(2c_C-A)' in q['reduced_functional'],'R(kappa_g)=24g' in q['self_consistency'],'for every g>0' in q['all_coupling_strictness'],'omega_k/sqrt(omega_k^2+kappa_g N^2)' in q['finite_cutoff_recovery'],'limsup_' in q['unrestricted_limsup'],'not a matching unrestricted lower coefficient' in q['scope_guard'],d['unique_profiled_minimizer_proved'],d['finite_cutoff_recovery_sequence_constructed'],d['vacuum_coefficient_beaten_for_every_positive_coupling'],d['uniform_family_threshold_is_not_full_gaussian_threshold'],d['explicit_unrestricted_limsup_improved'],not d['ground_energy_ratio_convergence_proved'],not d['bounded_error_recentering_proved'],not d['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1566')]+[(('profiled_upper',k),'changed') for k in ('reduced_functional','self_consistency','all_coupling_strictness','finite_cutoff_recovery','unrestricted_limsup','scope_guard')]+[(('decision',k),False) for k in ('unique_profiled_minimizer_proved','finite_cutoff_recovery_sequence_constructed','vacuum_coefficient_beaten_for_every_positive_coupling','uniform_family_threshold_is_not_full_gaussian_threshold','explicit_unrestricted_limsup_improved')]+[(('decision',k),True) for k in ('ground_energy_ratio_convergence_proved','bounded_error_recentering_proved','protected_status_change')]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
