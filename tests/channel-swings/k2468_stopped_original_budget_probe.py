"""Actual binary stopping/entropy proof algebra and rigorous numerical consumers."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,sys
import sympy as sp
from flint import arb,ctx
ctx.prec=256
ROOT=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ctrl(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
def ar(x):
 x=F(x);return arb(x.numerator)/x.denominator
c=arb(2).log();Ls=c-ar(F(1,2));C=(1+Ls)**2/(4*Ls);lower=(1+c)**2/(4*(1-c));rr=(3*c-1)/(3-c)
ck('rigorous_constant_bracket',ar(F(2335,1000))<lower<ar(F(2336,1000))<ar(F(5,2))<2*C)
ck('prior_upper_large_a',C<ar(F(15,8)) and 4*C/3<ar(F(5,2)))
ck('optimal_endpoint_ratio',(2*(c-rr)*(1+rr)/(1-rr)**2-lower).contains(0) and 0<rr<c<1)
a,d,x,r,cs=sp.symbols('a d x r c',real=True)
den=(2*a+d)*(2-2*a-d);v=d*d/den;Nbar=sp.Rational(7,10)*(a+d)-2*a/(a+2)
P=8*a*a*(1-a)*(6-7*a)-4*a*(22+5*a-28*a*a)*d+(63*a*a+128*a+44)*d*d+(7*a+14)*d**3
ck('global_upper_polynomial_identity',sp.cancel(10*(a+2)*den*(5*v-Nbar*(2+v))-P)==0)
Q=P-(7*a+14)*d**3;FF=-98*a**4-434*a**3+749*a*a-172*a-44
ck('quadratic_discriminant',sp.expand(sp.discriminant(Q,d)-16*a*a*FF)==0)
bern=[-44,-sp.Rational(131,2),-sp.Rational(1339,24),-sp.Rational(455,16),-sp.Rational(25,8)]
ck('full_Bernstein_identity',sp.expand(sum(b*sp.binomial(4,i)*x**i*(1-x)**(4-i) for i,b in enumerate(bern))-FF.subs(a,x/2))==0)
ck('all_Bernstein_strict_negative',all(b<0 for b in bern))
R0=2*(cs-r)*(1+r)/(1-r)**2;rstar=(3*cs-1)/(3-cs)
ck('endpoint_stationary',sp.cancel(sp.diff(R0,r).subs(r,rstar))==0)
ck('endpoint_value',sp.cancel(R0.subs(r,rstar)-(1+cs)**2/(4*(1-cs)))==0)
# Explicit actual absorption law, exact recurrence and finite tail.
a0=F(1,100);b0=F(1,50);eps=F(99,100);p=1/(1+a0);v0=(b0-a0)**2/((a0+b0)*(2-a0-b0));ck('actual_v',v0==F(1,591))
w=(1+ar(v0)/2).log();K=2*w*ar(p);hit=c*ar(b0);bad_threshold=(1/ar(eps)).log()+2*K/ar(eps)
ctrl('coefficient_two_actual_violation',hit>bad_threshold and p>eps)
ck('upper_2point5_covers_fixture',(1/ar(eps)).log()+ar(F(5,2))*K/ar(eps)>hit)
psi=(hit-(1+ar(a0)).log())/2;h=((1-ar(a0))/2+(c*ar(b0)).exp()/2).log()
ck('strict_entropy_cost_gain',0<psi<h)
ck('actual_entropy_equality',(ar(p)*(hit+ar(p).log())-2*ar(p)*psi).contains(0))
epsJ=p-F(1,10000000)
ctrl('coefficient_below_one_entropy_fails',hit>(1/ar(epsJ)).log()+ar(F(99,100))*2*ar(p)*psi/ar(epsJ) and p>epsJ)
ck('test_use_pass_failure_total',F(1,2)+a0/2+(1-a0)/2==1)
ck('exact_eventual_hit',F(1,2)/(1-(1-a0)/2)==p)
ck('exact_expected_steps',1/(1-(1-a0)/2)==2*p)
passprob=(1-a0)/2
for n in [1,2,5,20]:
 hitprob=sum(passprob**i/2 for i in range(n));failprob=sum(passprob**i*a0/2 for i in range(n));tail=passprob**n
 ck('actual_finite_tree_'+str(n),hitprob+failprob+tail==1 and hitprob==p*(1-tail))
# Direct entropy optimization finite controls, distinct from universal derivative proof.
for ai in [F(0),F(1,100),F(1,2),F(1)]:
 for bi in [F(1,50),F(1,2),F(1)]:
  N=c*ar(bi)-(1+ar(ai)).log();ps=arb(0) if N<0 else N/2
  for xi in [F(1,4),F(1,2),F(1)]:
   xv=ar(xi);yv=xv/(1+ar(ai));qv=(xv+(1-ar(ai))*yv)/2
   phi=xv*c*ar(bi)/2+qv*qv.log()-xv*xv.log()/2-(1-ar(ai))*yv*yv.log()/2
   ck('entropy_max_equality_'+str((ai,bi,xi)),(phi-xv*N/2).contains(0))
   for yj in [F(1,10),F(1,3),F(9,10)]:
    y=ar(yj);q=(xv+(1-ar(ai))*y)/2;ph=xv*c*ar(bi)/2+q*q.log()-xv*xv.log()/2-(1-ar(ai))*y*y.log()/2
    ck('entropy_perturbation_'+str((ai,bi,xi,yj)),ph<phi or (ph-phi).contains(0))
# Global bound grids are controls only, not universal proof.
for ai in range(11):
 for bi in range(ai+1,11):
  aa=ar(F(ai,10));bb=ar(F(bi,10));vv=(bb-aa)**2/((aa+bb)*(2-aa-bb));ww=(1+vv/2).log();N=c*bb-(1+aa).log()
  ck('finite_bound_'+str((ai,bi)),N/2<ar(F(5,2))*ww)
ctrl('B_not_equal_J',not (psi-w).contains(0))
ctrl('H_not_equal_J',not (psi-h).contains(0))
for bv in [F(1,2),F(3,4)]:
 rv=ar(F(9,10));bb=ar(bv);av=(1-rv)**2/(2*(1+rv));bv0=1+rv
 wp=2*av/((2-bv0*bb)*(2-(bv0-av)*bb));np=c-rv/(1+rv*bb)
 ctrl('sharp_derivative_shortcut_fails_'+str(bv),np>2*lower*wp)
 if bv==F(3,4):ck('derivative_failure_positive_score',c*bb-(1+rv*bb).log()>0)
ck('exact_derivative_counter_bound',F(400,16779)<F(166,2349))
consumers=[]
for nu in [F(2,5),F(9,20)]:
 ep=ar(F(1,20));budget=ar(F(1,1000));e=ar(F(2499,500000));beta=ar(F(1,100000000));D=ar(nu)*e*e-beta
 nnew=((1/ep).log()+ar(F(5,2))*budget/ep)/(c*D);nold=((1/ep).log()+2*C*budget/ep)/(c*D)
 n=int(nnew.upper().ceil().unique_fmpz());o=int(nold.upper().ceil().unique_fmpz())
 ck('use_count_'+str(nu),n>=nnew and n-1<nnew and n<o)
 ck('positive_actual_success_'+str(nu),ar(F(1,4))-(2*((((1/ep).log()+ar(F(5,2))*budget/ep)/(c*n)+beta)/ar(nu)).sqrt()+ar(F(1,1000000)))>0)
 consumers.append({'gap':str(nu),'expected_original_budget':'1/1000','confidence':'1/20','new_uses':n,'prior_uses':o})
note='explorations/conditional-build/k2468-stopped-original-budget-2026-11-01.md';deps=[note,str(Path(__file__).relative_to(ROOT)),'lab/process/k2465-sharp-leakage-compensator.json']
prior=json.loads((ROOT/deps[-1]).read_text())
ck('prior_authentication',all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in prior['dependencies'].items()))
report={'result_id':'K2468','checks':checks,'controls':controls,'coefficient_lower':str(lower),'coefficient_upper':'5/2','contrary_law':{'a':str(a0),'b':str(b0),'confidence':str(eps),'hit_probability':str(p),'hit_score':str(hit),'false_coefficient2_threshold':str(bad_threshold)},'prospective_consumers':consumers,'bernstein_coefficients':[str(z) for z in bern],'evidence_kinds':{'universal':'entropy potential and first-use/failure scalar reduction; polynomial positivity and endpoint limit','finite':'exact absorption recurrences; symbolic identities; Arb256 counterlaw and consumers','ceiling':'uniform-confidence coefficient bracket, not exact scalar supremum or measured budget'},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2468-stopped-original-budget.json'
if '--check' in sys.argv:assert json.loads(out.read_text())==report
else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('K2468',len(checks),'checks',len(controls),'controls PASS')
