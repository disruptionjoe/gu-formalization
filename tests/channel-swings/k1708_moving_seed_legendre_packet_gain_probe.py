#!/usr/bin/env python3
"""Hostile semantic mutations for K1708."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1708-moving-seed-legendre-packet-gain.json').read_text())
def valid(x):
 q,z=x.get('transfer',{}),x.get('decision',{})
 return all([x.get('claim_id')=='K1708','81D-2187/32' in q.get('generic_legendre',''),'(735/8)r^4' in q.get('profile_gap',''),
  '5880g^4' in q.get('fixed_packet_gap',''),'c_*g^4' in q.get('optimized_shape_consequence',''),z.get('legendre_quartic_gain_exact'),
  z.get('fixed_packet_quartic_gain_exact'),z.get('fully_rectangular_optimized_strict_gain'),not z.get('exact_global_quartic_shape_coefficient_identified'),
  not z.get('unrestricted_coefficient_identified'),'K1683' in x.get('scope_guard','')])
def setp(x,p,v):
 y=copy.deepcopy(x);c=y
 for k in p[:-1]:c=c[k]
 c[p[-1]]=v;return y
def main():
 assert valid(D);print('PASS 01: baseline')
 muts=[(('claim_id',),'K1707'),(('transfer','generic_legendre'),'changed'),(('transfer','profile_gap'),'changed'),
  (('transfer','fixed_packet_gap'),'changed'),(('transfer','optimized_shape_consequence'),'no gain'),
  (('decision','legendre_quartic_gain_exact'),False),(('decision','fixed_packet_quartic_gain_exact'),False),
  (('decision','fully_rectangular_optimized_strict_gain'),False),(('decision','exact_global_quartic_shape_coefficient_identified'),True),
  (('decision','unrestricted_coefficient_identified'),True),(('scope_guard',),'unrestricted')]
 for n,(p,v) in enumerate(muts,2):assert not valid(setp(D,p,v));print(f"PASS {n:02d}: reject {'/'.join(p)}")
 print(f'RESULT: PASS {len(muts)+1}/{len(muts)+1}')
if __name__=='__main__':main()
