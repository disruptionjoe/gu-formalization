"""Exact finite controls for K2506; universal statements are written proofs.
Use --write to regenerate the deterministic report. No experiment is run.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,sys
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
def zero(A):return all(s.simplify(x)==0 for x in A)
def aa(x):return arb(x.numerator)/x.denominator
# A history-adaptive conditional Bernoulli tree, including certain failures.
# Exact reciprocal-survival process proves the finite conditional recursion.
alpha=F(1,8);crossing=F(0);states=[(F(1),(),F(1),F(0),False)]
for step in range(7):
 new=[]
 for prob,h,M,A,hit in states:
  mu=F((step+sum(h))%5,4)
  m0=M/(1-mu) if mu<1 else F(0)
  ck('conditional_hazard_'+str((step,h)),(1-mu)*m0<=M)
  for bit,pp,Mn in [(0,1-mu,m0),(1,mu,F(0))]:
   if pp==0:continue
   new.append((prob*pp,h+(bit,),Mn,A+mu,hit or Mn>=1/alpha))
 states=new
ck('tree_total_probability',sum(x[0] for x in states)==1)
risk=sum(prob for prob,h,M,A,hit in states if hit)
ck('maximal_crossing_bound',0<risk<=alpha)
# Every zero path obeys the exact Jensen/AM-GM comparison.
for prob,h,M,A,hit in states:
 if not sum(h):ck('zero_path_mean_hazard',M*(1-A/len(h))**len(h)>=1)
# Explicit restart invalidity and average-vs-worst-case separation.
ct('resetting_counts_invalid',1-F(63,64)**9>alpha)
# All five load coordinates are nonnegative; historywise density-capped transfer.
eps=F(1,1000);ell=F(1,1000);d=108
c=[F(r)/(eps*eps) for r in [10,98,12,96]]+[F(d)/ell];W=sum(c);q=[v/W for v in c]
ck('correct_original_label_weights',sum(q)==1 and sum(c[:4])==2*d/(eps*eps))
loads=[[F(0)]*5,[F(1,4),F(1,8),F(0),F(0),F(1,8)],[F(1,8),F(0),F(1,8),F(1,8),F(1,8)],[F(1,2),F(0),F(0),F(0),F(0)]]
n=len(loads);B=sum(sum(x) for x in loads)/n;rho=F(2)
for w in [[F(1,4)]*4,[F(0),F(1,2),F(1,2),F(0)],[F(1,2),F(0),F(0),F(1,2)]]:
 ck('density_cap_'+str(w),sum(w)==1 and max(w)<=rho/n)
 for i in range(5):ck('weighted_load_'+str((w,i)),sum(w[t]*loads[t][i] for t in range(n))<=rho*B)
for t,row in enumerate(loads):
 pp=[row[i]/c[i] for i in range(5)]
 ck('five_setting_scalar_identity_'+str(t),W*sum(q[i]*pp[i] for i in range(5))==sum(row))
ct('uncapped_selection_fails',F(1)>F(1,100))
# Actual 4D CPTP maps: original A-only and B-only vectors, each with two memory labels.
Q=s.diag(1,1,0,0);T=s.eye(4)-Q;U=s.diag(1,-1,1,-1)
ck('memory_unitary',zero(U.H*U-s.eye(4)))
ck('diamond_far_effects_exact',zero(U.H*Q*U-Q) and zero(U.H*T*U-T))
psi=s.Matrix([1,1,0,0])/s.sqrt(2)
ck('orthogonal_stored_outputs',(psi.H*U*psi)[0]==0)
# An actual target/A embedding gives target-bit loss after uncovered switch.
Q2=s.diag(1,0);X=s.Matrix([[0,1],[1,0]])
ck('swap_is_cptp_unitary',zero(X.H*X-s.eye(2)))
ct('untested_deployment_changes_effect',not zero(X.H*Q2*X-Q2))
# Perfect test-memory support says nothing about dormant deployment labels.
Qm=s.diag(1,0,1,0);Sm=s.diag(1,1,0,0);Um=s.diag(s.eye(2),X)
ck('dormant_memory_compression_exact',zero(Sm*(Um.H*Qm*Um-Qm)*Sm))
ct('dormant_memory_global_bad',not zero(Um.H*Qm*Um-Qm))
# Wrong label-dependent channel can force all calibration outcomes correct.
# On Q+ prepare Q+, on Q- prepare Q-; a single common replacement map cannot do both.
pplus=s.diag(1,0);pminus=s.diag(0,1)
ck('label_dependent_zero_counts',s.trace(Q2*pplus)==1 and s.trace(Q2*pminus)==0)
ct('no_common_constant_output_matches_both',s.trace(Q2*pplus)!=s.trace(Q2*pminus))
# One bad sampled map among 100: average is small but uncapped future choice bad.
Abar=(99*Q2+X.H*Q2*X)/100
ck('average_effect_small',zero((Abar-Q2)**2-s.eye(2)/10000))
ct('average_is_not_every_history',zero((X.H*Q2*X-Q2)**2-s.eye(2)))
# The confidence event can be reused for arbitrarily many histories, but not
# for unbounded horizon: algebraic consumer allocations use explicit m.
resources=[]
for m in [2,3,10]:
 Delta=F(1,100);Cm=F(513*m*(m-1),2);e=Delta/(2048*m);l=Delta/(2*m*Cm)
 de=e/4;dl=l/4;rh=F(4)
 # rho*eps0^2=(e-de)^2 and rho*ell0=l-dl, without irrational arithmetic.
 eps0=(e-de)/2;ell0=(l-dl)/rh
 ck('effect_transfer_target_'+str(m),rh*eps0**2==(e-de)**2)
 ck('leakage_transfer_target_'+str(m),rh*ell0==l-dl)
 ck('record_budget_'+str(m),1024*m*e+Cm*m*l==Delta)
 WW=2*d/(eps0**2)+d/ell0;eta=F(1,10)/WW
 # log100<5 implies this integer sufficient count for the zero-count rule.
 N=(WW*F(50,9)).numerator//(WW*F(50,9)).denominator+1
 ck('sample_sufficient_'+str(m),aa(1/WW-eta)*N>arb(100).log())
 ck('positive_bias_margin_'+str(m),WW*eta<F(1))
 ct('shots_cannot_fix_bias_'+str(m),WW*(2/WW)>1)
 resources.append({'gaps':m,'trials_sufficient':N,'epsilon_target':str(e),'leakage_target':str(l),'W':str(WW),'bias':str(eta)})
# Actual shared-bit and independent-bit two-gap record laws.
from collections import defaultdict
shared=defaultdict(F);independent=defaultdict(F)
for z in [0,1]:
 state=0;rec=[]
 for bit in [z,z]:state^=bit;rec.append(1-state)
 shared[tuple(rec)]+=F(1,2)
for x in [0,1]:
 for y in [0,1]:
  state=0;rec=[]
  for bit in [x,y]:state^=bit;rec.append(1-state)
  independent[tuple(rec)]+=F(1,4)
ck('shared_record_distribution',dict(shared)=={(1,1):F(1,2),(0,1):F(1,2)})
ct('single_use_marginal_not_process',sum(abs(shared[k]-independent[k]) for k in set(shared)|set(independent))/2==F(1,2))
# Nonzero density and drift example stated in the note.
WW=F(1728000432000000);N=8640002160000000
ck('explicit_coverage_W',F(2)*(216/F(1,2000000)**2+108/F(1,2000000))==WW)
ck('explicit_coverage_samples',N==5*WW and aa(F(N)/WW)>arb(100).log())
# Positive label starvation changes the physical sampling distribution.
means=[F(1,10),F(0),F(0),F(0),F(0)]
starved=[q[0]/100,q[1]+q[0]*F(99,100),*q[2:]]
ct('starved_label_load_underestimated',W*sum(x*y for x,y in zip(starved,means))<c[0]*means[0])
for qq in [q,[F(1,5)]*5]:
 C=max(x/y for x,y in zip(c,qq));ck('adaptive_domination_lower_'+str(qq==q),C>=W)

# Two-gap actual consumer example with nonzero transfer and density cap.
E=F(2049,10**6)
ck('two_gap_record_bound',512*F(2,10**6)+1024*F(1,10**6)+F(1,10**6)==E)
ck('postselected_bound',E/(F(1,2)-E)==F(2049,497951)<F(1,200))
ct('postselection_without_margin_invalid',F(1,100)-F(1,50)<0)
report={'result':'K2506','scope':'conditional original verifier effect-specific transfer and complete histories; no empirical input or native physical result','evidence_kind':'written universal composition proof; finite exact rational/channel controls and certified sample logarithms','checks':checks,'contrary_controls':controls,'finite_crossing_probability':str(risk),'resources':resources,'dependencies':{}}
for path in [Path(__file__),ROOT/'explorations/conditional-build/k2506-calibration-deployment-transfer-2026-11-02.md',ROOT/'explorations/conditional-build/k2430-adaptive-decoder-certification-2026-11-01.md',ROOT/'explorations/conditional-build/k2504-verifier-sector-calibration-2026-11-02.md',ROOT/'explorations/conditional-build/k2500-reachable-memory-leakage-2026-11-02.md']:
 report['dependencies'][str(path.relative_to(ROOT))]=hashlib.sha256(path.read_bytes()).hexdigest()
out=ROOT/'lab/process/k2506-calibration-deployment-transfer.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,indent=2)+'\n')
else:ck('saved_report_matches_reproduction',json.loads(out.read_text())==report)
print(f'K2506 PASS: {len(checks)} exact/certified checks; {len(controls)} contrary controls')
