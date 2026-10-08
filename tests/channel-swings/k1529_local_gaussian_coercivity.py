#!/usr/bin/env python3
"""Controls for K1529's pointwise Gaussian coercivity."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1529-local-gaussian-coercivity.json').read_text())
def F(C,h,v):return h**4+6*h*h*v+3*v*v-6*C*(h*h+v)+9*C*C
def f(C,v):return 6*v*(2*C-v) if v<=C else 3*(v-C)**2+6*C*C
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['local_coercivity'],D['decision'];c=6*(math.sqrt(3)-1)
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1529'),('local variance','b_N(x)^T S b_N(x)>=0' in q['field_data']),('exact fourth','h^4+6h^2v+3v^2' in q['exact_expectation']),('two branches','6v(2C-v)' in q['mean_optimization'] and '3(v-C)^2+6C^2' in q['mean_optimization']),('sharp constant','6(sqrt(3)-1)' in q['uniform_coercivity']),('sqrt3 minimizer','t=sqrt(3)' in q['uniform_coercivity']),('spike guard','local-variance spikes cannot evade' in q['spike_guard']),('integrated trace','V_N=integral v(x)dx=Tr(Lambda S)' in q['integrated_consequence']),('scope nonstationary','does not impose stationarity or diagonal covariance' in q['scope_guard']),('arbitrary mean',d['arbitrary_mean_included']),('varying variance',d['spatially_varying_variance_included']),('constant decision',d['sharp_linear_coercivity_constant']=='6(sqrt(3)-1)'),('no spike escape',not d['variance_spike_escape_exists']),('nongaussian fenced',not d['nongaussian_moment_bound_proved']),('protected',not d['protected_status_change'])]
 for C in (0.5,2.0,7.0):
  for t in (0.0,0.1,0.7,1.0,math.sqrt(3),3.0,20.0):
   v=C*t;y=max(0.0,3*(C-v));h=math.sqrt(y)
   checks += [(f'mean minimum C={C} t={t}',math.isclose(F(C,h,v),f(C,v),rel_tol=1e-12,abs_tol=1e-10)),(f'coercivity C={C} t={t}',f(C,v)+1e-10>=c*C*v)]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
