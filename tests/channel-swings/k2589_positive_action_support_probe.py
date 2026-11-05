#!/usr/bin/env python3
"""Exact supporting identities/consumers; universal proof is in companion note."""
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

a,b,r=s.symbols('a b r',positive=True);w=s.log(1+(b-a)**2/(2*(a+b)*(2-a-b)));wa=s.cancel(s.diff(w,a));waa=s.cancel(s.diff(wa,a))
q=2*(r-1)*(2*b*(r+1)-r-3)/((r+1)*(b*(r+1)-2)*(b*(r*r+6*r+1)-4*(r+1)))
ck('score_derivative',s.cancel(q+wa.subs(a,r*b))==0)
P=(b*b-b)*r**4+(8*b*b-10*b+3)*r**3+(14*b*b-28*b+11)*r*r+(8*b*b-22*b+17)*r+(b*b-3*b+1)
den=(r+1)*(b*(r+1)-2)**2*(b*(r*r+6*r+1)-4*(r+1))**2
ck('score_derivative_polynomial',s.cancel(s.diff(q,b)-4*(1-r)*P/den)==0)
Q=(2*b*b-3*b)*r**4+(16*b*b-30*b+12)*r**3+(28*b*b-84*b+44)*r*r+(16*b*b-66*b+68)*r+(2*b*b-9*b+4)
# Recover the exact denominator from independently differentiated half-scale difference.
diff=s.cancel(q-q.subs(b,b/2));numhalf=s.factor(diff/(2*b*(1-r)*Q))
ck('half_scale_numerator',s.cancel(diff-2*b*(1-r)*Q*numhalf)==0)
# The four b-dependent factors below are negative, their product positive; this explicit identity avoids a tautological sign test.
expected=1/((r+1)*(b*(r+1)-2)*(b*(r+1)-4)*(b*(r*r+6*r+1)-4*(r+1))*(b*(r*r+6*r+1)-8*(r+1)))
ck('half_scale_positive_denominator',s.cancel(numhalf-expected)==0)
# Coefficient lower bounds proved by monotonicity on entire intervals.
for label,polys,end,lower in [('quarter',[9*b*b-11*b+3,14*b*b-28*b+11,8*b*b-22*b+17,b*b-3*b+1],s.Rational(1,4),[s.Rational(13,16),s.Rational(39,8),12,s.Rational(5,16)]),('half',[18*b*b-33*b+12,28*b*b-84*b+44,16*b*b-66*b+68,2*b*b-9*b+4],s.Rational(1,2),[0,9,39,0])]:
 for i,(poly,bound) in enumerate(zip(polys,lower)):
  ck(label+'_coefficient_'+str(i),poly.subs(b,end)>=bound and s.diff(poly,b).subs(b,end)<0 and s.diff(poly,b,2)>0)
ck('negative_leading_absorption_quarter',(b*b-b).subs(b,s.Rational(1,4))<0)
Mfun=-2*(1+a)*wa+2*w
ck('optimizer_monotonic_derivative',s.cancel(s.diff(Mfun,a)+2*(1+a)*waa)==0)
lam,k=s.symbols('lam k');J=(1-2*lam*w-2*k)/(1+a)
ck('priced_first_derivative',s.cancel(s.diff(J,a)-(lam*Mfun-(1-2*k))/(1+a)**2)==0)
ck('zero_leakage_endpoint',s.simplify(Mfun.subs(a,b))==0)
def lb(q):
 q=F(q);assert q>=1;u=(q-1)/(q+1);lo=2*sum((u**(2*j+1)/F(2*j+1) for j in range(20)),F(0));return lo,lo+2*u**41/(41*(1-u*u))
def add(x,y):return x[0]+y[0],x[1]+y[1]
def mul(c,x):return(c*x[0],c*x[1]) if c>=0 else(c*x[1],c*x[0])
def sub(x,y):return add(x,mul(-1,y))
def exact(x):return(F(x),F(x))
def W(a,b):return lb(1+(b-a)**2/(2*(a+b)*(2-a-b)))
def H(n,S):return mul(n,W(F(0),S/n))
def delta(S):return sub(H(1,S),H(2,S))
def WA(a0,b0):return F(wa.subs({a:s.Rational(a0.numerator,a0.denominator),b:s.Rational(b0.numerator,b0.denominator)}))
def MF(a0,S):return add(exact(-2*(1+a0)*WA(a0,S)),mul(2,W(a0,S)))
def price(a0,S,l):return mul(F(1,2),sub(exact(1),mul(l,MF(a0,S))))
cons=[]
for name,S,l,action in [('half',F(1,2),F(11,20),F(1,100)),('quarter',F(1,4),F(13,20),F(1,50))]:
 kp=price(action,S,l);ks=mul(l,delta(S));crit=add(MF(F(0),S),mul(2,delta(S)))
 ck(name+'_beyond_Lambda',l*crit[0]>1)
 ck(name+'_global_price',kp[0]>ks[1]>0 and kp[1]<F(1,2))
 p0=1/(1+action);resource=2*p0;C=mul(2*p0,W(action,S));Fval=sub(exact(p0),mul(l,C));Qval=sub(Fval,mul(resource,kp))
 ck(name+'_positive_supported_value',Qval[0]>0)
 ck(name+'_original_resource',resource== (F(200,101) if name=='half' else F(100,51)))
 ck(name+'_below_old_merge_price',kp[1]<l*S*(2+S)/6)
 ct(name+'_omit_failed_trial_cost',p0!=resource)
 ct(name+'_unit_survival',p0!=1)
 cons.append({'label':name,'score':str(S),'lambda':str(l),'action':str(action),'resource':str(resource),'price':list(map(str,kp)),'value':list(map(str,Fval))})
