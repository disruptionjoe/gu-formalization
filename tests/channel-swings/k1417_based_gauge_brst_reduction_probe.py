#!/usr/bin/env python3
"""Mutation probe for K1417."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1417-based-gauge-brst-reduction.json').read_text())
def validate(x):
 f,q=x['based_reduction'],x['decision']; e=[]
 if 'no stabilizer' not in f['free_action']: e.append('free')
 if 'contractible' not in f['brst_doublet']: e.append('doublet')
 for k in ('based_action_free','global_coulomb_coordinate_constructed','based_brst_doublet_contracted','positive_based_ghost_cohomology_zero','degree_zero_based_reduction_identified'):
  if not q[k]: e.append(k)
 if q['constant_gauge_group_removed']: e.append('constant')
 if q['protected_status_change']: e.append('protected')
 return e
assert not validate(D)
mutations=[('free prose',lambda x:x['based_reduction'].__setitem__('free_action','unknown')),('doublet prose',lambda x:x['based_reduction'].__setitem__('brst_doublet','unknown')),('free flag',lambda x:x['decision'].__setitem__('based_action_free',False)),('coordinate',lambda x:x['decision'].__setitem__('global_coulomb_coordinate_constructed',False)),('doublet',lambda x:x['decision'].__setitem__('based_brst_doublet_contracted',False)),('cohomology',lambda x:x['decision'].__setitem__('positive_based_ghost_cohomology_zero',False)),('constant',lambda x:x['decision'].__setitem__('constant_gauge_group_removed',True)),('protected',lambda x:x['decision'].__setitem__('protected_status_change',True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D); mutate(x); e=validate(x); assert e,label; print(f'PASS {i:02d}: rejects {label} via [FAIL] {e[0]}')
print(f'RESULT: PASS {len(mutations)}/{len(mutations)}')
