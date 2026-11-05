#!/usr/bin/env python3
"""Exact supporting identities and original-object consumers; universal proofs in note."""
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

a,b,t,d=s.symbols('a b t d',positive=True)
w=s.log(1+(b-a)**2/(2*(a+b)*(2-a-b)));w0=s.log((4-b)/(4-2*b));cc=2*(3-2*b)/((2-b)*(4-b));cs=s.Rational(16,21)
ck('score_sensitive_factor',s.factor(cc-cs+2*(2*b-1)*(4*b-1)/(21*(b-4)*(b-2)))==0)
ck('equal_count_bounds',cc.subs(b,s.Rational(1,2))==cs and cc.subs(b,s.Rational(1,4))==cs)
ct('global16over21_bound_false',cc.subs(b,s.Rational(3,8))>cs)
N=2*t*(2-t)+d*d;wt=s.log(N/(2*t*(2-t)));P=2*t*t*(2-t)**2-d*d*(t*t-2*t+2)
htt=s.cancel(s.diff(wt,t,2));hdd=s.cancel(s.diff(wt,d,2));htd=s.cancel(s.diff(wt,t,d))
ck('joint_Hessian_determinant',s.cancel(4*(htt*hdd-htd**2)-16*d*d*P/(t*t*(2-t)**2*N**3))==0)
ct('omit_d_squared_changes_actual_Hessian',s.cancel((4*(htt*hdd-htd**2)-16*P/(t*t*(2-t)**2*N**3)).subs({t:s.Rational(1,2),d:s.Rational(1,4)}))!=0)
ck('determinant_lower',s.expand(P.subs(d,t)-t*t*(t*t-6*t+6))==0)
ck('positive_unit_polynomial',s.expand(t*t-6*t+6-((1-t)**2+4*(1-t)+1))==0)
ck('strict_action_convexity_fixture',s.diff(w,a,2).subs({a:s.Rational(1,20),b:s.Rational(1,4)})>0)
S=s.symbols('S',positive=True)
ck('all_score_c_comparison',s.factor(cc.subs(b,S)-cc.subs(b,S/2)-2*S*(2*S-1)/((S-8)*(S-4)*(S-2)))==0)
ck('small_score_c_monotonicity',s.factor(s.diff(cc,b)-4*(b*b-3*b+1)/((b-4)**2*(b-2)**2))==0)
active,cost0,tail=s.symbols('active cost0 tail',positive=True)
first=(tail-cost0-active)/(1+a);last=(tail-active)/(1+a)-cost0
ck('active_first_exchange_gain',s.factor(first-last-cost0*a/(1+a))==0)
ct('reverse_exchange_worse',s.factor(last-first)==-cost0*a/(1+a))
lam,k,H1,H2=s.symbols('lam k H1 H2',positive=True);crit=1/(2*cs+4*H1-2*H2);k1=lam*(H1-H2)
ck('critical_support_margin',s.simplify((1-2*lam*H1-2*k1-2*lam*cs).subs(lam,crit))==0)
M=s.symbols('M',positive=True);curve=M/2-lam*M*w.subs({a:2/M-1,b:s.Rational(1,2)})
left=s.simplify(s.diff(curve,M).subs(M,2));expected=(1-lam*(2*cs+2*s.log(s.Rational(7,6))))/2
ck('one_stage_left_derivative',s.simplify(left-expected)==0)
critlogs=crit.subs({H1:s.log(s.Rational(7,6)),H2:2*s.log(s.Rational(15,14))})
ck('critical_corner_tangent',s.cancel(s.expand_log((left-k1.subs({H1:s.log(s.Rational(7,6)),H2:2*s.log(s.Rational(15,14))})).subs(lam,critlogs),force=True))==0)
def logbounds(q):
 q=F(q);u=(q-1)/(q+1);lo=2*sum((u**(2*j+1)/F(2*j+1) for j in range(12)),F(0));return lo,lo+2*u**25/(25*(1-u*u))
def add(x,y):return x[0]+y[0],x[1]+y[1]
def mul(c,x):return (c*x[0],c*x[1]) if c>=0 else (c*x[1],c*x[0])
def law(stages):
 p=F(1);R=F(0);C=(F(0),F(0))
 for aa,bb in stages:
  p/=1+aa;R+=2*p;arg=1+(bb-aa)**2/(2*(aa+bb)*(2-aa-bb));C=add(C,mul(2*p,logbounds(arg)))
 return p,C,R
