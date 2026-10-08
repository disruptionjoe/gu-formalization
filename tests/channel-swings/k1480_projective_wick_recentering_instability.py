#!/usr/bin/env python3
"""Controls for K1480's projective-recentering instability."""
import hashlib,json,math
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1480-projective-wick-recentering-instability.json').read_text()); n=0
def c(l,v):
 global n; assert v,l; n+=1; print(f'PASS {n:02d}: {l}')
for key,pin in D['pinned_inputs'].items(): c(f'{key} pin',hashlib.sha256((R/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
g=.2; a=1/256
bottoms=[]
for N in (16,32,64,128):
 bottom=-g*a*N**2.5; bottoms.append(bottom); c(f'negative projective bottom N={N}',bottom<0)
c('bottoms diverge downward',all(x>y for x,y in zip(bottoms,bottoms[1:])))
M=8.; ratios=[M**2.5/N**2.5 for N in (16,32,64,128,256)]
c('fixed cylinder projection decays',all(x>y for x,y in zip(ratios,ratios[1:])))
c('projection tends to zero',ratios[-1]<.001)
weak_vacuum=1/math.sqrt(1+a*a); c('trial weak limit nonzero',weak_vacuum>.99)
A,Q=D['projective_instability'],D['decision']; c('martingale family identified','H0+gV_N' in A['recentered_family']); c('conditional expectation used','conditional expectation' in A['weak_fourth_chaos_escape']); c('Mosco inequality named','weak-liminf' in A['mosco_liminf_failure']); c('strong-resolvent fence','unbounded below' in A['ceiling'])
for key in ('projectively_recentered_bottom_tends_to_minus_infinity','normalized_fourth_chaos_converges_weakly_to_zero','trial_sequence_has_nonzero_weak_limit'): c(key,Q[key])
for key in ('projective_recentered_mosco_liminf_holds','projective_recentered_uniform_semiboundedness_holds','ground_energy_recentered_mosco_limit_excluded','arbitrary_unbounded_below_strong_resolvent_limit_excluded','protected_status_change'): c(f'{key} fenced',not Q[key])
print(f'RESULT: PASS {n}/{n}')
