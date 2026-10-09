#!/usr/bin/env python3
"""Hostile mutations for K1592."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1592-negative-defect-cat-coefficient-rigidity.json').read_text())
def valid(x):
 q=x['cat_coefficient'];z=x['decision'];return all([x['claim_id']=='K1592','-2h_N^4' in q['negative_defect'],'Wick quartic is even' in q['interaction_identity'],'Q_N^cat/N^4->h_g^prof' in q['coefficient'],'Theta_g(N^(5/2))' in q['coefficient'],'one exact nonperturbative cat family' in q['scope_guard'],z['leading_negative_defect_exact'],z['cat_interaction_equals_component'],z['profiled_cat_coefficient_rigid'],not z['cat_explains_residual_ritz_scale'],not z['unrestricted_leading_coefficient_identified'],not z['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1591')]+[(('cat_coefficient',k),'changed') for k in ('negative_defect','interaction_identity','coefficient','scope_guard')]+[(('decision',k),False) for k in ('leading_negative_defect_exact','cat_interaction_equals_component','profiled_cat_coefficient_rigid')]+[(('decision',k),True) for k in ('cat_explains_residual_ritz_scale','unrestricted_leading_coefficient_identified','protected_status_change')]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
