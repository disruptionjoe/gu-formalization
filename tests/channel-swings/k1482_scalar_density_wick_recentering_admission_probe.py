#!/usr/bin/env python3
"""Hostile mutations for K1482."""
import copy,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1482-scalar-density-wick-recentering-admission.json').read_text()); B=copy.deepcopy(D['bridge_census']); Q=copy.deepcopy(D['decision']); S=D['source_and_ledger_effect']; n=0
def valid(x): return x['bridge_census']==B and x['decision']==Q and x['source_and_ledger_effect']==S
for key in B:
 x=copy.deepcopy(D); x['bridge_census'][key]=0 if isinstance(x['bridge_census'][key],int) else []; assert not valid(x); n+=1; print(f'REJECT {n:02d}: {key}')
for key in Q:
 x=copy.deepcopy(D); x['decision'][key]=not x['decision'][key]; assert not valid(x); n+=1; print(f'REJECT {n:02d}: {key}')
x=copy.deepcopy(D); x['source_and_ledger_effect']='MUTATED'; assert not valid(x); n+=1; print(f'REJECT {n:02d}: source_and_ledger_effect')
print(f'RESULT: PASS {n}/{n}')
