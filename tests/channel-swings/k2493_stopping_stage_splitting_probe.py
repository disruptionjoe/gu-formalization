"""Original-law exact split controls; universal proofs are in the paired note."""
from fractions import Fraction as F
from pathlib import Path
import json, hashlib, sys
import sympy as S
R=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError('FAIL '+k)
def ct(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError('FAIL contrary '+k)
def xcost(a,b):
 if not 0<=a<=1 or not 0<=b<=1:raise ValueError('domain')
 return F(0) if a>=b else (b-a)**2/(2*(a+b)*(2-a-b))
def logbounds(x):
 if not 0<=x<=1:raise ValueError('small logarithm domain')
 return x-x*x/2,x-x*x/2+x*x*x/3
def policy(stages):
 survival=F(1);lo=hi=F(0);score=F(0)
 for a,b in stages:
  l,h=logbounds(xcost(a,b));lo+=survival*2*l/(1+a);hi+=survival*2*h/(1+a)
  survival/=1+a;score+=b
 return survival,lo,hi,score
# Symbolic perspective and split derivative independent of finite witness.
a,b,t,r,p=S.symbols('a b t r p',positive=True)
w=S.log(1+(b-a)**2/(2*(a+b)*(2-a-b)))
wa=S.factor(S.diff(w,a));wb=S.factor(S.diff(w,b));waa=S.factor(S.diff(w,a,2))
U=S.symbols('U');N=2*U*(2-U)+(2*b-U)**2
ck('numerator_factor',S.expand(N-(-U**2+4*(1-b)*U+4*b*b))==0)
D=S.sqrt((1-b)**2+b*b);Rp=2*(1-b)+2*D;T=-2*(1-b)+2*D
ck('factored_numerator',S.simplify((Rp-U)*(U+T)-N)==0)
curv=(1/U**2+1/(2-U)**2-1/(Rp-U)**2-1/(U+T)**2)
ck('curvature_identity',S.simplify(waa-curv.subs(U,a+b))==0)
C=2*p*w.subs(a,1/p-1)
ck('perspective_second',S.simplify(S.diff(C,p,2)-2*waa.subs(a,1/p-1)/p**3)==0)
g=(1-r)**2/(2*(1+r));A=-2*wa;B=2*wb/(1+a)
# The first tiny-stage cost has derivative g; the second uses da2/dt=-r(1+a).
a2=(a-r*t)/(1+r*t)
second=2*w.subs({a:a2,b:b-t}, simultaneous=True)/(1+a)
ck('split_derivative',S.simplify(S.diff(second,t).subs(t,0)-A*r+B)==0)
ck('tiny_stage_limit',S.simplify(2*S.cancel(((b-a)**2/(2*(a+b)*(2-a-b))).subs({a:r*t,b:t}, simultaneous=True)/t).subs(t,0)-g)==0)
ck('g_derivative',S.simplify(S.diff(g,r)-(S.Rational(1,2)-2/(1+r)**2))==0)
ck('negative_split_slope',S.simplify((g+A*r-B).subs({a:S.Rational(3,10),b:S.Rational(1,2),r:S.Rational(1,2)}))==-S.Rational(19,3822))
# Exact finite witness and comparison with all initial single-stage mixtures.
stages=[(F(1,200),F(1,100)),(F(59,201),F(49,100))];K=F(317,10000)
P,lo,hi,score=policy(stages);single=policy([(F(3,10),F(1,2))]);ck('same_success',P==single[0]==F(10,13));ck('same_score',score==F(1,2));ck('strict_budget_separation',hi<K<single[1]);ck('native_log_arguments',[xcost(*q) for q in stages]==[F(1,2382),F(15594601,770157598)]);ck('single_lower_bound',single[1]==F(475,14976))
ck('tangent_slope_upper',F(1,24)+F(325,588)<F(3,5))
ck('single_class_gap',F(475,14976)-K==F(163,9360000) and F(163,9360000)/F(3,5)==F(163,5616000))
# Local stability of the previous tiny-budget one-stage witness: positive minimum.
aa=F(2309,5000);bb=F(1,2)
Av=F(str(A.subs({a:S.Rational(aa.numerator,aa.denominator),b:S.Rational(1,2)})));Bv=F(str(B.subs({a:S.Rational(aa.numerator,aa.denominator),b:S.Rational(1,2)})))
# For A<=3/2, min g+Ar-B=2sqrt(1+2A)-A-2-B.
ck('prior_small_budget_positive_split_derivative',0<Av<F(3,2) and (Av+2+Bv)>0 and 4*(1+2*Av)>(Av+2+Bv)**2)
# Meaningful contrary models / failed witness directions.
ct('merge_increases_cost',single[1]>hi)
wrong_hi=sum(2*logbounds(xcost(a,b))[1]/(1+a) for a,b in stages)
ct('omitting_survival_changes_cost',wrong_hi!=hi)
wrong_P=1/(1+sum(a for a,b in stages));ct('additive_failure_wrong',wrong_P!=P)
ct('free_stages_do_not_match_success',1/((1+stages[0][1])*(1+stages[1][1]))<P)
ct('taylor_upper_not_lower',logbounds(F(1,48))[0]<logbounds(F(1,48))[1])
# A low-cost construction shows why a global merge cannot be inferred from a tiny-budget local test.
for budget in [K,F(1,1000)]:
 ct('budget_actual_'+str(budget),(hi<budget)==(budget==K))
for bad in [(F(-1),F(1,2)),(F(0),F(2))]:
 try:xcost(*bad);ok=False
 except ValueError:ok=True
 ct('invalid_'+str(bad),ok)
deps=['lab/process/k2491-analytic-stopping-certificate.json','explorations/conditional-build/k2485-constrained-stopping-frontier-2026-11-01.md']
report={'result':'K2493','checks':checks,'contrary_controls':controls,'witness':{'stages':[[str(a),str(b)] for a,b in stages],'success':str(P),'budget':str(K),'cost_lower':str(lo),'cost_upper':str(hi),'single_cost_lower':str(single[1]),'single_cost_upper':str(single[2]),'split_derivative':'-19/3822'},'prior_witness_local_stability':{'A':str(Av),'B':str(Bv),'claim':'positive insertion derivative for every ratio r in [0,1]; not global optimality'},'dependencies':{q:hashlib.sha256((R/q).read_bytes()).hexdigest() for q in deps},'evidence_kinds':{'universal':'written strict convex perspective and Jensen mixture exclusion; exact insertion derivative','exact':'symbolic identities and rational logarithm brackets','not_claimed':'global adaptive optimum, small-budget one-stage optimality, native GU physics, novelty'}}
pth=R/'lab/process/k2493-stopping-stage-splitting.json'
if '--write' in sys.argv:pth.write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
else:ck('saved_reproduction',json.loads(pth.read_text())==report)
print(json.dumps({'result':'PASS','checks':len(checks),'controls':len(controls),'witness':report['witness']}))
