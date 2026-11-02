"""Exact effect reconstruction and physical contrary fixtures, not experimental data."""
from pathlib import Path
from fractions import Fraction as F
import sympy as s
import json,hashlib,sys
R=Path(__file__).resolve().parents[2]; checks={}; controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ct(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
def reconstruct(A):
 d=A.rows;eye=s.eye(d);out=s.zeros(d);diag=[A[i,i] for i in range(d)]
 for i in range(d):out[i,i]=diag[i]
 for i in range(d):
  for j in range(i+1,d):
   v=eye[:,i]+eye[:,j];z=eye[:,i]+s.I*eye[:,j]
   pr=(v.conjugate().T*A*v)[0]/2;pi=(z.conjugate().T*A*z)[0]/2
   out[i,j]=pr-(diag[i]+diag[j])/2+s.I*((diag[i]+diag[j])/2-pi);out[j,i]=s.conjugate(out[i,j])
 return out.applyfunc(s.simplify)
# Selected P,A,B reducing block embeds unchanged into the original108 carrier.
Q=s.diag(1,1,0);T=s.diag(1,0,1);V=s.Matrix([[1,0,0],[0,0,1],[0,1,0]]);I=s.eye(3)
U=s.Matrix([[s.Rational(4,5),s.I*s.Rational(3,5),0],[s.I*s.Rational(3,5),s.Rational(4,5),0],[0,0,1]])
ck('complex_channel_unitary',U.conjugate().T*U==I)
for idx,A in enumerate([Q,T,U.conjugate().T*Q*U,U.conjugate().T*T*U,(T+V.T*T*V)/2]):
 ck('exact_complex_reconstruction_'+str(idx),reconstruct(A)==A)
A=U.conjugate().T*T*U;defect=A-T
ck('complex_defect_square',defect[:2,:2]**2==s.eye(2)*s.Rational(9,25))
realonly=A.applyfunc(s.re)-T
ct('real_states_miss_true_norm',max(abs(v) for v in realonly)==s.Rational(9,25)<s.Rational(3,5))
ct('wrong_imaginary_sign',A!=s.conjugate(A))
for d in [2,3,4,108,216]:
 ck('setting_count_'+str(d),d+2*(d*(d-1)//2)==d*d)
 ck('HS_constant_'+str(d),d+8*d*(d-1)==8*d*d-7*d)
# Exact nontrivial signed errors generated at the probability level.
for d in [2,3,4]:
 for z in range(8):
  diag=[s.Rational(1 if (z+i)%2 else -1,100) for i in range(d)];err=s.diag(*diag)
  for i in range(d):
   for j in range(i+1,d):
    er=s.Rational(1 if (z+i+j)%2 else -1,100)-(diag[i]+diag[j])/2
    ei=(diag[i]+diag[j])/2-s.Rational(1 if (z+2*i+j)%3 else -1,100)
    err[i,j]=er+s.I*ei;err[j,i]=er-s.I*ei
  hs=s.trace(err.conjugate().T*err)
  ck('probability_error_HS_'+str((d,z)),hs<=(8*d*d-7*d)*s.Rational(1,10000))
D=108;G=1;delta=F(1,22);eps=delta/512;N=32*(8*D*D-7*D)*11264**2
ck('consumer_margin',eps==F(1,11264) and (F(0)+delta)/(F(1,2)-delta)==F(1,10))
ck('sample_integer',N==375785344991232)
# exp(16)>4665600 proves log(4665600)<16, with positive rational terms only.
exp_lower=sum((F(16)**k/F(s.factorial(k)) for k in range(41)),F(0))
ck('certified_log_upper',exp_lower>4665600)
ck('sample_radius_bound',F((8*D*D-7*D)*16,2*N)==(eps/2)**2)
ck('use_count',2*G*D*D*N==8766320527955460096)
ct('systematic_floor',F(8*D*D-7*D,10**12)>(eps/2)**2)
ct('nonpositive_margin',F(1,10)*F(1,100)-F(1,100)<=0)
ct('nonpositive_acceptance_denominator',F(1,100)-F(1,50)<0)
# Full two-level dormant memory, with exact invariant inclusion J.
E0=s.diag(1,0);E1=s.diag(0,1);W=s.kronecker_product(I,E0)+s.kronecker_product(V,E1)
J=s.kronecker_product(I,s.Matrix([1,0]));ck('dormant_unitary',W.T*W==s.eye(6));ck('reachable_identity',W*J==J)
for idx,B in enumerate([Q,T]):
 full=s.kronecker_product(B,s.eye(2));diff=W.T*full*W-full
 ck('dormant_bad_sector_'+str(idx),diff.is_diagonal() and max(abs(x) for x in diff)==1)
 ck('dormant_restricted_effect_'+str(idx),J.T*diff*J==s.zeros(3))
ct('initialized_effects_not_global',W!=s.eye(6) and W*J==J)
# Entangled system/reference vector on initialized memory is still fixed.
v=s.Matrix([1,0,0,1,0,0])/s.sqrt(2);jr=s.kronecker_product(J,s.eye(2));wr=s.kronecker_product(W,s.eye(2));ck('reference_indistinguishability',wr*jr*v==jr*v)
for L in [1,2,4]:
 W=s.zeros(3*(L+1));shift=s.zeros(L+1)
 for k in range(L):
  step=s.zeros(L+1);step[k+1,k]=1;W+=s.kronecker_product(I,step);shift+=step
 step=s.zeros(L+1);step[0,L]=1;W+=s.kronecker_product(V,step);shift+=step
 W0=s.kronecker_product(I,shift);j=s.kronecker_product(I,s.eye(L+1)[:,0]);ck('clock_unitary_'+str(L),W.T*W==s.eye(3*(L+1)))
 for k in range(L+1):ck('clock_prefix_'+str((L,k)),W**k*j==W0**k*j)
 a=s.Matrix([0,1,0]);z=W**(L+1)*j*a;zz=W0**(L+1)*j*a;obs=s.kronecker_product(Q,s.eye(L+1))
 ct('future_failure_'+str(L),(z.T*obs*z)[0]==0 and (zz.T*obs*zz)[0]==1)
# Changing maps between settings breaks the single-effect data premise.
ct('uncovered_map_can_fail',V.T*Q*V!=Q and s.trace(V.T*Q*V)==s.trace(Q))
deps=['explorations/conditional-build/k2496-approximate-verifier-effects-2026-11-02.md','explorations/conditional-build/k2494-memory-transparent-storage-2026-11-02.md']
report={'result':'K2498','checks':checks,'contrary_controls':controls,'sample_example':{'D':D,'G':G,'epsilon_target':str(eps),'shots_per_setting':N,'total_map_uses':2*G*D*D*N,'status':'sufficient theoretical count; no experiment executed'},'bounds':{'effect_radius':'sqrt(8D^2-7D)*(sqrt(log(4GD^2/alpha)/(2N))+eta)','record_error':'min(1,512*sum(epsilon_j))'},'evidence_kinds':{'exact':'complex reconstruction, invariant embeddings, actual unitary controls and rational resource arithmetic','universal':'written norm/concentration, arbitrary-duration and reference arguments','not_claimed':'measured device, efficient/optimal calibration, unknown-memory guarantee or GU realization'},'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps}}
p=R/'lab/process/k2498-joint-effect-calibration.json'
if '--write' in sys.argv:p.write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
else:ck('saved_reproduction',json.loads(p.read_text())==report)
print(json.dumps({'result':'PASS','checks':len(checks),'controls':len(controls),'sample_example':report['sample_example']}))
