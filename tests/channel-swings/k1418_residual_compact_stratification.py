#!/usr/bin/env python3
"""Controls for K1418's residual compact orbit stratification."""
import hashlib,json,math
from functools import reduce
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1418-residual-compact-stratification.json').read_text()); n=0
def check(label,value):
 global n
 assert value,label; n+=1; print(f'PASS {n:02d}: {label}')
for key,pin in D['pinned_inputs'].items(): check(f'{key} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
F,Q=D['residual_strata'],D['decision']
for label,key,needle in [('group','group','compact circle'),('stabilizer','support_stabilizer','gcd'),('neutral','neutral_stabilizer','full residual'),('free','free_stratum','gcd one'),('proper','properness','proper'),('strata','stratification','orbit-type'),('energy','energy','descends'),('boundary','boundary','hilbert-space representation')]: check(label,needle in F[key].lower())
for support,expected in (((1,2),1),((4,8),4),((6,10,14),2)):
 d=reduce(math.gcd,support); check(f'gcd stabilizer {support}',d==expected)
for key in ('residual_group_compact','support_stabilizers_classified','residual_action_proper','quotient_hausdorff'): check(key,Q[key])
for key in ('global_free_action','single_smooth_manifold_quotient','physical_charge_normalization_selected','protected_status_change'): check(f'{key} fenced',not Q[key])
print(f'RESULT: PASS {n}/{n}')
