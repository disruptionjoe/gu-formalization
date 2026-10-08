#!/usr/bin/env python3
"""Mutation probe for K1409."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1409-homogeneous-current-free-invariant-manifold.json').read_text())
def validate(x):
 f,q=x['invariant_manifold'],x['decision']; e=[]
 for key,needle in (('real_structure','CQ=QC'),('data','A=E=0'),('spatial_current','=0'),('charge_density','=0'),('reduced_equation',"u''+(m^2+mu Q^2)u+lambda||u||^2u=0"),('boundary','not a gauge fixing')):
  if needle not in f[key]: e.append(key)
 if not q['homogeneous_real_slice_invariant']: e.append('invariance')
 if q['full_spatial_flow_constructed']: e.append('full overclaim')
 if q['source_reality_selected']: e.append('source overclaim')
 return e
assert not validate(D)
mutations=[('real',lambda x:x['invariant_manifold'].__setitem__('real_structure','none')),('data',lambda x:x['invariant_manifold'].__setitem__('data','general')),('current',lambda x:x['invariant_manifold'].__setitem__('spatial_current','unknown')),('density',lambda x:x['invariant_manifold'].__setitem__('charge_density','unknown')),('equation',lambda x:x['invariant_manifold'].__setitem__('reduced_equation','unknown')),('boundary',lambda x:x['invariant_manifold'].__setitem__('boundary','all solutions')),('invariance',lambda x:x['decision'].__setitem__('homogeneous_real_slice_invariant',False)),('full',lambda x:x['decision'].__setitem__('full_spatial_flow_constructed',True)),('source',lambda x:x['decision'].__setitem__('source_reality_selected',True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D); mutate(x); e=validate(x); assert e,label; print(f'PASS {i:02d}: rejects {label} via [FAIL] {e[0]}')
print('RESULT: PASS 9/9')
