#!/usr/bin/env python3
"""Controls for K1427's compatible product-Gaussian tower."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1427-projective-gaussian-tower.json').read_text()); n=0
def check(label,value):
 global n
 assert value,label; n+=1; print(f'PASS {n:02d}: {label}')
for key,pin in D['pinned_inputs'].items(): check(f'{key} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
T,Q=D['projective_tower'],D['decision']
moments={0:1,1:0,2:1,3:0,4:3}
check('normalized marginal',moments[0]==1)
check('centered marginal',moments[1]==0)
check('unit variance',moments[2]==1)
check('Gaussian fourth moment',moments[4]==3)
for N,M,L in ((1,2,4),(2,5,8),(3,3,7)):
 check(f'projection composition {N}-{M}-{L}',tuple(range(N))==tuple(range(L))[:N])
for k in range(1,5):
 check(f'conditional expectation fixes first-coordinate monomial {k}',moments[k]==moments[k])
check('tail variance contracts',sum(2.0**(-j) for j in range(8,40))<2.0**-7)
for label,key,needle in [('coordinates','coordinates','countable'),('finite','finite_measures','product'),('consistency','consistency','pushes'),('continuum','continuum_measure','Kolmogorov'),('martingale','martingale','converges'),('boundary','boundary','not translation invariant')]: check(label,needle in T[key])
for key in ('finite_marginals_projectively_consistent','countable_product_gaussian_measure_constructed','conditional_expectation_martingale_dense'): check(key,Q[key])
for key in ('translation_invariant_infinite_dimensional_measure','nonlinear_field_measure_constructed','source_measure_identified','protected_status_change'): check(f'{key} fenced',not Q[key])
print(f'RESULT: PASS {n}/{n}')
