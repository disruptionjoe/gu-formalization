#!/usr/bin/env python3
"""Hostile mutations for K1522."""
import json,copy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1522-quadratic-localization-admission.json').read_text())
def valid(x):
 c,p,d=x['bridge_census'],x['protected_state'],x['decision']
 return all([x['claim_id']=='K1522',c['row_count']==c['satisfied_count']+c['conditional_count']+c['excluded_count']+c['missing_count'],c['missing_count']==4,'SC-META-53 remains UNCERTAIN' in p['source_claims'],'0/7' in p['candidate_counts'],not p['public_posture_change'],not d['source_owned_gu_hamiltonian'],not d['matching_ground_energy_asymptotic'],not d['prediction_or_confirmation'],not d['protected_status_change']])
def main():
 muts=[]
 for path,value in [(('claim_id',),'K1521'),(('bridge_census','row_count'),227),(('bridge_census','missing_count'),3),(('protected_state','source_claims'),'SC-META-53 proved'),(('protected_state','candidate_counts'),'1/7'),(('protected_state','public_posture_change'),True),(('decision','source_owned_gu_hamiltonian'),True),(('decision','matching_ground_energy_asymptotic'),True),(('decision','prediction_or_confirmation'),True),(('decision','protected_status_change'),True)]:
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;muts.append(x)
 assert valid(D)
 for i,x in enumerate(muts,1):assert not valid(x),i;print(f'PASS {i:02d}: rejected mutation')
 print(f'RESULT: PASS {len(muts)}/{len(muts)}')
if __name__=='__main__':main()
