#!/usr/bin/env python3
"""Hostile mutations for K1554."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1554-spectral-shell-defect-gap.json').read_text())
def valid(x):
 q,d=x['spectral_gap'],x['decision'];return all([x['claim_id']=='K1554','sqrt(eta)/2' in q['shell_transfer'],'alpha^2 eta N^2/4' in q['gradient_floor'],'16delta_N/9' in q['transition_set'],'degree(g_N)<=2N' in q['outer_gradient'],'C N^2 sqrt(delta_N)' in q['inner_gradient'],'c_(alpha,eta)>0 uniformly in N' in q['defect_gap'],'nonvanishing fixed-ratio shell mass' in q['scope_guard'],d['sign_shell_transferred_to_field'],d['order_N2_gradient_floor_proved'],d['transition_and_complement_gradient_split_proved'],d['cutoff_independent_defect_gap_proved'],not d['k1549_Nminus4over3_bound_sharp'],not d['weighted_capacity_computed'],not d['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1549'),(('spectral_gap','shell_transfer'),'changed'),(('spectral_gap','gradient_floor'),'changed'),(('spectral_gap','transition_set'),'changed'),(('spectral_gap','outer_gradient'),'changed'),(('spectral_gap','inner_gradient'),'changed'),(('spectral_gap','defect_gap'),'changed'),(('spectral_gap','scope_guard'),'changed'),(('decision','sign_shell_transferred_to_field'),False),(('decision','order_N2_gradient_floor_proved'),False),(('decision','transition_and_complement_gradient_split_proved'),False),(('decision','cutoff_independent_defect_gap_proved'),False),(('decision','k1549_Nminus4over3_bound_sharp'),True),(('decision','weighted_capacity_computed'),True),(('decision','protected_status_change'),True)]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
