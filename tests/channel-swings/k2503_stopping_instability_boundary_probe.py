"""Exact original-cost, directional and interval certificates for K2503."""
from pathlib import Path
from fractions import Fraction as F
import sympy as s
import json,hashlib,sys
ROOT=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ct(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
def warg(a,b):return (b-a)**2/(2*(a+b)*(2-a-b))
def lb(x):return x-x*x/2
def ub(x):return x-x*x/2+x**3/3
r,u,d,z=s.symbols('r u d z',real=True)
g=(1-r)**2/(2*(1+r));D=(1-d*d)*(2-d*d);A=4*d/D;q=1-2*d*d;L=s.Rational(3,2)-d
w=s.log((2-d*d)/(2*(1-d*d)));B=A*q/L;M=L*A+2*w;N=A*q;Z=M+N;H=Z*Z+4*(N-M)
ck('g_first',s.cancel(s.diff(g,r)-(s.Rational(1,2)-2/(1+r)**2))==0)
ck('g_second',s.cancel(s.diff(g,r,2)-4/(1+r)**3)==0)
rr=2/s.sqrt(1+2*u)-1
ck('interior_value',s.simplify((g+u*r).subs(r,rr)-(2*s.sqrt(1+2*u)-u-2))==0)
ck('w_derivative',s.cancel(s.diff(w,d)-A/2)==0)
ck('M_derivative',s.simplify(s.diff(M,d)-L*s.diff(A,d))==0)
ck('Z_second',s.simplify(s.diff(Z,d,2)-((s.Rational(5,2)-d-2*d*d)*s.diff(A,d,2)-(1+8*d)*s.diff(A,d)-4*A))==0)
ck('H_initial',H.subs(d,0)==0 and s.diff(H,d).subs(d,0)==-4)
Dz=2-3*z+z*z;Ez=2+3*z-3*z*z
polys=[36*z-38*z*z+12*z**3-2*z**4,2*z*(2-41*z+59*z*z-29*z**3+5*z**4),z*(560-1260*z+1182*z*z-594*z**3+162*z**4-18*z**5),2*z*(1-5*z+2*z*z)]
ck('Aprime_lower_identity',s.expand(4*Ez-2*Dz**2-polys[0])==0)
ck('Aprime_upper_identity',s.expand((2+10*z)*Dz**2-4*Ez-polys[1])==0)
ck('Asecond_lower_identity',s.expand(8*(18-11*z-9*z*z+6*z**3)-18*Dz**3-polys[2])==0)
ck('A_upper_identity',s.expand((2+4*z)*Dz-4-polys[3])==0)
# Divide the common nonnegative z factor; bound every negative monomial on [0,1/25].
for i,poly in enumerate(polys):
 pp=s.Poly(s.cancel(poly/z),z);lower=F(0)
 for (deg,),coef in pp.terms():
  cc=F(int(coef.p),int(coef.q))
  if deg==0:lower+=cc
  elif cc<0:lower+=cc*F(1,25)**deg
 ck('whole_interval_polynomial_'+str(i),lower>0)
ck('Asecond_upper',F(144)/(F(47,25)**3)<22)
ck('Z_second_lower',21-28*F(1,5)-132*F(1,5)**2>0)
ck('Z_first_lower',F(111,50)*2-4*F(1,5)*F(54,125)==F(2559,625))
ck('Z_upper',F(27,25)+F(1,24)==F(673,600))
ck('NM_second_lower',-F(1,2)*F(22,5)-F(3,5)*F(12,5)-4*F(54,125)==-F(671,125))
ck('H_convex_bound',2*F(2559,625)**2-4*F(673,600)-F(2684,125)>7)
ck('M_interior_domain',F(3,2)*F(54,125)+F(1,24)<F(3,2))
ck('H_decreases_in_M',F(673,600)<2)
def hr(dd,ww):
 aa=4*dd/((1-dd*dd)*(2-dd*dd));mm=(F(3,2)-dd)*aa+2*ww;nn=aa*(1-2*dd*dd)
 return (mm+nn)**2+4*(nn-mm)
root_signs={}
for name,dd,upper in [('left',F(4,25),True),('right',F(17,100),False)]:
 xx=dd*dd/(2*(1-dd*dd));hh=hr(dd,lb(xx) if upper else xx)
 ck('root_bracket_'+name,hh<0 if upper else hh>0);root_signs[name]=str(hh)
R=-6+41*d-43*d*d-44*d**3+61*d**4-16*d**6+8*d**7
ck('prefix_sign_polynomial',s.cancel(((A+B)**2+4*(B-A))*D**2*L**2/(4*d)-R)==0)
ck('prefix_tail_pair_sign',-44+61*F(17,100)<0 and -16+8*F(17,100)<0)
ck('prefix_quadratic_increasing',41-86*F(17,100)>0)
ck('prefix_interval_bound',-6+41*F(17,100)-43*F(17,100)**2==-F(2727,10000))
AA=F(864,2485);BB=F(612,2485)
ck('exact_prefix_positive', (AA+BB)**2+4*(BB-AA)==-F(326304,6175225))
ck('suffix_negative',-F(268,17395)+F(6,7)*F(1,70)==-F(11,3479))
# Rational finite policy directly from original cost and survival.
stages=[(F(691,2109),F(49,100)),(F(3,700),F(1,100))];p=F(1);lo=hi=F(0)
for a,b in stages:
 ck('feasible_'+str(a),0<=a<=b);p/=1+a;xx=warg(a,b);lo+=2*p*lb(xx);hi+=2*p*ub(xx)
K=F(2127,100000);single_lo=F(3,2)*lb(F(1,70))
ck('score',sum(b for a,b in stages)==F(1,2));ck('success',p==F(3,4));ck('finite_policy_budget',hi<K)
ck('one_stage_cost_lower',single_lo==F(417,19600));ck('cost_gap',single_lo-K==F(27,4900000))
ck('derivative_upper',2*F(1,70)+F(1152,2485)<F(1,2))
ck('mixture_gap',2*(single_lo-K)==F(27,2450000))
# Exact cost derivative with p reparametrization.
pv=s.symbols('p',positive=True);av=1/pv-1
cv=2*pv*s.log(1+(s.Rational(1,2)-av)**2/(2*(av+s.Rational(1,2))*(s.Rational(3,2)-av)))
ck('cost_derivative_at_witness',s.simplify(s.diff(cv,pv).subs(pv,s.Rational(3,4))-2*s.log(s.Rational(71,70))-s.Rational(1152,2485))==0)
def boundary_second_checks():
 t=s.symbols('t',real=True);a=s.Rational(1,2)-d;L=1+a;k=r*L
 uu,v=s.symbols('uu v');u=uu;D=2*u*(2-u);N=D+v*v;W=s.log(N/D)
 sub={u:1-d,v:d}
 wuu=s.cancel(s.diff(W,u,2).subs(sub));wuv=s.cancel(s.diff(W,u,v).subs(sub));wvv=s.cancel(s.diff(W,v,2).subs(sub));wb=s.cancel((s.diff(W,u)+s.diff(W,v)).subs(sub))
 B=(1+k)**2*wuu+2*(1-k*k)*wuv+(1-k)**2*wvv-2*r*wb+(1-r)**2/4-(1-r)**4/(16*(1+r)**2)
 # Chain derivative of (1+rt)w(a(t),b(t)), plus smooth satellite log.
 at=(a-r*t)/(1+r*t);bt=s.Rational(1,2)-t;ut=at+bt;vt=bt-at
 mainsecond=(s.diff(W,u,2)*s.diff(ut,t)**2+2*s.diff(W,u,v)*s.diff(ut,t)*s.diff(vt,t)+s.diff(W,v,2)*s.diff(vt,t)**2+s.diff(W,u)*s.diff(ut,t,2)+s.diff(W,v)*s.diff(vt,t,2)+2*r*(s.diff(W,u)*s.diff(ut,t)+s.diff(W,v)*s.diff(vt,t))).subs(t,0).subs(sub)
 small=s.log(1+(1-r)**2*t/(2*(1+r)*(2-(1+r)*t)))
 ck('second_coefficient_identity',s.cancel(mainsecond+s.diff(small,t,2).subs(t,0)-B)==0)

 ck('root_ratio_M_lower',F(284,625)>F(759,1682))
 ck('root_ratio_M_upper',F(129,250)<F(51,98))
 ck('root_box_A_upper',(2*F(17,100)+4*F(17,100)**3)<F(9,25))
 ck('root_box_log_upper',F(17,100)**2/(1-F(17,100)**2)<F(3,100))
 ck('root_box_k_bounds',F(2,5)*F(133,100)>F(1,2) and F(9,20)*F(67,50)<F(61,100))
 ck('root_box_mixed_hessian',8*F(17,100)**2/(2-F(17,100)**2)**2<F(3,50))
 ck('root_box_vv_hessian',1-4*F(17,100)**2/(2-F(17,100)**2)**2>F(97,100))
 ck('root_box_wb',2*F(17,100)/((1-F(17,100)**2)*(2-F(17,100)**2))<F(9,50))
 ck('root_box_satellite',F(121,1600)-F(81,19600)>F(7,100))
 lower=F(9,4)*F(16,625)-F(3,2)*F(3,50)+F(39,100)**2*F(97,100)-2*F(9,20)*F(9,50)+F(7,100)
 ck('root_box_second_lower',lower==F(23137,1000000) and lower>F(1,50))
 ck('root_box_cost_second_lower',F(1,50)/F(67,50)==F(1,67))
boundary_second_checks()

# Released onset identities and leading-order optimized/repriced cost algebra.
ck('single_cost_d_derivative',s.simplify(s.diff(2*w/L,d)-M/L**2)==0)
ck('fixed_success_d_derivative',s.simplify(s.diff(1/L,d)-1/L**2)==0)
a0,b0,c0,L0,M0=s.symbols('a0 b0 c0 L0 M0',positive=True)
x=s.symbols('x',real=True)
ck('quadratic_score_optimum',s.diff(-a0*x+b0*x*x,x).subs(x,a0/(2*b0))==0)
ck('quadratic_cost_gain',s.simplify((-a0*x+b0*x*x).subs(x,a0/(2*b0))+a0*a0/(4*b0))==0)
ck('budget_gain_coefficient',s.cancel((a0*a0/(4*b0))*(1/L0**2)/(M0/L0**2)**3-(a0*a0/(4*b0))*L0**4/M0**3)==0)
ck('stationary_jacobian_invertible',s.Matrix([[2*b0,0],[c0,s.Integer(1)]]).det()==2*b0)

# Contrary constructions are changed models/formulas, not flipped checker Booleans.
ct('prefix_only_misses_suffix', (AA+BB)**2+4*(BB-AA)<0 and -F(268,17395)+F(6,490)<0)
ct('unclipped_ratio_invalid', 2/s.sqrt(1+2*s.Integer(4))-1<0)
wrong_success=1/((1+F(1,3))*(1+F(3,700)))
ct('unrepaired_success_changes',wrong_success!=p)
wrong_cost=2*p*sum(lb(warg(a,b)) for a,b in stages)
ct('final_survival_for_all_stages_wrong',wrong_cost<lo)
ct('cost_free_satellite_wrong',2*p*ub(warg(*stages[0]))<lo)
ct('global_one_stage_optimum_false',hi<single_lo)
ct('tiny_interval_not_transition',F(1,2**88)<K)
deps=[next((ROOT/'explorations/conditional-build').glob(k+'-*.md')) for k in ['k2485','k2493','k2499','k2501']]
report={'result':'K2503','checks':checks,'contrary_controls':controls,'root_bracket':['4/25','17/100'],'boundary_equality':{'second_cost_coefficient_lower':'1/67','coefficient_scope':'suffix ratios r in [2/5,9/20] and d in [4/25,17/100]','scope':'uniform sufficiently small single satellites, both orders; no explicit radius or global optimum'},'root_sign_certificates':root_signs,'onset_branch':{'satellite_score':'alpha*(d-d_star)/(2*beta0)+O((d-d_star)^2)','fixed_success_cost_gain':'Gamma*(d-d_star)^2+O((d-d_star)^3)','same_budget_success_gain':'Gamma*L0^4/M0^3*(K-K0)^2+O((K-K0)^3)','scope':'constructed local suffix optimum; lower separation from one-stage mixtures; not the global frontier'},'finite_policy':{'stages':[[str(a),str(b)] for a,b in stages],'success':str(p),'cost_lower':str(lo),'cost_upper':str(hi),'budget':str(K),'one_stage_mixture_gap':'27/2450000'},'evidence_kinds':{'exact':'symbolic identities, rational whole-interval bounds and original finite-policy costs','universal':'written strict-convexity/root and supporting convex-mixture arguments','not_claimed':'global adaptive transition or finite-error optimizer'},'dependencies':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2503-stopping-instability-boundary.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
else:ck('saved_report_reproduction',json.loads(out.read_text())==report)
print(json.dumps({'result':'PASS','checks':len(checks),'contrary_controls':len(controls)}))
