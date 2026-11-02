"""Exact algebra and rational inequality controls for the collective stopping proof."""
from pathlib import Path
from fractions import Fraction as F
import sympy as s
import json,hashlib,sys,itertools
ROOT=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ct(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
def prod(xs):
 out=F(1)
 for x in xs:out*=x
 return out
def log_bounds(x):
 # For x>=0, the integral of 1/(1+t) is between x/(1+x) and x.
 return x/(1+x),x
def warg(a,b):return (b-a)**2/(2*(a+b)*(2-a-b)) if a+b else F(0)
def cost_bounds(stages):
 p=F(1);lo=F(0);hi=F(0)
 for a,b in stages:
  p/=1+a;l,h=log_bounds(warg(a,b));lo+=2*p*l;hi+=2*p*h
 return p,lo,hi
S,d,x,b=s.symbols('S d x b',positive=True);L0=1+S
h=s.log(1+x*x/(2*(2*b-x)*(2-2*b+x)))
a2=1/(4*S*(1-S)*L0);ratio=1/L0-(2*S-1)/(2*S*(1-S));a3=a2*ratio
# Differentiate analytic factor instead of asking for an expensive nested inverse series.
q=x*x/(2*(2*S-x)*(2-2*S+x));cq=2/(L0-x)*q
ck('cost_quadratic',s.simplify(s.diff(cq,x,2).subs(x,0)/2-a2)==0)
ck('cost_cubic',s.simplify(s.diff(cq,x,3).subs(x,0)/6-a3)==0)
# log(1+q)-q starts at order x^4 because q starts at order x^2.
ck('log_remainder_order',s.simplify(q.subs(x,0))==0 and s.simplify(s.diff(q,x).subs(x,0))==0)
qS=s.cancel(-a3/(2*a2*a2*L0*L0)+1/(a2*L0**3))
ck('subleading_coefficient',s.factor(qS-(3*S-1)/(1+S)**2)==0)
ck('half_score_subleading',qS.subs(S,s.Rational(1,2))==s.Rational(2,9))
ck('third_score_zero_subleading',qS.subs(S,s.Rational(1,3))==0)
ck('leading_square',s.cancel(1/(a2*L0**4)-4*S*(1-S)/(1+S)**3)==0)
ck('hxx_at_zero',s.simplify(s.diff(h,x,2).subs(x,0)-1/(4*b*(1-b)))==0)
u=2*b-x;D=2*u*(2-u);N=D+x*x
ck('hessian_rational_identity',s.cancel(s.diff(h,x,2)-(4/D-2/N+s.diff(D,x)**2/D**2-s.diff(N,x)**2/N**2))==0)
ck('hb_factor',s.cancel(s.diff(h,b)+8*(1-u)*x*x/(D*N))==0)
ck('Nx_formula',s.expand(s.diff(N,x)-(8*b-4-2*x))==0)
# Continuous S=1/2 derivative certificate: exact endpoint arithmetic for inequalities in the note.
ck('rectangle_u_min',2*F(3,8)-F(1,8)==F(5,8))
ck('rectangle_D_min',2*F(5,8)*(2-F(5,8))==F(55,32))
ck('rectangle_M_bound',F(128,55)+F(48,55)**2<4)
ck('rectangle_L_bound',F(3072,3025)<2)
eps=F(1,2**14)
ck('explicit_case_one',24*eps<F(1,512))
ck('explicit_case_two',F(1,256)-8*eps-1024*eps*eps>0)
# Nontrivial many-satellite fixtures, preserving exact success with a recomputed main atom.
for score in [F(1,4),F(1,3),F(1,2)]:
 for dd in [F(1,10000)]:
  for n in [2,6]:
   for ratiof in [F(0),F(99,100),F(1)]:
    bs=[F(i+1,10**6) for i in range(n)];sat=[(ratiof*z,z) for z in bs];tt=sum(bs,F(0));vv=sum((bb-aa for aa,bb in sat),F(0));qq=prod(1+aa for aa,bb in sat)-1
    mainb=score-tt;maina=(1+score-dd)/(1+qq)-1;xx=mainb-maina
    if not 0<=maina<=mainb:continue
    tag=str((score,dd,n,ratiof));ck('fixed_success_'+tag,(1+maina)*(1+qq)==1+score-dd)
    ck('exact_delta_'+tag,xx-dd==((1+score-tt-dd)*qq-tt)/(1+qq))
    ck('product_bracket_'+tag,tt-vv<=qq<=2*tt)
    ck('deficiency_bracket_'+tag,score*tt/4-2*vv<=xx-dd<=3*tt)
    us=[aa+bb for aa,bb in sat];penalty=sum(((bb-aa)**2/(4*(aa+bb)) for aa,bb in sat),F(0))
    ck('collective_Cauchy_'+tag,penalty>=vv*vv/(8*tt))
    for order,stages in enumerate([[(maina,mainb)]+sat,sat+[(maina,mainb)],sat[:n//2]+[(maina,mainb)]+sat[n//2:]]):
     survival=F(1);final=1/(1+score-dd)
     for aa,bb in stages:
      survival/=1+aa;ck('weight_'+tag+str(order)+str((aa,bb)),survival>=final)
# A main-deficiency reduction without paying satellite cost can look profitable.
score=F(1,2);dd=F(1,100);tt=F(1,100000);vv=tt;qq=F(0)
mainb=score-tt;maina=score-dd;xx=mainb-maina
ct('omit_satellite_penalty_wrong_route',xx<dd and warg(maina,mainb)<warg(score-dd,score))
# Missing failure/survival weights changes genuine two-stage cost, not only a manifest.
a,b=F(1,10),F(1,5);p,lo,hi=cost_bounds([(a,b),(a,b)])
wlo,whi=log_bounds(warg(a,b));naive=4*p*whi
ct('survival_weight_omission',lo>naive)
# Leading square-root cannot be extended with a smaller coefficient at score1/2.
ct('wrong_subleading_sign',qS.subs(S,s.Rational(1,2))>0)
ct('split_without_success_repair',1/((1+F(49,100))*(1+F(1,1000)))!=1/(1+F(49,100)))
ck('fixed_S_coefficient_grows',a2.subs(S,s.Rational(1,100000))>10000)
# Tangent to p0+c sqrt(C) dominates all costs up to eta but needs a remote tail certificate.
p0=F(2,3);c=F(1,2);K=F(1,10**8);eta=F(1,100)
rootK=F(1,10000);intercept=p0+c*rootK/2;slope=c/(2*rootK)
ck('tangent_tail_actual_bound',intercept+slope*eta>1)
# Explicit interval and contrary finite-budget witness, both under the original cost law.
dstar=F(1,2**18);eta=F(1,2**40);Kstar=F(1,2**88)
ck('concentration_enters_rectangle',13*dstar<eps and dstar<F(1,16))
ck('explicit_local_cost_cutoff',eta==dstar*dstar/16 and eta<F(2,3)*dstar*dstar)
ck('global_bound_enters_success_interval',F(9,4)**2*2*eta<dstar*dstar)
ck('explicit_derivative_lower',F(8,243)>F(1,32))
ck('explicit_tangent_tail',Kstar==eta*eta/256 and F(2,3)+F(1,2)>1)
ck('one_stage_upper_coefficient',F(2)*F(8,11)*F(32,63)<1)
ck('one_stage_derivative_coefficient',2*F(1,8)+8<9)
stages=[(F(1,200),F(1,100)),(F(59,201),F(49,100))]
p=F(1);upper=F(0)
for a,b in stages:
 p/=1+a;z=warg(a,b);upper+=2*p*(z-z*z/2+z**3/3)
z=warg(F(3,10),F(1,2));lower=2*F(10,13)*(z-z*z/2)
ck('finite_counterpolicy_success',p==F(10,13))
ct('global_one_stage_extrapolation_fails',upper<F(317,10000)<lower)
ct('explicit_interval_not_counterbudget',Kstar<F(317,10000))
deps=['explorations/conditional-build/k2485-constrained-stopping-frontier-2026-11-02.md','explorations/conditional-build/k2499-sharp-small-budget-stopping-2026-11-02.md','explorations/conditional-build/k2493-multistage-stopping-advantage-2026-11-02.md']
# Resolve predecessor filenames without weakening their identity.
for i,p in enumerate(deps):
 if not (ROOT/p).exists():
  matches=list((ROOT/'explorations/conditional-build').glob(Path(p).name.split('-')[0]+'-*.md'));assert len(matches)==1;deps[i]=str(matches[0].relative_to(ROOT))
report={'result':'K2501','checks':checks,'contrary_controls':controls,'coefficients':{'leading_square':'4S(1-S)/(1+S)^3','linear':'(3S-1)/(1+S)^2'},'rectangle_certificate':{'S':'1/2','x':'[0,1/8]','b':'[3/8,1/2]','m':1,'M':4,'L':2,'epsilon':'1/16384','fixed_success_d':'1/262144','all_policy_budget':'2^-88'},'evidence_kinds':{'exact':'symbolic derivatives/series and rational multi-satellite controls','universal':'written collective exclusion, concentration and affine-mixture proof','not_claimed':'global one-stage optimum or native GU physics'},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2501-collective-stopping-satellites.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
else:ck('saved_report_reproduction',json.loads(out.read_text())==report)
print(json.dumps({'result':'PASS','checks':len(checks),'contrary_controls':len(controls)}))
