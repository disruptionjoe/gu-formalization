#!/usr/bin/env python3
"""Mutation probe for K1447."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1447-uv-dispersion-negative-scale-phase-diagram.json').read_text())
def v(x):
 b,q=x['coherent_model'],x['decision']; e=[]
 for key,needle in [('dispersion_and_covariance','q_beta'),('phase_boundary','beta(s+4)>9'),('checks','beta=1'),('ceiling','does not repair')]:
  if needle not in b[key]: e.append(key)
 for k in ('sharp_beta_s_phase_boundary_proved','beta_one_recovers_s_greater_than_five','l2_threshold_beta_greater_than_nine_fourths','form_dual_threshold_beta_greater_than_nine_fifths'):
  if not q[k]: e.append(k)
 for k in ('original_beta_one_interaction_constructed','representations_silently_mixed','protected_status_change'):
  if q[k]: e.append(k)
 return e
assert not v(D)
M=[('covariance',lambda x:x['coherent_model'].__setitem__('dispersion_and_covariance','mixed')),('boundary',lambda x:x['coherent_model'].__setitem__('phase_boundary','beta(s+4)>=9')),('check',lambda x:x['coherent_model'].__setitem__('checks','none')),('ceiling',lambda x:x['coherent_model'].__setitem__('ceiling','repairs beta=1')),('phase',lambda x:x['decision'].__setitem__('sharp_beta_s_phase_boundary_proved',False)),('l2',lambda x:x['decision'].__setitem__('l2_threshold_beta_greater_than_nine_fourths',False)),('original',lambda x:x['decision'].__setitem__('original_beta_one_interaction_constructed',True)),('mixed',lambda x:x['decision'].__setitem__('representations_silently_mixed',True)),('protected',lambda x:x['decision'].__setitem__('protected_status_change',True))]
for i,(l,m) in enumerate(M,1): x=copy.deepcopy(D); m(x); assert v(x),l; print(f'PASS {i:02d}: rejects {l}')
print(f'RESULT: PASS {len(M)}/{len(M)}')
