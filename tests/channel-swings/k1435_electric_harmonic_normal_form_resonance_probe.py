#!/usr/bin/env python3
"""Mutation probe for K1435."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1435-electric-harmonic-normal-form-resonance.json').read_text())
def validate(x):
 r,q=x['resonance'],x['decision']; e=[]
 for key,needle in [('gauss','Im<Q phi'),('time_average','q^(2n+1)'),('bounded_normal_form_obstruction','zero average'),('maxwell_energy_composition','q=4 and q=8'),('scope','zero-harmonic')]:
  if needle not in r[key]: e.append(key)
 for k in ('gauss_compatible_periodic_resonance_constructed','nonzero_lifted_current_time_average_proved'):
  if not q[k]: e.append(k)
 for k in ('bounded_autonomous_cubic_cancellation_possible','one_maxwell_energy_coefficient_cancels_all_charges','zero_harmonic_sector_excluded','all_spacetime_or_hierarchy_mechanisms_excluded','global_full_pde_flow_constructed','protected_status_change'):
  if q[k]: e.append(k)
 return e
assert not validate(D)
M=[('gauss',lambda x:x['resonance'].__setitem__('gauss','unknown')),('average',lambda x:x['resonance'].__setitem__('time_average','unknown')),('normal',lambda x:x['resonance'].__setitem__('bounded_normal_form_obstruction','unknown')),('Maxwell',lambda x:x['resonance'].__setitem__('maxwell_energy_composition','unknown')),('scope',lambda x:x['resonance'].__setitem__('scope','unknown')),('resonance',lambda x:x['decision'].__setitem__('gauss_compatible_periodic_resonance_constructed',False)),('nonzero',lambda x:x['decision'].__setitem__('nonzero_lifted_current_time_average_proved',False)),('cubic',lambda x:x['decision'].__setitem__('bounded_autonomous_cubic_cancellation_possible',True)),('coefficient',lambda x:x['decision'].__setitem__('one_maxwell_energy_coefficient_cancels_all_charges',True)),('zero',lambda x:x['decision'].__setitem__('zero_harmonic_sector_excluded',True)),('all',lambda x:x['decision'].__setitem__('all_spacetime_or_hierarchy_mechanisms_excluded',True)),('flow',lambda x:x['decision'].__setitem__('global_full_pde_flow_constructed',True)),('protected',lambda x:x['decision'].__setitem__('protected_status_change',True))]
for i,(label,mutate) in enumerate(M,1):
 x=copy.deepcopy(D); mutate(x); assert validate(x),label; print(f'PASS {i:02d}: rejects {label}')
print(f'RESULT: PASS {len(M)}/{len(M)}')
