#!/usr/bin/env python3
"""Mutation probe for K1429."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1429-continuum-gaussian-brst-cohomology.json').read_text())
def validate(x):
 c,q=x['continuum_complex'],x['decision']; e=[]
 if 'number operator' not in c['hodge_operator']: e.append('Hodge')
 if 'chain maps' not in c['refinement']: e.append('refinement')
 for k in ('closed_continuum_gaussian_brst_operator_constructed','continuum_hodge_gap_positive','continuum_degreewise_ranges_closed','positive_nonzero_degree_zero_cohomology','higher_cohomology_zero','cohomology_refinement_stable'):
  if not q[k]: e.append(k)
 for k in ('interacting_quantum_brst_constructed','source_physical_cohomology_identified','protected_status_change'):
  if q[k]: e.append(k)
 return e
assert not validate(D)
M=[('Hodge',lambda x:x['continuum_complex'].__setitem__('hodge_operator','unknown')),('refinement',lambda x:x['continuum_complex'].__setitem__('refinement','unknown')),('closed',lambda x:x['decision'].__setitem__('closed_continuum_gaussian_brst_operator_constructed',False)),('gap',lambda x:x['decision'].__setitem__('continuum_hodge_gap_positive',False)),('ranges',lambda x:x['decision'].__setitem__('continuum_degreewise_ranges_closed',False)),('H0',lambda x:x['decision'].__setitem__('positive_nonzero_degree_zero_cohomology',False)),('higher',lambda x:x['decision'].__setitem__('higher_cohomology_zero',False)),('stable',lambda x:x['decision'].__setitem__('cohomology_refinement_stable',False)),('interacting',lambda x:x['decision'].__setitem__('interacting_quantum_brst_constructed',True)),('source',lambda x:x['decision'].__setitem__('source_physical_cohomology_identified',True))]
for i,(label,mutate) in enumerate(M,1):
 x=copy.deepcopy(D); mutate(x); assert validate(x),label; print(f'PASS {i:02d}: rejects {label}')
print(f'RESULT: PASS {len(M)}/{len(M)}')
