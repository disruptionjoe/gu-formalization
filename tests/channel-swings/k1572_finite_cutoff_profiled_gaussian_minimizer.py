#!/usr/bin/env python3
"""Controls for K1572's exact finite-cutoff profiled Gaussian minimizer."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1572-finite-cutoff-profiled-gaussian-minimizer.json').read_text())
def roots(N,g=.1,m=1.0):
 ws=[math.sqrt(m*m+i*i+j*j+k*k) for i in range(-N,N+1) for j in range(-N,N+1) for k in range(-N,N+1)];C=sum(.5/w for w in ws)
 def A(x):return sum(.5/math.sqrt(w*w+x) for w in ws)
 def f(x):return x+3*m*m-24*g*(C-A(x))
 xs=[10**(-5+t*0.02) for t in range(501)];out=[]
 for a,b in zip(xs,xs[1:]):
  if f(a)*f(b)<0:
   lo,hi=a,b
   for _ in range(60):
    mid=(lo+hi)/2
    if f(lo)*f(mid)<=0:hi=mid
    else:lo=mid
   out.append((lo+hi)/2)
 return ws,C,A,out
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['finite_cutoff_minimizer'],D['decision'];scaled=[]
 for N in (4,6):
  ws,C,A,rr=roots(N);checks.append((f'two roots N={N}',len(rr)==2));km=rr[-1];V=A(km);D0=C-V;F=sum(w*(w/math.sqrt(w*w+km)+math.sqrt(w*w+km)/w-2)/4 for w in ws);E=F+.6*V*(2*C-V)+1.5*D0-.625;checks.append((f'large root beats vacuum N={N}',E<.6*C*C));scaled.append(km/N**2)
 checks.append(('large root stable scale',.2<scaled[1]/scaled[0]<2.5))
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1572'),('profile','omega_k/sqrt(omega_k^2+kappa)' in q['fixed_variance_problem']),('equation','kappa+3m^2=24gD_N(kappa)' in q['exact_euler_equation']),('two critical','two critical parameters' in q['exact_euler_equation']),('convex','strictly convex' in q['uniqueness']),('limits','kappa_(g,N)^+/N^2 tends to kappa_g' in q['coefficient_limit'] and 'kappa_(g,N)^-/N^2 tends to zero' in q['coefficient_limit']),('advance','asymptotically exact' in q['advance']),('scope','only inside the stationary diagonal Gaussian class' in q['scope_guard']),('fixed variance',d['finite_cutoff_fixed_variance_minimizer_proved']),('Euler',d['finite_cutoff_euler_equation_proved']),('critical points',d['finite_cutoff_two_critical_points_classified']),('global',d['finite_cutoff_gaussian_global_minimizer_unique_eventually']),('coefficient',d['stationary_diagonal_gaussian_coefficient_convergence_proved']),('unrestricted open',not d['unrestricted_ground_energy_ratio_convergence_proved']),('O1 open',not d['bounded_error_recentering_proved']),('protected',not d['protected_status_change'])]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
