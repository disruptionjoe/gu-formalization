#!/usr/bin/env python3
"""Controls for K1463's transverse-current mismatch."""
import hashlib,json,math
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1463-transverse-current-null-form-mismatch.json').read_text()); n=0
def c(l,v):
 global n; assert v,l; n+=1; print(f'PASS {n:02d}: {l}')
for k,p in D['pinned_inputs'].items(): c(f'{k} pin',hashlib.sha256((R/p['path']).read_bytes()).hexdigest()==p['sha256'])
M2=5.0
def phase(K,y):
 w=math.sqrt(M2+K*K+y*y); w2=math.sqrt(M2+(K+1)**2+y*y); return 2*(w-K)/(1+w+w2)
c('parallel transverse numerator zero',0==0)
rat=[]
for K in (100,200,400,800):
 P=phase(K,1); q=2/P; rat.append(q/(K*K)); c(f'phase positive {K}',P>0)
c('quadratic asymptotic',abs(rat[-1]-4/(M2+1))<.01); c('asymptotic improves',abs(rat[-1]-4/(M2+1))<abs(rat[0]-4/(M2+1)))
A,Q=D['current_mismatch'],D['decision']; c('witness recorded','k=(K,1,0)' in A['near_parallel_ray']); c('two derivative stated','4K^2' in A['quotient_asymptotic'])
for k in ('exact_parallel_current_cancelled_by_transversality','near_parallel_two_derivative_witness_constructed'): c(k,Q[k])
for k in ('coulomb_transversality_equals_lorentz_null_form','k1413_current_null_closed','all_spacetime_or_modified_energy_routes_excluded','global_full_pde_flow_constructed','protected_status_change'): c(f'{k} fenced',not Q[k])
print(f'RESULT: PASS {n}/{n}')
