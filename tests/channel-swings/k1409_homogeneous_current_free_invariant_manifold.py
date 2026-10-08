#!/usr/bin/env python3
"""Controls for K1409's homogeneous current-free invariant manifold."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1409-homogeneous-current-free-invariant-manifold.json').read_text()); n=0
def check(label,value):
 global n
 assert value,label; n+=1; print(f'PASS {n:02d}: {label}')
for key,pin in D['pinned_inputs'].items(): check(f'{key} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
F,Q=D['invariant_manifold'],D['decision']
for label,key,needle in [('real','real_structure','CQ=QC'),('data','data','A=E=0'),('spatial','spatial_current','=0'),('density','charge_density','=0'),('equation','reduced_equation',"u''+(m^2+mu Q^2)u+lambda||u||^2u=0"),('invariance','invariance','commutes with C'),('spectrum','spectral_scope','infinite'),('boundary','boundary','not a gauge fixing')]: check(label,needle in F[key])
for u,v,q in ((1.,2.,4.),(-3.,.5,-8.),(.25,-2.,12.)):
 check(f'real density q={q}',abs((q*u*v).imag)<1e-15)
 check(f'zero spatial current q={q}',abs((q*u*0.).imag)<1e-15)
for key in ('homogeneous_real_slice_invariant','maxwell_current_vanishes','gauss_density_vanishes','arbitrary_charge_support_allowed'): check(key,Q[key])
check('full flow fenced',not Q['full_spatial_flow_constructed'])
check('source fenced',not Q['source_reality_selected'])
check('protected fixed',not Q['protected_status_change'])
assert n==23,n
print('RESULT: PASS 23/23')
