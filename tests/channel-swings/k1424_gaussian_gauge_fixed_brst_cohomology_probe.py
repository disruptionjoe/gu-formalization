#!/usr/bin/env python3
"""Mutation probe for K1424."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1424-gaussian-gauge-fixed-brst-cohomology.json').read_text())
def validate(x):
 g,q=x['gauge_fixed_complex'],x['decision']; e=[]
 if 'number operator' not in g['hodge_operator']: e.append('hodge')
 for k in ('closed_nilpotent_gauge_fixed_differential','positive_hodge_gap','closed_ranges','degree_zero_cohomology_equals_compact_invariant_reduced_block','positive_nonzero_finite_block_cohomology'):
  if not q[k]: e.append(k)
 for k in ('translation_invariant_measure','continuum_quantum_brst_constructed'):
  if q[k]: e.append(k)
 return e
assert not validate(D)
M=[('hodge',lambda x:x['gauge_fixed_complex'].__setitem__('hodge_operator','unknown')),('closed',lambda x:x['decision'].__setitem__('closed_nilpotent_gauge_fixed_differential',False)),('gap',lambda x:x['decision'].__setitem__('positive_hodge_gap',False)),('range',lambda x:x['decision'].__setitem__('closed_ranges',False)),('H0',lambda x:x['decision'].__setitem__('degree_zero_cohomology_equals_compact_invariant_reduced_block',False)),('positive',lambda x:x['decision'].__setitem__('positive_nonzero_finite_block_cohomology',False)),('translation',lambda x:x['decision'].__setitem__('translation_invariant_measure',True)),('continuum',lambda x:x['decision'].__setitem__('continuum_quantum_brst_constructed',True))]
for i,(label,mutate) in enumerate(M,1):
 x=copy.deepcopy(D); mutate(x); assert validate(x),label; print(f'PASS {i:02d}: rejects {label}')
print(f'RESULT: PASS {len(M)}/{len(M)}')
