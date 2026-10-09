#!/usr/bin/env python3
"""Hostile mutations for K1579."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1579-flat-connection-covariant-energy-cancellation.json').read_text())
def valid(x):
 q,d=x['covariant_cancellation'],x['decision'];return all([x['claim_id']=='K1579','D_a=grad-i e a' in q['operator'],'sqrt(|k-ea|^2+m^2)' in q['fourier_diagonalization'],'commutes' in q['charge_hierarchy'],'zero analytic radius' in q['radius_consequence'],'split harmonic flat connection' in q['next_required_structure'],'fixed static flat background' in q['scope_guard'],d['static_flat_covariant_energy_conserved'],d['charge_tier_commutation_proved'],not d['static_flat_radius_expenditure_necessary'],not d['nonlinear_harmonic_split_closed'],not d['global_positive_analytic_radius'],not d['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1578')]+[(('covariant_cancellation',k),'changed') for k in ('operator','fourier_diagonalization','charge_hierarchy','radius_consequence','next_required_structure','scope_guard')]+[(('decision',k),False) for k in ('static_flat_covariant_energy_conserved','charge_tier_commutation_proved')]+[(('decision',k),True) for k in ('static_flat_radius_expenditure_necessary','nonlinear_harmonic_split_closed','global_positive_analytic_radius','protected_status_change')]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
