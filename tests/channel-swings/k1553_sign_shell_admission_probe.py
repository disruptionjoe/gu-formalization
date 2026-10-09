#!/usr/bin/env python3
"""Hostile mutations for K1553."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1553-sign-shell-admission.json').read_text())
def valid(x):
 c,p,d=x['bridge_census'],x['protected_state'],x['decision'];return all([x['claim_id']=='K1553',c['row_count']==268,c['row_count']==c['satisfied_count']+c['conditional_count']+c['excluded_count']+c['missing_count'],len(c['new_satisfied_rows'])==6,len(c['protected_missing_rows'])==4,'SC-META-53 remains UNCERTAIN' in p['source_claims'],'33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED' in p['physics_ledger'],'0/7' in p['candidate_counts'],not p['public_posture_change'],d['conditional_mathematical_advance'],d['arbitrary_fixed_shell_order_N2_route_excluded'],d['ground_energy_lower_boundary_raised'],not d['matching_ground_energy_asymptotic'],not d['continuum_interacting_brst_operator'],not d['source_owned_gu_hamiltonian'],not d['prediction_or_confirmation'],not d['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1552'),(('bridge_census','row_count'),267),(('bridge_census','satisfied_count'),188),(('bridge_census','conditional_count'),11),(('bridge_census','excluded_count'),64),(('bridge_census','missing_count'),3),(('bridge_census','new_satisfied_rows'),[]),(('bridge_census','protected_missing_rows'),[]),(('protected_state','source_claims'),'changed'),(('protected_state','physics_ledger'),'changed'),(('protected_state','candidate_counts'),'changed'),(('protected_state','public_posture_change'),True),(('decision','conditional_mathematical_advance'),False),(('decision','arbitrary_fixed_shell_order_N2_route_excluded'),False),(('decision','ground_energy_lower_boundary_raised'),False),(('decision','matching_ground_energy_asymptotic'),True),(('decision','continuum_interacting_brst_operator'),True),(('decision','source_owned_gu_hamiltonian'),True),(('decision','prediction_or_confirmation'),True),(('decision','protected_status_change'),True)]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
