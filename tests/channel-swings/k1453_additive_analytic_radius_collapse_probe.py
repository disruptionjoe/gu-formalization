#!/usr/bin/env python3
"""Hostile mutations for K1453."""
import copy,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1453-additive-analytic-radius-collapse.json').read_text()); EXPECT=copy.deepcopy(D['decision']); n=0
def valid(x):
 return x['decision']==EXPECT and 'proof-method obstruction' in x['radius_boundary']['ceiling']
for key in ('finite_radius_global_under_k1450_law','pde_blowup_proved','all_global_hierarchy_routes_excluded','protected_status_change'):
 x=copy.deepcopy(D); x['decision'][key]=not x['decision'][key]; assert not valid(x); n+=1; print(f'REJECT {n:02d}: {key}')
x=copy.deepcopy(D); x['radius_boundary']['ceiling']='global PDE blow-up'; assert not valid(x); n+=1; print(f'REJECT {n:02d}: ceiling')
print(f'RESULT: PASS {n}/{n}')
