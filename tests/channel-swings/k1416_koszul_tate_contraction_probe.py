#!/usr/bin/env python3
"""Mutation probe for K1416."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1416-koszul-tate-contraction.json').read_text())
def validate(x):
 f,q=x['koszul_tate'],x['decision']; e=[]
 if 'id-iota pi' not in f['contraction_identity']: e.append('identity')
 if 'finite-rank' not in f['algebra'].lower(): e.append('scope')
 for k in ('koszul_tate_nilpotent','explicit_contracting_homotopy_constructed','positive_antighost_homology_zero','degree_zero_is_gauss_surface_functions'):
  if not q[k]: e.append(k)
 for k in ('unrestricted_local_functional_exactness_claimed','quantum_cohomology_constructed','protected_status_change'):
  if q[k]: e.append(k)
 return e
assert not validate(D)
mutations=[('identity',lambda x:x['koszul_tate'].__setitem__('contraction_identity','local')),('scope',lambda x:x['koszul_tate'].__setitem__('algebra','all functionals')),('nilpotence',lambda x:x['decision'].__setitem__('koszul_tate_nilpotent',False)),('homotopy',lambda x:x['decision'].__setitem__('explicit_contracting_homotopy_constructed',False)),('positive degree',lambda x:x['decision'].__setitem__('positive_antighost_homology_zero',False)),('unrestricted',lambda x:x['decision'].__setitem__('unrestricted_local_functional_exactness_claimed',True)),('quantum',lambda x:x['decision'].__setitem__('quantum_cohomology_constructed',True)),('protected',lambda x:x['decision'].__setitem__('protected_status_change',True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D); mutate(x); e=validate(x); assert e,label; print(f'PASS {i:02d}: rejects {label} via [FAIL] {e[0]}')
print(f'RESULT: PASS {len(mutations)}/{len(mutations)}')
