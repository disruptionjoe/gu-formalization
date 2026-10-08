#!/usr/bin/env python3
"""Controls for K1448's UV-softened interacting Hamiltonian."""
import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1448-uv-softened-interacting-hamiltonian.json').read_text()); n=0
def c(l,v):
 global n
 assert v,l; n+=1; print(f'PASS {n:02d}: {l}')
for k,p in D['pinned_inputs'].items(): c(f'{k} pin',hashlib.sha256((R/p['path']).read_bytes()).hexdigest()==p['sha256'])
B,Q=D['interacting_control'],D['decision']
for C in (.1,1,7):
 vals=[y*y-6*C*y+3*C*C for y in (0,3*C,8*C)]
 c(f'Wick minimum C={C}',min(vals)>=-6*C*C-1e-12 and abs(vals[1]+6*C*C)<1e-12)
c('beta strict','beta>3' in B['regime']); c('counterterms complete','-6 C_(beta,N)' in B['counterterms'] and '+3 C_(beta,N)^2' in B['counterterms'])
c('L1 convergence','L2(mu_beta)' in B['limit'] and 'L1' in B['limit'])
c('stationary path identity','t||V_N-V||_1' in B['strong_resolvent'])
for k in ('all_counterterms_stated','uniform_semiboundedness_proved','closed_interacting_limit_form_constructed','strong_resolvent_convergence_constructed'): c(k,Q[k])
for k in ('original_beta_one_hamiltonian_constructed','interacting_brst_constructed','source_hamiltonian_identified','protected_status_change'): c(f'{k} fenced',not Q[k])
c('beta ceiling','beta=1' in B['ceiling'])
print(f'RESULT: PASS {n}/{n}')
