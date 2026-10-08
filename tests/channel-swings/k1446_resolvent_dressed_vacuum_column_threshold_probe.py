#!/usr/bin/env python3
"""Mutation probe for K1446."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1446-resolvent-dressed-vacuum-column-threshold.json').read_text())
def v(x):
 b,q=x['resolvent_column'],x['decision']; e=[]
 for key,needle in [('identity','S_(2r)'),('sharp_threshold','r>5/2'),('one_resolvent_boundary','r=1'),('ceiling','only the vacuum column')]:
  if needle not in b[key]: e.append(key)
 for k in ('sharp_resolvent_column_threshold_proved','converges_for_r_greater_than_five_halves'):
  if not q[k]: e.append(k)
 for k in ('converges_at_r_equal_five_halves','one_resolvent_vacuum_column_converges','full_dressing_constructed','full_interacting_resolvent_constructed','protected_status_change'):
  if q[k]: e.append(k)
 return e
assert not v(D)
M=[('identity',lambda x:x['resolvent_column'].__setitem__('identity','unknown')),('strict',lambda x:x['resolvent_column'].__setitem__('sharp_threshold','r>=5/2')),('one',lambda x:x['resolvent_column'].__setitem__('one_resolvent_boundary','works')),('ceiling',lambda x:x['resolvent_column'].__setitem__('ceiling','full theory')),('threshold',lambda x:x['decision'].__setitem__('sharp_resolvent_column_threshold_proved',False)),('endpoint',lambda x:x['decision'].__setitem__('converges_at_r_equal_five_halves',True)),('one-converges',lambda x:x['decision'].__setitem__('one_resolvent_vacuum_column_converges',True)),('dressing',lambda x:x['decision'].__setitem__('full_dressing_constructed',True)),('resolvent',lambda x:x['decision'].__setitem__('full_interacting_resolvent_constructed',True)),('protected',lambda x:x['decision'].__setitem__('protected_status_change',True))]
for i,(l,m) in enumerate(M,1): x=copy.deepcopy(D); m(x); assert v(x),l; print(f'PASS {i:02d}: rejects {l}')
print(f'RESULT: PASS {len(M)}/{len(M)}')
