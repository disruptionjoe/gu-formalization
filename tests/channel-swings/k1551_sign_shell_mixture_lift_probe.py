#!/usr/bin/env python3
"""Hostile mutations for K1551."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1551-sign-shell-mixture-lift.json').read_text())
def valid(x):
 q,d=x['mixture_lift'],x['decision'];return all([x['claim_id']=='K1551','eta/(2-eta)>=eta/2' in q['threshold_probability'],'N^(-4/3)' in q['expected_conclusion'],'N^(8/3)' in q['wick_scale'],'N^(-3)' in q['fejer_boundary'],d['threshold_probability_bound_proved'],d['expected_defect_floor_proved'],d['expected_interaction_floor_N8over3_proved'],not d['fisher_cost_used'],not d['all_nonconstant_sign_laws_excluded'],not d['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1550'),(('mixture_lift','threshold_probability'),'changed'),(('mixture_lift','expected_conclusion'),'changed'),(('mixture_lift','wick_scale'),'changed'),(('mixture_lift','fejer_boundary'),'changed'),(('decision','threshold_probability_bound_proved'),False),(('decision','expected_defect_floor_proved'),False),(('decision','expected_interaction_floor_N8over3_proved'),False),(('decision','fisher_cost_used'),True),(('decision','all_nonconstant_sign_laws_excluded'),True),(('decision','protected_status_change'),True)]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
