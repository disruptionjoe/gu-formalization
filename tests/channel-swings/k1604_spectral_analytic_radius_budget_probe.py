#!/usr/bin/env python3
"""Hostile mutations for K1604."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1604-spectral-analytic-radius-budget.json').read_text())
def valid(x):
 q=x['spectral_budget'];z=x['decision'];return all([x['claim_id']=='K1604','B_E=B_0+B_3/2' in q['definitions'],'int|a|^2<=B_E B_a' in q['definitions'],'2|e|B_a+(e^2/m)B_E B_a' in q['bare_energy'],'curvature' in q['remainder'],'B_A(t)<=|e||a(t)|+R(t)' in q['remainder'],'rho_infinity>=rho_0' in q['radius'],'<rho_0' in q['positive_budget'],'conditional on the spectral representation' in q['scope_guard'],z['d_prime_m_prime_budget_closed_conditionally'],z['bare_energy_uniform_bound_proved_conditionally'],z['positive_limiting_radius_proved_conditionally'],not z['curvature_current_remainders_derived'],not z['source_owned_global_flow_constructed'],not z['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1603')]+[(('spectral_budget',k),'changed') for k in ('definitions','bare_energy','remainder','radius','positive_budget','scope_guard')]+[(('decision',k),False) for k in ('d_prime_m_prime_budget_closed_conditionally','bare_energy_uniform_bound_proved_conditionally','positive_limiting_radius_proved_conditionally')]+[(('decision',k),True) for k in ('curvature_current_remainders_derived','source_owned_global_flow_constructed','protected_status_change')]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
