#!/usr/bin/env python3
"""Mutation probe for K1441."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1441-fixed-domain-running-coupling-boundary.json').read_text())
def validate(x):
 r,q=x['running_coupling_boundary'],x['decision']; e=[]
 for key,needle in [('necessary_bound','O(N^-2)'),('fixed_coupling_consequence','fixed nonzero coupling'),('conditional_escape','does not prove'),('renormalization_ceiling','says nothing against')]:
  if needle not in r[key]: e.append(key)
 if not q['quadratic_cutoff_decay_necessary_on_fixed_free_domain']: e.append('necessity')
 for k in ('fixed_nonzero_coupling_passes_free_form_test','quadratic_and_vacuum_counterterms_change_necessary_decay','vanishing_coupling_escape_constructs_nontrivial_interaction','all_renormalization_routes_excluded','protected_status_change'):
  if q[k]: e.append(k)
 return e
assert not validate(D)
M=[('bound',lambda x:x['running_coupling_boundary'].__setitem__('necessary_bound','unknown')),('fixed',lambda x:x['running_coupling_boundary'].__setitem__('fixed_coupling_consequence','unknown')),('escape',lambda x:x['running_coupling_boundary'].__setitem__('conditional_escape','unknown')),('ceiling',lambda x:x['running_coupling_boundary'].__setitem__('renormalization_ceiling','unknown')),('necessity',lambda x:x['decision'].__setitem__('quadratic_cutoff_decay_necessary_on_fixed_free_domain',False)),('fixed-pass',lambda x:x['decision'].__setitem__('fixed_nonzero_coupling_passes_free_form_test',True)),('counterterms',lambda x:x['decision'].__setitem__('quadratic_and_vacuum_counterterms_change_necessary_decay',True)),('nontrivial',lambda x:x['decision'].__setitem__('vanishing_coupling_escape_constructs_nontrivial_interaction',True)),('all',lambda x:x['decision'].__setitem__('all_renormalization_routes_excluded',True)),('protected',lambda x:x['decision'].__setitem__('protected_status_change',True))]
for i,(label,mutate) in enumerate(M,1):
 x=copy.deepcopy(D); mutate(x); assert validate(x),label; print(f'PASS {i:02d}: rejects {label}')
print(f'RESULT: PASS {len(M)}/{len(M)}')
