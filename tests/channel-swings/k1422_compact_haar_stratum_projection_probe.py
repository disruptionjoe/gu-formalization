#!/usr/bin/env python3
"""Mutation probe for K1422."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1422-compact-haar-stratum-projection.json').read_text())
def validate(x):
 h,q=x['haar_projection'],x['decision']; e=[]
 if 'idempotent' not in h['operator_control']: e.append('projector')
 if 'gcd' not in h['orbit_types']: e.append('types')
 for k in ('orthogonal_haar_projection_constructed','invariant_subspace_closed','charge_zero_selection_exact','nonfree_orbit_types_retained'):
  if not q[k]: e.append(k)
 for k in ('global_free_quotient_assumed','continuum_physical_sector_constructed'):
  if q[k]: e.append(k)
 return e
assert not validate(D)
M=[('projector',lambda x:x['haar_projection'].__setitem__('operator_control','unknown')),('types',lambda x:x['haar_projection'].__setitem__('orbit_types','free')),('orthogonal',lambda x:x['decision'].__setitem__('orthogonal_haar_projection_constructed',False)),('closed',lambda x:x['decision'].__setitem__('invariant_subspace_closed',False)),('charge',lambda x:x['decision'].__setitem__('charge_zero_selection_exact',False)),('nonfree',lambda x:x['decision'].__setitem__('nonfree_orbit_types_retained',False)),('free',lambda x:x['decision'].__setitem__('global_free_quotient_assumed',True)),('continuum',lambda x:x['decision'].__setitem__('continuum_physical_sector_constructed',True))]
for i,(label,mutate) in enumerate(M,1):
 x=copy.deepcopy(D); mutate(x); assert validate(x),label; print(f'PASS {i:02d}: rejects {label}')
print(f'RESULT: PASS {len(M)}/{len(M)}')
