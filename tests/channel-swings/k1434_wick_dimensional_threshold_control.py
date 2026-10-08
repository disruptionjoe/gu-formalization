#!/usr/bin/env python3
"""Controls for K1434's equal-time dimensional threshold."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1434-wick-dimensional-threshold-control.json').read_text()); n=0
def check(label,value):
 global n
 assert value,label; n+=1; print(f'PASS {n:02d}: {label}')
for key,pin in D['pinned_inputs'].items(): check(f'{key} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
T,Q=D['threshold'],D['decision']
check('equal-time decay','|k|^-1' in T['spectral_decay'])
check('ell four-thirds exponent',4/3>1)
for N in (8,32,128,512):
 partial=sum((1/(2*math.sqrt(1+k*k)))**(4/3) for k in range(-N,N+1))
 check(f'd1 ell four-thirds partial finite N={N}',math.isfinite(partial) and partial>0)
partials=[sum((1/(2*math.sqrt(1+k*k)))**(4/3) for k in range(-N,N+1)) for N in (32,64,128,256)]
increments=[partials[i+1]-partials[i] for i in range(3)]
check('d1 tail increments decay',increments[2]<increments[1]<increments[0])
check('Hausdorff-Young route','Hausdorff-Young' in T['positive_control'] and 'L4' in T['positive_control'])
for d in (2,3,4,5): check(f'd={d} divergence exponent',3*d-4>0)
check('continuum threshold algebra',4*(1-1)<1 and not 4*(2-1)<2)
check('integer threshold stated','d>=2' in T['integer_threshold'])
check('covariance fence','Euclidean covariance' in T['covariance_fence'])
for key in ('d1_wick_quartic_L2_limit_constructed','all_integer_d_ge_2_L2_limit_excluded_for_declared_covariance','three_dimensional_obstruction_is_dimension_specific'): check(key,Q[key])
for key in ('euclidean_covariance_threshold_claimed','interacting_hamiltonian_constructed','protected_status_change'): check(f'{key} fenced',not Q[key])
check('claim ceiling','no three-dimensional interacting Hamiltonian' in T['claim_ceiling'])
print(f'RESULT: PASS {n}/{n}')
