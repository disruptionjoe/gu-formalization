#!/usr/bin/env python3
"""Hostile mutations for K1463."""
import copy,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1463-transverse-current-null-form-mismatch.json').read_text()); A=copy.deepcopy(D['current_mismatch']); Q=copy.deepcopy(D['decision']); n=0
def valid(x): return x['current_mismatch']==A and x['decision']==Q
for k in A:
 x=copy.deepcopy(D); x['current_mismatch'][k]+=' MUTATED'; assert not valid(x); n+=1; print(f'REJECT {n:02d}: {k}')
for k in Q:
 x=copy.deepcopy(D); x['decision'][k]=not x['decision'][k]; assert not valid(x); n+=1; print(f'REJECT {n:02d}: {k}')
print(f'RESULT: PASS {n}/{n}')
