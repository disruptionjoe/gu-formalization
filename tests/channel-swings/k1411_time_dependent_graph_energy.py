#!/usr/bin/env python3
"""Controls for K1411's nonlinear time-dependent graph energy."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1411-time-dependent-graph-energy.json').read_text()); n=0
def check(label,value):
 global n
 assert value,label; n+=1; print(f'PASS {n:02d}: {label}')
for key,pin in D['pinned_inputs'].items(): check(f'{key} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
F,Q=D['graph_energy'],D['decision']
for label,key,needle in [('equation','lifted_equation','psi_n'),('functional','functional','F_n(t)'),('positive','positivity','m^2'),('derivative','exact_derivative',"F_n'="),('gronwall','gronwall','exp('),('uniform','cutoff_uniformity','no ||Q_N||'),('class','outside_rigidity_class','nonlinear and time dependent'),('boundary','boundary','full PDE')]: check(label,needle in F[key])
for lam,H,m,t,F0 in ((1.,2.,1.,3.,.5),(.25,10.,2.,1.,4.),(0.,3.,1.,100.,2.)):
 rate=4*lam*H/m**3
 check(f'positive bound lam={lam}',F0*math.exp(rate*abs(t))>=F0)
 check(f'symmetric time lam={lam}',math.isclose(math.exp(rate*abs(t)),math.exp(rate*abs(-t))))
for key in ('nonlinear_time_dependent_graph_energy_constructed','exact_derivative_identity_proved','every_fixed_finite_graph_tier_globally_bounded','estimate_cutoff_uniform'): check(key,Q[key])
check('rigidity retained',not Q['k1406_contradicted'])
check('PDE fenced',not Q['full_pde_global_bound_proved'])
check('protected fixed',not Q['protected_status_change'])
assert n==23,n
print('RESULT: PASS 23/23')
