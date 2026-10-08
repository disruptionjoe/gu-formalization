#!/usr/bin/env python3
"""Mutation probe for K1431."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1431-quartic-wick-renormalization-boundary.json').read_text())
def validate(x):
 r,q=x['renormalization_boundary'],x['decision']; e=[]
 if '6 Delta C' not in r['conditional_expectation']: e.append('counterterms')
 if 'martingale' not in r['wick_candidate']: e.append('Wick')
 for k in ('naive_quartic_expectation_diverges','mass_and_vacuum_counterterms_forced','wick_quartic_martingale_constructed'):
  if not q[k]: e.append(k)
 if q['bare_quartic_projective_compatibility']: e.append('bare')
 for k in ('uniform_semibounded_interacting_forms_proved','interacting_resolvent_limit_constructed','renormalized_continuum_hamiltonian_constructed','global_nonlinear_pde_proved','protected_status_change'):
  if q[k]: e.append(k)
 return e
assert not validate(D)
M=[('counterterms',lambda x:x['renormalization_boundary'].__setitem__('conditional_expectation','unknown')),('Wick',lambda x:x['renormalization_boundary'].__setitem__('wick_candidate','unknown')),('divergence',lambda x:x['decision'].__setitem__('naive_quartic_expectation_diverges',False)),('bare',lambda x:x['decision'].__setitem__('bare_quartic_projective_compatibility',True)),('forced',lambda x:x['decision'].__setitem__('mass_and_vacuum_counterterms_forced',False)),('martingale',lambda x:x['decision'].__setitem__('wick_quartic_martingale_constructed',False)),('lower',lambda x:x['decision'].__setitem__('uniform_semibounded_interacting_forms_proved',True)),('resolvent',lambda x:x['decision'].__setitem__('interacting_resolvent_limit_constructed',True)),('Hamiltonian',lambda x:x['decision'].__setitem__('renormalized_continuum_hamiltonian_constructed',True)),('PDE',lambda x:x['decision'].__setitem__('global_nonlinear_pde_proved',True))]
for i,(label,mutate) in enumerate(M,1):
 x=copy.deepcopy(D); mutate(x); assert validate(x),label; print(f'PASS {i:02d}: rejects {label}')
print(f'RESULT: PASS {len(M)}/{len(M)}')
