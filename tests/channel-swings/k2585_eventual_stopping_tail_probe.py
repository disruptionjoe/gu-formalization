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


a,b=s.symbols('a b',positive=True);arg=1+(b-a)**2/(2*(a+b)*(2-a-b));w=s.log(arg);wa=s.cancel(s.diff(w,a));c=lambda b:2*(3-2*b)/((2-b)*(4-b))
ck('actual_zero_action_derivative',s.cancel(wa.subs(a,0)+c(b))==0)
S=s.symbols('S',positive=True)
ck('score_sensitive_difference',s.factor(c(S)-c(S/2)-2*S*(2*S-1)/((S-8)*(S-4)*(S-2)))==0)
v,lam,k=s.symbols('v lam k',positive=True);f=(v-2*lam*w-2*k)/(1+a)
ck('suffix_derivative_identity',s.cancel(s.diff(f,a)-(-2*lam*wa-f)/(1+a))==0)
N,H0,H1,H2=s.symbols('N H0 H1 H2');T0=(N+1)*H0-N*H1;T1=(N+2)*H1-(N+1)*H2
ck('T_monotonicity_identity',s.expand(T0-T1-(N+1)*(H0-2*H1+H2))==0)
ck('count_support_value',s.expand(1-2*lam*H0-2*lam*(H0-H1)*N-(1-2*lam*T0))==0)
ct('wrong_count_charge',s.expand(1-2*lam*H0-lam*(H0-H1)*N-(1-2*lam*T0))!=0)
x=s.symbols('x');ck('geometric_bound_identity',s.factor(4/(1-2*x)-1/(1-x)-(3-2*x)/((1-2*x)*(1-x)))==0)
ck('geometric_domain_denominator',F(3,4)*F(7,8)==F(21,32))
ck('T_uniform_constant',F(3,16)/F(21,32)==F(2,7))
A=3*S*S/32;B=7*S**3/192;u=s.symbols('u');h=S/4+A*u+B*u*u
ht=S/4+A*u/(1+u)+B*u*u/(1+u)**2
ck('T_asymptotic',s.expand(s.series((1/u+1)*h-ht/u,u,0,3).removeO()-S/4-2*A*u-(-A+3*B)*u*u)==0)
lim=1/(2*c(S)+S/2);bn=1/(2*(c(S)+S/4+2*A*u+(-A+3*B)*u*u))
ck('threshold_asymptotic_coefficient',s.cancel(s.diff(lim-bn,u).subs(u,0)-3*lim**2*S**2/8)==0)
ct('certificate_not_sharp_for_count3',c(F(1,6))<c(F(1,2)))
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
l=F(11,20);score=F(1,2);cs=F(c(score));L=1/(2*cs+score/2)
ck('exact_limit_threshold',L==F(84,149))
bs=[bound(n) for n in range(1,5)];ck('above_full_frontier_threshold',l>bs[0][1]);ck('minimal_certificate_count3',bs[1][1]<l<bs[2][0])
ck('increasing_threshold_consumers',all(bs[i][1]<bs[i+1][0] for i in range(3)))
nsafe=4*l*score**2/(7*(1-l/L));ck('safe_count4',3<nsafe<=4)
three=law([(F(0),F(1,6))]*3);four=law([(F(0),F(1,8))]*4)
C7=mul(F(1,2),add(three[1],four[1]));F7=add((F(1),F(1)),mul(-l,C7));k3=mul(l,sub(H(3),H(4)))
ck('budget7_original_law',three[0]==four[0]==1 and (three[2]+four[2])/2==7)
ck('budget7_leakage',C7==add(mul(3,lb(F(23,22))),mul(4,lb(F(31,30)))))
ck('budget7_support',k3[0]>0 and 1-2*l*T(3)[1]>=2*l*cs)
ck('budget7_value_bracket',F(854516981547,10**12)<F7[0]<=F7[1]<F(854516981549,10**12))
one=law([(F(1,1000),score)]);two=law([(F(0),F(1,4))]*2);q=F(1001,2004)
p3=q*one[0]+(1-q)*two[0];C3=add(mul(q,one[1]),mul(1-q,two[1]));R3=q*one[2]+(1-q)*two[2]
ck('adverse_budget_exact',R3==3)
ck('adverse_log_argument',1+(score-F(1,1000))**2/(2*(score+F(1,1000))*(2-score-F(1,1000)))==F(1750999,1501998))
v3=add((p3,p3),mul(-l,C3));old3=sub((F(1),F(1)),mul(l,add(H(1),H(2))));gain=sub(v3,old3)
ck('positive_action_gain_certified',gain[0]>F(1,100000))
ct('equal_mix_does_not_restore_budget',(one[2]+two[2])/2!=3)
ct('forget_failure_trials_halves_budget',R3/2!=3)
ct('low_budget_tail_reuse_false',v3[0]>old3[1])
ct('count2_certificate_fails_not_counterexample',1-2*l*T(2)[0]<2*l*cs)
ct('limit_no_finite_count_certificate',all(1-2*L*T(n)[0]<2*L*cs for n in range(1,6)))
# Execute the finite certified price-window search with a proven tail bound.
AA=1-l/L
qprice=lambda n:mul(F(1,2*n),sub((F(1),F(1)),mul(2*l,add(H(n),(cs,cs)))))
inc=qprice(3);ck('positive_price_incumbent',inc[0]>0)
cut=int(AA/(2*inc[0]))+1
qs={n:qprice(n) for n in range(1,cut+1)}
ck('finite_price_tail_excluded',AA/(2*(cut+1))<inc[0])
ck('certified_price_max_count3',all(inc[0]>qv[1] for n,qv in qs.items() if n!=3))
ck('price_window_value',F(2535657570,10**12)<inc[0]<=inc[1]<F(2535657571,10**12))
ct('window_not_old_countprice2',inc[1]<mul(l,sub(H(2),H(3)))[0])
# A general-score consumer: the same certified routine at S=1/4.
quarter=F(1,4);Lq=1/(2*F(c(quarter))+quarter/2);lq=F(3,5)
ck('quarter_above_Lambda_below_limit',bound(1,quarter)[1]<lq<Lq)
Nq=next((n for n in range(1,50) if lq<bound(n,quarter)[0]),None);ck('quarter_eventual_support',Nq==2 and 1-2*lq*T(Nq,quarter)[1]>2*lq*F(c(quarter)))
report={'result':'K2585','checks':checks,'contrary_controls':controls,'evidence_kind':'exact identities and rational original-policy/support consumers; universal proof in note','thresholds':[list(map(str,v)) for v in bs],'Ncert_half':3,'Nsafe_half':4,'budget7_value':list(map(str,F7)),'budget3_gain':list(map(str,gain)),'price_window':list(map(str,inc)),'price_search_last_count':cut,'quarter_certificate_count':Nq,'ceiling':'sufficient eventual tail and exact criterion price window, not complete above-transition optimizer or sharp onset'}
refs=['k2581-score-sensitive-tail-transition-2026-11-05','k2583-complete-stopping-resource-frontier-2026-11-05']
report['provenance']={'explorations/conditional-build/'+r+'.md':hashlib.sha256((root/('explorations/conditional-build/'+r+'.md')).read_bytes()).hexdigest() for r in refs}
out=root/'lab/process/k2585-eventual-stopping-tail.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved report mismatch'
print(json.dumps({'result':report['result'],'checks':len(checks),'controls':len(controls),'status':'pass','price_search_last_count':cut,'quarter_N':Nq}))
