#!/usr/bin/env python3
"""Mutation probe for K1438."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1438-quantum-pde-admission.json').read_text())
def validate(x):
 b,q=x['bridge_census'],x['decision']; e=[]
 if b['row_count']!=sum(b[k] for k in ('satisfied_count','conditional_count','excluded_count','missing_count')): e.append('sum')
 if len(b['new_satisfied_rows'])!=4: e.append('satisfied')
 if len(b['new_excluded_rows'])!=5: e.append('excluded')
 if len(b['missing_rows'])!=4: e.append('missing')
 for k in ('three_dimensional_wick_L2_multiplication_limit_constructed','renormalized_interacting_form_or_resolvent_constructed','bounded_same_tier_normal_form_closes_full_pde','completed_full_pde_global_flow_constructed','source_selected_reduction_constructed','protected_status_change'):
  if q[k]: e.append(k)
 if not q['zero_harmonic_spacetime_and_hierarchy_routes_remain_open']: e.append('routes')
 return e
assert not validate(D)
M=[('sum',lambda x:x['bridge_census'].__setitem__('row_count',105)),('satisfied',lambda x:x['bridge_census'].__setitem__('new_satisfied_rows',[])),('excluded',lambda x:x['bridge_census'].__setitem__('new_excluded_rows',[])),('missing',lambda x:x['bridge_census'].__setitem__('missing_rows',[])),('wick',lambda x:x['decision'].__setitem__('three_dimensional_wick_L2_multiplication_limit_constructed',True)),('operator',lambda x:x['decision'].__setitem__('renormalized_interacting_form_or_resolvent_constructed',True)),('normal',lambda x:x['decision'].__setitem__('bounded_same_tier_normal_form_closes_full_pde',True)),('routes',lambda x:x['decision'].__setitem__('zero_harmonic_spacetime_and_hierarchy_routes_remain_open',False)),('flow',lambda x:x['decision'].__setitem__('completed_full_pde_global_flow_constructed',True)),('source',lambda x:x['decision'].__setitem__('source_selected_reduction_constructed',True)),('protected',lambda x:x['decision'].__setitem__('protected_status_change',True))]
for i,(label,mutate) in enumerate(M,1):
 x=copy.deepcopy(D); mutate(x); assert validate(x),label; print(f'PASS {i:02d}: rejects {label}')
print(f'RESULT: PASS {len(M)}/{len(M)}')
