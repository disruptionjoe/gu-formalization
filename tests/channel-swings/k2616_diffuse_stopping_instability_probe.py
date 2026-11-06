#!/usr/bin/env python3
"""Original-log local defect and certified finite atom/tail consumers. No global phase claim."""
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F
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
r,b=s.symbols('r b',positive=True);a=s.symbols('a',real=True)
alpha=(1-r)**2/(4*(1+r));beta=(1+r)/2
# Original log argument is alpha*b/(1-beta*b), not a substituted cost model.
xx=(b-r*b)**2/(2*(r*b+b)*(2-r*b-b))
ck('original_log_argument',s.cancel(xx-alpha*b/(1-beta*b))==0)
xx=s.cancel(xx)
g=2*alpha;B=2*alpha*beta-alpha**2;T=2*alpha*beta**2-2*alpha**2*beta+2*alpha**3/3
for i,expr in enumerate([g,B,T],1):
    ck('log_coefficient_'+str(i),s.simplify(s.diff(2*s.log(1+xx),b,i).subs(b,0)/s.factorial(i)-expr)==0)
v=2/(1+r)**2-s.Rational(1,2);q=s.factor(r*v+g);qpp=s.factor(1/s.diff(v,r))
ck('generator_stationarity',s.cancel(v+s.diff(g,r))==0)
ck('strict_action_convexity',s.diff(g,r,2).factor()==4/(1+r)**3)
D=s.factor(B-q*r/2);rho=s.factor(-s.diff(B,r)/s.diff(g,r,2))
E=s.factor(T-s.diff(B,r)**2/(2*s.diff(g,r,2))-(qpp*q*q+r*r*q)/6)
ck('actual_quadratic_defect',s.cancel(D-q*(3-6*r-r*r)/8)==0)
ck('action_ratio_correction',s.cancel(rho+(r-1)*(3*r**3+11*r*r+17*r+1)/32)==0)
rc=2*s.sqrt(3)-3;vc=s.sqrt(3)/4;Ec=(10309-5949*s.sqrt(3))/192;Dp=(47*s.sqrt(3)-81)/2
ck('critical_input',s.simplify(v.subs(r,rc)-vc)==0)
ck('critical_D_zero',s.simplify(D.subs(r,rc))==0)
ck('critical_cubic',s.simplify(E.subs(r,rc)-Ec)==0)
ck('critical_D_derivative',s.simplify((s.diff(D,r)/s.diff(v,r)).subs(r,rc)-Dp)==0)
ck('positive_cubic_exact',10309**2-3*5949**2==103678 and Ec>0)
ck('positive_D_derivative_exact',3*47**2-81**2==66 and Dp>0)
t=s.symbols('t',positive=True);gain=Dp*t*t-Ec*t**3;tstar=2*Dp/(3*Ec)
ck('cubic_optimal_atom_stationarity',s.simplify(s.diff(gain,t).subs(t,tstar))==0)
ck('cubic_gain_coefficient',s.simplify(gain.subs(t,tstar)-4*Dp**3/(27*Ec**2))==0)
ct('critical_equality_not_local_instability',Ec>0)
ct('frozen_action_misses_cubic_optimization',s.simplify((T-(qpp*q*q+r*r*q)/6-E).subs(r,rc))>0)
# Rigorous flow roots and actual rational finite schedules. No sampled ODE is certified.
def ab(x):
    x=F(x);return arb(x.numerator)/x.denominator
def ta(vv):
    z=(1+2*vv).sqrt();return (z-1).log()-3*(3-z).log()
def qa(vv):return 2*(1+2*vv).sqrt()-2-vv
def interval(lo,hi):return arb(ab((lo+hi)/2),ab((hi-lo)/2))
def invert(target,lo=F(1,4),hi=F(4,5),steps=110):
    assert ta(ab(lo))<target<ta(ab(hi))
    for _ in range(steps):
        mid=(lo+hi)/2;tm=ta(ab(mid))
        if tm<target:lo=mid
        elif tm>target:hi=mid
        else:raise AssertionError('FAIL unresolved root sign')
    return lo,hi
ends=[];vca=arb(3).sqrt()/4
for S in [F(1,4),F(1,2)]:
    lo,hi=invert(ta(vca)+ab(S));theta=interval(lo,hi);ll=1/theta
    ck('critical_flow_bracket_'+str(S),ta(ab(lo))<ta(vca)+ab(S)<ta(ab(hi)))
    ck('critical_below_small_score_threshold_'+str(S),ll<4/arb(3).sqrt())
    ends.append({'score':str(S),'theta_bracket':[str(lo),str(hi)],'lambda_local_Arb':str(ll)})
# Direct first-action minimization by derivative bisection at the bracketed input.
def wa(aa,bb):
    dd=2*(aa+bb)*(2-aa-bb);nn=dd+(bb-aa)**2
    dda=4-4*(aa+bb);nna=dda+2*(aa-bb)
    return nna/nn-dda/dd
