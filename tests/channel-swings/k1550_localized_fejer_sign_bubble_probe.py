#!/usr/bin/env python3
"""Hostile mutations for K1550."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1550-localized-fejer-sign-bubble.json').read_text())
def valid(x):
 q,d=x['fejer_bubble'],x['decision'];return all([x['claim_id']=='K1550','sqrt(3)(m-1)<=N' in q['bandlimit'],'Theta(m^(-3))' in q['sign_geometry'],'O(m^(-3))' in q['upper_scale'],'Omega(m^(-3))' in q['lower_scale'],'O(N^(-3))' in q['shell_consequence'],d['nonlamellar_bandlimited_example_constructed'],d['sign_change_defect_scale_Nminus3_proved'],not d['shell_mass_nonvanishing'],d['phase_balance_hypothesis_essential'],not d['k1549_exponent_sharpness_proved'],not d['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1549'),(('fejer_bubble','bandlimit'),'changed'),(('fejer_bubble','sign_geometry'),'changed'),(('fejer_bubble','upper_scale'),'changed'),(('fejer_bubble','lower_scale'),'changed'),(('fejer_bubble','shell_consequence'),'changed'),(('decision','nonlamellar_bandlimited_example_constructed'),False),(('decision','sign_change_defect_scale_Nminus3_proved'),False),(('decision','shell_mass_nonvanishing'),True),(('decision','phase_balance_hypothesis_essential'),False),(('decision','k1549_exponent_sharpness_proved'),True),(('decision','protected_status_change'),True)]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
