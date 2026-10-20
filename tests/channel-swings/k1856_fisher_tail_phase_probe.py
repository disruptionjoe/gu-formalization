#!/usr/bin/env python3
"""Independent Fraction fixtures; these do not prove continuum limits."""
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

m=json.loads((ROOT/'lab/process/k1856-fisher-tail-phase.json').read_text())
def verify(C):
 for c in [F(1,10),F(1),F(10),F(100)]:
  for t in [F(1,2),F(1,10),F(1,100),F(1,10000)]:
   e=t**C['tail_weight_power']/(c+t**C['tail_weight_power']);v=1-t;w=1+C['tail_variance_coefficient']*c/t
   check(0<e<1 and 0<v<w,'positive mixture')
   check((1-e)*v+e*w==1,'raw second')
   check(C['gaussian_fourth']*((1-e)*v*v+e*w*w)==3*(1+c),'raw fourth')
   check((1-e)/v+e/w-1==c*t/((1-t)*(c+t)),'reciprocal variance')
   check(t*C['gaussian_sixth']*e*w**3==15*(t+c)**3/(c+t*t),'sixth moment scale')
 for D in [F(1,10),F(1),F(5)]:
  for M in [F(20),F(100)]:
   R2=2*(M+15)/D;d=D/(4*R2**2)
   check(2*R2**2*d+(M+15)/R2==D,'tail split')
   check(4*d*d==D**6/(C['sixth_cap_denominator']*(M+15)**4),'cap constant')
base,faults=run_mutations(m['constants'],verify,{'tail_weight_power':3,'tail_variance_coefficient':2,'gaussian_fourth':4,'gaussian_sixth':14,'sixth_cap_denominator':32})
reporting_mutations(m)
print(f'PASS K1856: {base} independent rational controls; {faults} input faults; 2 reporting faults')
