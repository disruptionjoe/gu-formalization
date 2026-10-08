#!/usr/bin/env python3
"""Controls for K1428's inductive Hilbert and Haar compatibility."""
import cmath,hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1428-inductive-hilbert-haar-compatibility.json').read_text()); n=0
def check(label,value):
 global n
 assert value,label; n+=1; print(f'PASS {n:02d}: {label}')
for key,pin in D['pinned_inputs'].items(): check(f'{key} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
H,Q=D['hilbert_limit'],D['decision']
weights=(.25,.75); f=(2.0,-1.0)
norm=sum(w*x*x for w,x in zip(weights,f))
embedded=tuple(x for x in f for _ in weights)
product_weights=tuple(a*b for a in weights for b in weights)
check('cylinder embedding isometry',abs(sum(w*x*x for w,x in zip(product_weights,embedded))-norm)<1e-12)
averaged=tuple(sum(weights[j]*embedded[2*i+j] for j in range(2)) for i in range(2))
check('conditional expectation left inverse',averaged==f)
charges=(-4,-2,0,2,4); theta=.37
check('coordinate action unitary',all(abs(abs(cmath.exp(1j*q*theta))-1)<1e-12 for q in charges))
check('group law',all(abs(cmath.exp(1j*q*(theta+.2))-cmath.exp(1j*q*theta)*cmath.exp(.2j*q))<1e-12 for q in charges))
check('strong cylinder continuity',max(abs(cmath.exp(1e-8j*q)-1) for q in charges)<5e-8)
for charge in (-6,-2,0,4,8): check(f'Haar charge rule {charge}',(charge==0)==(abs(sum(cmath.exp(1j*charge*2*math.pi*k/64) for k in range(64))/64)>1-1e-9))
for label,key,needle in [('embedding','embedding','isometry'),('adjoint','adjoint','conditional expectation'),('limit','limit','L2(gamma_infinity)'),('circle','circle_action','strongly continuous'),('Haar','haar_compatibility','J_NM P_N'),('boundary','boundary','neither selects')]: check(label,needle in H[key])
for key in ('isometric_cylinder_embeddings_constructed','conditional_expectations_are_adjoints','inductive_limit_identified_with_continuum_L2','strongly_continuous_residual_circle_constructed','haar_projection_refinement_compatible'): check(key,Q[key])
for key in ('charge_sequence_selected_by_source','complete_observable_quantization_constructed','protected_status_change'): check(f'{key} fenced',not Q[key])
print(f'RESULT: PASS {n}/{n}')
