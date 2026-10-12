#!/usr/bin/env python3
"""Exact Legendre and packet-factor controls for K1708."""
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/'lab/process/k1708-moving-seed-legendre-packet-gain.json').read_text());q,z=d['transfer'],d['decision']
 gain=Fraction(245,216)
 checks=[('schema',d['schema_version']=='1.0'),('claim',d['claim_id']=='K1708'),
  ('generic profile','81D-2187/32' in q['generic_legendre']),('profile text','(735/8)r^4' in q['profile_gap']),
  ('packet factor','tau_g(C)/4' in q['packet_factorization']),('packet text','5880g^4' in q['fixed_packet_gap']),
  ('legendre arithmetic',81*gain==Fraction(735,8)),('packet arithmetic',64*Fraction(735,8)==5880),
  ('shape strict','c_*g^4' in q['optimized_shape_consequence']),('legendre decision',z['legendre_quartic_gain_exact']),
  ('packet decision',z['fixed_packet_quartic_gain_exact']),('shape decision',z['fully_rectangular_optimized_strict_gain']),
  ('shape coefficient open',not z['exact_global_quartic_shape_coefficient_identified']),
  ('unrestricted open',not z['unrestricted_coefficient_identified']),('scope','K1683' in d['scope_guard'])]
 for n,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {n:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
