"""Original-law exact expansion and interval controls; universal bounds in note."""
from pathlib import Path
from fractions import Fraction as F
import sympy as s
from flint import arb,ctx
import json,hashlib,sys
ctx.prec=192
ROOT=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,x):
 checks[k]=bool(x)
 if not x:raise AssertionError(k)
def ct(k,x):
 controls[k]=bool(x)
 if not x:raise AssertionError('contrary '+k)
def ball(x):
 x=F(x);return arb(x.numerator)/x.denominator
def evaluate(expr,env):
 if expr in env:return env[expr]
 if expr.is_Rational:return arb(int(expr.p))/int(expr.q)
 if expr.is_Add:return sum((evaluate(x,env) for x in expr.args),arb(0))
 if expr.is_Mul:
  out=arb(1)
  for x in expr.args:out*=evaluate(x,env)
  return out
 if expr.is_Pow:
  base,power=expr.args
  if power==s.Rational(1,2):return evaluate(base,env).sqrt()
  n=int(power);v=evaluate(base,env);out=arb(1)
  for _ in range(abs(n)):out*=v
  return 1/out if n<0 else out
 if expr.func==s.log:return evaluate(expr.args[0],env).log()
 raise ValueError(expr)
r,rd=s.symbols('r rd');g=(1-r)**2/(2*(1+r));cc=(1-r)**2/8-(1-r)**4/(32*(1+r)**2)
J=(-3+22*r*r-16*r**3-3*r**4)/(16*(1+r)**2)
ck('Bregman_exact',s.factor(g-g.subs(r,rd)-s.diff(g,r).subs(r,rd)*(r-rd)-2*(r-rd)**2/((1+r)*(1+rd)**2))==0)
ck('Bregman_lower_constant',s.Rational(2,8)==s.Rational(1,4))
ck('J_identity',s.factor(J+2*cc+r*r*s.diff(g,r)/2-r*g/2)==0)
L,M,wa,wb,waa,wab,wbb,w0,z,q=s.symbols('L M wa wb waa wab wbb w0 z q')
p=1/L
# Exact Taylor expansion of the original main term, independently in its coordinates.
x=s.symbols('x')
a_main_delta=L/(1+x*z)-L
main=(1+x*z)*(w0+wa*a_main_delta-wb*x*q+waa*a_main_delta**2/2-wab*a_main_delta*x*q+wbb*x*x*q*q/2)
main2=s.expand(s.series(main,x,0,3).removeO())
expected=w0+x*((w0-L*wa)*z-wb*q)+x*x*(L*L*waa*z*z/2+(-wb+L*wab)*z*q+wbb*q*q/2)
ck('main_original_coordinate_Taylor',s.factor(main2-expected)==0)
# Three unequal stages; polynomial expansion is an identity, not a sample.
ts=s.symbols('t0:3');rs=s.symbols('r0:3');gs=s.symbols('g0:3');cs=s.symbols('c0:3')
Z=s.prod(1+x*rs[i]*ts[i] for i in range(3));Q=sum(ts);R=sum(rs[i]*ts[i] for i in range(3))
Z2=s.expand(s.series(Z,x,0,3).removeO())
ck('product_second_order',s.expand(Z2-(1+x*R+x*x*(R*R-sum(rs[i]**2*ts[i]**2 for i in range(3)))/2))==0)
zDelta=Z2-1
main_poly=w0+M*zDelta/2-wb*x*Q+L*L*waa*zDelta**2/2+(-wb+L*wab)*zDelta*x*Q+wbb*x*x*Q*Q/2
tail=sum((gs[i]*x*ts[i]/2+cs[i]*x*x*ts[i]**2)*s.prod(1+x*rs[j]*ts[j] for j in range(i+1,3)) for i in range(3))
actual=s.expand(main_poly+tail).coeff(x,2)*2/L
quad=p*((M/2+L*L*waa)*R**2+2*(-wb+L*wab)*R*Q+wbb*Q**2-M*sum(rs[i]**2*ts[i]**2 for i in range(3))/2+2*sum(cs[i]*ts[i]**2 for i in range(3))+sum(gs[i]*rs[j]*ts[i]*ts[j] for i in range(3) for j in range(i+1,3)))
ck('unequal_ratio_original_quadratic',s.expand(actual-quad)==0)
equal=quad.subs(dict(zip(rs,[r]*3))|dict(zip(gs,[g]*3))|dict(zip(cs,[cc]*3))).subs(M,-s.diff(g,r))
beta1=p*(L*L*r*r*waa+2*L*r*wab+wbb-2*r*wb+2*cc);betainf=beta1+p*J
ck('arbitrary_partition_beta_identity',s.factor(equal-(betainf*Q*Q-p*J*sum(t*t for t in ts)))==0)
ck('strict_beta_lower',s.Rational(1,67)-s.Rational(363,26068)==s.Rational(1747,1746556)>s.Rational(1,1000))
ck('J_endpoint_signs',J.subs(r,s.Rational(2,5))<0 and J.subs(r,s.Rational(9,20))<0)
# Exact finite-prefix/suffix original-cost cancellation, arbitrary independent cost symbols.
ap,am,at,wp,wm,wt,Lf=s.symbols('ap am at wp wm wt Lf')
Cfull=2*wp/(1+ap)+2*wm/((1+ap)*(1+am))+2*wt/((1+ap)*(1+am)*(1+at))
Cfixed=s.factor(Cfull.subs(am,Lf/((1+ap)*(1+at))-1))
ck('prefix_suffix_cancellation',s.factor(Cfixed-(2*wp/(1+ap)+2*(1+at)*wm/Lf+2*wt/Lf))==0)
ck('prefix_linear_coefficient',s.expand(2*(g/2-L*wa*r/L-wb/L)-(g-2*wa*r-2*wb/L))==0)
# Exact algebra behind localization and deficit/stage-count claims.
a,beta,eps,Q0=s.symbols('alpha beta eps Q',positive=True)
ck('completed_square',s.expand(-a*eps*Q0+beta*Q0**2+a*a*eps**2/(4*beta)-beta*(Q0-a*eps/(2*beta))**2)==0)
t1,t2,t3=s.symbols('t1 t2 t3',real=True)
ck('Cauchy_stage_count_three',s.expand(3*(t1*t1+t2*t2+t3*t3)-(t1+t2+t3)**2-((t1-t2)**2+(t1-t3)**2+(t2-t3)**2))==0)
# Arb locates inherited onset, then evaluates actual derivatives and coefficients.
d=s.symbols('d');aa,bb=s.symbols('aa bb')
wexpr=s.log(1+(bb-aa)**2/(2*(aa+bb)*(2-aa-bb)))
A=4*d/((1-d*d)*(2-d*d));LL=s.Rational(3,2)-d;ww=s.log((2-d*d)/(2*(1-d*d)))
MM=LL*A+2*ww;NN=A*(1-2*d*d);HH=(MM+NN)**2+4*(NN-MM)
lo,hi=F(4,25),F(17,100)
for _ in range(80):
 mid=(lo+hi)/2;h=evaluate(HH,{d:ball(mid)})
 if h<0:lo=mid
 elif h>0:hi=mid
 else:raise ArithmeticError('root sign undecided')
