#!/usr/bin/env python3
"""Hostile mutations for K1524."""
import json,copy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1524-stationary-quasi-free-exact-formulas.json').read_text())
def valid(x):
 q,d=x['quasi_free_formulas'],x['decision']
 return all([x['claim_id']=='K1524','s_j>0' in q['trial_class'],'translation invariant' in q['trial_class'],'(s_j-1)^2/s_j' in q['free_cost'],'v_N=sum_j lambda_j s_j' in q['point_variance'],'6v(2C-v)' in q['mean_optimization_low_variance'],'3(v-C)^2+6C^2' in q['mean_optimization_high_variance'],'All coordinates are real' in q['normalization_guard'],'do not cover nonstationary' in q['scope_guard'],d['exact_free_cost_proved'],d['mean_optimization_proved'],not d['full_gaussian_classified'],not d['protected_status_change']])
def main():
 muts=[]
 for path,value in [(('claim_id',),'K1523'),(('quasi_free_formulas','trial_class'),'arbitrary covariance'),(('quasi_free_formulas','free_cost'),'wrong sign'),(('quasi_free_formulas','point_variance'),'unknown'),(('quasi_free_formulas','mean_optimization_low_variance'),'zero'),(('quasi_free_formulas','mean_optimization_high_variance'),'zero'),(('quasi_free_formulas','normalization_guard'),'complex double count'),(('quasi_free_formulas','scope_guard'),'all Gaussians'),(('decision','exact_free_cost_proved'),False),(('decision','mean_optimization_proved'),False),(('decision','full_gaussian_classified'),True),(('decision','protected_status_change'),True)]:
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;muts.append(x)
 assert valid(D)
 for i,x in enumerate(muts,1):assert not valid(x),i;print(f'PASS {i:02d}: rejected mutation')
 print(f'RESULT: PASS {len(muts)}/{len(muts)}')
if __name__=='__main__':main()
