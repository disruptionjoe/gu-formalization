#!/usr/bin/env python3
"""Mutation probe for K1415."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1415-split-gauss-coordinate.json').read_text())
def validate(x):
 f,q=x['split_coordinate'],x['decision']; e=[]
 if 'div Rg=g' not in f['right_inverse']: e.append('right inverse')
 if 'mutual inverses' not in f['global_identity']: e.append('identity')
 for k in ('gauss_map_globally_split','bounded_right_inverse_constructed','gauss_surface_split_submanifold'):
  if not q[k]: e.append(k)
 for k in ('field_dependent_rank_jump_present','global_unbounded_charge_evolution_constructed','source_gu_constraint_identified','protected_status_change'):
  if q[k]: e.append(k)
 return e
assert not validate(D)
mutations=[('right inverse',lambda x:x['split_coordinate'].__setitem__('right_inverse','unproved')),('identity',lambda x:x['split_coordinate'].__setitem__('global_identity','local only')),('split',lambda x:x['decision'].__setitem__('gauss_map_globally_split',False)),('right inverse flag',lambda x:x['decision'].__setitem__('bounded_right_inverse_constructed',False)),('rank jump',lambda x:x['decision'].__setitem__('field_dependent_rank_jump_present',True)),('evolution',lambda x:x['decision'].__setitem__('global_unbounded_charge_evolution_constructed',True)),('source',lambda x:x['decision'].__setitem__('source_gu_constraint_identified',True)),('protected',lambda x:x['decision'].__setitem__('protected_status_change',True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D); mutate(x); e=validate(x); assert e,label; print(f'PASS {i:02d}: rejects {label} via [FAIL] {e[0]}')
print(f'RESULT: PASS {len(mutations)}/{len(mutations)}')
