#!/usr/bin/env python3
"""Controls for K1474's Gaussian entropy localization barrier."""
import hashlib,json,math
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1474-gaussian-entropy-localization-barrier.json').read_text()); n=0
def c(l,v):
 global n; assert v,l; n+=1; print(f'PASS {n:02d}: {l}')
for k,pin in D['pinned_inputs'].items(): c(f'{k} pin',hashlib.sha256((R/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
def kl_binary(m,d): return m*math.log(m/d)+(1-m)*math.log((1-m)/(1-d))
for d in (1e-2,1e-4,1e-8):
 for m in (.1,.4,.8): c(f'binary entropy lower d={d} m={m}',kl_binary(m,d)>=m*math.log(1/d)-math.log(2)-1e-12)
cLS=2.; g=.3
for N in (10,30,100,300):
 d=N**-3; L=math.log(1/d); C=N*N
 lower=min(L/(4*cLS),1.5*g*C*C)
 c(f'positive divergent lower N={N}',lower>0)
c('log lower grows',min(math.log(300**3)/(4*cLS),1.5*g*300**4)>min(math.log(10**3)/(4*cLS),1.5*g*10**4))
A,Q=D['entropy_localization'],D['decision']; c('Chebyshev input','Chebyshev' in A['low_potential_set']); c('data processing','data processing' in A['binary_entropy_contraction']); c('log Sobolev','Gross log-Sobolev' in A['gaussian_log_sobolev']); c('fixed positive coupling','fixed g>0' in A['energy_consequence'])
for k in ('binary_entropy_localization_bound_proved','cutoff_uniform_log_sobolev_constant_available','normalized_low_potential_localization_has_divergent_cost'): c(k,Q[k])
for k in ('ground_energy_asymptotic_determined','recentered_mosco_limit_excluded','protected_status_change'): c(f'{k} fenced',not Q[k])
c('probability order',Q['low_potential_probability_order']=='N^-3'); c('energy lower order',Q['unshifted_ground_energy_lower_order']=='log N')
print(f'RESULT: PASS {n}/{n}')
