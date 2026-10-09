#!/usr/bin/env python3
"""Hostile mutations for K1607."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1607-separated-heterogeneity-coefficient-rigidity.json').read_text())
def valid(x):
 q=x['separated_class'];z=x['decision'];return all([x['claim_id']=='K1607','Fix M independent of N' in q['hypothesis'],'delta d_N' in q['hypothesis'],'sech(kappa/2)' in q['overlap_decay'],'O_g(N^4)' in q['prefactor'],'N^4 exp(-cN^3)=o(1)' in q['mixing_gain'],'h_g^prof' in q['coefficient'],'Overlapping order-one components' in q['scope_guard'],z['order_one_covariance_heterogeneity_allowed'],z['macroscopic_pairwise_separation_required'],z['fixed_component_count_required'],z['mixing_gain_exponentially_small'],z['class_coefficient_h_g_prof'],not z['overlapping_order_one_class_controlled'],not z['unrestricted_leading_coefficient_identified'],not z['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1606')]+[(('separated_class',k),'changed') for k in ('hypothesis','overlap_decay','prefactor','mixing_gain','coefficient','scope_guard')]+[(('decision',k),False) for k in ('order_one_covariance_heterogeneity_allowed','macroscopic_pairwise_separation_required','fixed_component_count_required','mixing_gain_exponentially_small','class_coefficient_h_g_prof')]+[(('decision',k),True) for k in ('overlapping_order_one_class_controlled','unrestricted_leading_coefficient_identified','protected_status_change')]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
