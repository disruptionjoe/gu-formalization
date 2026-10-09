#!/usr/bin/env python3
"""Hostile mutations for K1552."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1552-superquadratic-ground-energy.json').read_text())
def valid(x):
 q,d=x['ground_energy'],x['decision'];return all([x['claim_id']=='K1552','N^(2/3)' in q['amplitude_error'],'eta_g>0' in q['sign_shell_release'],'E_N>=c_g N^(8/3)' in q['variational_floor'],'N^(-8/3)' in q['resolvent_consequence'],'Theta_g(N^4)' in q['scope_guard'],d['order_N2_trial_excluded'],d['ground_energy_floor_N8over3_proved'],d['sub_N8over3_recenterings_excluded'],not d['matching_ground_energy_asymptotic_proved'],not d['continuum_operator_constructed'],not d['source_owned_gu_hamiltonian'],not d['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1551'),(('ground_energy','amplitude_error'),'changed'),(('ground_energy','sign_shell_release'),'changed'),(('ground_energy','variational_floor'),'changed'),(('ground_energy','resolvent_consequence'),'changed'),(('ground_energy','scope_guard'),'changed'),(('decision','order_N2_trial_excluded'),False),(('decision','ground_energy_floor_N8over3_proved'),False),(('decision','sub_N8over3_recenterings_excluded'),False),(('decision','matching_ground_energy_asymptotic_proved'),True),(('decision','continuum_operator_constructed'),True),(('decision','source_owned_gu_hamiltonian'),True),(('decision','protected_status_change'),True)]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
