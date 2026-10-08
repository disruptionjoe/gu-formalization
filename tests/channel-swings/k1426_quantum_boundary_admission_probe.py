#!/usr/bin/env python3
"""Mutation probe for K1426."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1426-quantum-boundary-admission.json').read_text())
def validate(x):
 b,q=x['bridge_census'],x['decision']; e=[]
 if b['row_count']!=sum(b[k] for k in ('satisfied_count','conditional_count','excluded_count','missing_count')): e.append('sum')
 if len(b['missing_rows'])!=4: e.append('missing')
 for k in ('finite_cylindrical_positive_quantum_control_constructed','stratum_compatible_compact_projection_constructed','closed_gauge_fixed_brst_hilbert_complex_constructed','positive_interacting_finite_block_hamiltonian_constructed','bare_noncompact_gauge_volume_obstruction_proved'):
  if not q[k]: e.append(k)
 for k in ('continuum_quantum_physical_hilbert_cohomology_constructed','completed_full_pde_global_flow_constructed','source_selected_reduction_constructed'):
  if q[k]: e.append(k)
 return e
assert not validate(D)
M=[('sum',lambda x:x['bridge_census'].__setitem__('row_count',91)),('missing',lambda x:x['bridge_census'].__setitem__('missing_rows',[])),('finite',lambda x:x['decision'].__setitem__('finite_cylindrical_positive_quantum_control_constructed',False)),('strata',lambda x:x['decision'].__setitem__('stratum_compatible_compact_projection_constructed',False)),('BRST',lambda x:x['decision'].__setitem__('closed_gauge_fixed_brst_hilbert_complex_constructed',False)),('Hamiltonian',lambda x:x['decision'].__setitem__('positive_interacting_finite_block_hamiltonian_constructed',False)),('continuum',lambda x:x['decision'].__setitem__('continuum_quantum_physical_hilbert_cohomology_constructed',True)),('PDE',lambda x:x['decision'].__setitem__('completed_full_pde_global_flow_constructed',True)),('source',lambda x:x['decision'].__setitem__('source_selected_reduction_constructed',True))]
for i,(label,mutate) in enumerate(M,1):
 x=copy.deepcopy(D); mutate(x); assert validate(x),label; print(f'PASS {i:02d}: rejects {label}')
print(f'RESULT: PASS {len(M)}/{len(M)}')
