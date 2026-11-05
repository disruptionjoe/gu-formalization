#!/usr/bin/env python3
"""Exact supporting identities and original-law consumers; universal proofs in note."""
import argparse,json,hashlib
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

a,b,lam,M,k,kstar,J,Jstar,R,Rstar=s.symbols('a b lam M k kstar J Jstar R Rstar',positive=True)
arg=1+(b-a)**2/(2*(a+b)*(2-a-b));w=s.log(arg);wa=s.cancel(s.diff(w,a));Mfun=-2*(1+a)*wa+2*w
ck('price_domination_identity',s.expand(J-k*R-(Jstar-k*Rstar)-(J-kstar*R-Jstar+kstar*Rstar)+(k-kstar)*(R-Rstar))==0)
ct('reverse_price_direction_can_lose',((k-kstar)*(R-Rstar)).subs({k:1,kstar:2,R:3,Rstar:2})<0)
ck('one_stage_derivative',s.cancel(s.diff((1-2*k-2*lam*w)/(1+a),a)-(lam*Mfun-(1-2*k))/(1+a)**2)==0)
ck('Mfun_decreases_identity',s.cancel(s.diff(Mfun,a)+2*(1+a)*s.diff(wa,a))==0)
ck('Mfun_free_endpoint',s.simplify(Mfun.subs(a,b))==0)
ck('consumer_derivative_exact',wa.subs({a:s.Rational(1,4),b:s.Rational(1,2)})==-s.Rational(128,465))
curve=M/2-lam*M*w.subs(a,2/M-1)
ck('frontier_derivative_price',s.cancel(s.diff(curve,M)-(1-lam*Mfun.subs(a,2/M-1))/2)==0)
wm=s.cancel(wa.subs(a,2/M-1)*(-2/M**2)); wmm=s.cancel(s.diff(wm,M))
ck('frontier_curvature',s.cancel(-2*lam*wm-lam*M*wmm-lam*s.cancel(s.diff(Mfun,a)).subs(a,2/M-1)/M**2)==0)
cs,H1,H2=s.symbols('cs H1 H2');k0=(1-lam*(2*cs+2*H1))/2;k1=lam*(H1-H2)
ck('corner_gap',s.expand(k0-k1-(1-lam*(2*cs+4*H1-2*H2))/2)==0)
ck('multistage_resource_gap_rational_bound',F(4,1)/F(5,3)>2)
# exp(.5)<5/3: through degree4 plus geometric tail (successive ratios <=1/12).
e4=sum((F(1,2)**i/F(s.factorial(i)) for i in range(5)),F(0));etail=F(1,2)**5/F(120)/(1-F(1,12))
ck('exponential_upper_certificate',e4+etail<F(5,3))
def lb(q):
 q=F(q);assert q>=1;u=(q-1)/(q+1);lo=2*sum((u**(2*j+1)/F(2*j+1) for j in range(12)),F(0));return lo,lo+2*u**25/(25*(1-u*u))
def add(x,y):return x[0]+y[0],x[1]+y[1]
def mul(c,x):return (c*x[0],c*x[1]) if c>=0 else(c*x[1],c*x[0])
def law(stages):
 p=F(1);cost=(F(0),F(0));resource=F(0)
 for aa,bb in stages:
  assert 0<=aa<=bb and bb>0
  p/=1+aa;resource+=2*p
  cost=add(cost,mul(2*p,lb(1+(bb-aa)**2/(2*(aa+bb)*(2-aa-bb)))))
 return p,cost,resource
