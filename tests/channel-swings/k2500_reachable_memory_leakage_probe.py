"""Exact leakage/repaired-channel controls; universal bounds live in the note."""
from pathlib import Path
from fractions import Fraction as F
import sympy as s
import json,hashlib,sys
ROOT=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ct(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
def star(A):return A.conjugate().T
def rec(A):
 d=A.rows;E=s.eye(d);B=s.zeros(d)
 for a in range(d):B[a,a]=A[a,a]
 for a in range(d):
  for b in range(a+1,d):
   v=E[:,a]+E[:,b];z=E[:,a]+s.I*E[:,b]
   real=(star(v)*A*v)[0]/2-(A[a,a]+A[b,b])/2
   imag=(A[a,a]+A[b,b])/2-(star(z)*A*z)[0]/2
   B[a,b]=real+s.I*imag;B[b,a]=s.conjugate(B[a,b])
 return B.applyfunc(s.simplify)
Q=s.diag(1,1,0);T=s.diag(1,0,1);J=s.kronecker_product(s.eye(3),s.Matrix([1,0]));S=J*J.T;O=s.eye(6)-S
for c,t in [(s.Rational(4,5),s.Rational(3,5)),(s.Rational(12,13),s.Rational(5,13)),(s.Rational(99,101),s.Rational(20,101))]:
 ell=t*t;U=s.eye(6);U[2,2]=U[3,3]=c;U[3,2]=t;U[2,3]=-t
 ck('unitary_'+str(c),U.T*U==s.eye(6))
 A=U*J;L=star(A)*O*A;ck('uniform_leak_'+str(c),L==s.diag(0,ell,0))
 tau=s.Matrix([0,0,1]);K=[J.T*A]+[tau*A[k,:] for k in [1,3,5]]
 ck('repair_TP_'+str(c),sum((star(k)*k for k in K),s.zeros(3))==s.eye(3))
 for name,R in [('Q',Q),('T',T)]:
  full=s.kronecker_product(R,s.eye(2));effect=star(A)*full*A
  repaired=sum((star(k)*R*k for k in K),s.zeros(3));diff=repaired-effect
  ck('compressed_exact_'+name+str(c),effect==R)
  ck('repair_defect_'+name+str(c),diff.is_diagonal() and max(abs(z) for z in diff)<=ell)
  ck('reconstruct_'+name+str(c),rec(effect)==effect)
 ck('reconstruct_leak_'+str(c),rec(L)==L)
 # Pure coherent leak, repair to the originating A state: distance squared=ell.
 v=U*s.eye(6)[:,2];D=v*v.T-s.eye(6)[:,2]*s.eye(6)[2,:]
 ck('coherent_difference_square_'+str(c),D.extract([2,3],[2,3])**2==ell*s.eye(2))
 ct('linear_full_state_bound_fails_'+str(c),t>ell)
 ck('invisible_coherence_Q_'+str(c),(v.T*s.kronecker_product(Q,s.eye(2))*v)[0]==1)
 # Entangled input with two distinct reference labels, repair keeps leak marginal.
 vr=s.Matrix([0,0,1,0,0,1])/s.sqrt(2);rho=vr*vr.T
 actual=s.kronecker_product(A,s.eye(2))*rho*s.kronecker_product(A.T,s.eye(2))
 repaired=sum((s.kronecker_product(k,s.eye(2))*rho*s.kronecker_product(star(k),s.eye(2)) for k in K),s.zeros(6))
 embed=s.kronecker_product(J,s.eye(2));comp=s.kronecker_product(S,s.eye(2))*actual*s.kronecker_product(S,s.eye(2))
 marginal=s.zeros(2)
 for k in [1,3,5]:marginal+=actual[2*k:2*k+2,2*k:2*k+2]
 ck('leak_reference_'+str(c),marginal==s.diag(ell/2,0))
 ck('amplified_repair_'+str(c),embed*repaired*embed.T==comp+s.kronecker_product(J*tau*tau.T*J.T,marginal))
 ct('wrong_reference_product_'+str(c),marginal!=ell/2*s.eye(2)/2)
# Complex preparation remains necessary for the smaller-support effect.
V=s.Matrix([[s.Rational(4,5),s.I*s.Rational(3,5),0],[s.I*s.Rational(3,5),s.Rational(4,5),0],[0,0,1]])
B=star(V)*T*V;ck('complex_reconstruction',rec(B)==B);ct('real_only_misses',B!=B.applyfunc(s.re))
# Actual two-gap counterexample: uniform-mixture leakage small but selected input fails.
U=s.eye(6);U[2,2]=U[3,3]=0;U[2,3]=U[3,2]=1
V=s.eye(6);V[3,3]=V[5,5]=0;V[3,5]=V[5,3]=1
L=J.T*U.T*O*U*J
ck('rank_one_leakage',L==s.diag(0,1,0));ck('second_supported_identity',V*J==J)
a=s.eye(6)[:,2];fullQ=s.kronecker_product(Q,s.eye(2))
ct('actual_two_gap_record_failure',(a.T*U.T*V.T*fullQ*V*U*a)[0]==0 and (a.T*fullQ*a)[0]==1)
ct('actual_prefix_not_supported',O*U*a!=s.zeros(6,1))
K0=J.T*U*J;K1=s.Matrix([0,1,0])*U[3,:]*J
ck('repaired_prefix_supported',O*J*(K0*K0.T+K1*K1.T)*J.T==s.zeros(6))
for M in [1,2,10,100]:
 d=108*M;average=F(1,d)
 ck('trace_to_norm_'+str(M),d*average==1)
 ct('average_not_worst_case_'+str(M),average<1)
for q in [F(1,2),F(1,100),F(1,10000),F(1,10**8)]:
 eps=q/1536;ell=min(q*q/9,2*q/3075)
 ck('sqrt_budget_'+str(q),ell<=(q/3)**2)
 ck('linear_leak_budget_'+str(q),F(1025,2)*ell<=q/3)
 ck('effect_budget_'+str(q),512*eps==q/3)
 r=min(eps,ell)
 ck('sample_radius_algebra_'+str(q),F(1,4)*r*r<=(eps/2)**2 and r*r/4<=(ell/2)**2)
 ct('unqualified_linear_leak_budget_'+str(q),q/3>(q/3)**2)
for d in [3,108,216]:
 ck('three_effect_settings_'+str(d),3*(d+2*d*(d-1)//2)==3*d*d)
 ck('radius_constant_'+str(d),d+8*d*(d-1)==8*d*d-7*d)
# Pure compression trace norm formula is independently verified via a symbolic 2x2 characteristic polynomial.
p,z=s.symbols('p z',real=True);D=s.Matrix([[0,s.sqrt(p*(1-p))],[s.sqrt(p*(1-p)),p]])
ck('projection_characteristic',s.expand((z*s.eye(2)-D).det()-(z*z-p*z-p*(1-p)))==0)
ck('gentle_discriminant',s.expand(p*p+4*p*(1-p))==4*p-3*p*p)
ct('nonpositive_margin',F(1,10)*F(1,100)-F(1,100)<0)
# Direct fixed-horizon record bounds and actual coherent accumulation.
for c,t in [(s.Rational(4,5),s.Rational(3,5)),(s.Rational(12,13),s.Rational(5,13))]:
 rotation=s.Matrix([[c,-t],[t,c]])
 for j in range(1,9):
  v=rotation**j*s.Matrix([1,0]);pj=s.expand(v[1]**2)
  ck('aggregate_rotation_'+str(c)+'_'+str(j),pj<=j*j*t*t)
 marker=s.eye(6);marker[3,3]=marker[5,5]=0;marker[3,5]=marker[5,3]=1
 out=marker*s.kronecker_product(s.eye(3),rotation)*s.eye(6)[:,2]
 ck('sharp_two_gap_record_'+str(c),s.simplify(1-(out.T*fullQ*out)[0])==t*t)

for N,theta in [(2,s.pi/4),(3,s.pi/6),(4,s.pi/8)]:
 rotation=s.Matrix([[s.cos(theta),-s.sin(theta)],[s.sin(theta),s.cos(theta)]])
 mem=(rotation**N).applyfunc(s.simplify);U=s.kronecker_product(s.eye(3),mem)
 marker=s.eye(6);marker[3,3]=marker[5,5]=0;marker[3,5]=marker[5,3]=1
 a=s.eye(6)[:,2];out=marker*U*a
 ck('coherent_cap_record_'+str(N),s.simplify((out.T*fullQ*out)[0])==0)
 ck('marker_supported_identity_'+str(N),marker*J==J)
 ct('no_cap_independent_certificate_'+str(N),s.simplify(N*s.sin(theta)**2)<s.Rational(3,2))
# A support/outside mixer has nonzero off-diagonal record effect.
c=s.Rational(4,5);v=s.Rational(3,5);U=s.eye(6)
U[2,2]=U[5,5]=c;U[5,2]=v;U[2,5]=-v
D=U.T*fullQ*U-fullQ
ck('compressed_diagonal_defect',J.T*D*J==s.diag(0,-v*v,0))
ck('nonzero_cross_defect',(S*D*O)[2,5]==-c*v)
ck('cross_sqrt_bound',c*c*v*v<=v*v)
for m in [2,3,10,100]:
 C=F(513*m*(m-1),2)
 for delta in [F(1,2),F(1,1000)]:
  ep=delta/(2048*m);el=delta/(2*m*C)
  ck('direct_calibration_'+str(m)+'_'+str(delta),1024*m*ep+C*m*el==delta)
 ck('cauchy_horizon_'+str(m),sum(range(m))==m*(m-1)//2)
for ep,q in [(F(1,100),F(1,10)),(F(1,2),F(1,2)),(F(0),F(1))]:
 ck('young_squared_'+str(ep)+'_'+str(q),4*ep*q<=(ep+q)**2)
deps=['explorations/conditional-build/k2496-approximate-verifier-effects-2026-11-02.md','explorations/conditional-build/k2498-joint-effect-calibration-2026-11-02.md']
report={'result':'K2500','checks':checks,'contrary_controls':controls,'bounds':{'repair':'sqrt(ell)+ell/2','direct_record':'min(1,1024 sum epsilon+513m(m-1)/2 sum ell)','record':'min(1,sum_j max_h[min(1,sqrt(ell)+ell/2)+512 min(1,epsilon+ell)])','calibration_settings':'3 G d^2','sufficient_sampling':'2(8d^2-7d) log(6Gd^2/alpha)/min(epsilon_target,ell_target)^2'},'evidence_kinds':{'exact':'rational channel/effect/reference matrices and budget inequalities','universal':'written compression, hybrid, effect and concentration proof','not_claimed':'optimal horizon dependence, executed calibration or native GU realization'},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2500-reachable-memory-leakage.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
else:ck('saved_report_reproduction',json.loads(out.read_text())==report)
print(json.dumps({'result':'PASS','checks':len(checks),'contrary_controls':len(controls)}))
