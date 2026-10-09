#!/usr/bin/env python3
"""Hostile mutations for K1533."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1533-relative-fisher-covariance-extremality.json').read_text())
def valid(x):
 q,d=x['fisher_extremality'],x['decision']
 return all([x['claim_id']=='K1533','E_nu u=m' in q['score_identities'],'S-I' in q['score_identities'],'Cov_nu(u)>=' in q['matrix_regression'],'S+S^(-1)-2I' in q['sharp_bound'],'Gaussian N(m,S)' in q['equality'],'(1/4)I_Omega' in q['wavefunction'],'cannot lower' in q['wavefunction'],'no lower bound' in q['scope_guard'],d['all_density_fisher_covariance_bound_proved'],d['gaussian_fixed_moment_extremizer'],not d['arbitrary_phase_can_lower_cost'],not d['universal_nongaussian_wick_coercivity_proved'],not d['protected_status_change']])
def main():
 assert valid(D);mut=[(('claim_id',),'K1532'),(('fisher_extremality','score_identities'),'changed'),(('fisher_extremality','matrix_regression'),'changed'),(('fisher_extremality','sharp_bound'),'changed'),(('fisher_extremality','equality'),'changed'),(('fisher_extremality','wavefunction'),'changed'),(('fisher_extremality','scope_guard'),'changed'),(('decision','all_density_fisher_covariance_bound_proved'),False),(('decision','gaussian_fixed_moment_extremizer'),False),(('decision','arbitrary_phase_can_lower_cost'),True),(('decision','universal_nongaussian_wick_coercivity_proved'),True),(('decision','protected_status_change'),True)]
 for i,(path,value) in enumerate(mut,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(mut)}/{len(mut)}')
if __name__=='__main__':main()
