#!/usr/bin/env python3
"""Exact new output barrier, interval phase endpoints, original finite policies.
The unchanged bivariate generator certificate is reused by exact dependency hashes.
"""
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F
from math import comb
import sympy as s
from flint import arb,ctx
root=Path(__file__).resolve().parents[2]
ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();ctx.prec=256
checks=[];controls=[]
def ck(n,v):
    assert bool(v),'FAIL '+n
    checks.append(n)
def ct(n,v):
    assert bool(v),'FAIL contrary '+n
    controls.append(n)
a,b,y,v=s.symbols('a b y v',real=True);D=2*(a+b)*(2-a-b);N=D+(b-a)**2
wa=s.cancel(s.diff(N,a)/N-s.diff(D,a)/D);xx=(b-a)**2/D
U=s.factor((-2*(1+a)*wa+2*xx).subs(a,2*b/5))
expected=1-2*(3421*b*b-6095*b+2350)/(7*(7*b-10)*(89*b-140))
ck('original_log_upper_barrier',s.cancel(U-expected)==0)
num=173339*b*b-443380*b+275900
ck('barrier_derivative_exact',s.cancel(s.diff(U,b)-30*num/(7*(7*b-10)**2*(89*b-140)**2))==0)
p=s.Poly(num.subs(b,y/2),y)
bern=[sum(p.nth(j)*s.Rational(comb(i,j),comb(2,j)) for j in range(i+1)) for i in range(3)]
ck('new_barrier_Bernstein_positive',bern==[275900,165055,s.Rational(390179,4)] and all(c>0 for c in bern))
ck('independent_Bernstein_reconstruction',s.expand(sum(bern[i]*comb(2,i)*y**i*(1-y)**(2-i) for i in range(3))-p.as_expr())==0)
v0=F(16119,17381);ck('exact_output_floor',U.subs(b,s.Rational(1,2))==s.Rational(v0.numerator,v0.denominator))
ck('floor_above_zero_score_root_barrier',s.Rational(v0.numerator,v0.denominator)>s.Rational(51,98)) # r=2/5 gives v=51/98
ck('floor_below_one',0<v0<1)
ck('strict_uniform_extension',v0+F(1,4)<F(5,4))
q=2*s.sqrt(1+2*v)-2-v;tau=s.log(s.sqrt(1+2*v)-1)-3*s.log(3-s.sqrt(1+2*v))
ck('actual_clock_derivative',s.simplify(s.diff(tau,v)*q-1)==0)
ck('flow_monotone_and_concave_below_switch',s.simplify(s.diff(q,v,2))==-2/(2*v+1)**s.Rational(3,2))
prior=json.loads((root/'lab/process/k2561-higher-budget-stopping.json').read_text())
for f,digest in prior['dependencies'].items():ck('unchanged_certificate_dependency_'+f,hashlib.sha256((root/f).read_bytes()).hexdigest()==digest)
gen=prior['certificates']['increasing_generator']
ck('reused_gamma_from_exact_bounds',2*s.Rational(gen['minimum_numerator'])/s.Rational(gen['maximum_denominator'])==s.Rational(prior['generator_increment']))
# All new transcendental consumers use outward Arb arithmetic and rational roots.
def ab(x):
    x=F(x);return arb(x.numerator)/x.denominator
def qa(vv):return 2*(1+2*vv).sqrt()-2-vv
def ta(vv):
    z=(1+2*vv).sqrt();return (z-1).log()-3*(3-z).log()
def interval(lo,hi):
    mid=(lo+hi)/2;rad=(hi-lo)/2
    return arb(ab(mid),ab(rad))
def invert_clock(target,lo=F(3,4),hi=F(3,2),steps=150):
    assert ta(ab(lo))<target and ta(ab(hi))>target
    for _ in range(steps):
        mid=(lo+hi)/2;value=ta(ab(mid))
        if value<target:lo=mid
        elif value>target:hi=mid
        else:raise AssertionError('FAIL unresolved root sign')
    return lo,hi
