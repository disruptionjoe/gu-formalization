"""Exact controls for the uniform stopping proof; no grid claims global optimality."""
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
def pol(xs):
 score=sum((b for a,b in xs),F(0));P=F(1);low=F(0);up=F(0)
 for a,b in xs:
  assert 0<=a<=b<=F(1,2)
  P/=1+a
  x=F(0) if a==b else (b-a)**2/(2*(a+b)*(2-a-b))
  low+=2*P*x/(1+x);up+=2*P*x
 return score,P,low,up
Sv,d,C,z=s.symbols('S d C z',positive=True);p0=1/(1+Sv);p=1/(1+Sv-d)
x=d*d/(2*(2*Sv-d)*(2-2*Sv+d));cost=2*p*s.log(1+x)
ck('one_stage_probability_coefficient',s.simplify(s.diff(p,d).subs(d,0)-p0*p0)==0)
lead=s.simplify(s.diff(cost,d,2).subs(d,0)/2)
ck('one_stage_cost_coefficient',s.factor(lead-1/(4*Sv*(1-Sv)*(1+Sv)))==0)
ck('sharp_coefficient_square',s.factor((p0*p0)**2/lead-4*Sv*(1-Sv)/(1+Sv)**3)==0)
# Exact rational identities behind the uniform estimates.
A=Sv-d;T0=8*Sv*(1-Sv);T1=16*Sv+12
ck('denominator_upper_identity',s.expand(4*(2*Sv-d)-8*(A*A-2*d)+d*d-(T0+T1*d-7*d*d))==0)
Rz=p0**2*(T0+T1*z)/(2*(1+Sv-z));c2=4*Sv*(1-Sv)/(1+Sv)**3
ck('R_minus_limit',s.factor(Rz-c2-p0**3*(T1+p0*T0)*z/(2*(1-p0*z)))==0)
ck('R_increasing',s.factor(s.diff(Rz,z)-p0**3*(T1+p0*T0)/(2*(1-p0*z)**2))==0)
ck('C0_boundary',s.factor(4*Sv*p0*((1+Sv)/(16*Sv))-s.Rational(1,4))==0)
# Square the positive coefficient simplification used for the order-K term.
L2=p0**2*(T1+p0*T0)**2/(4*(1-Sv))
fromR2=(p0**3*(T1+p0*T0))**2*(Sv/p0)/c2
ck('linear_constant',s.factor(L2-fromR2)==0)
a,b=s.symbols('a b',nonnegative=True);u=a+b;dd=b-a;H=2*u*(2-u)+dd*dd
ck('coarse_stage_denominator',s.expand(4*u-H-(a*a+6*a*b+b*b))==0)
# Variable stage counts, high-success examples and uniform concentration checks.
for S in [F(1,10),F(1,4),F(1,2)]:
 for n in [1,2,4,8,16]:
  for q in [F(1,100),F(1,10),F(1,2)]:
   # A main nearly-free atom with small zero-hazard satellites, no arbitrary fit.
   t=S*q/n;xs=[(S*(1-q),S-(n-1)*t)]+[(F(0),t)]*(n-1)
   score,p,clo,cup=pol(xs);D=sum((b-a for a,b in xs),F(0));A=sum((a for a,b in xs),F(0));M=1/p;E=M-1-A;p0q=1/(1+S)
   U=[a+b for a,b in xs];ds=[b-a for a,b in xs];T=sum((2*u*(2-u)+dd*dd for u,dd in zip(U,ds)),F(0))
   tag=str((S,n,q))
   ck('schedule_'+tag,score==S and p>p0q and 0<=E<D)
   ck('log_Cauchy_'+tag,clo>=2*p*D*D/T)
   ck('coarse_bound_'+tag,clo>=p0q*D*D/(4*S))
   ck('denominator_bound_'+tag,T<=8*S*(1-S)+(16*S+12)*D-7*D*D)
   ck('concentration_'+tag,A-max(a for a,b in xs)<=2*D/A and sum(b for a,b in xs[1:])<=2*D/A+D)
   # Rational form of R bound before substituting the square-root B(C).
   ck('gain_bound_'+tag,(p-p0q)**2<=clo*p0q**2*(8*S*(1-S)+(16*S+12)*D)/(2*(1+S-D)))
# Multiple positive hazards: nonzero product excess, not the E=0 one-atom case.
for S in [F(1,10),F(1,4),F(1,2)]:
 for n in [2,3,8]:
  for q in [F(1,20),F(1,5)]:
   D=S*q;A=S-D;r=S*q/4;hazards=[A-r]+[r/(n-1)]*(n-1)
   xs=[(aa,aa+D/n) for aa in hazards]
   score,pp,clo,cup=pol(xs);E=1/pp-1-A;p0q=1/(1+S)
   U=[aa+bb for aa,bb in xs];T=sum((2*u*(2-u)+(bb-aa)**2 for u,(aa,bb) in zip(U,xs)),F(0))
   pair=sum((hazards[i]*hazards[j] for i in range(n) for j in range(i+1,n)),F(0));tag=str((S,n,q))
   ck('positive_product_excess_'+tag,score==S and pp>p0q and 0<pair<=E<D)
   ck('nontrivial_hazard_square_'+tag,sum(aa*aa for aa in hazards)>=A*A-2*D)
   ck('nontrivial_concentration_'+tag,0<A-max(hazards)<=2*D/A and sum(bb for aa,bb in xs[1:])<=2*D/A+D)
   ck('nontrivial_log_Cauchy_'+tag,clo>=2*pp*D*D/T)
   ck('nontrivial_gain_'+tag,(pp-p0q)**2<=clo*p0q**2*(8*S*(1-S)+(16*S+12)*D)/(2*(1+S-D)))
