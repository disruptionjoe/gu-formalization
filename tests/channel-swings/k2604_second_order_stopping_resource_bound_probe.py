#!/usr/bin/env python3
"""K2604 exact barrier constants and actual finite-policy consumers.

Arithmetic certificates support, but do not replace, the all-policy proof.
"""
import argparse,json,hashlib,math
from pathlib import Path
from fractions import Fraction as Q
import sympy as s
from flint import arb,fmpq,ctx
ctx.prec=192
root=Path(__file__).resolve().parents[2]
ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
checks=[];controls=[];certificates={}
def ck(n,v):
 assert bool(v),'FAIL '+n
 checks.append(n)
def ct(n,v):
 assert bool(v),'FAIL contrary '+n
 controls.append(n)
r,b=s.symbols('r b');alpha=(1+6*r+r*r)/(4*(1+r));beta=(1+r)/2
arg=1+(b-r*b)**2/(2*(r*b+b)*(2-r*b-b))
ck('actual_log_argument_factorization',s.cancel(arg-(1-alpha*b)/(1-beta*b))==0)
g=(1-r)**2/(2*(1+r));B=(1-r)**2/4-(1-r)**4/(16*(1+r)**2)
ck('actual_first_coefficient',s.cancel(2*(beta-alpha)-g)==0)
ck('actual_second_coefficient',s.cancel(beta**2-alpha**2-B)==0)
ck('strong_convexity',s.cancel(s.diff(g,r,2)-4/(1+r)**3)==0)
q=(1-r)*(3*r+1)/(2*(1+r)**2);D=s.factor(B-q*r/2)
def bernstein(expr,lo,hi,name):
 """Exact whole-interval rational sign certificate; both denominator and numerator."""
 x=s.symbols('x');num,den=s.fraction(s.cancel(expr.subs(r,lo+(hi-lo)*x)))
 def coeff(poly):
  pp=s.Poly(poly,x);n=pp.degree()
  if pp.is_zero:return [s.Integer(0)]
  return [sum(pp.nth(k)*s.binomial(i,k)/s.binomial(n,k) for k in range(i+1)) for i in range(n+1)]
 nc,dc=coeff(num),coeff(den)
 if all(v<0 for v in dc):nc=[-v for v in nc];dc=[-v for v in dc]
 ck(name,all(v>=0 for v in nc) and all(v>0 for v in dc))
 certificates[name]={'numerator':list(map(str,nc)),'denominator':list(map(str,dc)),'interval':[str(lo),str(hi)]}
