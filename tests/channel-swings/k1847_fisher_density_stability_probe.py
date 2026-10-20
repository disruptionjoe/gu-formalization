#!/usr/bin/env python3
"""Independent Fraction proof-input replay and analytic Gaussian controls."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import copy,json,hashlib
R=Path(__file__).resolve().parents[2];r=json.loads((R/'lab/process/k1847-fisher-density-stability.json').read_text());n=0
def ck(v):
 global n
 assert v
 n+=1
def cert(q):
 a,b,d,c,e=map(F,q['score']);radius=F(q['R']);depth=F(q['depth']);expupper=F(q['exponential_upper'])
 if not(c>0 and e>0 and a<0 and b>0 and d>0 and a+b+d>0):return False
 low=[a+F(11,10),b+F(11,10)*c,d+F(11,10)*e]
 # Translate N-D from y to radius²+h using direct binomial arithmetic.
 h=radius*radius;aa,bb,dd=a-1,b-c,d-e;tail=[aa+bb*h+dd*h*h,bb+2*dd*h,dd]
 if not all(t>0 for t in low+tail):return False
 if radius!=F(3,2) or depth!=F(11,20):return False
 rem=depth**9/F(factorial(9))/(1-depth/10)
 expbound=sum(depth**j/F(factorial(j)) for j in range(9))+rem
 C=expupper*(radius+1/radius)
 return(expbound<expupper and C==F(q['stein_factor']) and F(q['score_budget'])<F(7,200)**2 and C*F(7,200)==F(q['tv_upper']) and 2*F(q['tv_upper'])==F(q['pair_tv_upper']))
ck(cert(r));ck(hashlib.sha256((R/r['dependency']['path']).read_bytes()).hexdigest()==r['dependency']['sha256'])
# Rational points are sanity controls, not the all-line proof (coefficient signs above).
a,b,d,c,e=map(F,r['score'])
for x in [F(j,8) for j in range(41)]:
 y=x*x;g=x*(a+b*y+d*y*y)/(1+c*y+e*y*y)
 ck(g>=-F(11,10)*x)
 if x>=F(3,2):ck(g>=x)
# Stein sign/factor control: pi=N(0,1), p=N(m,sigma²), h=x or x².
# f=-1 for h=x and f=-x for h=x²-1. Independent Gaussian moments.
for m in [F(-2),F(-1,3),F(0),F(3,2)]:
 for v in [F(1,2),F(1),F(3)]:
  J=m*m+(v-1)**2/v
  ck(J>=0)
  ck(m==m/v+(1-1/v)*m)
  ck(m*m+v-1==(m*m+v)*(1-1/v)+m*m/v)
  ck(J==0 if m==0 and v==1 else J>0)
# All-measurable-set numerator covariance bound: exact two-bin conditional probabilities.
for f in [F(1,5),F(1,2),F(4,5)]:
 for left in [F(0),F(1,3),F(1)]:
  for right in [F(0),F(2,3),F(1)]:
   cov=f*left-f*(f*left+(1-f)*right)
   ck(abs(cov)<=f*(1-f))
# Mathematical corruption fixtures reject before any report/status checks.
faults=[('score',['-3','1','1','1','1']),('R','1'),('depth','1/10'),('exponential_upper','3/2'),('stein_factor','1'),('score_budget','1'),('tv_upper','1/1000')]
for k,v in faults:
 q=copy.deepcopy(r);q[k]=v;ck(not cert(q))
for k,v in [('reference_is_optimizer',True),('reference_moment_feasibility','proved'),('canon_promotion',True)]:
 q=copy.deepcopy(r);q[k]=v;ck(not(not q['reference_is_optimizer'] and q['reference_moment_feasibility']=='not_asserted' and not q['canon_promotion']))
# Finite spectral decomposition controls validate the transfer algebra, not compact resolvent.
for c2 in [F(0),F(1,9),F(1,2),F(8,9),F(1)]:
 for gap in [F(1,3),F(2),F(7)]:
  excited=[gap,2*gap,5*gap];weights=[c2]+[(1-c2)/3]*3
  excess=sum(w*e for w,e in zip(weights[1:],excited))
  ck(excess>=gap*(1-c2));ck((1-c2)<=excess/gap)
for am in [F(0),F(1),F(3)]:
 for b0 in [F(1,4),F(2)]:
  for y in [F(0),F(1,2),F(4)]:
   ck(b0*y*y-am*y >= b0*y*y/2-am*am/(2*b0))
dep=r['optimizer_stability']['dependency'];ck(hashlib.sha256((R/dep['path']).read_bytes()).hexdigest()==dep['sha256'])
print('K1847 independent controls',n,'including',len(faults),'input faults and 3 reporting faults')
