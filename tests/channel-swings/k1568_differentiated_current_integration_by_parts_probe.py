#!/usr/bin/env python3
"""Hostile mutations for K1568."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1568-differentiated-current-integration-by-parts.json').read_text())
def valid(x):
 q,d=x['current_identity'],x['decision'];return all([x['claim_id']=='K1568',q['differentiation'].count('e Im<')==3,'partial^a A_a' in q['integration_by_parts'],'electric curvature' in q['commutator'],'sqrt(H_n H_(n+1))' in q['tame_bound'],'adjacent charge tier' in q['advance'],'does not make M_n gauge invariant' in q['scope_guard'],d['differentiated_current_identity_proved'],d['covariant_integration_by_parts_proved'],d['spatial_derivative_loss_removed'],d['one_charge_shift_remains'],not d['single_tier_coercive_modified_energy_proved'],not d['global_full_pde_flow_constructed'],not d['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1567')]+[(('current_identity',k),'changed') for k in ('differentiation','integration_by_parts','commutator','tame_bound','advance','scope_guard')]+[(('decision',k),False) for k in ('differentiated_current_identity_proved','covariant_integration_by_parts_proved','spatial_derivative_loss_removed','one_charge_shift_remains')]+[(('decision',k),True) for k in ('single_tier_coercive_modified_energy_proved','global_full_pde_flow_constructed','protected_status_change')]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
