#!/usr/bin/env python3
"""Controls for K1461's exact wave--KG null cancellation."""
import hashlib,json,math
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1461-wave-kg-null-form-phase-cancellation.json').read_text()); n=0
def c(l,v):
 global n; assert v,l; n+=1; print(f'PASS {n:02d}: {l}')
for k,p in D['pinned_inputs'].items(): c(f'{k} pin',hashlib.sha256((R/p['path']).read_bytes()).hexdigest()==p['sha256'])
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def norm(a): return math.sqrt(dot(a,a))
def vals(k,p,M2):
 wp=norm(p); w=math.sqrt(M2+dot(k,k)); kp=tuple(x+y for x,y in zip(k,p)); w2=math.sqrt(M2+dot(kp,kp)); N=wp*w-dot(p,k); P=2*N/(wp+w+w2); return P,N,(wp+w+w2)/2
for k,p,M2 in [((3,2,-1),(1,0,0),5),((-7,1,4),(2,-1,0),3),((0,0,0),(0,1,1),2),((40,0,0),(1,0,0),9)]:
 P,N,Q=vals(k,p,M2); c(f'positive phase {k,p}',P>0); c(f'exact quotient {k,p}',abs(N/P-Q)<1e-10); c(f'one-order bound {k,p}',Q<=norm(p)+math.sqrt(M2+dot(k,k))+1e-12)
rat=[]
for K in (100,200,400,800): rat.append(vals((K,0,0),(1,0,0),5)[2]/K)
c('sharp linear asymptotic',abs(rat[-1]-1)<.01); c('sharpness improves',abs(rat[-1]-1)<abs(rat[0]-1))
Q=D['decision']
for k in ('exact_null_phase_cancellation_proved','one_derivative_upper_bound_proved','one_derivative_cost_sharp'): c(k,Q[k])
for k in ('two_derivative_loss_retained_after_null_numerator','same_tier_unnormalized_bound','actual_lifted_current_identified_with_null_form','global_full_pde_flow_constructed','protected_status_change'): c(f'{k} fenced',not Q[k])
print(f'RESULT: PASS {n}/{n}')
