#!/usr/bin/env python3
"""Hostile mutations for K1573."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1573-moving-radius-current-absorption.json').read_text())
def valid(x):
 q,d=x['moving_radius'],x['decision'];return all([x['claim_id']=='K1573','partial_rho G_rho=(2/rho)' in q['analytic_energy'],'(epsilon/4)partial_rho G_rho' in q['parameterized_shift_bound'],'2uv<=epsilon u^2+epsilon^(-1)v^2' in q['proof'],'weight derivative' in q['radius_absorption'],"-rho'=C_mB_A/4" in q['optimized_budget'],'does not prove global coefficient integrability' in q['scope_guard'],d['parameterized_same_radius_derivative_bound_proved'],d['moving_radius_absorption_proved'],d['explicit_radius_budget_proved'],not d['outer_radius_comparison_required_for_local_moving_estimate'],not d['global_positive_radius_proved'],not d['global_full_pde_flow_constructed'],not d['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1572')]+[(('moving_radius',k),'changed') for k in ('analytic_energy','parameterized_shift_bound','proof','radius_absorption','optimized_budget','scope_guard')]+[(('decision',k),False) for k in ('parameterized_same_radius_derivative_bound_proved','moving_radius_absorption_proved','explicit_radius_budget_proved')]+[(('decision',k),True) for k in ('outer_radius_comparison_required_for_local_moving_estimate','global_positive_radius_proved','global_full_pde_flow_constructed','protected_status_change')]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