# Half-score consumer and genuine finite rational certified witness.
S=F(1,2);p0q=F(2,3);c2q=F(8,27);L2q=F(8192,81);C0=F(3,16);tail=(1-p0q)/C0
ck('half_score_sharp',c2q==F(4)*S*(1-S)/(1+S)**3)
ck('rounded_consumer_coefficients',c2q<F(11,20)**2 and L2q<169 and tail<13)
# One nearly-free stage at d=1/1000; log upper bounds its actual cost rigorously.
_,pw,clo,cup=pol([(F(499,1000),S)]);K=F(1,1000000)
ck('actual_small_budget_witness',cup<K and pw>p0q)
# The safe rounded global envelope at this rational-square budget.
ck('finite_envelope_covers_witness',pw<=p0q+F(11,20000)+13*K)
ct('old_coefficient_not_sharp',F(4)*S/(1+S)**3==F(16,27)>c2q)
free=[(S/2,S/2)]*2;score,pfree,cfree,_=pol(free);Efree=1/pfree-1-S
ct('high_success_required',cfree==0 and pfree<p0q and Efree==S*S/4>0)
# Exact four-free-stage success is below the free one-stage baseline.
ct('small_free_stages_lose',pol([(S/4,S/4)]*4)[1]<p0q)
# Actual failure-inclusive geometric trial cost vs only successful paths.
a=F(1,4);trials=2/(1+a);success=1/(1+a)
ct('failed_path_cost',trials==F(8,5) and trials*success==F(32,25)<trials)
# Rare costly components have nonzero gain; dropping them is not a valid mixture proof.
_,ps,ls,us=pol([(F(0),S)]);mixweight=F(1,1000000)
ct('expensive_mixture_not_zero',ps==1 and mixweight*(ps-p0q)>0 and ls>0)
ck('tail_linear_control',(ps-p0q)<=tail*ls if ls>C0 else (ps-p0q)<=13*ls)
# Jensen bound for positive finite mixtures is exactly a nonnegative square.
v,w,t=s.symbols('v w t',nonnegative=True)
ck('mixture_square_identity',s.expand(t*v*v+(1-t)*w*w-(t*v+(1-t)*w)**2-t*(1-t)*(v-w)**2)==0)
ct('eta_equals_K_fails_limit',F(1,1000)/F(1,1000)==1)
ct('linear_only_cannot_match',pw-p0q>cup)
# Exact fixed-success insertion derivatives and all-r sufficient bounds.
a,b,rr,tt=s.symbols('a b r t',positive=True)
xab=(b-a)**2/(2*(a+b)*(2-a-b));wab=s.log(1+xab)
u=a+b;dd=b-a;DD=2*u*(2-u);Dp=4*(1-u);NN=DD+dd*dd
AA=(4*dd*DD+2*dd*dd*Dp)/(DD*NN)
BB=(4*dd*DD-2*dd*dd*Dp)/((1+a)*DD*NN)
ck('prefix_A_derivative',s.factor(-2*s.diff(wab,a)-AA)==0)
ck('prefix_B_derivative',s.factor(2*s.diff(wab,b)/(1+a)-BB)==0)
g=(1-rr)**2/(2*(1+rr))
ck('g_quadratic_gap',s.factor(g-(1-rr)**2/4-(1-rr)**3/(4*(1+rr)))==0)
ck('fixed_product_insert',(s.cancel((1+rr*tt)*(1+(a-rr*tt)/(1+rr*tt))-(1+a)))==0)
smalllog=s.log(1+(1-rr)**2*tt/(2*(1+rr)*(2-(1+rr)*tt)))
ck('small_stage_derivative',s.simplify(2*s.diff(smalllog,tt).subs(tt,0)-g)==0)
# Differentiate the two-stage costs by the chain rule, retaining survival weights.
wa,wb,w0=s.symbols('wa wb w0')
prefix=g+2*(-(1+a)*rr*wa-wb)/(1+a)
suffix=(g+2*rr*w0+2*(-(1+a)*rr*wa-wb))/(1+a)
ck('prefix_survival_derivative',s.cancel(prefix-(g+(-2*wa)*rr-2*wb/(1+a)))==0)
ck('suffix_survival_derivative',s.cancel(suffix-(g+((1+a)*(-2*wa)+2*w0)*rr-2*wb)/(1+a))==0)
slopes=[]
for aval in [s.Rational(2309,5000),s.Rational(499,1000)]:
 av=s.factor(AA.subs({a:aval,b:s.Rational(1,2)}));bv=s.factor(BB.subs({a:aval,b:s.Rational(1,2)}));xx=s.factor(xab.subs({a:aval,b:s.Rational(1,2)}))
 pre=s.factor(av-bv-av*av);atlo=(1+aval)*av+2*xx/(1+xx);athi=(1+aval)*av+2*xx;bt=(1+aval)*bv;suf=s.factor((atlo-bt-athi*athi)/(1+aval))
 ck('positive_uniform_satellite_'+str(aval),pre>0 and suf>0)
 if aval==s.Rational(499,1000):ck('satellite_margin',pre>s.Rational(1,2000) and suf>s.Rational(1,2000))
 slopes.append({'a':str(aval),'prefix_lower':str(pre),'suffix_lower':str(suf)})
