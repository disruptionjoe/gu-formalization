#!/usr/bin/env python3
"""K2602 continuum resource coefficient: exact algebra and rigorous interval integrals.

Intervals cover each quadrature cell, not sampled point estimates. Written
occupation/mesh proofs supply the universal result; finite policies are consumers.
"""
import argparse,json,hashlib
from pathlib import Path
from fractions import Fraction as Q
import sympy as s
from flint import arb,fmpq,ctx
ctx.prec=192
root=Path(__file__).resolve().parents[2]
ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
checks=[];controls=[]
def ck(n,v):
 assert bool(v),'FAIL '+n
 checks.append(n)
def ct(n,v):
 assert bool(v),'FAIL contrary '+n
 controls.append(n)
b,r=s.symbols('b r');v=s.symbols('v',positive=True)
g=(1-r)**2/(2*(1+r));B=(1-r)**2/4-(1-r)**4/(16*(1+r)**2)
w=s.log(1+(b-r*b)**2/(2*(r*b+b)*(2-r*b-b)))
ck('actual_original_cost_uniform_coefficients',s.simplify(s.series(2*w,b,0,3).removeO()-b*g-b*b*B)==0)
ck('strong_action_convexity',s.cancel(s.diff(g,r,2)-4/(1+r)**3)==0)
ck('strong_convexity_min_on_unit_interval',4/(1+s.Integer(1))**3==s.Rational(1,2))
v_r=2/(1+r)**2-s.Rational(1,2);q_r=s.factor(r*v_r+g)
ck('interior_minimizer_stationarity',s.cancel(v_r+s.diff(g,r))==0)
ck('interior_generator',s.cancel(q_r-(1-r)*(3*r+1)/(2*(1+r)**2))==0)
DD=s.factor(B-q_r*r/2)
ck('actual_second_order_residual',s.cancel(DD-(1-r)*(3*r+1)*(3-6*r-r*r)/(16*(1+r)**2))==0)
ck('D_generator_factor',s.cancel(DD-q_r*(3-6*r-r*r)/8)==0)
ck('branch_join_D',DD.subs(r,0)==s.Rational(3,16))
rm=2/s.sqrt(3)-1
ck('interior_action_range',0<rm<s.Rational(1,6))
ck('D_positive_remaining_factor_at_upper',s.simplify(3-6*rm-rm*rm)>0)
ck('D_positive_factor_monotone',s.diff(3-6*r-r*r,r).subs(r,0)<0)
ct('ignoring_flow_curvature_changes_D',s.cancel(B-DD)!=0)
ct('wrong_survival_occupation_not_equivalent',s.cancel(q_r-s.Rational(1,2))!=0)
ct('action_zero_outside_branch_not_stationary',s.cancel((v+s.diff(g,r)).subs({v:1,r:0}))!=0)
# Completing the square is the uniform r-to-r* transfer, including KKT boundaries.
z,L=s.symbols('z L',real=True)
ck('uniform_remainder_absorption',s.expand(b*z*z/4-b*b*L*z+b**3*L*L-b*(z/2-b*L)**2)==0)
# Variable-mesh cost/resource cancellation with the same survival density.
P,D,t=s.symbols('P D t',positive=True)
ck('mesh_resource_integrand',s.simplify(2*P/(t/s.sqrt(D))-2*P*s.sqrt(D)/t)==0)
ck('mesh_loss_integrand',s.simplify(P*D*(t/s.sqrt(D))-t*P*s.sqrt(D))==0)
ck('critical_coefficient_recovered',s.simplify(2*v*(S:=s.symbols('S',positive=True))**2*s.Rational(3,16)-3*v*S*S/8)==0)
MM,RR,WW,ZZ,II=s.symbols('MM RR WW ZZ II',positive=True)
ck('optimal_mesh_square_expansion',s.expand((MM**2*WW-4*MM*II*ZZ+4*II**2*RR)/MM-(MM*WW-4*II*ZZ+4*II**2*RR/MM))==0)
ck('optimal_mesh_limit_cancellation',s.expand(4*II**2-4*II*(2*II)+4*II**2)==0)
def aa(x):
 x=Q(x);return arb(fmpq(x.numerator,x.denominator))
