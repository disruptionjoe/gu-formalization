#!/usr/bin/env python3
"""Hostile mutations for K1605."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1605-heterogeneous-mixture-spectral-admission.json').read_text())
def valid(x):
 b=x['bridge_census'];p=x['protected_state'];z=x['decision'];return all([x['claim_id']=='K1605',b['row_count']==320,b['satisfied_count']==241,b['conditional_count']==10,b['excluded_count']==65,b['missing_count']==4,sum(b[k] for k in ('satisfied_count','conditional_count','excluded_count','missing_count'))==b['row_count'],'ASSERTS' in p['source_claims'],'UNCERTAIN' in p['source_claims'],p['physics_ledger']=='33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED',not p['canon_change'],not p['paper_change'],not p['prediction_or_confirmation'],not p['public_posture_change'],z['conditional_mathematical_advance'],z['heterogeneous_gaussian_sandwich_proved'],z['shrinking_relative_band_coefficient_rigid'],z['atomic_resonance_exclusion_proved'],z['conditional_positive_radius_budget_proved'],not z['unrestricted_leading_coefficient_identified'],not z['source_owned_global_flow'],not z['source_owned_hamiltonian'],not z['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1604'),(('bridge_census','row_count'),319),(('bridge_census','satisfied_count'),240),(('bridge_census','conditional_count'),11),(('bridge_census','excluded_count'),64),(('bridge_census','missing_count'),5),(('protected_state','source_claims'),'changed'),(('protected_state','physics_ledger'),'changed')]+[(('protected_state',k),True) for k in ('canon_change','paper_change','prediction_or_confirmation','public_posture_change')]+[(('decision',k),False) for k in ('conditional_mathematical_advance','heterogeneous_gaussian_sandwich_proved','shrinking_relative_band_coefficient_rigid','atomic_resonance_exclusion_proved','conditional_positive_radius_budget_proved')]+[(('decision',k),True) for k in ('unrestricted_leading_coefficient_identified','source_owned_global_flow','source_owned_hamiltonian','protected_status_change')]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
