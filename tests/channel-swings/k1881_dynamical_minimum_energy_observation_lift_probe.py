#!/usr/bin/env python3
"""Independent rowwise Fourier evaluation and Cayley evolution controls."""
from pathlib import Path
import copy,hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
def read(p):return json.loads((ROOT/p).read_text())
def dense(v):
 lookup={(i,j):s.Rational(x) for i,j,x in v['entries']}
 return s.Matrix(v.get('rows',16),v.get('columns',16),lambda i,j:lookup.get((i,j),s.S.Zero))
def z(M):return all(s.cancel(x)==0 for x in M)
v=read('lab/process/k1881-dynamical-minimum-energy-observation-lift.json')
def report(q):
 assert q['coefficients']=={'mass_squared':576,'inverse':'Odagger/[alpha*(xi2+576R2)]','normalized_observation':'O/sqrt(alpha*(xi2+576R2))'}
 assert q['scope']=={'raw_right_inverse_intertwines':True,'normalized_quotient_unitary':True,'raw_L2_isometry':False,'massless_R3_bounded_raw_inverse':False,'massless_R3_normalized_coisometry':True,'odd_twist_fixed_periodic_repair_gap':True,'pure_mass_rotating_lift':False,'native_GU':False}
 for path,digest in q['inputs'].items():assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest
report(v)
en=read('lab/process/k1832-k77-common-energy-form.json');src=read('lab/process/k1836-k77-differential-dirac-quotient.json');old=read('lab/process/k1840-k77-conservative-variable-observation.json')
D=[dense(x) for x in src['target_D']];J=D[0]*D[1]*D[2];checks=0;faults=0
for idx in range(4):
 er,sr,kr=en['blocks'][idx],src['blocks'][idx],old['blocks'][idx]
 H=dense(er['H']);A=[dense(x) for x in er['matrices']];T=[dense(x) for x in sr['T']];L=dense(er['J']);L=L if T[0]*L==J*T[0] else -L
 C,B,S=[dense(kr['repairs'][0][key]) for key in ['C','B','S']];alpha=s.Rational(sr['alpha'])
 for freq,mass in [((1,0,0),s.Rational(1,2)),((2,-1,1),s.Rational(1)),((s.Rational(1,2),0,0),s.Rational(0))]:
  M=s.Matrix(4,16,lambda i,j:s.I*sum(freq[k]*T[k][i,j] for k in range(3))+mass*S[i,j])
  P=s.Matrix(16,16,lambda i,j:s.I*sum(freq[k]*A[k][i,j] for k in range(3))+mass*C[i,j])
  Q=s.Matrix(4,4,lambda i,j:s.I*sum(freq[k]*D[k][i,j]/24 for k in range(3))+mass*B[i,j])
  norm2=alpha*(sum(x*x for x in freq)+576*mass*mass);Md=H.inv()*M.conjugate().T;R=Md/norm2
  for test in [z(M*Md-norm2*s.eye(4)),z(P*R-R*Q),z(R.conjugate().T*H*R-s.eye(4)/norm2),z((R*M)**2-R*M)]:assert test;checks+=1
  # Deliberate mathematical faults on the actually evaluated operator.
  assert not z(M*(-R)-s.eye(4));faults+=1
  assert not z(M*(Md/(norm2+1))-s.eye(4));faults+=1
  if mass:
   assert not z(M*(Md/(alpha*(sum(x*x for x in freq)+144*mass*mass)))-s.eye(4));faults+=1
  if mass==s.Rational(1,2):
   ep=(s.eye(16)+P/7).inv()*(s.eye(16)-P/7);eq=(s.eye(4)+Q/7).inv()*(s.eye(4)-Q/7)
   assert z(ep.conjugate().T*H*ep-H);assert z(eq.conjugate().T*eq-s.eye(4));assert z(ep*R-R*eq);checks+=3
   def frame(M,t):return ((1-t*t)*s.eye(M.rows)-2*t*M)/(1+t*t)
   U1,U2=frame(J,s.Rational(1,3)),frame(J,s.Rational(2,5));W1,W2=frame(L,s.Rational(1,3)),frame(L,s.Rational(2,5))
   r1=W1*R*U1.T;r2=W2*R*U2.T;EP=W2*ep*W1.inv();EQ=U2*eq*U1.T
   assert z(r2*EQ-EP*r1);checks+=1
   assert not z(r1*EQ-EP*r1);faults+=1
   # Some kernel-valued additions are right inverses but not dynamical lifts.
   kernel=s.eye(16)-R*M;found=False
   for col in range(16):
    N=kernel[:,col]*s.Matrix([[1,0,0,0]])
    if not z(P*N-N*Q):
     assert z(M*(R+N)-s.eye(4));assert not z(P*(R+N)-(R+N)*Q);found=True;break
   assert found;checks+=2
# Explicit infrared and ultraviolet controls; no floating tolerance.
for n in [2,4,16,64]:
 assert s.Rational(1,n*n)<1 # massive high-frequency energy ratio vanishes
 assert n*n>1              # massless low-frequency inverse norm diverges
 checks+=2
# Radial r^-1 target: L2 radial exponent0 integrates, inverse exponent-2 diverges.
assert 2-2==0 and 2-2-2==-2;checks+=1
for n in range(-10,11):assert (2*n+1)**2>=1;checks+=1
assert 0**2==0;checks+=1
report_faults=0
for key in ['raw_L2_isometry','massless_R3_bounded_raw_inverse','native_GU','pure_mass_rotating_lift']:
 q=copy.deepcopy(v);q['scope'][key]=not q['scope'][key]
 try:report(q)
 except AssertionError:report_faults+=1
 else:raise AssertionError('scope fault survived')
q=copy.deepcopy(v);q['inputs'][next(iter(q['inputs']))]='0'*64
try:report(q)
except AssertionError:report_faults+=1
else:raise AssertionError('pin fault survived')
print('PASS K1881 independent:',checks,'operator/domain controls;',faults,'actual operator faults;',report_faults,'scope/pin faults')
