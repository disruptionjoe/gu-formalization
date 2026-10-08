#!/usr/bin/env python3
"""Mutation probe for K1442."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1442-zero-harmonic-phase-nonresonance.json').read_text())
def validate(x):
 r,q=x['phase_geometry'],x['decision']; e=[]
 for key,needle in [('declared_phase','p in Z^3 minus {0}'),('exact_identity','2(|p| omega_q(k)-p dot k)'),('positive_numerator','M_q^2+|k_perp|^2'),('nonresonance','Phi_q(k,p)>0'),('parallel_asymptotic','2K^2'),('scope','Other sign combinations')]:
  if needle not in r[key]: e.append(key)
 for k in ('strict_zero_harmonic_phase_nonresonant','exact_positive_phase_identity_proved'):
  if not q[k]: e.append(k)
 for k in ('phase_has_uniform_positive_lower_bound_in_k','harmonic_resonance_extends_to_nonzero_modes','full_zero_harmonic_normal_form_constructed','global_full_pde_flow_constructed','protected_status_change'):
  if q[k]: e.append(k)
 return e
assert not validate(D)
M=[('phase',lambda x:x['phase_geometry'].__setitem__('declared_phase','unknown')),('identity',lambda x:x['phase_geometry'].__setitem__('exact_identity','unknown')),('positive',lambda x:x['phase_geometry'].__setitem__('positive_numerator','unknown')),('nonresonance',lambda x:x['phase_geometry'].__setitem__('nonresonance','unknown')),('asymptotic',lambda x:x['phase_geometry'].__setitem__('parallel_asymptotic','unknown')),('scope',lambda x:x['phase_geometry'].__setitem__('scope','unknown')),('decision',lambda x:x['decision'].__setitem__('strict_zero_harmonic_phase_nonresonant',False)),('proof',lambda x:x['decision'].__setitem__('exact_positive_phase_identity_proved',False)),('gap',lambda x:x['decision'].__setitem__('phase_has_uniform_positive_lower_bound_in_k',True)),('harmonic',lambda x:x['decision'].__setitem__('harmonic_resonance_extends_to_nonzero_modes',True)),('normal',lambda x:x['decision'].__setitem__('full_zero_harmonic_normal_form_constructed',True)),('flow',lambda x:x['decision'].__setitem__('global_full_pde_flow_constructed',True)),('protected',lambda x:x['decision'].__setitem__('protected_status_change',True))]
for i,(label,mutate) in enumerate(M,1):
 x=copy.deepcopy(D); mutate(x); assert validate(x),label; print(f'PASS {i:02d}: rejects {label}')
print(f'RESULT: PASS {len(M)}/{len(M)}')
