#!/usr/bin/env python3
"""Hostile semantic mutations for K1729."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1729-four-point-legendre-packet-gain.json').read_text())
def valid(x):
 q,z=x.get('transfer',{}),x.get('decision',{})
 return all([x.get('claim_id')=='K1729','5(sqrt(105)+19)/168' in q.get('coefficient_gap',''),
  '135(sqrt(105)+19)/56' in q.get('legendre_gap',''),'tau_g(C)/4' in q.get('packet_factorization',''),
  '1080(sqrt(105)+19)/7' in q.get('fixed_packet_gap',''),z.get('legendre_gap_exact'),z.get('fixed_packet_gap_exact'),
  z.get('rectangular_shape_optimized_strict_gain'),not z.get('exact_global_quartic_shape_coefficient_identified'),
  not z.get('unrestricted_coefficient_identified'),'no unrestricted lower bound' in x.get('scope_guard','')])
def setp(x,p,v):
 y=copy.deepcopy(x);c=y
 for k in p[:-1]:c=c[k]
 c[p[-1]]=v;return y
def main():
 assert valid(D);print('PASS 01: baseline')
 muts=[(('claim_id',),'K1728'),(('transfer','coefficient_gap'),'zero'),(('transfer','legendre_gap'),'changed'),
  (('transfer','packet_factorization'),'changed'),(('transfer','fixed_packet_gap'),'changed'),
  (('decision','legendre_gap_exact'),False),(('decision','fixed_packet_gap_exact'),False),
  (('decision','rectangular_shape_optimized_strict_gain'),False),(('decision','exact_global_quartic_shape_coefficient_identified'),True),
  (('decision','unrestricted_coefficient_identified'),True)]
 for n,(p,v) in enumerate(muts,2):assert not valid(setp(D,p,v));print(f"PASS {n:02d}: reject {'/'.join(p)}")
 print(f'RESULT: PASS {len(muts)+1}/{len(muts)+1}')
if __name__=='__main__':main()