def ball(lo,hi):return aa((lo+hi)/2)+arb(0,aa((hi-lo)/2))
def qfun(v):
 return 2*(1+2*v).sqrt()-2-v

def tau(x):
 if x>=Q(3,2):return 2*aa(x)-3
 vv=aa(x);z=(1+2*vv).sqrt();return (z-1).log()-3*(3-z).log()
def initial_bracket(score,lm):
 theta=1/lm;target=tau(theta)-aa(score);lo=theta-score/2;hi=theta
 for _ in range(100):
  mid=(lo+hi)/2;diff=tau(mid)-target
  if diff>0:hi=mid
  elif diff<0:lo=mid
  else:raise AssertionError('root sign unresolved')
 ck('clock_root_bracket_'+str(score)+'_'+str(lm),tau(lo)<target and tau(hi)>target)
 return lo,hi

def interior(v):
 q=qfun(v);r=2/(1+2*v).sqrt()-1;D=q*(3-6*r-r*r)/8
 return q,D

def integrand(v):
 q,D=interior(v);return D.sqrt()/(q*q)

def coeff(score,lm,cells=16384):
 theta=1/lm;lo,hi=initial_bracket(score,lm);vv=ball(lo,hi)
 if lo>=Q(3,2):qu=aa(Q(1,2))
 else:qu=qfun(vv)
 end=min(theta,Q(3,2));J=arb(0);J0=arb(0);JD=arb(0)
 if lo<end:
  width=(end-lo)/cells
  for i in range(cells):
   cell=ball(lo+i*width,lo+(i+1)*width);qc,dc=interior(cell)
   J+=dc.sqrt()/(qc*qc)*aa(width)
   J0+=aa(width)/(qc*qc);JD+=dc/(qc*qc)*aa(width)
  # Remove the uncertain lower-root segment. Interval is [0, upper].
  err=integrand(ball(lo,hi)).abs_upper()*aa(hi-lo)
  J-=arb(0,err)/2+err/2
  ql,dl=interior(ball(lo,hi))
  err0=(1/(ql*ql)).abs_upper()*aa(hi-lo);errd=(dl/(ql*ql)).abs_upper()*aa(hi-lo)
  J0-=arb(0,err0)/2+err0/2;JD-=arb(0,errd)/2+errd/2
 if theta>Q(3,2):
  interval=aa(theta-max(lo,Q(3,2)));J+=interval*arb(3).sqrt();J0+=4*interval;JD+=aa(Q(3,4))*interval
 I=qu*J;C=2*aa(lm)*I*I;Ceq=2*aa(lm)*qu*qu*J0*JD
 if lm==Q(4,5):ct('actual_equal_mesh_coefficient_strictly_worse',Ceq>C)
 ck('integral_positive_'+str(score)+'_'+str(lm),I>0 and C>0)
 ck('integral_width_'+str(score)+'_'+str(lm),C.rad()<aa(Q(1,100000)))
 return {'score':str(score),'multiplier':str(lm),'u_lo':str(lo),'u_hi':str(hi),'I_interval':I.str(35,more=True),'coefficient_interval':C.str(35,more=True),'equal_mesh_coefficient_interval':Ceq.str(35,more=True),'cells':cells},C
consumers=[];coeffs=[]
for score,lm in [(Q(1,2),Q(3,5)),(Q(1,2),Q(4,5)),(Q(1,4),Q(7,10))]:
 row,C=coeff(score,lm);consumers.append(row);coeffs.append(C)
