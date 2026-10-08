#!/usr/bin/env python3
"""Hostile mutations for K1519."""
import json,copy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1519-quadratic-kinetic-localization-lower-bound.json').read_text())
def valid(x):
 q,d=x['localization_lower_bound'],x['decision']
 return all([x['claim_id']=='K1519','binary data processing' in q['entropy_contraction'],'Gross inequality' in q['log_sobolev'],'c_g N^2' in q['energy_boundary'],'every normalized vector' in q['many_chaos_scope'],d['many_chaos_lower_boundary_proved'],not d['matching_upper_bound_proved'],not d['ground_energy_asymptotic_determined'],not d['protected_status_change']])
def main():
 muts=[]
 for path,value in [(('claim_id',),'K1518'),(('localization_lower_bound','entropy_contraction'),'none'),(('localization_lower_bound','log_sobolev'),'cutoff dependent'),(('localization_lower_bound','energy_boundary'),'log N'),(('localization_lower_bound','many_chaos_scope'),'finite trial only'),(('decision','matching_upper_bound_proved'),True),(('decision','ground_energy_asymptotic_determined'),True),(('decision','protected_status_change'),True)]:
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;muts.append(x)
 assert valid(D)
 for i,x in enumerate(muts,1):assert not valid(x),i;print(f'PASS {i:02d}: rejected mutation')
 print(f'RESULT: PASS {len(muts)}/{len(muts)}')
if __name__=='__main__':main()
