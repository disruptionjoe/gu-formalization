#!/usr/bin/env python3
"""Hostile mutations for K1599."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1599-transverse-nonzero-mode-periodic-family.json').read_text())
def valid(x):
 q=x['transverse_periodic_family'];z=x['decision'];return all([x['claim_id']=='K1599','nonzero lattice k' in q['geometry'],'perpendicular' in q['geometry'],'phi_+(t,x)=phi_-(t,x)' in q['solution'],'k dot a(t)=0' in q['scalar_equations'],'Gauss densities cancel' in q['maxwell_and_gauss'],"a''+2e^2R^2a=0" in q['maxwell_and_gauss'],'D=0' in q['normal_form_control'],'Excluding only k=0 is insufficient' in q['route_consequence'],'does not exclude scattering' in q['scope_guard'],z['nonzero_mode_exact_solution'],z['gauss_neutral'],z['finite_conserved_energy'],z['harmonic_electric_l1_infinite'],not z['homogeneous_mode_exclusion_sufficient'],not z['all_dispersive_closure_excluded'],not z['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1598')]+[(('transverse_periodic_family',k),'changed') for k in ('geometry','solution','scalar_equations','maxwell_and_gauss','normal_form_control','route_consequence','scope_guard')]+[(('decision',k),False) for k in ('nonzero_mode_exact_solution','gauss_neutral','finite_conserved_energy','harmonic_electric_l1_infinite')]+[(('decision',k),True) for k in ('homogeneous_mode_exclusion_sufficient','all_dispersive_closure_excluded','protected_status_change')]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
