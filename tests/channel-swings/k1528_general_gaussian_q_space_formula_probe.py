#!/usr/bin/env python3
"""Hostile mutations for K1528."""
import json,copy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1528-general-gaussian-q-space-formula.json').read_text())
def valid(x):
 q,d=x['general_gaussian_formula'],x['decision']
 return all([x['claim_id']=='K1528','positive-definite covariance' in q['trial_class'],'det(S)^(-1/2)' in q['density'],'grad log psi=(1/2)' in q['logarithmic_gradient'],'Tr[Omega(S+S^(-1)-2I)]' in q['exact_amplitude_cost'],'(I-S)S^(-1)(I-S)' in q['matrix_positivity'],'without requiring [S,Omega]=0' in q['matrix_positivity'],'cannot lower' in q['phase_guard'],'finite-cutoff Gaussian Q-space wavefunctions' in q['scope_guard'],d['arbitrary_positive_covariance_formula_proved'],d['off_diagonal_covariance_included'],not d['gaussian_phase_can_lower_cost'],not d['nongaussian_classified'],not d['protected_status_change']])
def main():
 muts=[]
 for path,value in [(('claim_id',),'K1527'),(('general_gaussian_formula','trial_class'),'diagonal only'),(('general_gaussian_formula','density'),'unnormalized'),(('general_gaussian_formula','logarithmic_gradient'),'missing half'),(('general_gaussian_formula','exact_amplitude_cost'),'wrong trace'),(('general_gaussian_formula','matrix_positivity'),'requires commuting'),(('general_gaussian_formula','phase_guard'),'phase lowers'),(('general_gaussian_formula','scope_guard'),'all states'),(('decision','arbitrary_positive_covariance_formula_proved'),False),(('decision','off_diagonal_covariance_included'),False),(('decision','gaussian_phase_can_lower_cost'),True),(('decision','nongaussian_classified'),True),(('decision','protected_status_change'),True)]:
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;muts.append(x)
 assert valid(D)
 for i,x in enumerate(muts,1):assert not valid(x),i;print(f'PASS {i:02d}: rejected mutation')
 print(f'RESULT: PASS {len(muts)}/{len(muts)}')
if __name__=='__main__':main()
