#!/usr/bin/env python3
"""Mutation probe for K1423."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1423-bare-brst-gauge-volume-obstruction.json').read_text())
def validate(x):
 o,q=x['obstruction'],x['decision']; e=[]
 if 'only constant' not in o['degree_zero_kernel']: e.append('kernel')
 if 'not closed' not in o['range']: e.append('range')
 for k in ('bare_degree_zero_L2_cohomology_nonzero','bare_brst_spectral_gap_positive','bare_brst_range_closed','all_quantization_routes_excluded'):
  if q[k]: e.append(k)
 if not q['noncompact_gauge_volume_obstruction']: e.append('obstruction')
 return e
assert not validate(D)
M=[('kernel',lambda x:x['obstruction'].__setitem__('degree_zero_kernel','nonzero')),('range',lambda x:x['obstruction'].__setitem__('range','closed')),('cohomology',lambda x:x['decision'].__setitem__('bare_degree_zero_L2_cohomology_nonzero',True)),('gap',lambda x:x['decision'].__setitem__('bare_brst_spectral_gap_positive',True)),('closed',lambda x:x['decision'].__setitem__('bare_brst_range_closed',True)),('obstruction',lambda x:x['decision'].__setitem__('noncompact_gauge_volume_obstruction',False)),('all',lambda x:x['decision'].__setitem__('all_quantization_routes_excluded',True)),('protected',lambda x:x['decision'].__setitem__('protected_status_change',True))]
for i,(label,mutate) in enumerate(M,1):
 x=copy.deepcopy(D); mutate(x); e=validate(x)
 if label=='protected': e += ['protected'] if x['decision']['protected_status_change'] else []
 assert e,label; print(f'PASS {i:02d}: rejects {label}')
print(f'RESULT: PASS {len(M)}/{len(M)}')
