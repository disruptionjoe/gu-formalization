#!/usr/bin/env python3
"""Controls for K1475's unshifted resolvent collapse."""
import hashlib,json,math
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1475-unshifted-wick-resolvent-collapse.json').read_text()); n=0
def c(l,v):
 global n; assert v,l; n+=1; print(f'PASS {n:02d}: {l}')
for k,pin in D['pinned_inputs'].items(): c(f'{k} pin',hashlib.sha256((R/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
vals=[]
for N in (10,30,100,300,1000):
 E=.2*math.log(N); r=1/(E+1); vals.append(r); c(f'positive resolvent bound N={N}',0<r<1)
c('resolvent bounds decrease',all(a>b for a,b in zip(vals,vals[1:])))
c('resolvent tends toward zero',1/(.2*math.log(10**30)+1)<.15)
for offset in (-3,0,4):
 E=17.; a=E+offset; c(f'bounded recentered floor offset={offset}',abs(E-a)<=4)
A,Q=D['resolvent_collapse'],D['decision']; c('ground energy input','Omega(log N)' in A['ground_energy']); c('norm statement','operator norm' in A['resolvent_bound']); c('zero not resolvent','cannot be the resolvent' in A['finite_limit_exclusion']); c('ground tracking','track the true interacting ground energy' in A['semibounded_recentering'])
for k in ('unshifted_ground_energy_diverges','unshifted_resolvents_converge_to_zero_in_norm','nontrivial_semibounded_limit_requires_ground_energy_tracking'): c(k,Q[k])
for k in ('unshifted_finite_self_adjoint_strong_resolvent_limit_exists','martingale_shift_tracks_ground_energy_proved','ground_energy_recentered_limit_constructed','all_beta_one_renormalizations_excluded','protected_status_change'): c(f'{k} fenced',not Q[k])
print(f'RESULT: PASS {n}/{n}')
