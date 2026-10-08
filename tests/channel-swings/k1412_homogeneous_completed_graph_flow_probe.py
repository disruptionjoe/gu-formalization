#!/usr/bin/env python3
"""Mutation probe for K1412."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1412-homogeneous-completed-graph-flow.json').read_text())
def validate(x):
 f,q=x['completed_flow'],x['decision']; e=[]
 for key,needle in (('tier','G_n='),('uniform_cutoffs','independent of N'),('difference_equation','delta='),('cauchy_estimate','Gronwall'),('global_limit','two-sided global flow'),('boundary','not on the spatially dependent')):
  if needle not in f[key]: e.append(key)
 if not q['spectral_cutoff_cauchy_convergence_proved']: e.append('Cauchy decision')
 if q['full_completed_pde_flow_constructed']: e.append('PDE overclaim')
 if q['bv_bfv_physical_flow_constructed']: e.append('physical overclaim')
 return e
assert not validate(D)
mutations=[('tier',lambda x:x['completed_flow'].__setitem__('tier','none')),('uniform',lambda x:x['completed_flow'].__setitem__('uniform_cutoffs','N dependent')),('difference',lambda x:x['completed_flow'].__setitem__('difference_equation','unknown')),('Cauchy',lambda x:x['completed_flow'].__setitem__('cauchy_estimate','none')),('global',lambda x:x['completed_flow'].__setitem__('global_limit','local')),('boundary',lambda x:x['completed_flow'].__setitem__('boundary','full PDE')),('decision',lambda x:x['decision'].__setitem__('spectral_cutoff_cauchy_convergence_proved',False)),('PDE',lambda x:x['decision'].__setitem__('full_completed_pde_flow_constructed',True)),('physical',lambda x:x['decision'].__setitem__('bv_bfv_physical_flow_constructed',True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D); mutate(x); e=validate(x); assert e,label; print(f'PASS {i:02d}: rejects {label} via [FAIL] {e[0]}')
print('RESULT: PASS 9/9')
