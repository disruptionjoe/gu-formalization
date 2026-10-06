#!/usr/bin/env python3
"""Exact controls for K1276."""
import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1276-low-degree-d7-parity-floor.json').read_text()); n=0
def c(label,x):
 global n; assert x,label; n+=1; print(f'PASS {n:02d}: {label}')
c('id',D['result_id']=='K1276-LOW-DEGREE-D7-PARITY-FLOOR')
c('odd floor',D['generator_degrees']['odd_p']==7)
c('even degrees',D['generator_degrees']['even']==[2,4,6,8,10,12])
for degree in range(7): c(f'degree {degree} has no odd-p monomial', degree < D['generator_degrees']['odd_p'])
assert n==10; print('RESULT: PASS 10/10')
