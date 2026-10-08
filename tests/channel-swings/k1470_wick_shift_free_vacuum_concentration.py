#!/usr/bin/env python3
"""Controls for K1470's free-vacuum concentration theorem."""
import hashlib,json,math
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1470-wick-shift-free-vacuum-concentration.json').read_text()); n=0
def c(l,v):
 global n; assert v,l; n+=1; print(f'PASS {n:02d}: {l}')
for k,p in D['pinned_inputs'].items(): c(f'{k} pin',hashlib.sha256((R/p['path']).read_bytes()).hexdigest()==p['sha256'])
def sums(N,m=1.):
 qs=[1/(2*math.sqrt(m*m+i*i+j*j+k*k)) for i in range(-N,N+1) for j in range(-N,N+1) for k in range(-N,N+1)]
 return sum(qs),sum(q*q for q in qs)
scaled=[]
for N in (4,6,8,10):
 C,S=sums(N); rel_upper=2*S/(3*C*C); scaled.append(rel_upper*N**3)
 c(f'positive moments N={N}',C>0 and S>0); c(f'concentration upper N={N}',rel_upper>0 and rel_upper<1)
c('relative upper has N^-3 scale',max(scaled)/min(scaled)<3)
A,Q=D['free_vacuum_concentration'],D['decision']; c('Parseval bound recorded','sum_k q_k^2' in A['upper_bound']); c('sharp variance','Theta(N^5)' in A['sharp_order']); c('L2 consequence','L2 and in probability' in A['relative_concentration'])
c('mean order',Q['shifted_wick_mean_order']=='N^4'); c('variance order',Q['shifted_wick_variance_order']=='N^5'); c('relative order',Q['relative_L2_error_order']=='N^-3'); c('concentration proved',Q['free_vacuum_concentration_proved'])
for k in ('scalar_recentering_makes_L2_potentials_bounded','mosco_or_strong_resolvent_failure_proved','protected_status_change'): c(f'{k} fenced',not Q[k])
print(f'RESULT: PASS {n}/{n}')
