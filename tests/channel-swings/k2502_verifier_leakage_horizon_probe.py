"""Exact channels and finite certified record/reference controls for K2502."""
from pathlib import Path
from fractions import Fraction as F
import sympy as s
import json,hashlib,sys
from flint import arb,ctx
ctx.prec=160
ROOT=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ct(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
def zero(M):return all(s.simplify(v)==0 for v in M)
def simp(M):return M.applyfunc(s.expand)
def ball(x):
 x=s.cancel(x)
 if x.is_Rational:return arb(int(x.p))/int(x.q)
 if x.is_Add:return sum((ball(t) for t in x.args),arb(0))
 if x.is_Mul:
  v=arb(1)
  for t in x.args:v*=ball(t)
  return v
 if x.is_Pow and x.exp==s.Rational(1,2):return ball(x.base).sqrt()
 raise ValueError(str(x))
def rot(t):return (1-t*t)/(1+t*t),2*t/(1+t*t)
I=s.eye(2);O=s.zeros(2);Q=s.diag(1,0);T=s.Matrix([[27,30*s.sqrt(3)],[30*s.sqrt(3),100]])/127
ck('original_plane_T_projector',zero(T*T-T));ck('original_plane_noncommuting',not zero(Q*T-T*Q))
S=s.diag(1,1,0,0);Q4=s.diag(Q,Q);T4=s.diag(T,T)
# Memory block ordering E,H. These isometries have nontransparent outside action.
for t,W in [(s.Rational(1,10),s.Matrix([[0,1],[1,0]])),(s.Rational(1,12),s.diag(1,-1))]:
 c,v=rot(t);U=s.BlockMatrix([[c*I,-v*W],[v*I,c*W]]).as_explicit();B=s.Matrix.vstack(I,O)
 ck('unitary_'+str(t),zero(U.H*U-s.eye(4)))
 for name,R in [('Q',Q4),('T',T4)]:
  ck('supported_effect_'+name+str(t),zero(S*(U.H*R*U-R)*S))
  ck('supported_intertwiner_'+name+str(t),zero((R*U-U*R)*S))
 C=B.H*U[:,2:];H=B.H*U[:,:2]
 ck('polar_H_'+str(t),zero(H-c*I));ck('polar_cross_row_'+str(t),zero(C*C.H-v*v*I))
 ct('global_transparency_not_implied_'+str(t),not zero(U.H*Q4*U-Q4) or not zero(U.H*T4*U-T4))
# Original A/B sectors: Q=diag(1,0), T=diag(0,1), target bit0.
# Coherent rotation accumulation followed by outside-controlled A/B swap.
rotation_cert=[]
for tf in [F(1,20),F(1,50),F(1,100)]:
 cc,vv=rot(tf);R2=[[cc,-vv],[vv,cc]]
 for N in [1,2,3,8]:
  x,y=F(1),F(0)
  for j in range(N):x,y=cc*x-vv*y,vv*x+cc*y
  ell=vv*vv;E=y*y;refined=N*N*ell+N*(1-cc)**2
  ck('rotation_norm_'+str((tf,N)),x*x+y*y==1)
  ck('coherent_bound_'+str((tf,N)),E<=refined)
  ck('coarse_bound_'+str((tf,N)),E<=(N+1)*N*ell)
  if N>1:ct('linear_dephased_extension_fails_'+str((tf,N)),E>N*ell)
  rotation_cert.append({'t':str(tf),'N':N,'E':str(E),'total_leakage':str(N*ell),'refined_bound':str(refined)})
theta=s.symbols('theta',real=True)
for N in [1,2,3,8]:ck('weak_lower_limit_'+str(N),s.limit(s.sin(N*theta)**2/(N*s.sin(theta)**2),theta,0)==N)
# Whole recorded instrument with noncommuting ORIGINAL plane, entangled reference,
# two unequal cross-row-saturating maps and a nontransparent final outside map.
U=[];cs=[];vs=[]
for t,W in [(s.Rational(1,10),s.Matrix([[0,1],[1,0]])),(s.Rational(1,12),s.diag(1,-1))]:
 c,v=rot(t);cs.append(c);vs.append(v);U.append(s.BlockMatrix([[c*I,-v*W],[v*I,c*W]]).as_explicit())
U.append(s.diag(I,s.Matrix([[0,1],[1,0]])))
phi=s.Matrix([1,0,0,1,0,0,0,0])/s.sqrt(2);rho=phi*phi.H
IR=s.eye(2);I8=s.eye(8)
def instrument(storage):
 branches={():rho}
 for j in range(4):
  nextb={}
  for hist,rr in branches.items():
   if j:rr=simp(s.kronecker_product(storage[j-1],IR)*rr*s.kronecker_product(storage[j-1].H,IR))
   R=T if j==0 or (j==2 and hist[0]==1) else Q
   P=s.kronecker_product(s.eye(2),R,IR)
   for bit,K in [(1,P),(0,I8-P)]:nextb[hist+(bit,)]=simp(K*rr*K)
  branches=nextb
 # trace E/H, retain untouched reference in each complete history.
 return {h:s.Matrix(2,2,lambda a,b:sum(rr[2*k+a,2*k+b] for k in range(4))) for h,rr in branches.items()}
a=instrument(U);b=instrument([s.eye(4)]*3)
ck('complete_trace_actual',s.simplify(sum(s.trace(v) for v in a.values()))==1)
ck('complete_trace_ideal',s.simplify(sum(s.trace(v) for v in b.values()))==1)
Eball=arb(0);nonzero=0
for h in a:
 delta=simp(a[h]-b[h]);ck('reference_block_hermitian_'+str(h),zero(delta-delta.H))
 det=s.simplify(delta.det());tr=s.simplify(s.trace(delta))
 norm=s.sqrt(s.simplify((delta[0,0]-delta[1,1])**2+4*delta[0,1]*delta[1,0])) if det<0 else abs(tr)
 Eball+=ball(norm)/2
 nonzero+=not zero(delta)
refined=2*sum(1-c for c in cs)+2*vs[0]*vs[1]
ck('actual_complete_reference_bound',Eball.upper()<ball(refined).lower())
ck('actual_record_nontrivial',nonzero>0 and Eball.lower()>0)
# Reference is not reset: all instrument branches together retain original marginal.
ck('reference_marginal_unchanged',zero(sum(a.values(),s.zeros(2))-I/2))
# Exact dephased channel: memory rotation then support-block dephasing.
cc,vv=rot(s.Rational(1,5));Rmem=s.Matrix([[cc,-vv],[vv,cc]]);Um=s.kronecker_product(Rmem,I)
K0=S*Um;K1=(s.eye(4)-S)*Um
ck('dephased_CPTP',zero(K0.H*K0+K1.H*K1-s.eye(4)))
psi=s.Matrix([1,0,0,1])/s.sqrt(2);rh=s.kronecker_product(s.diag(1,0),psi*psi.H)
sigma=simp(s.kronecker_product(K0,IR)*rh*s.kronecker_product(K0.H,IR)+s.kronecker_product(K1,IR)*rh*s.kronecker_product(K1.H,IR))
S8=s.kronecker_product(S,IR);ck('dephased_supported_blocks',zero(S8*sigma*(I8-S8)))
reset=s.zeros(8)
for eh in range(2):
 for eh2 in range(2):
  for rr in range(2):
   for rr2 in range(2):reset[2*eh+rr,2*eh2+rr2]=sum(sigma[4*e+2*eh+rr,4*e+2*eh2+rr2] for e in range(2))
for Robs in [Q,T]:
 Rp=s.kronecker_product(s.eye(2),Robs,IR)
 ck('memory_reset_preserves_system_effect_'+str(Robs[0,0]),s.simplify(s.trace(Rp*(reset-sigma)))==0)
ck('memory_reset_preserves_reference_entanglement',zero(reset-rh))
# Outside and replacement blocks each have trace ell, so exact half norm is ell.
ck('dephased_repair_leakage',s.simplify(s.trace((I8-S8)*sigma)-vv*vv)==0)
# Original A/B, dephased leakage then controlled swap: final error ell exactly.
v0=s.Matrix([1,0,0,0]);rr=v0*v0.H;out=K0*rr*K0.H+K1*rr*K1.H;swap=s.diag(I,s.Matrix([[0,1],[1,0]]));out=swap*out*swap.H
ck('dephased_sharp_error',s.simplify(s.trace((s.eye(4)-Q4)*out)-vv*vv)==0)
# Contrary state-level output has sqrt leakage even though last-gap record error0.
pure=Um*(v0*v0.H)*Um.H;defect=pure-v0*v0.H
# Its nonzero2x2 block has eigenvalues +/-vv, while Q on A is unchanged.
ct('full_state_not_record_error',s.simplify(defect.extract([0,2],[0,2]).det()+vv*vv)==0 and s.trace(Q4*pure)==1 and vv>vv*vv)
ct('coherent_output_not_dephased',not zero(S*Um*(v0*v0.H)*Um.H*(s.eye(4)-S)))
# Nonzero epsilon consumer and exact-error scope.
for m in [2,3,10]:
 Delta=F(1,100);eps=Delta/(1024*m);ell=Delta/(2*(m-1))
 ck('calibration_allocation_'+str(m),(m-1)*ell+512*m*eps==Delta)
# Positive-error Bernoulli process still produces all-zero counts with positive probability.
error=F(1,1000);shots=100
ct('finite_zero_counts_not_exact',(1-error)**shots>F(9,10) and error>0)
# Original full test algebra: exact amplified-intertwiner projection fixtures.
def generic_projection_checks():
 Q6=s.diag(1,1,0,1,0,0);T6=s.diag(s.ones(1),T,s.zeros(1),s.ones(1),s.zeros(1))
 def unit(i,j):
  X=s.zeros(6);X[i,j]=1;return X
 PP,ZZ,YY,UU,AA,BB,NN=unit(0,0),unit(1,1),unit(2,2),unit(1,2),unit(3,3),unit(4,4),unit(5,5)
 rr=s.Rational(27,127);dd=1-rr;cc=s.sqrt(rr*dd)
 ck('generic_P_polynomial',zero((Q6*T6*Q6*T6*Q6-rr*Q6*T6*Q6)/dd-PP))
 ck('generic_Z_polynomial',zero((Q6*T6*Q6-Q6*T6*Q6*T6*Q6)/(rr*dd)-ZZ))
 ck('generic_Y_polynomial',zero((T6*Q6*T6-Q6*T6*Q6*T6-T6*Q6*T6*Q6+Q6*T6*Q6*T6*Q6)/(rr*dd)-YY))
 ck('generic_U_polynomial',zero((Q6*T6-Q6*T6*Q6)/cc-UU))
 units=[(PP,1),(AA,1),(BB,1),(NN,1),(ZZ,s.Rational(1,2)),(YY,s.Rational(1,2)),(UU,s.Rational(1,2)),(UU.H,s.Rational(1,2))]
 def pi(X):return sum((w*e*X*e.H for e,w in units),s.zeros(6))
 ck('projection_row_identity',zero(sum((w*e*e.H for e,w in units),s.zeros(6))-s.eye(6)))
 ck('projection_column_identity',zero(sum((w*e.H*e for e,w in units),s.zeros(6))-s.eye(6)))
 X=s.Matrix(6,6,lambda i,j:7*i+3*j+int(i==j));Y=pi(X)
 ck('projection_idempotent',zero(pi(Y)-Y))
 ck('projection_intertwines_Q',zero(Q6*Y-Y*Q6));ck('projection_intertwines_T',zero(T6*Y-Y*T6))
 W=s.diag(2,3,3,5,7,11)
 ck('projection_bimodule',zero(pi(W.H*X)-W.H*pi(X)))
 constants=[F(23,3),F(176,3),F(341,3),F(330),F(50,2),F(100,2),F(25,4),F(25,4)]
 ck('projection_constant_600',sum(constants)==F(1195,2) and sum(constants)<600)
 # Actual coherent unitary, not an assumed stochastic transparent mixture.
 c,v=rot(s.Rational(1,10**12));V=s.eye(6);V[0,0]=V[3,3]=c;V[0,3]=-v;V[3,0]=v
 ck('generic_unitary',zero(V.H*V-s.eye(6)))
 W=pi(V);D=V-W;A0=W.H*W;Z0=W.H*D
 ck('generic_projected_cross_zero',zero(pi(Z0)))
 ck('generic_isometry_expansion',zero(A0+Z0+Z0.H+D.H*D-s.eye(6)))
 for name,Robs in [('Q',Q6),('T',T6)]:
  delta=V.H*Robs*V-Robs
  ck('generic_commutator_identity_'+name,zero(delta-(Robs*Z0-Z0*Robs+D.H*(Robs*D-D*Robs))))
 ck('generic_nonzero_effect_error',not zero(V.H*T6*V-T6))
 block=(V.H*T6*V-T6).extract([0,3],[0,3]);ck('generic_effect_error_norm',zero(block*block-v*v*s.eye(2)))
 kk=600;eps=v;MM=kk*kk*eps;z=kk*(1+kk)*eps;tau=MM+2*z
 ck('generic_small_polar_branch',tau<F(1,2) and 1-c<=tau+2*z)
 # At this fixture B=I: polar overlap and actual one-step record error.
 ck('generic_actual_overlap',1-c>0 and 1-c<=4*540600*eps)
 ck('generic_actual_record_bound',v*v<=8*540600*eps)
 ck('generic_Young_constant',F(3,2)*kk*kk+kk==540600)
 for m in [1,2,10]:
  ck('generic_horizon_coefficient_'+str(m),2*(m-1)*s.sqrt(2)<=3*(m-1))
  ck('generic_large_error_cap_'+str(m),F(3*m+5,4)>=1)
 ct('general_epsilon_not_exact_transparency',not zero(T6*V-V*T6))
generic_projection_checks()
Lsum=F(99,10**8);Esum=F(1,10**14);mm=100
qsum=F(sum(i*i for i in range(mm)),10**8)
crosssum=F(sum(range(mm)),10**12)
ordered_old=512*Esum+1024*crosssum+qsum
coarse_old=1024*Esum+F(513*mm*(mm-1),2)*Lsum
new_bound=(3*mm+5)*(Lsum+540600*Esum)
ck('generic_consumer_qsum',qsum==F(328350,10**8) and F(99**2,10**8)<1 and crosssum==F(4950,10**12))
ck('generic_consumer_ordered_bounds',ordered_old==F(328856880512,10**14) and new_bound==F(30359883,10**11) and new_bound<ordered_old<coarse_old)
ck('generic_consumer_crossover',Esum/Lsum<(F(513*mm*(mm-1),2)-(3*mm+5))/(540600*(3*mm+5)-1024))
ct('generic_not_uniformly_better',1024*Esum<(3*mm+5)*540600*Esum)

deps=[next((ROOT/'explorations/conditional-build').glob(k+'-*.md')) for k in ['k2494','k2496','k2500']]
report={'result':'K2502','checks':checks,'contrary_controls':controls,'coherent_rotations':rotation_cert,'general_coherent_error_bound':{'projection_constant':600,'epsilon_weight':540600,'horizon_coefficient':'3*m+5','last_gap_leakage':'absent','scope':'complete recorded output and reference; retain tighter prior bounds'},'complete_reference_fixture':{'error_enclosure':str(Eball),'bound':str(refined),'nonzero_blocks':nonzero,'scope':'original principal plane, entangled reference, four tests and three gaps; final P bit identically0 on this invariant plane'},'evidence_kinds':{'exact':'symbolic channel, polar row, reference and rational rotation identities','certified_finite':'160-bit Arb evaluation of exact complete-record trace norm','universal':'written supported-intertwiner telescope, dephased repair and quantified approximate-intertwiner proof','not_claimed':'finite-leakage optimal constant or calibrated exact zero effects'},'dependencies':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2502-verifier-leakage-horizon.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
else:ck('saved_report_reproduction',json.loads(out.read_text())==report)
print(json.dumps({'result':'PASS','checks':len(checks),'contrary_controls':len(controls),'reference_error':str(Eball)}))
