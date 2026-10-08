#!/usr/bin/env python3
"""Controls for K1421's finite-cylindrical Schrödinger representation."""
import cmath,hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1421-cylindrical-schrodinger-representation.json').read_text()); n=0
def check(label,value):
 global n
 assert value,label; n+=1; print(f'PASS {n:02d}: {label}')
for key,pin in D['pinned_inputs'].items(): check(f'{key} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
R,Q=D['representation'],D['decision']
charges=(-4,-2,0,2,4); theta=.371
phases=[cmath.exp(1j*theta*q) for q in charges]
check('integer charges',all(isinstance(q,int) for q in charges))
check('unit phases',all(abs(abs(z)-1)<1e-12 for z in phases))
check('group law',all(abs(cmath.exp(1j*(theta+.2)*q)-cmath.exp(1j*theta*q)*cmath.exp(.2j*q))<1e-12 for q in charges))
check('strong finite continuity',max(abs(cmath.exp(1e-8j*q)-1) for q in charges)<5e-8)
for label,key,needle in [('block','block','finite'),('measure','measure','Gaussian'),('space','hilbert_space','L2'),('action','circle_action','unitary'),('core','dense_core','dense'),('observables','observables','bounded'),('boundary','boundary','neither')]: check(label,needle in R[key])
for key in ('positive_finite_cylindrical_representation','residual_circle_unitary','dense_invariant_polynomial_core','bounded_invariant_multipliers_represented'): check(key,Q[key])
for key in ('preferred_continuum_measure_constructed','complete_observable_algebra_quantized','source_representation_identified','protected_status_change'): check(f'{key} fenced',not Q[key])
print(f'RESULT: PASS {n}/{n}')
