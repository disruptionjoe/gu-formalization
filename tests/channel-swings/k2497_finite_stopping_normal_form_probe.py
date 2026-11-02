"""Exact identity and contrary controls; universal arguments in the K2497 note."""
from pathlib import Path
from fractions import Fraction as F
import sympy as s
import json,hashlib,sys
R=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ct(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
def arg(a,b):
 if not 0<=a<=b<=F(1,2):raise ValueError('stage domain')
 return F(1) if a==b else 1+(b-a)**2/(2*(a+b)*(2-a-b))
def policy(xs):
 p=F(1);score=F(0);terms=[]
 for a,b in xs:
  z=arg(a,b);p/=1+a;score+=b;terms.append((2*p,z))
 return p,score,terms
old=[(F(1,10),F(1,10)),(F(1,10),F(1,10)),(F(1,20),F(3,10))]
new=[(F(21,100),F(21,100)),(F(1,20),F(29,100))]
p,S,co=policy(old);pn,Sn,cn=policy(new)
ck('exact_success_score',p==pn==F(2000,2541) and S==Sn==F(1,2))
ratio=co[-1][1]/cn[-1][1];gain_lower=2*p*(ratio-1)/ratio
ck('log_cost_gain_argument',ratio==F(687157,685146))
ck('strict_cost_gain',gain_lower>F(1,250))
# Actual coalescence algorithm, with proportional slack allocation avoiding new free stages.
def merge_free(xs):
 fs=[(a,b) for a,b in xs if a==b and b>0];paid=[(a,b) for a,b in xs if b>a]
 T=sum((b for a,b in fs),F(0));B=F(1)
 for a,b in fs:B*=1+b
 B-=1;delta=B-T;slack=sum((b-a for a,b in paid),F(0))
 if delta and slack<=delta:raise ValueError('high-success slack required')
 out=([(B,B)] if B else [])+[(a,b-delta*(b-a)/slack if delta else b) for a,b in paid]
 return out,delta
for x in [F(1,20),F(1,10),F(1,8)]:
 for y in [F(1,20),F(1,10)]:
  xs=[(x,x),(y,y),(F(1,100),F(1,2)-x-y)]
  pp,ss,tt=policy(xs);zz,delta=merge_free(xs);pp2,ss2,tt2=policy(zz)
  ck('merge_invariants_'+str((x,y)),pp==pp2 and ss==ss2 and pp>F(2,3) and all(a<=b for a,b in zz))
  ck('merge_strict_'+str((x,y)),tt[-1][0]==tt2[-1][0] and tt[-1][1]>tt2[-1][1] and delta==x*y)
# Saturating a paid slack creates a new free stage; a second merge removes it.
created=[(F(1,10),F(1,10)),(F(1,10),F(1,10)),(F(1,100),F(1,50)),(F(1,50),F(7,25))]
mid=[(F(21,100),F(21,100)),(F(1,100),F(1,100)),(F(1,50),F(7,25))]
end=[(F(2221,10000),F(2221,10000)),(F(1,50),F(2779,10000))]
pc,sc,tc=policy(created);pm,sm,tm=policy(mid);pe,se,te=policy(end)
ck('newly_free_iteration_invariants',pc==pm==pe and sc==sm==se==F(1,2) and pc>F(2,3))
ck('newly_free_iteration_cost',tc[-1][0]==tm[-1][0]==te[-1][0] and tc[-2][1]>1 and tm[-2][1]==1 and tm[-1][1]>te[-1][1])
a,b,k,pv,Sv=s.symbols('a b k p S',real=True)
x=(b-a)**2/(2*(a+b)*(2-a-b));dx=(b-a)*(3*a+b-2*a*a-2*a*b)/((a+b)**2*(2-a-b)**2)
ck('fixed_a_derivative',s.factor(s.diff(x,b)-dx)==0)
f=s.log((4-b)/(4-2*b));f2=4*(3-b)/((4-b)**2*(2-b)**2)
ck('zero_hazard_convexity_identity',s.factor(s.diff(f,b,2)-f2)==0)
ratio0=arg(F(0),F(1,2))/arg(F(0),F(1,4))**2
ck('zero_hazard_split_ratio',ratio0==F(686,675))
ck('zero_hazard_gain',2*(ratio0-1)/ratio0==F(11,343))
# Strict log lower bound gives > this rational value.
D=2*(a+b)*(2-a-b);d=b-a
ck('stage_bound_identity',s.expand(4*(a+b)-(D+d*d)-(a*a+6*a*b+b*b))==0)
for aa,bb in [(F(0),F(1,10)),(F(1,20),F(1,4)),(F(1,4),F(1,2))]:
 xx=arg(aa,bb)-1
 ck('stage_lower_'+str((aa,bb)),xx/(1+xx)>=(bb-aa)**2/(4*(aa+bb)))
def lower(S,p):return max(F(0),(1+S)*p-1)**2/(2*(1+(S-1)*p))
num=((1+Sv)*pv-1)**2-2*k*(1+(Sv-1)*pv)
rad=4*Sv*(1+Sv)*k+(1-Sv)**2*k*k
center=1+Sv-(1-Sv)*k
ck('quadratic_inverse_identity',s.expand((1+Sv)**2*num-(((1+Sv)**2*pv-center)**2-rad))==0)
L=((1+Sv)*pv-1)**2/(2*(1+(Sv-1)*pv))
ck('convexity_identity',s.factor(s.diff(L,pv,2)-4*Sv**2/(1+(Sv-1)*pv)**3)==0)
ck('baseline',lower(F(1,2),F(2,3))==0)
ck('critical_budget',lower(F(1,2),F(1))==F(1,4))
ck('upper_below_691_thousandths',lower(F(1,2),F(691,1000))>F(1,1000))
ck('upper_above_existing_certificate',lower(F(1,2),F(684885741753,10**12))<F(1,1000))
# Finite original trial occupancy: one geometric stage, then abort after a use if score insufficient.
# For target equal b, p=1/(1+a), expected trials=2/(1+a); includes failed trials.
for aa,bb in [(F(1,20),F(1,2)),(F(1,5),F(1,2)),(F(1,2),F(1,2))]:
 pp=1/(1+aa);A=2*aa*pp;B=2*bb*pp;xx=arg(aa,bb)-1
 costlo=2*pp*xx/(1+xx)
 ck('actual_occupation_'+str(aa),A==2*(1-pp) and B==2*bb*pp)
 ck('actual_cost_bound_'+str(aa),costlo>=lower(bb,pp))
ct('merge_sum_only_changes_success',policy([(F(1,5),F(1,5)),old[-1]])[0]!=p)
ct('merge_without_score_repair_changes_target',policy([(F(21,100),F(21,100)),old[-1]])[1]!=S)
ct('positive_part_essential',lower(F(1,2),F(1,2))==0 and ((1+F(1,2))*F(1,2)-1)**2>0)
# Geometric one-stage expected-cost coefficients include terminal failures.
aa=F(1,4);u=F(1,2);tt=1-u;haz=u+tt*aa;success=u/haz
all_cost_coefficient=1/haz;success_only_coefficient=success/haz
ct('failed_paths_cannot_be_dropped',all_cost_coefficient==F(8,5) and success_only_coefficient==F(32,25) and success_only_coefficient<all_cost_coefficient)
u=F(1,3);tt=1-u;haz=u+tt*aa;A=aa/haz;failure=tt*aa/haz
ct('fair_coin_factor_essential',A==F(1,2) and failure==F(1,3) and A!=2*failure)
ct('zero_hazard_not_finite_optimum',ratio0>1)
ct('new_bound_does_not_beat_k2491',lower(F(1,2),F(684885741753,10**12))<F(1,1000))
ct('all_free_outside_high_success',(1+F(1,10))**2-1>F(1,5))
for bad in [(F(-1),F(1,2)),(F(1,2),F(1,4))]:
 try:arg(*bad);rejected=False
 except ValueError:rejected=True
 ct('invalid_stage_'+str(bad),rejected)
deps=['explorations/conditional-build/k2495-stopping-order-and-continuum-2026-11-02.md','explorations/conditional-build/k2485-constrained-stopping-frontier-2026-11-01.md','explorations/conditional-build/k2491-stopping-jensen-bernstein-2026-11-02.md']
# Resolve the exact existing K2491 filename instead of inventing its spelling.
deps[-1]=str(next((R/'explorations/conditional-build').glob('k2491-*.md')).relative_to(R))
report={'result':'K2497','checks':checks,'contrary_controls':controls,'witness':{'old':[[str(a),str(b)] for a,b in old],'new':[[str(a),str(b)] for a,b in new],'success':str(p),'score':str(S),'gain_log_argument':str(ratio),'gain_lower':str(gain_lower)},'analytic_bound':'positive_part((1+S)*p-1)^2/(2*(1+(S-1)*p))','evidence_kinds':{'universal':'written free coalescence, convex splitting, nonnegative occupancy and Cauchy proof','exact':'symbolic identities and rational finite witnesses','not_claimed':'sharp global positive-budget optimum, finite attainment, GU recovery, hardware or novelty'},'dependencies':{f:hashlib.sha256((R/f).read_bytes()).hexdigest() for f in deps}}
pth=R/'lab/process/k2497-finite-stopping-normal-form.json'
if '--write' in sys.argv:pth.write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
else:ck('saved_reproduction',json.loads(pth.read_text())==report)
print(json.dumps({'result':'PASS','checks':len(checks),'controls':len(controls),'witness':report['witness']}))
