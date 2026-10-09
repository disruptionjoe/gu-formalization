#!/usr/bin/env python3
"""Hostile mutations for K1537."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1537-wick-dominant-nongaussian-admission.json').read_text())
def valid(x):
 c,p,d=x['bridge_census'],x['protected_state'],x['decision']
 return all([x['claim_id']=='K1537',c['row_count']==c['satisfied_count']+c['conditional_count']+c['excluded_count']+c['missing_count'],c['row_count']==248,c['satisfied_count']==169,c['conditional_count']==10,c['excluded_count']==65,c['missing_count']==4,len(c['new_satisfied_rows'])==8,len(c['protected_missing_rows'])==4,'SC-META-53 remains UNCERTAIN' in p['source_claims'],'33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED' in p['physics_ledger'],'0/7' in p['candidate_counts'],not p['public_posture_change'],d['conditional_mathematical_advance'],d['material_nongaussian_class_classified'],not d['all_nongaussian_states_classified'],not d['order_N2_trial_constructed'],not d['source_owned_gu_hamiltonian'],not d['matching_ground_energy_asymptotic'],not d['prediction_or_confirmation'],not d['protected_status_change']])
def main():
 assert valid(D);mut=[(('claim_id',),'K1536'),(('bridge_census','row_count'),249),(('bridge_census','satisfied_count'),168),(('bridge_census','conditional_count'),9),(('bridge_census','excluded_count'),64),(('bridge_census','missing_count'),3),(('bridge_census','new_satisfied_rows'),[]),(('bridge_census','protected_missing_rows'),[]),(('protected_state','source_claims'),'changed'),(('protected_state','physics_ledger'),'changed'),(('protected_state','candidate_counts'),'1/7'),(('protected_state','public_posture_change'),True),(('decision','conditional_mathematical_advance'),False),(('decision','material_nongaussian_class_classified'),False),(('decision','all_nongaussian_states_classified'),True),(('decision','order_N2_trial_constructed'),True),(('decision','source_owned_gu_hamiltonian'),True),(('decision','matching_ground_energy_asymptotic'),True),(('decision','prediction_or_confirmation'),True),(('decision','protected_status_change'),True)]
 for i,(path,value) in enumerate(mut,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(mut)}/{len(mut)}')
if __name__=='__main__':main()
