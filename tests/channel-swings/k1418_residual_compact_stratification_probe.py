#!/usr/bin/env python3
"""Mutation probe for K1418."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1418-residual-compact-stratification.json').read_text())
def validate(x):
 f,q=x['residual_strata'],x['decision']; e=[]
 if 'gcd' not in f['support_stabilizer']: e.append('gcd')
 if 'orbit-type' not in f['stratification']: e.append('strata')
 for k in ('residual_group_compact','support_stabilizers_classified','residual_action_proper','quotient_hausdorff'):
  if not q[k]: e.append(k)
 for k in ('global_free_action','single_smooth_manifold_quotient','physical_charge_normalization_selected','protected_status_change'):
  if q[k]: e.append(k)
 return e
assert not validate(D)
mutations=[('gcd',lambda x:x['residual_strata'].__setitem__('support_stabilizer','unknown')),('strata',lambda x:x['residual_strata'].__setitem__('stratification','manifold')),('compact',lambda x:x['decision'].__setitem__('residual_group_compact',False)),('proper',lambda x:x['decision'].__setitem__('residual_action_proper',False)),('free',lambda x:x['decision'].__setitem__('global_free_action',True)),('manifold',lambda x:x['decision'].__setitem__('single_smooth_manifold_quotient',True)),('normalization',lambda x:x['decision'].__setitem__('physical_charge_normalization_selected',True)),('protected',lambda x:x['decision'].__setitem__('protected_status_change',True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D); mutate(x); e=validate(x); assert e,label; print(f'PASS {i:02d}: rejects {label} via [FAIL] {e[0]}')
print(f'RESULT: PASS {len(mutations)}/{len(mutations)}')
