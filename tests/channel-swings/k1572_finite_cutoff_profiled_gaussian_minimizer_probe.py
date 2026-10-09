#!/usr/bin/env python3
"""Hostile mutations for K1572."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1572-finite-cutoff-profiled-gaussian-minimizer.json').read_text())
def valid(x):
 q,d=x['finite_cutoff_minimizer'],x['decision'];return all([x['claim_id']=='K1572','omega_k/sqrt(omega_k^2+kappa)' in q['fixed_variance_problem'],'kappa+3m^2=24gD_N(kappa)' in q['exact_euler_equation'],'two critical parameters' in q['exact_euler_equation'],'strictly convex' in q['uniqueness'],'kappa_(g,N)^+/N^2 tends to kappa_g' in q['coefficient_limit'],'only inside the stationary diagonal Gaussian class' in q['scope_guard'],d['finite_cutoff_fixed_variance_minimizer_proved'],d['finite_cutoff_euler_equation_proved'],d['finite_cutoff_two_critical_points_classified'],d['finite_cutoff_gaussian_global_minimizer_unique_eventually'],d['stationary_diagonal_gaussian_coefficient_convergence_proved'],not d['unrestricted_ground_energy_ratio_convergence_proved'],not d['bounded_error_recentering_proved'],not d['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1571')]+[(('finite_cutoff_minimizer',k),'changed') for k in ('fixed_variance_problem','exact_euler_equation','uniqueness','coefficient_limit','scope_guard')]+[(('decision',k),False) for k in ('finite_cutoff_fixed_variance_minimizer_proved','finite_cutoff_euler_equation_proved','finite_cutoff_two_critical_points_classified','finite_cutoff_gaussian_global_minimizer_unique_eventually','stationary_diagonal_gaussian_coefficient_convergence_proved')]+[(('decision',k),True) for k in ('unrestricted_ground_energy_ratio_convergence_proved','bounded_error_recentering_proved','protected_status_change')]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
