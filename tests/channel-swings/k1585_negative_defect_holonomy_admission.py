#!/usr/bin/env python3
"""Certificate for K1585's protected admission replay."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/'lab/process/k1585-negative-defect-holonomy-admission.json').read_text());c=d['bridge_census'];p=d['protected_state'];z=d['decision'];checks=[]
 checks += [('claim',d['claim_id']=='K1585'),('rows',c['row_count']==300),('sum',c['satisfied_count']+c['conditional_count']+c['excluded_count']+c['missing_count']==c['row_count']),('satisfied',c['satisfied_count']==221),('conditional',c['conditional_count']==10),('excluded',c['excluded_count']==65),('missing',c['missing_count']==4),('five new',len(c['new_satisfied_rows'])==5),('four protected missing',len(c['protected_missing_rows'])==4),('source fixed','ASSERTS' in p['source_claims'] and 'UNCERTAIN' in p['source_claims']),('ledger fixed','33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED'==p['physics_ledger']),('candidate fixed','0/7' in p['candidate_counts']),('no canon',not p['canon_change']),('no paper',not p['paper_change']),('no prediction',not p['prediction_or_confirmation']),('no posture',not p['public_posture_change'])]
 checks += [('advance',z['conditional_mathematical_advance']),('descent',z['strict_gaussian_descent_proved']),('linear excluded',z['linear_fisher_compensation_excluded']),('holonomy',z['moving_holonomy_identity_proved']),('radius conditional',z['conditional_harmonic_radius_budget_proved']),('coefficient open',not z['unrestricted_coefficient_identified']),('bounded open',not z['bounded_error_recentering']),('flow open',not z['nonlinear_global_flow']),('source open',not z['source_owned_hamiltonian']),('protected',not z['protected_status_change'])]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
