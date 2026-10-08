#!/usr/bin/env python3
"""Controls for K1443's optimal two-derivative homological boundary."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1443-zero-harmonic-derivative-loss-boundary.json').read_text()); n=0
def check(label,value):
 global n
 assert value,label; n+=1; print(f'PASS {n:02d}: {label}')
for key,pin in D['pinned_inputs'].items(): check(f'{key} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
R,Q=D['derivative_boundary'],D['decision']
M2=5.0; r=1.0
def phi(K): return r+math.sqrt(M2+K*K)-math.sqrt(M2+(K+r)**2)
ratios=[(1/phi(K))/(K*K) for K in (100,200,400,800)]
check('inverse phase quadratic limit',abs(ratios[-1]-2/(M2*r))<.005)
check('quadratic convergence',abs(ratios[-1]-2/(M2*r))<abs(ratios[0]-2/(M2*r)))
for s in (-1,0,2,5):
 values=[(1+K*K)**(s/2)*(1/phi(K))/(1+K*K)**((s+2)/2) for K in (10,50,100,500)]
 check(f'h{s+2} to h{s} ratios bounded',max(values)<1)
check('multiplier declared','Phi_q(k,p)^(-1)' in R['homological_multiplier'])
check('upper two-derivative bound','<k>^2' in R['upper_bound'])
check('optimality stated','alpha<2' in R['optimality'])
check('finite-tier implication','Cauchy in h^(s+2)' in R['finite_tier_cauchy_consequence'])
check('same-tier fence','does not restore a same-tier' in R['same_tier_boundary'])
check('full PDE ceiling','differentiated current numerator' in R['full_pde_ceiling'])
for key in ('fixed_nonzero_mode_homological_inverse_constructed','two_derivative_mapping_bound_proved','two_derivative_loss_optimal','finite_tier_scalar_cauchy_implication_proved'): check(key,Q[key])
for key in ('same_tier_zero_harmonic_normal_form_bounded','full_nonlinear_zero_harmonic_normal_form_constructed','global_full_pde_flow_constructed','protected_status_change'): check(f'{key} fenced',not Q[key])
print(f'RESULT: PASS {n}/{n}')
