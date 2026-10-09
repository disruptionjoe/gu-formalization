#!/usr/bin/env python3
"""Hostile mutations for K1569."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1569-two-radius-current-normal-form-boundary.json').read_text())
def valid(x):
 q,d=x['two_radius_bound'],x['decision'];return all([x['claim_id']=='K1569','G_rho=sum_' in q['analytic_energies'],'(1-(sigma/rho)^2)^(-2)' in q['nested_radius_estimate'],'B_A' in q['modified_energy_control'],'outer analytic energy' in q['combined_identity'],'sqrt(N+1)/rho' in q['same_radius_obstruction'],'does not create a same-radius coercive energy' in q['consequence'],'does not prove global coefficient integrability' in q['scope_guard'],d['two_radius_cross_term_bound_proved'],d['differentiated_current_analytic_sum_controlled_conditionally'],not d['single_radius_uniform_relative_bound_exists'],not d['k1450_radius_collapse_repaired'],not d['coercive_global_modified_energy_constructed'],not d['global_full_pde_flow_constructed'],not d['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1568')]+[(('two_radius_bound',k),'changed') for k in ('analytic_energies','nested_radius_estimate','modified_energy_control','combined_identity','same_radius_obstruction','consequence','scope_guard')]+[(('decision',k),False) for k in ('two_radius_cross_term_bound_proved','differentiated_current_analytic_sum_controlled_conditionally')]+[(('decision',k),True) for k in ('single_radius_uniform_relative_bound_exists','k1450_radius_collapse_repaired','coercive_global_modified_energy_constructed','global_full_pde_flow_constructed','protected_status_change')]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
