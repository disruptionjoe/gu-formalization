#!/usr/bin/env python3
"""Independent polynomial arrays and Fraction moments, no Sympy/producer import."""
from pathlib import Path
import json, hashlib
ROOT=Path(__file__).resolve().parents[2]
from fractions import Fraction as F
from copy import deepcopy
import math
checks=0
def check(ok,label):
 global checks
 checks+=1
 if not ok: raise AssertionError(label)
def run_mutations(base,verify,changes):
 verify(base)
 clean=checks
 for key,value in changes.items():
  bad=deepcopy(base);bad[key]=value
  try: verify(bad)
  except AssertionError as err: print('[DETECTED INPUT]',key,': [FAIL]',err)
  else: raise AssertionError('undetected '+key)
 return clean,len(changes)
def reporting(m):
 for p,h in m['dependencies'].items():check(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'dependency '+p)
 check(m['scope']['gu_physics'] is False,'scope')
def reporting_mutations(m):
 reporting(m)
 for field in ['dependency','scope']:
  b=deepcopy(m)
  if field=='dependency':b['dependencies'][next(iter(b['dependencies']))]='0'*64
  else:b['scope']['gu_physics']=True
  try:reporting(b)
  except AssertionError as err:print('[DETECTED REPORT]',field,': [FAIL]',err)
  else:raise AssertionError('undetected report '+field)

m=json.loads((ROOT/'lab/process/k1857-fisher-gaussian-profile.json').read_text())
def add(a,b):return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]
def mul(a,b):
 out=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out
def scale(a,t):return [x*t for x in a]
def derivative(a):return [i*a[i] for i in range(1,len(a))]
def moment(n):
 if n%2:return 0
 out=1
 for k in range(1,n,2):out*=k
 return out
def G(a):return sum(c*moment(i) for i,c in enumerate(a))
def verify(C):
 H3=[0,-3,0,1];H4=[3,0,-6,0,1];r=scale(H4,-F(1,C['profile_denominator']));dr=derivative(r)
 check(add(dr,scale(H3,F(1,12)))==[0]*4,'derivative profile')
 check(G(r)==0,'mean tangent');check(G(mul([0,0,1],r))==0,'second tangent')
 check(G(mul([0,0,0,0,1],scale(H4,-F(1,C['density_denominator']))))==-1,'fourth tangent')
 check(G(mul(dr,dr))==F(1,C['derivative_norm_denominator']),'derivative norm')
 check(G(mul(r,r))==F(1,C['sqrt_distance_denominator']),'sqrt distance')
 check(G(mul(r,r))/2==F(1,C['affinity_denominator']),'affinity')
 check(add(add(derivative(H3),scale(mul([0,1],H3),-1)),H4)==[0]*5,'Gaussian primitive')
 for q in [F(1,100),F(1,200),F(1,1000),F(1,10000)]:
  e=q**C['tail_weight_power'];w=q**C['tail_variance_power'];v=(1-q**6)/(1-q**10);k0=(3-q-3*q*q)*(1-q**10)/(1-q**6)**2
  check(1<k0<3 and v>0 and 0<e<1,'domain')
  check((1-e)*v+e*w==1,'contaminated second')
  check((1-e)*v*v*k0+3*e*w*w==3-q,'contaminated fourth')
  check(15*e*w**3==C['tail_sixth_coefficient']/q**2,'sixth divergence')
  q0=3-k0
  check(q<q0<q+4*q*q,'q0 bracket')
base,faults=run_mutations(m['constants'],verify,{'profile_denominator':24,'density_denominator':48,'derivative_norm_denominator':48,'sqrt_distance_denominator':192,'affinity_denominator':96,'tail_weight_power':9,'tail_variance_power':-3,'tail_sixth_coefficient':14})
reporting_mutations(m)
print(f'PASS K1857: {base} independent polynomial/rational controls; {faults} input faults; 2 reporting faults')
