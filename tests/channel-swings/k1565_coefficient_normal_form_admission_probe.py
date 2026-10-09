#!/usr/bin/env python3
"""Hostile mutations for K1565."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1565-coefficient-normal-form-admission.json').read_text())
def valid(x):
 c,p,d=x['bridge_census'],x['protected_state'],x['decision'];return all([x['claim_id']=='K1565',c['row_count']==280,c['satisfied_count']==201,c['row_count']==c['satisfied_count']+c['conditional_count']+c['excluded_count']+c['missing_count'],len(c['new_satisfied_rows'])==6,len(c['protected_missing_rows'])==4,'SC-META-53 remains UNCERTAIN' in p['source_claims'],'33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED' in p['physics_ledger'],'0/7' in p['candidate_counts'],not p['canon_change'],not p['paper_change'],not p['prediction_or_confirmation'],not p['public_posture_change'],d['conditional_mathematical_advance'],d['cube_coefficient_control_proved'],d['squeezed_limsup_coefficient_proved'],d['vacuum_coefficient_beaten_above_family_threshold'],d['radial_leakage_same_tier_exchange_proved'],d['residual_gauge_boundary_cocycle_proved'],not d['ground_energy_to_bounded_error'],not d['full_pde_leakages_closed'],not d['continuum_interacting_brst_operator'],not d['source_owned_gu_hamiltonian'],not d['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1564'),(('bridge_census','row_count'),279),(('bridge_census','satisfied_count'),200),(('bridge_census','conditional_count'),11),(('bridge_census','excluded_count'),64),(('bridge_census','missing_count'),3),(('bridge_census','new_satisfied_rows'),[]),(('bridge_census','protected_missing_rows'),[]),(('protected_state','source_claims'),'changed'),(('protected_state','physics_ledger'),'changed'),(('protected_state','candidate_counts'),'changed'),(('protected_state','canon_change'),True),(('protected_state','paper_change'),True),(('protected_state','prediction_or_confirmation'),True),(('protected_state','public_posture_change'),True),(('decision','conditional_mathematical_advance'),False),(('decision','cube_coefficient_control_proved'),False),(('decision','squeezed_limsup_coefficient_proved'),False),(('decision','vacuum_coefficient_beaten_above_family_threshold'),False),(('decision','radial_leakage_same_tier_exchange_proved'),False),(('decision','residual_gauge_boundary_cocycle_proved'),False),(('decision','ground_energy_to_bounded_error'),True),(('decision','full_pde_leakages_closed'),True),(('decision','continuum_interacting_brst_operator'),True),(('decision','source_owned_gu_hamiltonian'),True),(('decision','protected_status_change'),True)]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
