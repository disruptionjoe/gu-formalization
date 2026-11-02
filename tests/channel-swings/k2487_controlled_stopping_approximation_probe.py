"""Original-law compression/grid checks; continuum proof is in the accompanying note."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,hashlib,sys,math
import sympy as S
from flint import arb,ctx
ctx.prec=256
R=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError('FAIL '+k)
def ctrl(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError('FAIL contrary '+k)
def ar(x):
 x=F(x);return arb(x.numerator)/x.denominator
def c(a,b):
 if a==b:return arb(0)
 return 2*(1+ar((b-a)**2/(2*(a+b)*(2-a-b)))).log()/ar(1+a)
def f(a,b):return F(0) if a+b==0 else (b-a)**2/(2*(a+b))
def law(seq,target=None):
 p=F(1);cost=arb(0);score=F(0)
 for a,b in seq:
  if target is not None and score>=target:break
  cost+=ar(p)*c(a,b);p/=1+a;score+=b
 if target is not None and score<target:p=F(0)
 return p,cost,score
# Symbolic checks of the analytic bridge; inequalities still use the written proof.
a,b,a2,b2=S.symbols('a b a2 b2');u=a+b;d=b-a;x=d*d/(2*u*(2-u))
ck('triangle_identity',S.expand(u*(2-u)-d-(a*(3-a-2*b)+b*(1-b)))==0)
ck('derivative_a',S.factor(S.diff(x,a)+d/(u*(2-u))+d*d*(1-u)/(u*u*(2-u)**2))==0)
ck('derivative_b',S.factor(S.diff(x,b)-d/(u*(2-u))+d*d*(1-u)/(u*u*(2-u)**2))==0)
ff=lambda aa,bb:(bb-aa)**2/(2*(aa+bb))
ck('subadditivity_exact_gap',S.factor(ff(a,b)+ff(a2,b2)-ff(a+a2,b+b2)-2*(a*b2-a2*b)**2/((a+b)*(a2+b2)*(a+b+a2+b2)))==0)
for j in range(1,13):
 for i in range(j+1):
  a,b=F(i,24),F(j,24);cc=c(a,b);ck(f'cost_bound_{i}_{j}',cc<=ar(b));ck(f'small_stage_error_{i}_{j}',abs(cc-ar(f(a,b)))<=ar(b*b))
# Greedy implementation, preserving large stages and total tiny mass.
def compress(seq,delta):
 result=[];aa=F(0);bb=F(0)
 def flush():
  nonlocal aa,bb
  if bb:result.append((aa,bb));aa=bb=F(0)
 for a,b in seq:
  if b>delta:flush();result.append((a,b))
  else:
   aa+=a;bb+=b
   if bb>=delta:flush()
 flush();return result
def round_grid(seq,M):return [(F(math.floor(a*M),M),F(math.ceil(b*M),M)) for a,b in seq]
seq=[(F(1,100),F(1,50))]*9+[(F(1,20),F(1,2))]+[(F(1,200),F(1,40))]*8+[(F(0),F(3,25))]
target=sum(b for a,b in seq);delta=F(1,10);N=math.ceil(2*target/delta)+1;M=37
small=compress(seq,delta);grid=round_grid(small,M);pp,kk,_=law(seq,target);pc,kc,ss=law(small,target);pg,kg,sg=law(grid,target);E=delta*target*(6+target)+F(N*(9+target),M)
ck('compression_score_and_count',ss==target and len(small)<=N and all(0<=a<=b<=1 for a,b in small));ck('compression_probability',pc>=pp);ck('compression_complete_cost',kc<=kk+ar(delta*target*(6+target)))
ck('directed_grid_hits',pg>=pc and sg>=target);ck('grid_complete_cost',kg<=kk+ar(E));ck('rounding_keeps_triangle',all(0<=a<=b<=1 for a,b in grid))
ctrl('merging_not_free',F(7,6)**2>F(15,14)**4 and c(F(0),F(1,2))>2*c(F(0),F(1,4)))
ctrl('downward_rounding_misses',law([(F(0),F(1,4))],F(1,3))[0]==0 and law([(F(0),F(1,2))],F(1,3))[0]==1)
ctrl('deleting_tiny_stages_misses',law([(F(0),F(1,100))]*100,F(1))[0]==1 and law([],F(1))[0]==0)
# Actual unconditional trial cost sums geometric loop reaches; failure-path cost is required.
a,b=F(1,3),F(2,3);w=c(a,b)*ar(1+a)/2;ck('original_geometric_trial_cost',(w/(1-ar((1-a)/2))).overlaps(c(a,b)));ctrl('one_trial_cost_wrong',c(a,b)>w)
ctrl('merged_survival_not_equal',1/(1+F(1,5))>1/(1+F(1,10))**2)
ctrl('ungrouped_count_unbounded',100>N and all(b<delta for a,b in [(F(0),F(1,100))]*100))
# Certified finite Bellman implementation. Overlapping candidates are enclosed, never ordered by midpoints.
def maxball(x,y):
 if x>y:return x
 if y>x:return y
 return x.union(y)
def dp(s,M,N,lam):
 J=math.ceil(s*M);acts=[(F(l,M),F(k,M),k) for k in range(1,M+1) for l in range(k+1)]
 @lru_cache(None)
 def W(n,j):
  if j>=J:return arb(1)
  if n==0:return arb(0)
  z=arb(0)
  for a,b,k in acts:z=maxball(z,(W(n-1,j+k)-ar(lam)*ar(1+a)*c(a,b))/ar(1+a))
  return z
 return W(N,0)
def enumerate_laws(s,M,N):
 acts=[(F(l,M),F(k,M)) for k in range(1,M+1) for l in range(k+1)];out=[]
 def visit(seq,score):
  if score>=s:out.append(law(seq,s)[:2]);return
  if len(seq)==N:return
  for ab in acts:visit(seq+[ab],score+ab[1])
 visit([],F(0));return [(F(0),arb(0))]+out
lib=enumerate_laws(F(1),2,3);D=[]
for lam in [F(0),F(1,3),F(2),F(10)]:
 val=dp(F(1),2,3,lam);ex=arb(0)
 for pp,kk in lib:ex=maxball(ex,ar(pp)-ar(lam)*kk)
 ck('DP_exhaustive_'+str(lam),val.overlaps(ex));ck('DP_narrow_'+str(lam),val.rad()<arb('1e-65'));D.append({'lambda':str(lam),'DP':str(val),'enumerated':str(ex)})
# A failed implementation substitutes one-trial leakage w for complete stage cost c.
wrong=2*(1+ar(F(1,6))).log()/2;ctrl('unconditional_cost_reference_changed',c(F(0),F(1,2))>wrong)
# Explicit tolerance recipe is exact parameter arithmetic, not an enormous numerical solve.
s=F(1);K=F(1,10);tol=F(1,100);delta=min(F(1,4),tol*K/(2*(1-tol)*s*(6+s)));N=math.ceil(2*s/delta)+1;M=math.ceil(2*(1-tol)*N*(9+s)/(tol*K));E=delta*s*(6+s)+F(N*(9+s),M)
ck('tolerance_recipe',E<=tol*K/(1-tol) and E/(K+E)<=tol)
# Abort mixture is exactly budget preserving for any fixed mapped pair at cost K+E.
alpha=K/(K+E);ck('abort_budget_exact',alpha*(K+E)==K);ctrl('unmixed_budget_not_preserved',K+E>K)
deps=['explorations/conditional-build/k2483-adaptive-stopping-bellman-2026-11-01.md','explorations/conditional-build/k2485-constrained-stopping-frontier-2026-11-01.md','lab/process/k2485-constrained-stopping-frontier.json']
report={'result':'K2487','checks':checks,'contrary_controls':controls,'compression_fixture':{'original_stages':len(seq),'compressed_stages':len(small),'probability':[str(x) for x in [law(seq,target)[0],pc,pg]],'costs':[str(x) for x in [law(seq,target)[1],kc,kg]]},'tiny_DP':{'library_size':len(lib),'values':D,'scope':'algorithm comparison only; not a useful continuum bound at this mesh'},'tolerance_parameters':{'s':str(s),'K':str(K),'additive_tolerance':str(tol),'delta':str(delta),'N':N,'M':M,'E':str(E),'guaranteed_error':str(E/(K+E)),'library_evaluated':False},'evidence_kinds':{'universal':'written compression, cost-Lipschitz, directed-rounding and support/mixture proofs','exact':'symbolic identities, rational parameter and contrary-control arithmetic','interval':'Arb256 logarithmic original costs and finite Bellman vs exhaustive comparison','inherited':'K2483/K2485 full-policy reduction authenticated, not reproved by finite tests'},'dependencies':{x:hashlib.sha256((R/x).read_bytes()).hexdigest() for x in deps}}
out=R/'lab/process/k2487-controlled-stopping-approximation.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
else:ck('saved_report_reproduces',json.loads(out.read_text())==report)
print(json.dumps({'result':'PASS','checks':len(checks),'controls':len(controls),'tolerance_parameters':report['tolerance_parameters']}))
