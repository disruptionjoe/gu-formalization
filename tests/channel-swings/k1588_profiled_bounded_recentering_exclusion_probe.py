#!/usr/bin/env python3
"""Hostile mutations for K1588."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1588-profiled-bounded-recentering-exclusion.json').read_text())
def valid(x):
 q=x['bounded_recentering'];z=x['decision'];return all([x['claim_id']=='K1588','c_g N^(5/2)' in q['diverging_gap'],'o(N^(5/2))' in q['recentering_exclusion'],'K1577 remains exact' in q['class_compatibility'],'N^(5/2)=o(N^4)' in q['leading_limit_open'],'unknown true E_N' in q['scope_guard'],z['profiled_gaussian_gap_diverges'],z['profiled_bounded_error_recentering_excluded'],z['wick_dominant_class_theorem_preserved'],not z['unrestricted_leading_coefficient_identified'],not z['true_ground_bounded_recentering_decided'],not z['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1587')]+[(('bounded_recentering',k),'changed') for k in ('diverging_gap','recentering_exclusion','class_compatibility','leading_limit_open','scope_guard')]+[(('decision',k),False) for k in ('profiled_gaussian_gap_diverges','profiled_bounded_error_recentering_excluded','wick_dominant_class_theorem_preserved')]+[(('decision',k),True) for k in ('unrestricted_leading_coefficient_identified','true_ground_bounded_recentering_decided','protected_status_change')]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
