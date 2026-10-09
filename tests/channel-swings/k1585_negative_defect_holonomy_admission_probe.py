#!/usr/bin/env python3
"""Hostile mutations for K1585."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1585-negative-defect-holonomy-admission.json').read_text())
def valid(x):
 c=x['bridge_census'];p=x['protected_state'];z=x['decision'];return all([x['claim_id']=='K1585',c['row_count']==300,c['satisfied_count']==221,c['conditional_count']==10,c['excluded_count']==65,c['missing_count']==4,sum(c[k] for k in ('satisfied_count','conditional_count','excluded_count','missing_count'))==c['row_count'],len(c['new_satisfied_rows'])==5,'ASSERTS' in p['source_claims'],'UNCERTAIN' in p['source_claims'],'33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED'==p['physics_ledger'],not p['canon_change'],not p['paper_change'],not p['prediction_or_confirmation'],not p['public_posture_change'],z['conditional_mathematical_advance'],z['strict_gaussian_descent_proved'],z['linear_fisher_compensation_excluded'],z['moving_holonomy_identity_proved'],z['conditional_harmonic_radius_budget_proved'],not z['unrestricted_coefficient_identified'],not z['bounded_error_recentering'],not z['nonlinear_global_flow'],not z['source_owned_hamiltonian'],not z['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1584'),(('bridge_census','row_count'),299),(('bridge_census','satisfied_count'),220),(('bridge_census','conditional_count'),11),(('bridge_census','excluded_count'),64),(('bridge_census','missing_count'),5),(('protected_state','source_claims'),'changed'),(('protected_state','physics_ledger'),'changed')]+[(('protected_state',k),True) for k in ('canon_change','paper_change','prediction_or_confirmation','public_posture_change')]+[(('decision',k),False) for k in ('conditional_mathematical_advance','strict_gaussian_descent_proved','linear_fisher_compensation_excluded','moving_holonomy_identity_proved','conditional_harmonic_radius_budget_proved')]+[(('decision',k),True) for k in ('unrestricted_coefficient_identified','bounded_error_recentering','nonlinear_global_flow','source_owned_hamiltonian','protected_status_change')]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
