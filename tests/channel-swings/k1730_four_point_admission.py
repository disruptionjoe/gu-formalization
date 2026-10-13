#!/usr/bin/env python3
"""Protected-state integration certificate for K1730."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/'lab/process/k1730-four-point-admission.json').read_text());b,p,z=d['bridge_census'],d['protected_state'],d['decision']
 checks=[('schema',d['schema_version']=='1.0'),('claim',d['claim_id']=='K1730'),('classification',d['classification']=='INTERNAL_STRUCTURAL_ONLY'),
  ('rows',b['row_count']==430),('sum',sum(b[k] for k in ('satisfied_count','conditional_count','excluded_count','missing_count'))==430),
  ('satisfied',b['satisfied_count']==351),('conditional',b['conditional_count']==10),('excluded',b['excluded_count']==65),('missing',b['missing_count']==4),
  ('five rows',len(b['new_satisfied_rows'])==5),('four protected',len(b['protected_missing_rows'])==4),
  ('source','ASSERTS' in p['source_claims'] and 'UNCERTAIN' in p['source_claims']),('ledger',p['physics_ledger']=='33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED'),
  ('candidates','0/7' in p['candidate_counts']),('no canon',not p['canon_change']),('no paper',not p['paper_change']),
  ('no prediction',not p['prediction_or_confirmation']),('no posture',not p['public_posture_change']),
  ('advance',z['conditional_mathematical_advance']),('floor',z['regular_path_quartic_floor_proved']),('seed',z['exact_four_point_equality_seed_constructed']),
  ('attainment',z['moving_four_point_attainment_proved']),('three point false',not z['moving_three_point_wider_class_optimality']),
  ('packet',z['rectangular_packet_quartic_gain_proved']),('finite open',not z['all_seed_nonperturbative_optimizer_identified']),
  ('lower open',not z['unrestricted_stationary_lower_bound_proved']),('physical open',not z['source_owned_physical_theory']),
  ('protected',not z['protected_status_change']),('next finite','finite-strength' in d['next_condition'])]
 for n,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {n:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
