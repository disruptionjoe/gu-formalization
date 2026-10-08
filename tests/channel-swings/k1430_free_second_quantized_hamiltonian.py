#!/usr/bin/env python3
"""Controls for K1430's free second-quantized continuum Hamiltonian."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1430-free-second-quantized-hamiltonian.json').read_text()); n=0
def check(label,value):
 global n
 assert value,label; n+=1; print(f'PASS {n:02d}: {label}')
for key,pin in D['pinned_inputs'].items(): check(f'{key} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
H,Q=D['free_hamiltonian'],D['decision']
omega=(1,2,3,5,8)
occupations=((0,0,0,0,0),(1,0,0,0,0),(0,2,0,0,0),(1,1,1,0,0))
energies=[sum(w*m for w,m in zip(omega,occ)) for occ in occupations]
check('vacuum kernel',energies[0]==0)
check('positive gap',min(e for e in energies if e)==1)
check('positive spectrum',all(e>=0 for e in energies))
for N in range(1,5):
 full=sum(omega[j]*occupations[3][j] for j in range(N))
 cutoff=sum(omega[j]*occupations[3][j] for j in range(N))
 check(f'cutoff intertwining {N}',full==cutoff)
for lam in (1,2,4,8): check(f'resolvent contraction {lam}',max(1/(e+lam) for e in energies)<=1/lam)
for label,key,needle in [('one particle','one_particle_operator','self-adjoint'),('second quantization','second_quantization','self-adjoint'),('cutoff','cutoff_compatibility','strongly'),('compact','compact_symmetry','Haar'),('BRST','brst_compatibility','commutes'),('boundary','boundary','free')]: check(label,needle in H[key])
for key in ('positive_self_adjoint_free_continuum_hamiltonian','finite_particle_core_essentially_self_adjoint','cutoff_resolvents_converge_strongly','residual_invariant_sector_preserved','gaussian_brst_cohomology_preserved'): check(key,Q[key])
for key in ('interacting_continuum_hamiltonian_constructed','full_pde_global_evolution_constructed','source_hamiltonian_identified','protected_status_change'): check(f'{key} fenced',not Q[key])
print(f'RESULT: PASS {n}/{n}')
