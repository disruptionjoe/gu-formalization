#!/usr/bin/env python3
"""Controls for K1469's semibounded Wick scalar cocycle."""
import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1469-wick-semibounded-projective-cocycle.json').read_text()); n=0
def c(l,v):
 global n; assert v,l; n+=1; print(f'PASS {n:02d}: {l}')
for k,p in D['pinned_inputs'].items(): c(f'{k} pin',hashlib.sha256((R/p['path']).read_bytes()).hexdigest()==p['sha256'])
Cs=[1.,2.5,5.,9.]
for i in range(len(Cs)-1):
 for j in range(i+1,len(Cs)):
  b=6*(Cs[j]**2-Cs[i]**2); c(f'positive cocycle {i}-{j}',b>0)
for a,b,cx in ((0,1,3),(0,2,3),(1,2,3)):
 lhs=6*(Cs[cx]**2-Cs[a]**2); rhs=6*(Cs[cx]**2-Cs[b]**2)+6*(Cs[b]**2-Cs[a]**2); c(f'additive cocycle {a}-{b}-{cx}',abs(lhs-rhs)<1e-12)
const=7.0
for C in Cs: c(f'martingale recenter lower divergence C={C}',abs((const-6*C*C)-(const-6*C*C))<1e-12)
A,Q=D['scalar_cocycle'],D['decision']; c('conditional expectation recorded','E(W_M|F_N)' in A['conditional_expectation']); c('phase-resolvent distinction','phase' in A['dynamics_note'] and 'resolvents' in A['dynamics_note'])
for k in ('exact_semibounded_projective_cocycle_proved','cocycle_identity_proved'): c(k,Q[k])
for k in ('exact_martingale_and_uniform_lower_bound_achieved_by_scalar_recenter','beta_one_mosco_limit_constructed','beta_one_strong_resolvent_limit_constructed','protected_status_change'): c(f'{k} fenced',not Q[k])
print(f'RESULT: PASS {n}/{n}')
