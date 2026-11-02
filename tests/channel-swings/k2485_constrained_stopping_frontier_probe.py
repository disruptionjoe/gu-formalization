"""Small exact/Arb checks; paired written proofs, not finite grids, carry universal scope.
Run with the GU dependency interpreter. No writes to owner truth.
"""
from fractions import Fraction as F
import json,hashlib,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
from flint import arb, ctx
import sympy as sy
ctx.prec=256
checks={};controls={}
def ck(n,v):
 checks[n]=bool(v)
 if not v: raise AssertionError(n)
def ctrl(n,v):
 controls[n]=bool(v)
 if not v: raise AssertionError('contrary: '+n)
def ar(x):
 x=F(x);return arb(x.numerator)/x.denominator
def Q(s):
 if s<=0:return F(1)
 m=s.numerator//s.denominator
 return F(1,2**m)/(1+s-m)
def U(s,l):return F(1) if s<=0 else min(F(1),Q(s)+s/l)
def lower(a,b):
 if a>=b:return F(0)
 d=b-a;D=2*(a+b)*(2-a-b)
 return d*d/(D+d*d)
def cost(a,b):
 if a>=b:return arb(0)
 return (1+ar((b-a)**2/(2*(a+b)*(2-a-b)))).log()
a,b,d,l=sy.symbols('a b d l')
D=2*(a+b)*(2-a-b)
ck('original_denominator_gap_identity',sy.expand(8*b-D-(b-a)**2-(4*(b-a)+a*a+6*a*b+b*b))==0)
xx=(b-a)**2/(2*(a+b)*(2-a-b))
ck('overshoot_cost_monotonicity_derivative',sy.factor(sy.diff(xx,b)-(b-a)*(3*a+b-2*a*a-2*a*b)/((a+b)**2*(2-a-b)**2))==0)
ck('overshoot_derivative_positive_decomposition',sy.expand(3*a+b-2*a*a-2*a*b-(a*(1-a)+(a+b)*(1-a)+a*(1-b)))==0)
ck('young_square_identity',sy.expand(l*l*d*d-4*b*l*d+4*b*b-(l*d-2*b)**2)==0)
# Exact rational lower cost establishes stronger sampled inequalities than actual log cost.
for si in range(1,17):
 s=F(si,4)
 for lam in [F(1,2),F(1),F(2),F(8),F(32)]:
  for bi in range(9):
   bb=F(bi,8)
   for ai in range(bi+1):
    aa=F(ai,8)
    ck(f'whole_stage_{si}_{lam}_{bi}_{ai}',U(s-bb,lam)-(1+aa)*U(s,lam)<=2*lam*lower(aa,bb))
# Strict contrary controls reveal why cost slack and overshoot extension matter.
ctrl('bare_zero_budget_boundary_not_positive_cost_supersolution',ar(Q(F(0))-Q(F(1)))>2*ar(F(1,10))*cost(F(0),F(1)))
ctrl('naive_negative_extension_breaks_target_majorization',Q(F(-1,2))+F(-1,2)/8<1)
ctrl('target_cap_is_active',Q(F(1,4))+F(1,4)/F(1,2)>1 and U(F(1,4),F(1,2))==1)
# Native cost bound checked at interior and degenerate controls without replacing the law.
for aa,bb in [(F(0),F(1,2)),(F(1,4),F(1,2)),(F(7,8),F(1)),(F(0),F(1))]:
 ck('actual_log_bound_'+str((aa,bb)),cost(aa,bb)>ar(lower(aa,bb))>=ar((bb-aa)**2/(8*bb)))
