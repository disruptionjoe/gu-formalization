#!/usr/bin/env python3
"""Hostile mutations for K1580."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1580-nongaussian-flat-connection-admission.json').read_text())
def valid(x):
 c,p,d=x['bridge_census'],x['protected_state'],x['decision'];return all([x['claim_id']=='K1580',c['row_count']==295,c['satisfied_count']==216,c['row_count']==c['satisfied_count']+c['conditional_count']+c['excluded_count']+c['missing_count'],len(c['new_satisfied_rows'])==5,len(c['protected_missing_rows'])==4,'SC-META-53 remains UNCERTAIN' in p['source_claims'],'33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED' in p['physics_ledger'],not any(p[k] for k in ('canon_change','paper_change','prediction_or_confirmation','public_posture_change')),d['conditional_mathematical_advance'],d['wick_dominant_nongaussian_class_coefficient_proved'],d['class_minimizer_rigidity_proved'],d['raw_B_A_global_necessity_excluded'],d['static_flat_covariant_cancellation_proved'],not d['unrestricted_ground_energy_ratio_convergence'],not d['ground_energy_to_bounded_error'],not d['global_positive_analytic_radius'],not d['nonlinear_harmonic_split_closed'],not d['continuum_interacting_brst_operator'],not d['source_owned_gu_hamiltonian'],not d['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1579'),(('bridge_census','row_count'),294),(('bridge_census','satisfied_count'),215),(('bridge_census','new_satisfied_rows'),[]),(('bridge_census','protected_missing_rows'),[])]+[(('protected_state',k),True) for k in ('canon_change','paper_change','prediction_or_confirmation','public_posture_change')]+[(('decision',k),False) for k in ('conditional_mathematical_advance','wick_dominant_nongaussian_class_coefficient_proved','class_minimizer_rigidity_proved','raw_B_A_global_necessity_excluded','static_flat_covariant_cancellation_proved')]+[(('decision',k),True) for k in ('unrestricted_ground_energy_ratio_convergence','ground_energy_to_bounded_error','global_positive_analytic_radius','nonlinear_harmonic_split_closed','continuum_interacting_brst_operator','source_owned_gu_hamiltonian','protected_status_change')]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