ends=[]
for score in [F(1,2),F(1,4)]:
    target=ta(ab(v0))+ab(score);lo,hi=invert_clock(target)
    theta=interval(lo,hi);ll=1/theta;prob=qa(ab(v0))/qa(theta);budget=theta*prob-ab(v0)
    ck('endpoint_bracket_'+str(score),ta(ab(lo))<target<ta(ab(hi)))
    ck('endpoint_strict_phase_gain_'+str(score),ll>ab(F(4,5)) and budget>0 and budget<ab(score/2) and prob<1)
    ends.append({'score':str(score),'theta_rational_bracket':[str(lo),str(hi)],'theta_Arb':str(theta),'lambda_Arb':str(ll),'budget_Arb':str(budget),'success_Arb':str(prob)})
# Fixed rational17/20 is strictly inside the enlarged half-score region.
score=F(1,2);ll=F(17,20);theta=1/ll
ck('new_rational_multiplier_admitted',ta(ab(theta))-ta(ab(v0))>ab(score))
u_lo,u_hi=invert_clock(ta(ab(theta))-ab(score));u=interval(u_lo,u_hi);V=ab(ll)*u
finite=[]
for n in [16,32,64]:
    h=score/n;P=F(1);trials=F(0);cost=arb(0);actions=[]
    for i in range(n):
        vl,vh=invert_clock(ta(ab(theta))-ab(score-i*h),steps=100)
        rr=2/(1+2*interval(vl,vh)).sqrt()-1
        # Rounding creates actual rational admissible policies, not an optimizer assertion.
        ratio=F(round(float(rr.mid())*10**10),10**10);aa=h*ratio
        assert 0<=aa<=h
        actions.append(str(aa));P/=1+aa;trials+=2*P
        logarg=1+(h-aa)**2/(2*(aa+h)*(2-aa-h));cost+=2*ab(P)*ab(logarg).log()
    value=ab(P)-ab(ll)*cost;gap=V-value
    ck('finite_policy_strict_gap_'+str(n),gap>0)
    finite.append({'score':str(score),'lambda':str(ll),'n':n,'b':str(h),'a':actions,'success':str(P),'expected_positive_trials':str(trials),'leakage_Arb':str(cost),'dual_Arb':str(value),'gap_Arb':str(gap),'n_gap_illustration':str(n*gap)})
# Preserve the actual predecessor contrary data: the generator is not global.
counter=prior['certificates']['intermediate_output_counterexample']
ct('known_counterexample_below_new_domain',F(counter['output_upper'])<v0)
ct('known_hybrid_not_in_new_phase',F(19,10)>1/v0)
# Original weighted cost cannot be replaced by an unweighted sum.
a1,a2,w1,w2=s.symbols('a1 a2 w1 w2',positive=True)
ct('unweighted_cost_wrong',s.cancel(2*w1/(1+a1)+2*w2/((1+a1)*(1+a2))-2*(w1+w2))!=0)
xactual=F(9,100)/(2*F(7,10)*F(13,10))
ct('actual_endpoint_log_upper_bound_is_strict',2*ab(xactual)-2*(1+ab(xactual)).log()>0)
report={'result':'K2612','checks':checks,'contrary_controls':controls,'output_floor':str(v0),'new_barrier_Bernstein':list(map(str,bern)),'reused_generator_increment':prior['generator_increment'],'phase_endpoints':ends,'finite_policy_consumers':finite,'evidence_kind':'exact univariate barrier; unchanged hash-pinned bivariate certificate reused; certified Arb clock endpoints and original rational finite-policy costs; universal adaptive theorem in note','ceiling':'sufficient phase, not sharp boundary or new higher resource correctors, no physical law','provenance':{f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in ['lab/process/k2561-higher-budget-stopping.json','explorations/conditional-build/k2561-higher-budget-stopping-2026-11-05.md']}}
out=root/'lab/process/k2612-extended-diffuse-stopping-phase.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'FAIL saved report replay'
print(json.dumps({'result':'K2612','checks':len(checks),'controls':len(controls),'finite_policies':len(finite),'status':'pass'}))
