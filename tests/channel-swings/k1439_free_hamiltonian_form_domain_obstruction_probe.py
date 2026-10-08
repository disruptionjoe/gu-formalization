#!/usr/bin/env python3
"""Mutation probe for K1439."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1439-free-hamiltonian-form-domain-obstruction.json').read_text())
def validate(x):
 r,q=x['form_domain_obstruction'],x['decision']; e=[]
 for key,needle in [('dual_norm_identity','(H_0+1)^(-1/2)'),('cone_lower_bound','N^4'),('necessary_form_test','uniformly continuous'),('lower_chaos_counterterms','zeroth and second'),('conclusion','not uniformly KLMN-form-bounded'),('operator_ceiling','does not exclude')]:
  if needle not in r[key]: e.append(key)
 if not q['free_form_dual_norm_identity_proved']: e.append('identity')
 if q['three_dimensional_free_form_dual_lower_bound_order']!='N^4': e.append('growth')
 for k in ('uniform_fixed_coupling_free_form_bound','quadratic_and_vacuum_counterterms_cancel_four_particle_sector','all_interacting_resolvent_limits_excluded','source_hamiltonian_identified','protected_status_change'):
  if q[k]: e.append(k)
 return e
assert not validate(D)
M=[('identity-text',lambda x:x['form_domain_obstruction'].__setitem__('dual_norm_identity','unknown')),('growth-text',lambda x:x['form_domain_obstruction'].__setitem__('cone_lower_bound','unknown')),('test',lambda x:x['form_domain_obstruction'].__setitem__('necessary_form_test','unknown')),('counterterms',lambda x:x['form_domain_obstruction'].__setitem__('lower_chaos_counterterms','unknown')),('conclusion',lambda x:x['form_domain_obstruction'].__setitem__('conclusion','unknown')),('ceiling',lambda x:x['form_domain_obstruction'].__setitem__('operator_ceiling','unknown')),('identity',lambda x:x['decision'].__setitem__('free_form_dual_norm_identity_proved',False)),('order',lambda x:x['decision'].__setitem__('three_dimensional_free_form_dual_lower_bound_order','N^3')),('form',lambda x:x['decision'].__setitem__('uniform_fixed_coupling_free_form_bound',True)),('cancel',lambda x:x['decision'].__setitem__('quadratic_and_vacuum_counterterms_cancel_four_particle_sector',True)),('all',lambda x:x['decision'].__setitem__('all_interacting_resolvent_limits_excluded',True)),('source',lambda x:x['decision'].__setitem__('source_hamiltonian_identified',True)),('protected',lambda x:x['decision'].__setitem__('protected_status_change',True))]
for i,(label,mutate) in enumerate(M,1):
 x=copy.deepcopy(D); mutate(x); assert validate(x),label; print(f'PASS {i:02d}: rejects {label}')
print(f'RESULT: PASS {len(M)}/{len(M)}')
