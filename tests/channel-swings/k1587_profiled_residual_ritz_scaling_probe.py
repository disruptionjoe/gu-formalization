#!/usr/bin/env python3
"""Hostile mutations for K1587."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1587-profiled-residual-ritz-scaling.json').read_text())
def valid(x):
 q=x['ritz_scaling'];z=x['decision'];return all([x['claim_id']=='K1587','Gamma_N^3=Theta_g(N^3)' in q['convolution_scales'],'Gamma_N^4=Theta_g(N^5)' in q['convolution_scales'],'sigma_N=Theta_g(N^(5/2))' in q['residual_scale'],'hypercontractivity' in q['second_diagonal'],'Delta_N=Theta_g(N^(5/2))' in q['ritz_gap'],'o(N^4)' in q['coefficient_ceiling'],z['covariance_convolution_scales_proved'],z['residual_norm_n_five_halves'],z['ritz_second_diagonal_controlled'],z['ritz_gap_n_five_halves'],not z['leading_n_four_coefficient_changed'],not z['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1586')]+[(('ritz_scaling',k),'changed') for k in ('convolution_scales','residual_scale','second_diagonal','ritz_gap','coefficient_ceiling')]+[(('decision',k),False) for k in ('covariance_convolution_scales_proved','residual_norm_n_five_halves','ritz_second_diagonal_controlled','ritz_gap_n_five_halves')]+[(('decision',k),True) for k in ('leading_n_four_coefficient_changed','protected_status_change')]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
