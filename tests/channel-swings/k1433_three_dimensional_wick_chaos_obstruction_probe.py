#!/usr/bin/env python3
"""Mutation probe for K1433."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1433-three-dimensional-wick-chaos-obstruction.json').read_text())
def validate(x):
 m,r,q=x['declared_model'],x['fourth_chaos_obstruction'],x['decision']; e=[]
 if '2 sqrt' not in m['covariance']: e.append('covariance')
 if '24 integral' not in r['variance_identity']: e.append('variance')
 if 'N^5' not in r['d3_consequence']: e.append('growth')
 if 'Var(U_N)>=Var(V_N)' not in r['lower_chaos_counterterms']: e.append('chaos')
 for k in ('exact_equal_time_fourier_model_declared','wick_fourth_chaos_variance_identity_proved'):
  if not q[k]: e.append(k)
 for k in ('wick_martingale_L2_bounded','quadratic_and_vacuum_counterterms_cancel_fourth_chaos','L2_multiplication_potential_limit_constructed','renormalized_form_or_resolvent_nonexistence_proved','source_or_protected_status_change'):
  if q[k]: e.append(k)
 return e
assert not validate(D)
M=[('covariance',lambda x:x['declared_model'].__setitem__('covariance','unspecified')),('variance',lambda x:x['fourth_chaos_obstruction'].__setitem__('variance_identity','unknown')),('growth',lambda x:x['fourth_chaos_obstruction'].__setitem__('d3_consequence','unknown')),('chaos',lambda x:x['fourth_chaos_obstruction'].__setitem__('lower_chaos_counterterms','unknown')),('model',lambda x:x['decision'].__setitem__('exact_equal_time_fourier_model_declared',False)),('identity',lambda x:x['decision'].__setitem__('wick_fourth_chaos_variance_identity_proved',False)),('L2',lambda x:x['decision'].__setitem__('wick_martingale_L2_bounded',True)),('counterterm',lambda x:x['decision'].__setitem__('quadratic_and_vacuum_counterterms_cancel_fourth_chaos',True)),('potential',lambda x:x['decision'].__setitem__('L2_multiplication_potential_limit_constructed',True)),('operator',lambda x:x['decision'].__setitem__('renormalized_form_or_resolvent_nonexistence_proved',True)),('protected',lambda x:x['decision'].__setitem__('source_or_protected_status_change',True))]
for i,(label,mutate) in enumerate(M,1):
 x=copy.deepcopy(D); mutate(x); assert validate(x),label; print(f'PASS {i:02d}: rejects {label}')
print(f'RESULT: PASS {len(M)}/{len(M)}')
