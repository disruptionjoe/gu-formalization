#!/usr/bin/env python3
"""Controls for K1425's finite-block interacting Friedrichs Hamiltonian."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1425-finite-block-friedrichs-hamiltonian.json').read_text()); n=0
def check(label,value):
 global n
 assert value,label; n+=1; print(f'PASS {n:02d}: {label}')
for key,pin in D['pinned_inputs'].items(): check(f'{key} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
H,Q=D['hamiltonian'],D['decision']
def V(r,q,m=2,mu=3,lam=5): return m*m*r*r+mu*q*q*r*r+lam*r**4
for r in (0,.5,1,2,4): check(f'coercive sample {r}',V(r,2)>=4*r*r)
for label,key,needle in [('form','form','grad'),('potential','potential','lambda'),('closure','closure','closed'),('operator','operator','self-adjoint'),('gauge','gauge_compatibility','Haar'),('continuum','continuum_boundary','no compatible'),('PDE','pde_boundary','unchanged')]: check(label,needle in H[key])
for key in ('closed_semibounded_finite_block_form','self_adjoint_friedrichs_hamiltonian','finite_block_compact_resolvent','compact_invariant_sector_preserved','positive_interacting_finite_block_control'): check(key,Q[key])
for key in ('cutoff_compatible_continuum_limit_constructed','renormalized_continuum_hamiltonian_constructed','global_nonlinear_pde_proved','source_hamiltonian_identified','protected_status_change'): check(f'{key} fenced',not Q[key])
print(f'RESULT: PASS {n}/{n}')
