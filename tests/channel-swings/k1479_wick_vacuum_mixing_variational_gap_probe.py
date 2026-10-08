#!/usr/bin/env python3
"""Hostile mutations for K1479."""
import copy,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1479-wick-vacuum-mixing-variational-gap.json').read_text()); A=copy.deepcopy(D['variational_gap']); Q=copy.deepcopy(D['decision']); n=0
def valid(x): return x['variational_gap']==A and x['decision']==Q
for key in A:
 x=copy.deepcopy(D); x['variational_gap'][key]+=' MUTATED'; assert not valid(x); n+=1; print(f'REJECT {n:02d}: {key}')
for key in Q:
 x=copy.deepcopy(D); x['decision'][key]=not x['decision'][key] if isinstance(x['decision'][key],bool) else 'MUTATED'; assert not valid(x); n+=1; print(f'REJECT {n:02d}: {key}')
print(f'RESULT: PASS {n}/{n}')
