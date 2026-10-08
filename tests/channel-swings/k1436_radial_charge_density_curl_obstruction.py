#!/usr/bin/env python3
"""Controls for K1436's radial curl and divisor obstruction."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1436-radial-charge-density-curl-obstruction.json').read_text()); n=0
def check(label,value):
 global n
 assert value,label; n+=1; print(f'PASS {n:02d}: {label}')
for key,pin in D['pinned_inputs'].items(): check(f'{key} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
R,Q=D['radial_obstruction'],D['decision']; q,r,nlift=4,8,1
curl=r**(2*nlift)-q**(2*nlift)
check('curl coefficient nonzero',curl!=0)
check('wedge orientation flips',-curl==q**(2*nlift)-r**(2*nlift))
def ratio(K,m=1,mu=2):
 oq=math.sqrt(K*K+m*m+mu*q*q); orr=math.sqrt(K*K+m*m+mu*r*r)
 return (oq+orr)/(oq-orr)
scaled=[ratio(K)/(K*K) for K in (100,200,400)]
limit=4/(2*(q*q-r*r))
check('two-derivative divisor limit',abs(scaled[-1]-limit)<3e-5)
check('convergence toward signed limit',abs(scaled[-1]-limit)<abs(scaled[0]-limit))
check('one-form stated','dM0 wedge dMn' in R['curl'])
check('density no-go stated','No derivative-free' in R['density_no_go'])
check('surviving routes','spacetime estimates' in R['scope'] and 'summable hierarchies' in R['scope'])
for key in ('radial_one_form_nonclosed_on_unequal_charges','two_spatial_derivative_cost_proved'): check(key,Q[key])
for key in ('derivative_free_quartic_density_cancellation_possible','normal_form_symbol_same_tier_bounded','all_radial_mechanisms_excluded','global_full_pde_flow_constructed','protected_status_change'): check(f'{key} fenced',not Q[key])
print(f'RESULT: PASS {n}/{n}')
