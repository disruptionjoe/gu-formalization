#!/usr/bin/env python3
"""Hostile mutations for K1561."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1561-uniform-squeeze-coefficient.json').read_text())
def valid(x):
 q,d=x['uniform_squeeze'],x['decision'];return all([x['claim_id']=='K1561','0<s<=1' in q['trial'],'[3C_N(1-s)-m^2/(4g)]_+' in q['finite_cutoff_optimizer'],'(m^2/2)y_N' in q['finite_cutoff_free_cost'],'y_N^2-6C_N(1-s)y_N' in q['finite_cutoff_interaction'],'[6gC_N(1-s)-m^2/2]_+^2/(4g)' in q['finite_cutoff_total'],'-m^4/(16g)' in q['active_branch_total'],'e_g(s)' in q['leading_functional'],'upper-trial coefficient' in q['scope_guard'],d['uniform_squeeze_trial_constructed'],d['mean_optimized_at_finite_cutoff'],d['zero_mode_mass_cost_included'],d['leading_coefficient_functional_derived'],d['vacuum_endpoint_recovered'],not d['unrestricted_ground_energy_coefficient_proved'],not d['bounded_error_recentering_proved'],not d['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1560'),(('uniform_squeeze','trial'),'changed'),(('uniform_squeeze','finite_cutoff_optimizer'),'changed'),(('uniform_squeeze','finite_cutoff_free_cost'),'changed'),(('uniform_squeeze','finite_cutoff_interaction'),'changed'),(('uniform_squeeze','finite_cutoff_total'),'changed'),(('uniform_squeeze','active_branch_total'),'changed'),(('uniform_squeeze','leading_functional'),'changed'),(('uniform_squeeze','scope_guard'),'changed'),(('decision','uniform_squeeze_trial_constructed'),False),(('decision','mean_optimized_at_finite_cutoff'),False),(('decision','zero_mode_mass_cost_included'),False),(('decision','leading_coefficient_functional_derived'),False),(('decision','vacuum_endpoint_recovered'),False),(('decision','unrestricted_ground_energy_coefficient_proved'),True),(('decision','bounded_error_recentering_proved'),True),(('decision','protected_status_change'),True)]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
