#!/usr/bin/env python3
"""Mutation probe for K1420."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1420-classical-boundary-admission.json').read_text())
def validate(x):
 b,q=x['bridge_census'],x['decision']; e=[]
 if b['row_count']!=sum(b[k] for k in ('satisfied_count','conditional_count','excluded_count','missing_count')): e.append('census')
 if (b['row_count'],b['satisfied_count'],b['conditional_count'],b['excluded_count'],b['missing_count'])!=(86,61,6,15,4): e.append('counts')
 if len(b['new_satisfied_rows'])!=5: e.append('new satisfied')
 for k in ('classical_bfv_boundary_exactness_constructed','proper_stratified_classical_quotient_constructed','positive_reduced_classical_hamiltonian_constructed'):
  if not q[k]: e.append(k)
 for k in ('completed_full_pde_global_flow_constructed','positive_gu_physical_hilbert_cohomology_constructed','source_selected_reduction_constructed','k1145_k1150_candidate_counts_move','protected_status_change'):
  if q[k]: e.append(k)
 return e
assert not validate(D)
mutations=[('census',lambda x:x['bridge_census'].__setitem__('row_count',85)),('counts',lambda x:x['bridge_census'].__setitem__('satisfied_count',62)),('new satisfied',lambda x:x['bridge_census'].__setitem__('new_satisfied_rows',[])),('classical',lambda x:x['decision'].__setitem__('classical_bfv_boundary_exactness_constructed',False)),('strata',lambda x:x['decision'].__setitem__('proper_stratified_classical_quotient_constructed',False)),('PDE',lambda x:x['decision'].__setitem__('completed_full_pde_global_flow_constructed',True)),('physical',lambda x:x['decision'].__setitem__('positive_gu_physical_hilbert_cohomology_constructed',True)),('source',lambda x:x['decision'].__setitem__('source_selected_reduction_constructed',True)),('protected',lambda x:x['decision'].__setitem__('protected_status_change',True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D); mutate(x); e=validate(x); assert e,label; print(f'PASS {i:02d}: rejects {label} via [FAIL] {e[0]}')
print(f'RESULT: PASS {len(mutations)}/{len(mutations)}')
