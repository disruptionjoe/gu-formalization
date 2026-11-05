#!/usr/bin/env python3
"""Exact identities and independent original-object consumers; universal proof is in the note."""
import argparse,json,hashlib
from pathlib import Path
import sympy as s
from fractions import Fraction as F
root=Path(__file__).resolve().parents[2]
pa=argparse.ArgumentParser();pa.add_argument('--write',action='store_true');args=pa.parse_args()
checks=[];controls=[]
def ck(name,condition):
    assert bool(condition),'FAIL '+name
    checks.append(name)
def ct(name,condition):
    assert bool(condition),'FAIL contrary '+name
    controls.append(name)

a,b,ep,lam,kk,HH,cc=s.symbols('a b ep lam kk HH cc',positive=True)
w=s.log(1+(b-a)**2/(2*(a+b)*(2-a-b)))
w0=s.log((4-b)/(4-2*b));c=2*(3-2*b)/((2-b)*(4-b))
ck('action_derivative',s.simplify(-s.diff(w,a).subs(a,0)-c)==0)
ck('w0_identity',s.simplify(s.exp(w.subs(a,0))-s.exp(w0))==0)
ck('c_strict_lower_identity',s.factor(c-s.Rational(3,4)-b*(2-3*b)/(4*(2-b)*(4-b)))==0)
bstar=(3-s.sqrt(5))/2;cmax=3-s.sqrt(5)
ck('cmax_at_stationary',s.simplify(c.subs(b,bstar)-cmax)==0)
ck('cmax_derivative',s.simplify(s.diff(c,b).subs(b,bstar))==0)
# Factor verifies global max, denominator positive on [0,1/2].
ck('global_cmax_square',s.simplify((cmax-c)*(2-b)*(4-b)-(3-s.sqrt(5))*(b-bstar)**2)==0)
ck('looser_bound_not_exact',s.Rational(4,5)>cmax)
n,Hn,Hnext,M=s.symbols('n Hn Hnext M',positive=True)
Jep=(1-2*lam*(w.subs(a,ep)+(n-1)*w0))/(1+ep);Rep=2*n/(1+ep)
der=s.simplify(s.diff(Jep-kk*Rep,ep).subs(ep,0))
ck('support_derivative',s.simplify(der-(-1+2*lam*c+2*lam*n*w0+2*n*kk))==0)
r,j,j0,j1=s.symbols('r j j0 j1',real=True);theta=(M-r)/(2*n+2-r)
chord=j0+(M-2*n)*(j1-j0)/2;mix=(1-theta)*j+theta*j1
ck('resource_restoration',s.simplify((1-theta)*r+theta*(2*n+2)-M)==0)
ck('feasible_chord_difference',s.simplify(mix-chord-(2*n+2-M)/(2*n+2-r)*(j-j0-(r-2*n)*(j1-j0)/2))==0)
# Rational log intervals and original-law witness evaluation.
def logbounds(q):
 q=F(q);u=(q-1)/(q+1);lo=2*sum((u**(2*j+1)/F(2*j+1) for j in range(8)),F(0));return lo,lo+2*u**17/(17*(1-u*u))
def add(x,y):return(x[0]+y[0],x[1]+y[1])
def mul(c,x):return(c*x[0],c*x[1]) if c>=0 else(c*x[1],c*x[0])
def ratlog_arg(a,b):return 1+(b-a)**2/(2*(a+b)*(2-a-b))
def law(stages):
 p=F(1);R=F(0);C=(F(0),F(0))
 for a,b in stages:
  p/=1+a;R+=2*p;C=add(C,mul(2*p,logbounds(ratlog_arg(a,b))))
 return p,C,R
