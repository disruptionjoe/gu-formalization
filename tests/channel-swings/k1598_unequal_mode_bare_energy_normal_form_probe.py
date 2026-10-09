#!/usr/bin/env python3
"""Hostile mutations for K1598."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1598-unequal-mode-bare-energy-normal-form.json').read_text())
def valid(x):
 q=x['bare_energy_normal_form'];z=x['decision'];return all([x['claim_id']=='K1598','D=sum_k k' in q['mode_moments'],"H_a'=-e dot(a) dot D" in q['signed_work'],'H_a=E_0-e a dot D' in q['energy_expansion'],'E_0=H_a+e a dot D' in q['normal_form'],"no dot(a) term" in q['normal_form'],"|D'|<=2E_0" in q['same_tier_bound'],'still spends holonomy amplitude' in q['scope_guard'],z['unequal_modes_allowed'],z['exact_boundary_correction'],z['harmonic_electric_variation_removed'],z['same_tier_no_derivative_loss'],not z['global_positive_radius_proved'],not z['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1597')]+[(('bare_energy_normal_form',k),'changed') for k in ('mode_moments','signed_work','energy_expansion','normal_form','same_tier_bound','scope_guard')]+[(('decision',k),False) for k in ('unequal_modes_allowed','exact_boundary_correction','harmonic_electric_variation_removed','same_tier_no_derivative_loss')]+[(('decision',k),True) for k in ('global_positive_radius_proved','protected_status_change')]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
