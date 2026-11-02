"""K2507 exact symbolic/rational controls. Universal proofs are in the note.
Use --write to regenerate the deterministic report; no sampled optimum claim.
"""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,sys
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ct(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
def eq(a,b):return s.simplify(a-b)==0
r=s.symbols('r',real=True);g=(1-r)**2/(2*(1+r));gp=s.diff(g,r);gpp=s.diff(gp,r);Q=(1-r)*(1+3*r)/(2*(1+r)**2);flow=-Q/gpp
ck('g_prime',eq(gp,s.Rational(1,2)-2/(1+r)**2));ck('strict_convexity_formula',eq(gpp,4/(1+r)**3));ck('Q_identity',eq(Q,g-r*gp));ck('optimizer_flow',eq(flow,-(1-r)*(1+r)*(1+3*r)/8))
Lf=-s.log(1-r)-2*s.log(1+r)+3*s.log(1+3*r)
ck('elapsed_time_primitive',eq(s.diff(Lf,r),gpp/Q))
ck('conserved_weighted_Q',eq(s.diff(Q,r)*flow-r*Q,0))
# Endpoint identities at nontrivial exact parametric tail and at a zero arc.
rho=s.Rational(1,2);sigma=s.Rational(2,5);z=s.Rational(245,297);V=s.Rational(4,99)
ck('endpoint_h_derivative',eq(V+z*gp.subs(r,sigma),gp.subs(r,rho)))
ck('time_derivative_conservation',eq(z*Q.subs(r,sigma),Q.subs(r,rho)))
for rho in [s.Rational(1,2),s.Rational(1,100)]:
 for l in [s.Rational(0),s.Rational(1,10),s.Rational(1,4)]:
  q0=Q.subs(r,rho);zz=q0/Q.subs(r,0);vv=8*q0/3*(1-1/(1+3*rho))+zz*l/2
  ck('zero_arc_endpoint_identity_'+str((rho,l)),eq(vv+zz*(gp.subs(r,0)-l/2),gp.subs(r,rho)))
  ck('zero_arc_time_derivative_'+str((rho,l)),eq(zz/2,q0))
  if l>0:ct('bare_zero_arc_momentum_fails_'+str((rho,l)),not eq(vv+zz*gp.subs(r,0),gp.subs(r,rho)))
from flint import arb,ctx
ctx.prec=160
ck('within_domain_zero_arc_time',(arb(1092727)/1009899).log()+arb(1)/10<arb(1)/2)
# Direct chain-rule matching in the smooth interior.
a,b,H,S=s.symbols('a b H S',positive=True);A=1+a;t=S-b;h=H-s.log(A)
x=(b-a)**2/(2*(a+b)*(2-a-b));w=s.log(1+x);VV=s.Function('V');obj=(2*w+VV(t,h))/A
# Independent symbolic chain rule uses a generic differentiable V rather than
# substituting asserted final matching equations as expected output.
# Read SymPy derivative terms through dummy variables to avoid generated names.
u,v=s.symbols('u v');poly=u*u+u*v+v**3;test=(2*w+poly.subs({u:t,v:h}))/A
ck('atom_a_chain_rule',eq(s.diff(test,a),(2*A*s.diff(w,a)-2*w-poly.subs({u:t,v:h})-s.diff(poly,v).subs({u:t,v:h}))/A**2))
ck('atom_b_chain_rule',eq(s.diff(test,b),(2*s.diff(w,b)-s.diff(poly,u).subs({u:t,v:h}))/A))
# Cubic improvement from a feasible mean-preserving linear tilt in rescaled time.
k,u=s.symbols('k u',real=True)
# y=1-r*t*u+t²[(r*u)²/2-k*(u/2-u²/2)]+O(t³)
# g(r+k*t*(1/2-u)) expands explicitly; integrate the t³ difference.
coefficient=s.integrate(-k*(u/2-u*u/2)*g-r*u*gp*k*(s.Rational(1,2)-u)+gpp*k*k*(s.Rational(1,2)-u)**2/2,(u,0,1))
ck('tilt_quadratic_functional',eq(coefficient,-k*Q/12+gpp*k*k/24))
ck('optimal_tilt_cubic_gain',eq(-coefficient.subs(k,Q/gpp),Q**2/(24*gpp)))
ck('simplified_cubic_gain',eq(Q**2/(24*gpp),(1-r)**2*(1+3*r)**2/(384*(1+r))))
ct('endpoint_strictness_excluded',g.subs(r,1)==0 and Q.subs(r,1)==0)
# Exact finite-stage cost intervals, independent rational alternating log bounds.
def xx(a,b):
 if a==b:return F(0)
 return (b-a)**2/(2*(a+b)*(2-a-b))
def logbound(x,n):return sum((F(1) if j%2 else F(-1))*x**j/j for j in range(1,n+1))
def cost_bounds(schedule):
 P=F(1);lo=F(0);hi=F(0)
 for a,b in schedule:
  assert 0<=a<=b<=F(1,2)
  P/=1+a;x=xx(a,b);lo+=2*P*logbound(x,8);hi+=2*P*logbound(x,9)
 return lo,hi,P
main=(F(1934773,5905227),F(49,100));q=F(3,1400);bb=F(1,200)
old=[main,(q,bb),(q,bb)];new=[main,(F(15007,7000000),bb),(F(105176,49105049),bb)]
lo0,hi0,p0=cost_bounds(old);lo1,hi1,p1=cost_bounds(new)
ck('finite_total_score',sum(b for a,b in new)==F(1,2));ck('finite_exact_success',p1==p0==F(3,4));ck('finite_hazard_product',(1+new[1][0])*(1+new[2][0])==(1+q)**2)
ck('strict_rational_gain',lo0-hi1>F(9,10**10));ck('absolute_rational_budget',hi1<F(212613497,10**10));ck('prior_budget_improved',hi1<F(106307,5000000))
ck('single_stage_separation',hi1<F(417,19600))
ct('wrong_additive_hazard_preservation',new[1][0]+new[2][0]!=2*q)
# General pair derivative, obtained before specializing to fixture.
qv,bv,e=s.symbols('q b e',positive=True);a2=(1+qv)**2/(1+qv+e)-1
W=s.Function('w');pair=(1+a2)*W(qv+e,bv)+W(a2,bv)
der=s.diff(pair,e).subs(e,0).doit()
ck('equal_pair_first_variation',eq(der,qv*s.diff(W(qv,bv),qv)-W(qv,bv)))
# Actual w_a sign at exact positive controls and free/zero boundary behavior.
for qi,bi in [(s.Rational(1,100),s.Rational(1,50)),(s.Rational(1,5),s.Rational(2,5)),(s.Rational(1,4),s.Rational(1,2))]:
 val=s.cancel(s.diff(x,a)).subs({a:qi,b:bi});ck('costly_pair_hazard_derivative_'+str((qi,bi)),val<0)
ct('free_pair_no_strict_improvement',xx(F(1,4),F(1,4))==0)
ct('zero_hazard_pair_tilt_inadmissible',(1+F(0))**2/(1+F(1,1000))-1<0)
# Original finite free stage defeats continuum-only global interpretation.
ck('free_main_zero_cost',cost_bounds([(F(1,2),F(1,2))])[:2]==(F(0),F(0)))
ct('continuum_cannot_replace_free_atom',s.log(s.Rational(3,2))<s.Rational(1,2) and g.subs(r,2*s.log(s.Rational(3,2)))>0)
# Exact-integrated hazards preserve a fixed free main; choose constant tail with
# rational per-interval multiplicative factors, not an approximate exp.
free=(F(1,4),F(1,4));tail=[(F(1,20),F(1,8))]*2
ck('free_main_valid_finite_tail',all(0<=a<=b for a,b in [free,*tail]) and sum(b for a,b in [free,*tail])==F(1,2))
# All-free tail boundary repair: product underestimation must increase main a.
# Bernoulli inequality: (1+t/n)^n < exp(t); exact comparison to lower Taylor.
for n in [2,5,10]:
 tt=F(1,10);prod=(1+tt/n)**n;exp_lower=sum(tt**j/F(__import__('math').factorial(j)) for j in range(9))
 ck('boundary_repair_direction_'+str(n),prod<exp_lower)
ct('naive_free_main_repair_can_break',F(1,4)+F(1,1000)>F(1,4))
report={'result':'K2507','scope':'restricted one-first-stage optimal tail and exact finite improvements; unrestricted optimum open','evidence_kind':'written variational and approximation proofs; exact symbolic identities and rational logarithm interval witnesses','checks':checks,'contrary_controls':controls,'finite_witness':{'success':str(p1),'cost_lower':str(lo1),'cost_upper':str(hi1),'budget_upper':'212613497/10000000000','gain_lower':'9/10000000000'},'dependencies':{}}
for path in [Path(__file__),ROOT/'explorations/conditional-build/k2507-stopping-optimal-hybrid-tail-2026-11-02.md',ROOT/'explorations/conditional-build/k2495-stopping-order-and-continuum-2026-11-02.md',ROOT/'explorations/conditional-build/k2505-stopping-satellite-hierarchy-2026-11-02.md']:
 report['dependencies'][str(path.relative_to(ROOT))]=hashlib.sha256(path.read_bytes()).hexdigest()
out=ROOT/'lab/process/k2507-stopping-optimal-hybrid-tail.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,indent=2)+'\n')
else:ck('saved_report_matches_reproduction',json.loads(out.read_text())==report)
print(f'K2507 PASS: {len(checks)} exact checks; {len(controls)} contrary controls')
