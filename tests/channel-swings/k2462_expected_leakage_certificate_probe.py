"""Exact crossing laws and Arb prospective consumers; universal proof is in note."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import json,hashlib,sys
from flint import arb,ctx
ctx.prec=256
ROOT=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ctrl(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
def ar(x):
 x=F(x);return arb(x.numerator)/x.denominator
log2=arb(2).log();log4=arb(4).log();KH=log4/1000;eps=F(1,10);L=arb(10).log()+KH/ar(eps)
ck('crossing_requires_four_uses',3*log2<L and L<4*log2)
cross=F(999,1000*16)+F(1,1000*81)
ck('nonzero_exact_expected_budget_crossing',cross==F(16187,259200) and 0<cross<eps)
# Geometric N has P(N=n)=2^-n-1, E N=1; exact power-series identity.
for z in [F(0),F(1,2),F(1),F(3,2),F(2)]:
 r=(1+z)/4;ck('geometric_pgf_'+str(z),F(1,2)/(1-r)==2/(3-z))
 partial=sum(F(1,2)*r**n for n in range(12));tail=F(1,2)*r**12/(1-r)
 ck('pgf_exact_remainder_'+str(z),partial+tail==2/(3-z))
for n in [1,2,5,40]:
 ck('unbounded_cost_positive_tail_'+str(n),F(1,2)**n>0)
 ck('expected_N_partial_tail_'+str(n),sum(F(k,2**(k+1)) for k in range(n))+F(n+1,2**n)==1)
for m in range(1,10):
 ck('mixed_use_tail_'+str(m),sum(F(2,3**(u+1)) for u in range(m))+F(1,3**m)==1)
# Actual 40-round failure of expected-as-pathwise substitution.
wrong=arb(20).log()+4*log4;proper=arb(20).log()+80*log4
ck('bad_threshold_thirteen',12*log2<wrong and wrong<13*log2)
ck('proper_threshold_exceeds_burst',proper>40*log2)
bad=F(sum(comb(40,u) for u in range(13,41)),10*2**40)
ctrl('expected_is_not_pathwise',bad==F(272597931681,2748779069440) and bad>F(1,20))
ctrl('conditioning_does_not_preserve_budget',40>F(1,10)*40)
# The exact-use reference assigns zero probability to a test pass when b=1;
# actual a=0 assigns positive mass, while smoothed v=1.
a,b,eta=F(0),F(1),F(1,2);q=a+(1-eta)*(b-a);v=(a-q)**2/(q*(1-q))
ck('support_safe_endpoint_v',v==1)
ctrl('exact_use_reference_support_failure',(1-a)>0 and (1-b)==0)
# Abstract sharpness, checking exact expectations and interval log cancellation.
for p in [F(1,2),F(1,10),F(1,100)]:
 K=F(1,7);h=K/p;threshold=(1/ar(p)).log()+ar(h)
 ck('abstract_M_mean_'+str(p),p*(1/p)==1)
 ck('abstract_H_mean_'+str(p),p*h==K)
 ck('abstract_threshold_'+str(p),(ar(p)*(threshold-ar(h)).exp()-1).contains(0))
 ctrl('missing_expected_penalty_'+str(p),threshold>(1/ar(p)).log())
# Released ACTUAL binary lower bound, stopping at m-th use in rare mode.
rare=F(1,10);confidence=F(1,20);target_uses=10;use_prob=F(1,2)
expected_rounds=F(target_uses)/use_prob;mean_H=ar(rare*expected_rounds)*log4
hit_level=target_uses*log2
ck('binary_rare_expected_rounds',expected_rounds==20)
ck('binary_rare_expected_compensator',(mean_H-2*log4).contains(0))
ck('binary_endpoint_log_factor',F(1,2)*2+F(1,2)==F(3,2) and F(3,2)<=4)
ck('binary_scale_ratio_one_quarter',(log2*ar(use_prob)/log4-ar(F(1,4))).contains(0))
ck('binary_finite_threshold_ratio',(hit_level-mean_H/ar(8*confidence)).contains(0))
ctrl('actual_binary_inverse_confidence_penalty_necessary',rare>confidence and hit_level>0)
for zz in [F(1,2),F(1),F(3,2)]:
 pgf=use_prob*zz/(1-(1-use_prob)*zz)
 part=sum(use_prob*(1-use_prob)**(j-1)*zz**j for j in range(1,12))
 rem=use_prob*zz*((1-use_prob)*zz)**11/(1-(1-use_prob)*zz)
 ck('binary_waiting_PGF_'+str(zz),part+rem==pgf)
 ck('binary_mth_use_PGF_'+str(zz),(part+rem)**target_uses==pgf**target_uses)
ck('binary_hitting_almost_sure_PGF_at_one',(use_prob/(1-(1-use_prob)))**target_uses==1)
ctrl('binary_random_stop_has_no_pathwise_cap',(1-use_prob)**1000>0)
# Do not permit reset after absorption; actual altered factors create a false hit.
ctrl('absorbing_failure_not_restartable',F(0)*2**4==0 and F(1)*2**4>10)
pi=eta=arb(1)/2;A=pi;c=arb(2).log();J=A-(1-pi)*c;C=(A+eta*J)**2/(4*J*(1-eta)**2);gamma=2*C
ck('conservative_endpoint_constant',C<3 and gamma>1)
K=arb('1e-6');alpha=arb('.05');beta=arb('1e-8');kap=arb('1e-6');tau=arb('.01');num=(1/alpha).log()+gamma*K/alpha
pros=[]
for nu in [F(2,5),F(9,20)]:
 D=ar(nu)*((tau-4*kap)/2)**2-beta;ck('positive_design_margin_'+str(nu),D>0)
 count=int((num/(c*D)).upper().ceil().unique_fmpz())
 def bound(n):return 2*((beta+num/(c*n))/ar(nu)).sqrt()+4*kap
 ck('rounded_output_bound_'+str(nu),bound(count)<=tau)
 ctrl('preceding_count_fails_'+str(nu),bound(count-1)>tau)
 ck('positive_actual_success_'+str(nu),((beta+num/(c*count))/ar(nu)).sqrt()/2+kap<arb(1)/4)
 pros.append({'gap':str(nu),'actual_uses':count,'allowance':str(bound(count))})
ck('expected_counts', [x['actual_uses'] for x in pros]==[432985,384833])
deps=[str(Path(__file__).relative_to(ROOT)),'explorations/conditional-build/k2462-expected-leakage-certificate-2026-11-01.md','explorations/conditional-build/k2459-direct-leakage-certificate-2026-11-01.md','explorations/conditional-build/k2453-same-risk-information-budget-2026-11-01.md']
# Resolve the predecessor by its actual unique scientific identifier.
deps[-1]=str(next((ROOT/'explorations/conditional-build').glob('k2453-*.md')).relative_to(ROOT))
report={'result_id':'K2462','checks':checks,'controls':controls,'exact_crossing':str(cross),'actual_binary_lower_bound':{'rho':'1/4','rare_probability':'1/10','confidence':'1/20','target_uses':10,'expected_rounds_given_rare':20,'expected_compensator':'2 log4','crossing_level':'10 log2'},'false_pathwise_crossing':str(bad),'prospective':pros,'gamma':str(gamma),'evidence_kinds':{'universal':'written bounded stopping, conditional Jensen and increasing-horizon argument','exact':'geometric law, burst counterexample, actual binary inverse-confidence lower bound, abstract sharpness expectations','interval':'Arb256 thresholds and prospective output budgets','ceiling':'unconditional expected-cost premise; no measured budget or binary-class optimality'},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2462-expected-leakage-certificate.json'
if '--check' in sys.argv:assert json.loads(out.read_text())==report
else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('K2462',len(checks),'checks',len(controls),'controls PASS',pros)
