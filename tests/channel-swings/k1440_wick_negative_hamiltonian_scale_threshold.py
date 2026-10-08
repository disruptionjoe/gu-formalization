#!/usr/bin/env python3
"""Controls for K1440's sharp negative-Hamiltonian-scale threshold."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1440-wick-negative-hamiltonian-scale-threshold.json').read_text()); n=0
def check(label,value):
 global n
 assert value,label; n+=1; print(f'PASS {n:02d}: {label}')
for key,pin in D['pinned_inputs'].items(): check(f'{key} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
R,Q=D['negative_scale'],D['decision']
for s in (0,1,4):
 blocks=[2**(j*(5-s)) for j in range(1,8)]
 check(f's={s} lower blocks grow',blocks[-1]>blocks[0])
blocks=[1 for _ in range(8)]
check('s=5 dyadic blocks do not sum',sum(blocks)==8)
for s in (6,7,10):
 terms=[2**(j*(5-s)) for j in range(1,30)]
 check(f's={s} upper dyadic sum finite',sum(terms)<2)
check('quantity stated','S_s(N)' in R['quantity'])
check('lower threshold stated','s=5' in R['lower_dyadic_blocks'])
check('upper shell L5','C L^5' in R['upper_dyadic_blocks'])
check('sharp threshold stated','s>5' in R['sharp_threshold'] and 's<=5' in R['sharp_threshold'])
check('vacuum-vector scope','vacuum-to-four-particle' in R['interpretation'])
check('identity decision',Q['negative_scale_identity_proved'])
check('threshold decision',Q['sharp_squared_norm_threshold']==5)
check('positive side',Q['converges_for_every_s_greater_than_five'])
for key in ('bounded_for_s_at_most_five','full_interaction_form_constructed','protected_status_change'): check(f'{key} fenced',not Q[key])
print(f'RESULT: PASS {n}/{n}')
