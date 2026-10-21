#!/usr/bin/env python3
"""Independent Fraction controls and assertion-detected input faults."""
import copy,json,hashlib
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'lab/process/k1870-fisher-effective-two-well-stability.json'
def check(c):
 k=c['constants'];n=0
 def ck(ok,msg):
  nonlocal n
  assert ok,msg
  n+=1
 # Directly evaluate the proof's inequalities, independent of symbolic simplification.
 for i in range(1,51):
  r=F(i,100);a=1/(1-r/2)**2;delta=r**3
  lost=F(k['lost_mass_factor'])*delta/r**2
  ck(lost>=4*delta/r**2,'lost cutoff mass')
  for eta in [F(0),F(1,100),F(1)]:
   raw=(1+r)*(4+eta)/16+(1+1/r)*4*delta**2/r**4+a/4-(1-lost)/2
   upper=F(k['oscillator_defect_radius_factor'])*r+F(k['oscillator_defect_energy_factor'])*eta
   ck(upper>=raw,'localized oscillator energy bound')
 ck(F(k['even_TV_radius_factor'])>=2*4+4*3,'even triangle factor')
 ck(F(k['mean_zero_TV_radius_factor'])>=2*4+4*3+F(1,2),'mean-zero triangle factor')
 ck(F(k['TV_energy_sqrt_factor'])>=4*F(1,8),'square-root split factor')
 for v in [F(1,100),F(1,10),F(1,4)]:
  d=4*v-2*v*v;ck(1/v<=4/d,'explicit feasible trial upper')
 ck(F(k['example_TV'])>=F(k['mean_zero_TV_radius_factor'],10000)+F(1,10000),'finite tolerance budget')
 ck(k['example_product_count']*F(k['example_TV'])<=F(1,100),'product tolerance')
 math=n
 for key,value in c['scope'].items():ck(value==(key=='effective_endpoint_TV'),'scope '+key)
 for p,h in c['inputs'].items():ck(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'dependency '+p)
 return math,n-math
if __name__=='__main__':
 c=json.loads(P.read_text());m,r=check(c);print('PASS baseline',m,'rational mathematical checks',r,'reporting/dependency checks')
 faults={'lost_mass_factor':3,'oscillator_defect_radius_factor':8,'oscillator_defect_energy_factor':'1/32','even_TV_radius_factor':19,'mean_zero_TV_radius_factor':20,'TV_energy_sqrt_factor':'1/4','example_TV':'1/1000','example_product_count':5}
 caught=0
 for key,value in faults.items():
  x=copy.deepcopy(c);x['constants'][key]=value
  try:check(x)
  except AssertionError as e:print('[DETECTED mathematical-input]',key,str(e));caught+=1
  else:raise AssertionError('undetected '+key)
 for key in ['fixed_delta_deficit_modulus','entropy_bound','sharp_gap','source_owned','novelty_claim']:
  x=copy.deepcopy(c);x['scope'][key]=True
  try:check(x)
  except AssertionError as e:print('[DETECTED reporting]',key,str(e))
  else:raise AssertionError('undetected '+key)
 print('PASS',caught,'mathematical-input faults; 5 reporting faults')
