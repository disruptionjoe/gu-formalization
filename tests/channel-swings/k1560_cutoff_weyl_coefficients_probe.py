#!/usr/bin/env python3
"""Hostile mutations for K1560."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1560-cutoff-weyl-coefficients.json').read_text())
def valid(x):
 q,d=x['weyl_coefficients'],x['decision'];return all([x['claim_id']=='K1560','||k||_infinity<=N' in q['cutoff'],'12 log((1+sqrt(3))/sqrt(2))-pi' in q['covariance_sum'],'2sqrt(3)+8 log((1+sqrt(3))/sqrt(2))-pi/3' in q['frequency_trace'],'[-1,1]^3' in q['proof_route'],'no extra factor two' in q['real_mode_guard'],'not a source normalization' in q['scope_guard'],d['covariance_cube_coefficient_proved'],d['frequency_trace_cube_coefficient_proved'],d['real_mode_counting_fixed'],not d['bounded_error_expansion_proved'],not d['source_normalization_selected'],not d['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1559'),(('weyl_coefficients','cutoff'),'changed'),(('weyl_coefficients','covariance_sum'),'changed'),(('weyl_coefficients','frequency_trace'),'changed'),(('weyl_coefficients','proof_route'),'changed'),(('weyl_coefficients','real_mode_guard'),'changed'),(('weyl_coefficients','scope_guard'),'changed'),(('decision','covariance_cube_coefficient_proved'),False),(('decision','frequency_trace_cube_coefficient_proved'),False),(('decision','real_mode_counting_fixed'),False),(('decision','bounded_error_expansion_proved'),True),(('decision','source_normalization_selected'),True),(('decision','protected_status_change'),True)]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
