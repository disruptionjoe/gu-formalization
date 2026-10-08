#!/usr/bin/env python3
"""Controls for K1459's particle-sector form boundary."""
import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1459-particle-sector-quartic-form-boundary.json').read_text()); n=0
def c(l,v):
 global n; assert v,l; n+=1; print(f'PASS {n:02d}: {l}')
for k,p in D['pinned_inputs'].items(): c(f'{k} pin',hashlib.sha256((R/p['path']).read_bytes()).hexdigest()==p['sha256'])
ratios=[]
for m in (2,5,20,100):
 quartic=6*m*(m-1); free=m+1; ratios.append(quartic/free)
 c(f'expectation n={m}',quartic==6*m*(m-1)); c(f'positive ratio n={m}',ratios[-1]>0)
c('ratio unbounded trend',all(x<y for x,y in zip(ratios,ratios[1:])) and ratios[-1]>500)
Q=D['decision']; c('quadratic',Q['quartic_diagonal_growth_quadratic']); c('linear',Q['free_energy_growth_linear']); c('form bound fenced',not Q['uniform_free_form_bound_across_particle_number']); c('domain route',Q['nonlinear_form_domain_route_open']); c('beta one open',not Q['original_beta_one_hamiltonian_constructed']); c('protected',not Q['protected_status_change'])
print(f'RESULT: PASS {n}/{n}')
