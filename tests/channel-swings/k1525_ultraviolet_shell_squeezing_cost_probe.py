#!/usr/bin/env python3
"""Hostile mutations for K1525."""
import json,copy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1525-ultraviolet-shell-squeezing-cost.json').read_text())
def valid(x):
 q,d=x['shell_cost'],x['decision']
 return all([x['claim_id']=='K1525','Theta(N^3)' in q['shell'],'omega_j=Theta(N)' in q['shell'],'>=kappa C_N' in q['shell'],'(kappa/2)C_N' in q['low_variance_deficit'],'Cauchy gives' in q['weighted_cauchy'],'=O(1)' in q['dual_shell_bound'],'>=cN^4' in q['free_cost_consequence'],'c C_N^2=cN^4' in q['high_variance_consequence'],'stationary translation-invariant diagonal covariance' in q['scope_guard'],d['order_one_variance_suppression_cost']=='N^4',d['ultraviolet_shell_required'],not d['arbitrary_trial_lower_bound_proved'],not d['protected_status_change']])
def main():
 muts=[]
 for path,value in [(('claim_id',),'K1524'),(('shell_cost','shell'),'one mode'),(('shell_cost','low_variance_deficit'),'no deficit'),(('shell_cost','weighted_cauchy'),'reversed'),(('shell_cost','dual_shell_bound'),'O(log N)'),(('shell_cost','free_cost_consequence'),'N2'),(('shell_cost','high_variance_consequence'),'N2'),(('shell_cost','scope_guard'),'all states'),(('decision','order_one_variance_suppression_cost'),'N^2'),(('decision','ultraviolet_shell_required'),False),(('decision','arbitrary_trial_lower_bound_proved'),True),(('decision','protected_status_change'),True)]:
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;muts.append(x)
 assert valid(D)
 for i,x in enumerate(muts,1):assert not valid(x),i;print(f'PASS {i:02d}: rejected mutation')
 print(f'RESULT: PASS {len(muts)}/{len(muts)}')
if __name__=='__main__':main()
