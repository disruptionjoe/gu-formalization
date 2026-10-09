#!/usr/bin/env python3
"""Hostile mutations for K1546."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1546-lamellar-endpoint-exclusion.json').read_text())
def valid(x):
 q,d=x['lamellar_exclusion'],x['decision'];return all([x['claim_id']=='K1546','Omega(N^3)' in q['quadratic_budget'],'Omega(N^4)' in q['k1541_compatible_branch'],'before any relative-Fisher' in q['capacity_position'],'non-lamellar' in q['surviving_route'],'three-dimensional' in q['scope_guard'],d['canonical_lamellar_order_N2_route_excluded'],d['k1541_lamellar_branch_has_quartic_interaction'],not d['fisher_cost_needed_for_family_exclusion'],not d['all_sign_textures_excluded'],not d['unrestricted_ground_energy_asymptotic_proved'],not d['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1545'),(('lamellar_exclusion','quadratic_budget'),'changed'),(('lamellar_exclusion','k1541_compatible_branch'),'changed'),(('lamellar_exclusion','capacity_position'),'changed'),(('lamellar_exclusion','surviving_route'),'changed'),(('lamellar_exclusion','scope_guard'),'changed'),(('decision','canonical_lamellar_order_N2_route_excluded'),False),(('decision','k1541_lamellar_branch_has_quartic_interaction'),False),(('decision','fisher_cost_needed_for_family_exclusion'),True),(('decision','all_sign_textures_excluded'),True),(('decision','unrestricted_ground_energy_asymptotic_proved'),True),(('decision','protected_status_change'),True)]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
