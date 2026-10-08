#!/usr/bin/env python3
"""Mutation probe for K1413."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1413-full-pde-graph-energy-leakage.json').read_text())
def validate(x):
 f,q=x['leakage'],x['decision']; e=[]
 for key,needle in (('lifted_field','Q commutes'),('exact_identity','E dot j_n'),('lifted_current','Q^(n+1)'),('homogeneous_restriction','reduces exactly to K1411'),('second_full_pde_defect','L-infinity_x'),('boundary','remain open')):
  if needle not in f[key]: e.append(key)
 if q['direct_homogeneous_energy_promotion_valid']: e.append('promotion overclaim')
 if q['all_full_pde_mechanisms_excluded']: e.append('global no-go overclaim')
 if q['completed_full_pde_flow_constructed']: e.append('flow overclaim')
 return e
assert not validate(D)
mutations=[('field',lambda x:x['leakage'].__setitem__('lifted_field','unknown')),('identity',lambda x:x['leakage'].__setitem__('exact_identity','zero')),('current',lambda x:x['leakage'].__setitem__('lifted_current','none')),('restriction',lambda x:x['leakage'].__setitem__('homogeneous_restriction','unrelated')),('coefficient',lambda x:x['leakage'].__setitem__('second_full_pde_defect','controlled')),('boundary',lambda x:x['leakage'].__setitem__('boundary','all excluded')),('promotion',lambda x:x['decision'].__setitem__('direct_homogeneous_energy_promotion_valid',True)),('no-go',lambda x:x['decision'].__setitem__('all_full_pde_mechanisms_excluded',True)),('flow',lambda x:x['decision'].__setitem__('completed_full_pde_flow_constructed',True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D); mutate(x); e=validate(x); assert e,label; print(f'PASS {i:02d}: rejects {label} via [FAIL] {e[0]}')
print('RESULT: PASS 9/9')
