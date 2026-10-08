#!/usr/bin/env python3
"""Controls for K1504's growing Hermite trial."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1504-growing-hermite-trial.json').read_text())
def add(a,b):
 out=[0.0]*max(len(a),len(b))
 for i,x in enumerate(a):out[i]+=x
 for i,x in enumerate(b):out[i]+=x
 return out
def scale(a,s):return [s*x for x in a]
def mul_x(a):return [0.0]+a
def hermite_normalized(n):
 if n==0:return [1.0]
 p0,p1=[1.0],[0.0,1.0]
 for j in range(1,n):p0,p1=p1,add(mul_x(p1),scale(p0,-j))
 return scale(p1,1/math.sqrt(math.factorial(n)))
def gauss_moment(n):return 0.0 if n%2 else odddf(n-1)
def odddf(n):
 out=1
 for k in range(1,n+1,2):out*=k
 return float(out)
def expectation(poly):return sum(c*gauss_moment(i) for i,c in enumerate(poly))
def multiply(a,b):
 out=[0.0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 h,t,q=D['hermite_control'],D['transfer'],D['decision']
 checks += [('claim',D['claim_id']=='K1504'),('basis','sqrt(j!)' in h['basis']),('coefficients','exp(C_H j log(j+1))' in h['coefficient_bound']),('trial','phi_(d_N-1)-phi_(d_N)' in h['trial']),('degree','M_N/3' in h['degree']),('moment ceiling','2d_N+1' in h['moment_orders'] and '<=M_N' in h['moment_orders']),('Gaussian norm','=1' in t['gaussian_norm']),('Gaussian quotient','-sqrt(d_N)' in t['gaussian_quotient']),('cutoff norm','1+o(1)' in t['cutoff_norm']),('cutoff quotient','-sqrt(d_N)+o(1)' in t['cutoff_quotient']),('eventual half','-sqrt(d_N)/2' in t['eventual_bound']),('transfer proved',q['one_growing_hermite_trial_transferred']),('operator fenced',not q['growing_jacobi_operator_norm_convergence_proved']),('largest fenced',not q['largest_degree_window_proved']),('protected fenced',not q['protected_status_change'])]
 for d in range(1,11):
  p=scale(add(hermite_normalized(d-1),scale(hermite_normalized(d),-1)),1/math.sqrt(2));p2=multiply(p,p)
  checks.append((f'd{d} norm',abs(expectation(p2)-1)<1e-8))
  checks.append((f'd{d} quotient',abs(expectation(mul_x(p2))+math.sqrt(d))<1e-7))
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
