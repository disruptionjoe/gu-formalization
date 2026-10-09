#!/usr/bin/env python3
"""Hostile mutations for K1586."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1586-profiled-gaussian-residual-chaos.json').read_text())
def valid(x):
 q=x['residual_chaos'];z=x['decision'];return all([x['claim_id']=='K1586','constant, first and second' in q['stationary_cancellation'],':eta(x)^3:' in q['exact_residual'],':eta(x)^4:' in q['exact_residual'],'96 h_N^2' in q['orthogonal_norm'],'24 int_T3' in q['orthogonal_norm'],'finite-cutoff' in q['scope_guard'],z['low_chaos_projections_cancel'],z['third_fourth_residual_exact'],z['orthogonal_norm_identity'],z['residual_nonzero'],not z['unrestricted_ground_state_identified'],not z['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1585')]+[(('residual_chaos',k),'changed') for k in ('stationary_cancellation','exact_residual','orthogonal_norm','scope_guard')]+[(('decision',k),False) for k in ('low_chaos_projections_cancel','third_fourth_residual_exact','orthogonal_norm_identity','residual_nonzero')]+[(('decision',k),True) for k in ('unrestricted_ground_state_identified','protected_status_change')]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
