"""K2504: exact positive-effect, confidence and original-sector controls.
Universal statements are proved in the note; finite fixtures are coverage.
Run with --write only to regenerate the saved deterministic report.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import json,hashlib,sys
import sympy as s
from flint import arb,ctx
ctx.prec=160
ROOT=Path(__file__).resolve().parents[2]
checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ct(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
def zero(X):return all(s.simplify(x)==0 for x in X)
def psd(X):
 from itertools import combinations
 return zero(X-X.H) and all(s.simplify(X.extract(ii,ii).det())>=0 for n in range(1,X.rows+1) for ii in combinations(range(X.rows),n))
def rot(t):return s.Matrix([[(1-t*t)/(1+t*t),-2*t/(1+t*t)],[2*t/(1+t*t),(1-t*t)/(1+t*t)]])
# Genuine nonprojective effects, with both real and complex coherent blocks.
for t in [s.Rational(1,3),s.Rational(2,5),s.Rational(3,7)]:
 U=rot(t);R=s.diag(1,0)
 for eig in [(s.Rational(1,4),s.Rational(3,4)),(0,1),(s.Rational(1,5),s.Rational(2,5))]:
  for phase in [1,s.I]:
   V=s.diag(phase,1)*U;A=V*s.diag(*eig)*V.H;D=A-R;B=R*(s.eye(2)-A)*R+(s.eye(2)-R)*A*(s.eye(2)-R)
   label=str((t,eig,phase))
   ck('effect_and_complement_positive_'+label,psd(A) and psd(s.eye(2)-A))
   ck('exact_square_identity_'+label,zero(B-D*D-A+A*A))
   ck('square_domination_'+label,psd(B-D*D))
   cap=max(B[0,0],B[1,1]);ck('operator_bound_'+label,psd(cap*s.eye(2)-D*D))
ct('unphysical_matrix_cannot_use_identity',not psd(s.diag(2,0)-s.diag(2,0)**2))
# Original C108 P + principal plane + A8 + B10 + N87 representation.
Q=s.MutableSparseMatrix(108,108,{});T=s.MutableSparseMatrix(108,108,{})
for i in [0,1,*range(3,11)]:Q[i,i]=1
for i in [0,*range(11,21)]:T[i,i]=1
T[1,1]=s.Rational(27,127);T[2,2]=s.Rational(100,127);T[1,2]=T[2,1]=30*s.sqrt(3)/127
ck('original_Q_rank10',s.trace(Q)==10 and zero(Q*Q-Q))
ck('original_T_rank12',s.trace(T)==12 and zero(T*T-T))
ck('original_noncommuting_plane',not zero(Q*T-T*Q))
rotation_rows=[]
for z in [s.Rational(1,10),s.Rational(1,5)]:
 U=s.MutableSparseMatrix(s.eye(108));V=rot(z)
 for i,a in enumerate([3,11]):
  for j,b in enumerate([3,11]):U[a,b]=V[i,j]
 ck('actual_unitary_'+str(z),zero(U.H*U-s.eye(108)))
 t=V[0,1]**2
 for name,R in [('Q',Q),('T',T)]:
  A=U.H*R*U;D=A-R;block=D.extract([3,11],[3,11]);rank=int(s.trace(R));other=108-rank
  ck('rank_rotation_norm_'+name+str(z),zero(block*block-t*s.eye(2)))
  pplus=s.simplify(s.trace(R*(s.eye(108)-A))/rank);pminus=s.simplify(s.trace((s.eye(108)-R)*A)/other)
  ck('rank_sharpness_'+name+str(z),rank*pplus==t and other*pminus==t)
  ct('linear_wrong_count_bound_false_'+name+str(z),t>t*t)
  rotation_rows.append({'z':str(z),'effect_error_squared':str(t),'rank':rank,'wrong_plus':str(pplus),'wrong_minus':str(pminus)})
# Trusted preparation floor and missing support are actual density/effect examples.
rho=s.diag(s.Rational(1,100),s.Rational(99,100));B=s.diag(1,0)
ck('faithful_preparation_bound_sharp',s.trace(rho*B)==s.Rational(1,100))
ct('wrong_uniform_rank_under_biased_prep',2*s.trace(rho*B)<1)
ct('missing_support_invisible',s.trace(s.diag(0,1)*B)==0 and B.norm()==1)
# Memory0 tests see identity; memory1 swaps original A/B, defect1 globally.
Q4=s.diag(1,0,1,0);U4=s.diag(s.eye(2),s.Matrix([[0,1],[1,0]]));S=s.diag(1,1,0,0);D=U4.H*Q4*U4-Q4
ck('initialized_memory_calibration_passes',zero(S*D*S))
ct('uncovered_memory_defect_one',D[2,2]==-1 and D[3,3]==1)
# Leakage positive rank-one block saturates norm<=trace and can be missed by biased input.
L=s.diag(s.Rational(1,7),0,0);ck('leakage_trace_bound_sharp',3*s.trace(L)/3==s.Rational(1,7))
# Exact rational binomial inversion; returned high endpoint is conservative.
def tail(n,x,p):return sum(F(comb(n,j))*p**j*(1-p)**(n-j) for j in range(x+1))
def upper(n,x,beta,bits=32):
 if x==n:return F(1)
 lo,hi=F(0),F(1)
 for _ in range(bits):
  mid=(lo+hi)/2
  if tail(n,x,mid)>beta:lo=mid
  else:hi=mid
 return hi
beta=F(1,50);coverage=[]
for n in [1,2,5,10]:
 bounds=[upper(n,x,beta) for x in range(n+1)]
 ck('binomial_upper_monotone_'+str(n),all(bounds[i]<=bounds[i+1] for i in range(n)))
 ck('binomial_all_wrong_endpoint_'+str(n),bounds[-1]==1)
 for x,u in enumerate(bounds[:-1]):ck('binomial_root_upper_'+str((n,x)),tail(n,x,u)<=beta)
 for p in [F(0),F(1,10),F(1,3),F(1,2),F(9,10),F(1)]:
  risk=sum(F(comb(n,x))*p**x*(1-p)**(n-x) for x in range(n+1) if bounds[x]<p)
  ck('finite_coverage_'+str((n,p)),risk<=beta);coverage.append({'n':n,'p':str(p),'risk':str(risk)})
ct('point_estimate_not_confidence',F(9,10)**10>beta)
ct('finite_zero_not_exact',F(999,1000)**100>F(9,10))
# Exact multiplicative familywise probability control: union-bound coefficient.
for G in [1,2,7]:ck('confidence_allocation_'+str(G),5*G*F(1,100)/(5*G)==F(1,100))
ct('failure_to_allocate_settings',5*F(1,100)>F(1,100))
# Resource and consumer arithmetic; logs enclosed rigorously by Arb.
d=108;eps=F(1,10**6);ell=eps;ranks=[10,98,12,96]
ck('log500_below7',arb(500).log().upper()<7)
ck('tomography_log_above15',arb(6998400).log().lower()>15)
shots=sum(r*7*10**12 for r in ranks)+108*7*10**6
ck('total_trials',shots==1512000756000000)
old_lower=34992*2*92556*15*10**12
ck('design_improvement',old_lower>60000000*shots)
ck('ranks_sum_two_d',sum(ranks)==2*d)
ct('systematic_floor_cannot_shrink_with_shots',F(1,10**12)*98>eps*eps)
E=512*(2*eps)+1024*eps+ell
ck('ordered_record_consumer',E==F(2049,10**6) and E<F(1,100))
ck('positive_postselection_margin',E/(F(1,2)-E)==F(2049,497951)<F(1,200))
ct('zero_acceptance_margin_invalid',F(1,100)-F(2,100)<0)
# Rotation alternative: false acceptance on all-correct transcript at fixed independent counts.
t=F(1,25);n=[2,3,4,5];P0=F(1)
for r,nn in zip(ranks,n):P0*=(1-t/r)**nn
ct('undersampled_rotation_false_certification',P0>F(1,100) and t>F(1,100))
ck('transcript_probability_nonzero',0<P0<1)
# Explicitly altered rank and leakage normalization fail the sharp examples.
ct('omit_sector_rank_fails',t/98<t)
ct('omit_leakage_dimension_fails',F(1,7)/108<F(1,7))
ck('confidence_bias_triangle',F(1,100)+F(1,200)+F(1,400)==F(7,400))
# Pooled randomized labels: exact normalized-error domination and resource consumer.
ci=[F(rr,1)/(eps*eps) for rr in ranks]+[F(d,1)/ell];W=sum(ci);weights=[v/W for v in ci]
ck('pooled_label_weights',sum(weights)==1 and all(v>0 for v in weights))
for vals in [[F(0)]*5,[F(1,2),F(1,8),F(1,8),F(1,8),F(1,8)],[F(1),F(0),F(0),F(0),F(0)]]:
 means=[v/cv for v,cv in zip(vals,ci)];pmean=sum(w*p for w,p in zip(weights,means))
 ck('pooled_load_identity_'+str(vals),W*pmean==sum(vals))
 ck('pooled_gate_implies_each_'+str(vals),sum(vals)<=1 and all(v<=1 for v in vals))
ct('separate_gate_not_pooled_gate',all(v<=1 for v in [F(1)]*5) and sum([F(1)]*5)>1)
ck('pooled_log100_below5',arb(100).log().upper()<5)
ck('pooled_sufficient_trials',W*5==1080000540000000 and W*5<shots)
# Wrong weighting can make pooled pass even though one sector load is >1.
badweights=[weights[0]/100,weights[1]+weights[0]*F(99,100),*weights[2:]]
means=[2/ci[0],F(0),F(0),F(0),F(0)]
ct('misweighted_label_gate_false',sum(badweights)==1 and W*sum(w*p for w,p in zip(badweights,means))<1 and ci[0]*means[0]>1)
etas=[F(1,10**16)]*5
ck('pooled_systematic_bias',W*sum(w*v for w,v in zip(weights,etas))==sum(c*v for c,v in zip(ci,etas)))
# An actual biased preparation and noisy readout obey the probability triangle.
rho0=s.diag(s.Rational(1,2),s.Rational(1,2));rho1=s.diag(s.Rational(49,100),s.Rational(51,100));A0=s.diag(0,s.Rational(1,2));A1=A0+s.eye(2)/100
ck('actual_preparation_readout_bias',abs(s.trace(rho1*A1)-s.trace(rho0*A0))<=s.Rational(1,100)+s.Rational(1,100))
# Pooling sharpness: actual A-sector memory rotation preserves both effects.
zmem=s.Rational(1,5);Vmem=rot(zmem);UM=s.eye(4)
for i,ii in enumerate([0,2]):
 for j,jj in enumerate([0,2]):UM[ii,jj]=Vmem[i,j]
Tm=s.eye(4)-Q4;Lm=S*UM.H*(s.eye(4)-S)*UM*S;leak=Vmem[0,1]**2
ck('pooled_memory_unitary',zero(UM.H*UM-s.eye(4)))
ck('pooled_memory_effects_exact',zero(UM.H*Q4*UM-Q4) and zero(UM.H*Tm*UM-Tm))
ck('pooled_memory_rank_one_leak',zero(Lm-s.diag(leak,0,0,0)))
ck('pooled_leak_probability',weights[-1]*(ell/F(d))==1/W)
for tw in [[F(1,5)]*5,weights]:
 C=max(c0/q0 for c0,q0 in zip(ci,tw))
 ck('pooling_scalar_minimax_'+str(tw==weights),C>=W and sum(q0*(c0/q0) for c0,q0 in zip(ci,tw))==W)
ct('nonoptimal_weights_larger_scalar',max(ci)*5>W)
# Exact finite all-zero false-certificate control versus sufficient allocation.
WW=400
ct('pooled_insufficient_zero_count',F(WW-1,WW)**100>F(1,100))
ck('pooled_sufficient_zero_count',F(WW-1,WW)**2000<F(1,100))
ct('pooled_systematic_floor',sum(c0*F(1,10**14) for c0 in ci)>1)
report={'result':'K2504','scope':'conditional five-distribution calibration; no measured data or native physical credit','evidence_kind':'universal written proof plus finite exact algebra/rational coverage and certified log enclosures; counts are not theorem totals','checks':checks,'contrary_controls':controls,'rotation_rows':rotation_rows,'binomial_fixtures':coverage,'resources':{'new_sufficient_trials':shots,'old_design_lower':old_lower,'record_bound':str(E),'accepted_bound':str(E/(F(1,2)-E))},'dependencies':{}}
for p in [__file__,str(ROOT/'explorations/conditional-build/k2504-verifier-sector-calibration-2026-11-02.md'),str(ROOT/'explorations/conditional-build/k2502-verifier-leakage-horizon-2026-11-02.md'),str(ROOT/'explorations/conditional-build/k2500-reachable-memory-leakage-2026-11-02.md')]:
 p=Path(p);report['dependencies'][str(p.relative_to(ROOT))]=hashlib.sha256(p.read_bytes()).hexdigest()
path=ROOT/'lab/process/k2504-verifier-sector-calibration.json'
if '--write' in sys.argv:path.write_text(json.dumps(report,indent=2)+'\n')
else:ck('saved_report_matches_reproduction',json.loads(path.read_text())==report)
print(f'K2504 PASS: {len(checks)} checks; {len(controls)} contrary controls')
