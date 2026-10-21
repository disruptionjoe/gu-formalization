#!/usr/bin/env python3
"""Independent Fraction inequalities; input faults must fail assertions."""
import copy,hashlib,json
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def check(z):
 p=z['parameters'];n=0
 def ck(v,msg):
  nonlocal n
  assert v,msg;n+=1
 ck(p['delta_open_interval']==['0','2'],'parameter interval')
 # Symbolic coefficient bounds are checked by coefficient dominance and endpoints.
 ck(p['F_upper_numerator']>=4,'trial numerator')
 ck(p['b_upper_numerator']>=4*p['F_upper_numerator'],'dual secant')
 ck(p['R']**2>=9,'tail certificate')
 ck(p['L']>p['R'],'comparison interval')
 Y=p['L']**2
 ck(p['kappa_numerator']**2>= (p['b_upper_numerator']*(Y*Y+6*Y+3)+2*p['F_upper_numerator']*(Y-2))/4,'compact Q upper bound')
 ck(p['gap_exponent_numerator']>=4*p['R']*p['kappa_numerator']+8,'gap exponential margin')
 ck(2*p['TV_exponent_numerator']>=p['gap_exponent_numerator'],'TV square root')
 ck(p['a_error_numerator']>=2*p['F_upper_numerator']+6*p['b_upper_numerator'],'a moment error')
 ck(p['b_error_numerator']>=p['b_upper_numerator'],'b moment error')
 ck(p['Sobolev_numerator']>=2*(4*p['F_upper_numerator']+18*p['b_upper_numerator']),'Sobolev coefficient')
 # Rational endpoint/vertex checks of the polynomial estimates, not continuum proof.
 for d in [Q(1,100),Q(1,8),Q(1,2),Q(1),Q(3,2),Q(199,100)]:
  k=1+d
  for y in [Q(0),k,Q(9),Q(16)]:
   ck(abs(y*y-2*k*y+k)<=355,'compact absolute polynomial')
   ck(abs(y-2)<=14,'compact linear factor')
  ck((Q(1420)+14*d)<1600,'Q kappa')
  ck((9*9-2*k*9+k)+(9-2)>=37,'tail Q')
  ck(Q(8)/d+Q(288)/d**2<=Q(304)/d**2,'form constant')
 for c in [Q(0),Q(1,3),Q(1,2),Q(99,100),Q(1)]:
  ck(2*(1-c)<=2*(1-c*c),'Hellinger spectral conversion')
 for path,h in z['inputs'].items():ck(hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==h,'dependency pin')
 expected={'all_parities':True,'balance_required':False,'fixed_delta_vanishing_deficit':True,'uniform_positive_endpoint_gap':False,'practical_tunneling_constant':False,'entropy_bound':False,'native_GU_credit':False}
 for k,v in expected.items():ck(z['claims'][k]==v,'scope '+k)
 return n
if __name__=='__main__':
 z=json.loads((ROOT/'lab/process/k1872-fisher-global-deficit-modulus.json').read_text());n=check(z);mathfaults={'F_upper_numerator':3,'b_upper_numerator':15,'R':2,'L':3,'kappa_numerator':37,'gap_exponent_numerator':479,'TV_exponent_numerator':243,'a_error_numerator':103,'b_error_numerator':15,'Sobolev_numerator':607};caught=[]
 for k,v in mathfaults.items():
  q=copy.deepcopy(z);q['parameters'][k]=v
  try:check(q)
  except AssertionError as e: caught.append(k);print('DETECTED input',k,str(e))
  else:raise AssertionError('MISSED '+k)
 for k in z['claims']:
  q=copy.deepcopy(z);q['claims'][k]=not q['claims'][k]
  try:check(q)
  except AssertionError:print('DETECTED reporting',k)
  else:raise AssertionError('MISSED reporting '+k)
 print('PASS K1872 probe',n,'controls (including dependency/scope);',len(caught),'math-input faults;',len(z['claims']),'reporting faults')
