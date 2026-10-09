#!/usr/bin/env python3
"""Certificate for K1590's protected admission replay."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/'lab/process/k1590-residual-harmonic-admission.json').read_text());b=d['bridge_census'];p=d['protected_state'];z=d['decision'];c=[]
 c += [('claim',d['claim_id']=='K1590'),('rows',b['row_count']==305),('sum',sum(b[k] for k in ('satisfied_count','conditional_count','excluded_count','missing_count'))==b['row_count']),('satisfied',b['satisfied_count']==226),('conditional',b['conditional_count']==10),('excluded',b['excluded_count']==65),('missing',b['missing_count']==4),('five new',len(b['new_satisfied_rows'])==5),('four protected missing',len(b['protected_missing_rows'])==4),('source','ASSERTS' in p['source_claims'] and 'UNCERTAIN' in p['source_claims']),('ledger',p['physics_ledger']=='33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED'),('candidates','0/7' in p['candidate_counts']),('no canon',not p['canon_change']),('no paper',not p['paper_change']),('no prediction',not p['prediction_or_confirmation']),('no posture',not p['public_posture_change'])]
 c += [('advance',z['conditional_mathematical_advance']),('Ritz',z['residual_ritz_scale_proved']),('recentering',z['profiled_bounded_recentering_excluded']),('harmonic obstruction',z['energy_only_harmonic_integrability_excluded']),('coefficient open',not z['unrestricted_leading_coefficient_identified']),('true shift open',not z['true_ground_bounded_recentering_decided']),('flow open',not z['nonlinear_global_flow']),('source open',not z['source_owned_hamiltonian']),('protected',not z['protected_status_change'])]
 for i,(label,ok) in enumerate(c,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(c)}/{len(c)}')
if __name__=='__main__':main()
