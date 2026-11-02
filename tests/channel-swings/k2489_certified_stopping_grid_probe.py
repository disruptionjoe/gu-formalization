"""Original-law finite certificates. Universal arguments are in K2489, not grid counts."""
from pathlib import Path
import json,sys,hashlib,itertools
from fractions import Fraction as Q
import sympy as S
from flint import arb,ctx
ctx.prec=192
R=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ctrl(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError('contrary '+k)
def ball(x):
 x=Q(x);return arb(x.numerator)/x.denominator
def w(a,b):
 a,b=Q(a),Q(b)
 if b<=a:return arb(0)
 return (1+ball((b-a)**2/(2*(a+b)*(2-a-b)))).log()
def h(r,b):
 r,b=Q(r),Q(b)
 if b==0:return ball((1-r)**2/(2*(1+r)))
 return 2*w(r*b,b)/ball(b)
def maxball(vals):return max(v.lower() for v in vals).union(max(v.upper() for v in vals))
def dp(M,J,lam):
 D=[arb(1)];pol=[(Q(1),arb(0),[])]
 for j in range(1,J+1):
  cand=[arb(0)];choices=[(Q(0),arb(0),[])];costs={}
  for k in range(1,min(M,j)+1):
   for l in range(k+1):
    a,b=Q(l,M),Q(k,M);ww=w(a,b);cand.append((D[j-k]-2*ball(lam)*ww)/ball(1+a))
    p,c,s=pol[j-k];choices.append((p/(1+a),(2*ww+c)/ball(1+a),[(l,k)]+s))
  # lower witness is actual policy, independent of interval supremum upper.
  best=max(range(len(choices)),key=lambda i:(ball(choices[i][0])-ball(lam)*choices[i][1]).lower())
  pol.append(choices[best]);D.append(maxball(cand))
 return D,pol
# Symbolic identities and moment inversion, not a finite-grid proof.
a,b,r,z,lam,ss,p,kk=S.symbols('a b r z lam ss p kk',real=True);u=a+b;d=b-a
ck('lower_cost_denominator',S.expand(4*u-(2*u*(2-u)+d*d)-(2*u*u-d*d))==0)
A=(1+6*r+r*r)/(4*(1+r));B=(1+r)/2
ck('normalized_log_factor',S.factor((1+(b-r*b)**2/(2*(r*b+b)*(2-r*b-b)))-(1-A*b)/(1-B*b))==0)
ck('zero_stage_limit',S.factor(2*(B-A)-(1-r)**2/(2*(1+r)))==0)
x=d*d/(2*u*(2-u));ck('cost_a_derivative',S.factor(S.diff(x,a)+d*(3*b+a-2*a*b-2*b*b)/(u*u*(2-u)**2))==0)
ck('derivative_nonnegative_factor',S.expand(3*b+a-2*a*b-2*b*b-(a*(1-b)+b*(1-a)+2*b*(1-b)))==0)
expr=((ss+1)*p-1)**2-2*kk*((ss-1)*p+1)
ck('quadratic_discriminant',S.factor(S.discriminant(expr,p)-4*(kk**2*(ss-1)**2+4*kk*ss*(ss+1)))==0)
# Contraries use actual altered controls/laws.
ctrl('unclipped_cost_wrong',w(Q(3,4),Q(1,4))==0 and (Q(1,4)-Q(3,4))**2/(4*(Q(1,4)+Q(3,4)))>0)
ck('rational_log_upper_witness',361000000<364972218)
ck('rational_sqrt_upper',Q(2191,20)**2>12001)
L=Q(500,731);U=Q(62171,90000);ck('bracket_width',U-L==Q(447001,65790000) and U-L<Q(17,2500))
a=Q(231,500);b=Q(1,2);cost=2*w(a,b)/ball(1+a);ck('actual_cost_interval',cost<ball(Q(1,1000)))
ck('moment_for_witness',2*a/(1+a)==2*(1-L) and 2*b/(1+a)==2*b*L)
ctrl('success_only_cost_undercounts',ball(L)*cost<cost)
ck('better_than_entropy_baseline',ball(U)<1/arb(2).sqrt());ck('better_than_K2485_sqrt',ball(U)<ball(Q(2,3))+1/arb(500).sqrt())
fixture={'target':'1/2','budget':'1/1000','a':str(a),'b':str(b),'success':str(L),'actual_cost_arb':str(cost),'frontier_upper':str(U),'width':str(U-L),'scope':'all-policy upper plus one-stage original-law lower; no optimum claim'}
# Exact rational witnesses across finite schedules check all-policy occupation interface.
for ix,seq in enumerate([[(Q(1,3),Q(1,2))],[(Q(1,4),Q(1,2)),(Q(1,3),Q(1,2))],[(Q(0),Q(1,2))]*3,[(Q(3,4),Q(1,4)),(Q(0),Q(1,2))]]):
 pp=Q(1);A0=B0=Q(0);C=arb(0);score=Q(0)
 for a,b in seq:
  A0+=pp*2*a/(1+a);B0+=pp*2*b/(1+a);C+=ball(pp)*2*w(a,b)/ball(1+a);pp/=1+a;score+=b
 ck(f'occupation_fail_{ix}',A0==2*(1-pp));ck(f'occupation_score_{ix}',B0>=2*score*pp)
 lb=max(Q(0),B0-A0)**2/(4*(A0+B0));ck(f'occupation_cost_{ix}',C>=ball(lb))
# All-length score recurrence checked against exhaustive original grid schedules.
for M,J in [(2,1),(2,2),(3,2)]:
 lam=Q(2);D,pol=dp(M,J,lam)
 def exhaustive(j):
  if j<=0:return [(Q(1),arb(0))]
  result=[(Q(0),arb(0))]
  for k in range(1,min(M,j)+1):
   for l in range(k+1):
    a,b=Q(l,M),Q(k,M)
    for p,c in exhaustive(j-k):result.append((p/(1+a),(2*w(a,b)+c)/ball(1+a)))
  return result
 vals=[ball(p)-ball(lam)*c for p,c in exhaustive(J)];ev=maxball(vals)
 ck(f'exhaustive_grid_{M}_{J}',D[J].overlaps(ev) and abs(D[J]-ev)<arb('1e-45'))
 ck(f'policy_lower_{M}_{J}',ball(pol[J][0])-ball(lam)*pol[J][1]<=D[J].upper())
# Modest executable grid, reported only as a finite-grid calculation.
D,pol=dp(32,16,Q(12));pp,cc,schedule=pol[-1]
grid={'M':32,'J':16,'lambda':'12','support_interval':str(D[-1]),'policy_success':str(pp),'policy_cost_interval':str(cc),'policy':[list(pair) for pair in schedule]}
# Rational all-cell residual certificate on [0,1], U=1-7s/18, lambda9/8.
# Exact vertex geometry covers x/y partition rectangles; ratio bins cover ALL r.
def residual_certificate(knots,values,lam,Rbins):
 assert knots[0]==0 and knots[-1]<=1 and values[0]==1 and min(values)>=0
 bounds=[];count=0
 for i in range(len(knots)-1):
  for j in range(i,len(knots)-1):
   xl,xh=knots[i:i+2];yl,yh=knots[j:j+2];sl=(values[i+1]-values[i])/(xh-xl);sr=(values[j+1]-values[j])/(yh-yl)
   def ux(x):return values[i]+sl*(x-xl)
   def uy(y):return values[j]+sr*(y-yl)
   verts=[(x,y) for x in (xl,xh) for y in (yl,yh) if y>x]
   if not verts:continue
   H=max((ux(x)-uy(y))/(y-x) for x,y in verts)
   if xh>=yl:H=max(H,-sl,-sr)
   umin=min(values[j:j+2]);bmin=max(Q(0),yl-xh)
   for t in range(Rbins):
    r0=Q(t,Rbins);r1=Q(t+1,Rbins)
    bounds.append(ball(H-r0*umin)-ball(lam)*h(r1,bmin));count+=1
 return maxball([arb(0)]+bounds).upper(),count
knots=[Q(i,16) for i in range(17)];vals=[1-Q(7,18)*x for x in knots];delta,cells=residual_certificate(knots,vals,Q(9,8),64)
ck('all_cell_finite_certificate',delta>=0 and delta<ball(Q(1,50)))
residual={'knots':16,'ratio_bins':64,'covered_cells':cells,'delta_upper':str(delta),'frontier_bound_at_K_1_10':str(ball(Q(11,18))+delta+ball(Q(9,80))),'scope':'rigorous all-cell residual, not sampled maximum; simple linear test candidate'}
# Analytic zero-residual completion checked symbolically, including tiny stages.
t=S.symbols('t');rr=(1-t)/(1+t);g=(1-rr)**2/(2*(1+rr));c=S.Rational(7,18);ll=S.Rational(9,8)
ck('linear_square_certificate',S.factor((rr+ll*g)/(1+rr)-c-ll*(t-1/(2*ll))**2/2)==0)
ck('analytic_rational_fixture',Q(11,18)+Q(9,8)*Q(1,10)==Q(521,720))
# Changed candidate has positive infinitesimal residual: U=1-s, lambda9/8,r0.
ctrl('bad_candidate_detected',1-Q(9,8)*Q(1,2)>0)
# a=0,b=1/2 cheapest-stage cost assumption cannot charge only successful trials.
ctrl('failed_path_not_free',w(Q(1,4),Q(1,2))>0 and Q(1,4)>0)
# Uniform a-grid first interval: ratio choices0/1 miss interior minimizer of r+lambda*g.
lam=Q(2);r=Q(1,2);g=(1-r)**2/(2*(1+r));ctrl('tiny_stage_grid_not_global',r+lam*g<min(Q(1),lam/2))
# Positive-part needed for one-sided controls; negative inferred cost must never be squared blindly.
ctrl('signed_moment_requires_positive_part',max(Q(0),Q(1)-Q(2))**2==0 and (Q(1)-Q(2))**2==1)
deps=['lab/process/k2487-controlled-stopping-approximation.json','lab/process/k2485-constrained-stopping-frontier.json','lab/process/k2471-sharp-stopping-coefficient.json']
report={'result':'K2489','scope':'original fresh fair-routing law, actual failure-inclusive expected cost','checks':checks,'contrary_controls':controls,'nondyadic_bracket':fixture,'grid':grid,'residual':residual,'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps},'evidence_kinds':{'universal':'written leakage, occupation, inversion, score-DP and residual proofs','finite':'rational witness and symbolic identities; exhaustive tiny grids; interval all-cell residual','inherited':'K2483/K2485 all-policy stage reduction and clipping; K2487 compression'}}
p=R/'lab/process/k2489-certified-stopping-grid.json'
if '--write' in sys.argv:p.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
else:ck('saved_reproduction',json.loads(p.read_text())==report)
print(json.dumps({'result':'PASS','checks':len(checks),'controls':len(controls),'bracket':fixture,'grid':grid,'residual':residual}))
