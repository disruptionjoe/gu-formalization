#!/usr/bin/env python3
"""Hostile mutations for K1523."""
import json,copy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1523-coherent-wick-square-boundary.json').read_text())
def valid(x):
 q,d=x['coherent_boundary'],x['decision']
 return all([x['claim_id']=='K1523','N(alpha,I)' in q['q_space_trial'],'(1/4)sum_j omega_j alpha_j^2' in q['free_cost'],'6C_N^2+int h(x)^4' in q['wick_expectation'],'vacuum alpha=0 attains exactly 6gC_N^2' in q['coherent_infimum'],'covariance-preserving coherent shifts only' in q['scope_guard'],not d['coherent_order_N2_trial_exists'],not d['arbitrary_gaussian_classified'],not d['full_ground_energy_asymptotic_proved'],not d['protected_status_change']])
def main():
 muts=[]
 for path,value in [(('claim_id',),'K1522'),(('coherent_boundary','q_space_trial'),'unnormalized'),(('coherent_boundary','free_cost'),'zero'),(('coherent_boundary','wick_expectation'),'zero'),(('coherent_boundary','coherent_infimum'),'N2 trial'),(('coherent_boundary','scope_guard'),'all states'),(('decision','coherent_order_N2_trial_exists'),True),(('decision','arbitrary_gaussian_classified'),True),(('decision','full_ground_energy_asymptotic_proved'),True),(('decision','protected_status_change'),True)]:
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;muts.append(x)
 assert valid(D)
 for i,x in enumerate(muts,1):assert not valid(x),i;print(f'PASS {i:02d}: rejected mutation')
 print(f'RESULT: PASS {len(muts)}/{len(muts)}')
if __name__=='__main__':main()
