#!/usr/bin/env python3
"""Hostile mutations for K1606."""
import copy, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1606-gaussian-mixture-missing-information.json').read_text())
def valid(x):
 q=x['missing_information'];z=x['decision'];return all([x['claim_id']=='K1606','w_i=p_i f_i/f' in q['mixture'],'u=sum_i w_i u_i' in q['score_identity'],'U-I_Omega' in q['score_identity'],'sqrt(f_i f_j)' in q['pairwise_bound'],'BC_ij' in q['gaussian_formula'],'-(U-I_Omega(nu|mu))/4' in q['energy_identity'],'fixed finite mixture' in q['scope_guard'],z['posterior_score_identity_proved'],z['exact_missing_information_identity_proved'],z['pairwise_bhattacharyya_bound_proved'],z['gaussian_pair_integral_closed_form'],not z['all_order_one_mixtures_controlled'],not z['unrestricted_leading_coefficient_identified'],not z['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1605')]+[(('missing_information',k),'changed') for k in ('mixture','score_identity','pairwise_bound','gaussian_formula','energy_identity','scope_guard')]+[(('decision',k),False) for k in ('posterior_score_identity_proved','exact_missing_information_identity_proved','pairwise_bhattacharyya_bound_proved','gaussian_pair_integral_closed_form')]+[(('decision',k),True) for k in ('all_order_one_mixtures_controlled','unrestricted_leading_coefficient_identified','protected_status_change')]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
