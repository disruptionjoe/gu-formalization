#!/usr/bin/env python3
"""Hostile mutations for K1576."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1576-wick-dominant-stationary-reduction.json').read_text())
def valid(x):
 q,d=x['stationary_reduction'],x['decision'];return all([x['claim_id']=='K1576','translation-invariant' in q['admitted_class'],'nonnegative' in q['admitted_class'],'K1533' in q['free_reduction'],'K1534' in q['interaction_reduction'],'Fourier diagonal' in q['stationary_diagonalization'],'infima are equal' in q['finite_cutoff_consequence'],'thin bimodal' in q['scope_guard'],d['all_density_fixed_moment_reduction_used'],d['wick_defect_sign_is_load_bearing'],d['stationary_diagonal_gaussian_infimum_matches_class'],d['material_nongaussian_class_included'],not d['unrestricted_nongaussian_lower_bound'],not d['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1575')]+[(('stationary_reduction',k),'changed') for k in ('admitted_class','free_reduction','interaction_reduction','stationary_diagonalization','finite_cutoff_consequence','scope_guard')]+[(('decision',k),False) for k in ('all_density_fixed_moment_reduction_used','wick_defect_sign_is_load_bearing','stationary_diagonal_gaussian_infimum_matches_class','material_nongaussian_class_included')]+[(('decision',k),True) for k in ('unrestricted_nongaussian_lower_bound','protected_status_change')]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
