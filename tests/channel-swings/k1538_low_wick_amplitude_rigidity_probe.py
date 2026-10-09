#!/usr/bin/env python3
"""Hostile mutations for K1538."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1538-low-wick-amplitude-rigidity.json').read_text())
def valid(x):
 q,d=x['amplitude_rigidity'],x['decision']
 return all([x['claim_id']=='K1538','(|phi_N|-A_N)^2=' in q['pointwise_identity'],'W_N/(3C_N)' in q['configuration_bound'],'For every probability law' in q['state_bound'],'spatial sign field' in q['interpretation'],'neither a small-ball exponent nor a Dirichlet-capacity bound' in q['scope_guard'],d['exact_amplitude_identity_proved'],d['all_configuration_bound_proved'],d['quadratic_wick_implies_order_one_amplitude_error'],not d['global_sign_selected'],not d['endpoint_capacity_computed'],not d['protected_status_change']])
def main():
 assert valid(D);mut=[(('claim_id',),'K1537'),(('amplitude_rigidity','pointwise_identity'),'changed'),(('amplitude_rigidity','configuration_bound'),'changed'),(('amplitude_rigidity','state_bound'),'changed'),(('amplitude_rigidity','interpretation'),'changed'),(('amplitude_rigidity','scope_guard'),'changed'),(('decision','exact_amplitude_identity_proved'),False),(('decision','all_configuration_bound_proved'),False),(('decision','quadratic_wick_implies_order_one_amplitude_error'),False),(('decision','global_sign_selected'),True),(('decision','endpoint_capacity_computed'),True),(('decision','protected_status_change'),True)]
 for i,(path,value) in enumerate(mut,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(mut)}/{len(mut)}')
if __name__=='__main__':main()
