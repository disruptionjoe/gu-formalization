"""Exact finite controls for full-memory transparency; universal proofs in paired note."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import sympy as s
import json,hashlib,sys
R=Path(__file__).resolve().parents[2]; checks={}; controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v: raise AssertionError(k)
def ct(k,v):
 controls[k]=bool(v)
 if not v: raise AssertionError(k)
# Original carrier multiplicities, and noncommuting original plane angles.
ck('original_dimension',1+2+8+10+87==108)
ck('test_ranks',1+1+8==10 and 1+1+10==12)
ck('commutant_dimension',1+1+8**2+10**2+87**2==7735)
ck('algebra_dimension',1+4+1+1+1==8)
Qp=s.diag(1,0);I2=s.eye(2)
for r in [s.Rational(27,127),s.Rational(15,67)]:
 z=s.sqrt(r*(1-r));Tp=s.Matrix([[r,z],[z,1-r]])
 ck('projection_'+str(r),s.simplify(Tp*Tp-Tp)==s.zeros(2))
 ck('noncommuting_'+str(r),Qp*Tp!=Tp*Qp)
 x,y=s.symbols('x y');comm=s.diag(x,y)*Tp-Tp*s.diag(x,y)
 ck('scalar_commutant_'+str(r),s.simplify(comm[0,1]-(x-y)*z)==0)
 V=s.Matrix([[s.sqrt(r),s.sqrt(1-r)],[-s.sqrt(1-r),s.sqrt(r)]])
 ck('clock_rotation_'+str(r),s.simplify(V*V.T)==I2 and s.simplify(V*s.Matrix([s.sqrt(r),s.sqrt(1-r)]))==s.Matrix([1,0]))
 ck('three_test_clock_'+str(r),s.simplify((Qp*V*Tp*Qp).T*(Qp*V*Tp*Qp))==r*Qp and s.simplify((Qp*Tp*Qp).T*(Qp*Tp*Qp))==r*r*Qp)
# Exact rational-angle fixture with multiplicities A2/B2/N1, dimension8.
# Joint retained two-level memory, not a memoryless averaged channel.
n=8;Q=s.diag(1,1,0,1,1,0,0,0);T=s.diag(1,0,0,0,0,1,1,0)
T[1:3,1:3]=s.Matrix([[s.Rational(9,25),s.Rational(12,25)],[s.Rational(12,25),s.Rational(16,25)]])
P=s.diag(1,0,0,0,0,0,0,0);I=s.eye(n);J=s.eye(2*n)
q=s.kronecker_product(Q,I2);t=s.kronecker_product(T,I2);p=s.kronecker_product(P,I2)
# Memory-controlled within-A swap; arbitrary memory flip used between gaps.
U=s.zeros(2*n)
for i in range(n):
 for m in range(2):
  j=7-i if m==1 and i in (3,4) else i
  U[2*j+m,2*i+m]=1
X=s.kronecker_product(I,s.Matrix([[0,1],[1,0]]));Us=[U,X,U]
for k,u in enumerate(Us):ck('joint_unitary_'+str(k),u.T*u==J and u*q==q*u and u*t==t*u)
# Add an untouched reference, distinct from the evolving storage memory.
qR=s.kronecker_product(q,I2);tR=s.kronecker_product(t,I2);pR=s.kronecker_product(p,I2);IR=s.eye(4*n)
UR=[s.kronecker_product(u,I2) for u in Us]
ref0=s.kronecker_product(J,s.diag(1,0));refX=s.kronecker_product(J,s.Matrix([[0,1],[1,0]]))
v=s.zeros(4*n,1)
for i in [0,1,3,4,7,12,15,20,23]:v[i]=s.Rational(1,3)
ck('entangled_fixture_normalized',(v.T*v)[0]==1)
changed=False
nonzero_reference=False
for bits in product([0,1],repeat=4):
 a=v;b=v
 for j,(test,bit) in enumerate(zip([qR,tR,qR,tR],bits)):
  z=test if bit==0 else IR-test;a=z*a;b=z*b
  if j<3:b=UR[j]*b
  key=''.join(map(str,bits))+':'+str(j)
  ck('prefix_probability_'+key,(a.T*a)[0]==(b.T*b)[0])
  ck('prefix_target_'+key,(a.T*pR*a)[0]==(b.T*pR*b)[0])
  ck('prefix_target_reference_'+key,(a.T*pR*ref0*a)[0]==(b.T*pR*ref0*b)[0])
  ck('prefix_reference_coherence_'+key,(a.T*refX*a)[0]==(b.T*refX*b)[0])
  changed=changed or a!=b
  nonzero_reference=nonzero_reference or (a.T*refX*a)[0]!=0
ck('storage_does_not_cancel',Us[2]*Us[1]*Us[0]!=J)
ck('actual_joint_state_changes',changed)
ck('reference_coherence_nonzero',nonzero_reference)
# Nonunitary commutant channel: full sector dephasing is TP and commutes.
sectors=[s.diag(*[int(i in ids) for i in range(n)]) for ids in [[0],[1,2],[3,4],[5,6],[7]]]
ck('sector_dephasing_tp',sum(sectors,s.zeros(n))==I)
ck('sector_dephasing_commutes',all(k*Q==Q*k and k*T==T*k for k in sectors))
# Explicit necessity identity for an arbitrary noncommuting Kraus unitary.
V=s.eye(n);V[3,3]=V[5,5]=0;V[3,5]=V[5,3]=1
for test in [Q,T]:
 A=V.T*test*V;comm=V*test-test*V
 ck('necessity_identity_'+str(test==Q),comm.T*comm==A-test*A-A*test+test)
ct('target_fixing_swap_is_not_transparent',V*P==P*V and V*Q!=Q*V)
ct('covariant_bad_mixing_changes_QT',F((1+1+10)-1,108-1)==F(11,107) and F(11,107)!=0)
# Apply covariant mixing to A in reduced fixture: T has rank4, P rank1.
A=s.zeros(n);A[3,3]=1;mixed=(I-P)/7
ct('covariance_fixture_actual',s.trace(T*A*T)==0 and s.trace(T*mixed*T)==s.Rational(3,7) and s.trace(P*mixed)==0)
# Isolated clock reset is identity, but reused clock maps a T vector to z.
r=s.Rational(9,25);V=s.eye(n);V[1:3,1:3]=s.Matrix([[s.Rational(3,5),s.Rational(4,5)],[-s.Rational(4,5),s.Rational(3,5)]])
W=s.kronecker_product(I,s.Matrix([[0,0],[1,0]]))+s.kronecker_product(V,s.Matrix([[0,1],[0,0]]))
ck('clock_unitary',W.T*W==J)
for i in range(n):
 u=s.zeros(2*n,1);u[2*i]=1;vv=s.zeros(2*n,1);vv[2*i+1]=1
 ck('isolated_clock_identity_'+str(i),W*u==vv)
z=s.zeros(2*n,1);z[2]=1;actual=q*W*t*W*q*z;ideal=q*t*q*z
ct('retained_clock_changes_law',(actual.T*actual)[0]==r and (ideal.T*ideal)[0]==r*r)
ct('clock_fails_joint_condition',W*q!=q*W or W*t!=t*W)
flag_good=s.zeros(2*n,1);flag_good[0]=1
accepted=s.kronecker_product(Q,s.diag(1,0))+s.kronecker_product(I-Q,s.diag(0,1))
ct('memory_flag_flip_changes_acceptance',(flag_good.T*accepted*flag_good)[0]==1 and (flag_good.T*X.T*accepted*X*flag_good)[0]==0)
# Event-level robust arithmetic and rare-postselection denominator.
s0=F(1,1000);b0=F(1,1000000);e=F(1,100000)
bound=(b0+e)/(s0-e)
ck('rare_event_bound',bound==F(1,90))
ct('unnormalized_error_is_not_conditional',bound>b0+e)
ct('vacuous_when_error_exceeds_acceptance',s0-F(1,100)<=0)
# Maximize over feasible rational accepted/bad perturbations in a bounded control grid.
for ds in [-e,0,e]:
 for db in [-e,0,e]:
  if 0<=b0+db<=s0+ds:ck('event_bound_'+str(ds)+'_'+str(db),(b0+db)/(s0+ds)<=bound)
# Prefix charges, with gap1 error=1/100, gap2=1/200.
E=[F(0),F(0),F(1,100),F(3,200)];c=[F(2),F(3),F(5)];d=[F(7),F(11)]
D=sum(c[j-1]*E[j-1] for j in range(1,4))+sum(d[j-1]*E[j] for j in range(1,3))
ck('prefix_cost_error',D==F(4,25))
ct('charging_last_gap_before_error_matters',D!=sum(c)*E[3]+sum(d)*E[3])
deps=['explorations/conditional-build/k2488-markov-flag-filtering-2026-11-02.md','explorations/conditional-build/k2492-target-preserving-storage-2026-11-02.md']
report={'result':'K2494','checks':checks,'contrary_controls':controls,'commutant_dimension':7735,'rare_event_bound':str(bound),'dependencies':{f:hashlib.sha256((R/f).read_bytes()).hexdigest() for f in deps},'evidence_kinds':{'universal':'written positive-sum converse, wordwise Kraus commutation, block algebra and CPTP telescoping','finite':'rational-angle memory fixture; symbolic original-r plane controls; exact event/cost arithmetic','not_claimed':'hardware, native positive quotient, unconstrained flag memory, asymptotic stability at fixed noise'}}
p=R/'lab/process/k2494-memory-transparent-storage.json'
if '--write' in sys.argv:p.write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
else:ck('saved_reproduction',json.loads(p.read_text())==report)
print(json.dumps({'result':'PASS','checks':len(checks),'controls':len(controls)}))
