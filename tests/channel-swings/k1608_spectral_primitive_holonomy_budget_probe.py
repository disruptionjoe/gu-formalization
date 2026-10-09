#!/usr/bin/env python3
"""Hostile mutations for K1608."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1608-spectral-primitive-holonomy-budget.json').read_text())
def valid(x):
 q=x['primitive_budget'];z=x['decision'];return all([x['claim_id']=='K1608','pure-point harmonic-electric sector is absent' in q['spectral_primitive'],'arbitrary constant flat holonomy' in q['spectral_primitive'],'F/omega' in q['weaker_hypothesis'],'W^{2,1}' in q['weaker_hypothesis'],'t^(-2)B_G2' in q['decay'],'B_G0+B_G2' in q['budgets'],'does not prove E_h in L1' in q['scope_guard'],z['pure_point_exclusion_retained'],z['primitive_w21_sufficient'],z['holonomy_remainder_l1_proved'],z['nonzero_asymptotic_flat_holonomy_allowed'],not z['electric_field_l1_proved'],not z['nonlinear_scattering_proved'],not z['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1607')]+[(('primitive_budget',k),'changed') for k in ('spectral_primitive','weaker_hypothesis','decay','budgets','scope_guard')]+[(('decision',k),False) for k in ('pure_point_exclusion_retained','primitive_w21_sufficient','holonomy_remainder_l1_proved','nonzero_asymptotic_flat_holonomy_allowed')]+[(('decision',k),True) for k in ('electric_field_l1_proved','nonlinear_scattering_proved','protected_status_change')]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
