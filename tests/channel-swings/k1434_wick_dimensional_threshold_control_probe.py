#!/usr/bin/env python3
"""Mutation probe for K1434."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1434-wick-dimensional-threshold-control.json').read_text())
def validate(x):
 t,q=x['threshold'],x['decision']; e=[]
 if '|k|^-1' not in t['spectral_decay']: e.append('decay')
 if 'Hausdorff-Young' not in t['positive_control']: e.append('positive')
 if 'd>=2' not in t['integer_threshold']: e.append('threshold')
 if 'Euclidean covariance' not in t['covariance_fence']: e.append('fence')
 for k in ('d1_wick_quartic_L2_limit_constructed','all_integer_d_ge_2_L2_limit_excluded_for_declared_covariance','three_dimensional_obstruction_is_dimension_specific'):
  if not q[k]: e.append(k)
 for k in ('euclidean_covariance_threshold_claimed','interacting_hamiltonian_constructed','protected_status_change'):
  if q[k]: e.append(k)
 return e
assert not validate(D)
M=[('decay',lambda x:x['threshold'].__setitem__('spectral_decay','unknown')),('positive',lambda x:x['threshold'].__setitem__('positive_control','unknown')),('threshold',lambda x:x['threshold'].__setitem__('integer_threshold','unknown')),('fence',lambda x:x['threshold'].__setitem__('covariance_fence','unknown')),('d1',lambda x:x['decision'].__setitem__('d1_wick_quartic_L2_limit_constructed',False)),('d2',lambda x:x['decision'].__setitem__('all_integer_d_ge_2_L2_limit_excluded_for_declared_covariance',False)),('specific',lambda x:x['decision'].__setitem__('three_dimensional_obstruction_is_dimension_specific',False)),('Euclidean',lambda x:x['decision'].__setitem__('euclidean_covariance_threshold_claimed',True)),('Hamiltonian',lambda x:x['decision'].__setitem__('interacting_hamiltonian_constructed',True)),('protected',lambda x:x['decision'].__setitem__('protected_status_change',True))]
for i,(label,mutate) in enumerate(M,1):
 x=copy.deepcopy(D); mutate(x); assert validate(x),label; print(f'PASS {i:02d}: rejects {label}')
print(f'RESULT: PASS {len(M)}/{len(M)}')
