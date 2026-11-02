"""Universal proof is in the paired note; finite controls and dependency authentication here."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,sys
ROOT=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ctrl(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
def authenticate(p):
 data=json.loads((ROOT/p).read_text())
 return all(hashlib.sha256((ROOT/q).read_bytes()).hexdigest()==h for q,h in data['dependencies'].items())
def finish(st,evidence,deps,extra=None):
 deps=[f'explorations/conditional-build/{st}-2026-11-01.md',str(Path(__file__).relative_to(ROOT)),*deps]
 report={'result_id':st.split('-')[0].upper(),'checks':checks,'controls':controls,'evidence_kinds':evidence,'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},**(extra or {})}
 out=ROOT/f'lab/process/{st}.json'
 if '--check' in sys.argv:assert json.loads(out.read_text())==report
 else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
 print(st,len(checks),'check groups',len(controls),'contrary controls PASS')

from flint import arb,ctx
import sympy as sp
ctx.prec=256
def ar(x):
 x=F(x);return arb(x.numerator)/x.denominator
c=arb(2).log();C=(1+c)**2/(4*(1-c));r=F(117,250)
# Stage recursion derives the budget independently of the closed finite-N expression.
for a,b in [(F(1,10),F(1,4)),(F(1,3),F(2,3)),(F(1,100),F(1,50))]:
 s=1/(1+a);ep=F(0);p=F(1)
 for N in range(1,9):
  ep+=p*2/(1+a);p*=s
  ck('stage_law_'+str((a,b,N)),p==(1+a)**(-N) and ep==2/a*(1-p))
# Exact strict dyadic selection. No float floor/log endpoint ambiguity.
def prelude(eps):
 m=0;rho=F(1)
 while rho/2>eps:m+=1;rho/=2
 return m,rho,eps/rho
for eps in [F(1,2),F(1,4),F(1,8),F(1,20),F(1,100),F(9,10)]:
 m,rho,eta=prelude(eps)
 ck('strict_prelude_'+str(eps),rho>eps and rho/2<=eps and F(1,2)<=eta<1)
 if eps.denominator&(eps.denominator-1)==0 and eps.numerator==1:ck('dyadic_endpoint_'+str(eps),eta==F(1,2))
ctrl('rho_equal_epsilon_cannot_exceed',not (F(1,4)*F(1)>F(1,4)))
rr,cc=sp.symbols('r c',real=True);R0=2*(cc-rr)*(1+rr)/(1-rr)**2;rs=(3*cc-1)/(3-cc)
ck('inherited_endpoint_algebra',sp.cancel(R0.subs(rr,rs)-(1+cc)**2/(4*(1-cc)))==0)
eta=sp.symbols('eta',positive=True);f=eta*sp.log(1/eta)/(1-eta)
ck('staircase_monotonic_derivative',sp.simplify(sp.diff(f,eta)-(-sp.log(eta)-1+eta)/(1-eta)**2)==0)
# Actual finite laws violating coefficients below the new bound. Exact pN is rational;
# a=pN^(-1/N)-1 is specified algebraically and enclosed by Arb256.
witnesses=[]
for eps in [F(1,2),F(1,4),F(1,20),F(1,100),F(9,10)]:
 m,rho,eta=prelude(eps);N=100000;pN=eta+(1-eta)/F(N+1)
 a=(-(ar(pN).log())/N).exp()-1;b=a/ar(r)
 w=(1+(b-a)**2/(2*(a+b)*(2-a-b))).log()
 K=ar(rho)*2*w/a*(1-ar(pN));z=m*c+N*c*b
 lower=C*ar(eta)*(1/ar(eta)).log()/(1-ar(eta));lam=lower*ar(F(99,100))
 ck('finite_law_domain_'+str(eps),a>0 and b>a and b<1 and rho*pN>eps and K>0)
 ctrl('finite_staircase_counterexample_'+str(eps),z>(1/ar(eps)).log()+lam*K/ar(eps))
 ck('uniform_upper_covers_same_law_'+str(eps),z<(1/ar(eps)).log()+C*K/ar(eps))
 witnesses.append({'epsilon':str(eps),'prelude':m,'N':N,'p_chain':str(pN),'r':str(r),'lower_bound':str(lower),'violated_coefficient':str(lam),'score':str(z),'expected_budget':str(K)})
# Activation entropy deficit: exact symbol identity, interval actual-law example.
alpha,s=sp.symbols('alpha s',positive=True);pp=alpha*s
ck('activation_entropy_deficit',sp.simplify(sp.expand_log(pp*sp.log(s)-pp*sp.log(pp),force=True)+pp*sp.log(alpha))==0)
aa=ar(F(1,10000));bb=2*aa;al=ar(F(1,20));p=al/(1+aa)
ww=(1+(bb-aa)**2/(2*(aa+bb)*(2-aa-bb))).log();K=2*p*ww
ctrl('activation_does_not_create_score',c*bb<(1/ar(F(1,20))).log())
ck('initial_entropy_is_lost',-p*al.log()>0)
ctrl('artificial_offset_changes_score',c*bb-al.log()>c*bb)
# Exact equality at epsilon1/2, lambda0 matters: b1,a0 gives p1 and score c.
a0=F(0);b0=F(1);eps0=F(1,2);hit0=1/(1+a0);score_in_log2_units=b0;threshold_in_log2_units=F(1)
ctrl('inclusive_threshold_endpoint',hit0>eps0 and score_in_log2_units>=threshold_in_log2_units and not score_in_log2_units>threshold_in_log2_units)
for eps in [F(3,5),F(3,4),F(9,10)]:
 h=(1/ar(eps)).log();A=1/ar(eps)-1
 ck('activated_region_separated_'+str(eps),h/c>A)
deps=['lab/process/k2468-stopped-original-budget.json','lab/process/k2471-sharp-stopping-coefficient.json']
for pth in deps:ck('authenticated_'+Path(pth).stem,authenticate(pth))
finish('k2474-fixed-confidence-stopping',{'universal':'finite stopped-law derivation, dyadic prelude limit, monotonicity, initial entropy and compactness','finite':'exact rational stage-length coefficients and dyadic endpoints, Arb256 genuine finite-law violations','reused':'K2471 uniform coefficient and original law premises','ceiling':'lower bounds only; exact fixed-confidence optimum remains open'},deps,{'finite_counterexamples':witnesses})