ck('zero_diagonal_cost',cost(F(0),F(0))==0 and cost(F(1),F(1))==0)
# Original one-stage finite library at remaining score1/2. At K=K_C/2 a mixture
# is strictly better than every feasible individual member of this library.
pq=F(2,3);pc=F(4,5);pb=F(1)
kc=ar(F(8,5))*(ar(F(31,30))).log()
kb=2*(ar(F(7,6))).log()
ck('native_C_cost_formula',(2*cost(F(1,4),F(1,2))/ar(F(5,4))).overlaps(kc))
ck('native_B_cost_formula',(2*cost(F(0),F(1,2))).overlaps(kb))
ck('finite_library_strict_cost_order',kb>kc and kc>0)
K=kc/2;pm=(pq+pc)/2;mu=ar(pc-pq)/kc
ck('finite_library_support_excludes_B',ar(pb)-mu*kb<ar(pq))
ck('finite_library_support_excludes_abort',ar(pq)>0)
ck('exact_two_policy_probability',pm==F(11,15))
ck('finite_library_dual_equals_primal',(ar(pq)+mu*K).overlaps(ar(pm)))
ctrl('single_policy_restriction_loses_finite_library_frontier',pm>pq and kc>K and kb>K)
# The universal theorem concerns all schedules: this fixture is not a global optimum.
# Exact original stage law from finite geometric pass-loop sums.
aa,bb=F(1,4),F(1,2);stay=(1-aa)/2
for n in [1,2,8,32]:
 hit=sum(stay**j/2 for j in range(n));trials=sum(stay**j for j in range(n))
 ck(f'geometric_hit_{n}',hit==(1-stay**n)/(1+aa))
 ck(f'geometric_all_path_cost_multiplier_{n}',trials==2*(1-stay**n)/(1+aa))
ctrl('success_only_accounting_is_not_original_cost',F(2)/(1+aa)>F(2)/(1+aa)**2)
# Exact saturation/no-attainment ingredients on the original law.
ck('sure_hit_cost_lower_polynomial',sy.expand(4*(b-a)**2-(b-3*a)*(D+(b-a)**2)-(16*a*a+(b-3*a)*(a*a+6*a*b+b*b)))==0)
for bi in range(9):
 for ai in range(9):
  aa,bb=F(ai,8),F(bi,8)
  ck(f'saturation_scalar_{ai}_{bi}',lower(aa,bb)>=(bb-3*aa)/4)
  if bb>0:ck(f'saturation_scalar_strict_{ai}_{bi}',lower(aa,bb)>(bb-3*aa)/4)
ck('equal_stage_sure_hit_limit',sy.limit(2*sy.log((4-b)/(4-2*b))/b,b,0)==sy.Rational(1,2))
ss=F(3,2);sat=[]
for n in [2,8,32,128,1024]:
 bb=ss/n;kn=2*n*cost(F(0),bb);alpha=ar(ss)/(2*kn)
 ck('sure_hit_cost_strict_'+str(n),kn>ar(ss/2))
 ck('critical_budget_mixture_probability_'+str(n),0<alpha and alpha<1)
 ck('critical_budget_exact_spending_'+str(n),(alpha*kn).overlaps(ar(ss/2)))
 sat.append({'n':n,'cost':str(kn),'critical_budget_probability':str(alpha)})
