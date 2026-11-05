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



a,b=s.symbols('a b',positive=True);u=a+b;d=b-a;D=2*u*(2-u);N=D+d*d;w=s.log(N/D)
wa=s.cancel(s.diff(w,a));waa=s.cancel(s.diff(wa,a));c=lambda b:2*(3-2*b)/((2-b)*(4-b))
ck('original_derivative',s.cancel(wa.subs(a,0)+c(b))==0)
Dd=4*(u-1);Nd=2*a+6*b-4
ck('curvature_identity',s.cancel(waa-(4/D-2/N+Dd**2/D**2-Nd**2/N**2))==0)
ck('curvature_numerator_order',s.expand(Nd-Dd)==2*(b-a))
# Dd<=Nd<=0 and N>=D yield the stated curvature bound on the triangle.
ck('Nd_upper_corner',Nd.subs({a:b})==8*b-4)
ck('D_upper_for_curvature',s.expand(8*b-D)==2*a*a+4*a*b-4*a+2*b*b+4*b)
cp=s.cancel(s.diff(c(b),b));den=(b-4)**2*(b-2)**2
ck('c_derivative',s.cancel(cp-4*(b*b-3*b+1)/den)==0)
ck('one_sided_slope_numerator',s.expand(den-64*(b*b-3*b+1)-b*(b**3-12*b*b-12*b+96))==0)
ck('slope_remainder_positive',F(96)-12*F(1,2)**2-12*F(1,2)>0)
ck('n1_score_order',s.factor(c(b)-c(b/2)-2*b*(2*b-1)/((b-8)*(b-4)*(b-2)))==0)
m,n=s.symbols('m n',positive=True);gap=1/m-1/n-(n-m)/(n*(n+1))
ck('leading_convex_chord_gap',s.factor(gap-(n-m)*(n+1-m)/(m*n*(n+1)))==0)
S,A,lam,Q,jm,cm=s.symbols('S A lam Q jm cm',positive=True)
ck('quadratic_maximum',s.expand(2*cm*A-A*A/(4*S)-(4*S*cm*cm-(A-4*S*cm)**2/(4*S)))==0)
ck('gap_to_gain_ratio',s.cancel((3*S*S/s.Integer(32)*(n-m)*(n+1-m)/(m*n*(n+1)))/(2*S*(S*(n-m)/(16*m*n))**2)-12*m*n*(n+1-m)/(S*(n-m)*(n+1)))==0)
ct('omit_product_cross_term',(1+F(1,10))*(1+F(1,5))>1+F(1,10)+F(1,5))
ct('survival_not_all_terminal',1/(1+F(1,10))>1/((1+F(1,10))*(1+F(1,5))))
x=s.symbols('x');H=S/4+3*S*S*x/32+7*S**3*x*x/192
Hnext=H.subs(x,x/(1+x));Tseries=s.series((1/x+1)*H-Hnext/x,x,0,3).removeO()
Lstar=2/(3+S);threshold=1/(2*c(S*x)+2*Tseries)
ck('sharp_onset_asymptotic',s.cancel(s.diff(Lstar-threshold,x).subs(x,0)-Lstar**2*S*(1+3*S)/8)==0)
eps,k,Hm,cm=s.symbols('eps k Hm cm');fakew=Hm-cm*eps
J=(1-2*lam*fakew-2*k*n)/(1+eps)
ck('first_action_derivative',s.expand(s.diff(J,eps).subs(eps,0)-(2*lam*cm-(1-2*lam*Hm-2*k*n)))==0)
def lb(q):
 q=F(q);assert q>=1;u=(q-1)/(q+1);lo=2*sum((u**(2*j+1)/F(2*j+1) for j in range(16)),F(0));return lo,lo+2*u**33/(33*(1-u*u))
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def mul(c,a):return(c*a[0],c*a[1]) if c>=0 else(c*a[1],c*a[0])
def sub(a,b):return add(a,mul(-1,b))
def H(n,S=F(1,2)):return mul(n,lb((4-S/n)/(4-2*S/n)))
def T(n,S=F(1,2)):return sub(mul(n+1,H(n,S)),mul(n,H(n+1,S)))
def bound(n,S=F(1,2)):
 d=mul(2,add((F(c(S)),F(c(S))),T(n,S)));return 1/d[1],1/d[0]
def law(stages):
 p=F(1);C=(F(0),F(0));R=F(0)
 for a,b in stages:
  assert 0<=a<=b and b>0
  p/=1+a;R+=2*p;C=add(C,mul(2*p,lb(1+(b-a)**2/(2*(a+b)*(2-a-b)))))
 return p,C,R
def value(z,l):return add((z[0],z[0]),mul(-l,z[1]))

def sharp(n,S):
 den=mul(2,add((F(c(S/n)),F(c(S/n))),T(n,S)));return 1/den[1],1/den[0]
def onset(l,S):
 for n in range(1,1000):
  if l<=sharp(n,S)[0]:return n
 raise AssertionError('no tested onset')
