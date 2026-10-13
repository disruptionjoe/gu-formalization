#!/usr/bin/env python3
"""Hostile semantic mutations for K1727."""
import copy, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1727-four-point-equality-seed.json').read_text())
def valid(x):
 q,z=x.get('algebraic_seed',{}),x.get('decision',{})
 return all([x.get('claim_id')=='K1727','17u^3-38u^2+84u-24=0' in q.get('u',''),'0<A<1<B' in q.get('order',''),
  'E[X^2]=1' in q.get('order',''),'kappa_4=-u<0' in q.get('hermite_moments',''),'kappa_6=0' in q.get('hermite_moments',''),
  'h_8=35u^2' in q.get('hermite_moments',''),z.get('bounded_symmetric_unit_variance'),z.get('negative_fourth_cumulant'),
  z.get('sixth_hermite_zero'),z.get('eighth_ratio_exact')=='35',not z.get('three_point_family'),
  'four-atom' in x.get('scope_guard','')])
def setp(x,p,v):
 y=copy.deepcopy(x);c=y
 for k in p[:-1]:c=c[k]
 c[p[-1]]=v;return y
def main():
 assert valid(D);print('PASS 01: baseline')
 muts=[(('claim_id',),'K1726'),(('algebraic_seed','u'),'fitted decimal'),(('algebraic_seed','order'),'untyped'),
  (('algebraic_seed','hermite_moments'),'changed'),(('decision','bounded_symmetric_unit_variance'),False),
  (('decision','negative_fourth_cumulant'),False),(('decision','sixth_hermite_zero'),False),
  (('decision','eighth_ratio_exact'),'34'),(('decision','three_point_family'),True),(('scope_guard',),'physical seed')]
 for n,(p,v) in enumerate(muts,2):assert not valid(setp(D,p,v));print(f"PASS {n:02d}: reject {'/'.join(p)}")
 print(f'RESULT: PASS {len(muts)+1}/{len(muts)+1}')
if __name__=='__main__':main()
