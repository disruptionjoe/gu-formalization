#!/usr/bin/env python3
"""Mutation probe for K1445."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1445-unitary-dressing-form-obstruction.json').read_text())
def v(x):
 b,q=x['dressing_boundary'],x['decision']; e=[]
 if 'U_N^(-1)' not in b['admitted_dressing'] or 'U_N^(-1)' not in b['pullback_argument']: e.append('inverse')
 if 'K1439' not in b['contradiction']: e.append('contradiction')
 if not q['graph_equivalent_unitary_dressing_excluded'] or not q['inverse_graph_bound_required']: e.append('result')
 for k in ('singular_dressing_excluded','all_changed_domain_routes_excluded','source_hamiltonian_identified','protected_status_change'):
  if q[k]: e.append(k)
 if 'Singular dressings' not in b['ceiling']: e.append('ceiling')
 return e
assert not v(D)
M=[('inverse',lambda x:x['dressing_boundary'].__setitem__('admitted_dressing','unitary only')),('pullback',lambda x:x['dressing_boundary'].__setitem__('pullback_argument','unknown')),('contradiction',lambda x:x['dressing_boundary'].__setitem__('contradiction','unknown')),('result',lambda x:x['decision'].__setitem__('graph_equivalent_unitary_dressing_excluded',False)),('singular',lambda x:x['decision'].__setitem__('singular_dressing_excluded',True)),('all',lambda x:x['decision'].__setitem__('all_changed_domain_routes_excluded',True)),('source',lambda x:x['decision'].__setitem__('source_hamiltonian_identified',True)),('protected',lambda x:x['decision'].__setitem__('protected_status_change',True)),('ceiling',lambda x:x['dressing_boundary'].__setitem__('ceiling','all dressings fail'))]
for i,(l,m) in enumerate(M,1):
 x=copy.deepcopy(D); m(x); assert v(x),l; print(f'PASS {i:02d}: rejects {l}')
print(f'RESULT: PASS {len(M)}/{len(M)}')
