#!/usr/bin/env python3
"""Hostile mutations for K1544."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1544-lamellar-interaction-defect.json').read_text())
def valid(x):
 q,d=x['interaction_defect'],x['decision'];return all([x['claim_id']=='K1544','N=(2R+1)M' in q['cutoff_family'],'Fourier best approximation' in q['best_approximation'],'T_R<=delta_R' in q['defect_comparison'],'9C_N^2' in q['wick_identity'],'Theta(N^3 M)' in q['family_scale'],'Omega(N^3)' in q['cubic_floor'],d['fourier_best_approximation_bound_proved'],d['optimal_wick_scaling_proved'],d['lamellar_cubic_floor_proved'],not d['order_N2_lamellar_center_constructed'],not d['all_sign_textures_excluded'],not d['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1543'),(('interaction_defect','cutoff_family'),'changed'),(('interaction_defect','best_approximation'),'changed'),(('interaction_defect','defect_comparison'),'changed'),(('interaction_defect','wick_identity'),'changed'),(('interaction_defect','family_scale'),'changed'),(('interaction_defect','cubic_floor'),'changed'),(('decision','fourier_best_approximation_bound_proved'),False),(('decision','optimal_wick_scaling_proved'),False),(('decision','lamellar_cubic_floor_proved'),False),(('decision','order_N2_lamellar_center_constructed'),True),(('decision','all_sign_textures_excluded'),True),(('decision','protected_status_change'),True)]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
