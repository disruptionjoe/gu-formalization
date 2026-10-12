#!/usr/bin/env python3
"""Protected-state integration certificate for K1710."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/'lab/process/k1710-moving-three-point-admission.json').read_text());b,p,z=d['bridge_census'],d['protected_state'],d['decision']
 checks=[('schema',d['schema_version']=='1.0'),('claim',d['claim_id']=='K1710'),('rows',b['row_count']==425),
  ('sum',sum(b[k] for k in ('satisfied_count','conditional_count','excluded_count','missing_count'))==425),
  ('satisfied',b['satisfied_count']==346),('conditional',b['conditional_count']==10),('excluded',b['excluded_count']==65),('missing',b['missing_count']==4),
  ('five rows',len(b['new_satisfied_rows'])==5),('four protected',len(b['protected_missing_rows'])==4),
  ('source','ASSERTS' in p['source_claims'] and 'UNCERTAIN' in p['source_claims']),('ledger',p['physics_ledger']=='33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED'),
  ('candidates','0/7' in p['candidate_counts']),('no canon',not p['canon_change']),('no paper',not p['paper_change']),
  ('no prediction',not p['prediction_or_confirmation']),('no posture',not p['public_posture_change']),('advance',z['conditional_mathematical_advance']),
  ('eighth',z['eighth_order_fisher_law_proved']),('moving',z['moving_three_point_optimizer_proved']),('global',z['complete_three_point_weak_globality_proved']),
  ('packet',z['rectangular_packet_quartic_gain_proved']),('all seed open',not z['all_seed_finite_strength_optimizer_identified']),
  ('haar open',not z['haar_saving_scale_identified']),('unrestricted open',not z['unrestricted_leading_coefficient_identified']),
  ('physical open',not z['source_owned_physical_theory']),('protected',not z['protected_status_change'])]
 for n,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {n:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
