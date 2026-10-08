#!/usr/bin/env python3
"""Hostile mutations for K1476."""
import copy,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1476-brst-resolvent-collapse-and-recentering-boundary.json').read_text()); A=copy.deepcopy(D['brst_spectral_boundary']); Q=copy.deepcopy(D['decision']); n=0
def valid(x): return x['brst_spectral_boundary']==A and x['decision']==Q
for k in A:
 x=copy.deepcopy(D); x['brst_spectral_boundary'][k]+=' MUTATED'; assert not valid(x); n+=1; print(f'REJECT {n:02d}: {k}')
for k in Q:
 x=copy.deepcopy(D); x['decision'][k]=not x['decision'][k]; assert not valid(x); n+=1; print(f'REJECT {n:02d}: {k}')
print(f'RESULT: PASS {n}/{n}')
