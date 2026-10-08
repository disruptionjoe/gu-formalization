#!/usr/bin/env python3
"""Controls for K1464's Wick square completion."""
import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1464-wick-cutoff-square-completion.json').read_text()); n=0
def c(l,v):
 global n; assert v,l; n+=1; print(f'PASS {n:02d}: {l}')
for k,p in D['pinned_inputs'].items(): c(f'{k} pin',hashlib.sha256((R/p['path']).read_bytes()).hexdigest()==p['sha256'])
for C in (.25,1,3,10):
 for x in (-5,-1,0,.5,2,7): c(f'square identity C={C} x={x}',abs((x**4-6*C*x*x+3*C*C)-((x*x-3*C)**2-6*C*C))<1e-10)
 c(f'exact minimum C={C}',abs(((3*C)**2-6*C*(3*C)+3*C*C)+6*C*C)<1e-10)
A,Q=D['square_completion'],D['decision']; c('counterterm explicit','vacuum-energy counterterm' in A['counterterm_accounting'])
for k in ('exact_square_completion_proved','finite_cutoff_nonnegative_shift_constructed','fixed_cutoff_all_particle_sectors_semibounded'): c(k,Q[k])
for k in ('uniform_free_form_bound_constructed','beta_one_continuum_limit_constructed','protected_status_change'): c(f'{k} fenced',not Q[k])
print(f'RESULT: PASS {n}/{n}')
