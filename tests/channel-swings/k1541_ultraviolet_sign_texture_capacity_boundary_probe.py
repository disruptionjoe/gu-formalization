#!/usr/bin/env python3
"""Hostile mutations for K1541."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1541-ultraviolet-sign-texture-capacity-boundary.json').read_text())
def valid(x):
 q,d=x['sign_texture_boundary'],x['decision']
 return all([x['claim_id']=='K1541','q0[psi]<=K N^2' in q['order_N2_assumption'],'T_N>=kappa C_N/2' in q['amplitude_and_shell'],'phi_N=A_N s_phi+s_phi e_phi' in q['sign_factorization'],'kappa/12+o(1)' in q['ultraviolet_sign_mass'],'Gaussian weighted Dirichlet capacity' in q['capacity_reduction'],'8int(D_N^3+3C_ND_N^2)' in q['carre_improvement'],'O(N^(9/2))' in q['carre_improvement'],'relative transition-mass estimate' in q['scope_guard'],d['order_N2_requires_ultraviolet_sign_texture'],not d['constant_two_well_endpoint_sufficient'],d['carre_prefactor_improved_from_crude_N5_to_N9over2'],not d['relative_transition_mass_control_proved'],not d['order_N2_trial_constructed'],not d['superquadratic_capacity_lower_bound_proved'],not d['protected_status_change']])
def main():
 assert valid(D);mut=[(('claim_id',),'K1540'),(('sign_texture_boundary','order_N2_assumption'),'changed'),(('sign_texture_boundary','amplitude_and_shell'),'changed'),(('sign_texture_boundary','sign_factorization'),'changed'),(('sign_texture_boundary','ultraviolet_sign_mass'),'changed'),(('sign_texture_boundary','capacity_reduction'),'changed'),(('sign_texture_boundary','carre_improvement'),'changed'),(('sign_texture_boundary','scope_guard'),'changed'),(('decision','order_N2_requires_ultraviolet_sign_texture'),False),(('decision','constant_two_well_endpoint_sufficient'),True),(('decision','carre_prefactor_improved_from_crude_N5_to_N9over2'),False),(('decision','relative_transition_mass_control_proved'),True),(('decision','order_N2_trial_constructed'),True),(('decision','superquadratic_capacity_lower_bound_proved'),True),(('decision','protected_status_change'),True)]
 for i,(path,value) in enumerate(mut,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(mut)}/{len(mut)}')
if __name__=='__main__':main()
