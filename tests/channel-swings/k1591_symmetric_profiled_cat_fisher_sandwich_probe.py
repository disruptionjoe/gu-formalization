#!/usr/bin/env python3
"""Hostile mutations for K1591."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1591-symmetric-profiled-cat-fisher-sandwich.json').read_text())
def valid(x):
 q=x['fisher_sandwich'];z=x['decision'];return all([x['claim_id']=='K1591','N(m,S)+N(-m,S)' in q['cat_law'],'Fisher convexity' in q['convex_upper'],'T=S+mm^T' in q['moment_lower'],'Sherman--Morrison' in q['rank_one_width'],'Theta_g(N)' in q['profiled_scale'],'symmetric two-component' in q['scope_guard'],z['fisher_convex_upper_proved'],z['fixed_moment_lower_proved'],z['rank_one_width_exact'],z['profiled_cat_gain_at_most_order_N'],not z['arbitrary_negative_defect_controlled'],not z['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1590')]+[(('fisher_sandwich',k),'changed') for k in ('cat_law','convex_upper','moment_lower','rank_one_width','profiled_scale','scope_guard')]+[(('decision',k),False) for k in ('fisher_convex_upper_proved','fixed_moment_lower_proved','rank_one_width_exact','profiled_cat_gain_at_most_order_N')]+[(('decision',k),True) for k in ('arbitrary_negative_defect_controlled','protected_status_change')]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