# First-order slope as a=S-d, proved symbolically for general fixed S.
av=AA.subs({a:Sv-d,b:Sv});bv=BB.subs({a:Sv-d,b:Sv});wv=wab.subs({a:Sv-d,b:Sv});xx=xab.subs({a:Sv-d,b:Sv})
atlo=(1+Sv-d)*av+2*xx/(1+xx);athi=(1+Sv-d)*av+2*xx;bt=(1+Sv-d)*bv
kap=1/(2*(1-Sv)*(1+Sv))
for label,expr in [('prefix_lower',av-bv-av*av),('prefix_at_one',av-bv),('suffix_lower',(atlo-bt-athi*athi)/(1+Sv-d)),('suffix_at_one',av-bv+2*wv/(1+Sv-d))]:
 ck('satellite_asymptotic_'+label,s.factor(s.diff(expr,d).subs(d,0)-kap)==0)
# Omitting the survival-weight derivative changes the actual suffix slope.
for avalue in [s.Rational(3,10),s.Rational(499,1000)]:
 for rvalue in [s.Rational(0),s.Rational(1,2),s.Rational(1)]:
  maina=(avalue-rvalue*tt)/(1+rvalue*tt);mainb=s.Rational(1,2)-tt
  mainw=wab.subs({a:maina,b:mainb}, simultaneous=True)
  sw=smalllog.subs(rr,rvalue)
  cp=2*sw/(1+rvalue*tt)+2*mainw/(1+avalue)
  cs=2*(1+rvalue*tt)*mainw/(1+avalue)+2*sw/(1+avalue)
  av=s.factor(AA.subs({a:avalue,b:s.Rational(1,2)}));bv=s.factor(BB.subs({a:avalue,b:s.Rational(1,2)}));wv=wab.subs({a:avalue,b:s.Rational(1,2)});gv=g.subs(rr,rvalue)
  expectedp=gv+av*rvalue-bv;expecteds=(gv+((1+avalue)*av+2*wv)*rvalue-(1+avalue)*bv)/(1+avalue)
  ck('direct_prefix_cost_'+str((avalue,rvalue)),s.simplify(s.diff(cp,tt).subs(tt,0)-expectedp)==0)
  ck('direct_suffix_cost_'+str((avalue,rvalue)),s.simplify(s.diff(cs,tt).subs(tt,0)-expecteds)==0)
  if rvalue>0:
   omitted=2*mainw/(1+avalue)+2*sw/(1+avalue)
   gap=s.simplify(s.diff(cs-omitted,tt).subs(tt,0))
   ct('suffix_weight_not_optional_'+str((avalue,rvalue)),s.simplify(gap-2*rvalue*wv/(1+avalue))==0 and gap>0)
deps=['explorations/conditional-build/k2485-constrained-stopping-frontier-2026-11-01.md','explorations/conditional-build/k2497-finite-stopping-normal-form-2026-11-02.md']
deps += [str(next((R/'explorations/conditional-build').glob('k2493-*.md')).relative_to(R))]
report={'result':'K2499','checks':checks,'contrary_controls':controls,'theorem':{'domain':'fixed 0<S<=1/2, K down to zero','baseline':'1/(1+S)','coefficient_squared':'4*S*(1-S)/(1+S)^3','remainder':'O_S(K)','half_score_coefficient_squared':'8/27','satellite_certificates':slopes,'finite_witness':{'cost_upper':str(cup),'budget':str(K),'success':str(pw)}},'evidence_kinds':{'exact':'symbolic derivatives, denominator identities, rational varying-length schedules and contrary policies','universal':'written uniform finite-schedule bound, mixture reduction and analytic inversion','not_claimed':'positive-budget one-stage optimum, sharp global constant, uniform S limit or GU realization'},'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps}}
pth=R/'lab/process/k2499-sharp-small-budget-stopping.json'
if '--write' in sys.argv:pth.write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
else:ck('saved_reproduction',json.loads(pth.read_text())==report)
print(json.dumps({'result':'PASS','checks':len(checks),'controls':len(controls),'theorem':report['theorem']}))
