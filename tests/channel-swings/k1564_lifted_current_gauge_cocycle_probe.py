#!/usr/bin/env python3
"""Hostile mutations for K1564."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1564-lifted-current-gauge-cocycle.json').read_text())
def valid(x):
 q,d=x['gauge_cocycle'],x['decision'];return all([x['claim_id']=='K1564','rho_n=e Im' in q['density'],'partial_t rho_n+div j_n=0' in q['continuity'],'time-independent residual temporal-gauge' in q['residual_gauge'],'matching charge phase' in q['residual_gauge'],'d/dt int chi rho_n' in q['boundary_cocycle'],'fix the residual gauge' in q['consequence'],'does not control int A dot partial_t j_n' in q['scope_guard'],'large non-single-valued' in q['scope_guard'],d['lifted_current_continuity_proved'],d['residual_gauge_cocycle_proved'],not d['instantaneous_gauge_invariance_proved'],d['spacetime_boundary_completion_required'],not d['differentiated_current_controlled'],not d['global_gauge_fixed'],not d['global_full_pde_flow_constructed'],not d['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1563'),(('gauge_cocycle','density'),'changed'),(('gauge_cocycle','continuity'),'changed'),(('gauge_cocycle','residual_gauge'),'changed'),(('gauge_cocycle','boundary_cocycle'),'changed'),(('gauge_cocycle','consequence'),'changed'),(('gauge_cocycle','scope_guard'),'changed'),(('decision','lifted_current_continuity_proved'),False),(('decision','residual_gauge_cocycle_proved'),False),(('decision','instantaneous_gauge_invariance_proved'),True),(('decision','spacetime_boundary_completion_required'),False),(('decision','differentiated_current_controlled'),True),(('decision','global_gauge_fixed'),True),(('decision','global_full_pde_flow_constructed'),True),(('decision','protected_status_change'),True)]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