for name,expr in [('alpha_nonnegative',alpha),('beta_above_alpha',beta-alpha),('beta_at_most_one',1-beta),('B_Lipschitz_upper',4-s.diff(B,r)),('B_Lipschitz_lower',4+s.diff(B,r))]:bernstein(expr,s.Integer(0),s.Integer(1),name)
for name,expr in [('D_positive_lower',D-s.Rational(1,10)),('D_upper',s.Rational(3,16)-D),('D_decreasing',-s.diff(D,r)),('D_derivative_bound',s.Rational(2,3)+s.diff(D,r)),('q_lower',q-s.Rational(9,20)),('q_upper',s.Rational(1,2)-q)]:bernstein(expr,s.Integer(0),s.Rational(1,6),name)
ck('log_third_derivative_bound',4*1/(1-s.Rational(1,2))**3==32)
ck('Taylor_constant_six',s.Rational(32,6)+s.Rational(1,24)<6)
ck('D_join',D.subs(r,0)==s.Rational(3,16))
ck('D_endpoint',D.subs(r,s.Rational(1,6))==s.Rational(355,3136))
ck('r_prime_bound',1/(3*s.sqrt(3))<s.Rational(1,4))
ck('v_second_derivative_Lipschitz',s.Rational(1,2)*(s.Rational(1,36)+s.Rational(1,4))<s.Rational(1,4))
ck('h_Lipschitz',s.Rational(1,6)/(2*s.Rational(3,10))<s.Rational(1,3))
e,c,L,z,lm=s.symbols('e c L z lm',positive=True)
ck('priced_square',s.simplify(L*(b-e*s.sqrt(2/L))**2-(L*b*b-2*s.sqrt(2*L)*e*b+2*e*e))==0)
ct('zero_action_not_optimal_interior_flow',s.diff(g,r).subs(r,0)+1<0)
ct('one_trial_price_wrong_at_minimum',s.simplify((L*b*b-2*s.sqrt(2*L)*e*b+e*e).subs(b,e*s.sqrt(2/L)))==-e*e)
# Young/square inequalities as exact nonnegative squares, not sampled actions.
A=s.symbols('A',nonnegative=True)
ck('action_error_completion',s.expand(lm*b*z*z/4-b*A*z+b*A*A/lm-lm*b*(z/2-A/lm)**2)==0)
ck('sum_square_bound',s.expand(2*(4*lm*b)**2+2*e**2-(4*lm*b+e)**2-(4*lm*b-e)**2)==0)
ck('cubic_absorption',s.expand(2*b*(b-e*c)**2+2*b*e*e*c*c-b**3-b*(b-2*e*c)**2)==0)
ck('mixed_absorption',s.expand(b*(b-e*c)**2/2+(s.Rational(1,2)+c)*e*e*b-e*b*b-b*((b-e*c)-e)**2/2)==0)
ck('B_constant_31',38*s.Rational(4,5)<31)
ck('small_step_half_absorption',s.simplify((62+s.Rational(1,2))*lm/1250-lm/20)==0)
ck('cmax_bound_on_lambda_range',20*s.Rational(4,5)<=16)
ck('K_dominates_remainder',1251>1240+4+2)
# Exact final-stage and survival-weighted Riemann constants.
E0=s.Rational(25,108);hmin=s.Rational(3,10);hmax=s.Rational(1,2);S=s.Rational(1,2);rr=s.Rational(1,6);lh=s.Rational(1,3)
KR=2*(E0*(S*hmax+1)+S*(lh+rr*hmax)/(2*hmin)+1)
KE=E0*hmax*S+S*(lh+rr*hmax)/(2*hmin)+s.Rational(1,4)+6*S/hmin**2
ck('prefix_constant',((rr**2+s.Rational(1,4))*S/(2*hmin))==E0)
ck('resource_slack_constant',KR==s.Rational(707,216) and KR<4)
ck('loss_constant',KE==s.Rational(14683,432) and KE<35)
x,t=s.symbols('x t',real=True)
ck('last_clip_quadratic',s.expand(t*t/4-x*(t-x)-(x-t/2)**2)==0)
C,M,K,SS=s.symbols('C M K SS',positive=True)
ck('dual_resource_substitution',s.simplify((-2*s.sqrt(C)*e+(M+K*SS)*e*e).subs(e,s.sqrt(C)/M)+C/M-K*SS*C/M**2)==0)
ck('priced_mesh_loss_70',s.simplify(35*lm*(e*s.sqrt(2/lm))**2-70*e**2)==0)
ck('priced_error_74',70+4==74)
ct('uncorrected_certificate_lower_bound_negative',(-31*b**3-e*b*b-2*e*e*b/lm).subs(b,e*c).is_negative)
# A bound alone cannot select a second coefficient: oscillating errors obey it.
ct('bounded_remainder_not_second_coefficient',s.sin(s.pi/2)!=s.sin(3*s.pi/2))

u=s.symbols('u',positive=True)
ck('forward_sqrt_secant_error',s.simplify((s.sqrt(1+u)-1)/u-s.Rational(1,2)+u/(2*(1+s.sqrt(1+u))**2))==0)
ck('backward_sqrt_secant_error',s.simplify((1-s.sqrt(1-u))/u-s.Rational(1,2)-u/(2*(1+s.sqrt(1-u))**2))==0)
ck('price_secant_error_balance',-s.Rational(1,2)+s.Rational(1,4)==-s.Rational(1,4))
# Abstract convex affine model, not original-law policies: a maximum has a kink at a tie.
k=s.symbols('k',real=True);left=1-k;right=2-3*k
ct('abstract_convex_affine_tie_need_not_be_differentiable',left.subs(k,s.Rational(1,2))==right.subs(k,s.Rational(1,2)) and s.diff(left,k)!=s.diff(right,k))

def aa(x):
 x=Q(x);return arb(fmpq(x.numerator,x.denominator))
def ball(lo,hi):return aa((lo+hi)/2)+arb(0,aa((hi-lo)/2))
def tau(x):
 if x>=Q(3,2):return 2*aa(x)-3
 zz=(1+2*aa(x)).sqrt();return (zz-1).log()-3*(3-zz).log()
def flow(score,lm):
 theta=1/lm;lo=theta-score/2;hi=theta
 if lo>=Q(3,2):return lo,lo
 target=tau(theta)-aa(score)
 for _ in range(90):
  mid=(lo+hi)/2;dif=tau(mid)-target
  if dif>0:hi=mid
  elif dif<0:lo=mid
  else:raise AssertionError('FAIL unresolved clock sign')
 assert tau(lo)<target and tau(hi)>target,'FAIL clock bracket'
 return lo,hi
