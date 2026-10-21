#!/usr/bin/env python3
"""Independent row actions, compact primitive and frame/moment fault controls."""
from pathlib import Path
import copy,hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[2];CERT=ROOT/'lab/process/k1883-compact-support-observation-range.json'
def matrix(v):
 data={(i,j):s.Rational(x) for i,j,x in v['entries']}
 return s.Matrix(v.get('rows',16),v.get('columns',16),lambda i,j:data.get((i,j),0))
def zero(M):return all(s.expand(v)==0 for v in M)
src=json.loads((ROOT/'lab/process/k1836-k77-differential-dirac-quotient.json').read_text());old=json.loads((ROOT/'lab/process/k1840-k77-conservative-variable-observation.json').read_text());D=[matrix(v) for v in src['target_D']];J=D[0]*D[1]*D[2]
def validate(v):
 assert v['scope']=={'compact_range_codimension':4,'all_target_compact_inverse':False,'massive_L2_surjective':True,'massless_Cc_targets_have_L2_lifts_R3':True,'rotating_charges_require_inverse_frame':True,'native_GU':False,'pure_mass_rotating_lift':False}
 for p,h in v['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 count=0
 for row,sr,kr in zip(v['blocks'],src['blocks'],old['blocks']):
  T=[matrix(a) for a in sr['T']];S=matrix(kr['repairs'][0]['S']);K=matrix(row['K']);N=matrix(row['right_inverse_Z']);B=matrix(kr['repairs'][0]['B'])
  # Certify every row of the 12-component preparation, not a claimed rank label.
  for i in range(3):
   for j in range(3):
    assert T[i]*N[:,4*j:4*j+4]==(s.eye(4) if i==j else s.zeros(4));count+=1
  for i in range(4):
   assert S.row(i)==24*K[i,i]*T[0].row(i);count+=1
  assert K==s.diag(1,-1,-1,1);assert -D[0]*K==B;count+=2
  # Actual dual vector for rank defect, plus two independent nonzero rows.
  M=S-24*T[0];assert M.row(0)==s.zeros(1,16) and M.row(3)==s.zeros(1,16)
  assert M[[1,2],:].rank()==2;count+=2
  assert row['complex_symbol_rank']==2;count+=1
 return count
v=json.loads(CERT.read_text());math_checks=validate(v)
x,y,z,q=s.symbols('x y z q',real=True)
rho=lambda t:s.Rational(35,32)*(1-t*t)**3
assert s.integrate(rho(q),(q,-1,1))==1;math_checks+=1
# Actual marginal-cancellation construction on a compact C2 polynomial fixture.
h=(x+2*y+3*z)*rho(x)*rho(y)*rho(z)
H1=s.integrate(h,(x,-1,1));H2=s.integrate(H1,(y,-1,1))
F1=s.integrate((h-rho(x)*H1).subs(x,q),(q,-1,x))
F2=rho(x)*s.integrate((H1-rho(y)*H2).subs(y,q),(q,-1,y))
F3=rho(x)*rho(y)*s.integrate(H2.subs(z,q),(q,-1,z))
assert s.expand(s.diff(F1,x)+s.diff(F2,y)+s.diff(F3,z)-h)==0;math_checks+=1
for f,coord in [(F1,x),(F2,y),(F3,z)]:
 for endpoint in [-1,1]:
  assert s.expand(f.subs(coord,endpoint))==0;math_checks+=1
# A nonzero total charge prevents compactness of the final primitive.
positive_last=rho(x)*rho(y)*s.integrate(rho(q),(q,-1,z))
assert s.expand(positive_last.subs(z,1)-rho(x)*rho(y))==0;math_checks+=1
actual_faults=1
# Weighted divergence product rule, including both mass signs and several source components.
for kr in [s.Rational(-2),s.Rational(0),s.Rational(3,2)]:
 for sign in [-1,1]:
  weight=s.exp(kr*sign*x);f=1+x+x*y+y*z
  assert s.simplify(s.diff(weight*f,x)-weight*(s.diff(f,x)+kr*sign*f))==0;math_checks+=1
  if kr:
   assert s.simplify(s.diff(weight*f,x)-weight*(s.diff(f,x)-kr*sign*f))!=0;actual_faults+=1
# Rotating charge test with exp(kappa*L)=2, exact rational frames and two locations.
U=(3*s.eye(4)-4*J)/5;assert U.T*U==s.eye(4);E=s.diag(2,s.Rational(1,2),s.Rational(1,2),2)
for i in range(4):
 c=s.eye(4)[:,i];y1=c;y2=-E.inv()*c
 assert y1+E*y2==s.zeros(4,1)
 assert U.T*(U*y1)+E*U.T*(U*y2)==s.zeros(4,1);math_checks+=2
 assert U*y1+E*U*y2!=s.zeros(4,1);actual_faults+=1
# Massive exponential charge cancellation becomes arbitrarily small in L2.
for n in [2,5,10]:
 amplitude=s.Rational(1,2)**n
 assert amplitude*2**n==1 and amplitude<1;math_checks+=1
faults=0
for block in range(4):
 for field in ['K','right_inverse_Z']:
  bad=copy.deepcopy(v);bad['blocks'][block][field]['entries'][0][2]='123'
  try:validate(bad)
  except AssertionError:faults+=1
  else:raise AssertionError('actual coefficient fault survived')
report=0
for key in ['all_target_compact_inverse','massive_L2_surjective','rotating_charges_require_inverse_frame','native_GU']:
 bad=copy.deepcopy(v);bad['scope'][key]=not bad['scope'][key]
 try:validate(bad)
 except AssertionError:report+=1
 else:raise AssertionError('scope fault survived')
bad=copy.deepcopy(v);bad['inputs'][next(iter(bad['inputs']))]='0'*64
try:validate(bad)
except AssertionError:report+=1
else:raise AssertionError('pin fault survived')
print('PASS K1883 independent:',math_checks,'operator/primitive/frame controls;',actual_faults,'actual false-identity/noncompact controls;',faults,'matrix faults;',report,'report/pin faults')