def support(n,l,S):return sub((F(1),F(1)),mul(2*l,T(n,S)))
def priced(z,l,k):return sub(value(z,l),mul(z[2],k))
cons=[]
for label,l,score,want in [('half55',F(11,20),F(1,2),3),('half56',F(14,25),F(1,2),5),('half57',F(57,100),F(1,2),36),('quarter60',F(3,5),F(1,4),2)]:
 n=onset(l,score);ck(label+'_sharp_onset',n==want)
 ck(label+'_threshold_bracket',sharp(n-1,score)[1]<l<=sharp(n,score)[0])
 M=2*n+1;zn=law([(F(0),score/n)]*n);zp=law([(F(0),score/(n+1))]*(n+1))
 C=mul(F(1,2),add(zn[1],zp[1]));val=sub((F(1),F(1)),mul(l,C));kp=mul(l,sub(H(n,score),H(n+1,score)))
 ck(label+'_exact_budget',zn[0]==zp[0]==1 and (zn[2]+zp[2])/2==M)
 ck(label+'_global_support',support(n,l,score)[0]>=2*l*F(c(score/n)))
 # Actual original-law witness on preceding failing chord, sufficiently small action.
 r=n-1;action=F(1,10**8);old=law([(F(0),score/r)]*r);pert=law([(action,score/r)]+[(F(0),score/r)]*(r-1));up=law([(F(0),score/(r+1))]*(r+1));badM=F(2*r+1)
 q=(2*r+2-badM)/(2*r+2-pert[2]);mixv=add(mul(q,value(pert,l)),mul(1-q,value(up,l)));oldv=mul(F(1,2),add(value(old,l),value(up,l)));gain=sub(mixv,oldv)
 ck(label+'_restored_resource',q*pert[2]+(1-q)*up[2]==badM and 0<q<1)
 ck(label+'_strict_counterpolicy',gain[0]>0)
 ct(label+'_equal_weights_not_budget',(pert[2]+up[2])/2!=badM)
 # Both adjacent support conditions license a full price interval for count n+1.
 ck(label+'_released_price_interval',kp[0]>mul(l,sub(H(n+1,score),H(n+2,score)))[1]>0)
 cons.append({'label':label,'S':str(score),'lambda':str(l),'onset':n,'budget':M,'value':list(map(str,val)),'preceding_budget':str(badM),'counterpolicy_gain':list(map(str,gain))})
ck('new_regime_exceeds_old_limit',F(57,100)>F(84,149))
ct('wrong_fair_trial_charge',law([(F(0),F(1,4))]*2)[2]/2!=4)
ct('wrong_threshold_denominator',1/(F(c(F(1,10)))+2*T(5)[0])>sharp(5,F(1,2))[1])
ck('old_certificate56_minimum8',bound(7,F(1,2))[1]<F(14,25)<bound(8,F(1,2))[0])
ck('old_certificate56_still_fails_at5',F(14,25)>bound(5,F(1,2))[1])
ck('critical_limit_half',F(Lstar.subs(S,F(1,2)))==F(4,7))
ct('critical_all_finite_chord_consumers',all(sharp(n,F(1,2))[1]<F(4,7) for n in [1,2,5,36,100]))
ct('old_sufficient_not_sharp',bound(5,F(1,2))[1]<sharp(5,F(1,2))[0])
# Boundary: resource-repair weight is zero at the right endpoint, positive at left.
n=5;eps=F(1,1000);rp=2*n/(1+eps)
ck('left_endpoint_positive_mix',(2*n+2-2*n)/(2*n+2-rp)>0)
ct('right_endpoint_no_improvement_weight',(2*n+2-(2*n+2))/(2*n+2-rp)==0)
# Execute an interior price in the entire globally supported count6 interval.
ln=F(14,25);sn=F(1,2);count=6
klo=mul(ln,sub(H(count,sn),H(count+1,sn)));khi=mul(ln,sub(H(count-1,sn),H(count,sn)))
kmid=(klo[1]+khi[0])/2
ck('price6_interior',klo[1]<kmid<khi[0])
z6=law([(F(0),sn/count)]*count);q6=priced(z6,ln,(kmid,kmid))
ck('price6_original_law',z6[0]==1 and z6[2]==12)
ck('price6_both_global_endpoints',ln<sharp(count-1,sn)[0] and ln<sharp(count,sn)[0])
ck('price6_neighbor_exclusion',all(q6[0]>priced(law([(F(0),sn/r)]*r),ln,(kmid,kmid))[1] for r in [5,7]))
price_consumer={'count':count,'price':str(kmid),'value':list(map(str,q6)),'interval_lower':list(map(str,klo)),'interval_upper':list(map(str,khi))}
report={'result':'K2587','checks':checks,'contrary_controls':controls,'evidence_kind':'exact identities and rational original-law consumers; universal proof in note','consumers':cons,'price_consumer':price_consumer,'ceiling':'sharp finite-resource zero-action chord thresholds, not positive-action optimizer or new unrestricted-value theorem'}
refs=['explorations/conditional-build/k2581-score-sensitive-tail-transition-2026-11-05.md','explorations/conditional-build/k2585-eventual-stopping-tail-2026-11-05.md']
report['provenance']={f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in refs}
out=root/'lab/process/k2587-countwise-stopping-support.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved report mismatch'
print(json.dumps({'result':report['result'],'checks':len(checks),'controls':len(controls),'status':'pass','onsets':{x['label']:x['onset'] for x in cons}}))
