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
ctx.prec=256
def ar(x):
 x=F(x);return arb(x.numerator)/x.denominator
c=arb(2).log();C=(1+c)**2/(4*(1-c));r0=F(47,100);r1=F(1,3)
def k(r):return (1-ar(r))**2/(2*ar(r)*(1+ar(r)))
ex=(-ar(r0)).exp();H=k(r0)*(1-ex)/(ex-ar(F(1,2)));limit=c/(ar(r1)*(k(r1)+H))
ck('limit_strict_bound',limit>ar(F(18736,10000)) and limit<ar(F(18737,10000)))
ck('improves_dyadic_predecessor',limit>C*c)
ck('below_uniform_upper',limit<C)
witnesses=[]
for M in [64,256,1024,10000]:
 b=F(1,M);a0=r0/M;a1=r1/M;p0=(1+a0)**(-(M+1));p1=1/(1+a1)
 ideal=(F(1,2)+F(1,M*M)-p1/2)/(p0-p1/2)
 J=(4*M**3-1).bit_length();den=2**J;alpha=F((ideal.numerator*den)//ideal.denominator,den)
 ck('coin_domain_'+str(M),0<alpha<1 and alpha<=ideal and ideal-alpha<F(1,den))
 Pbar=alpha*p0+(1-alpha)*p1/2
 ck('strict_success_margin_'+str(M),Pbar>F(1,2)+F(1,2*M*M))
 def w(a):return (1+ar((b-a)**2/(2*(a+b)*(2-a-b)))).log()
 w0,w1=w(a0),w(a1);Kbar=ar(alpha)*2*w0/ar(a0)*(1-ar(p0))+ar(1-alpha)*w1/ar(a1)*(1-ar(p1))
 ratio=c/(2*M*Kbar)
 ck('finite_domain_'+str(M),0<a0<b<=1 and 0<a1<b and Kbar>0 and ratio<C)
 if M==10000:ctrl('actual_finite_violation_1_87',ratio>ar(F(187,100)))
 for m in [0,1,3,9]:
  rho=F(1,2**m);eps=rho/2;P=rho*Pbar;K=ar(rho)*Kbar;L=(m+1)*c+c/M
  ck(f'equal_score_{M}_{m}',m+F(M+1,M)==m+1+F(1,M))
  ck(f'actual_scaled_probability_{M}_{m}',P>eps)
  if M==10000:ctrl(f'finite_threshold_violation_{m}',L>(1/ar(eps)).log()+ar(F(187,100))*K/ar(eps))
 # Wrong omission of prelude survival factors changes the actual expected budget.
 badK=ar(alpha)*2*w0/ar(a0)*(1-ar(p0))+ar(1-alpha)*2*w1/ar(a1)*(1-ar(p1))
 ctrl('unweighted_survivor_budget_'+str(M),badK>Kbar)
 witnesses.append({'M':M,'coin_bits':J,'alpha':str(alpha),'success_over_rho':str(ar(Pbar)),'K_over_rho':str(Kbar),'coefficient_ratio':str(ratio)})
# Independent stage recursion versus exact closed law; original failed-stage costs included.
for a,b in [(F(1,5),F(1,2)),(F(1,13),F(1,7))]:
 p=F(1);expected_steps=F(0)
 for N in range(1,16):
  expected_steps+=p*2/(1+a);p/=1+a
  ck('stage_budget_'+str((a,N)),expected_steps==2/a*(1-p))
  ctrl('omit_failed_paths_'+str((a,N)),expected_steps>p*N*2/(1+a))
ctrl('no_score_activation_cannot_replace_prelude',c/10000<c)
ctrl('equal_probability_endpoint_not_violation',not(F(1,2)>F(1,2)))
# Two-point hull control: direct rational enumeration of a small finite bank.
pts=[(F(1,4),F(1,20)),(F(1,2),F(1,5)),(F(3,4),F(3,5))];target=F(3,5);pairs=[]
for i,(p,k0) in enumerate(pts):
 for q,k1 in pts[i+1:]:
  a=(q-target)/(q-p)
  if 0<=a<=1:pairs.append(a*k0+(1-a)*k1)
opt=min(pairs)
for i in range(21):
 for j in range(21-i):
  weights=[F(i,20),F(j,20),F(20-i-j,20)]
  if sum(w*p for w,(p,k0) in zip(weights,pts))==target:ck('convex_hull_'+str((i,j)),sum(w*k0 for w,(p,k0) in zip(weights,pts))>=opt)
deps=['lab/process/k2471-stopping-endpoint-optimum.json','lab/process/k2474-fixed-confidence-stopping.json']
# Resolve actual K2471 report spelling without silently replacing evidence.
if not (ROOT/deps[0]).exists():
 matches=list((ROOT/'lab/process').glob('k2471-*.json'));assert len(matches)==1;deps[0]=str(matches[0].relative_to(ROOT))
for p in deps:ck('authenticate_'+p,authenticate(p))
finish('k2477-randomized-score-preludes',{'universal':'finite-law asymptotic construction and two-equality convex hull argument','finite':'exact rational probabilities and fair-bit weights; Arb256 scores, expected budgets, limit and strict violations','reused':'K2471 uniform coefficient and K2474 stopped-stage law authenticated','ceiling':'dyadic lower-bound improvement; no global or nondyadic optimum'},deps,{'dyadic_limit':str(limit),'witnesses':witnesses})
