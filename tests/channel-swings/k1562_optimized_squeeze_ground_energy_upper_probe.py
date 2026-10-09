#!/usr/bin/env python3
"""Hostile mutations for K1562."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1562-optimized-squeeze-ground-energy-upper.json').read_text())
def valid(x):
 q,d=x['optimized_upper'],x['decision'];return all([x['claim_id']=='K1562','c_Omega/(4s)-6g c_C^2' in q['vacuum_difference'],'c_Omega/(24c_C^2)' in q['threshold'],'48g c_C^2 s_g^2=c_Omega(s_g+1)' in q['interior_minimizer'],'h_g=c_Omega(s_g^2-3s_g+4)/(8s_g)' in q['optimized_coefficient'],'limsup_' in q['limsup'],'positive finite quartic coefficient corridor' in q['composition'],'not a phase transition of the full theory' in q['scope_guard'],d['vacuum_difference_factorized'],d['family_threshold_proved'],d['interior_minimizer_proved'],d['explicit_ground_energy_limsup_proved'],not d['vacuum_coefficient_unrestricted_upper_sharp_for_large_g'],not d['ground_energy_ratio_convergence_proved'],not d['mosco_limit_constructed'],not d['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1561'),(('optimized_upper','vacuum_difference'),'changed'),(('optimized_upper','threshold'),'changed'),(('optimized_upper','interior_minimizer'),'changed'),(('optimized_upper','optimized_coefficient'),'changed'),(('optimized_upper','limsup'),'changed'),(('optimized_upper','composition'),'changed'),(('optimized_upper','scope_guard'),'changed'),(('decision','vacuum_difference_factorized'),False),(('decision','family_threshold_proved'),False),(('decision','interior_minimizer_proved'),False),(('decision','explicit_ground_energy_limsup_proved'),False),(('decision','vacuum_coefficient_unrestricted_upper_sharp_for_large_g'),True),(('decision','ground_energy_ratio_convergence_proved'),True),(('decision','mosco_limit_constructed'),True),(('decision','protected_status_change'),True)]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
