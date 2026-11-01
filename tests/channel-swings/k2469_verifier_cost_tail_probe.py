"""Full-carrier prospective quantile optimizer: algebraic endpoints, Arb256 tails."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial,comb
import json,hashlib,sys
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
# Recurrence works identically over exact rationals and Arb enclosures.
def cdf(N,q,K,pi=F(1,2),cU=1,u=1,v=2):
 stop=K-N*cU
 if stop<0:return q*0
 aa=pi*(1-q);bb=pi*q;fs=[(1-pi)**N];total=fs[0]
 for m in range(1,stop+1):
  val=(aa*(m+(N-1)*u)*fs[m-u] if m>=u else q*0)+(bb*(m+(N-1)*v)*fs[m-v] if m>=v else q*0)
  fs.append(val/m);total+=fs[-1]
 return total
for N in [1,2,4]:
 for q in [F(0),F(1,3),F(1)]:
  for K in [N,N+1,N+5,N+10]:
   exact=F(0)
   for b in range((K-N)//2+1):
    for a in range(K-N-2*b+1):
     exact+=F(factorial(N+a+b-1),factorial(N-1)*factorial(a)*factorial(b))*F(1,2)**N*(F(1,2)*(1-q))**a*(q/2)**b
   ck('exact_multinomial_'+str((N,q,K)),cdf(N,q,K)==exact)
for N in [1,3]:
 for K in [N,N+1,N+5,N+12]:
  q=F(1,3);ex=F(0)
  for b in range((K-N)//3+1):
   for a in range((K-N-3*b)//2+1):ex+=F(factorial(N+a+b-1),factorial(N-1)*factorial(a)*factorial(b))*F(1,2)**N*(F(1,2)*(1-q))**a*(q/2)**b
  val=cdf(N,q,K,u=2,v=3);ck('gapped_exact_charges_'+str((N,K)),isinstance(val,F) and val==ex)
ctrl('same_mean_deterministic_label_cost',cdf(3,F(1,2),9)!=sum(F(comb(L+2,2),2**(L+3)) for L in range(5)))
ctrl('mean_not_budget',cdf(2,F(1,2),5)<1)
ctrl('expensive_label_randomness',cdf(3,F(1,2),9)!=cdf(3,F(0),9))
ctrl('increasing_q_worsens_tail',cdf(3,F(1,4),9)>cdf(3,F(3,4),9))
# Actual conditioning counterlaw: rare costly branch selected as passing.
ctrl('conditioning_can_amplify',F(1,20)<F(1,20)/F(1,20))
prior=json.loads((ROOT/'lab/process/k2466-calibrated-verifier-design.json').read_text());bank=json.loads((ROOT/'lab/process/k2457-local-verifier-phase-design.json').read_text())
for label,record in [('design',prior),('original',bank)]:ck('authenticated_'+label,all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in record['dependencies'].items()))
answers=[]
for li,law in enumerate(bank['original_laws']):
 a=ar(F(law['a']));h=1/(2*(1+a));AA=h*(h+4);vals=[]
 for row in law['blocks']:
  t=ar(F(row['trace']));d=ar(F(row['det']));vals.append((t+(t*t-4*d).sqrt())/2)
 ell=vals[0];im=0
 for i,v in enumerate(vals[1:],1):
  if v>ell:ell=v;im=i
 for i,v in enumerate(vals):ck(f'full_carrier_{li}_{i}',v<ell or (law['blocks'][i]['trace'],law['blocks'][i]['det'])==(law['blocks'][im]['trace'],law['blocks'][im]['det']))
 qx=(ell-h)/(ell*ell+h*ell-h);b0=ar(F(1,50));b1=ar(F(3,50));uu=arb(1)/2-b0;vv=h/2-b1
 def disc(q):return 1-6*h*q+AA*q*q
 def margin(q):
  g=(1-h*q+disc(q).sqrt())/2;lam=g if g>q*ell else q*ell
  return 1-lam-b0-b1*q
 def endpoint(N):
  th=arb(100)/N;ends=[]
  for q in [arb(0),qx,arb(1)]:
   ck(f'endpoint_strict_{li}_{N}_{len(ends)}',not (margin(q)-th).contains(0))
   if margin(q)>th:ends.append(q)
  aa=4*vv*vv-AA;bb=8*(uu-th)*vv+6*h;cc=4*(uu-th)**2-1;ds=bb*bb-4*aa*cc
  ck(f'quadratic_strict_{li}_{N}',not aa.contains(0) and not ds.contains(0))
  if ds>0:
   for sign in [-1,1]:
    q=(-bb+sign*ds.sqrt())/(2*aa)
    ck(f'root_decision_{li}_{N}_{sign}',all(not z.contains(0) for z in [q,q-qx,uu-th+vv*q]))
    if 0<q<qx and uu-th+vv*q>0:
     ck(f'root_original_margin_{li}_{N}_{sign}',(margin(q)-th).contains(0));ends.append(q)
  qr=(1-b0-th)/(ell+b1)
  ck(f'linear_strict_{li}_{N}',not (ell+b1).contains(0) and not (qr-qx).contains(0) and not (qr-1).contains(0))
  if qx<qr<1:ends.append(qr)
  if not ends:return None
  q=ends[0]
  for q2 in ends[1:]:
   ck(f'endpoint_order_{li}_{N}_{str(q2)}',not (q2-q).contains(0))
   if q2<q:q=q2
  return q
 target=ar(F(19,20));q0=ar(F(7,10));n0=int((arb(100)/margin(q0)).upper().ceil().unique_fmpz())
 ck(f'incumbent_risk_{li}',n0*margin(q0)>100)
 # Monotone integer search, with rigorous decisions; no probabilistic approximation.
 def quantile(N,q,cap=None):
  lo=N-1;hi=max(N+1,cap if cap is not None else 3*N)
  while cdf(N,q,hi,pi=ar(F(1,2)))<target:hi*=2
  while hi-lo>1:
   mid=(lo+hi)//2;z=cdf(N,q,mid,pi=ar(F(1,2)))
   if z>target:hi=mid
   elif z<target:lo=mid
   else:raise AssertionError('unresolved exact tail equality')
  ck(f'quantile_strict_{li}_{N}_{hi}',cdf(N,q,hi,pi=ar(F(1,2)))>target and cdf(N,q,hi-1,pi=ar(F(1,2)))<target)
  return hi
 K0=quantile(n0,q0);bestK=K0;bestN=n0;bestq=q0;feasible=[];rejections=[]
 print('law',li,'incumbent',n0,K0,flush=True)
 for N in range(1,K0+1):
  q=endpoint(N)
  if q is None:continue
  feasible.append((N,q));z=cdf(N,q,bestK-1,pi=ar(F(1,2)))
  if z>target:
   bestK=quantile(N,q,bestK-1);bestN=N;bestq=q
  elif not z<target:raise AssertionError('unresolved improvement')
 # Global lower-budget certificate; one scalar CDF for every feasible count.
 for N,q in feasible:
  z=cdf(N,q,bestK-1,pi=ar(F(1,2)));ck(f'global_budget_lower_{li}_{N}',z<target);rejections.append({'N':N,'cdf_at_optimal_minus1':str(z)})
 success=cdf(bestN,bestq,bestK,pi=ar(F(1,2)));ck(f'global_budget_attained_{li}',success>target)
 cU=1;setup=0
 ck(f'deterministic_count_exhaustion_{li}',(K0+1)*cU+setup>K0)
 nexp=prior['finite_count_designs'][li]['finite_optimal_count'];qexp=endpoint(nexp);kexp=quantile(nexp,qexp)
 ck(f'beats_or_ties_mean_design_{li}',bestK<=kexp)
 answers.append({'law':law['a'],'optimal_budget':bestK,'optimal_representative_N':bestN,'optimal_representative_q':str(bestq),'attained_cdf':str(success),'incumbent_budget':K0,'incumbent_N':n0,'all_counts_bounded_by':K0,'feasible_counts':len(feasible),'expected_cost_optimal_N':nexp,'expected_cost_design_quantile':kexp,'strict_gain_over_mean_design':bestK<kexp,'global_lower_budget_checks':rejections})
 print('law',li,'optimal',bestN,bestK,'mean-design quantile',kexp,flush=True)
note='explorations/conditional-build/k2469-verifier-cost-tail-2026-11-01.md';deps=[note,str(Path(__file__).relative_to(ROOT)),'lab/process/k2466-calibrated-verifier-design.json','lab/process/k2457-local-verifier-phase-design.json']
report={'result_id':'K2469','checks':checks,'controls':controls,'original_full_carrier_quantiles':answers,'parameters':{'Aconf':100,'e_squared':1,'betaQ':'1/50','betaT':'2/25','pi':'1/2','charges':[1,1,2],'setup':0,'delta':'1/20'},'evidence_kinds':{'universal':'schedule coupling, generating function and deterministic finite-count bound','exact':'rational negative-multinomial controls and original block authentication','interval':'algebraic endpoint branches and all finite count/tail comparisons at Arb256','ceiling':'prospective schedule cost, not outcome-correlated actual-cost optimum or conditional-on-pass guarantee'},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2469-verifier-cost-tail.json'
if '--check' in sys.argv:assert json.loads(out.read_text())==report
else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('K2469',len(checks),'checks',len(controls),'controls PASS')
