#!/usr/bin/env python3
"""Mutation probe for K1419."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1419-classical-bfv-boundary-exactness.json').read_text())
def validate(x):
 f,q=x['classical_bfv'],x['decision']; e=[]
 if 'H^0' not in f['degree_zero_result']: e.append('H0')
 if 'not a quantized' not in f['boundary']: e.append('boundary')
 for k in ('boundary_moment_map_constructed','bfv_master_equation_constructed','functional_kt_resolution_on_declared_algebra_constructed','based_brst_reduction_constructed','classical_bfv_degree_zero_identified','positive_classical_hamiltonian_descends'):
  if not q[k]: e.append(k)
 for k in ('quantum_physical_hilbert_cohomology_constructed','source_gu_bfv_complex_identified','protected_status_change'):
  if q[k]: e.append(k)
 return e
assert not validate(D)
mutations=[('H0 prose',lambda x:x['classical_bfv'].__setitem__('degree_zero_result','unknown')),('boundary prose',lambda x:x['classical_bfv'].__setitem__('boundary','quantized')),('moment',lambda x:x['decision'].__setitem__('boundary_moment_map_constructed',False)),('KT',lambda x:x['decision'].__setitem__('functional_kt_resolution_on_declared_algebra_constructed',False)),('BRST',lambda x:x['decision'].__setitem__('based_brst_reduction_constructed',False)),('H0',lambda x:x['decision'].__setitem__('classical_bfv_degree_zero_identified',False)),('quantum',lambda x:x['decision'].__setitem__('quantum_physical_hilbert_cohomology_constructed',True)),('source',lambda x:x['decision'].__setitem__('source_gu_bfv_complex_identified',True)),('protected',lambda x:x['decision'].__setitem__('protected_status_change',True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D); mutate(x); e=validate(x); assert e,label; print(f'PASS {i:02d}: rejects {label} via [FAIL] {e[0]}')
print(f'RESULT: PASS {len(mutations)}/{len(mutations)}')