A=law([(F(1,100),F(1,2))]);B=law([(F(0),F(1,4))]*2);E=law([(F(0),F(1,2))])
ck('actual_A_log_argument',ratlog_arg(F(1,100),F(1,2))==F(17599,15198))
ck('actual_resources',A[2]==F(200,101) and B[2]==4 and E[2]==2)
wa=F(101,204);wb=F(103,204);lam0=F(3,5)
ck('mixture_probability',wa+wb==1)
ck('actual_mixture_budget',wa*A[2]+wb*B[2]==3)
J=lambda law:add((law[0],law[0]),mul(-lam0,law[1]))
new=add(mul(wa,J(A)),mul(wb,J(B)));old=mul(F(1,2),add(J(E),J(B)));gap=add(new,mul(-1,old))
ck('strict_feasible_gain_lower',gap[0]>F(49,100000));ck('strict_feasible_gain_upper',gap[1]<F(1,2000))
ct('equal_weights_not_exact_budget',(A[2]+B[2])/2!=3)
ct('ignore_failure_trials_wrong_resource',wa*A[0]+2*wb*B[0]!=3)
ct('no_resource_repair_changes_budget',A[2]<2)
H1=logbounds(F(7,6));H2=mul(F(2),logbounds(F(15,14)))
common=add(mul(F(4),H1),mul(F(-2),H2))
rootlo=F(2236067977499789,10**15);roothi=F(2236067977499790,10**15)
ck('sqrt5_rational_bracket',rootlo**2<5<roothi**2)
safeden=add((6-2*roothi,6-2*rootlo),common);safe=(1/safeden[1],1/safeden[0])
failureden=add((F(32,21),F(32,21)),common);failure=(1/failureden[1],1/failureden[0])
ck('safe_lambda_interval',F(535190,10**6)<safe[0]<safe[1]<F(535191,10**6))
ck('failure_lambda_interval',F(536353,10**6)<failure[0]<failure[1]<F(536354,10**6))
ck('transition_bracket_width',failure[1]-safe[0]<F(1164,10**6))
ck('new_rational_multiplier_consumer',F(8,15)<safe[0])
ck('lambda_three_fifths_outside_safe',F(3,5)>failure[1])
ck('four_sevenths_exceeds_first_threshold',F(4,7)>failure[1])
# Execute the new positive consumer from actual schedule quantities.
positiveC=mul(F(1,2),add(E[1],B[1]));positiveP=(E[0]+B[0])/2;positiveR=(E[2]+B[2])/2
positiveJ=add((positiveP,positiveP),mul(-F(8,15),positiveC))
positiveFormula=add((F(1),F(1)),mul(-F(8,15),add(H1,H2)))
ck('new_positive_consumer_law',positiveP==1 and positiveR==3 and positiveJ==positiveFormula)
# Exact series supports count threshold limit; all-count proof in note.
ck('w0_series',s.series(w0,b,0,4).removeO()==b/4+3*b*b/32+7*b**3/192)
ck('c_series',s.series(c,b,0,3).removeO()==s.Rational(3,4)+b/16-3*b*b/64)
# An implemented scalar equation's expected-cost charge, not self-labelled flags.
ct('wrong_price_sign_derivative',s.simplify(s.diff(Jep+kk*Rep,ep).subs(ep,0)-der)==-4*n*kk)
report={'result':'K2579','evidence_kind':'exact action/mixture identities, global rational maximum, rational logarithm bounds and original-policy consumer; universal optimizer and convexity proofs in note','checks':checks,'contrary_controls':controls,'lambda_safe':[str(v) for v in safe],'lambda_failure_first_chord':[str(v) for v in failure],'positive_budget3_lambda_8_15':[str(v) for v in positiveJ],'budget3':{'new':[str(v) for v in new],'old':[str(v) for v in old],'gain':[str(v) for v in gap]},'ceiling':'exact enlarged post2 tail and transition bracket, not middle segment extension or intermediate optimizer'}
refs=['k2577-exact-resource-tail-2026-11-05','k2571-stopping-resource-price-2026-11-05']

report['provenance']={'explorations/conditional-build/'+r+'.md':hashlib.sha256((root/('explorations/conditional-build/'+r+'.md')).read_bytes()).hexdigest() for r in refs}
out=root/'lab/process/k2579-resource-tail-breakdown.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved report mismatch'
print(json.dumps({'result':'K2579','checks':len(checks),'controls':len(controls),'status':'pass'}))
