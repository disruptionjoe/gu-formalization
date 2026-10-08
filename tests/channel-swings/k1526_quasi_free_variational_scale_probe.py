#!/usr/bin/env python3
"""Hostile mutations for K1526."""
import json,copy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1526-quasi-free-variational-scale.json').read_text())
def valid(x):
 q,d=x['variational_boundary'],x['decision']
 return all([x['claim_id']=='K1526','stationary translation-invariant diagonal quasi-free' in q['restricted_bottom'],'E_N^qf=Theta_g(N^4)' in q['vacuum_upper'],'genuinely non-Gaussian correlations' in q['surviving_routes'],'not an operator spectral or resolvent bound' in q['restricted_recentering'],'without constraining general BRST states' in q['brst_transfer'],'c_gN^2 lower bound' in q['unrestricted_corridor'],d['stationary_diagonal_quasi_free_scale']=='N^4',not d['coherent_or_stationary_diagonal_quasi_free_N2_trial_exists'],d['restricted_brst_transfer'],not d['unrestricted_ground_energy_asymptotic_proved'],not d['operator_resolvent_consequence_proved'],not d['protected_status_change']])
def main():
 muts=[]
 for path,value in [(('claim_id',),'K1525'),(('variational_boundary','restricted_bottom'),'all states'),(('variational_boundary','vacuum_upper'),'N2'),(('variational_boundary','surviving_routes'),'no survivors'),(('variational_boundary','restricted_recentering'),'operator theorem'),(('variational_boundary','brst_transfer'),'all BRST states'),(('variational_boundary','unrestricted_corridor'),'matching asymptotic'),(('decision','stationary_diagonal_quasi_free_scale'),'N^2'),(('decision','coherent_or_stationary_diagonal_quasi_free_N2_trial_exists'),True),(('decision','restricted_brst_transfer'),False),(('decision','unrestricted_ground_energy_asymptotic_proved'),True),(('decision','operator_resolvent_consequence_proved'),True),(('decision','protected_status_change'),True)]:
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;muts.append(x)
 assert valid(D)
 for i,x in enumerate(muts,1):assert not valid(x),i;print(f'PASS {i:02d}: rejected mutation')
 print(f'RESULT: PASS {len(muts)}/{len(muts)}')
if __name__=='__main__':main()
