#!/usr/bin/env python3
"""Mutation probe for K1411."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1411-time-dependent-graph-energy.json').read_text())
def validate(x):
 f,q=x['graph_energy'],x['decision']; e=[]
 for key,needle in (('lifted_equation','psi_n'),('functional','F_n(t)'),('exact_derivative',"F_n'="),('gronwall','exp('),('outside_rigidity_class','nonlinear and time dependent')):
  if needle not in f[key]: e.append(key)
 if not q['estimate_cutoff_uniform']: e.append('uniform')
 if q['k1406_contradicted']: e.append('rigidity contradiction')
 if q['full_pde_global_bound_proved']: e.append('PDE overclaim')
 return e
assert not validate(D)
mutations=[('equation',lambda x:x['graph_energy'].__setitem__('lifted_equation','none')),('functional',lambda x:x['graph_energy'].__setitem__('functional','none')),('derivative',lambda x:x['graph_energy'].__setitem__('exact_derivative','unknown')),('gronwall',lambda x:x['graph_energy'].__setitem__('gronwall','none')),('class',lambda x:x['graph_energy'].__setitem__('outside_rigidity_class','same class')),('uniform',lambda x:x['decision'].__setitem__('estimate_cutoff_uniform',False)),('rigidity',lambda x:x['decision'].__setitem__('k1406_contradicted',True)),('PDE',lambda x:x['decision'].__setitem__('full_pde_global_bound_proved',True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D); mutate(x); e=validate(x); assert e,label; print(f'PASS {i:02d}: rejects {label} via [FAIL] {e[0]}')
print('RESULT: PASS 8/8')
