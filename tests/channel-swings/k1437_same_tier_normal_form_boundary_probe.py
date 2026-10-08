#!/usr/bin/env python3
"""Mutation probe for K1437."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1437-same-tier-normal-form-boundary.json').read_text())
def validate(x):
 b,q=x['combined_boundary'],x['decision']; e=[]
 for key,needle in [('admitted_class','same-spatial-tier'),('electric_result','periodic-orbit'),('radial_result','K^2'),('joint_conclusion','both K1413'),('claim_ceiling','not a no-go')]:
  if needle not in b[key]: e.append(key)
 if len(b['surviving_routes'])!=4: e.append('routes')
 if not q['electric_and_radial_leakage_jointly_replayed']: e.append('replay')
 if q['bounded_same_tier_time_local_polynomial_normal_form_closes_both']: e.append('closure')
 for k in ('zero_harmonic_nonzero_mode_route_open','spacetime_and_hierarchy_routes_open'):
  if not q[k]: e.append(k)
 for k in ('finite_tier_cauchy_consequence_constructed','completed_full_pde_flow_constructed','protected_status_change'):
  if q[k]: e.append(k)
 return e
assert not validate(D)
M=[('class',lambda x:x['combined_boundary'].__setitem__('admitted_class','unknown')),('electric',lambda x:x['combined_boundary'].__setitem__('electric_result','unknown')),('radial',lambda x:x['combined_boundary'].__setitem__('radial_result','unknown')),('joint',lambda x:x['combined_boundary'].__setitem__('joint_conclusion','unknown')),('ceiling',lambda x:x['combined_boundary'].__setitem__('claim_ceiling','unknown')),('routes',lambda x:x['combined_boundary'].__setitem__('surviving_routes',[])),('replay',lambda x:x['decision'].__setitem__('electric_and_radial_leakage_jointly_replayed',False)),('closure',lambda x:x['decision'].__setitem__('bounded_same_tier_time_local_polynomial_normal_form_closes_both',True)),('zero',lambda x:x['decision'].__setitem__('zero_harmonic_nonzero_mode_route_open',False)),('space',lambda x:x['decision'].__setitem__('spacetime_and_hierarchy_routes_open',False)),('Cauchy',lambda x:x['decision'].__setitem__('finite_tier_cauchy_consequence_constructed',True)),('flow',lambda x:x['decision'].__setitem__('completed_full_pde_flow_constructed',True)),('protected',lambda x:x['decision'].__setitem__('protected_status_change',True))]
for i,(label,mutate) in enumerate(M,1):
 x=copy.deepcopy(D); mutate(x); assert validate(x),label; print(f'PASS {i:02d}: rejects {label}')
print(f'RESULT: PASS {len(M)}/{len(M)}')
