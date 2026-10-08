#!/usr/bin/env python3
"""Mutation probe for K1448."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1448-uv-softened-interacting-hamiltonian.json').read_text())
def v(x):
 b,q=x['interacting_control'],x['decision']; e=[]
 for key,needle in [('regime','beta>3'),('counterterms','-6 C_(beta,N)'),('uniform_lower_bound','-6 C_beta^2'),('limit','L2(mu_beta)'),('strong_resolvent','t||V_N-V||_1'),('ceiling','beta=1')]:
  if needle not in b[key]: e.append(key)
 for k in ('all_counterterms_stated','uniform_semiboundedness_proved','closed_interacting_limit_form_constructed','strong_resolvent_convergence_constructed'):
  if not q[k]: e.append(k)
 for k in ('original_beta_one_hamiltonian_constructed','interacting_brst_constructed','source_hamiltonian_identified','protected_status_change'):
  if q[k]: e.append(k)
 return e
assert not v(D)
M=[('beta',lambda x:x['interacting_control'].__setitem__('regime','beta>9/5')),('counterterm',lambda x:x['interacting_control'].__setitem__('counterterms','none')),('lower',lambda x:x['interacting_control'].__setitem__('uniform_lower_bound','positive')),('limit',lambda x:x['interacting_control'].__setitem__('limit','formal')),('resolvent',lambda x:x['interacting_control'].__setitem__('strong_resolvent','asserted')),('ceiling',lambda x:x['interacting_control'].__setitem__('ceiling','solves original')),('closed',lambda x:x['decision'].__setitem__('closed_interacting_limit_form_constructed',False)),('strong',lambda x:x['decision'].__setitem__('strong_resolvent_convergence_constructed',False)),('original',lambda x:x['decision'].__setitem__('original_beta_one_hamiltonian_constructed',True)),('brst',lambda x:x['decision'].__setitem__('interacting_brst_constructed',True)),('source',lambda x:x['decision'].__setitem__('source_hamiltonian_identified',True)),('protected',lambda x:x['decision'].__setitem__('protected_status_change',True))]
for i,(l,m) in enumerate(M,1): x=copy.deepcopy(D); m(x); assert v(x),l; print(f'PASS {i:02d}: rejects {l}')
print(f'RESULT: PASS {len(M)}/{len(M)}')
