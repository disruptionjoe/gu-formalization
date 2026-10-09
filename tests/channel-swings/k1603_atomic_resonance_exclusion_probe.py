#!/usr/bin/env python3
"""Hostile mutations for K1603."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1603-atomic-resonance-exclusion.json').read_text())
def valid(x):
 q=x['spectral_exclusion'];z=x['decision'];return all([x['claim_id']=='K1603','pure-point trigonometric polynomial' in q['decomposition'],'infinite time L1 norm' in q['atomic_obstruction'],'P_pp E_h=0' in q['exact_exclusion'],'W^{3,1}' in q['density_hypothesis'],'first two derivatives zero' in q['density_hypothesis'],'t^(-3)B_3' in q['decay'],'B_0+B_3/2' in q['budgets'],'B_0/2+B_3' in q['budgets'],'not derived here' in q['scope_guard'],z['pure_point_sector_excluded_by_hypothesis'],z['transverse_periodic_family_excluded'],z['electric_l1_proved_in_declared_class'],z['holonomy_amplitude_l1_proved_with_zero_limit'],not z['nonlinear_scattering_proved'],not z['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1602')]+[(('spectral_exclusion',k),'changed') for k in ('decomposition','atomic_obstruction','exact_exclusion','density_hypothesis','decay','budgets','scope_guard')]+[(('decision',k),False) for k in ('pure_point_sector_excluded_by_hypothesis','transverse_periodic_family_excluded','electric_l1_proved_in_declared_class','holonomy_amplitude_l1_proved_with_zero_limit')]+[(('decision',k),True) for k in ('nonlinear_scattering_proved','protected_status_change')]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
