#!/usr/bin/env python3
"""Mutation probe for K1440."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1440-wick-negative-hamiltonian-scale-threshold.json').read_text())
def validate(x):
 r,q=x['negative_scale'],x['decision']; e=[]
 for key,needle in [('quantity','S_s(N)'),('lower_dyadic_blocks','s=5'),('upper_dyadic_blocks','C L^5'),('sharp_threshold','s>5'),('interpretation','vacuum-to-four-particle')]:
  if needle not in r[key]: e.append(key)
 for k in ('negative_scale_identity_proved','converges_for_every_s_greater_than_five'):
  if not q[k]: e.append(k)
 if q['sharp_squared_norm_threshold']!=5: e.append('threshold')
 for k in ('bounded_for_s_at_most_five','full_interaction_form_constructed','protected_status_change'):
  if q[k]: e.append(k)
 return e
assert not validate(D)
M=[('quantity',lambda x:x['negative_scale'].__setitem__('quantity','unknown')),('lower',lambda x:x['negative_scale'].__setitem__('lower_dyadic_blocks','unknown')),('upper',lambda x:x['negative_scale'].__setitem__('upper_dyadic_blocks','unknown')),('sharp',lambda x:x['negative_scale'].__setitem__('sharp_threshold','unknown')),('scope',lambda x:x['negative_scale'].__setitem__('interpretation','unknown')),('identity',lambda x:x['decision'].__setitem__('negative_scale_identity_proved',False)),('threshold',lambda x:x['decision'].__setitem__('sharp_squared_norm_threshold',4)),('converges',lambda x:x['decision'].__setitem__('converges_for_every_s_greater_than_five',False)),('bounded',lambda x:x['decision'].__setitem__('bounded_for_s_at_most_five',True)),('form',lambda x:x['decision'].__setitem__('full_interaction_form_constructed',True)),('protected',lambda x:x['decision'].__setitem__('protected_status_change',True))]
for i,(label,mutate) in enumerate(M,1):
 x=copy.deepcopy(D); mutate(x); assert validate(x),label; print(f'PASS {i:02d}: rejects {label}')
print(f'RESULT: PASS {len(M)}/{len(M)}')
