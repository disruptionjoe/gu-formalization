#!/usr/bin/env python3
"""Hostile mutations for K1481."""
import copy,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1481-brst-projective-recentering-instability.json').read_text()); A=copy.deepcopy(D['brst_projective_boundary']); Q=copy.deepcopy(D['decision']); n=0
def valid(x): return x['brst_projective_boundary']==A and x['decision']==Q
for key in A:
 x=copy.deepcopy(D); x['brst_projective_boundary'][key]+=' MUTATED'; assert not valid(x); n+=1; print(f'REJECT {n:02d}: {key}')
for key in Q:
 x=copy.deepcopy(D); x['decision'][key]=not x['decision'][key]; assert not valid(x); n+=1; print(f'REJECT {n:02d}: {key}')
print(f'RESULT: PASS {n}/{n}')
