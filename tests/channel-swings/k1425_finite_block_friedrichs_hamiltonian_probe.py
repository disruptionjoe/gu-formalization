#!/usr/bin/env python3
"""Mutation probe for K1425."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1425-finite-block-friedrichs-hamiltonian.json').read_text())
def validate(x):
 h,q=x['hamiltonian'],x['decision']; e=[]
 if 'self-adjoint' not in h['operator']: e.append('operator')
 for k in ('closed_semibounded_finite_block_form','self_adjoint_friedrichs_hamiltonian','finite_block_compact_resolvent','compact_invariant_sector_preserved','positive_interacting_finite_block_control'):
  if not q[k]: e.append(k)
 for k in ('cutoff_compatible_continuum_limit_constructed','renormalized_continuum_hamiltonian_constructed','global_nonlinear_pde_proved'):
  if q[k]: e.append(k)
 return e
assert not validate(D)
M=[('operator',lambda x:x['hamiltonian'].__setitem__('operator','unknown')),('closed',lambda x:x['decision'].__setitem__('closed_semibounded_finite_block_form',False)),('selfadjoint',lambda x:x['decision'].__setitem__('self_adjoint_friedrichs_hamiltonian',False)),('compact',lambda x:x['decision'].__setitem__('finite_block_compact_resolvent',False)),('invariant',lambda x:x['decision'].__setitem__('compact_invariant_sector_preserved',False)),('continuum',lambda x:x['decision'].__setitem__('cutoff_compatible_continuum_limit_constructed',True)),('renormalized',lambda x:x['decision'].__setitem__('renormalized_continuum_hamiltonian_constructed',True)),('PDE',lambda x:x['decision'].__setitem__('global_nonlinear_pde_proved',True))]
for i,(label,mutate) in enumerate(M,1):
 x=copy.deepcopy(D); mutate(x); assert validate(x),label; print(f'PASS {i:02d}: rejects {label}')
print(f'RESULT: PASS {len(M)}/{len(M)}')
