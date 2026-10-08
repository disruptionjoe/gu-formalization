#!/usr/bin/env python3
"""Mutation probe for K1432."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1432-continuum-quantum-admission.json').read_text())
def validate(x):
 b,q=x['bridge_census'],x['decision']; e=[]
 if b['row_count']!=sum(b[k] for k in ('satisfied_count','conditional_count','excluded_count','missing_count')): e.append('sum')
 if len(b['missing_rows'])!=4: e.append('missing')
 for k in ('compatible_continuum_gaussian_representation_constructed','closed_refinement_stable_continuum_brst_cohomology_constructed','positive_free_continuum_hamiltonian_constructed','naive_quartic_cutoff_compatibility_excluded','wick_interaction_candidate_constructed'):
  if not q[k]: e.append(k)
 for k in ('renormalized_interacting_hamiltonian_constructed','completed_full_pde_global_flow_constructed','source_selected_reduction_constructed','protected_status_change'):
  if q[k]: e.append(k)
 return e
assert not validate(D)
M=[('sum',lambda x:x['bridge_census'].__setitem__('row_count',96)),('missing',lambda x:x['bridge_census'].__setitem__('missing_rows',[])),('representation',lambda x:x['decision'].__setitem__('compatible_continuum_gaussian_representation_constructed',False)),('BRST',lambda x:x['decision'].__setitem__('closed_refinement_stable_continuum_brst_cohomology_constructed',False)),('free',lambda x:x['decision'].__setitem__('positive_free_continuum_hamiltonian_constructed',False)),('quartic',lambda x:x['decision'].__setitem__('naive_quartic_cutoff_compatibility_excluded',False)),('Wick',lambda x:x['decision'].__setitem__('wick_interaction_candidate_constructed',False)),('interacting',lambda x:x['decision'].__setitem__('renormalized_interacting_hamiltonian_constructed',True)),('PDE',lambda x:x['decision'].__setitem__('completed_full_pde_global_flow_constructed',True)),('source',lambda x:x['decision'].__setitem__('source_selected_reduction_constructed',True))]
for i,(label,mutate) in enumerate(M,1):
 x=copy.deepcopy(D); mutate(x); assert validate(x),label; print(f'PASS {i:02d}: rejects {label}')
print(f'RESULT: PASS {len(M)}/{len(M)}')