def value(z,l):return add((z[0],z[0]),mul(-l,z[1]))
l=F(67,125);h1=lb(F(7,6));h2=mul(2,lb(F(15,14)));dd=add((F(32,21),F(32,21)),add(mul(4,h1),mul(-2,h2)))
threshold=(1/dd[1],1/dd[0]);ck('lambda_in_range',F(2,5)<l<threshold[0])
actual=law([(F(1,4),F(1,2))]);v=value(actual,l)
ck('middle_original_policy',actual[0]==F(4,5) and actual[2]==F(8,5))
ck('middle_leakage',actual[1]==mul(F(8,5),lb(F(31,30))))
mm=add((F(64,93),F(64,93)),mul(2,lb(F(31,30))))
price=mul(F(1,2),add((F(1),F(1)),mul(-l,mm)))
lowprice=mul(F(1,2),add((F(1),F(1)),mul(-l,add((F(32,21),F(32,21)),mul(2,h1)))))
countprice=mul(l,add(h1,mul(-1,h2)))
ck('full_price_branch',0<countprice[0]<=countprice[1]<lowprice[0]<lowprice[1]<price[0]<price[1]<F(1,2))
ck('priced_value_positive',v[0]-price[1]*actual[2]>0)
ct('omit_failure_trials_changes_budget',actual[2]/2!=F(8,5))
free=law([(F(1,2),F(1,2))]);ck('abort_free_budget1',F(3,4)*free[0]==F(1,2) and F(3,4)*free[2]==1 and free[1]==(0,0))
zero=law([(F(0),F(1,2))]);two=law([(F(0),F(1,4))]*2)
ck('exact_count_price_tie',s.expand(1-2*lam*H1-2*lam*(H1-H2)-(1-2*lam*H2-4*lam*(H1-H2)))==0)
tie=s.expand((1-2*lam*H1)-2*lam*(H1-H2)-(1-2*lam*H2)+4*lam*(H1-H2))
ct('strict_tie_claim_rejected',tie==0)
C3=mul(F(1,2),add(zero[1],two[1]));ck('certain_success_tradeoff_budget3',(zero[2]+two[2])/2==3 and zero[0]==two[0]==1)
ct('leakage_without_success_constraint',C3[0]>0 and free[1]==(0,0))
ct('middle_above2_has_invalid_action',F(2,3)-1<0)
small=law([(F(1,9),F(1,4))]);ls=F(59,100);vs=value(small,ls)
ck('quarter_score_middle_original',small[0]==F(9,10) and small[2]==F(9,5))
ck('quarter_score_log_argument',small[1]==mul(F(9,5),lb(F(1559,1534))))
dsmall=add((F(32,21),F(32,21)),add(mul(4,lb(F(15,14))),mul(-4,lb(F(31,30)))))
ck('quarter_score_multiplier_admitted',ls<1/dsmall[1])
# Rigorous monotone action bracket at a rational price k=3/10.
kfix=F(3,10)
def mf_bounds(aa):
 aa=F(aa);bb=F(1,2);ww=lb(1+(bb-aa)**2/(2*(aa+bb)*(2-aa-bb)))
 deriv=F(wa.subs({a:s.Rational(aa.numerator,aa.denominator),b:s.Rational(1,2)}))
 return add((-2*(1+aa)*deriv,)*2,mul(2,ww))
target=(1-2*kfix)/l;left=F(0);right=F(1,2)
for _ in range(30):
 mid=(left+right)/2;mmid=mf_bounds(mid)
 if mmid[0]>target:left=mid
 elif mmid[1]<target:right=mid
 else:raise AssertionError('log precision inadequate for certified bisection')
ck('certified_scalar_price_solver',mf_bounds(left)[0]>target and mf_bounds(right)[1]<target and right-left<F(1,10**8))
# Above-threshold original-policy countercontrol (inherited construction, newly replayed).
la=F(537,1000);eps=law([(F(1,10000),F(1,2))]);weight=1/(4-eps[2]);new=add(mul(weight,value(eps,la)),mul(1-weight,value(two,la)));old=mul(F(1,2),add(value(zero,la),value(two,la)));gain=add(new,mul(-1,old))
ck('counterpolicy_preserves_resource',weight*eps[2]+(1-weight)*two[2]==3)
ct('beyond_threshold_tail_extension_false',gain[0]>0)
report={'result':'K2583','evidence_kind':'exact price/derivative identities and rational-log original-law consumers; universal reduction/support proof in note','checks':checks,'contrary_controls':controls,'middle_budget8over5':[str(x) for x in v],'support_price':[str(x) for x in price],'quarter_score_budget9over5':[str(x) for x in vs],'certain_success_leakage_budget3':[str(x) for x in C3],'rational_price3over10_action_bracket':[str(left),str(right)],'ceiling':'all budgets/all positive prices for lambda<=Lambda(S), not above-transition optimizer'}
refs=['k2581-score-sensitive-tail-transition-2026-11-05','k2575-constructive-priced-optimization-2026-11-05','k2569-stopping-maximizing-sequences-2026-11-05']

report['provenance']={'explorations/conditional-build/'+r+'.md':hashlib.sha256((root/('explorations/conditional-build/'+r+'.md')).read_bytes()).hexdigest() for r in refs}
out=root/'lab/process/k2583-complete-stopping-resource-frontier.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved report mismatch'
print(json.dumps({'result':report['result'],'checks':len(checks),'controls':len(controls),'status':'pass'}))
