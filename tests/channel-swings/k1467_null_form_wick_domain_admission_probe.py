#!/usr/bin/env python3
"""Hostile mutations for K1467."""
import copy,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1467-null-form-wick-domain-admission.json').read_text()); C=copy.deepcopy(D['bridge_census']); Q=copy.deepcopy(D['decision']); n=0
def valid(x): return x['bridge_census']==C and x['decision']==Q
for k in ('row_count','satisfied_count','conditional_count','excluded_count','missing_count'):
 x=copy.deepcopy(D); x['bridge_census'][k]+=1; assert not valid(x); n+=1; print(f'REJECT {n:02d}: {k}')
for k in Q:
 x=copy.deepcopy(D); x['decision'][k]=not x['decision'][k]; assert not valid(x); n+=1; print(f'REJECT {n:02d}: {k}')
print(f'RESULT: PASS {n}/{n}')
