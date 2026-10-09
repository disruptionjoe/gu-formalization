#!/usr/bin/env python3
"""Hostile mutations for K1570."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1570-profile-current-admission.json').read_text())
def valid(x):
 c,p,d=x['bridge_census'],x['protected_state'],x['decision'];return all([x['claim_id']=='K1570',c['row_count']==285,c['satisfied_count']==206,c['row_count']==c['satisfied_count']+c['conditional_count']+c['excluded_count']+c['missing_count'],len(c['new_satisfied_rows'])==5,len(c['protected_missing_rows'])==4,'SC-META-53 remains UNCERTAIN' in p['source_claims'],'33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED' in p['physics_ledger'],'0/7' in p['candidate_counts'],not p['canon_change'],not p['paper_change'],not p['prediction_or_confirmation'],not p['public_posture_change'],d['conditional_mathematical_advance'],d['profiled_gaussian_coefficient_reduction_proved'],d['vacuum_coefficient_beaten_for_all_positive_couplings'],d['differentiated_current_spatial_loss_removed'],d['two_radius_analytic_boundary_proved'],not d['ground_energy_ratio_convergence'],not d['ground_energy_to_bounded_error'],not d['full_pde_leakages_closed'],not d['continuum_interacting_brst_operator'],not d['source_owned_gu_hamiltonian'],not d['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1569'),(('bridge_census','row_count'),284),(('bridge_census','satisfied_count'),205),(('bridge_census','new_satisfied_rows'),[]),(('bridge_census','protected_missing_rows'),[]),(('protected_state','source_claims'),'changed'),(('protected_state','physics_ledger'),'changed'),(('protected_state','candidate_counts'),'changed')]+[(('protected_state',k),True) for k in ('canon_change','paper_change','prediction_or_confirmation','public_posture_change')]+[(('decision',k),False) for k in ('conditional_mathematical_advance','profiled_gaussian_coefficient_reduction_proved','vacuum_coefficient_beaten_for_all_positive_couplings','differentiated_current_spatial_loss_removed','two_radius_analytic_boundary_proved')]+[(('decision',k),True) for k in ('ground_energy_ratio_convergence','ground_energy_to_bounded_error','full_pde_leakages_closed','continuum_interacting_brst_operator','source_owned_gu_hamiltonian','protected_status_change')]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
