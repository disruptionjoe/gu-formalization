#!/usr/bin/env python3
"""Hostile mutations for K1583."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1583-moving-holonomy-energy-identity.json').read_text())
def valid(x):
 q=x['moving_holonomy'];z=x['decision'];return all([x['claim_id']=='K1583','m>0' in q['equation'],'H_a\'' in q['exact_derivative'],'2m|p|' in q['relative_bound'],'TV(a)' in q['relative_bound'],'commutes' in q['charge_hierarchy'],'static generic flat holonomy has zero cost' in q['maxwell_interpretation'],'prescribed harmonic' in q['scope_guard'],z['energy_derivative_exact'],z['amplitude_cost_removed'],z['total_variation_bound'],z['charge_tiers_controlled'],not z['coupled_nonlinear_integrability'],not z['global_positive_radius'],not z['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1582')]+[(('moving_holonomy',k),'changed') for k in ('equation','exact_derivative','relative_bound','charge_hierarchy','maxwell_interpretation','scope_guard')]+[(('decision',k),False) for k in ('energy_derivative_exact','amplitude_cost_removed','total_variation_bound','charge_tiers_controlled')]+[(('decision',k),True) for k in ('coupled_nonlinear_integrability','global_positive_radius','protected_status_change')]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
