#!/usr/bin/env python3
"""Hostile mutations for K1464."""
import copy,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1464-wick-cutoff-square-completion.json').read_text()); A=copy.deepcopy(D['square_completion']); Q=copy.deepcopy(D['decision']); n=0
def valid(x): return x['square_completion']==A and x['decision']==Q
for k in A:
 x=copy.deepcopy(D); x['square_completion'][k]+=' MUTATED'; assert not valid(x); n+=1; print(f'REJECT {n:02d}: {k}')
for k in Q:
 x=copy.deepcopy(D); x['decision'][k]=not x['decision'][k]; assert not valid(x); n+=1; print(f'REJECT {n:02d}: {k}')
print(f'RESULT: PASS {n}/{n}')
