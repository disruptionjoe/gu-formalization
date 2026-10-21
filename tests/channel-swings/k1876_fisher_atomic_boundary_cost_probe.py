#!/usr/bin/env python3
"""Independent rational controls and real-failure mutation checks (not a continuum proof)."""
import copy,hashlib,json,math
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]

def mathematical(c=None):
 c={'remainder_k':3,'remainder_a':5,'width_ratio':2,'jacobian':1,'slack_k':1,'cost_shift':1} if c is None else c
 n=0
 def ck(v,label):
  nonlocal n
  if not v:raise AssertionError('FAIL '+label)
  n+=1
 for k in [F(7,2),F(4),F(9)]:
  for a in [F(1,100),F(1),F(2)]:
   for x in [F(0),F(1,3),F(1),F(3),F(-2)]:
    g=x**3-k*x;h=(x*x-a)/(x*x+a);hp=4*a*x/(x*x+a)**2
    derivative=hp*g+h*(3*x*x-k);linear=k+(k-3*a)*x*x/(k+a)
    rem=2*(a*(c['remainder_a']*a+c['remainder_k']*k)+(3*a+k)*x*x)/((a+k)*(a+x*x)**2)
    ck(derivative==linear+x*g*rem,'score remainder')
    ck((h*g)**2<=g*g,'test domination')
    ck(x*x*rem*rem<=(5*a+3*k)**2/((a+k)**2*a),'uniform remainder bound')
  # IFT derivative and mixture moments independently from Gaussian moment formulas.
  yp=k-F(7,2);wp=-F(2)/k+4/(k*k)
  ck(-k*k+F(7,2)*k+c['jacobian']*k*yp==0,'root derivative')
  sixthprime=wp*k**3+3*k*yp+F(15,2)*k
  ck(sixthprime==k*(k+c['slack_k']),'slack derivative')
  ck(sixthprime*(1+1/k)==(k+c['cost_shift'])**2,'sharp coefficient')
  p0=1-1/k;p1=1/k
  for c0,c1 in [(F(2),F(1)),(F(1),F(1)),(F(3),F(2))]:
   prod=(p0/c0+p1/c1)*(p0*k*k*c0+p1*4*k*k*c1)
   ck(prod-(k+1)**2==(k-1)*(c0-c['width_ratio']*c1)**2/(c0*c1),'allocation square')
 # Use integer/rational interval arithmetic, no producer import or float tolerance.
 t=F(1,20001000000000);delta=F(1,10**12);yl=4+t/2-10*t*t;yh=4+t/2+10*t*t
 def poly(y):return 4*(1-t)*y*y+4*(3*t-4)*y+8*t-9*t*t+3*t**3
 ck(poly(yl)<0<poly(yh),'root interval');wh=(1-t)/(yl-t/2)
 mom6upper=15*t**3+wh*(yh**3+F(15,2)*yh*yh*t+F(45,4)*yh*t*t+F(15,8)*t**3)
 ck(mom6upper<16+delta,'finite cap');ck(delta*(1+wh)/t<F(12501,500),'finite upper')
 a=F(1,10000);lower=5-4*a/(4+a)-(5*a+12)/(4+a)*F(1,10000)
 ck(lower>F(9999,2000),'finite lower')
 return n

def reporting(doc):
 assert doc['coefficients']['atomic_cost']=='(k+1)^2','FAIL cost reporting'
 assert doc['finite_example']['scaled_value_lower']=='99980001/4000000','FAIL lower reporting'
 assert not doc['scope']['native_GU_verdict'],'FAIL scope'
 assert not doc['scope']['exact_optimizer_coefficients_computed'],'FAIL coefficient scope'
 for p,h in doc['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'FAIL pin'
 return 4+len(doc['inputs'])
if __name__=='__main__':
 doc=json.loads((ROOT/'lab/process/k1876-fisher-atomic-boundary-cost.json').read_text());n=mathematical();r=reporting(doc)
 base={'remainder_k':3,'remainder_a':5,'width_ratio':2,'jacobian':1,'slack_k':1,'cost_shift':1};caught=[]
 for key in base:
  bad=dict(base);bad[key]+=1
  try:mathematical(bad)
  except AssertionError as e:assert str(e).startswith('FAIL ');caught.append(key);print('DETECTED mathematical',key,str(e))
  else:raise AssertionError('FAIL undetected '+key)
 mutants=[('coefficients','atomic_cost','(k-3)^2'),('finite_example','scaled_value_lower','25'),('scope','native_GU_verdict',True),('scope','exact_optimizer_coefficients_computed',True)]
 for section,key,value in mutants:
  bad=copy.deepcopy(doc);bad[section][key]=value
  try:reporting(bad)
  except AssertionError as e:assert str(e).startswith('FAIL ');print('DETECTED reporting',key,str(e))
  else:raise AssertionError('FAIL undetected reporting')
 print('PASS K1876 probe',n,'independent rational controls;',r,'reporting/pins;',len(caught),'math faults;',len(mutants),'reporting faults')