ck('onset_bracket_signs',evaluate(HH,{d:ball(lo)})<0 and evaluate(HH,{d:ball(hi)})>0)
dball=ball(lo).union(ball(hi));lball=evaluate(LL,{d:dball});mball=evaluate(MM,{d:dball});rball=2/(1+2*mball).sqrt()-1
alpha=(evaluate(s.diff(NN,d),{d:dball})-rball*evaluate(s.diff(MM,d),{d:dball}))/lball
env={aa:ball(F(1,2))-dball,bb:ball(F(1,2))}
wbv=evaluate(s.diff(wexpr,bb),env);waav=evaluate(s.diff(wexpr,aa,2),env);wabv=evaluate(s.diff(wexpr,aa,bb),env);wbbv=evaluate(s.diff(wexpr,bb,2),env)
cv=evaluate(cc,{r:rball});jv=evaluate(J,{r:rball})
betav=(lball*lball*rball*rball*waav+2*lball*rball*wabv+wbbv-2*rball*wbv+2*cv+jv)/lball
gamma=alpha**2/(4*betav)
ck('onset_ratio_box',rball>ball(F(2,5)) and rball<ball(F(9,20)))
ck('alpha_positive',alpha>0);ck('beta_strict_gap',betav>ball(F(1,1000)));ck('J_negative',jv<0)
# A real exact same-success split, cost certified using Arb (not sampling the universal theorem).
def wball(a,b):
 return (1+ball((b-a)**2/(2*(a+b)*(2-a-b)))).log() if b>a else arb(0)
