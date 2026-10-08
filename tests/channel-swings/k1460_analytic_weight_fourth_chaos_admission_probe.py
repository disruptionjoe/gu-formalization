#!/usr/bin/env python3
"""Hostile mutations for K1460."""
import copy,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1460-analytic-weight-fourth-chaos-admission.json').read_text()); EXPECT_C=copy.deepcopy(D['bridge_census']); EXPECT_Q=copy.deepcopy(D['decision']); n=0
def valid(x):
 return x['bridge_census']==EXPECT_C and x['decision']==EXPECT_Q
for key in ('row_count','satisfied_count','conditional_count','excluded_count','missing_count'):
 x=copy.deepcopy(D); x['bridge_census'][key]+=1; assert not valid(x); n+=1; print(f'REJECT {n:02d}: {key}')
for key in D['decision']:
 x=copy.deepcopy(D); x['decision'][key]=not x['decision'][key]; assert not valid(x); n+=1; print(f'REJECT {n:02d}: {key}')
print(f'RESULT: PASS {n}/{n}')
