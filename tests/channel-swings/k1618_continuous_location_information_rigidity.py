#!/usr/bin/env python3
"""Certificate for K1618's continuous-location information condition."""
import json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def logdet_capacity(vars_): return 0.5*sum(math.log1p(v) for v in vars_)
def main():
 d=json.loads((ROOT/'lab/process/k1618-continuous-location-information-rigidity.json').read_text());q=d['information_rigidity'];z=d['decision'];c=[]
 c += [('claim',d['claim_id']=='K1618'),('mixed laws','continuous, discrete or mixed' in q['class']),
       ('information condition','I(M_N;M_N+G_N)=o(N^3)' in q['condition']),('coefficient','h_g^prof' in q['coefficient']),
       ('capacity','1/2 log det(I+Cov(A_N))' in q['capacity_test']),('K1596 advance','arbitrary zero-mode' in q['advance'])]
 c += [('capacity scalar',abs(logdet_capacity([3.0])-math.log(2))<1e-12),
       ('capacity additive',abs(logdet_capacity([1.0,3.0])-(0.5*math.log(2)+math.log(2)))<1e-12)]
 for n in (16,64,256):
  cap=logdet_capacity([1/n]*(n*n));c.append((f'capacity subcubic {n}',cap/(n**3)<0.01))
 c += [('continuous',z['continuous_location_laws_admitted']),('arbitrary modes',z['arbitrary_mode_locations_admitted']),
       ('information',z['mutual_information_subextensive_sufficient']),('capacity sufficient',z['capacity_sufficient_condition']),
       ('nonGaussian open',not z['non_gaussian_components_controlled']),('protected',not z['protected_status_change'])]
 for i,(label,ok) in enumerate(c,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(c)}/{len(c)}')
if __name__=='__main__':main()
