#!/usr/bin/env python3
"""Hostile mutations for K1458."""
import copy,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1458-general-fourth-chaos-projection-criterion.json').read_text()); EXPECT=copy.deepcopy(D['decision']); n=0
def valid(x):
 return x['decision']==EXPECT
for key in D['decision']:
 x=copy.deepcopy(D); x['decision'][key]=not x['decision'][key]; assert not valid(x); n+=1; print(f'REJECT {n:02d}: {key}')
print(f'RESULT: PASS {n}/{n}')
