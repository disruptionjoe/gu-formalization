#!/usr/bin/env python3
"""Controls for K1433's exact equal-time Wick fourth-chaos obstruction."""
import hashlib,json,math
from functools import lru_cache
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1433-three-dimensional-wick-chaos-obstruction.json').read_text()); n=0
def check(label,value):
 global n
 assert value,label; n+=1; print(f'PASS {n:02d}: {label}')
for key,pin in D['pinned_inputs'].items(): check(f'{key} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
M,R,Q=D['declared_model'],D['fourth_chaos_obstruction'],D['decision']
check('normalized torus declared','torus' in M['space'])
check('real Gaussian field declared','real centered Gaussian' in M['field'])
check('nested box cutoff declared','K_N' in M['cutoff'])
check('equal-time covariance declared','2 sqrt' in M['covariance'])
check('Euclidean/source fence','not the Euclidean' in M['scope'] and 'not a source-selected' in M['scope'])

def pairings(items):
 if not items: return [()]
 a=items[0]; out=[]
 for j in range(1,len(items)):
  b=items[j]
  for rest in pairings(items[1:j]+items[j+1:]): out.append(((a,b),)+rest)
 return out
def gaussian_moment(labels,rho):
 def cov(a,b): return rho if a!=b else 1
 return sum(math.prod(cov(a,b) for a,b in p) for p in pairings(tuple(labels)))
rho=.37
e44=gaussian_moment('XXXXYYYY',rho)
e42=gaussian_moment('XXXXYY',rho)
e24=gaussian_moment('XXYYYY',rho)
e22=gaussian_moment('XXYY',rho)
wick4=e44-6*e42-6*e24+36*e22+3*3+3*3-18*1-18*1+9
check('independent Isserlis H4 pairing',abs(wick4-24*rho**4)<1e-10)
h4h2=gaussian_moment('XXXXYY',rho)-6*gaussian_moment('XXYY',rho)+3*gaussian_moment('YY',rho)
check('fourth and second chaos orthogonal',abs(h4h2)<1e-10)

def lower(N,d,m=1): return 1.5*(N//8+1)**(3*d)/(m*m+d*N*N)**2
for N in (8,16,32):
 lo=N//8; hi=N//4
 check(f'cone membership N={N}',3*hi<=N and lo>=1)
 check(f'positive exact lower N={N}',lower(N,3)>0)
scaled=[lower(N,3)/N**5 for N in (64,128,256)]
check('N^5 lower scaling stabilizes',min(scaled)>0 and max(scaled)/min(scaled)<4)
check('cone count exponent', '(N/8+1)^(3d)' in R['lower_bound'])
check('martingale identity stated','conditional on F_N' in R['martingale'])
check('variance identity stated','24 integral' in R['variance_identity'])
check('lower-chaos variance fence','Var(U_N)>=Var(V_N)' in R['lower_chaos_counterterms'])
for key in ('exact_equal_time_fourier_model_declared','wick_fourth_chaos_variance_identity_proved'): check(key,Q[key])
check('N5 decision',Q['three_dimensional_variance_lower_bound_order']=='N^5')
for key in ('wick_martingale_L2_bounded','quadratic_and_vacuum_counterterms_cancel_fourth_chaos','L2_multiplication_potential_limit_constructed','renormalized_form_or_resolvent_nonexistence_proved','source_or_protected_status_change'): check(f'{key} fenced',not Q[key])
check('operator ceiling preserved','does not exclude' in R['operator_ceiling'])
print(f'RESULT: PASS {n}/{n}')
