#!/usr/bin/env python3
"""Mutation probe for K1436."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1436-radial-charge-density-curl-obstruction.json').read_text())
def validate(x):
 r,q=x['radial_obstruction'],x['decision']; e=[]
 for key,needle in [('two_charge_coordinates','|q|!=|r|'),('curl','r^(2n)-q^(2n)'),('density_no_go','No derivative-free'),('small_divisor','4K^2'),('derivative_cost','two spatial derivatives'),('scope','summable hierarchies')]:
  if needle not in r[key]: e.append(key)
 for k in ('radial_one_form_nonclosed_on_unequal_charges','two_spatial_derivative_cost_proved'):
  if not q[k]: e.append(k)
 for k in ('derivative_free_quartic_density_cancellation_possible','normal_form_symbol_same_tier_bounded','all_radial_mechanisms_excluded','global_full_pde_flow_constructed','protected_status_change'):
  if q[k]: e.append(k)
 return e
assert not validate(D)
M=[('coordinates',lambda x:x['radial_obstruction'].__setitem__('two_charge_coordinates','unknown')),('curl',lambda x:x['radial_obstruction'].__setitem__('curl','unknown')),('density',lambda x:x['radial_obstruction'].__setitem__('density_no_go','unknown')),('divisor',lambda x:x['radial_obstruction'].__setitem__('small_divisor','unknown')),('cost',lambda x:x['radial_obstruction'].__setitem__('derivative_cost','unknown')),('scope',lambda x:x['radial_obstruction'].__setitem__('scope','unknown')),('nonclosed',lambda x:x['decision'].__setitem__('radial_one_form_nonclosed_on_unequal_charges',False)),('density_possible',lambda x:x['decision'].__setitem__('derivative_free_quartic_density_cancellation_possible',True)),('bounded',lambda x:x['decision'].__setitem__('normal_form_symbol_same_tier_bounded',True)),('loss',lambda x:x['decision'].__setitem__('two_spatial_derivative_cost_proved',False)),('all',lambda x:x['decision'].__setitem__('all_radial_mechanisms_excluded',True)),('flow',lambda x:x['decision'].__setitem__('global_full_pde_flow_constructed',True)),('protected',lambda x:x['decision'].__setitem__('protected_status_change',True))]
for i,(label,mutate) in enumerate(M,1):
 x=copy.deepcopy(D); mutate(x); assert validate(x),label; print(f'PASS {i:02d}: rejects {label}')
print(f'RESULT: PASS {len(M)}/{len(M)}')
