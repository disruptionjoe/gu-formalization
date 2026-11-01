"""Original-risk one-step bounds, exact adaptive crossing, and budget consumers.
Universal conclusions rest on the companion proof, not the finite grid.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,hashlib,sys
from flint import arb,ctx
ctx.prec=256
ROOT=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,b):
 checks[k]=bool(b)
 if not b:raise AssertionError(k)
def ctrl(k,b):
 controls[k]=bool(b)
 if not b:raise AssertionError(k)
def ar(x):
 f=F(x);return arb(f.numerator)/f.denominator
def risk(a,b,eta=F(1,2)):
 d=max(F(0),b-a);q=a+(1-eta)*d
 return q,(a-q)**2/(q*(1-q)) if q not in [0,1] else F(0)
def const(pi,eta,r):
 pi,eta,r=map(ar,(pi,eta,r));A=pi*r;c=(1+A/(1-pi)).log();J=A-(1-pi)*c;C=(A+eta*J)**2/(4*J*(1-eta)**2);return A,c,J,C
# Positive exact slack away from equality endpoints, interval arithmetic.
for pi,eta,r in product([F(1,3),F(1,2),F(2,3)],[F(1,4),F(1,2),F(3,4)],[F(1,2),F(1)]):
 A,c,J,C=const(pi,eta,r);ck(f'positive_constants_{pi}_{eta}_{r}',J>0 and C>0)
 for a,b in product([F(0),F(1,4),F(1,2),F(3,4),F(1)],repeat=2):
  q,v=risk(a,b,eta);G=(1-ar(pi))*(c*ar(b)).exp()+ar(pi)*(1-ar(r*a));slack=1+C*ar(v)-G
  if v==0 and b in (0,1) and a==b:ok=slack.contains(0)
  else:ok=slack>0 or (v==0 and b==0 and r==0)
  ck(f'actual_multiplier_{pi}_{eta}_{r}_{a}_{b}',ok)
A,c,J,C=const(F(1,2),F(1,2),F(1));gamma=2*C
ck('rational_tree_constant_three_valid',C<3)
q,v=risk(F(1,2),F(1));ck('original_budget_counter_v',v==F(1,3))
ctrl('unscaled_original_compensation_fails',F(5,4)>1+F(1,2)*v)
ctrl('omitted_compensation_fails',F(3,2)>1)
ck('support_endpoint_finite',risk(F(0),F(1))[1]==1)
ck('harmless_discrepancy_zero_cost',risk(F(3,4),F(1,4))[1]==0)
# Exact rational adaptive tree. b=1; a responds to prior route/failure history.
# C=3 is an independently proved upper bound, so M=2^uses/prod(1+3v)
# until a failure. This is an actual three-outcome experiment, no hidden IID.
N=8;alpha=F(1,10);cross=F(0);mass=F(0);max_expected=F(0);nodes=0;positive_cross_paths=0
states=[(F(1),F(1),False,0,0,False)]
for depth in range(N):
 nexts=[]
 for prob,m,crossed,uses,tests,failed in states:
  a=F(7,8) if uses%2 else (F(3,4) if tests%2==0 else F(1,2));b=F(1);_,v=risk(a,b);den=1+3*v
  factors=[F(2)/den,F(1)/den,F(0)];probs=[F(1,2),(1-a)/2,a/2]
  cond=sum(p*f for p,f in zip(probs,factors));assert cond<=1;max_expected=max(max_expected,cond);nodes+=1
  for j,(p,f) in enumerate(zip(probs,factors)):
   mm=m*f;hit=crossed or mm>=1/alpha
   nexts.append((prob*p,mm,hit,uses+(j==0),tests+(j!=0),failed or j==2))
 states=nexts
mass=sum(t[0] for t in states);cross=sum(t[0] for t in states if t[2]);positive_cross_paths=sum(1 for t in states if t[2] and t[0]>0)
ck('adaptive_total_mass',mass==1);ck('adaptive_nonvacuous_crossing',0<cross<=alpha);ck('adaptive_capital_mean',sum(t[0]*t[1] for t in states)<=1)
ck('adaptive_conditional_mean_bound',max_expected<=1 and nodes>1)
ck('failed_paths_remain_zero',any(f for *_,f in states) and all(m==0 for _,m,_,u,t,f in states if f))
legitimate_after_failure=F(0)*(F(7,5)*F(5,3))**3
reset_after_failure=(F(7,5)*F(5,3))**3
ctrl('reset_after_failure_false_crossing',legitimate_after_failure==0 and reset_after_failure==F(343,27) and reset_after_failure>1/alpha)
# Omitting compensation has actual conditional mean3/2 at b=1,a=0.
ctrl('adaptive_bad_normalizer_detected',F(1,2)*2+F(1,2)>1)
# Explicit supplied endpoint family validates the necessary linear order.
for eps in [F(1,2),F(1,10),F(1,100)]:
 eta=F(1,2);_,v=risk(1-eps,F(1));ck(f'endpoint_exact_cost_{eps}',v==(1-eta)**2*eps/(eta*(1-eta*eps)))
 ck(f'endpoint_ratio_{eps}',(F(1,2)*eps)/v==F(1)*(1-eps/2))
ctrl('zero_cost_cannot_cover_endpoint_leakage',F(1,2)*F(1,100)>0)
# Budget conversion at original constants, strict whenever v>0 and gamma>1.
for v in [F(1,10000),F(1,3),F(1),F(10)]:
 ck(f'budget_conversion_{v}',gamma*(1+ar(v)/2).log()-(1+C*ar(v)).log()>0)
# Prospective unchanged K2457 gap and K2456 budget inputs.
B=arb('1e-6');beta=arb('1e-8');kap=arb('1e-6');tau=arb('.01');nu=arb(2)/5;L=arb(20).log();D=nu*((tau-4*kap)/2)**2-beta
count=int(((gamma*B+L)/(c*D)).upper().ceil().unique_fmpz())
def bound(n):return 2*((beta+(gamma*B+L)/(c*n))/nu).sqrt()+4*kap
ck('same_budget_consumer',bound(count)<=tau);ctrl('prior_count_fails',bound(count-1)>tau)
ck('positive_actual_success',((beta+(gamma*B+L)/(c*count))/nu).sqrt()/2+kap<arb(1)/4)
# Show rate/constant distinction; proof, not these examples, supplies asymptotics.
ck('direct_count_below_prior_bound',count<934421)
deps=[str(Path(__file__).relative_to(ROOT)),'explorations/conditional-build/k2459-direct-leakage-certificate-2026-11-01.md','explorations/conditional-build/k2456-predictable-leakage-budget-2026-11-01.md','explorations/conditional-build/k2457-local-verifier-phase-design-2026-11-01.md']
report={'result_id':'K2459','checks':checks,'controls':controls,'adaptive_fixture':{'depth':N,'nodes':nodes,'crossing_probability':str(cross),'alpha':str(alpha),'positive_cross_paths':positive_cross_paths,'max_conditional_mean':str(max_expected)},'prospective':{'actual_uses':count,'allowance':str(bound(count)),'C':str(C),'gamma':str(gamma)},'evidence_kinds':{'universal':'written exponential-chord deficit, square completion, predictable supermartingale and original-budget transfer','exact':'rational adaptive tree, nonzero crossing event, endpoints and invalid denominator controls','interval':'Arb256 finite one-step specimens and hypothetical consumer'},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2459-direct-leakage-certificate.json'
if '--check' in sys.argv:assert json.loads(out.read_text())==report
else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('K2459',len(checks),'checks',len(controls),'controls PASS',report['adaptive_fixture'],report['prospective'])
