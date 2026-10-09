#!/usr/bin/env python3
"""Hostile mutations for K1602."""
import copy, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1602-relative-band-coefficient-stability.json').read_text())
def valid(x):
 q=x['relative_band'];z=x['decision'];return all([x['claim_id']=='K1602','(1-epsilon_N)S_N^*' in q['hypothesis'],'Cov(m_z)<=eta_N S_N^*' in q['hypothesis'],'d_N Tr[Omega(S_N^*)^(-1)]' in q['loewner_bound'],'O_g(N^4)' in q['trace_scale'],'lambda_N^prof-Delta/4' in q['energy_lower'],'h_g^prof' in q['coefficient'],'Fixed order-one heterogeneity' in q['scope_guard'],z['genuinely_heterogeneous_band_allowed'],z['arbitrary_mode_translation_covariance_allowed'],z['precision_gap_subleading_when_band_shrinks'],z['class_coefficient_h_g_prof'],not z['order_one_heterogeneity_controlled'],not z['unrestricted_coefficient_identified'],not z['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1601')]+[(('relative_band',k),'changed') for k in ('hypothesis','loewner_bound','trace_scale','energy_lower','coefficient','scope_guard')]+[(('decision',k),False) for k in ('genuinely_heterogeneous_band_allowed','arbitrary_mode_translation_covariance_allowed','precision_gap_subleading_when_band_shrinks','class_coefficient_h_g_prof')]+[(('decision',k),True) for k in ('order_one_heterogeneity_controlled','unrestricted_coefficient_identified','protected_status_change')]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
