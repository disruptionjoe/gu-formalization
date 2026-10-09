#!/usr/bin/env python3
"""Hostile mutations for K1609."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1609-primitive-radius-composition.json').read_text())
def valid(x):
 q=x['primitive_composition'];z=x['decision'];return all([x['claim_id']=='K1609','q_(sigma,k)=k-sigma e a_infinity' in q['shifted_normal_form'],'E_infinity=H_a' in q['shifted_normal_form'],'B_a=B_G0+B_G2' in q['bare_energy'],'B_A(t)<=|e||tilde a(t)|+R(t)' in q['adapted_radius'],'<rho_0' in q['positive_budget'],'conditional on the atom-free' in q['scope_guard'],z['shifted_normal_form_proved'],z['static_asymptotic_holonomy_absorbed'],z['bare_energy_uniform_bound_proved_conditionally'],z['positive_limiting_radius_proved_conditionally'],not z['electric_l1_required'],not z['curvature_current_remainders_derived'],not z['source_owned_global_flow_constructed'],not z['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1608')]+[(('primitive_composition',k),'changed') for k in ('shifted_normal_form','bare_energy','adapted_radius','positive_budget','scope_guard')]+[(('decision',k),False) for k in ('shifted_normal_form_proved','static_asymptotic_holonomy_absorbed','bare_energy_uniform_bound_proved_conditionally','positive_limiting_radius_proved_conditionally')]+[(('decision',k),True) for k in ('electric_l1_required','curvature_current_remainders_derived','source_owned_global_flow_constructed','protected_status_change')]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
