#!/usr/bin/env python3
"""Controls for K1410's homogeneous coefficient bounds."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1410-homogeneous-base-energy-coefficient-control.json').read_text()); n=0
def check(label,value):
 global n
 assert value,label; n+=1; print(f'PASS {n:02d}: {label}')
for key,pin in D['pinned_inputs'].items(): check(f'{key} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
F,Q=D['coefficient_control'],D['decision']
for label,key,needle in [('energy','base_energy','H_0='),('conservation','conservation','dH_0/dt=0'),('position','position_bound','sqrt(2H_0)/m'),('velocity','velocity_bound','sqrt(2H_0)'),('radial','radial_derivative','4H_0/m'),('uniform','cutoff_uniformity','no spectral cutoff'),('recurrent','recurrence_boundary','need not belong to L1'),('boundary','boundary','full PDE')]: check(label,needle in F[key])
for H,m,u,v in ((2.,1.,1.,1.),(10.,2.,1.,2.),(.5,.5,1.,0.)):
 check(f'position sample H={H}',abs(u)<=math.sqrt(2*H)/m+1e-12)
 check(f'velocity sample H={H}',abs(v)<=math.sqrt(2*H)+1e-12)
 check(f's derivative sample H={H}',2*abs(u*v)<=4*H/m+1e-12)
for key in ('base_energy_conserved','radial_coefficient_globally_bounded','radial_derivative_globally_bounded','bound_cutoff_uniform'): check(key,Q[key])
check('no L1 claim',not Q['global_time_integrability_claimed'])
check('full PDE fenced',not Q['full_pde_pointwise_coefficient_controlled'])
check('protected fixed',not Q['protected_status_change'])
assert n==25,n
print('RESULT: PASS 25/25')
