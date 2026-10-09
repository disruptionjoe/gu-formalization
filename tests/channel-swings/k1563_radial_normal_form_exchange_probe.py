#!/usr/bin/env python3
"""Hostile mutations for K1563."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1563-radial-normal-form-exchange.json').read_text())
def valid(x):
 q,d=x['radial_exchange'],x['decision'];return all([x['claim_id']=='K1563','-(lambda/2)' in q['correction'],'H_n\'' in q['exact_identity'],'(|lambda|/m)' in q['same_tier_bound'],'A dot partial_t j_n' in q['combined_k1558_identity'],'partial_t|phi|^2 is removed' in q['advance'],'not a coercive gauge-invariant modified energy' in q['scope_guard'],'replacement of K1450' in q['scope_guard'],d['radial_correction_constructed'],d['radial_time_derivative_cancelled'],d['same_tier_bound_proved'],d['combined_normal_form_identity_proved'],not d['differentiated_current_controlled'],not d['coercive_modified_energy_constructed'],not d['global_full_pde_flow_constructed'],not d['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1562'),(('radial_exchange','correction'),'changed'),(('radial_exchange','exact_identity'),'changed'),(('radial_exchange','same_tier_bound'),'changed'),(('radial_exchange','combined_k1558_identity'),'changed'),(('radial_exchange','advance'),'changed'),(('radial_exchange','scope_guard'),'changed'),(('decision','radial_correction_constructed'),False),(('decision','radial_time_derivative_cancelled'),False),(('decision','same_tier_bound_proved'),False),(('decision','combined_normal_form_identity_proved'),False),(('decision','differentiated_current_controlled'),True),(('decision','coercive_modified_energy_constructed'),True),(('decision','global_full_pde_flow_constructed'),True),(('decision','protected_status_change'),True)]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
