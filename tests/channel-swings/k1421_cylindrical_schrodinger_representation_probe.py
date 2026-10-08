#!/usr/bin/env python3
"""Mutation probe for K1421."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1421-cylindrical-schrodinger-representation.json').read_text())
def validate(x):
 r,q=x['representation'],x['decision']; e=[]
 if 'Gaussian' not in r['measure']: e.append('measure')
 if 'unitary' not in r['circle_action']: e.append('unitary')
 for k in ('positive_finite_cylindrical_representation','residual_circle_unitary','dense_invariant_polynomial_core','bounded_invariant_multipliers_represented'):
  if not q[k]: e.append(k)
 for k in ('preferred_continuum_measure_constructed','source_representation_identified'):
  if q[k]: e.append(k)
 return e
assert not validate(D)
M=[('measure',lambda x:x['representation'].__setitem__('measure','Lebesgue')),('unitary',lambda x:x['representation'].__setitem__('circle_action','unknown')),('positive',lambda x:x['decision'].__setitem__('positive_finite_cylindrical_representation',False)),('circle',lambda x:x['decision'].__setitem__('residual_circle_unitary',False)),('core',lambda x:x['decision'].__setitem__('dense_invariant_polynomial_core',False)),('observable',lambda x:x['decision'].__setitem__('bounded_invariant_multipliers_represented',False)),('continuum',lambda x:x['decision'].__setitem__('preferred_continuum_measure_constructed',True)),('source',lambda x:x['decision'].__setitem__('source_representation_identified',True))]
for i,(label,mutate) in enumerate(M,1):
 x=copy.deepcopy(D); mutate(x); assert validate(x),label; print(f'PASS {i:02d}: rejects {label}')
print(f'RESULT: PASS {len(M)}/{len(M)}')
