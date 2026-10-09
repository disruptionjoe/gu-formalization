#!/usr/bin/env python3
"""Hostile mutations for K1566."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1566-profiled-stationary-squeeze-reduction.json').read_text())
def valid(x):
 q,d=x['profile_reduction'],x['decision'];return all([x['claim_id']=='K1566','A[s]=(1/2)int_Q s/r' in q['continuum_data'],'r/sqrt(r^2+kappa)' in q['fixed_variance_minimizer'],'strictly convex' in q['proof'],"F_*'(A)=-kappa(A)/2" in q['reduced_derivative'],'strictly increasing from 0 to infinity' in q['ratio_monotonicity'],'not an unrestricted lower bound' in q['scope_guard'],d['fixed_variance_profile_minimizer_proved'],d['continuum_reduction_to_one_parameter_proved'],d['profile_ratio_strictly_monotone'],d['uniform_profile_strictly_suboptimal_at_fixed_nonvacuum_variance'],not d['unrestricted_ground_energy_coefficient_proved'],not d['bounded_error_recentering_proved'],not d['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1565')]+[(('profile_reduction',k),'changed') for k in ('continuum_data','fixed_variance_minimizer','proof','reduced_derivative','ratio_monotonicity','scope_guard')]+[(('decision',k),False) for k in ('fixed_variance_profile_minimizer_proved','continuum_reduction_to_one_parameter_proved','profile_ratio_strictly_monotone','uniform_profile_strictly_suboptimal_at_fixed_nonvacuum_variance')]+[(('decision',k),True) for k in ('unrestricted_ground_energy_coefficient_proved','bounded_error_recentering_proved','protected_status_change')]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
