#!/usr/bin/env python3
"""Hostile mutations for K1480."""
import copy,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1480-projective-wick-recentering-instability.json').read_text()); A=copy.deepcopy(D['projective_instability']); Q=copy.deepcopy(D['decision']); n=0
def valid(x): return x['projective_instability']==A and x['decision']==Q
for key in A:
 x=copy.deepcopy(D); x['projective_instability'][key]+=' MUTATED'; assert not valid(x); n+=1; print(f'REJECT {n:02d}: {key}')
for key in Q:
 x=copy.deepcopy(D); x['decision'][key]=not x['decision'][key]; assert not valid(x); n+=1; print(f'REJECT {n:02d}: {key}')
print(f'RESULT: PASS {n}/{n}')
