#!/usr/bin/env python3
"""Hostile mutations for K1532."""
import json,copy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1532-all-gaussian-admission.json').read_text())
def valid(x):
 c,p,d=x['bridge_census'],x['protected_state'],x['decision']
 return all([x['claim_id']=='K1532',c['row_count']==c['satisfied_count']+c['conditional_count']+c['excluded_count']+c['missing_count'],c['row_count']==240,c['satisfied_count']==161,c['conditional_count']==10,c['excluded_count']==65,c['missing_count']==4,len(c['new_satisfied_rows'])==6,len(c['protected_missing_rows'])==4,'SC-META-53 remains UNCERTAIN' in p['source_claims'],'33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED' in p['physics_ledger'],'0/7' in p['candidate_counts'],not p['public_posture_change'],d['conditional_mathematical_advance'],d['all_finite_cutoff_gaussian_route_classified'],not d['nongaussian_route_classified'],not d['source_owned_gu_hamiltonian'],not d['matching_ground_energy_asymptotic'],not d['prediction_or_confirmation'],not d['protected_status_change']])
def main():
 muts=[]
 for path,value in [(('claim_id',),'K1531'),(('bridge_census','row_count'),241),(('bridge_census','satisfied_count'),160),(('bridge_census','conditional_count'),9),(('bridge_census','excluded_count'),64),(('bridge_census','missing_count'),3),(('bridge_census','new_satisfied_rows'),[]),(('bridge_census','protected_missing_rows'),[]),(('protected_state','source_claims'),'changed'),(('protected_state','physics_ledger'),'changed'),(('protected_state','candidate_counts'),'1/7'),(('protected_state','public_posture_change'),True),(('decision','conditional_mathematical_advance'),False),(('decision','all_finite_cutoff_gaussian_route_classified'),False),(('decision','nongaussian_route_classified'),True),(('decision','source_owned_gu_hamiltonian'),True),(('decision','matching_ground_energy_asymptotic'),True),(('decision','prediction_or_confirmation'),True),(('decision','protected_status_change'),True)]:
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;muts.append(x)
 assert valid(D)
 for i,x in enumerate(muts,1):assert not valid(x),i;print(f'PASS {i:02d}: rejected mutation')
 print(f'RESULT: PASS {len(muts)}/{len(muts)}')
if __name__=='__main__':main()
