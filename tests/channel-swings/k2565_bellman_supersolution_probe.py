"""Exact whole-domain Bellman certificate; adaptive transfer is proved in the note."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
from itertools import product
import argparse, hashlib, json
import sympy as sy

ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');ap.add_argument('--root',type=Path);ap.add_argument('--scout',action='store_true');ap.add_argument('--draft',action='store_true');args=ap.parse_args()
ROOT=args.root or Path(__file__).resolve().parents[2]
checks={};controls={}
def ck(name,condition):
 checks[name]=bool(condition)
 if not condition: raise AssertionError(name)
def ct(name,condition):
 controls[name]=bool(condition)
 if not condition: raise AssertionError('contrary: '+name)
lam=F(19,10);c=F(3221,5000);d=F(1337,10000)
r,y,z=sy.symbols('r y z');b=y/2;s=b+(sy.Rational(1,2)-b)*z
D=8*(1+r)-b*(3+10*r+3*r*r)
U=lambda t:1-sy.Rational(c.numerator,c.denominator)*t+sy.Rational(d.numerator,d.denominator)*t*t
P=sy.Poly(sy.expand(D*(r*U(s)-sy.Rational(c)+2*sy.Rational(d)*s-sy.Rational(d)*b)+sy.Rational(38,5)*(1-r)**2),r,y,z)
ns=P.degree_list();indices=list(product(*(range(n+1) for n in ns)))
power={k:F(int(q.p),int(q.q)) for k,q in P.terms()}
def bernstein(power):
 return {k:sum((v*F(comb(k[0],j[0]),comb(ns[0],j[0]))*F(comb(k[1],j[1]),comb(ns[1],j[1]))*F(comb(k[2],j[2]),comb(ns[2],j[2])) for j,v in power.items() if all(j[i]<=k[i] for i in range(3))),F(0)) for k in indices}
B=bernstein(power)
# Independent inverse expansion authenticates the basis conversion, not just its sign.
inverse={}
for k,v in B.items():
 for off in product(*(range(ns[i]-k[i]+1) for i in range(3))):
  j=tuple(k[i]+off[i] for i in range(3));coef=v
  for i in range(3):coef*=comb(ns[i],k[i])*comb(ns[i]-k[i],off[i])*(-1)**off[i]
  inverse[j]=inverse.get(j,F(0))+coef
ck('power_to_Bernstein_inverse',all(inverse.get(k,F(0))==power.get(k,F(0)) for k in indices))
ck('polynomial_multidegree',ns==(3,3,2))
def split(coeff,axis):
 lo={};hi={};other=[i for i in range(3) if i!=axis]
 for rest in product(*(range(ns[i]+1) for i in other)):
  key=[0]*3
  for i,k in zip(other,rest):key[i]=k
  vals=[]
  for j in range(ns[axis]+1):key[axis]=j;vals.append(coeff[tuple(key)])
  left=[vals[0]];right=[vals[-1]]
  while len(vals)>1:
   vals=[(vals[j]+vals[j+1])/2 for j in range(len(vals)-1)];left.append(vals[0]);right.append(vals[-1])
  for j in range(ns[axis]+1):key[axis]=j;lo[tuple(key)]=left[j];hi[tuple(key)]=right[-1-j]
 return lo,hi
# Authenticate one split in each axis against a fresh affine power substitution.
for axis,var in enumerate((r,y,z)):
 lo,hi=split(B,axis)
 for tag,actual,sub in [('left',lo,var/2),('right',hi,(var+1)/2)]:
  pp=sy.Poly(P.as_expr().subs(var,sub),r,y,z)
  pw={k:F(int(q.p),int(q.q)) for k,q in pp.terms()}
  ck('de_Casteljau_'+str(axis)+'_'+tag,actual==bernstein(pw))
stack=[(B,0,'')];leaves=[]
while stack:
 coeff,depth,path=stack.pop();minimum=min(coeff.values())
 if minimum>0:
  leaves.append((path,depth,minimum,coeff));continue
 if depth>=24:raise AssertionError('uncertified leaf '+path)
 lo,hi=split(coeff,depth%3);stack.extend([(lo,depth+1,path+'0'),(hi,depth+1,path+'1')])
minimum=min(row[2] for row in leaves);depth=max(row[1] for row in leaves)
ck('leaf_cover_volume',sum((F(1,2**row[1]) for row in leaves),F(0))==1)
ck('leaf_paths_prefix_free',not any(a[0]!=bb[0] and bb[0].startswith(a[0]) for a in leaves for bb in leaves))
ck('all_leaf_coefficients_strictly_positive',minimum>0)
ck('certificate_leaf_count',len(leaves)==120)
ck('certificate_max_depth',depth==16)
ck('certificate_minimum',minimum==F(268141,1966080000))
certificate_rows=[{'path':p,'depth':dep,'coefficients':[str(co[k]) for k in indices]} for p,dep,m,co in sorted(leaves)]
certificate_digest=hashlib.sha256(json.dumps(certificate_rows,sort_keys=True,separators=(',',':')).encode()).hexdigest()
x=sy.symbols('x',nonnegative=True)
ck('log_lower_derivative',sy.simplify(sy.diff(sy.log(1+x)-2*x/(2+x),x)-x*x/((1+x)*(2+x)**2))==0)
ck('log_lower_origin',(sy.log(1+x)-2*x/(2+x)).subs(x,0)==0)
rr,bb,ss=sy.symbols('rr bb ss');DD=8*(1+rr)-bb*(3+10*rr+3*rr**2)
ck('denominator_positive_decomposition',sy.expand(DD-(4*(1+rr)*(2-bb*(1+rr))+bb*(1-rr)**2))==0)
ck('denominator_upper_decomposition',sy.expand(16-DD-(8*(1-rr)+bb*(3+10*rr+3*rr**2)))==0)
xx=bb*(1-rr)**2/(2*(1+rr)*(2-bb*(1+rr)))
ck('log_rational_substitution',sy.cancel(4*xx/(2+xx)/bb-4*(1-rr)**2/DD)==0)
ck('quadratic_residual_identity',sy.expand(((1+rr*bb)*U(ss)-U(ss-bb))/bb-(rr*U(ss)-sy.Rational(c)+2*sy.Rational(d)*ss-sy.Rational(d)*bb))==0)
ck('potential_origin',U(0)==1)
upper=F(28453,40000);ck('potential_endpoint',U(sy.Rational(1,2))==sy.Rational(upper))
ck('potential_positive_decreasing',upper>0 and -c+d<0 and d>0)
gamma=minimum/16
ck('uniform_residual_constant',gamma==F(268141,31457280000))

def log1p_interval(x,n=24):
 x=F(x);assert x>=0;t=x/(2+x)
 lo=2*sum((t**(2*j+1)/F(2*j+1) for j in range(n)),F(0))
 return lo,lo+2*t**(2*n+1)/(F(2*n+1)*(1-t*t))
def w_interval(a,b):
 if a==b:return F(0),F(0)
 return log1p_interval((b-a)**2/(2*(a+b)*(2-a-b)))
def actual_residual_interval(a,b,s,cc=c,dd=d):
 u=lambda q:1-cc*q+dd*q*q
 lo,hi=w_interval(a,b);base=(1+a)*u(s)-u(s-b)
 return base+2*lam*lo,base+2*lam*hi
# The prior finite construction is replayed using an explicit prefix loop, not a copied decimal.
stages=[(F(349,2000),F(3,10))]+[(F(21,5000),F(1,100))]*20
prob=F(1);clo=F(0);chi=F(0);unweighted=F(0)
for aa,bb in stages:
 wl,wh=w_interval(aa,bb);prob/=1+aa;clo+=2*prob*wl;chi+=2*prob*wh;unweighted+=2*wl/(1+aa)
lo=prob-lam*chi;hi=prob-lam*clo
ck('finite_witness_admissible',all(0<=aa<=bb<=F(1,2) for aa,bb in stages))
ck('finite_witness_total_score',sum(bb for aa,bb in stages)==F(1,2))
ck('finite_witness_original_lower',lo>F(711020048691,10**12))
ck('finite_witness_original_upper',hi<F(711020048692,10**12))
ck('finite_witness_budget_interval',F(37866038451,10**12)<clo<=chi<F(37866038452,10**12))
ck('global_bracket_below_previous_precision_target',upper-lo<F(1,2500))
ck('global_bracket_below_305_micro',upper-lo<F(305,10**6))
# Outcome-contingent consumer of uniform residual: all-policy occupation and budget ceiling.
strong_upper=upper/(1+gamma/2)
ck('occupation_upper_strictly_sharper',lo<strong_upper<upper)
ck('budget_witness_gap_below_305_micro',(upper+lam*chi)/(1+gamma/2)-prob<F(305,10**6))
ck('witness_relative_abort_nonabsorption_bound',(upper-lo)/upper<F(43,100000))
ck('witness_relative_clipping_rejection_bound',2*(upper-lo)/upper<F(86,100000))
ck('witness_relative_clipping_cost_bound',(upper-lo)/lam<F(161,10**6))
# True altered-mathematics counterfixtures, including the reconnaissance error.
wrongc=F(1289,2000);wrongd=F(671,5000)
ck('bad_candidate_boundary_exact_value',F(2,5)+lam*F(9,70)-wrongc==-F(3,14000))
ct('sampled_LP_candidate_fails_actual_small_stage',actual_residual_interval(F(2,5*10**6),F(1,10**6),F(1,10**6),wrongc,wrongd)[1]<0)
ct('reduced_curvature_fails_actual_finite_stage',actual_residual_interval(F(1,7),F(1,4),F(1,2),c,F(13,100))[1]<0)
ct('missing_prefix_overcharges_real_witness',unweighted>chi)
ct('uncertified_exact_optimum_below_actual_witness',lo>F(711,1000))
ct('coarse_cube_has_negative_Bernstein_coefficient',min(B.values())<0)
ct('log_linear_upper_is_not_lower',log1p_interval(F(1,6))[1]<F(1,6))
# Four exact idle transitions; this same invariant holds for endless idling.
idle_p=F(0);idle_cost=F(0);idle_slack=F(0);idle_live=F(1);idle_s=F(1,2)
for _ in range(4):
 idle_delta=upper-((1-F(0))*upper+upper)/2+lam*F(0)
 idle_slack+=idle_live*idle_delta
 idle_live*=((1-F(0))+1)/2
idle_eta=upper-idle_p+lam*idle_cost;idle_tail=idle_live*upper
ck('actual_idle_telescope_with_tail',idle_eta==idle_slack+idle_tail and idle_p==idle_cost==idle_slack==0)
ct('terminal_potential_cannot_be_deleted',idle_eta!=idle_slack and idle_tail==upper>0)
# Executed successor: 41 finite rational stages, not a numerical fluid limit.
new_stages=[(F(8793,50000),F(151,500))]
new_b=F(99,20000)
for i in range(40):
 ratio=F(221,500)-F(23,500)*F(2*i+1,80)
 new_stages.append((new_b*ratio,new_b))
new_p=F(1);new_clo=F(0);new_chi=F(0)
# Outward rounding of each logarithm interval limits denominator growth.
log_den=10**24
for aa,bb in new_stages:
 wl,wh=w_interval(aa,bb)
 wl=F((wl.numerator*log_den)//wl.denominator,log_den)
 wh=F(-((-wh.numerator*log_den)//wh.denominator),log_den)
 new_p/=1+aa;new_clo+=2*new_p*wl;new_chi+=2*new_p*wh
new_lo=new_p-lam*new_chi;new_hi=new_p-lam*new_clo
ck('successor_41_original_stages',len(new_stages)==41)
ck('successor_controls_admissible',all(0<aa<bb<=F(1,2) for aa,bb in new_stages))
ck('successor_total_score_exact',sum(bb for aa,bb in new_stages)==F(1,2))
ck('successor_affine_tail_strictly_decreases',all(new_stages[i][0]>new_stages[i+1][0] for i in range(1,40)))
ck('successor_exact_dual_lower',new_lo>F(711079567311,10**12))
ck('successor_exact_dual_upper',new_hi<F(711079567312,10**12))
ck('successor_improves_old_dual_by_1_over_20000',new_lo-hi>F(1,20000))
ck('successor_conservative_global_gap',upper-new_lo<F(246,10**6))
ck('successor_refined_global_gap',strong_upper-new_lo<F(243,10**6))
ck('successor_same_exact_budget_gap',(upper+lam*new_chi)/(1+gamma/2)-new_p<F(243,10**6))
# Optional, noncertifying reconnaissance reproduces the two-atom discriminator.
# It is not part of the exact mathematical certificate or its pass count.
if args.scout:
 import math
 import numpy as np
 from scipy.optimize import minimize,brentq
 theta=10/19
 def tau(v):
  x=math.sqrt(1+2*v);return math.log(x-1)-3*math.log(3-x)
 clock=tau(theta)
 def fluid(t):
  v=brentq(lambda v:tau(v)-clock+t,theta*math.exp(-t-1),theta,xtol=1e-14) if t else theta
  return 1.9*v
 def ww(a,b):
  return 0. if b<1e-15 else 2*math.log1p((b-a)**2/(2*(a+b)*(2-a-b)))
 def one(v):
  b,r=v;a=b*r;return -(fluid(.5-b)-1.9*ww(a,b))/(1+a)
 first=minimize(one,[.3,.58],bounds=[(0,.5),(0,1)],method='Nelder-Mead',options={'xatol':1e-12,'fatol':1e-14,'maxiter':1000})
 def two(v):
  x,y,r1,r2=v;b1=.5*x;b2=(.5-b1)*y;a1=b1*r1;a2=b2*r2
  q=(fluid(.5-b1-b2)-1.9*ww(a2,b2))/(1+a2)
  return -(q-1.9*ww(a1,b1))/(1+a1)
 seeds=[[.55,.1,.6,.45],[.3,.5,.6,.5],[.05,.65,.6,.58],[.65,.8,.57,.42],[.1,.1,.4,.4],[.9,.9,.6,.5]]
 rows=[]
 for seed in seeds:
  q=minimize(two,seed,bounds=[(0,1)]*4,method='Nelder-Mead',options={'xatol':1e-10,'fatol':1e-14,'maxiter':1800})
  rows.append({'seed':seed,'controls':q.x.tolist(),'value':float(-q.fun),'optimizer_reported_success':bool(q.success)})
 print(json.dumps({'kind':'nonexhaustive floating-point scout, never global certification','one_controls_b_ratio':first.x.tolist(),'one_value':float(-first.fun),'two_atom_runs':rows},indent=2))
paths=['explorations/conditional-build/k2565-bellman-supersolution-2026-11-05.md','tests/channel-swings/k2565_bellman_supersolution_probe.py','explorations/conditional-build/k2561-higher-budget-stopping-2026-11-05.md','explorations/conditional-build/k2563-global-hybrid-reduction-2026-11-05.md','explorations/conditional-build/k2557-parametric-stopping-support-2026-11-05.md','explorations/conditional-build/k2483-adaptive-stopping-bellman-2026-11-01.md']
if not args.draft:
 assert all((ROOT/p).is_file() for p in paths),'required native dependency missing'
report={'result':'K2565','checks':checks,'contrary_controls':controls,'certificate':{'multidegree':list(ns),'leaf_count':len(leaves),'max_depth':depth,'minimum_coefficient':str(minimum),'leaf_digest':certificate_digest,'rule':'strict-positive leaves; cyclic axes depth modulo 3; exact midpoint de Casteljau; maximum allowed depth 24'},'bounds':{'score_domain':'0<S<=1/2','multiplier':'19/10','potential_c':str(c),'potential_d':str(d),'residual_gamma':str(gamma),'score_half_upper':str(upper),'occupation_refined_upper':str(strong_upper),'witness_probability':str(prob),'witness_cost_interval':[str(clo),str(chi)],'witness_dual_interval':[str(lo),str(hi)],'constrained_upper':'min(1,(U(S)+(19/10)*B)/(1+gamma*S))','executed_successor':{'stages':41,'main_action':['8793/50000','151/500'],'tail_score':'99/20000','tail_ratio':'221/500-(23/500)*(2*i+1)/80, i=0,...,39','probability':str(new_p),'cost_interval':[str(new_clo),str(new_chi)],'dual_interval':[str(new_lo),str(new_hi)],'strict_gain_over_old':'1/20000','refined_global_gap_less_than':'243/1000000'}},'evidence_kinds':{'exact':'whole-cube rational Bernstein subdivision; inverse basis and affine-subdivision checks; actual-log interval controls and finite prefix replay','universal':'log inequality, original-trial supersolution and occupation/tail telescope proved in note','reused':'K2561 initial finite witness, K2483 adaptive Bellman equivalence and K2557 clipping/tail accounting','new_finite_construction':'41 rational stages with exact original prefix/log brackets; optional --scout is expressly noncertifying','not_claimed':'exact intermediate optimum, uniqueness, original finite attainment, complete multiplier frontier, native GU or external certification'},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths if (ROOT/p).exists()}}
if args.draft:
 print(json.dumps({'checks':len(checks),'controls':len(controls),'certificate':report['certificate'],'draft_dependencies_missing':[p for p in paths if not (ROOT/p).exists()]},indent=2))
else:
 out=ROOT/'lab/process/k2565-bellman-supersolution.json'
 if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(out.read_text())==report,'saved report consistency'
 print('K2565 PASS',len(checks),'exact/supporting groups',len(controls),'contrary controls')
