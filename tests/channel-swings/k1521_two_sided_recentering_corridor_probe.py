#!/usr/bin/env python3
"""Hostile mutations for K1521."""
import json,copy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1521-two-sided-recentering-corridor.json').read_text())
def valid(x):
 q,d=x['recentering_corridor'],x['decision']
 return all([x['claim_id']=='K1521','c_g N^2<=E_N' in q['ground_energy_bracket'],'nonmatching corridor' in q['surviving_corridor'],'P_harm' in q['brst_transfer'],d['two_sided_recentering_corridor_proved'],not d['corridor_endpoints_match'],not d['ground_energy_shift_identified'],not d['interacting_continuum_brst_constructed'],not d['protected_status_change']])
def main():
 muts=[]
 for path,value in [(('claim_id',),'K1520'),(('recentering_corridor','ground_energy_bracket'),'E exact'),(('recentering_corridor','surviving_corridor'),'matching asymptotic'),(('recentering_corridor','brst_transfer'),'full continuum BRST'),(('decision','corridor_endpoints_match'),True),(('decision','ground_energy_shift_identified'),True),(('decision','interacting_continuum_brst_constructed'),True),(('decision','protected_status_change'),True)]:
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;muts.append(x)
 assert valid(D)
 for i,x in enumerate(muts,1):assert not valid(x),i;print(f'PASS {i:02d}: rejected mutation')
 print(f'RESULT: PASS {len(muts)}/{len(muts)}')
if __name__=='__main__':main()
