"""Exact actual-spending recurrence, original-carrier counterlaw and capped paths."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import ast,json,hashlib,sys
ROOT=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ctrl(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
# Reuse only predecessor's exact recurrence, not its numerical optimization.
p=ROOT/'tests/channel-swings/k2469_verifier_cost_tail_probe.py'
for node in ast.parse(p.read_text()).body:
 if isinstance(node,ast.FunctionDef) and node.name=='cdf':exec(compile(ast.Module(body=[node],type_ignores=[]),str(p),'exec'),globals())
def dist(N,K,q,caps,pi=F(1,2),cU=1,charges=(1,2)):
 rows=[[F(int(k==0)) for k in range(K+1)]]
 for n in range(1,N+1):
  row=[]
  for k in range(K+1):
   val=(1-pi)*rows[n-1][k-cU] if k>=cU else F(0)
   for pj,sj,cj in zip((1-q,q),caps,charges):
    if k>=cj:val+=pi*pj*sj*row[k-cj]
    if k==cj:val+=pi*pj*(1-sj)
   row.append(val)
  rows.append(row)
 return rows[-1]
for N in [1,2,3]:
 for q in [F(0),F(1,3),F(1)]:
  for K in [0,2,5,9]:
   ck('all_pass_original_recurrence_'+str((N,q,K)),sum(dist(N,K,q,(F(1),F(1))))==cdf(N,q,K))
   dd=dist(N,K,q,(F(0),F(0)))
   # Uses can precede rejection; all-reject tests do not stop preceding uses.
   ex=F(0)
   for uses in range(N):
    for pj,cj in [(1-q,1),(q,2)]:
     if uses+cj<=K:ex+=F(1,2)**(uses+1)*pj
   if N<=K:ex+=F(1,2)**N
   ck('all_reject_closed_form_'+str((N,q,K)),sum(dd)==ex)
# A finite-budget path recursion independently computes the adaptive process tail.
def tail_tree(N,K,q,caps,adaptive=False):
 @lru_cache(None)
 def go(n,c,h):
  if c>K:return F(1)
  if n==0:return F(0)
  out=F(1,2)*go(n-1,c+1,h+1)
  for j,(pj,cj) in enumerate([(1-q,1),(q,2)]):
   sj=caps[j]*(F(1,2) if adaptive and (h+j)%2 else 1)
   # The rejecting test itself is charged, hence may exceed the budget.
   out+=F(1,2)*pj*(F(1) if c+cj>K else sj*go(n,c+cj,h+1))
  return out
 return go(N,0,0)
for N in [1,2]:
 for K in range(7):
  caps=(F(2,3),F(1,4));q=F(2,5);reference=1-sum(dist(N,K,q,caps))
  ck('independent_tree_recurrence_'+str((N,K)),tail_tree(N,K,q,caps)==reference)
  ck('adaptive_tail_domination_'+str((N,K)),tail_tree(N,K,q,caps,True)<=reference)
# Original target-orthogonal Q/T zero block: h=1/[2(1+a)],
# T=[[2*a*h,sqrt(2*a)*h],[sqrt(2*a)*h,h]], so first-vector acceptance=2*a*h.
prior=json.loads((ROOT/'lab/process/k2463-local-verifier-calibration.json').read_text())
bank=json.loads((ROOT/'lab/process/k2457-local-verifier-phase-design.json').read_text())
counter=[]
for law in bank['original_laws']:
 av=F(law['a']);h=1/(2*(1+av));r=2*av*h
 ck('original_block_r_'+str(av),r==av/(1+av) and r<F(1,2))
 for q in [F(0),F(1,3),F(1)]:
  value=1-sum(dist(1,2,q,(F(1),r)))
  ck('original_counterlaw_'+str((av,q)),value==F(1,4)+q*(r/2-F(1,4)))
 counter.append({'a':str(av),'r':str(r),'tail_q0':'1/4','tail_q1':str(r/2)})
 ctrl('actual_monotonicity_reversed_'+str(av),r/2<F(1,4))
ctrl('upper_calibration_does_not_force_rejection',sum(dist(1,3,F(1,2),(F(1),F(1))))<1)
# Finite horizon paths make capped-completion inclusion explicit without relying on assertions.
def paths(N,q,caps,steps=7):
 states=[(0,0,F(1),())];complete=[];reject=[];live=[]
 for _ in range(steps):
  nxt=[]
  for n,c,pr,hist in states:
   nh=hist+(1,);p=pr/2
   if n+1==N:complete.append((c+1,p,nh))
   else:nxt.append((n+1,c+1,p,nh))
   for pj,sj,cj in zip((1-q,q),caps,(1,2)):
    reject.append((c+cj,pr*pj*(1-sj)/2,hist+(cj,)))
    if sj:nxt.append((n,c+cj,pr*pj*sj/2,hist+(cj,)))
  states=nxt
 return complete,reject,states
comp,rej,live=paths(2,F(1,3),(F(3,4),F(1,2)))
ck('finite_path_mass',sum(x[1] for x in comp+rej)+sum(x[2] for x in live)==1)
for K in range(1,8):
 capped=[x for x in comp if all(sum(x[2][:i])<=K for i in range(1,len(x[2])+1))]
 lost=sum(x[1] for x in comp)-sum(x[1] for x in capped)
 ck('capped_path_inclusion_'+str(K),all(x in comp for x in capped))
 ck('completion_loss_identity_'+str(K),lost==sum(x[1] for x in comp if x[0]>K))
 ck('completion_loss_envelope_'+str(K),lost<=1-cdf(2,F(1,3),K))
 ctrl('postcharge_abort_is_too_late_'+str(K),any(x[0]>K for x in comp))
ctrl('unconditional_not_conditional',F(1,100)/F(1,20)>F(1,100))
deps=['explorations/conditional-build/k2472-outcome-dependent-cost-2026-11-01.md',str(Path(__file__).relative_to(ROOT)),'lab/process/k2469-verifier-cost-tail.json','lab/process/k2463-local-verifier-calibration.json','lab/process/k2457-local-verifier-phase-design.json']
for dep in deps[2:]:
 data=json.loads((ROOT/dep).read_text());ck('authenticated_'+Path(dep).stem,all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in data['dependencies'].items()))
old=json.loads((ROOT/deps[2]).read_text());inherited=[{k:v for k,v in row.items() if k!='global_lower_budget_checks'} for row in old['original_full_carrier_quantiles']]
report={'result_id':'K2472','checks':checks,'controls':controls,'inherited_minimax_quantiles':inherited,'original_counterlaws':counter,'evidence_kinds':{'universal':'coupling, ideal target attainment, PGF recurrence and event inclusion','finite':'rational recurrence and independent finite adaptive path trees; original block fractions','reused':'K2469 complete-carrier optimum and original calibration block','ceiling':'uncertainty-class minimax under inherited sufficient risk constraint; cap sharpness classical unless realized'},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2472-outcome-dependent-cost.json'
if '--check' in sys.argv:assert json.loads(out.read_text())==report
else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('K2472',len(checks),'checks',len(controls),'controls PASS')
