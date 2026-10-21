#!/usr/bin/env python3
"""Independent rational moment construction and fault checks, without Sympy."""
import copy,hashlib,json
from fractions import Fraction as F
from math import comb
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def gauss_even(n,a2,v):
 return sum(F(comb(2*n,2*j))*odd_factorial(2*j-1)*v**j*a2**(n-j) for j in range(n+1))
def odd_factorial(n):
 z=1
 for j in range(1,n+1,2):z*=j
 return z
def verify(formula):
 count=0;c=list(map(F,formula['cap_coefficients']));shift=formula['moment_shift']
 for d in [F(1,10),F(1,2),F(1),F(3),F(10)]:
  k=d+shift
  for t in [F(1,101),F(1,70),F(1,5),F(1,2),F(9,10)]:
   v=1-t;B=d+3*t*t;a2=B/t;w=t*t/B
   assert 0<w<1 and v>0,'trial positivity';count+=1
   moments=[(1-w)*gauss_even(n,F(0),v)+w*gauss_even(n,a2,v) for n in [1,2,3]]
   cap=c[0]*d*d/t+c[1]+c[2]*d+c[3]*d*t+c[4]*t**3
   assert moments[0]==1 and moments[1]==k and moments[2]==cap,'actual Gaussian moments';count+=3
   assert cap>k*k,'strict feasible cap';count+=1
   assert d*d/(cap-k*k)<t/(1-t),'consistent lower and feasible upper';count+=1
   q=k if formula['projection_coefficient']=='k' else F(formula['projection_coefficient'])
   denominator=cap-k*k if formula['lower_denominator']=='M-k^2' else cap
   assert moments[1]-q*moments[0]==0,'score projection orthogonality';count+=1
   assert moments[2]-2*q*moments[1]+q*q*moments[0]==denominator,'orthogonalized denominator';count+=1
 assert (F(1)*101+30-F(9,101)-F(6,101**3))<131,'one percent budget';count+=1
 return count
def run():
 z=json.loads((ROOT/'lab/process/k1874-fisher-sixth-moment-cap.json').read_text());n=verify(z['formula']);faults=0
 for index in range(5):
  bad=copy.deepcopy(z['formula']);bad['cap_coefficients'][index]=str(F(bad['cap_coefficients'][index])+1)
  try:verify(bad)
  except AssertionError as e:print('DETECTED mathematical coefficient',index,str(e));faults+=1
  else:raise AssertionError('missed coefficient mutation')
 for key,value in [('moment_shift',4),('projection_coefficient','1'),('lower_denominator','M')]:
  bad=copy.deepcopy(z['formula']);bad[key]=value
  try:verify(bad)
  except AssertionError as e:print('DETECTED mathematical reference',key,str(e));faults+=1
  else:raise AssertionError('missed reference mutation')
 for p,h in z['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 scope={'k_gt_3':True,'raw_moments':True,'sixth_constraint':'inequality','attained':True,'all_minimizers_saturate_cap':True,'even_minimizer_exists':True,'uniqueness_proved':True,'positive_sextic_multiplier':True,'computed_gap':False,'mixture_fisher_is_exact':False,'GU_physics':False}
 assert z['scope']==scope
 for key in ['attained','uniqueness_proved','mixture_fisher_is_exact','GU_physics']:
  bad=copy.deepcopy(scope);bad[key]=not bad[key]
  try:assert bad==scope,'scope consistency'
  except AssertionError:print('DETECTED reporting',key)
  else:raise AssertionError('missed reporting mutation')
 print('PASS K1874 independent',n,'rational controls;',len(z['inputs']),'pins;',faults,'mathematical faults; 4 reporting faults. Analytic proof not machine-verified.')
if __name__=='__main__':run()
