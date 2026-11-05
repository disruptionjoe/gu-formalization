#!/usr/bin/env python3
"""Exact supporting identities and original-law consumers; proofs remain in note."""
import argparse, json, hashlib
from pathlib import Path
from fractions import Fraction as F
import sympy as s
root=Path(__file__).resolve().parents[2]
parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args()
checks=[];controls=[]
def ck(name,condition):
    assert bool(condition),'FAIL '+name
    checks.append(name)
def ct(name,condition):
    assert bool(condition),'FAIL contrary '+name
    controls.append(name)
a,b=s.symbols('a b',positive=True)
w=s.log(1+(b-a)**2/(2*(a+b)*(2-a-b)))
f=s.log((4-b)/(4-2*b))
ck('actual_zero_action_cost',s.simplify(w.subs(a,0)-f)==0)
wa=s.diff(w,a)
ck('actual_zero_action_derivative',s.cancel(-wa.subs(a,0)-2*(3-2*b)/((2-b)*(4-b)))==0)
ck('uniform_derivative_margin_polynomial',s.expand(s.Rational(4,5)*(2-b)*(4-b)-2*(3-2*b))==(4*b*b-4*b+2)/5)
ck('margin_positive_square',s.expand((4*b*b-4*b+2)-(4*(b-s.Rational(1,2))**2+1))==0)
ck('zero_action_second_derivative',s.simplify(s.diff(f,b,2)-(1/(2-b)**2-1/(4-b)**2))==0)
ck('upper_second_derivative_remainder',s.Rational(1,1)/(2-s.Rational(1,2))**2==s.Rational(4,9))
ck('third_derivative',s.simplify(s.diff(f,b,3)-(2/(2-b)**3-2/(4-b)**3))==0)
ck('third_derivative_upper',2/(2-s.Rational(1,2))**3==s.Rational(16,27))
ck('optimizer_lower_value',1-s.Rational(2,5)/2-2*s.Rational(1,16)==s.Rational(27,40))
ck('strict_uniform_action_margin',s.Rational(27,40)-s.Rational(16,25)==s.Rational(7,200)>0)
ck('all_tie_prices_inside_region',F(2,5)*F(1,4)/9==F(1,90)<F(1,16))
x,S=s.symbols('x S',positive=True)
H=x*f.subs(b,S/x)
ck('perspective_second_derivative',s.simplify(s.diff(H,x,2)-S*S/x**3*s.diff(f,b,2).subs(b,S/x))==0)
coeff=[s.expand(s.series(f,b,0,5).removeO()).coeff(b,j) for j in (1,2,3)]
ck('series_coefficients',coeff==[s.Rational(1,4),s.Rational(3,32),s.Rational(7,192)])
v,c,k,l=s.symbols('v c k l',real=True)
V=(v-2*l*w-2*k)/(1+a)
ck('suffix_action_derivative_identity',s.simplify(s.diff(V,a)-(-2*l*wa-V)/(1+a))==0)
# Positive rational log remainder, separate from universal arguments.
def log_bounds(r,N=32):
    assert r>=1
    u=(r-1)/(r+1)
    lo=2*sum((u**(2*j+1)/F(2*j+1) for j in range(N)),F(0))
    return lo,lo+2*u**(2*N+1)/(F(2*N+1)*(1-u*u))
def law(stages):
    p=F(1);R=F(0);cl=F(0);cu=F(0)
    for aa,bb in stages:
        p/=1+aa;R+=2*p
        ratio=1+(bb-aa)**2/(2*(aa+bb)*(2-aa-bb))
        lo,hi=log_bounds(ratio);cl+=2*p*lo;cu+=2*p*hi
    return p,R,cl,cu
S0=F(1,2);lam=F(1,10)
rows={n:law([(F(0),S0/n)]*n) for n in (1,2,3,12)}
for n,row in rows.items():
    p,R,cl,cu=row;lo,hi=log_bounds((4-S0/n)/(4-2*S0/n))
    ck('original_equal_stage_law_'+str(n),p==1 and R==2*n and cl==2*n*lo and cu==2*n*hi)