ck("exact_zero_cost_endpoint_derivative",s.cancel(wa(b,b))==0)
neutral=[]
for bb,ul,uh in [(F(1,10),F(42,100),F(421,1000)),(F(1,2),F(367,1000),F(368,1000))]:
    signs=[]
    for uu in [ul,uh]:
        ck("neutral_action_endpoint_signs_"+str((bb,uu)),ab(uu)+2*wa(ab(0),ab(bb))<0 and uu>0)
        alo=F(0);ahi=bb
        for _ in range(110):
            mid=(alo+ahi)/2;der=ab(uu)+2*wa(ab(mid),ab(bb))
            if der<0:alo=mid
            elif der>0:ahi=mid
            else:raise AssertionError('FAIL neutral action root sign')
        aa=interval(alo,ahi);bv=ab(bb)
        exactF=(1+aa)*ab(uu)+2*(1+(bv-aa)**2/(2*(aa+bv)*(2-aa-bv))).log()
        hl,hh=invert(ta(ab(uu))+bv);defect=exactF-interval(hl,hh)
        signs.append(defect)
    ck('finite_atom_neutral_bracket_'+str(bb),signs[0]<0 and signs[1]>0)
    neutral.append({'score':str(bb),'input_bracket':[str(ul),str(uh)],'left_defect_Arb':str(signs[0]),'right_defect_Arb':str(signs[1]),'ceiling':'at least one neutral input by continuity; not global uniqueness or complete phase'})
finite=[]
for ll in [F(9,5),F(2)]:
    S=F(1,2);atom=F(1,5);ulo,uhi=invert(ta(ab(1/ll))-ab(S));u=interval(ulo,uhi);V=ab(ll)*u
    ck('initial_input_below_critical_'+str(ll),u<vca)
    alo=F(0);ahi=atom
    for _ in range(70):
        mid=(alo+ahi)/2;der=u+2*wa(ab(mid),ab(atom))
        if der<0:alo=mid
        elif der>0:ahi=mid
        else:raise AssertionError('FAIL unresolved action sign')
    aa=F(round(float(ab((alo+ahi)/2).mid())*10**10),10**10)
    for n in [64,256]:
        h=(S-atom)/n;acts=[aa];scores=[atom]
        for i in range(n):
            remaining=S-atom-i*h
            vl,vh=invert(ta(ab(1/ll))-ab(remaining),steps=70)
            ratio=2/(1+2*interval(vl,vh)).sqrt()-1
            action=F(round(float((ab(h)*ratio).mid())*10**10),10**10)
            acts.append(action);scores.append(h)
        ck('finite_scores_exact_'+str((ll,n)),sum(scores)==S and all(0<=a<=b for a,b in zip(acts,scores)))
        P=arb(1);C=arb(0);R=arb(0);Cwrong=arb(0)
        for a0,b0 in zip(acts,scores):
            P/=1+ab(a0);w=ab(1+(b0-a0)**2/(2*(a0+b0)*(2-a0-b0))).log();C+=2*P*w;R+=2*P;Cwrong+=2*w
        actual=P-ab(ll)*C;gap=actual-V
        ck('finite_policy_beats_fluid_'+str((ll,n)),gap>0)
        ct('unweighted_cost_changes_value_'+str((ll,n)),Cwrong>C)
        finite.append({'lambda':str(ll),'score':str(S),'first_score':str(atom),'tail_count':n,'tail_score':str(h),'actions':list(map(str,acts)),'success_Arb':str(P),'leakage_Arb':str(C),'expected_trials_Arb':str(R),'fluid_candidate_Arb':str(V),'actual_value_Arb':str(actual),'improvement_Arb':str(gap)})
report={'result':'K2616','checks':checks,'contrary_controls':controls,'coefficients':{'D':str(D),'rho':str(rho),'E':str(E),'E_critical':str(Ec),'D_prime_critical':str(Dp),'atom_scale':str(tstar),'gain_over_lambda_delta_cubed':str(4*Dp**3/(27*Ec**2))},'necessary_phase_endpoints':ends,'finite_policy_consumers':finite,'finite_atom_neutral_brackets':neutral,'evidence_kind':'original log/optimized flow coefficients and exact signs, outward Arb roots and original-prefix finite policies; universal fixed-score exclusion and near-critical lower bound in note','ceiling':'necessary local boundary and constructive improvement only; no sharp global phase, exact true-value onset, or physical probability','provenance':{f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in ['explorations/conditional-build/k2517-small-score-stopping-transition-2026-11-02.md','explorations/conditional-build/k2602-continuum-stopping-resource-law-2026-11-06.md','explorations/conditional-build/k2612-extended-diffuse-stopping-phase-2026-11-06.md']}}
out=root/'lab/process/k2616-diffuse-stopping-instability.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'FAIL saved report replay'
print(json.dumps({'result':'K2616','checks':len(checks),'controls':len(controls),'finite_policies':len(finite),'status':'pass'}))
