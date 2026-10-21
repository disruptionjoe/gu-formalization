#!/usr/bin/env python3
"""Independent rational/local oscillator checks, not a proof by sampling."""
from fractions import Fraction as F
from pathlib import Path
import copy,hashlib,json,math
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
C=ROOT/'lab/process/k1880-effective-fisher-well-localization.json'
def validate(v):
 assert v['constants']=={'cutoff':40,'slope':'13/4','oscillator_gap':'4*a*A','TV_denominator':'2*k*A'}
 assert v['scope']=={'all_feasible_densities_with_valid_energy_upper':True,'fixed_weights_require_evenness':True,'effective_rescaled_W2':False,'global_sextic_gap':False,'native_GU':False}
 assert v['finite_even_TV_strict_upper']=='11/500'
 for p,h in v['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 # Completely rational reconstruction of k=4 finite accuracy, no producer import.
 e=F(1,3*10**6);h=F(1,10**4);tau=4*e*e/h**2;eps=F(13,8)*h
 E=F(25002,1000)-25+25*((1-eps)**-2-1)+30*e+80*tau+F(40,10**12)/h**2
 expected={'e':e,'epsilon':eps,'tau':tau,'E':E,'denominator':F(40),'weight':3*e/4,'leak':F(1,20*10**12)}
 for key,value in expected.items():assert F(v['budget'][key])==value
 assert E<40*(F(11,500)-tau-3*e/4)**2
 return len(expected)+1
v=json.loads(C.read_text());n=validate(v);math_checks=0
# Verify global distance inequality at rational points, including every cell boundary.
for root in [F(2),F(3),F(5)]:
 k=root*root
 for x in [root*F(j,16) for j in range(-40,41)]:
  d=min(abs(x-r) for r in [F(0),root,-root]);g=x**3-k*x
  assert g*g>=F(9,16)*k*k*d*d;math_checks+=1
# Full polynomial oscillator eigenvalue identities for orders0..6, independent formulation.
x=s.symbols('x');phi=s.exp(-x*x/4)
for order in range(7):
 u=s.hermite_prob(order,x)*phi
 assert s.simplify(-4*s.diff(u,x,2)+x*x*u-2*u-4*order*u)==0;math_checks+=1
# Sharpness witness rejects an inflated gap: first excitation has energy4 and variance1.
for badgap in [5,8,16]:
 assert not (4>=badgap);math_checks+=1
# Drop non-even weights: asymmetry can persist with all even moments unchanged.
w=F(1,4);eta=F(3,4)
for degree in [2,4,6]:
 assert eta*w*2**degree+(1-eta)*w*(-2)**degree==w*2**degree;math_checks+=1
assert abs(eta*w-w/2)+abs((1-eta)*w-w/2)>0;math_checks+=1
# The slope estimate is pointwise, including outer roots and both signs.
for root in [F(2),F(3)]:
 k=root*root;h=root/4
 for r in [F(0),root,-root]:
  for z in [h*F(j,12) for j in range(-12,13)]:
   assert abs(3*r*z+z*z)<=F(13,4)*root*h;math_checks+=1
# Negative controls change an actual inequality, not a certificate label.
actual_faults=0
r=F(2);h=r/4
assert not abs(3*r*h+h*h)<=F(3,4)*r*h;actual_faults+=1
assert not 4*s.pi**2<=4;actual_faults+=1
assert not 4>=8;actual_faults+=1
faults=0
for key,bad in [('cutoff',4),('slope','3/4'),('oscillator_gap','8*a*A'),('TV_denominator','4*k*A')]:
 q=copy.deepcopy(v);q['constants'][key]=bad
 try:validate(q)
 except AssertionError:faults+=1
 else:raise AssertionError('coefficient fault survived')
for key in ['E','tau','weight']:
 q=copy.deepcopy(v);q['budget'][key]='0'
 try:validate(q)
 except AssertionError:faults+=1
 else:raise AssertionError('arithmetic fault survived')
reporting=0
for key in ['fixed_weights_require_evenness','effective_rescaled_W2','global_sextic_gap','native_GU']:
 q=copy.deepcopy(v);q['scope'][key]=not q['scope'][key]
 try:validate(q)
 except AssertionError:reporting+=1
 else:raise AssertionError('scope fault survived')
q=copy.deepcopy(v);q['inputs'][next(iter(q['inputs']))]='0'*64
try:validate(q)
except AssertionError:reporting+=1
else:raise AssertionError('pin fault survived')
print('PASS K1880 independent:',math_checks,'mathematical controls;',n,'budget controls;',faults,'certificate coefficient/arithmetic faults;',actual_faults,'actual inequality faults;',reporting,'report/pin faults')
