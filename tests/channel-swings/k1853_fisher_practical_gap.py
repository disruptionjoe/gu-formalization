#!/usr/bin/env python3
"""Exact finite premises for K1853; analytic transfer is in the linked note."""
from fractions import Fraction as Q
from pathlib import Path
import json, hashlib, math
ROOT=Path(__file__).resolve().parents[2]

def mul(a,b):
 c=[Q(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c

def evaluate(c,x):
 z=Q(0)
 for a in reversed(c):z=z*x+a
 return z

def verify(d):
 n=list(map(Q,d['N']));den=list(map(Q,d['D']));k=d['grid_steps'];h=Q(4,k)
 assert all(x>0 for x in den)
 nd=mul([n[1],2*n[2]],den);dn=mul(n,[den[1],2*den[2]])
 coeff=[a-b for a,b in zip(nd,dn)]
 assert all(x>0 for x in coeff[:3]) and coeff[3]==0
 r=lambda y:evaluate(n,y)/evaluate(den,y)
 low=up=Q(0);minlow=maxup=Q(0)
 for i in range(k):
  low+=h*r(i*h)/2;up+=h*r((i+1)*h)/2
  minlow=min(minlow,low);maxup=max(maxup,up)
 assert minlow>Q(d['potential_lower']) and maxup<Q(d['potential_upper'])
 assert Q(d['potential_lower'])>=-Q(1,5) and Q(d['potential_upper'])<=2
 # Exact rational Taylor upper bound for exp(2), and geometric exp(1/5).
 exp2upper=sum(Q(2**i,math.factorial(i)) for i in range(6))+Q(2**6,math.factorial(6))/(1-Q(2,7))
 assert exp2upper<8
 zupper=Q(5,2)*Q(5,4);ref=Q(d['reference_density_lower'])
 assert ref<=1/(8*zupper)
 delta=Q(d['delta']);assert delta==Q(1752673,1000000)-Q(875729,500000)
 assert d['second_moment']==1 and d['fourth_moment']==2
 assert Q(3,4)>Q(6,7)**2
 assert delta/4*(2/ref)<Q(1,64)
 m=ref*(Q(6,7)-Q(1,8))**2
 assert Q(d['true_density_lower'])<=m
 B=1/Q(d['true_density_lower'])+Q(1,4)
 assert B<d['gap_denominator']<49
 # True-tail lower bound, with y=4+z and positive coefficients.
 assert Q(3,4)*2+Q(7,4)*2>4
 assert d['kinetic_coefficient']==4
 assert 1+108*(2*d['gap_denominator'])==10153
 assert d['gap_denominator']*delta<Q(6,25)**2
 assert d['gap_denominator']*Q(1,4700)==Q(1,100)
 assert d['full_line'] and not d['optimizer_equals_reference'] and not d['novelty']
 for dep in d['dependencies']:
  assert hashlib.sha256((ROOT/dep['path']).read_bytes()).hexdigest()==dep['sha256']
 return dict(monotone_coefficients=[str(x) for x in coeff],potential_min_lower=float(minlow),potential_max_upper=float(maxup),hardy_upper=str(B),gap_lower='1/'+str(d['gap_denominator']))
if __name__=='__main__':
 d=json.loads((ROOT/'lab/process/k1853-fisher-practical-gap.json').read_text());print(json.dumps(verify(d),sort_keys=True));print('K1853 exact finite premises PASS; continuum argument reviewed in prose')
