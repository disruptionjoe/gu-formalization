#!/usr/bin/env python3
"""Mutation probe for K1428."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1428-inductive-hilbert-haar-compatibility.json').read_text())
def validate(x):
 h,q=x['hilbert_limit'],x['decision']; e=[]
 if 'isometry' not in h['embedding']: e.append('embedding')
 if 'J_NM P_N' not in h['haar_compatibility']: e.append('Haar')
 for k in ('isometric_cylinder_embeddings_constructed','conditional_expectations_are_adjoints','inductive_limit_identified_with_continuum_L2','strongly_continuous_residual_circle_constructed','haar_projection_refinement_compatible'):
  if not q[k]: e.append(k)
 for k in ('charge_sequence_selected_by_source','complete_observable_quantization_constructed','protected_status_change'):
  if q[k]: e.append(k)
 return e
assert not validate(D)
M=[('embedding',lambda x:x['hilbert_limit'].__setitem__('embedding','unknown')),('Haar',lambda x:x['hilbert_limit'].__setitem__('haar_compatibility','unknown')),('isometry',lambda x:x['decision'].__setitem__('isometric_cylinder_embeddings_constructed',False)),('adjoint',lambda x:x['decision'].__setitem__('conditional_expectations_are_adjoints',False)),('limit',lambda x:x['decision'].__setitem__('inductive_limit_identified_with_continuum_L2',False)),('circle',lambda x:x['decision'].__setitem__('strongly_continuous_residual_circle_constructed',False)),('projector',lambda x:x['decision'].__setitem__('haar_projection_refinement_compatible',False)),('source',lambda x:x['decision'].__setitem__('charge_sequence_selected_by_source',True)),('complete',lambda x:x['decision'].__setitem__('complete_observable_quantization_constructed',True))]
for i,(label,mutate) in enumerate(M,1):
 x=copy.deepcopy(D); mutate(x); assert validate(x),label; print(f'PASS {i:02d}: rejects {label}')
print(f'RESULT: PASS {len(M)}/{len(M)}')
