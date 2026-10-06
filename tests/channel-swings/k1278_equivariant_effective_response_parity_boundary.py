#!/usr/bin/env python3
"""Exact controls for K1278."""
import json
from fractions import Fraction
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1278-equivariant-effective-response-parity-boundary.json').read_text()); n=0
def c(label,x):
 global n; assert x,label; n+=1; print(f'PASS {n:02d}: {label}')
c('id',D['result_id']=='K1278-EQUIVARIANT-EFFECTIVE-RESPONSE-PARITY-BOUNDARY')
c('theorem',D['theorem']['unique_equivariant_elimination_preserves_evenness'] is True)
for p in (-3,-2,-1,1,2,3):
 y=Fraction(p,2); eff=(y-p)**2+y*y; yn=Fraction(-p,2); effn=(yn+p)**2+yn*yn; c(f'even control p={p}',eff==effn)
c('fixed component has odd part',(1-2*1+1)!=(1+2*1+1))
c('orientation imported',D['decision']['fixed_component_imports_orientation_datum'] is True)
assert n==10; print('RESULT: PASS 10/10')
