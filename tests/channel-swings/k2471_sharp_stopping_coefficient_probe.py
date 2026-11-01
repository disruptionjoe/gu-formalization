"""Exact identities for the universal sharp stopping proof; Arb consumers separate."""
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
def ar(v):
 v=F(v);return arb(v.numerator)/v.denominator
a,d,c,r=sp.symbols('a d c r',real=True);k=1-c;t=sp.Rational(2,3);h=3*c-1;z=1-c/3
C=(1+c)**2/(4*k);den=(2*a+d)*(2-2*a-d);v=d*d/den
L=c*a+3*k*a*(1-a)/(3+2*a);Q=21-30*c+(28-40*c)*a+(6-10*c)*a*a
ck('log_derivative_identity',sp.cancel(1/(1+a)-sp.diff(L,a)-a*Q/((1+a)*(3+2*a)**2))==0)
ck('log_bound_endpoints',L.subs(a,0)==0 and sp.simplify(L.subs(a,1)-c)==0)
A=sp.Rational(8,3)*(1+c-3*c*c);B=(-18+84*c-82*c*c)/9
Nb=c*d-k*a*(1-a)/(1+t*a)
square=(4*k*a*(1-a)-(h+2*z*a)*d)**2
poly=square+a*d*d*(A+B*a)+2*k*c*(1+t*a)*d**3
ck('whole_triangle_square_identity',sp.cancel(2*k*(1+t*a)*den*(2*C*v-Nb*(2+v))-poly)==0)
lo=sp.Rational(56,81);hi=sp.Rational(25,36)
ck('Q_zero_positive',Q.subs({a:0,c:hi})==sp.Rational(1,6))
ck('Q_one_negative',Q.subs({a:1,c:lo})==-sp.Rational(25,81))
ck('Q_leading_negative',(6-10*c).subs(c,lo)==-sp.Rational(74,81))
ck('A_lower',A.subs(c,hi)==sp.Rational(107,162))
ck('B_lower',B.subs(c,hi)==sp.Rational(511,5832))
ck('A_B_decrease',sp.diff(A,c).subs(c,lo)<0 and sp.diff(B,c).subs(c,lo)<0 and sp.diff(A,c,2)<0 and sp.diff(B,c,2)<0)
R0=2*(c-r)*(1+r)/(1-r)**2;rs=(3*c-1)/(3-c)
ck('unique_stationary_endpoint',sp.factor(sp.diff(R0,r))==sp.factor(2*((3*c-1)+(c-3)*r)/(1-r)**3))
ck('exact_endpoint_constant',sp.cancel(R0.subs(r,rs)-C)==0)
ctrl('omitted_mixed_square_term',sp.cancel(2*k*(1+t*a)*den*(2*C*v-Nb*(2+v))-(16*k*k*a*a*(1-a)**2+(h+2*z*a)**2*d*d+a*d*d*(A+B*a)+2*k*c*(1+t*a)*d**3))!=0)
cv=arb(2).log();CC=(1+cv)**2/(4*(1-cv));rv=(3*cv-1)/(3-cv)
ck('log_rational_bounds',ar(F(56,81))<cv<ar(F(25,36)))
ck('constant_enclosure',ar(F(2335604558,10**9))<CC<ar(F(2335604559,10**9)))
# Finite controls only; global proof is the signed polynomial identity.
for av,bv in [(F(0),F(1)),(F(1,2),F(1)),(F(9,10),F(99,100)),(F(1,100),F(1,50))]:
 aa=ar(av);bb=ar(bv);vv=(bb-aa)**2/((aa+bb)*(2-aa-bb));ww=(1+vv/2).log();N=cv*bb-(1+aa).log()
 ck('finite_strict_bound_'+str((av,bv)),N<2*CC*ww)
# An actual binary law defeats a concrete smaller coefficient, near the extremal endpoint.
bs=ar(F(1,10**7));aa=rv*bs;ww=(1+(bs-aa)**2/(2*(aa+bs)*(2-aa-bs))).log();ph=1/(1+aa);eps=ph-ar(F(1,10**12));lam=ar(F(2335,1000));budget=2*ph*ww
ctrl('actual_binary_smaller_coefficient_fails',cv*bs>(1/eps).log()+lam*budget/eps and ph>eps)
ck('sharp_constant_covers_same_law',cv*bs<(1/eps).log()+CC*budget/eps)
# Existing failed derivative shortcut remains false despite true global inequality.
bb=ar(F(3,4));rr=ar(F(9,10));aa0=(1-rr)**2/(2*(1+rr));wp=2*aa0/((2-(1+rr)*bb)*(2-(1+rr-aa0)*bb));np=cv-rr/(1+rr*bb)
ctrl('pointwise_derivative_method_still_false',np>2*CC*wp)
consumers=[]
for nu in [F(2,5),F(9,20)]:
 ep=ar(F(1,20));budget=ar(F(1,1000));ee=ar(F(2499,500000));beta=ar(F(1,100000000));D=ar(nu)*ee*ee-beta
 value=((1/ep).log()+CC*budget/ep)/(cv*D);prior=((1/ep).log()+ar(F(5,2))*budget/ep)/(cv*D)
 n=int(value.upper().ceil().unique_fmpz());oldn=int(prior.upper().ceil().unique_fmpz())
 ck('consumer_ceiling_'+str(nu),n>value and n-1<value and n<oldn)
 ck('positive_actual_success_'+str(nu),ar(F(1,4))-(2*((((1/ep).log()+CC*budget/ep)/(cv*n)+beta)/ar(nu)).sqrt()+ar(F(1,1000000)))>0)
 consumers.append({'gap':str(nu),'uses':n,'prior_uses':oldn})
note='explorations/conditional-build/k2471-sharp-stopping-coefficient-2026-11-01.md';dep='lab/process/k2468-stopped-original-budget.json';data=json.loads((ROOT/dep).read_text())
ck('predecessor_dependencies_authentic',all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in data['dependencies'].items()))
deps=[note,str(Path(__file__).relative_to(ROOT)),dep]
report={'result_id':'K2471','checks':checks,'controls':controls,'sharp_coefficient':str(CC),'sharp_coefficient_exact':'(1+log(2))^2/(4*(1-log(2)))','consumers':consumers,'evidence_kinds':{'universal':'log minorant sign proof, positive-square identity, inherited entropy and limiting actual-law sharpness','finite':'exact symbolic identities and Arb256 controls/consumers','ceiling':'uniform-confidence conditional certificate; not fixed-confidence optimum or inferred budget'},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2471-sharp-stopping-coefficient.json'
if '--check' in sys.argv:assert json.loads(out.read_text())==report
else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('K2471',len(checks),'checks',len(controls),'controls PASS',consumers)