ck('critical_budget_approach',alpha>ar(F(999,1000)))
ctrl('sure_hit_endpoint_not_attained_by_positive_stage',2*cost(F(0),F(1,2))>ar(F(1,4)))
# Optional two-stage tangent optimization: exact stationarity and root interval.
x,y,k=sy.symbols('x y k')
expr=(2*x-y+1)**2/(2*(2*x+y-1))+(y-x)**2/(2*(y+x))
kk=(2*x-y+1)/(2*x+y-1);ll=(y-x)/(y+x)
ck('tangent_x_derivative',sy.factor(sy.diff(expr,x)-(2*kk-kk*kk-ll-ll*ll/2))==0)
ck('tangent_value_euler_identity',sy.factor(expr-x*sy.diff(expr,x)-y*sy.diff(expr,y)-(kk+kk*kk/2))==0)
ck('tangent_y_derivative',sy.factor(sy.diff(expr,y)-(-kk-kk*kk/2+ll-ll*ll/2))==0)
llk=3*k/2-k*k/4
ck('stationary_cubic_identity',sy.expand(llk**2-k+3*k*k/2-k*(k**3-12*k*k+60*k-16)/16)==0)
lo=F(2822218562575163,10**16);hi=F(2822218562575165,10**16)
def cubic(t):return t**3-12*t*t+60*t-16
ck('unique_root_exact_bracket',cubic(lo)<0<cubic(hi))
clo=arb(2).log()/ar(hi+hi*hi/2);chi=arb(2).log()/ar(lo+lo*lo/2)
ck('tangent_coefficient_interval',clo>ar(F(21523205511465,10**13)) and chi<ar(F(21523205511466,10**13)))
# Algebraic stationary reconstruction, reducing numerator residuals modulo cubic.
rr=(1-llk)/(1+llk);tt=(1+k)/((1+k)-2*rr*(1-k));poly=k**3-12*k*k+60*k-16
for name,z in [('reconstructed_k',(2*rr*tt-tt+1)/(2*rr*tt+tt-1)-k),('reconstructed_l',(tt-rr*tt)/(tt+rr*tt)-llk),('stationary_x',2*k-k*k-llk-llk*llk/2),('stationary_y',-k-k*k/2+llk-llk*llk/2)]:
 num=sy.fraction(sy.cancel(z))[0]
 ck('mod_cubic_'+name,sy.rem(num,poly,k)==0)
ck('root_feasibility_bracket',F(7,25)<lo<hi<F(29,100))
ck('l_feasible_from_monotone_bracket',F(1,3)<F(3,2)*F(7,25)-F(7,25)**2/4 and F(3,2)*F(29,100)-F(29,100)**2/4<1)
# Predeclared rational two-stage witness; no control search or surrogate costs.
r=F(42509,100000);t=F(47703,25000);h=F(1,268435456);A=2*r*t;B=t-1
seq=[(1-A*h,1-B*h),(r*t*h,t*h)]
pp=F(1);budget=arb(0)
for aa,bb in seq:
 ck('finite_rational_admissible_'+str((aa,bb)),0<aa<bb<=1)
 budget+=ar(pp)*2*cost(aa,bb)/ar(1+aa);pp/=1+aa
ratio=arb(2).log()*ar(h)/(2*budget)
ck('finite_rational_exact_probability',pp==1/(2*(1-(r*t*h)**2)) and pp>F(1,2))
ck('finite_rational_exact_score',sum(bb for aa,bb in seq)==1+h and seq[0][1]<1)
ck('finite_rational_strict_coefficient',ratio>ar(F(26904,12500)))
for m in [0,1,4,20]:
 rho=F(1,2**m);eps=rho/2
 ck('dyadic_rational_witness_'+str(m),rho*pp>eps and eps/rho==F(1,2))
deps=['explorations/conditional-build/k2483-adaptive-stopping-bellman-2026-11-01.md','tests/channel-swings/k2483_adaptive_stopping_bellman_probe.py','lab/process/k2483-adaptive-stopping-bellman.json']
report={'result':'K2485','checks':checks,'contrary_controls':controls,'finite_library':{'K':str(K),'P':str(pm),'lambda':str(mu)},'tangent_coefficient':[str(clo),str(chi)],'finite_witness':{'r':str(r),'t':str(t),'h':str(h),'probability':str(pp),'original_budget':str(budget),'coefficient':str(ratio)},'saturation_fixtures':sat,'evidence_kinds':{'universal':'written original-law supersolution, supporting-line duality and finite LP proof','exact':'polynomial identities and finite rational regression cases','interval':'original logarithmic budgets and algebraic-root coefficient bounds','inherited':'K2483 original stage support equality and zero-cost law authenticated, not rerun'},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2485-constrained-stopping-frontier.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
else:ck('saved_report_reproduces',json.loads(out.read_text())==report)
print(json.dumps({'result':'PASS','checks':len(checks),'controls':len(controls),'tangent_coefficient':[str(clo),str(chi)]}))
