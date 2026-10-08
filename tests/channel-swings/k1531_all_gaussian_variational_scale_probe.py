#!/usr/bin/env python3
"""Hostile mutations for K1531."""
import json,copy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1531-all-gaussian-variational-scale.json').read_text())
def valid(x):
 q,d=x['variational_boundary'],x['decision']
 return all([x['claim_id']=='K1531','every normalized finite-cutoff Gaussian Q-space wavefunction' in q['gaussian_class'],'high integrated variance pays Omega_g(N^4)' in q['lower_boundary'],'E_N^Gauss=Theta_g(N^4)' in q['vacuum_upper'],'nonstationary or off-diagonal' in q['route_decision'],'genuinely non-Gaussian' in q['surviving_route'],'not an operator spectral or resolvent bound' in q['restricted_recentering'],'no continuum interacting BRST charge' in q['brst_transfer'],'c_gN^2 lower bound' in q['unrestricted_corridor'],d['all_finite_cutoff_gaussian_scale']=='N^4',not d['stationary_or_diagonal_assumption_required'],not d['gaussian_order_N2_trial_exists'],d['restricted_brst_transfer'],not d['unrestricted_ground_energy_asymptotic_proved'],not d['operator_resolvent_consequence_proved'],not d['protected_status_change']])
def main():
 muts=[]
 for path,value in [(('claim_id',),'K1530'),(('variational_boundary','gaussian_class'),'stationary only'),(('variational_boundary','lower_boundary'),'N2'),(('variational_boundary','vacuum_upper'),'unknown'),(('variational_boundary','route_decision'),'diagonal only'),(('variational_boundary','surviving_route'),'none survives'),(('variational_boundary','restricted_recentering'),'operator theorem'),(('variational_boundary','brst_transfer'),'full BRST'),(('variational_boundary','unrestricted_corridor'),'closed'),(('decision','all_finite_cutoff_gaussian_scale'),'N^2'),(('decision','stationary_or_diagonal_assumption_required'),True),(('decision','gaussian_order_N2_trial_exists'),True),(('decision','restricted_brst_transfer'),False),(('decision','unrestricted_ground_energy_asymptotic_proved'),True),(('decision','operator_resolvent_consequence_proved'),True),(('decision','protected_status_change'),True)]:
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;muts.append(x)
 assert valid(D)
 for i,x in enumerate(muts,1):assert not valid(x),i;print(f'PASS {i:02d}: rejected mutation')
 print(f'RESULT: PASS {len(muts)}/{len(muts)}')
if __name__=='__main__':main()
