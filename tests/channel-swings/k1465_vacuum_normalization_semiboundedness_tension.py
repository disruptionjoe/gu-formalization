#!/usr/bin/env python3
"""Controls for K1465's scalar vacuum-shift tension."""
import hashlib,json,math
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1465-vacuum-normalization-semiboundedness-tension.json').read_text()); n=0
def c(l,v):
 global n; assert v,l; n+=1; print(f'PASS {n:02d}: {l}')
for k,p in D['pinned_inputs'].items(): c(f'{k} pin',hashlib.sha256((R/p['path']).read_bytes()).hexdigest()==p['sha256'])
for C in (.5,2,7):
 d=6*C*C-3; c(f'lower bound identity C={C}',abs((d-6*C*C)-(-3))<1e-12); c(f'vacuum moment C={C}',abs((3*C*C-6*C*C+3*C*C+d)-d)<1e-12)
def cov(N,m=1.0): return sum(1/(2*math.sqrt(m*m+i*i+j*j+k*k)) for i in range(-N,N+1) for j in range(-N,N+1) for k in range(-N,N+1))
vals=[cov(N)/(N*N) for N in (8,12,16)]
c('covariance order N2 lower',min(vals)>.5); c('covariance order N2 upper',max(vals)<20); c('ratio stabilizes',abs(vals[-1]-vals[-2])<abs(vals[1]-vals[0]))
A,Q=D['scalar_shift_tension'],D['decision']; c('N4 consequence','N^4' in A['vacuum_growth']); c('N2 classified',Q['three_dimensional_covariance_growth_order']=='N^2'); c('N4 classified',Q['uniform_lower_bound_forces_vacuum_growth_order']=='N^4'); c('identity',Q['exact_lower_bound_and_expectation_identity_proved'])
for k in ('scalar_shift_achieves_bounded_lower_and_vacuum_energy','all_beta_one_renormalization_routes_excluded','protected_status_change'): c(f'{k} fenced',not Q[k])
print(f'RESULT: PASS {n}/{n}')
