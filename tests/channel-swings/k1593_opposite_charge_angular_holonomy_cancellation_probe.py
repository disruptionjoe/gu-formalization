#!/usr/bin/env python3
"""Hostile mutations for K1593."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1593-opposite-charge-angular-holonomy-cancellation.json').read_text())
def valid(x):
 q=x['angular_cancellation'];z=x['decision'];return all([x['claim_id']=='K1593','equal same-k amplitudes' in q['pairing_condition'],'momentum-linear terms cancel' in q['exact_sum'],'d(|a|^2)/dt' in q['exact_sum'],'int|dot a| diverges' in q['angular_consequence'],'homogeneous k=0' in q['invariant_control'],'Gauss neutrality alone' in q['scope_guard'],z['signed_species_work_identity_proved'],z['momentum_linear_terms_cancel'],z['angular_holonomy_cost_zero'],z['homogeneous_control_invariant'],not z['neutrality_alone_sufficient'],not z['global_positive_radius_proved'],not z['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1592')]+[(('angular_cancellation',k),'changed') for k in ('pairing_condition','exact_sum','angular_consequence','invariant_control','scope_guard')]+[(('decision',k),False) for k in ('signed_species_work_identity_proved','momentum_linear_terms_cancel','angular_holonomy_cost_zero','homogeneous_control_invariant')]+[(('decision',k),True) for k in ('neutrality_alone_sufficient','global_positive_radius_proved','protected_status_change')]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
