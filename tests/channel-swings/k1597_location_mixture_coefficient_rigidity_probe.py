#!/usr/bin/env python3
"""Hostile mutations for K1597."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1597-location-mixture-coefficient-rigidity.json').read_text())
def valid(x):
 q=x['coefficient_rigidity'];z=x['decision'];return all([x['claim_id']=='K1597','q_0=I_Omega/4' in q['mixture_energy'],'global stationary diagonal Gaussian minimum' in q['component_lower'],'lambda_N^prof-(1/4)' in q['class_lower'],'K1591' in q['class_upper'],'inf_pi Q_N(pi)/N^4->h_g^prof' in q['coefficient'],'must leave the class' in q['route_consequence'],'class-infimum theorem' in q['scope_guard'],z['componentwise_profiled_lower_bound_used'],z['location_mixture_class_coefficient_proved'],z['arbitrary_atom_count_allowed'],not z['unrestricted_leading_coefficient_identified'],not z['bounded_error_recentering_proved'],not z['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1596')]+[(('coefficient_rigidity',k),'changed') for k in ('mixture_energy','component_lower','class_lower','class_upper','coefficient','route_consequence','scope_guard')]+[(('decision',k),False) for k in ('componentwise_profiled_lower_bound_used','location_mixture_class_coefficient_proved','arbitrary_atom_count_allowed')]+[(('decision',k),True) for k in ('unrestricted_leading_coefficient_identified','bounded_error_recentering_proved','protected_status_change')]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
