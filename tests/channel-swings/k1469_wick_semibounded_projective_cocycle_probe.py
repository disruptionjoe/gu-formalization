#!/usr/bin/env python3
"""Hostile mutations for K1469."""
import copy,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1469-wick-semibounded-projective-cocycle.json').read_text()); A=copy.deepcopy(D['scalar_cocycle']); Q=copy.deepcopy(D['decision']); n=0
def valid(x): return x['scalar_cocycle']==A and x['decision']==Q
for k in A:
 x=copy.deepcopy(D); x['scalar_cocycle'][k]+=' MUTATED'; assert not valid(x); n+=1; print(f'REJECT {n:02d}: {k}')
for k in Q:
 x=copy.deepcopy(D); x['decision'][k]=not x['decision'][k]; assert not valid(x); n+=1; print(f'REJECT {n:02d}: {k}')
print(f'RESULT: PASS {n}/{n}')
