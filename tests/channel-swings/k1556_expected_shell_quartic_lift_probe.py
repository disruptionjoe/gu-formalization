#!/usr/bin/env python3
"""Hostile mutations for K1556."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1556-expected-shell-quartic-lift.json').read_text())
def valid(x):
 q,d=x['expected_lift'],x['decision'];return all([x['claim_id']=='K1556','eta/(2-eta)>=eta/2' in q['threshold_probability'],'c_(alpha,eta)>0' in q['pointwise_input'],"c'_(alpha,eta)>0" in q['expected_gap'],'9C_N^2' in q['wick_scale'],'Omega_(alpha,eta)(N^4)' in q['wick_scale'],'order N^-3' in q['localized_boundary'],'requires expected fixed-ratio shell mass' in q['scope_guard'],d['threshold_probability_bound_proved'],d['expected_defect_gap_proved'],d['expected_interaction_floor_N4_proved'],not d['fisher_cost_used'],not d['all_nonconstant_sign_laws_excluded'],not d['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1555'),(('expected_lift','threshold_probability'),'changed'),(('expected_lift','pointwise_input'),'changed'),(('expected_lift','expected_gap'),'changed'),(('expected_lift','wick_scale'),'changed'),(('expected_lift','localized_boundary'),'changed'),(('expected_lift','scope_guard'),'changed'),(('decision','threshold_probability_bound_proved'),False),(('decision','expected_defect_gap_proved'),False),(('decision','expected_interaction_floor_N4_proved'),False),(('decision','fisher_cost_used'),True),(('decision','all_nonconstant_sign_laws_excluded'),True),(('decision','protected_status_change'),True)]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
