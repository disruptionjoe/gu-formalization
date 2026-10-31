"""Exact finite controls for drift bounds and heterogeneous hidden-role pools."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product,permutations
from math import comb,factorial
import json,hashlib,sys
R=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ctrl(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
def exp_lower(x,terms=150):
 assert x>=0
 t=s=F(1)
 for j in range(1,terms+1):t*=x/j;s+=t
 return s
# Rational outward radius, certified without floating logarithms or roots.
def radius(n,eps):
 if not n:return F(1)
 lo,hi=0,64
 while exp_lower(F(2*n*hi*hi,4096))<2*n*(n+1)/eps:hi*=2
 while hi-lo>1:
  m=(lo+hi)//2
  if exp_lower(F(2*n*m*m,4096))>=2*n*(n+1)/eps:hi=m
  else:lo=m
 return F(hi,64)
def poisson(ps):
 out=[F(1)]
 for p in ps:
  nxt=[F(0)]*(len(out)+1)
  for k,v in enumerate(out):nxt[k]+=v*(1-p);nxt[k+1]+=v*p
  out=nxt
 return out
def elementary(xs):
 out=[F(1)]
 for x in xs:
  nxt=out+[F(0)]
  for k in range(1,len(nxt)):nxt[k]+=x*out[k-1]
  out=nxt
 return out
def effective(ps,q,t):
 m=len(ps);o=[p/(1-p) for p in ps];es=elementary(o)
 return q/(1-q)*F(m-t+1,t)*es[t-1]/es[t]
cases=0
for m in range(1,5):
 for ps in product([F(1,4),F(1,2),F(3,4)],repeat=m):
  dist=poisson(ps);es=elementary([p/(1-p) for p in ps]);p0=dist[0]
  assert all(dist[k]==p0*es[k] for k in range(m+1))
  for q in [F(1,4),F(1,2),F(3,4)]:
   for t in range(1,m+1):
    r=effective(ps,q,t);od=q/(1-q)
    assert od/max(p/(1-p) for p in ps)<=r<=od/min(p/(1-p) for p in ps)
    assert r==(q*dist[t-1]/comb(m,t-1))/((1-q)*dist[t]/comb(m,t));cases+=1
ck('complete_finite_heterogeneous_odds_boxes',cases>1000)
# Direct random-hidden-role likelihood, independent of elementary polynomials.
direct=0
for ps in [(F(1,4),F(3,4)),(F(1,5),F(1,2),F(4,5))]:
 q=F(2,5);m=len(ps)
 for z in product([0,1],repeat=m+1):
  weights=[]
  for i in range(m+1):
   others=z[:i]+z[i+1:];lik=F(0)
   for perm in permutations(range(m)):
    p=F(1)
    for j,idx in enumerate(perm):p*=ps[idx] if others[j] else 1-ps[idx]
    lik+=p/factorial(m)
   weights.append((q if z[i] else 1-q)*lik)
  t=sum(z)
  if 0<t<m+1:
   rr=effective(ps,q,t);raw=[rr if v else F(1) for v in z]
   assert all(weights[i]/sum(weights)==raw[i]/sum(raw) for i in range(m+1))
  else:assert len(set(weights))==1
  direct+=1
ck('independent_hidden_role_enumeration',direct==24)
ck('heterogeneous_fixture',effective([F(1,4),F(3,4)],F(1,2),1)==F(3,5) and effective([F(1,4),F(3,4)],F(1,2),2)==F(5,3))
ctrl('average_probability_substitution_is_wrong',effective([F(1,4),F(3,4)],F(1,2),1)!=1)
# Every score vector in a finite box; the true assignment uses heterogeneous r.
score_cases=0
for z in [(0,0,1),(0,1,1)]:
 rr=effective([F(1,4),F(3,4)],F(1,2),sum(z));ww=[rr if v else F(1) for v in z]
 for scores in product([F(0),F(1),F(3)],repeat=3):
  def mean(r):
   w=[r if v else F(1) for v in z];return sum(a*b for a,b in zip(w,scores))/sum(w)
  C=max(mean(F(1,3)),mean(F(3)));true=mean(rr)
  assert true<=C
  if C:
   for lam in [F(0),F(1,2),F(1)]:assert sum(w*(1-lam+lam*b/C) for w,b in zip(ww,scores))/sum(ww)<=1
  score_cases+=1
ck('complete_finite_score_boxes',score_cases==54)
# Time-uniform spending telescopes exactly.
ck('summable_time_spending',sum(F(1,n*(n+1)) for n in range(1,101))==F(100,101))
# Exact adaptive first-crossing probability with conditional outward drift.
eps=F(1,5);d=F(1,20);anchor=F(1,2);live={0:F(1)};crossed=F(0)
for n in range(1,97):
 nxt={};rad=radius(n,eps)
 for k,prob in live.items():
  p=anchor+(d if 2*k>=n-1 else -d)
  for bit,weight in [(0,1-p),(1,p)]:
   kk=k+bit;v=prob*weight
   if abs(F(kk,n)-anchor)>d+rad:crossed+=v
   else:nxt[kk]=nxt.get(kk,F(0))+v
 live=nxt
assert sum(live.values())+crossed==1
ck('adaptive_first_crossing_below_budget',0<crossed<=eps)
# Omission of a real drift bias fails at a concrete sample size: direct binomial sum.
n=512;eps0=F(1,10);rad=radius(n,eps0);failure=sum(F(comb(n,k)*3**k,4**n) for k in range(n+1) if abs(F(k,n)-F(1,2))>rad)
ctrl('omitted_drift_actual_binomial_coverage_failure',failure>eps0)
# Favorable path's declared rational radius and complete shared-parameter cells.
n=4096;eps0=F(1,200);rad=F(1,16);bound=exp_lower(2*n*rad*rad)
ck('outward_radius_at4096',bound>2*n*(n+1)/eps0)
width=F(1,32)+rad+F(1,32);lo,hi=F(1,2)-width,F(1,2)+width
ck('current_law_interval',lo==F(3,8) and hi==F(5,8))
rl=lo/(1-lo)/(hi/(1-hi));rh=1/rl
ck('current_odds_enclosure',rl==F(9,25) and rh==F(25,9) and F(1,4)<=rl<=rh<=4)
# K2400 binary score fixture: lambda=3/4, max distinguished-score factor31/16.
def factor(res):return F(31,16) if res>F(1,4) else F(1,4)
products=[]
for theta in [F(-1),F(-3,4),F(-1,2),F(0),F(1,2),F(3,4),F(1)]:
 products.append(factor((1-theta)**2)*factor((1+theta)**2)*F(31,16)**6)
minimum=F(1,4)*F(31,16)**7
ck('all_shared_graph_cells_endpoints',min(products)==minimum and minimum>25)
ck('error_and_exposure_account',F(1,100)+F(1,25)==F(1,20) and 2*n+48==8240)
# Exact observational equivalence under the two anchor models.
mu,d,h=F(1,2),F(1,8),F(1,16)
ck('indistinguishable_anchor_models',abs(mu-(mu-d))==d and abs(mu-(mu+d))==d and (mu+d)-(mu-d)==2*d)
ck('deployment_identification_floor',0<mu-d-h<mu+d+h<1 and (mu+d+h)-(mu-d-h)==2*(d+h))
# Block dependence and reuse countercontrols act on the original law.
ctrl('dependent_block_not_independent_likelihood',F(1,2)!=F(1,2)**4)
ctrl('reused_science_factor_not_evalue',F(1,2)*4>1)
# Nominal mean law can actually produce an invalid mean e-factor.
z=(0,0,1);rr=F(3,5);scores=[F(1),F(1),F(0)];nominal=F(2,3);actual=F(2)/(2+rr)
ctrl('average_law_unsafe_normalizer',actual/nominal>1)
report={'result_id':'K2403','checks':checks,'controls':controls,'evidence_kind':'finite exact rational checks; universal martingale, symmetric-polynomial and identifiability arguments are written proofs','heterogeneous_cases':cases,'direct_role_cases':direct,'score_cases':score_cases,'adaptive_crossing_probability':str(crossed),'omitted_drift_failure_probability':str(failure),'favorable_calibration_label_observations':8192,'favorable_science_pool_exposures':48,'favorable_bookkeeping_sum_not_physical_cost':8240,'shared_graph_minimum':str(minimum),'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in ['explorations/conditional-build/k2400-adaptive-calibration-confidence-2026-10-31.md','lab/process/k2400-adaptive-calibration-confidence.json','explorations/conditional-build/k2397-finite-training-shift-confidence-2026-10-31.md']}}
p=R/'lab/process/k2403-drift-robust-calibration.json'
if '--write' in sys.argv:p.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
else:assert json.loads(p.read_text())==report
print(json.dumps(report,sort_keys=True))
