#!/usr/bin/env python3
"""Hostile mutations for K1589."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1589-periodic-harmonic-electric-counterexample.json').read_text())
def valid(x):
 q=x['periodic_orbit'];z=x['decision'];return all([x['claim_id']=='K1589','charges +e and -e' in q['model'],'Omega=sqrt(2)eR' in q['exact_solution'],'cancel pointwise' in q['gauss_neutrality'],'A Omega T' in q['nonintegrable_harmonic_electric'],'additional dispersion' in q['obstruction'],'two-species' in q['scope_guard'],z['exact_coupled_periodic_orbit'],z['gauss_neutral'],z['finite_conserved_energy'],z['harmonic_electric_l1_infinite'],z['energy_only_integrability_excluded'],not z['all_global_pde_closure_excluded'],not z['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1588')]+[(('periodic_orbit',k),'changed') for k in ('model','exact_solution','gauss_neutrality','nonintegrable_harmonic_electric','obstruction','scope_guard')]+[(('decision',k),False) for k in ('exact_coupled_periodic_orbit','gauss_neutral','finite_conserved_energy','harmonic_electric_l1_infinite','energy_only_integrability_excluded')]+[(('decision',k),True) for k in ('all_global_pde_closure_excluded','protected_status_change')]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
