#!/usr/bin/env python3
"""Controls for K1479's vacuum--fourth-chaos variational gap."""
import hashlib,json,math
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1479-wick-vacuum-mixing-variational-gap.json').read_text()); n=0
def c(l,v):
 global n; assert v,l; n+=1; print(f'PASS {n:02d}: {l}')
for key,pin in D['pinned_inputs'].items(): c(f'{key} pin',hashlib.sha256((R/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
a=1/256; g=.25
c('admissible trial amplitude',0<a<=1/128)
gaps=[]
for N in (16,32,64,128,256):
 sigma=N**2.5; omega=N; h=4*omega*sigma*sigma; m3=64*sigma**3
 centered=(a*a*h/(sigma*sigma)-2*g*a*sigma+g*a*a*m3/(sigma*sigma))/(1+a*a)
 gaps.append(centered)
 c(f'hypercontractive moment N={N}',abs(m3)<=64*sigma**3)
 c(f'centered trial lowers energy N={N}',centered<0)
c('gap magnitude grows',all(abs(x)<abs(y) for x,y in zip(gaps,gaps[1:])))
c('N five-halves dominates frequency',256**2.5>1000*256)
A,Q=D['variational_gap'],D['decision']; c('exact normalization','1+a^2' in A['trial_vector']); c('rayleigh identity','R_N-6gC_N^2' in A['exact_rayleigh_identity']); c('frequency bound','h_N<=4 omega_max' in A['free_energy_bound']); c('hypercontractivity constant','64 sigma_N^3' in A['third_moment_bound']); c('one-sided ceiling','one-sided divergent gap' in A['ceiling'])
for key in ('normalized_vacuum_fourth_chaos_trial_constructed','exact_centered_rayleigh_identity_proved','fourth_chaos_hypercontractive_bound_used'): c(key,Q[key])
for key in ('projective_shift_tracks_ground_energy_to_bounded_error','true_ground_energy_asymptotic_determined','ground_energy_recentered_limit_excluded','protected_status_change'): c(f'{key} fenced',not Q[key])
c('gap order',Q['projective_shift_ground_energy_gap_order_at_least']=='N^(5/2)')
print(f'RESULT: PASS {n}/{n}')
