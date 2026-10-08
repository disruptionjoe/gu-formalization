#!/usr/bin/env python3
"""Controls for K1462's normalized same-tier null multiplier."""
import hashlib,json,math
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1462-normalized-null-form-same-tier-bound.json').read_text()); n=0
def c(l,v):
 global n; assert v,l; n+=1; print(f'PASS {n:02d}: {l}')
for k,p in D['pinned_inputs'].items(): c(f'{k} pin',hashlib.sha256((R/p['path']).read_bytes()).hexdigest()==p['sha256'])
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def norm(a): return math.sqrt(dot(a,a))
M=2.0
for p in ((1,0,0),(2,-1,0),(0,3,4)):
 for k in ((0,0,0),(10,1,-2),(-7,8,3),(100,0,0)):
  pp=norm(p); w=math.sqrt(M*M+dot(k,k)); kp=tuple(x+y for x,y in zip(k,p)); w2=math.sqrt(M*M+dot(kp,kp)); q=(pp+w+w2)/(2*pp*w)
  c(f'positive {p,k}',q>0); c(f'triangle bound {p,k}',q<=1/pp+1/w+1e-12); c(f'uniform bound {p,k}',q<=1+1/M+1e-12)
A,Q=D['normalized_bound'],D['decision']; c('nonlocal price explicit','|nabla|^(-1)' in A['nonlocal_price']); c('same tier',Q['uniform_same_tier_scalar_bound_proved']); c('torus gap',Q['nonzero_torus_gap_used']); c('nonlocal',Q['normalization_nonlocal'])
for k in ('k1413_current_already_has_normalization','both_full_pde_leakages_closed','global_full_pde_flow_constructed','protected_status_change'): c(f'{k} fenced',not Q[k])
print(f'RESULT: PASS {n}/{n}')
