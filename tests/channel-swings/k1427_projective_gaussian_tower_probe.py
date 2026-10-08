#!/usr/bin/env python3
"""Mutation probe for K1427."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1427-projective-gaussian-tower.json').read_text())
def validate(x):
 t,q=x['projective_tower'],x['decision']; e=[]
 if 'pushes' not in t['consistency']: e.append('consistency')
 if 'Kolmogorov' not in t['continuum_measure']: e.append('continuum')
 for k in ('finite_marginals_projectively_consistent','countable_product_gaussian_measure_constructed','conditional_expectation_martingale_dense'):
  if not q[k]: e.append(k)
 for k in ('translation_invariant_infinite_dimensional_measure','nonlinear_field_measure_constructed','source_measure_identified','protected_status_change'):
  if q[k]: e.append(k)
 return e
assert not validate(D)
M=[('consistency',lambda x:x['projective_tower'].__setitem__('consistency','unknown')),('continuum',lambda x:x['projective_tower'].__setitem__('continuum_measure','unknown')),('marginals',lambda x:x['decision'].__setitem__('finite_marginals_projectively_consistent',False)),('product',lambda x:x['decision'].__setitem__('countable_product_gaussian_measure_constructed',False)),('martingale',lambda x:x['decision'].__setitem__('conditional_expectation_martingale_dense',False)),('translation',lambda x:x['decision'].__setitem__('translation_invariant_infinite_dimensional_measure',True)),('nonlinear',lambda x:x['decision'].__setitem__('nonlinear_field_measure_constructed',True)),('source',lambda x:x['decision'].__setitem__('source_measure_identified',True)),('protected',lambda x:x['decision'].__setitem__('protected_status_change',True))]
for i,(label,mutate) in enumerate(M,1):
 x=copy.deepcopy(D); mutate(x); assert validate(x),label; print(f'PASS {i:02d}: rejects {label}')
print(f'RESULT: PASS {len(M)}/{len(M)}')
