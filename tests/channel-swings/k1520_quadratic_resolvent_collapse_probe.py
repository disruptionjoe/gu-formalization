#!/usr/bin/env python3
"""Hostile mutations for K1520."""
import json,copy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1520-quadratic-resolvent-collapse.json').read_text())
def valid(x):
 q,d=x['spectral_consequence'],x['decision']
 return all([x['claim_id']=='K1520','O(N^-2)' in q['unshifted_resolvent'],'a_N=o(N^2)' in q['subquadratic_shift'],'not the resolvent' in q['operator_ceiling'],'nonsharp' in q['rate_ceiling'],d['subquadratic_recentering_excluded'],not d['matching_resolvent_asymptotic_proved'],not d['protected_status_change']])
def main():
 muts=[]
 for path,value in [(('claim_id',),'K1519'),(('spectral_consequence','unshifted_resolvent'),'O(1/log N)'),(('spectral_consequence','subquadratic_shift'),'none'),(('spectral_consequence','operator_ceiling'),'zero operator resolvent'),(('spectral_consequence','rate_ceiling'),'sharp'),(('decision','subquadratic_recentering_excluded'),False),(('decision','matching_resolvent_asymptotic_proved'),True),(('decision','protected_status_change'),True)]:
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;muts.append(x)
 assert valid(D)
 for i,x in enumerate(muts,1):assert not valid(x),i;print(f'PASS {i:02d}: rejected mutation')
 print(f'RESULT: PASS {len(muts)}/{len(muts)}')
if __name__=='__main__':main()
