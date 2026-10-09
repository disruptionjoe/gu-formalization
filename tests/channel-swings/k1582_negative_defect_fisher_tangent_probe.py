#!/usr/bin/env python3
"""Hostile mutations for K1582."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1582-negative-defect-fisher-tangent.json').read_text())
def valid(x):
 q=x['fixed_moment_tangent'];z=x['decision'];return all([x['claim_id']=='K1582','orthogonal' in q['orthogonality'],'restore normalization, mean and covariance exactly' in q['exact_moment_correction'],'O(epsilon^2)' in q['fisher_order'],'-c_N epsilon' in q['defect_order'],'No neighborhood' in q['excluded_linear_compensation'],'fixed cutoff' in q['scope_guard'],z['negative_defect_states_constructed_locally'],z['fisher_excess_quadratic'],z['interaction_gain_linear'],z['linear_compensation_excluded'],not z['global_compensation_excluded'],not z['bounded_error_recentering'],not z['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1581')]+[(('fixed_moment_tangent',k),'changed') for k in ('orthogonality','exact_moment_correction','fisher_order','defect_order','excluded_linear_compensation','scope_guard')]+[(('decision',k),False) for k in ('negative_defect_states_constructed_locally','fisher_excess_quadratic','interaction_gain_linear','linear_compensation_excluded')]+[(('decision',k),True) for k in ('global_compensation_excluded','bounded_error_recentering','protected_status_change')]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