l1=logbounds(F(7,6));l2=mul(F(2),logbounds(F(15,14)));denom=add((F(32,21),F(32,21)),add(mul(F(4),l1),mul(F(-2),l2)));threshold=(1/denom[1],1/denom[0])
ck('sharp_transition_interval',F(536353,10**6)<threshold[0]<threshold[1]<F(536354,10**6))
lam0=F(67,125);ck('new_multiplier_in_sharp_range',lam0<threshold[0] and lam0>F(535191,10**6))
E=law([(F(0),F(1,2))]);B=law([(F(0),F(1,4))]*2)
p=(E[0]+B[0])/2;C=mul(F(1,2),add(E[1],B[1]));R=(E[2]+B[2])/2;value=add((p,p),mul(-lam0,C))
ck('executed_original_budget3',p==1 and R==3)
ck('budget3_formula',value==add((F(1),F(1)),mul(-lam0,add(l1,l2))))
ct('two_stage_exceeds_budget',B[2]>3)
ct('failure_trial_cost_omission',C!=mul(F(1,4),add(E[1],B[1])))
la=F(537,1000);aa=F(1,10000);A=law([(aa,F(1,2))]);weight=F(1)/(4-A[2]);JB=add((B[0],B[0]),mul(-la,B[1]));JA=add((A[0],A[0]),mul(-la,A[1]));JE=add((E[0],E[0]),mul(-la,E[1]));new=add(mul(weight,JA),mul(1-weight,JB));old=mul(F(1,2),add(JE,JB));gain=add(new,mul(-1,old))
ck('above_threshold_exact_resource',weight*A[2]+(1-weight)*B[2]==3)
ck('near_transition_strict_gain',gain[0]>0)
ct('equal_weights_not_exact_budget',(A[2]+B[2])/2!=3)
# Independent consumer at a different total score tests the released general-S theorem.
Esmall=law([(F(0),F(1,4))]);Bsmall=law([(F(0),F(1,8))]*2)
cs_small=F(16,21);h1small=logbounds(F(15,14));h2small=mul(F(2),logbounds(F(31,30)))
dsmall=add((2*cs_small,2*cs_small),add(mul(F(4),h1small),mul(F(-2),h2small)))
threshold_small=(1/dsmall[1],1/dsmall[0]);lsmall=F(59,100)
ck('general_score_consumer_in_range',lsmall<threshold_small[0])
small_value=add((F(1),F(1)),mul(-lsmall,mul(F(1,2),add(Esmall[1],Bsmall[1]))))
ck('general_score_original_budget3',(Esmall[2]+Bsmall[2])/2==3 and Esmall[0]==Bsmall[0]==1)
count,hn,hnext,hnext2=s.symbols('count hn hnext hnext2')
Tn=(count+1)*hn-count*hnext;Tnext=(count+2)*hnext-(count+1)*hnext2
ck('count_threshold_difference',s.expand(Tn-Tnext-(count+1)*(hn-2*hnext+hnext2))==0)
report={'result':'K2581','evidence_kind':'exact convexity, support and exchange identities; rational-log original-law consumers; universal proof in note','checks':checks,'contrary_controls':controls,'sharp_lambda_tail':[str(v) for v in threshold],'budget3_lambda67over125':[str(v) for v in value],'budget3_lambda537over1000_gain':[str(v) for v in gain],'budget3_score_quarter_lambda59over100':[str(v) for v in small_value],'ceiling':'sharp full post2 transition, not full middle/intermediate optimizer'}
refs=['k2579-resource-tail-breakdown-2026-11-05','k2577-exact-resource-tail-2026-11-05','k2571-stopping-resource-price-2026-11-05','k2509-stopping-atom-certificate-2026-11-02']

report['provenance']={'explorations/conditional-build/'+r+'.md':hashlib.sha256((root/('explorations/conditional-build/'+r+'.md')).read_bytes()).hexdigest() for r in refs}
out=root/'lab/process/k2581-score-sensitive-tail-transition.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved report mismatch'
print(json.dumps({'result':'K2581','checks':len(checks),'controls':len(controls),'status':'pass'}))
