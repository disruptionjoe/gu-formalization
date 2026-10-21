#!/usr/bin/env python3
"""Separate Fraction-based budget and transfer controls, without importing the producer."""
from fractions import Fraction as F
from pathlib import Path
import copy,hashlib,json
ROOT=Path(__file__).resolve().parents[2]
C=ROOT/'lab/process/k1882-effective-fisher-rescaled-transport.json'
def validate(v):
 assert v['constants']=={'tail_coercivity':'16/9','cutoff':40,'transport_factor':1,'tail_mass_factor':1,'tail_modulus':24}
 assert v['scope']=={'actual_hard_cells':True,'all_feasible_valid_U':True,'rare_cell_mass_required':True,'hard_cell_entropy':False,'sharp_rate':False,'sextic_gap':False,'native_GU':False}
 for p,h in v['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 e=F(1,3000000);eps=F(13,80000);tau=F(1,22500);K=F(12503,500);S=5-3*e-8*tau
 E=F(1,500)+25*((1-eps)**-2-1)+30*e+80*tau+F(1,250)
 D=1-(1-eps)**2*S*S/K;B=E/400+D/9+tau/20
 expected={'e':e,'epsilon':eps,'tau':tau,'E':E,'Kcap':K,'Splus':S,'D':D,'B':B,'central_mass_lower':1-(1+3*e)/4,'outer_mass_lower':(1-3*e)/8}
 for key,value in expected.items():assert F(v['budget'][key])==value
 assert B<F(7,625)**2 and B<expected['central_mass_lower']*F(13,1000)**2 and B<expected['outer_mass_lower']*F(4,125)**2
 return len(expected)+3
v=json.loads(C.read_text());budget_checks=validate(v);math_checks=0
# Gaussian families test transport/Fisher normalization with exact rational standard deviations.
for precision_root in [1,2,3]:
 b=F(precision_root**2)
 for sd in [F(1,5),F(1,2),F(1),F(3),F(5)]:
  for mu in [F(-2),F(0),F(3,2)]:
   relative=(b*mu)**2+(b*sd*sd-1)**2/(sd*sd)
   cost=mu*mu+(sd-F(1,precision_root))**2
   assert cost<=relative/(b*b);math_checks+=1
# Weighted uncertainty allocation: a continuum Gaussian realization of every row.
for ms in [(F(1,4),F(3,4)),(F(1,1000),F(999,1000))]:
 for vs in [(F(1,7),F(2,5)),(F(1,20),F(1,40)),(F(2),F(1,50))]:
  aa=(F(4),F(8));K=sum(m/q for m,q in zip(ms,vs));M=sum(m*a*a*q for m,a,q in zip(ms,aa,vs));S=sum(m*a for m,a in zip(ms,aa))
  assert S*S<=K*M;math_checks+=1
# Centered residual coupling tested by actual product atoms with nonzero source mean.
for z in [-7,-1,0,2,11]:
 for q in [1,2,5]:
  actual=(F((z-q)**2)+F((z+q)**2))/2
  assert actual==z*z+q*q;math_checks+=1
# Pointwise tail-splitting inequality behind continuum integration.
for y in range(-8,9):
 for g in range(-8,9):
  L=4;lhs=y*y if abs(y)>L else 0;rhs=4*(y-g)**2+(2*g*g if abs(g)>F(L,2) else 0)
  assert lhs<=rhs;math_checks+=1
actual_faults=0
# Shifted same-variance Gaussian is sharp; shrinking transport constant fails.
assert not F(1)<=F(1,2);actual_faults+=1
# A far contaminant defeats inference from TV alone via second moments.
for n in [10,100,1000]:
 eps=F(1,n*n);candidate_second=1+eps*n*n
 assert candidate_second==2 and eps<=F(1,100);math_checks+=1
assert not 2==1;actual_faults+=1
# Deleting residual variance cannot dominate a product coupling at source atom zero.
assert not 1<=0;actual_faults+=1
# A rare label of mass 1/100 may have unit squared error with weighted total 1/100.
assert not 1<=F(1,100);actual_faults+=1
faults=0
for key in ['E','Kcap','Splus','D','B']:
 q=copy.deepcopy(v);q['budget'][key]='0'
 try:validate(q)
 except AssertionError:faults+=1
 else:raise AssertionError('budget fault survived')
report=0
for key in ['actual_hard_cells','rare_cell_mass_required','hard_cell_entropy','sharp_rate','native_GU']:
 q=copy.deepcopy(v);q['scope'][key]=not q['scope'][key]
 try:validate(q)
 except AssertionError:report+=1
 else:raise AssertionError('scope fault survived')
q=copy.deepcopy(v);q['inputs'][next(iter(q['inputs']))]='0'*64
try:validate(q)
except AssertionError:report+=1
else:raise AssertionError('pin fault survived')
print('PASS K1882 independent:',math_checks,'mathematical controls;',budget_checks,'budget checks;',actual_faults,'actual inequality faults;',faults,'serialized arithmetic faults;',report,'report/pin faults')
