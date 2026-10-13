#!/usr/bin/env python3
"""Implicit-path and exact-gap controls for K1728."""
import json, math
from pathlib import Path
from scipy.optimize import brentq

ROOT=Path(__file__).resolve().parents[2]
def P(u): return 17*u**3-38*u**2+84*u-24


def main():
 d=json.loads((ROOT/'lab/process/k1728-moving-four-point-optimizer.json').read_text());q,c,z=d['moving_path'],d['comparison'],d['decision']
 u=brentq(P,0,1);S=2*(6-7*u)/(2-u);R=S-(3-u);disc=S*S-4*R
 A=(S-math.sqrt(disc))/2;B=(S+math.sqrt(disc))/2;p0=(B-1)/(B-A)
 T=2*(7*u**3-18*u**2+84*u-24)/(u-2)**2;dk=(A-B)*T;beta=(35/3)*u**1.5/dk
 def scaled(p):
  v=p*A+(1-p)*B;a=math.sqrt(A/v);b=math.sqrt(B/v)
  m4=p*a**4+(1-p)*b**4;m6=p*a**6+(1-p)*b**6;m8=p*a**8+(1-p)*b**8
  uu=3-m4;k6=m6-15*m4+30;h8=m8-28*m6+210*m4-315
  return uu,k6,h8
 limits=[]
 for defect in (1e-6,1e-7,1e-8):
  target=(35/3)*math.sqrt(defect)
  root=brentq(lambda p: scaled(p)[1]/scaled(p)[0]**1.5-target,p0-.02,p0,xtol=1e-15)
  uu,k6,h8=scaled(root);limits.append((root,k6/uu**1.5/math.sqrt(defect),h8/uu**2))
 D3=1009/1512+5*math.sqrt(105)/168;D4=11/108;gap=5*(math.sqrt(105)+19)/168
 checks=[('schema',d['schema_version']=='1.0'),('claim',d['claim_id']=='K1728'),('resultant', '589824000' in q['nonzero_certificate']),
  ('derivative nonzero',abs(dk)>4),('derivative negative',dk<0),('beta negative',beta<0),
  ('beta value',math.isclose(beta,-0.480253485638498,rel_tol=3e-13)),('implicit roots',all(0<x[0]<1 for x in limits)),
  ('scaled sixth exact',all(math.isclose(x[1],35/3,rel_tol=2e-10) for x in limits)),
  ('eighth tends 35',abs(limits[-1][2]-35)<abs(limits[0][2]-35)),('eighth near',abs(limits[-1][2]-35)<0.1),
  ('floor', '11/108' in q['attainment']),('gap formula',c['strict_gap']=='5(sqrt(105)+19)/168'),
  ('gap numeric',math.isclose(D3-D4,gap,rel_tol=3e-15)),('strict',D3>D4),
  ('path exists',z['local_implicit_path_exists']),('attained',z['regular_path_floor_attained']),
  ('three point beaten',z['moving_three_point_strictly_beaten']),('finite open',not z['exact_all_seed_finite_strength_optimizer_identified']),
  ('scope', 'weak matched reward' in d['scope_guard'] and 'growing support' in d['scope_guard'])]
 for n,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {n:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