S=F(1,2);l=F(11,20);ks=mul(l,delta(S));target=sub(exact(1/l),mul(2,delta(S)));low=F(0);high=S
ck('endpoint_initial_signs',MF(low,S)[0]>target[1] and MF(high,S)[1]<target[0])
for _ in range(30):
 mid=(low+high)/2;val=MF(mid,S)
 if val[0]>target[1]:low=mid
 elif val[1]<target[0]:high=mid
 else:raise AssertionError('log enclosure insufficient')
ck('endpoint_width',high-low==S/2**30)
ck('endpoint_final_signs',MF(low,S)[0]>target[1] and MF(high,S)[1]<target[0])
endpoint={'action_interval':list(map(str,[low,high])),'resource_interval':list(map(str,[2/(1+high),2/(1+low)])),'price':list(map(str,ks)),'priced_value_interval':list(map(str,[-2*l*WA(high,S),-2*l*WA(low,S)]))}
# Released post2 consumer: original rational-action mixture lower bound,
# exact global positive-action support upper bound at kstar.
a_trial=F(1,125);p_trial=1/(1+a_trial);r_trial=2*p_trial
v_trial=sub(exact(p_trial),mul(2*l*p_trial,W(a_trial,S)))
v_two=sub(exact(1),mul(2*l,H(2,S)));mix=(4-F(3))/(4-r_trial)
lower_value=add(mul(mix,v_trial),mul(1-mix,v_two))
qstar=(-2*l*WA(high,S),-2*l*WA(low,S));upper_value=add(qstar,mul(3,ks))
old_chord=sub(exact(1),mul(l,add(H(1,S),H(2,S))))
ck('post2_exact_resource',mix*r_trial+(1-mix)*4==3 and 0<mix<1)
ck('post2_strict_old_chord_improvement',lower_value[0]>old_chord[1])
ck('post2_bracket_order',upper_value[0]>lower_value[1])
ck('post2_bracket_width',upper_value[1]-lower_value[0]<F(51,1000000))
post2={'score':str(S),'lambda':str(l),'budget':'3','action':str(a_trial),'mixture_weight':str(mix),'lower':list(map(str,lower_value)),'upper':list(map(str,upper_value)),'old_chord':list(map(str,old_chord))}
# Actual lower-coefficient counterpolicy: t=Delta1/2, lambda=.1.
l=F(1,10);t=mul(F(1,2),delta(S));kbad=mul(l,t)
ck('small_lambda_one_stage_optimal',mul(l,add(MF(F(0),S),mul(2,t)))[1]<1)
j1=sub(sub(exact(1),mul(2*l,H(1,S))),mul(2,kbad));j2=sub(sub(exact(1),mul(2*l,H(2,S))),mul(4,kbad))
ct('lower_price_coefficient_counterpolicy',j2[0]>j1[1]>0)
actual_p=1/((1+F(1,5))*(1+F(1,5)));product_bound=1/(1+F(2,5));negative_N=F(-1)
ct('negative_numerator_wrong_product_bound',actual_p<product_bound and actual_p*negative_N>product_bound*negative_N)
ct('multiple_actions_product_strict',(1+F(1,10))**2>1+F(1,5))
ct('score_order_not_reversed',F(q.subs({r:s.Rational(1,2),b:s.Rational(1,4)}))<F(q.subs({r:s.Rational(1,2),b:s.Rational(1,2)})))
report={'result':'K2589','checks':checks,'contrary_controls':controls,'evidence_kind':'exact rational derivative identities and interval original-policy consumers; all-policy theorem in note','consumers':cons,'endpoint':endpoint,'post2_bracket':post2,'uniform_price_counterexample':{'one_stage':list(map(str,j1)),'two_stage':list(map(str,j2))},'ceiling':'global one-stage price wedge and supported below2 budget segment, not failed post2 chord optimum'}
refs=['explorations/conditional-build/k2581-score-sensitive-tail-transition-2026-11-05.md','explorations/conditional-build/k2587-countwise-stopping-support-2026-11-05.md']

report['provenance']={f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in refs}
out=root/'lab/process/k2589-positive-action-support.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved report mismatch'
print(json.dumps({'result':report['result'],'checks':len(checks),'controls':len(controls),'status':'pass'}))
