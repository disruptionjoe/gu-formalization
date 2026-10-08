#!/usr/bin/env python3
"""Hostile mutations for K1518."""
import json,copy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1518-gaussian-quadratic-mass-chernoff.json').read_text())
def valid(x):
 q,d=x['quadratic_mass_tail'],x['decision']
 return all([x['claim_id']=='K1518','real covariance eigenbasis' in q['mass_coordinate'],'(2-sqrt(3))C_N' in q['square_event'],'min(u^2/B_N,u/lambda_*)' in q['bernstein_bound'],'exp(-cN^2)' in q['small_ball_consequence'],not d['matching_small_ball_asymptotic_proved'],not d['ground_state_localization_proved'],not d['protected_status_change']])
def main():
 muts=[]
 for path,value in [(('claim_id',),'K1517'),(('quadratic_mass_tail','mass_coordinate'),'complex independent modes'),(('quadratic_mass_tail','square_event'),'reversed Jensen'),(('quadratic_mass_tail','bernstein_bound'),'one scale only'),(('quadratic_mass_tail','small_ball_consequence'),'exp(-cN)'),(('decision','matching_small_ball_asymptotic_proved'),True),(('decision','ground_state_localization_proved'),True),(('decision','protected_status_change'),True)]:
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;muts.append(x)
 assert valid(D)
 for i,x in enumerate(muts,1):assert not valid(x),i;print(f'PASS {i:02d}: rejected mutation')
 print(f'RESULT: PASS {len(muts)}/{len(muts)}')
if __name__=='__main__':main()
