#!/usr/bin/env python3
"""Exact transfer controls for K1729."""
import json,math
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/'lab/process/k1729-four-point-legendre-packet-gain.json').read_text());q,z=d['transfer'],d['decision'];r=math.sqrt(105)
 gap=F(5,168)*(r+19);leg=81*gap;packet=64*leg
 checks=[('schema',d['schema_version']=='1.0'),('claim',d['claim_id']=='K1729'),('gap positive',gap>0),
  ('legendre coefficient',math.isclose(leg,135*(r+19)/56,rel_tol=3e-15)),
  ('packet coefficient',math.isclose(packet,1080*(r+19)/7,rel_tol=3e-15)),
  ('gap text','5(sqrt(105)+19)/168' in q['coefficient_gap']),('legendre text','135(sqrt(105)+19)/56' in q['legendre_gap']),
  ('factorization','tau_g(C)/4' in q['packet_factorization']),('packet text','1080(sqrt(105)+19)/7' in q['fixed_packet_gap']),
  ('shape strict','strictly lower' in q['optimized_shape_consequence']),('legendre exact',z['legendre_gap_exact']),
  ('packet exact',z['fixed_packet_gap_exact']),('shape optimized',z['rectangular_shape_optimized_strict_gain']),
  ('shape coefficient open',not z['exact_global_quartic_shape_coefficient_identified']),('unrestricted open',not z['unrestricted_coefficient_identified']),
  ('scope','K1683' in d['scope_guard'] and 'no unrestricted lower bound' in d['scope_guard'])]
 for n,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {n:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
