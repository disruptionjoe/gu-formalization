#!/usr/bin/env python3
"""Controls for K1473's continuity/transverse-current boundary."""
import hashlib,json,math
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1473-current-conservation-transverse-boundary.json').read_text()); n=0
def c(l,v):
 global n; assert v,l; n+=1; print(f'PASS {n:02d}: {l}')
for k,pin in D['pinned_inputs'].items(): c(f'{k} pin',hashlib.sha256((R/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
M2=5.0
rat=[]
for K in (50,100,200,400):
 p=(1.,0.,0.); k=(float(K),1.,0.)
 w=math.sqrt(M2+sum(x*x for x in k)); kp=(k[0]+1,k[1],k[2]); wp=math.sqrt(M2+sum(x*x for x in kp))
 J0=wp+w; J=(2*k[0]+1,2*k[1],0.)
 continuity=(wp-w)*J0-sum(a*b for a,b in zip(p,J))
 phi=1+w-wp; trans=J[1]
 c(f'exact continuity K={K}',abs(continuity)<1e-9)
 c(f'transverse survives K={K}',trans==2.)
 rat.append((trans/phi)/(K*K))
c('quadratic quotient limit',abs(rat[-1]-4/(M2+1))<.02)
c('limit improves',abs(rat[-1]-4/(M2+1))<abs(rat[0]-4/(M2+1)))
A,Q=D['continuity_boundary'],D['decision']; c('longitudinal statement','parallel to p' in A['longitudinal_control']); c('transverse projection','P_T' in A['transverse_projection']); c('ceiling fenced','not a no-go' in A['ceiling'])
for k in ('exact_scalar_current_continuity_proved','continuity_controls_longitudinal_current','k1463_transverse_witness_survives_continuity'): c(k,Q[k])
for k in ('continuity_controls_transverse_current','continuity_alone_closes_k1413_leakage','all_spacetime_or_modified_energy_routes_excluded','global_full_pde_flow_constructed','protected_status_change'): c(f'{k} fenced',not Q[k])
print(f'RESULT: PASS {n}/{n}')
