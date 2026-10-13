#!/usr/bin/env python3
"""Hostile semantic mutations for K1728."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1728-moving-four-point-optimizer.json').read_text())
def valid(x):
 q,c,z=x.get('moving_path',{}),x.get('comparison',{}),x.get('decision',{})
 return all([x.get('claim_id')=='K1728','unit variance' in q.get('base',''),'589824000' in q.get('nonzero_certificate',''),
  '(35/3)sqrt(q)' in q.get('implicit_motion',''),'11/108' in q.get('attainment',''),c.get('three_point_wider_class_quartic_optimality') is False,
  z.get('local_implicit_path_exists'),z.get('regular_path_floor_attained'),z.get('moving_three_point_strictly_beaten'),
  not z.get('exact_all_seed_finite_strength_optimizer_identified'),'growing support' in x.get('scope_guard','')])
def setp(x,p,v):
 y=copy.deepcopy(x);c=y
 for k in p[:-1]:c=c[k]
 c[p[-1]]=v;return y
def main():
 assert valid(D);print('PASS 01: baseline')
 muts=[(('claim_id',),'K1727'),(('moving_path','base'),'unnormalized'),(('moving_path','nonzero_certificate'),'numerical guess'),
  (('moving_path','implicit_motion'),'fixed seed'),(('moving_path','attainment'),'D=0'),
  (('comparison','three_point_wider_class_quartic_optimality'),True),(('decision','local_implicit_path_exists'),False),
  (('decision','regular_path_floor_attained'),False),(('decision','moving_three_point_strictly_beaten'),False),
  (('decision','exact_all_seed_finite_strength_optimizer_identified'),True)]
 for n,(p,v) in enumerate(muts,2):assert not valid(setp(D,p,v));print(f"PASS {n:02d}: reject {'/'.join(p)}")
 print(f'RESULT: PASS {len(muts)+1}/{len(muts)+1}')
if __name__=='__main__':main()