cl=(rows[1][2]+rows[2][2])/2;cu=(rows[1][3]+rows[2][3])/2
Flo,Fhi=1-lam*cu,1-lam*cl
ck('mixture_exact_resource',F(1,2)*rows[1][1]+F(1,2)*rows[2][1]==3)
ck('mixture_log_combination',F(7,6)*F(15,14)**2==F(525,392))
ck('optimal_M3_bracket',F(970786357719,10**12)<Flo<Fhi<F(970786357720,10**12))
k1lo=lam*(rows[1][2]-rows[2][3])/2;k1hi=lam*(rows[1][3]-rows[2][2])/2
k2lo=lam*(rows[2][2]-rows[3][3])/2;k2hi=lam*(rows[2][3]-rows[3][2])/2
ck('first_two_support_prices',0<k2lo<k2hi<k1lo<k1hi<F(1,16))
ck('M3_support_price_bracket',F(1616493685,10**12)<k1lo<k1hi<F(1616493686,10**12))
# At the exact price lambda(H1-H2), the coefficients in all tied support identities cancel.
h1,h2=s.symbols('h1 h2');price=l*(h1-h2)
ck('support_tie',s.expand((1-2*l*h1-2*price)-(1-2*l*h2-4*price))==0)
ck('mixture_support',s.expand(1-l*(h1+h2)-(1-2*l*h1-2*price+3*price))==0)
M5lo=1-lam*(rows[2][3]+rows[3][3])/2;M5hi=1-lam*(rows[2][2]+rows[3][2])/2
ck('optimal_M5_bracket',F(972865896931,10**12)<M5lo<M5hi<F(972865896932,10**12))
ck('budget_join_corner',F(9,70)>F(1,90))
ck('finite_resource_sufficient',4*lam*S0*S0/(9*12)==F(1,1080)<F(1,1000))
V0=1-lam*S0/2;gap12lo=V0-(1-lam*rows[12][2]);gap12hi=V0-(1-lam*rows[12][3])
ck('exact_24_trial_gap',0<gap12lo<gap12hi<F(1,1000))
# Symbolic interpolation expansion: shift n=r-alpha, M=2r.
r,alpha=s.symbols('r alpha',positive=True)
expr=(1-alpha)/(r-alpha)+alpha/(r+1-alpha)
ck('interpolation_second_coefficient_cancels',s.limit(r*r*(expr-1/r),r,s.oo)==0)
ck('interpolation_third_coefficient',s.simplify(s.limit(r**3*(expr-1/r),r,s.oo)-alpha*(1-alpha))==0)
ck('sharp_resource_coefficient',2*s.Rational(3,32)*2==s.Rational(3,8))
ck('second_resource_coefficient',2*s.Rational(7,192)*4==s.Rational(7,24))
ck('small_price_duality_coefficient',(2*s.sqrt(2*s.Rational(3,16)))**2==s.Rational(3,2))
# Contrary controls alter actual objects/accounting, not checker predicates.
fraclo,frachi=log_bounds(F(11,10))
ct('fractional_stage_is_unattainable_chord',1-3*lam*frachi>Fhi)
ct('counting_one_trial_per_stage_wrong',rows[2][1]!=2)
ct('deterministic_two_stage_violates_M3',rows[2][1]>3)
ct('one_stage_is_suboptimal_at_M3',1-lam*rows[1][2]<Flo)
ct('dropping_fair_trial_factor_two_changes_consumer',1-lam*cu/2>Fhi)
ct('large_multiplier_zero_action_extension_false',F(2,3)-F(4,3)*F(1,10000)>1-F(19,10)*S0/2)
# Unequal score split is strictly worse than equal split at fixed actual resource.
un=law([(F(0),F(1,8)),(F(0),F(3,8))])
ct('unequal_two_stage_cost_worse',un[2]>rows[2][3] and un[1]==rows[2][1])
# Dropping the positive log remainder is not an upper enclosure.
lo1,hi1=log_bounds(F(7,6),1);lo2,hi2=log_bounds(F(7,6),2)
ct('truncated_log_is_not_upper_bound',lo2>lo1 and hi1>hi2)
def bracket(lo,hi):
    m=10**12
    return [str(F(lo.numerator*m//lo.denominator,m)),str(F(-(-hi.numerator*m//hi.denominator),m))]
report={'result':'K2577','evidence_kind':'exact symbolic identities and rational original-law consumers; universal optimality and duality proof in note','checks':checks,'contrary_controls':controls,'M3':{'p':'1','R':'3','C':'log(525/392)','F_bracket':bracket(Flo,Fhi),'support_price_bracket':bracket(k1lo,k1hi)},'M5':{'F_bracket':bracket(M5lo,M5hi)},'resource_consumer':{'expected_trials':24,'error_target':'1/1000','gap_bracket':bracket(gap12lo,gap12hi)},'ceiling':'complete resource frontier at S=1/2 and 0<lambda<=2/5; no general multiplier or GU claim'}
refs=['k2575-constructive-priced-optimization','k2571-stopping-resource-price','k2569-stopping-maximizing-sequences','k2561-higher-budget-stopping']
report['provenance']={'explorations/conditional-build/'+f+'-2026-11-05.md':hashlib.sha256((root/('explorations/conditional-build/'+f+'-2026-11-05.md')).read_bytes()).hexdigest() for f in refs}
out=root/'lab/process/k2577-exact-resource-tail.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved report mismatch'
print(json.dumps({'result':'K2577','checks':len(checks),'controls':len(controls),'status':'pass'}))
