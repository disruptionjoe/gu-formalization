#!/usr/bin/env python3
"""Hostile mutations for K1540."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1540-sign-coherent-endpoint-exclusion.json').read_text())
def valid(x):
 q,d=x['sign_coherent_exclusion'],x['decision']
 return all([x['claim_id']=='K1540','union of the two global sign cones' in q['class'],'W_N/(3C_N)' in q['projection_bound'],'T_N=Tr(P_N Lambda S)' in q['state_shell_bound'],'q0[psi]>=cN^6' in q['quadratic_consequence'],'No normalized fixed-representation wavefunction' in q['endpoint_exclusion'],'constant-mode covariance' in q['mixture_guard'],'support hypothesis is load-bearing' in q['scope_guard'],d['global_sign_cones_excluded_at_order_N2'],d['sign_coherent_free_floor']=='N^6',not d['random_global_sign_evades_shell_test'],not d['spatially_sign_changing_states_excluded'],not d['unrestricted_ground_energy_asymptotic_proved'],not d['protected_status_change']])
def main():
 assert valid(D);mut=[(('claim_id',),'K1539'),(('sign_coherent_exclusion','class'),'changed'),(('sign_coherent_exclusion','projection_bound'),'changed'),(('sign_coherent_exclusion','state_shell_bound'),'changed'),(('sign_coherent_exclusion','quadratic_consequence'),'changed'),(('sign_coherent_exclusion','endpoint_exclusion'),'changed'),(('sign_coherent_exclusion','mixture_guard'),'changed'),(('sign_coherent_exclusion','scope_guard'),'changed'),(('decision','global_sign_cones_excluded_at_order_N2'),False),(('decision','sign_coherent_free_floor'),'N^2'),(('decision','random_global_sign_evades_shell_test'),True),(('decision','spatially_sign_changing_states_excluded'),True),(('decision','unrestricted_ground_energy_asymptotic_proved'),True),(('decision','protected_status_change'),True)]
 for i,(path,value) in enumerate(mut,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(mut)}/{len(mut)}')
if __name__=='__main__':main()
