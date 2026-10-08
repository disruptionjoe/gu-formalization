#!/usr/bin/env python3
"""Hostile mutations for K1470."""
import copy,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1470-wick-shift-free-vacuum-concentration.json').read_text()); A=copy.deepcopy(D['free_vacuum_concentration']); Q=copy.deepcopy(D['decision']); n=0
def valid(x): return x['free_vacuum_concentration']==A and x['decision']==Q
for k in A:
 x=copy.deepcopy(D); x['free_vacuum_concentration'][k]+=' MUTATED'; assert not valid(x); n+=1; print(f'REJECT {n:02d}: {k}')
for k in Q:
 x=copy.deepcopy(D); x['decision'][k]=not x['decision'][k] if isinstance(x['decision'][k],bool) else 'MUTATED'; assert not valid(x); n+=1; print(f'REJECT {n:02d}: {k}')
print(f'RESULT: PASS {n}/{n}')
