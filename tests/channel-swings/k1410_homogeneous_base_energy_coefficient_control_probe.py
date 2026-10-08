#!/usr/bin/env python3
"""Mutation probe for K1410."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1410-homogeneous-base-energy-coefficient-control.json').read_text())
def validate(x):
 f,q=x['coefficient_control'],x['decision']; e=[]
 for key,needle in (('base_energy','H_0='),('conservation','dH_0/dt=0'),('radial_derivative','4H_0/m'),('cutoff_uniformity','no spectral cutoff'),('recurrence_boundary','need not belong to L1')):
  if needle not in f[key]: e.append(key)
 if not q['bound_cutoff_uniform']: e.append('uniform')
 if q['global_time_integrability_claimed']: e.append('L1 overclaim')
 if q['full_pde_pointwise_coefficient_controlled']: e.append('PDE overclaim')
 return e
assert not validate(D)
mutations=[('energy',lambda x:x['coefficient_control'].__setitem__('base_energy','none')),('conservation',lambda x:x['coefficient_control'].__setitem__('conservation','open')),('derivative',lambda x:x['coefficient_control'].__setitem__('radial_derivative','unknown')),('uniform text',lambda x:x['coefficient_control'].__setitem__('cutoff_uniformity','N dependent')),('recurrence',lambda x:x['coefficient_control'].__setitem__('recurrence_boundary','integrable')),('uniform decision',lambda x:x['decision'].__setitem__('bound_cutoff_uniform',False)),('L1',lambda x:x['decision'].__setitem__('global_time_integrability_claimed',True)),('PDE',lambda x:x['decision'].__setitem__('full_pde_pointwise_coefficient_controlled',True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D); mutate(x); e=validate(x); assert e,label; print(f'PASS {i:02d}: rejects {label} via [FAIL] {e[0]}')
print('RESULT: PASS 8/8')
