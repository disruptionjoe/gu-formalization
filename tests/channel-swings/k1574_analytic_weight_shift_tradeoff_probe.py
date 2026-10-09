#!/usr/bin/env python3
"""Hostile mutations for K1574."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1574-analytic-weight-shift-tradeoff.json').read_text())
def valid(x):
 q,d=x['weight_tradeoff'],x['decision'];return all([x['claim_id']=='K1574','if and only if' in q['criterion'],'sqrt(w_n/w_(n+1))' in q['criterion'],'C<=q' in q['criterion'],'sqrt(n+1)/rho' in q['factorial_obstruction'],'ratio is 1/rho' in q['geometric_control'],'(n+1)/rho' in q['leibniz_tradeoff'],'radius expenditure' in q['consequence'],'does not exclude all modified energies' in q['scope_guard'],d['general_weight_shift_criterion_proved'],d['factorial_same_radius_shift_excluded'],d['geometric_same_radius_shift_controlled'],not d['factorial_leibniz_and_bounded_shift_simultaneously_available'],not d['all_pde_repairs_excluded'],not d['global_full_pde_flow_constructed'],not d['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1573')]+[(('weight_tradeoff',k),'changed') for k in ('criterion','factorial_obstruction','geometric_control','leibniz_tradeoff','consequence','scope_guard')]+[(('decision',k),False) for k in ('general_weight_shift_criterion_proved','factorial_same_radius_shift_excluded','geometric_same_radius_shift_controlled')]+[(('decision',k),True) for k in ('factorial_leibniz_and_bounded_shift_simultaneously_available','all_pde_repairs_excluded','global_full_pde_flow_constructed','protected_status_change')]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
