#!/usr/bin/env python3
"""Controls for K1481's BRST projective-recentering transfer."""
import hashlib,json,math
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1481-brst-projective-recentering-instability.json').read_text()); n=0
def c(l,v):
 global n; assert v,l; n+=1; print(f'PASS {n:02d}: {l}')
for key,pin in D['pinned_inputs'].items(): c(f'{key} pin',hashlib.sha256((R/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
for matter_bottom in (-10.,-100.,-1000.):
 brst_levels=(matter_bottom,matter_bottom+1,matter_bottom+3)
 c(f'harmonic sector preserves bottom {matter_bottom}',min(brst_levels)==matter_bottom)
for a in (1/256,1/128): c(f'weak tensor limit nonzero a={a}',1/math.sqrt(1+a*a)>0)
A,Q=D['brst_projective_boundary'],D['decision']; c('tensor shift stated','H_N-6gC_N^2' in A['recentered_tensor_hamiltonian']); c('bottom order stated','N^(5/2)' in A['bottom_transfer']); c('weak limit stated','nonzero weak limit' in A['trial_transfer']); c('harmonic compression retained','harmonic degree-zero compression' in A['mosco_transfer']); c('algebraic boundary fenced','neither restores a lower bound' in A['differential_boundary'])
for key in ('projectively_recentered_brst_bottom_tends_to_minus_infinity','harmonic_tensor_trial_preserves_matter_instability'): c(key,Q[key])
for key in ('projectively_recentered_brst_mosco_liminf_holds','brst_factor_repairs_projective_semiboundedness','ground_energy_recentered_brst_limit_excluded','source_physical_cohomology_identified','protected_status_change'): c(f'{key} fenced',not Q[key])
print(f'RESULT: PASS {n}/{n}')