ct('coefficient_varies_across_actual_multipliers',coeffs[0]>coeffs[1])
# A fully rational mesh policy consumer uses interval roots only to suggest
# bounded rational actions. The actual policy and original law are exact.
def policy(score,lm,step):
 lo,hi=initial_bracket(score,lm);u=ball(lo,hi)
 remain=score;surv=Q(1);C=arb(0);resource=Q(0);schedule=[]
 while remain>0:
  vl,vh=initial_bracket_no_check(remain,lm)
  if vl>=Q(3,2):rv=arb(0);dv=aa(Q(3,16))
  else:
   vv=ball(vl,vh);qv,dv=interior(vv);rv=2/(1+2*vv).sqrt()-1
  proposed=Q(int((aa(step)/dv.sqrt()*10**12).floor().unique_fmpz()),10**12)
  bb=min(remain,proposed);assert bb>0
  numerator=int((rv*10**12).floor().unique_fmpz());action=bb*Q(max(0,numerator),10**12)
  assert 0<=action<=bb
  surv/=1+action;arg=1+(bb-action)**2/(2*(action+bb)*(2-action-bb))
  C+=2*aa(surv)*aa(arg).log();resource+=2*surv
  schedule.append([str(action),str(bb)]);remain-=bb
 J=aa(surv)-aa(lm)*C;V=aa(lm)*u;gap=V-J
 tag=str(lm)+'_'+str(step)
 ck('finite_variable_mesh_positive_gap_'+tag,gap>0)
 ck('finite_variable_mesh_exact_score_'+tag,sum((Q(z[1]) for z in schedule),Q(0))==score)
 ct('nominal_stage_resource_wrong_'+tag,resource!=2*len(schedule))
 return {'score':str(score),'multiplier':str(lm),'step_parameter':str(step),'schedule':schedule,'count':len(schedule),'success':str(surv),'resource':str(resource),'gap_interval':gap.str(35,more=True),'resource_gap_interval':(aa(resource)*gap).str(35,more=True),'role':'actual rational approximation to variable-mesh construction; exact original-law resource and gap, not finite optimality'}
def initial_bracket_no_check(score,lm):
 theta=1/lm;target=tau(theta)-aa(score);lo=theta-score/2;hi=theta
 if lo>=Q(3,2):return lo,lo
 for _ in range(65):
  mid=(lo+hi)/2
  diff=tau(mid)-target
  if diff>0:hi=mid
  elif diff<0:lo=mid
  else:raise AssertionError('policy root sign unresolved')
 assert tau(lo)<target and tau(hi)>target,'policy root not bracketed'
 return lo,hi
# Complete rational variable-mesh policies, no search or optimizer.
policies=[policy(Q(1,2),lm,step) for lm in [Q(3,5),Q(4,5)] for step in [Q(1,50),Q(1,100)]]
report={'result':'K2602','checks':checks,'contrary_controls':controls,'theorem':'For every fixed0<S<=1/2 and0<lambda<=4/5, gap=2lambda I^2/M+O(M^-3/2), I=integral P sqrtD ds; above-critical extension is new, subcritical matches exact tail','necessary_optimal_mesh':'Any eta=C/M+o(1/M) policy exhausts R/M->1 and has (1/M)E sum(M b sqrtD-2I)^2->0; averaged rigidity, not pathwise uniqueness','occupation':'mu_eta=(1/2)E sum b delta_s converges against Lipschitz tests to P(s)ds with O(sqrteta); action deviation weighted square is O(eta)','finite_coefficients':consumers,'finite_policy_comparisons':policies,'interval_method':'python-flint Arb192 bits; exact rational root bisection and integrand enclosure over every quadrature cell, split at3/2; root endpoint uncertainty explicitly subtracted','toolchain':'python-flint0.9.0','evidence_kind':'exact original-law coefficient identities, certified complete-interval coefficient consumers, actual rational policies; uniform adaptive occupation and resource asymptotic proofs in note','ceiling':'fixed S and lambda; supplied stochastic model, compact positive-parameter uniformity only; no exact finite optimizer, S-to-zero/lambda-to-zero or next-order transition claim, physical apparatus or GU claim'}
refs=['explorations/conditional-build/k2561-higher-budget-stopping-2026-11-05.md','explorations/conditional-build/k2601-critical-stopping-resource-limit-2026-11-06.md']
report['provenance']={f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in refs}
out=root/'lab/process/k2602-continuum-stopping-resource-law.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved report mismatch'
print(json.dumps({'result':'K2602','checks':len(checks),'controls':len(controls),'status':'pass','coefficient_intervals':[r['coefficient_interval'] for r in consumers]}))
