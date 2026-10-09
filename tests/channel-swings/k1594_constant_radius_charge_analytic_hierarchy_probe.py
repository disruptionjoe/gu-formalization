#!/usr/bin/env python3
"""Hostile mutations for K1594."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1594-constant-radius-charge-analytic-hierarchy.json').read_text())
def valid(x):
 q=x['charge_hierarchy'];z=x['decision'];return all([x['claim_id']=='K1594','only k=0 modes' in q['orbit_data'],'H_+(t)+H_-(t)=constant' in q['base_conservation'],'Q^n' in q['tier_lift'],'convergent positive charge-analytic sum' in q['analytic_sum'],'does not obstruct every cancellation-based' in q['interpretation'],'supplies no decay' in q['scope_guard'],z['base_paired_energy_conserved'],z['every_charge_tier_conserved'],z['positive_analytic_sum_conserved'],not z['k1589_universal_cancellation_no_go'],not z['global_nonlinear_flow_proved'],not z['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1593')]+[(('charge_hierarchy',k),'changed') for k in ('orbit_data','base_conservation','tier_lift','analytic_sum','interpretation','scope_guard')]+[(('decision',k),False) for k in ('base_paired_energy_conserved','every_charge_tier_conserved','positive_analytic_sum_conserved')]+[(('decision',k),True) for k in ('k1589_universal_cancellation_no_go','global_nonlinear_flow_proved','protected_status_change')]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
