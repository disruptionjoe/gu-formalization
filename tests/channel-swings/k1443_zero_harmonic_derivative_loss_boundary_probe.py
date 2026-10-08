#!/usr/bin/env python3
"""Mutation probe for K1443."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1443-zero-harmonic-derivative-loss-boundary.json').read_text())
def validate(x):
 r,q=x['derivative_boundary'],x['decision']; e=[]
 for key,needle in [('homological_multiplier','Phi_q(k,p)^(-1)'),('upper_bound','<k>^2'),('optimality','alpha<2'),('finite_tier_cauchy_consequence','Cauchy in h^(s+2)'),('same_tier_boundary','does not restore a same-tier'),('full_pde_ceiling','differentiated current numerator')]:
  if needle not in r[key]: e.append(key)
 for k in ('fixed_nonzero_mode_homological_inverse_constructed','two_derivative_mapping_bound_proved','two_derivative_loss_optimal','finite_tier_scalar_cauchy_implication_proved'):
  if not q[k]: e.append(k)
 for k in ('same_tier_zero_harmonic_normal_form_bounded','full_nonlinear_zero_harmonic_normal_form_constructed','global_full_pde_flow_constructed','protected_status_change'):
  if q[k]: e.append(k)
 return e
assert not validate(D)
M=[('multiplier',lambda x:x['derivative_boundary'].__setitem__('homological_multiplier','unknown')),('upper',lambda x:x['derivative_boundary'].__setitem__('upper_bound','unknown')),('optimal',lambda x:x['derivative_boundary'].__setitem__('optimality','unknown')),('cauchy',lambda x:x['derivative_boundary'].__setitem__('finite_tier_cauchy_consequence','unknown')),('tier',lambda x:x['derivative_boundary'].__setitem__('same_tier_boundary','unknown')),('ceiling',lambda x:x['derivative_boundary'].__setitem__('full_pde_ceiling','unknown')),('inverse',lambda x:x['decision'].__setitem__('fixed_nonzero_mode_homological_inverse_constructed',False)),('bound',lambda x:x['decision'].__setitem__('two_derivative_mapping_bound_proved',False)),('optimality',lambda x:x['decision'].__setitem__('two_derivative_loss_optimal',False)),('implication',lambda x:x['decision'].__setitem__('finite_tier_scalar_cauchy_implication_proved',False)),('same',lambda x:x['decision'].__setitem__('same_tier_zero_harmonic_normal_form_bounded',True)),('full',lambda x:x['decision'].__setitem__('full_nonlinear_zero_harmonic_normal_form_constructed',True)),('flow',lambda x:x['decision'].__setitem__('global_full_pde_flow_constructed',True)),('protected',lambda x:x['decision'].__setitem__('protected_status_change',True))]
for i,(label,mutate) in enumerate(M,1):
 x=copy.deepcopy(D); mutate(x); assert validate(x),label; print(f'PASS {i:02d}: rejects {label}')
print(f'RESULT: PASS {len(M)}/{len(M)}')
