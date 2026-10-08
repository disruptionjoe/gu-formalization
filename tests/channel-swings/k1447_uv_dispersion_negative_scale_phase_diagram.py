#!/usr/bin/env python3
"""Controls for K1447's coherent UV-dispersion phase diagram."""
import hashlib,json,math
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1447-uv-dispersion-negative-scale-phase-diagram.json').read_text()); n=0
def c(l,v):
 global n
 assert v,l; n+=1; print(f'PASS {n:02d}: {l}')
for k,p in D['pinned_inputs'].items(): c(f'{k} pin',hashlib.sha256((R/p['path']).read_bytes()).hexdigest()==p['sha256'])
B,Q=D['coherent_model'],D['decision']
for beta,s,want in ((1,5,False),(1,5.01,True),(2.25,0,False),(2.26,0,True),(1.8,1,False),(1.81,1,True),(3,0,True)):
 c(f'phase beta={beta} s={s}',(beta*(s+4)>9)==want)
c('coherent covariance','q_beta' in B['dispersion_and_covariance'] and 'same Gaussian' in B['dispersion_and_covariance'])
c('strict boundary','beta(s+4)>9' in B['phase_boundary'] and '<=9' in B['phase_boundary'])
for k in ('sharp_beta_s_phase_boundary_proved','beta_one_recovers_s_greater_than_five','l2_threshold_beta_greater_than_nine_fourths','form_dual_threshold_beta_greater_than_nine_fifths'): c(k,Q[k])
for k in ('original_beta_one_interaction_constructed','representations_silently_mixed','protected_status_change'): c(f'{k} fenced',not Q[k])
c('changed representation ceiling','does not repair' in B['ceiling'])
print(f'RESULT: PASS {n}/{n}')
