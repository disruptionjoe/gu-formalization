#!/usr/bin/env python3
"""Hostile mutations for K1557."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1557-quartic-ground-energy-scale.json').read_text())
def valid(x):
 q,d=x['ground_energy'],x['decision'];return all([x['claim_id']=='K1557','epsilon N^4' in q['bootstrap_assumption'],'T_N>C_sh,N/2' in q['quantitative_shell_covariance'],'r_N/C_N' in q['amplitude_error'],'kappa/12-epsilon/(9g c_C^2)' in q['sign_shell_release'],'E_nu W_N>=c1 N^4' in q['interaction_contradiction'],'E_N=Theta_g(N^4)' in q['lower_and_upper'],'E W_N=6C_N^2' in q['lower_and_upper'],'O_g(N^-4)' in q['resolvent_consequence'],'does not determine E_N to O(1)' in q['scope_guard'],d['quantitative_shell_bootstrap_proved'],d['ground_energy_scale_N4_proved'],d['vacuum_upper_scale_matches'],d['sub_N4_recenterings_excluded'],not d['ground_energy_to_bounded_error_proved'],not d['continuum_operator_constructed'],not d['source_owned_gu_hamiltonian'],not d['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1556'),(('ground_energy','bootstrap_assumption'),'changed'),(('ground_energy','quantitative_shell_covariance'),'changed'),(('ground_energy','amplitude_error'),'changed'),(('ground_energy','sign_shell_release'),'changed'),(('ground_energy','interaction_contradiction'),'changed'),(('ground_energy','lower_and_upper'),'changed'),(('ground_energy','resolvent_consequence'),'changed'),(('ground_energy','scope_guard'),'changed'),(('decision','quantitative_shell_bootstrap_proved'),False),(('decision','ground_energy_scale_N4_proved'),False),(('decision','vacuum_upper_scale_matches'),False),(('decision','sub_N4_recenterings_excluded'),False),(('decision','ground_energy_to_bounded_error_proved'),True),(('decision','continuum_operator_constructed'),True),(('decision','source_owned_gu_hamiltonian'),True),(('decision','protected_status_change'),True)]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