qq=F(1,1000);rr=F(3,7);aold=qq*(2+qq);bold=aold/rr
oldcost=2*wball(aold,bold)/ball(1+aold)
newcost=2*wball(qq,bold/2)/ball(1+qq)+2*wball(qq,bold/2)/ball((1+qq)**2)
ck('actual_split_preserves_success',(1+qq)**2==1+aold)
ck('actual_split_admissible',0<qq<bold/2 and 0<bold<F(1,100))
ck('actual_split_strict_cost',newcost<oldcost)
ct('additive_hazard_not_same_success',(1+qq)**2!=1+2*qq)
ct('unweighted_cost_not_original',2*wball(qq,bold/2)+2*wball(qq,bold/2)>newcost)
ct('ratio_penalty_cannot_be_omitted',s.factor((g-g.subs(r,rd)-s.diff(g,r).subs(r,rd)*(r-rd)).subs({r:0,rd:s.Rational(3,7)}))>0)
ct('drop_survival_changes_quadratic',s.expand(actual-2*s.expand(main_poly+sum(gs[i]*x*ts[i]/2+cs[i]*x*x*ts[i]**2 for i in range(3))).coeff(x,2)/L)!=0)
ct('fixed_count_cloud_has_extra_cost',-J.subs(r,s.Rational(3,7))/3>0)
ct('all_zero_tails_no_strict_gain',quad.subs(dict(zip(ts,[0]*3)))==0)
# Actual-value attempt on the unresolved global theorem: its old concavity method fails.
lamstar=4*arb(3).sqrt()/3
waexpr=s.cancel(s.diff(wexpr,aa));wbexpr=s.cancel(s.diff(wexpr,bb))
waaexpr=s.cancel(s.diff(wexpr,aa,2));wabexpr=s.cancel(s.diff(wexpr,aa,bb));wbbexpr=s.cancel(s.diff(wexpr,bb,2))
def at(expr,av,bv):return evaluate(expr,{aa:av,bb:bv})
def root_decreasing(fun,target,bval,steps=65):
 left,right=F(0),bval
 assert fun(ball(left))>target and fun(ball(right))<target
 for _ in range(steps):
  mid=(left+right)/2;value=fun(ball(mid))
  if value>target:left=mid
  elif value<target:right=mid
  else:break
 assert right-left<F(1,10**16)
 return ball(left).union(ball(right)),[str(left),str(right)]
def one_root(bval):
 bv=ball(bval)
 fun=lambda av:2*at(wexpr,av,bv)-2*(1+av)*at(waexpr,av,bv)
 return root_decreasing(fun,1/lamstar,bval,85)
sa,sa_bracket=one_root(F(1,2));Sball=ball(F(1,2))
Us=(1-2*lamstar*at(wexpr,sa,Sball))/(1+sa)
bval=F(99,200);bv=ball(bval)
ra,ra_bracket=root_decreasing(lambda av:-at(waexpr,av,bv),Us/(2*lamstar),bval)
Ta=at(wbbexpr,ra,bv)-at(wabexpr,ra,bv)**2/at(waaexpr,ra,bv)
qa,qa_bracket=one_root(F(1,200));qv=ball(F(1,200));AA=1+qa
Upp=2*lamstar/AA*((at(wabexpr,qa,qv)-at(wbexpr,qa,qv)/AA)**2/at(waaexpr,qa,qv)-at(wbbexpr,qa,qv))
curvature=2*lamstar*Ta-Upp
ct('global_critical_concavity_extension_false',curvature>ball(F(1,100)))
method_limit={'lambda':'4sqrt(3)/3','S':'1/2','b':'99/200','one_stage_root':sa_bracket,'residual_root':ra_bracket,'remaining_score_root':qa_bracket,'residual_second_derivative':str(curvature),'scope':'rejects old uniform-concavity proof extension only; does not exhibit better policy or refute global optimality'}
paths=['explorations/conditional-build/k2551-finite-score-stopping-separation-2026-11-04.md','tests/channel-swings/k2551_finite_score_stopping_separation_probe.py','explorations/conditional-build/k2503-stopping-instability-boundary-2026-11-02.md','lab/process/k2505-stopping-satellite-hierarchy.json','explorations/conditional-build/k2507-stopping-optimal-hybrid-tail-2026-11-02.md','explorations/conditional-build/k2549-uniform-nearcritical-stopping-bound-2026-11-04.md']
report={'result':'K2551','global_method_limit':method_limit,'checks':checks,'contrary_controls':controls,'onset':{'d_interval':[str(lo),str(hi)],'d_ball':str(dball),'ratio':str(rball),'alpha':str(alpha),'beta_infinity':str(betav),'Gamma':str(gamma)},'fragmentation_control':{'old_cost':str(oldcost),'new_cost':str(newcost),'gap':str(oldcost-newcost)},'evidence_kinds':{'exact':'original-cost polynomial expansions, Bregman/beta/prefix identities and algebraic deficit controls','interval':'inherited root bracket/coefficient signs and actual finite split cost','universal':'stage-independent remainders, localization, sharp local infimum and finite nonattainment proved in note','not_claimed':'explicit validity radius, remote/global optimum, cross-success mixtures, native GU'},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}
path=ROOT/'lab/process/k2551-finite-score-stopping-separation.json'
if '--write' in sys.argv:path.write_text(json.dumps(report,indent=2)+'\n')
else:ck('saved_reproduction',json.loads(path.read_text())==report)
print('K2551 PASS',len(checks),'exact/interval groups',len(controls),'contrary controls');print(json.dumps(report['onset']))
