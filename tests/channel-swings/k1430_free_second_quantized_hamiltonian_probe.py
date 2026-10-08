#!/usr/bin/env python3
"""Mutation probe for K1430."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1430-free-second-quantized-hamiltonian.json').read_text())
def validate(x):
 h,q=x['free_hamiltonian'],x['decision']; e=[]
 if 'self-adjoint' not in h['second_quantization']: e.append('operator')
 if 'strongly' not in h['cutoff_compatibility']: e.append('cutoff')
 for k in ('positive_self_adjoint_free_continuum_hamiltonian','finite_particle_core_essentially_self_adjoint','cutoff_resolvents_converge_strongly','residual_invariant_sector_preserved','gaussian_brst_cohomology_preserved'):
  if not q[k]: e.append(k)
 for k in ('interacting_continuum_hamiltonian_constructed','full_pde_global_evolution_constructed','source_hamiltonian_identified','protected_status_change'):
  if q[k]: e.append(k)
 return e
assert not validate(D)
M=[('operator',lambda x:x['free_hamiltonian'].__setitem__('second_quantization','unknown')),('cutoff',lambda x:x['free_hamiltonian'].__setitem__('cutoff_compatibility','unknown')),('positive',lambda x:x['decision'].__setitem__('positive_self_adjoint_free_continuum_hamiltonian',False)),('core',lambda x:x['decision'].__setitem__('finite_particle_core_essentially_self_adjoint',False)),('resolvent',lambda x:x['decision'].__setitem__('cutoff_resolvents_converge_strongly',False)),('invariant',lambda x:x['decision'].__setitem__('residual_invariant_sector_preserved',False)),('BRST',lambda x:x['decision'].__setitem__('gaussian_brst_cohomology_preserved',False)),('interacting',lambda x:x['decision'].__setitem__('interacting_continuum_hamiltonian_constructed',True)),('PDE',lambda x:x['decision'].__setitem__('full_pde_global_evolution_constructed',True)),('source',lambda x:x['decision'].__setitem__('source_hamiltonian_identified',True))]
for i,(label,mutate) in enumerate(M,1):
 x=copy.deepcopy(D); mutate(x); assert validate(x),label; print(f'PASS {i:02d}: rejects {label}')
print(f'RESULT: PASS {len(M)}/{len(M)}')
