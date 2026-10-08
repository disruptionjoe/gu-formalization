#!/usr/bin/env python3
"""Mutation probe for K1452."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1452-dressing-hierarchy-selector-admission.json').read_text())
def v(x):
 c,q=x['bridge_census'],x['decision']; e=[]
 if c['row_count']!=c['satisfied_count']+c['conditional_count']+c['excluded_count']+c['missing_count']: e.append('sum')
 if (c['row_count'],c['satisfied_count'],c['conditional_count'],c['excluded_count'],c['missing_count'])!=(121,79,10,28,4): e.append('values')
 if (len(c['new_satisfied_rows']),len(c['new_conditional_rows']),len(c['new_excluded_rows']),len(c['missing_rows']))!=(3,1,4,4): e.append('lists')
 for k in ('uv_softened_interacting_control_constructed','conditional_full_pde_hierarchy_constructed','source_normalization_dependency_sharpened'):
  if not q[k]: e.append(k)
 for k in ('original_beta_one_interacting_hamiltonian_constructed','generic_zero_harmonic_sector_invariant','completed_global_full_pde_flow_constructed','source_selected_reduction_constructed','k1145_k1150_candidate_counts_move','protected_status_change'):
  if q[k]: e.append(k)
 if 'LEDGER_UNCHANGED' not in x['source_and_ledger_effect'] or 'K1145/K1150 0/7' not in x['source_and_ledger_effect']: e.append('effects')
 return e
assert not v(D)
M=[('count',lambda x:x['bridge_census'].__setitem__('row_count',120)),('sat',lambda x:x['bridge_census'].__setitem__('new_satisfied_rows',[])),('cond',lambda x:x['bridge_census'].__setitem__('new_conditional_rows',[])),('excl',lambda x:x['bridge_census'].__setitem__('new_excluded_rows',[])),('missing',lambda x:x['bridge_census'].__setitem__('missing_rows',[])),('uv',lambda x:x['decision'].__setitem__('uv_softened_interacting_control_constructed',False)),('hierarchy',lambda x:x['decision'].__setitem__('conditional_full_pde_hierarchy_constructed',False)),('beta1',lambda x:x['decision'].__setitem__('original_beta_one_interacting_hamiltonian_constructed',True)),('zero',lambda x:x['decision'].__setitem__('generic_zero_harmonic_sector_invariant',True)),('global',lambda x:x['decision'].__setitem__('completed_global_full_pde_flow_constructed',True)),('source',lambda x:x['decision'].__setitem__('source_selected_reduction_constructed',True)),('counts',lambda x:x['decision'].__setitem__('k1145_k1150_candidate_counts_move',True)),('protected',lambda x:x['decision'].__setitem__('protected_status_change',True)),('effects',lambda x:x.__setitem__('source_and_ledger_effect','changed'))]
for i,(l,m) in enumerate(M,1): x=copy.deepcopy(D); m(x); assert v(x),l; print(f'PASS {i:02d}: rejects {l}')
print(f'RESULT: PASS {len(M)}/{len(M)}')
