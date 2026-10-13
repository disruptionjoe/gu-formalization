#!/usr/bin/env python3
"""Hostile semantic mutations for K1730."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1730-four-point-admission.json').read_text())
def valid(x):
 b,p,z=x.get('bridge_census',{}),x.get('protected_state',{}),x.get('decision',{})
 return all([x.get('claim_id')=='K1730',x.get('classification')=='INTERNAL_STRUCTURAL_ONLY',b.get('row_count')==430,
  b.get('satisfied_count')==351,b.get('conditional_count')==10,b.get('excluded_count')==65,b.get('missing_count')==4,
  sum(b.get(k,0) for k in ('satisfied_count','conditional_count','excluded_count','missing_count'))==430,
  'ASSERTS' in p.get('source_claims',''),'UNCERTAIN' in p.get('source_claims',''),'33 SAME' in p.get('physics_ledger',''),
  not p.get('canon_change'),not p.get('paper_change'),not p.get('prediction_or_confirmation'),not p.get('public_posture_change'),
  z.get('conditional_mathematical_advance'),z.get('regular_path_quartic_floor_proved'),z.get('exact_four_point_equality_seed_constructed'),
  z.get('moving_four_point_attainment_proved'),not z.get('moving_three_point_wider_class_optimality'),z.get('rectangular_packet_quartic_gain_proved'),
  not z.get('all_seed_nonperturbative_optimizer_identified'),not z.get('unrestricted_stationary_lower_bound_proved'),
  not z.get('source_owned_physical_theory'),not z.get('protected_status_change')])
def setp(x,p,v):
 y=copy.deepcopy(x);c=y
 for k in p[:-1]:c=c[k]
 c[p[-1]]=v;return y
def main():
 assert valid(D);print('PASS 01: baseline')
 muts=[(('claim_id',),'K1729'),(('classification',),'SOURCE_NATIVE_ROUTE'),(('bridge_census','row_count'),429),
  (('bridge_census','satisfied_count'),350),(('protected_state','source_claims'),'changed'),(('protected_state','physics_ledger'),'changed'),
  (('protected_state','canon_change'),True),(('decision','conditional_mathematical_advance'),False),
  (('decision','moving_three_point_wider_class_optimality'),True),(('decision','all_seed_nonperturbative_optimizer_identified'),True),
  (('decision','unrestricted_stationary_lower_bound_proved'),True),(('decision','source_owned_physical_theory'),True),
  (('decision','protected_status_change'),True)]
 for n,(p,v) in enumerate(muts,2):assert not valid(setp(D,p,v));print(f"PASS {n:02d}: reject {'/'.join(p)}")
 print(f'RESULT: PASS {len(muts)+1}/{len(muts)+1}')
if __name__=='__main__':main()
