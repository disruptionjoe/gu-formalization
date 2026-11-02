"""Exact original-law finite witness and Bellman boundary controls, with Arb log budgets."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,sys,math
from flint import arb,ctx
ctx.prec=256
ROOT=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,b):
 checks[k]=bool(b)
 if not b:raise AssertionError('FAIL '+k)
def ctrl(k,b):
 controls[k]=bool(b)
 if not b:raise AssertionError('FAIL contrary '+k)
def aa(x):
 x=F(x);return arb(x.numerator)/x.denominator
def cost(a,b):
 if a>=b:return arb(0)
 return (1+aa((b-a)**2/(2*(a+b)*(2-a-b)))).log()
def law(seq):
 p=F(1);K=arb(0);success_only=arb(0)
 for a,b in seq:
  ck('admissible_'+str((a,b)),0<=a<=b<=1)
  K+=aa(p)*2*cost(a,b)/aa(1+a);p/=1+a
 for a,b in seq:success_only+=aa(p)*2*cost(a,b)/aa(1+a)
 return p,K,success_only
A=[(F(3813,4096),F(123,128))]+[(F(7,2048),F(1,128))]*5+[(F(13,4096),F(1,128))]
B=[(F(1),F(1)),(F(13,4096),F(1,128))]
pA,kA,badA=law(A);pB,kB,badB=law(B)
ck('equal_exact_score',sum(b for a,b in A)==sum(b for a,b in B)==F(129,128))
ck('all_prefinal_scores_below_target',all(sum(b for a,b in seq[:i])<=1 for seq in [A,B] for i in range(len(seq))))
ck('bracketing_probabilities',pA>F(1,2)>pB)
alpha0=(F(1,2)-pB)/(pA-pB);bits=40;alpha=F((alpha0*(2**bits)).numerator//(alpha0*(2**bits)).denominator+1,2**bits)
p=alpha*pA+(1-alpha)*pB;K=aa(alpha)*kA+aa(1-alpha)*kB;c=arb(2).log();ratio=c/(256*K)
ck('fair_bit_mixture_strict',0<alpha<1 and p>F(1,2))
ck('rigorous_finite_ratio_above_2_1259',ratio>aa(F(21259,10000)))
ck('finite_ratio_below_uniform_bound',ratio<(1+c)**2/(4*(1-c)))
ck('strict_crossing_at_2_1259',c*aa(F(129,128))>c+2*aa(F(21259,10000))*K)
ctrl('failed_path_cost_omission_detected',kA>badA and kB>=badB)
ctrl('no_free_probability_one',p<1)
# Wrong native cost on the reverse half-square is a genuine altered-law countercontrol.
ck('original_one_sided_zero_cost',cost(F(3,4),F(1,4))==0)
symmetric=(1+aa(F(1,8))).log();ctrl('symmetric_cost_changes_native_law',symmetric>cost(F(3,4),F(1,4)))
# Exact zero-budget all-action Bellman boundary rational fixtures; proof covers continuum.
def q(s):
 if s<=0:return F(1)
 m=s.numerator//s.denominator;r=s-m;return F(1,2**m)/(1+r)
for n in range(1,49):
 s=F(n,12)
 for j in range(13):
  b=F(j,12);ck(f'zero_budget_stage_{n}_{j}',q(s-b)/(1+b)<=q(s))
 ck(f'zero_budget_attainment_{n}',q(s)==F(1,2**(n//12))/(1+F(n%12,12)))
ctrl('exponential_is_not_nondyadic_exact',aa(q(F(1,2)))<(-c/2).exp())
# Tiny finite trial recursion, independently expanded exhaustive action trees at a fixed state.
actions=[(F(0),F(1,2)),(F(1,2),F(1,2)),(F(1),F(1))]
# Rational cost upper envelope u>=w gives a fully exact comparison model, not actual-log equality.
def u(a,b):return F(0) if a>=b else (b-a)**2/(2*(a+b)*(2-a-b))
def bell(s,n):
 if s<=0:return F(1)
 if n==0:return F(0)
 return max([F(0)]+[-u(a,b)+(1-a)*bell(s,n-1)/2+bell(s-b,n-1)/2 for a,b in actions])
def treevals(s,n):
 if s<=0:return {F(1)}
 if n==0:return {F(0)}
 return {F(0)}|{-u(a,b)+(1-a)*v/2+t/2 for a,b in actions for v in treevals(s,n-1) for t in treevals(s-b,n-1)}
ck('independent_finite_history_tree',bell(F(3,2),2)==max(treevals(F(3,2),2)))
# Repeated-stage elimination directly from finite geometric pass-loop sums.
a,b=F(1,3),F(1,2);stay=(1-a)/2
for n in [1,2,8,32]:
 p_use=sum(stay**j/2 for j in range(n));ntr=sum(stay**j for j in range(n))
 ck(f'geometric_stage_{n}',p_use==(1-stay**n)/(1+a) and ntr==2*(1-stay**n)/(1+a))
ctrl('single_trial_not_whole_stage',F(1,2)!=1/(1+a))
for m in [0,1,2,10,30]:
 rho=F(1,2**m);eps=rho/2
 ck(f'dyadic_strict_probability_{m}',rho*p>eps)
 ck(f'dyadic_ratio_exact_cancellation_{m}',eps/rho==F(1,2))
ctrl('omitted_prelude_survival_changes_cost',F(1,8)*p!=p and aa(F(1,8))*K<K)
# Idle-only problem has arbitrary constant subthreshold fixed points: boundary least selection matters.
ctrl('idle_fixed_point_not_unique',F(1,3)==F(1,3)/2+F(1,3)/2 and F(0)!=F(1,3))
# Released exact two-stage law, independent of the exploratory control grid.
h=F(1,65536);r=F(17,40);t=F(19,10);Al=2*r*t;Bl=t-1
simple=[(1-Al*h,1-Bl*h),(r*t*h,t*h)];ps,ks,bads=law(simple)
D=(Al-Bl)**2/(2*(Al+Bl))+t*(1-r)**2/(2*(1+r));rs=c*aa(h)/(2*ks);limit=c/aa(D)
ck('two_stage_exact_probability',ps==1/(2*(1-(r*t*h)**2)) and ps-F(1,2)==F(104329,1374389534511342))
ck('two_stage_exact_target',sum(b for a,b in simple)==1+h and simple[0][1]<1)
ck('two_stage_rigorous_crossing',rs>aa(F(215223,100000)) and c*aa(1+h)>c+2*aa(F(215223,100000))*ks)
ck('two_stage_asymptotic_rational',D==F(388781,1207200) and limit>aa(F(53807,25000)))
ck('two_stage_stronger_than_mixture',rs>ratio)
ctrl('two_stage_failed_paths_cannot_be_omitted',ks>bads)
# Algebraic expansion coefficients are exact rational limits of log arguments / h.
# log(1+x)/x ->1 is the explicitly cited analytic bridge, not a sampled proof.
import sympy as sy
hh=sy.symbols('h',positive=True)
def ss(x):return sy.Rational(x.numerator,x.denominator)
a1,b1=1-ss(Al)*hh,1-ss(Bl)*hh;a2,b2=ss(r*t)*hh,ss(t)*hh
x1=(b1-a1)**2/(2*(a1+b1)*(2-a1-b1));x2=(b2-a2)**2/(2*(a2+b2)*(2-a2-b2))
ck('first_log_argument_limit',sy.limit(x1/hh,hh,0)==ss((Al-Bl)**2/(4*(Al+Bl))))
ck('second_log_argument_limit',sy.limit(x2/hh,hh,0)==ss(t*(1-r)**2/(4*(1+r))))
ck('reached_stage_multiplier_limits',sy.limit(2/(1+a1),hh,0)==1 and sy.limit(2/((1+a1)*(1+a2)),hh,0)==1)
deps=['explorations/conditional-build/k2474-fixed-confidence-stopping-2026-11-01.md','explorations/conditional-build/k2480-scheduled-stopping-preludes-2026-11-01.md','lab/process/k2471-sharp-stopping-coefficient.json']
rep={'result':'K2483','checks':checks,'contrary_controls':controls,'witness':{'A':[[str(a),str(b)] for a,b in A],'B':[[str(a),str(b)] for a,b in B],'P_A':str(pA),'P_B':str(pB),'K_A':str(kA),'K_B':str(kB),'fair_bits':bits,'alpha':str(alpha),'P_mix':str(p),'strict_probability_excess':str(p-F(1,2)),'K_mix':str(K),'ratio_interval':str(ratio),'certified_lower_bound':'21259/10000'},'two_stage':{'controls':[[str(a),str(b)] for a,b in simple],'h':str(h),'P':str(ps),'K':str(ks),'ratio_interval':str(rs),'limit_denominator':str(D),'limiting_lower_bound_interval':str(limit),'certified_finite_lower_bound':'215223/100000'},'evidence_kinds':{'universal':'written minimal-supersolution and zero-budget proofs, not finite-grid inference','exact':'rational probabilities, finite trees and boundary cases','interval':'Arb256 actual logarithmic costs and strict crossing'},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
p=ROOT/'lab/process/k2483-adaptive-stopping-bellman.json'
if '--write' in sys.argv:p.write_text(json.dumps(rep,indent=2,sort_keys=True)+'\n')
else:ck('saved_report_reproduces',json.loads(p.read_text())==rep)
print(json.dumps({'result':'PASS','checks':len(checks),'controls':len(controls),'witness':rep['witness'],'two_stage':rep['two_stage']}))