prior=json.loads((root/'lab/process/k2602-continuum-stopping-resource-law.json').read_text())
policies=[]
for lm in [Q(3,5),Q(4,5)]:
 rows=[v for v in prior['finite_coefficients'] if v['score']=='1/2' and v['multiplier']==str(lm)]
 ck('unique_coefficient_'+str(lm),len(rows)==1);row=rows[0];Ib=arb(row['I_interval']);Cb=arb(row['coefficient_interval'])
 for budget in [8,16,64]:
  # Concrete rational mesh approximation. Its resource and bound are checked directly.
  tball=2*Ib/(budget-4);step=Q(int((tball.lower()*10**12).floor().unique_fmpz()),10**12)
  remain=Q(1,2);surv=Q(1);resource=Q(0);cost=arb(0);schedule=[]
  while remain>0:
   lo,hi=flow(remain,lm);vv=ball(lo,hi)
   if lo>=Q(3,2):rv=arb(0);dv=aa(Q(3,16))
   else:
    rv=2/(1+2*vv).sqrt()-1;qv=2*(1+2*vv).sqrt()-2-vv;dv=qv*(3-6*rv-rv*rv)/8
   bb=min(remain,Q(int((aa(step)/dv.sqrt()*10**12).floor().unique_fmpz()),10**12))
   action=bb*Q(max(0,int((rv*10**12).floor().unique_fmpz())),10**12)
   assert bb>0 and 0<=action<=bb,'FAIL finite action'
   surv/=1+action;resource+=2*surv
   cost+=2*aa(surv)*aa(1+(bb-action)**2/(2*(bb+action)*(2-bb-action))).log()
   schedule.append([str(action),str(bb)]);remain-=bb
  lo,hi=flow(Q(1,2),lm);gap=aa(lm)*ball(lo,hi)-aa(surv)+aa(lm)*cost
  upper=Cb/(budget-4)+70*Cb/(budget-4)**2
  tag=str(lm)+'_'+str(budget)
  ck('actual_budget_feasible_'+tag,resource<=budget)
  ck('exact_score_'+tag,sum((Q(v[1]) for v in schedule),Q(0))==Q(1,2))
  ck('actual_gap_positive_'+tag,gap>0)
  ck('actual_gap_under_safe_bound_'+tag,gap<upper)
  ct('unweighted_resource_wrong_'+tag,resource!=2*len(schedule))
  policies.append({'multiplier':str(lm),'budget':budget,'step':str(step),'schedule':schedule,'count':len(schedule),'resource':str(resource),'gap':gap.str(35,more=True),'safe_bound':upper.str(35,more=True),'coefficient':Cb.str(35,more=True)})
report={'result':'K2604','checks':checks,'contrary_controls':controls,'interval_sign_certificates':certificates,'theorem':'gap=C/M+O(M^-2) for full original adaptive class, 0<S<=1/2,0<lambda<=4/5; compact positive-parameter uniformity','feasible_bound':'M>=8: C/(M-4)+70C/(M-4)^2 <= C/M+288C/M^2','barrier_constants':{'delta':'lambda_min/1250','K':'1251/lambda_min+1','e_max':'min(lambda_min/2,lambda_min*gamma*delta/16)'},'consequences':['priced value V-2sqrt(Ck)+O(k)','inverse resource C/eta+O(1)','every price optimizer R=sqrt(C/k)+O(k^-1/4); deterministic optimal n=Theta(k^-1/2)'],'finite_consumers':policies,'evidence_kind':'exact rational whole-interval coefficient/derivative inequalities, square and constant identities, actual original-law rational policies with Arb192-bit values; analytic barrier and telescope in note','ceiling':'no second coefficient, no exact finite optimal policy, no differentiability across count ties, no physical or GU claim'}
refs=['explorations/conditional-build/k2602-continuum-stopping-resource-law-2026-11-06.md','lab/process/k2602-continuum-stopping-resource-law.json','explorations/conditional-build/k2561-higher-budget-stopping-2026-11-05.md','explorations/conditional-build/k2571-stopping-resource-price-2026-11-05.md']
report['provenance']={f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in refs}
out=root/'lab/process/k2604-second-order-stopping-resource-bound.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'FAIL report replay'
print(json.dumps({'result':'K2604','checks':len(checks),'controls':len(controls),'finite_consumers':len(policies),'status':'pass'}))
