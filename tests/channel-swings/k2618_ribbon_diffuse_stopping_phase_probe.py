#!/usr/bin/env python3
"""Retained exact ribbon, new phase endpoints and original finite policies.
The retained coefficient tables are hash-pinned; universal transfers are analytic.
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
a,b,y,v,r=s.symbols('a b y v r',real=True)
prior=json.loads((root/'lab/process/k2567-stopping-family-structure.json').read_text())
ck('retained_ribbon_report_pin',hashlib.sha256((root/'lab/process/k2567-stopping-family-structure.json').read_bytes()).hexdigest()=='c8329c5ccabf1d0b07aa55fbbdd0bc37f19f2a85c59f8a03d1f9b6d9396a950f')
tables=prior['certificates']
ck('table_content_digest',hashlib.sha256(json.dumps(tables,sort_keys=True,separators=(',',':')).encode()).hexdigest()==prior['coefficient_digest'])
for key in ['numerator','denominator','barrier_denominator']:
 ck('retained_positive_coefficients_'+key,min(map(F,tables[key]['coefficients']))>0)
bn=list(map(F,tables['barrier_numerator']['coefficients']))
ck('retained_barrier_origin_only_zero',bn[0]==0 and min(bn[1:])>0)
k0=min(map(F,tables['numerator']['coefficients']))/max(map(F,tables['denominator']['coefficients']))
ck('exact_slope_constant',k0==F(prior['k0']) and 2*k0<F(5,16))
v0=F(51,98)
q=2*s.sqrt(1+2*v)-2-v;tau=s.log(s.sqrt(1+2*v)-1)-3*s.log(3-s.sqrt(1+2*v))
ck('actual_clock_derivative',s.simplify(s.diff(tau,v)*q-1)==0)
ck('q_floor',q.subs(v,s.Rational(51,98))==s.Rational(33,98))
rr=2/s.sqrt(1+2*v)-1
ck('action_floor',rr.subs(v,s.Rational(51,98))==s.Rational(2,5))
poly=3-6*r-r*r
ck('D_lower_factor',poly.subs(r,s.Rational(2,5))==s.Rational(11,25))
ck('D_lower_exact',s.Rational(33,98)*s.Rational(11,25)/8==s.Rational(363,19600))
ck('D_factor_decreasing',s.diff(poly,r)==-6-2*r)
qr=(1-r)*(3*r+1)/(2*(1+r)**2);Dr=qr*poly/8
ck('D_upper_gap_positive_formula',s.cancel(s.Rational(3,16)-Dr-r*(6+25*r-16*r*r-3*r**3)/(16*(1+r)**2))==0)
# On r in[0,2/5], numerator parenthesis >=6-16(2/5)^2-3(2/5)^3>0.
ck('D_upper_uniform',6-16*F(2,5)**2-3*F(2,5)**3>0)
ck('switch_D_match',Dr.subs(r,0)==s.Rational(3,16))
ck('switch_r_match',rr.subs(v,s.Rational(3,2))==0)
ck('switch_q_match',q.subs(v,s.Rational(3,2))==s.Rational(1,2))
ck('switch_q_derivative_match',s.diff(q,v).subs(v,s.Rational(3,2))==0)
ct('lower_floor_not_certified_by_same_ribbon',F(1,2)<F(51,98))
ct('necessary_boundary_is_below_floor',3*s.Rational(1,16)<s.Rational(51,98)**2)
# All new transcendental consumers use outward Arb arithmetic and rational roots.
def ab(x):
    x=F(x);return arb(x.numerator)/x.denominator
def qa(vv):return 2*(1+2*vv).sqrt()-2-vv
def ta(vv):
    z=(1+2*vv).sqrt();return (z-1).log()-3*(3-z).log()
def interval(lo,hi):
    mid=(lo+hi)/2;rad=(hi-lo)/2
    return arb(ab(mid),ab(rad))
def invert_clock(target,lo=F(1,4),hi=F(3,2),steps=150):
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
    ck('endpoint_strict_phase_gain_'+str(score),ll>ab(F(7,5)) and budget>0 and budget<ab(score/2) and prob<1)
    ends.append({'score':str(score),'theta_rational_bracket':[str(lo),str(hi)],'theta_Arb':str(theta),'lambda_Arb':str(ll),'budget_Arb':str(budget),'success_Arb':str(prob)})
# Fixed rational7/5 is strictly inside the enlarged half-score region.
score=F(1,2);ll=F(7,5);theta=1/ll
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
variable=[]
for inv_t in [64,128,256]:
    step=F(1,inv_t);remain=score;P=F(1);trials=F(0);cost=arb(0);stages=[]
    while remain>0:
        vl,vh=invert_clock(ta(ab(theta))-ab(remain),steps=100)
        vv=interval(vl,vh);rr=2/(1+2*vv).sqrt()-1;dv=qa(vv)*(3-6*rr-rr*rr)/8
        proposed=float(ab(step)/dv.sqrt())
        bb=min(remain,F(max(1,round(proposed*10**12)),10**12))
        ratio=F(round(float(rr.mid())*10**12),10**12);aa=bb*ratio
        assert 0<=aa<=bb
        P/=1+aa;trials+=2*P;cost+=2*ab(P)*(1+ab((bb-aa)**2/(2*(aa+bb)*(2-aa-bb)))).log()
        stages.append([str(aa),str(bb)]);remain-=bb
    gap=V-ab(P)+ab(ll)*cost
    ck('variable_mesh_original_gap_'+str(inv_t),gap>0)
    variable.append({'t':str(step),'stages':stages,'resource':str(trials),'success':str(P),'leakage_Arb':str(cost),'gap_Arb':str(gap),'resource_times_gap_illustration':str(ab(trials)*gap)})
ct('unweighted_cost_wrong',s.cancel(2/(1+a)+2/((1+a)*(1+b))-4)!=0)
ct('upper_instability_not_in_phase',F(9,5)>1/F(51,98)-F(0) or ta(ab(F(5,9)))-ta(ab(v0))<ab(score))
# Both are strict certified comparisons with the inherited necessary curve.
vc=arb(3).sqrt()/4
necessary_lo,necessary_hi=invert_clock(ta(vc)+ab(score))
necessary_lambda=1/interval(necessary_lo,necessary_hi)
ck('nonempty_remaining_phase_gap',necessary_lambda>1/interval(*invert_clock(ta(ab(v0))+ab(score))))
report={'result':'K2618','checks':checks,'contrary_controls':controls,'output_floor':str(v0),'k0':str(k0),'D_lower':'363/19600','phase_endpoints':ends,'finite_policy_consumers':finite,'variable_mesh_consumers':variable,'halfscore_necessary_lambda_Arb':str(necessary_lambda),'evidence_kind':'hash-bound retained exact ribbon coefficients and symbolic transfer bounds; outward interval endpoints and actual rational policy costs; universal flow and adaptive resource proof in note','ceiling':'sufficient phase and leading resource asymptotic only; no sharp boundary, higher corrector or physical law','provenance':{f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in ['lab/process/k2567-stopping-family-structure.json','explorations/conditional-build/k2567-stopping-family-structure-2026-11-05.md','explorations/conditional-build/k2602-continuum-stopping-resource-law-2026-11-06.md']}}
out=root/'lab/process/k2618-ribbon-diffuse-stopping-phase.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'FAIL saved report replay'
print(json.dumps({'result':'K2618','checks':len(checks),'controls':len(controls),'finite_policies':len(finite)+len(variable),'status':'pass'}))
