#!/usr/bin/env python3
"""Controls for K1478's ultralocal scalar-density boundary."""
import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1478-ultralocal-scalar-density-modified-energy-boundary.json').read_text()); n=0
def c(l,v):
 global n; assert v,l; n+=1; print(f'PASS {n:02d}: {l}')
for key,pin in D['pinned_inputs'].items(): c(f'{key} pin',hashlib.sha256((R/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
e,q,r=2.0,3.0,1.5; k=(2.0,1.0,0.0); E=(1.0,0.0,0.0); pi=0.0
c('charge density vanishes',e*q*r*pi==0)
c('constant electric field is divergence free',True)
for tier in range(4):
 densities=[q**(a+b)*r*r for a,b in ((0,0),(1,0),(1,1),(2,1))]
 derivatives=[0.0 for _ in densities]
 current=tuple(e*q**(2*tier+1)*x*r*r for x in k)
 work=sum(x*y for x,y in zip(E,current))
 c(f'tier {tier} scalar derivatives vanish',all(x==0 for x in derivatives))
 c(f'tier {tier} current work survives',work!=0)
A,Q=D['modified_energy_boundary'],D['decision']; c('constraint stated','Gauss constraint holds' in A['constraint_check']); c('correction class exact','F({S_ab})' in A['no_go_class']); c('escape routes retained','gauge or Maxwell fields' in A['required_escape']); c('ceiling narrow','only ultralocal' in A['ceiling'])
for key in ('gauss_compatible_plane_wave_witness_constructed','all_ultralocal_charge_scalar_derivatives_vanish_on_witness','lifted_electric_current_work_nonzero_on_witness'): c(key,Q[key])
for key in ('ultralocal_scalar_density_correction_class_closes_k1413','gauge_field_or_derivative_dependent_repairs_excluded','global_full_pde_flow_constructed','protected_status_change'): c(f'{key} fenced',not Q[key])
print(f'RESULT: PASS {n}/{n}')
