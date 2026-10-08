#!/usr/bin/env python3
"""Controls for K1442's strict zero-harmonic phase nonresonance."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1442-zero-harmonic-phase-nonresonance.json').read_text()); n=0
def check(label,value):
 global n
 assert value,label; n+=1; print(f'PASS {n:02d}: {label}')
for key,pin in D['pinned_inputs'].items(): check(f'{key} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
R,Q=D['phase_geometry'],D['decision']
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def norm(a): return math.sqrt(dot(a,a))
def phase(k,p,M2):
 r=norm(p); b=math.sqrt(M2+dot(k,k)); kp=tuple(x+y for x,y in zip(k,p)); a=math.sqrt(M2+dot(kp,kp))
 return r+b-a,2*(r*b-dot(p,k))/(r+b+a)
for k,p,M2 in [((3,2,-1),(1,0,0),5),((-7,1,4),(2,-1,0),3),((0,0,0),(0,1,1),2),((40,0,0),(1,0,0),9)]:
 direct,rational=phase(k,p,M2)
 check(f'identity {k,p}',abs(direct-rational)<1e-12)
 check(f'positive {k,p}',direct>0)
scaled=[]
M2=5; p=(1,0,0)
for K in (100,200,400,800):
 phi,_=phase((K,0,0),p,M2); scaled.append(phi*K*K)
check('parallel asymptotic',abs(scaled[-1]-M2/2)<.03)
check('phase gap collapses',phase((800,0,0),p,M2)[0]<phase((100,0,0),p,M2)[0])
check('declared nonzero mode','p in Z^3 minus {0}' in R['declared_phase'])
check('identity stated','2(|p| omega_q(k)-p dot k)' in R['exact_identity'])
check('positive numerator stated','M_q^2+|k_perp|^2' in R['positive_numerator'])
check('nonresonance stated','Phi_q(k,p)>0' in R['nonresonance'])
check('K^-2 asymptotic stated','2K^2' in R['parallel_asymptotic'])
for key in ('strict_zero_harmonic_phase_nonresonant','exact_positive_phase_identity_proved'): check(key,Q[key])
for key in ('phase_has_uniform_positive_lower_bound_in_k','harmonic_resonance_extends_to_nonzero_modes','full_zero_harmonic_normal_form_constructed','global_full_pde_flow_constructed','protected_status_change'): check(f'{key} fenced',not Q[key])
print(f'RESULT: PASS {n}/{n}')
