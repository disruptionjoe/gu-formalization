#!/usr/bin/env python3
"""Controls for K1524's stationary diagonal quasi-free formulas."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1524-stationary-quasi-free-exact-formulas.json').read_text())
def F(C,a,v):return a**4+6*a*a*v+3*v*v-6*C*(a*a+v)+9*C*C
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['quasi_free_formulas'],D['decision']
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1524'),('product Gaussian','N(alpha_j,s_j)' in q['trial_class']),('positive factors','s_j>0' in q['trial_class']),('stationarity','translation invariant' in q['trial_class']),('constant mean','constant zero mode a' in q['trial_class']),('free exact','(1/4)sum_j omega_j[alpha_j^2+(s_j-1)^2/s_j]' in q['free_cost']),('variance','v_N=sum_j lambda_j s_j' in q['point_variance']),('F formula','a^4+6a^2v+3v^2-6C(a^2+v)+9C^2' in q['wick_expectation']),('low optimizer','a^2=3(C-v)' in q['mean_optimization_low_variance']),('low minimum','6v(2C-v)' in q['mean_optimization_low_variance']),('high optimizer','a=0' in q['mean_optimization_high_variance']),('high minimum','3(v-C)^2+6C^2' in q['mean_optimization_high_variance']),('real guard','All coordinates are real' in q['normalization_guard']),('scope','do not cover nonstationary' in q['scope_guard']),('free proved',d['exact_free_cost_proved']),('W proved',d['exact_wick_expectation_proved']),('mean proved',d['mean_optimization_proved']),('diagonal only',d['stationary_diagonal_scope_only']),('full Gaussian fenced',not d['full_gaussian_classified']),('protected',not d['protected_status_change'])]
 for C,v in ((4.0,0.0),(4.0,1.0),(4.0,3.5)):
  a=math.sqrt(3*(C-v));checks.append((f'low branch C={C} v={v}',math.isclose(F(C,a,v),6*v*(2*C-v),abs_tol=1e-12)))
 for C,v in ((4.0,4.0),(4.0,6.0)):
  checks.append((f'high branch C={C} v={v}',math.isclose(F(C,0,v),3*(v-C)**2+6*C*C)))
 for s in (0.25,0.5,1.0,2.0):
  checks.append((f'free factor nonnegative {s}',(s-1)**2/s>=0))
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
