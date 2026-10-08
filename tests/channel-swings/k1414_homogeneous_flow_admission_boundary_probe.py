#!/usr/bin/env python3
"""Mutation probe for K1414."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1414-homogeneous-flow-admission-boundary.json').read_text())
def validate(x):
 b,q=x['bridge_census'],x['decision']; e=[]
 if b['row_count']!=sum(b[k] for k in ('satisfied_count','conditional_count','excluded_count','missing_count')): e.append('census')
 if (b['row_count'],b['satisfied_count'],b['conditional_count'],b['excluded_count'],b['missing_count'])!=(81,56,6,15,4): e.append('counts')
 if len(b['new_satisfied_rows'])!=4: e.append('new satisfied')
 if len(b['new_excluded_rows'])!=1: e.append('new excluded')
 if not q['homogeneous_completed_global_flow_constructed']: e.append('homogeneous decision')
 for key in ('completed_full_pde_global_flow_constructed','positive_gu_physical_hilbert_cohomology_constructed','source_selected_reduction_constructed','protected_status_change'):
  if q[key]: e.append(key)
 return e
assert not validate(D)
mutations=[('census',lambda x:x['bridge_census'].__setitem__('row_count',80)),('satisfied',lambda x:x['bridge_census'].__setitem__('satisfied_count',57)),('conditional',lambda x:x['bridge_census'].__setitem__('conditional_count',5)),('new satisfied',lambda x:x['bridge_census'].__setitem__('new_satisfied_rows',[])),('new excluded',lambda x:x['bridge_census'].__setitem__('new_excluded_rows',[])),('homogeneous',lambda x:x['decision'].__setitem__('homogeneous_completed_global_flow_constructed',False)),('PDE',lambda x:x['decision'].__setitem__('completed_full_pde_global_flow_constructed',True)),('physical',lambda x:x['decision'].__setitem__('positive_gu_physical_hilbert_cohomology_constructed',True)),('source',lambda x:x['decision'].__setitem__('source_selected_reduction_constructed',True)),('protected',lambda x:x['decision'].__setitem__('protected_status_change',True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D); mutate(x); e=validate(x); assert e,label; print(f'PASS {i:02d}: rejects {label} via [FAIL] {e[0]}')
print('RESULT: PASS 10/10')
