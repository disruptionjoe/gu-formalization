#!/usr/bin/env python3
"""Hostile mutations for K1578."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1578-flat-connection-radius-budget-obstruction.json').read_text())
def valid(x):
 q,d=x['flat_connection_test'],x['decision'];return all([x['claim_id']=='K1578','E=-partial_t A=0' in q['background'],'infinity' in q['budget_divergence'],'zero Maxwell curvature' in q['finite_energy_control'],'2pi Z' in q['global_gauge_boundary'],'sufficient but not necessary' in q['consequence'],'does not disprove local' in q['scope_guard'],d['raw_B_A_global_integrability_from_energy_excluded'],not d['finite_radius_survives_raw_budget_for_all_time'],not d['generic_flat_holonomy_periodically_gauge_removable'],d['moving_radius_local_estimate_remains_valid'],not d['global_full_pde_flow_constructed'],not d['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1577')]+[(('flat_connection_test',k),'changed') for k in ('background','budget_divergence','finite_energy_control','global_gauge_boundary','consequence','scope_guard')]+[(('decision','raw_B_A_global_integrability_from_energy_excluded'),False),(('decision','finite_radius_survives_raw_budget_for_all_time'),True),(('decision','generic_flat_holonomy_periodically_gauge_removable'),True),(('decision','moving_radius_local_estimate_remains_valid'),False),(('decision','global_full_pde_flow_constructed'),True),(('decision','protected_status_change'),True)]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
