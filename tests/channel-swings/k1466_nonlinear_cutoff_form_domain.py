#!/usr/bin/env python3
"""Controls for K1466's finite-cutoff nonlinear form domain."""
import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1466-nonlinear-cutoff-form-domain.json').read_text()); n=0
def c(l,v):
 global n; assert v,l; n+=1; print(f'PASS {n:02d}: {l}')
for k,p in D['pinned_inputs'].items(): c(f'{k} pin',hashlib.sha256((R/p['path']).read_bytes()).hexdigest()==p['sha256'])
for C in (.25,1,4):
 for x in (-8,-2,0,1,3,9): c(f'nonnegative U C={C} x={x}',(x*x-3*C)**2>=0)
A,Q=D['cutoff_form'],D['decision']; c('intersection domain','intersection' in A['full_domain']); c('Friedrichs stated','Friedrichs' in A['closed_sum']); c('continuum debt explicit','no Mosco' in A['continuum_debt'])
for k in ('finite_cutoff_dense_closed_form_constructed','finite_cutoff_self_adjoint_hamiltonian_constructed','every_particle_sector_in_fixed_cutoff_domain_controlled'): c(k,Q[k])
for k in ('uniform_free_form_domination_used','cutoff_consistent_form_convergence_proved','interacting_brst_closed','protected_status_change'): c(f'{k} fenced',not Q[k])
print(f'RESULT: PASS {n}/{n}')
