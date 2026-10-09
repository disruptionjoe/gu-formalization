#!/usr/bin/env python3
"""Hostile mutations for K1596."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1596-location-mixture-fisher-sandwich.json').read_text())
def valid(x):
 q=x['location_mixture'];z=x['decision'];return all([x['claim_id']=='K1596','any probability law' in q['law'],'common K1572 profiled covariance' in q['law'],'T=S+v e_0 e_0^T' in q['moments'],'Fisher convexity' in q['convex_upper'],'K1533' in q['moment_lower'],'omega_0 v/[s_(N,0)(s_(N,0)+v)]' in q['rank_one_width'],'Theta_g(N)' in q['profiled_scale'],'Heterogeneous covariances' in q['scope_guard'],z['arbitrary_location_law_controlled'],z['exact_rank_one_width'],z['mixing_gain_at_most_order_N'],not z['heterogeneous_covariances_controlled'],not z['unrestricted_negative_defect_controlled'],not z['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1595')]+[(('location_mixture',k),'changed') for k in ('law','moments','convex_upper','moment_lower','rank_one_width','profiled_scale','scope_guard')]+[(('decision',k),False) for k in ('arbitrary_location_law_controlled','exact_rank_one_width','mixing_gain_at_most_order_N')]+[(('decision',k),True) for k in ('heterogeneous_covariances_controlled','unrestricted_negative_defect_controlled','protected_status_change')]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
