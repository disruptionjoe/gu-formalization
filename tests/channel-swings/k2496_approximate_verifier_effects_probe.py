"""Exact algebra, joint-memory record fixtures and contrary controls for K2496."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import sympy as s
import json,hashlib,sys
R=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ct(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
def model(r):
 n=7;Q=s.diag(1,1,0,1,1,0,0);T=s.diag(1,0,0,0,0,1,0);c=s.sqrt(r*(1-r));T[1:3,1:3]=s.Matrix([[r,c],[c,1-r]])
 P=s.diag(1,0,0,0,0,0,0);Z=s.diag(0,1,0,0,0,0,0);Y=s.diag(0,0,1,0,0,0,0);U=s.zeros(n);U[1,2]=1
 return Q,T,P,Z,Y,U
def swap(n,a,b):
 V=s.eye(n);V[a,a]=V[b,b]=0;V[a,b]=V[b,a]=1;return V
for r in [s.Rational(27,127),s.Rational(15,67)]:
 Q,T,P,Z,Y,U=model(r);d=1-r;c=s.sqrt(r*d);tag=str(r);simp=lambda A:A.applyfunc(s.simplify)
 ck('projection_'+tag,Q*Q==Q and simp(T*T-T)==s.zeros(7))
 ck('P_polynomial_'+tag,simp((Q*T*Q*T*Q-r*Q*T*Q)/d-P)==s.zeros(7))
 ck('Z_polynomial_'+tag,simp((Q*T*Q-Q*T*Q*T*Q)/(r*d)-Z)==s.zeros(7))
 ck('Y_polynomial_'+tag,simp((T*Q*T-Q*T*Q*T-T*Q*T*Q+Q*T*Q*T*Q)/(r*d)-Y)==s.zeros(7))
 ck('U_polynomial_'+tag,simp((Q*T-Q*T*Q)/c-U)==s.zeros(7))
 ck('parameter_bounds_'+tag,s.Rational(1,5)<=r<=s.Rational(1,4) and r*d>=s.Rational(4,25))
 ck('target_constant_'+tag,(15+6*r)/d<=22)
 p,a,b,n,x,y,z,zb=s.symbols('p a b n x y z zb');I=s.eye(7)
 expected=s.diag(p,x,y,a,a,b,n);expected[1,2]=z;expected[2,1]=zb
 expanded=n*I+(a-n)*Q+(b-n)*T+(p-a-b+n)*P+(x-a-r*(b-n))*Z+(y-n-d*(b-n))*Y+(z-c*(b-n))*U+(zb-c*(b-n))*U.T
 ck('algebra_expansion_'+tag,simp(expanded-expected)==s.zeros(7))
ck('universal_constant',F(2)+44+F(5,4)*F(525,4)+F(1025,4)+45==F(8181,16)<512)
ck('word_recurrence',all(L*(L+1)//2+(L+1)==(L+1)*(L+2)//2 for L in range(1,12)))
# Rational angle fixture separate from original-r algebra identities.
Q,T,P,Z,Y,U=model(s.Rational(9,25));I=s.eye(7);eta=s.Rational(1,100000);V=swap(7,3,5)
def phi(A):return (1-eta)*A+eta*V.T*A*V
def delta(A):return phi(A)-A
for j,B in enumerate([Q,T]):
 comm=V*B-B*V
 ck('projection_defect_identity_'+str(j),eta*comm.T*comm==delta(B)-delta(B)*B-B*delta(B))
for i,A in enumerate([Q,T,Q*T,T*Q,Q*T*Q]):
 for j,B in enumerate([Q,T,Q*T]):
  cross=eta*(V.T*A-A*V.T)*(B*V-V*B)
  ck('word_product_identity_'+str((i,j)),delta(A*B)==delta(A)*B+A*delta(B)+cross)
# All length<=4 Q/T words, exact positive-semidefinite bound on E*E.
for L in range(1,5):
 for bits in product([0,1],repeat=L):
  A=I
  for bit in bits:A=A*[Q,T][bit]
  E=delta(A);bound=s.Rational(L*(L+1),2)*eta
  ck('word_bound_'+''.join(map(str,bits)),(bound*bound*I-E.T*E).is_positive_semidefinite)
# Noncommuting-plane perturbation, with exact positive-semidefinite norm checks.
Vp=s.eye(7);Vp[1:3,1:3]=s.Matrix([[s.Rational(3,5),s.Rational(4,5)],[-s.Rational(4,5),s.Rational(3,5)]])
for L in range(1,5):
 for bits in product([0,1],repeat=L):
  A=I
  for bit in bits:A=A*[Q,T][bit]
  E=eta*(Vp.T*A*Vp-A);bound=s.Rational(L*(L+1),2)*eta
  ck('noncommuting_plane_word_'+''.join(map(str,bits)),(bound*bound*I-E.T*E).is_positive_semidefinite)
ct('plane_channel_is_not_transparent',Vp*Q!=Q*Vp and Vp*T!=T*Vp)
ct('only_target_calibration_fails',V*P==P*V and (V.T*Q*V)[3,3]==0 and Q[3,3]==1)
ct('maxmixed_calibration_fails',s.trace(V.T*Q*V)==s.trace(Q) and V.T*Q*V!=Q)
ct('linear_order_record',(Q-phi(Q))[3,3]==eta)
# A P/A swap pumps target with exactly epsilon effect error; no exact nonpumping transfer.
VP=swap(7,0,3);dQ=eta*(VP.T*Q*VP-Q);dT=eta*(VP.T*T*VP-T);dP=eta*(VP.T*P*VP-P)
ct('approximate_transparency_can_pump',dQ==s.zeros(7) and dT[0,0]==-eta and dP[3,3]==eta)
VA=swap(7,3,4)
ct('full_state_not_preserved',VA*Q==Q*VA and VA*T==T*VA and VA[4,3]==1 and VA[3,3]==0)
# Exact rare-event postselection under A/B swapping, not a changed manifest assertion.
F0=eta**2;rho=F0*P;rho[3,3]=1-F0
out=T*((1-eta)*(Q*rho*Q)+eta*V*(Q*rho*Q)*V.T)*T
sacc=s.trace(out);bad=s.trace((I-P)*out)
ck('rare_event_actual_acceptance',sacc==F0+(1-F0)*eta and bad==(1-F0)*eta)
ct('rare_event_near_one',bad/sacc>s.Rational(999,1000))
# Retained two-level memory; conditional bad swap plus memory flip. Untouched reference separate.
I2=s.eye(2);J=s.eye(14);q=s.kronecker_product(Q,I2);t=s.kronecker_product(T,I2);p=s.kronecker_product(P,I2)
W=s.kronecker_product(I,s.diag(1,0))+s.kronecker_product(V,s.diag(0,1));X=s.kronecker_product(I,s.Matrix([[0,1],[1,0]]));W=X*W
ck('joint_map_unitary',W.T*W==J)
for j,Test in enumerate([q,t]):
 E=W.T*Test*W-Test
 ck('joint_effect_norm_'+str(j),E.is_diagonal() and max(abs(x) for x in E)==1)
qR=s.kronecker_product(q,I2);tR=s.kronecker_product(t,I2);pR=s.kronecker_product(p,I2);WR=s.kronecker_product(W,I2);IR=s.eye(28)
v=s.zeros(28,1)
for idx in [0,3,13,20]:v[idx]=s.Rational(1,2)
ck('joint_reference_fixture_normalized',(v.T*v)[0]==1)
refs=[s.diag(1,0),s.Matrix([[1,1],[1,1]])/2]
actual_mass={};ideal_mass={};different=False
for bits in product([0,1],repeat=3):
 a=v*v.T;bmat=a
 for j,(Test,bit) in enumerate(zip([qR,tR,qR],bits)):
  K=Test if bit==0 else IR-Test;a=K*a*K;bmat=K*bmat*K
  if j<2:bmat=(1-eta)*bmat+eta*WR*bmat*WR.T
 for target in [0,1]:
  E=pR if target==0 else IR-pR
  key=''.join(map(str,bits))+str(target);aa=s.trace(E*a);bb=s.trace(E*bmat)
  actual_mass[key]=bb;ideal_mass[key]=aa;different=different or aa!=bb
  ck('record_event_'+key,abs(aa-bb)<=1024*eta)
  for ri,rf in enumerate(refs):
   Er=E*s.kronecker_product(J,rf)
   ck('record_reference_effect_'+key+str(ri),abs(s.trace(Er*(a-bmat)))<=1024*eta)
ck('record_masses_normalized',sum(actual_mass.values())==sum(ideal_mass.values())==1)
ck('record_actual_difference_nonzero',different)
ck('whole_record_TV_bound',sum(abs(actual_mass[k]-ideal_mass[k]) for k in actual_mass)/2<=1024*eta)
s0=F(1,1000);b0=F(1,1000000);tau=F(1,50);ep=(tau*s0-b0)/(1024*(1+tau));E=F(1024,100000000)
ck('calibration_threshold',ep==F(19,1044480000))
ck('illustrative_budget',E==F(8,781250) and (b0+E)/(s0-E)<tau)
ct('postselection_requires_margin',s0-F(1,100)<=0)
ct('raw_error_is_not_conditioned_error',(b0+E)/(s0-E)>b0+E)
# An actual two-attempt fresh geometric renewal equation, with within-attempt correlation.
sp=F(1,4);cost_success=F(2);cost_fail=F(5);Acost=sp*cost_success+(1-sp)*cost_fail
renewal=Acost/sp
ck('renewal_equation',renewal==Acost+(1-sp)*renewal)
ct('conditional_success_price_is_not_renewal',renewal!=cost_success/sp)
deps=['explorations/conditional-build/k2494-memory-transparent-storage-2026-11-02.md']
report={'result':'K2496','checks':checks,'contrary_controls':controls,'bounds':{'algebra_constant':'512','target_constant':'22','word_constant':'L*(L+1)/2','record_error':'min(1,512*sum(epsilon_j))','example_epsilon_max':str(ep),'rare_event_conditional_bad':str(bad/sacc)},'evidence_kinds':{'universal':'written Stinespring identity, finite-algebra coefficient estimate and reverse hybrid','exact':'original-r algebra and rational retained-memory/reference finite records','not_claimed':'full output-state preservation, calibrated hardware, infinite cap, GU quotient or novelty'},'dependencies':{f:hashlib.sha256((R/f).read_bytes()).hexdigest() for f in deps}}
pth=R/'lab/process/k2496-approximate-verifier-effects.json'
if '--write' in sys.argv:pth.write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
else:ck('saved_reproduction',json.loads(pth.read_text())==report)
print(json.dumps({'result':'PASS','checks':len(checks),'controls':len(controls),'bounds':report['bounds']}))
