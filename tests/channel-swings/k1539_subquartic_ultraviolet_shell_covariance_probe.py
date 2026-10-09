#!/usr/bin/env python3
"""Hostile mutations for K1539."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1539-subquartic-ultraviolet-shell-covariance.json').read_text())
def valid(x):
 q,d=x['shell_covariance'],x['decision']
 return all([x['claim_id']=='K1539','T_N=Tr(P_N Lambda S)' in q['data'],'a_N<=L N^(-2)' in q['data'],'C_sh,N/2' in q['deficit'],'delta_N^2/(4a_N T_N)' in q['matrix_bound'],'every finite-Fisher density' in q['matrix_bound'],'cN^4' in q['quartic_floor'],'T_N>C_sh,N/2' in q['necessary_covariance'],'centered shell covariance' in q['mean_guard'],'not a sufficient low-energy construction' in q['scope_guard'],d['all_density_shell_fisher_bound_proved'],d['subquartic_requires_order_CN_shell_covariance'],not d['gaussian_likelihood_required'],not d['coherent_constant_mode_can_supply_shell_covariance'],not d['order_N2_trial_constructed'],not d['protected_status_change']])
def main():
 assert valid(D);mut=[(('claim_id',),'K1538'),(('shell_covariance','data'),'changed'),(('shell_covariance','deficit'),'changed'),(('shell_covariance','matrix_bound'),'changed'),(('shell_covariance','quartic_floor'),'changed'),(('shell_covariance','necessary_covariance'),'changed'),(('shell_covariance','mean_guard'),'changed'),(('shell_covariance','scope_guard'),'changed'),(('decision','all_density_shell_fisher_bound_proved'),False),(('decision','subquartic_requires_order_CN_shell_covariance'),False),(('decision','gaussian_likelihood_required'),True),(('decision','coherent_constant_mode_can_supply_shell_covariance'),True),(('decision','order_N2_trial_constructed'),True),(('decision','protected_status_change'),True)]
 for i,(path,value) in enumerate(mut,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(mut)}/{len(mut)}')
if __name__=='__main__':main()
