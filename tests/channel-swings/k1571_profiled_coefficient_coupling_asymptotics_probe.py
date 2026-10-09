#!/usr/bin/env python3
"""Hostile mutations for K1571."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1571-profiled-coefficient-coupling-asymptotics.json').read_text())
def valid(x):
 q,d=x['coupling_asymptotics'],x['decision'];return all([x['claim_id']=='K1571','pi/2' in q['cube_origin'],'1/(12pi)' in q['weak_coupling_scale'],'pi/16' in q['weak_coupling_gap'],'1/(6pi)' in q['weak_coupling_gap'],'4kappa^(-1/2)-2kappa^(-3/2)' in q['large_kappa_data'],'4sqrt(24c_C g)-4/c_C-c_Omega/2' in q['strong_coupling_scale'],'do not prove an unrestricted lower coefficient' in q['scope_guard'],d['weak_coupling_exponential_scale_proved'],d['weak_coupling_gap_constant_proved'],d['strong_coupling_square_root_scale_proved'],d['strong_coupling_constant_term_proved'],not d['unrestricted_ground_energy_coefficient_proved'],not d['bounded_error_recentering_proved'],not d['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1570')]+[(('coupling_asymptotics',k),'changed') for k in ('cube_origin','weak_coupling_scale','weak_coupling_gap','large_kappa_data','strong_coupling_scale','scope_guard')]+[(('decision',k),False) for k in ('weak_coupling_exponential_scale_proved','weak_coupling_gap_constant_proved','strong_coupling_square_root_scale_proved','strong_coupling_constant_term_proved')]+[(('decision',k),True) for k in ('unrestricted_ground_energy_coefficient_proved','bounded_error_recentering_proved','protected_status_change')]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
