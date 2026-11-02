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

from itertools import product
# Exact full adaptive binary no-output histories (history may carry a fresh latent label).
def tree(depth,history=()):
 if depth==0:return F(0),F(0),F(1),F(0)
 # Risk and output vary across reached histories while alpha=1/10,p=2/5 hold.
 q=F(2,5)+F(sum(history)%3,10);f=F(1,20)+F(len(history)%2,20)
 branches=[tree(depth-1,history+(bit,)) for bit in [0,1]]
 vals=[sum(row[j] for row in branches)/2 for j in range(4)]
 return f+(1-q)*vals[0],q+(1-q)*vals[1],(1-q)*vals[2],1+(1-q)*vals[3]
for m in range(1,9):
 wrong,out,none,attempts=tree(m);alpha=F(1,10);p=F(2,5)
 ck('adaptive_tree_'+str(m),out+none==1 and wrong<=alpha/p*out and none<=(1-p)**m and attempts<=1/p)
# Independent exact Bellman optimization over a rational simplex, not formula labels.
for alpha,p in product([F(0),F(1,10),F(2,5),F(4,5),F(1)], [F(1,5),F(1,2),F(1)]):
 v=F(0);qstar=max(alpha,p)
 for m in range(1,9):
  qs=sorted({p,F(1),qstar,*[F(i,20) for i in range(21) if F(i,20)>=p]})
  v=max(min(alpha,q)+(1-q)*v for q in qs)
  formula=alpha/qstar*(1-(1-qstar)**m)
  ck('Bellman_'+str((alpha,p,m)),v==formula)
# IID law attains simultaneous alpha<=p bounds including actual repeated costs.
for alpha,p in [(F(1,100),F(1,10)),(F(1,10),F(2,5)),(F(2,5),F(2,5))]:
 for m in [1,3,10]:
  reach=F(1);wrong=out=attempts=F(0)
  for _ in range(m):wrong+=reach*alpha;out+=reach*p;attempts+=reach;reach*=1-p
  ck('iid_sharp_'+str((alpha,p,m)),wrong==alpha/p*out and out==1-(1-p)**m and attempts==(1-(1-p)**m)/p)
# Marginal-only selection counterexample with ten equally likely original U cells.
wrong=out=F(0)
for u in range(10):
 first='bad' if u==0 else ('good' if u<9 else 'none')
 second='bad' if u==9 else 'good'
 final=second if first=='none' else first
 wrong+=F(final=='bad',10);out+=F(final!='none',10)
ctrl('marginal_error_not_history_valid',wrong==F(1,5)>F(1,9) and out==1)
latent=[[u<2]*3 for u in range(5)]
marginals=[sum(row[i] for row in latent)/F(5) for i in range(3)]
none3=sum(not any(row) for row in latent)/F(5)
ctrl('marginal_success_not_geometric',marginals==[F(2,5)]*3 and none3==F(3,5) and none3>(1-F(2,5))**3)
# Exact shared-good-event mixture directly checks the sufficient ratio across masses.
for zeta,p,rho in product([F(0),F(1,100),F(1,5)],[F(1,5),F(4,5)],[F(1,10),F(1)]):
 for m in [1,4]:
  cm=1-(1-p)**m;gmin=(1-zeta)*cm;bound=(zeta+rho*gmin)/(zeta+gmin)
  good=True
  for g in [gmin,(gmin+1-zeta)/2,1-zeta]:
   for bad in [F(0),zeta/2,zeta]:good &= (rho*g+bad)/(g+bad)<=bound
  ck('shared_event_ratio_'+str((zeta,p,rho,m)),good)
# Operational conditional design: cap loss composes to p, then finite retry cap.
alpha=F(1,1000);s=F(4,5);delta=F(1,10);p=s-delta;eta=F(1,500);S=7;K=11;m=4
ck('capped_retry_design',alpha<=eta*p and (1-p)**m<=F(1,100) and S+m*K==51)
ctrl('retry_without_risk_charge_fails',alpha/p>alpha)
ctrl('setup_is_not_paid_once',F(3)/p>3)
ctrl('no_pathwise_total_without_cap',(1-p)**100>0)
# The failure of the reach-history premise is a real latent-variable construction,
# not mutation of an asserted theorem Boolean.
# Cross-result consumer: quantities are supplied under the common good-event law.
from flint import arb,ctx
ctx.prec=256
def ar(x):
 x=F(x);return arb(x.numerator)/x.denominator
eta2=F(1,100);zeta2=F(1,1000);p2=F(7,10);m2=4;cm2=1-(1-p2)**m2
rho_max=eta2-(1-eta2)*zeta2/((1-zeta2)*cm2);alpha2=p2*rho_max
ck('shared_calibration_allocation_exact',rho_max>0 and (zeta2+rho_max*(1-zeta2)*cm2)/(zeta2+(1-zeta2)*cm2)==eta2)
floor=zeta2/(zeta2+(1-zeta2)*cm2)
ctrl('calibration_floor_blocks_zero_error_target',floor>zeta2 and floor>0)
cv=arb(2).log();CC=(1+cv)**2/(4*(1-cv));KB=F(1,1000000);D=F(1,100)
count=((1/ar(alpha2)).log()+CC*ar(KB)/ar(alpha2))/(cv*ar(D))
uses=int(count.upper().ceil().unique_fmpz())
ck('composed_count_ceiling',uses>count and uses-1<count)
no_cal_alpha=eta2*p2;uncal=((1/ar(no_cal_alpha)).log()+CC*ar(KB)/ar(no_cal_alpha))/(cv*ar(D))
ctrl('ignoring_shared_calibration_understates_count',count>uncal)
consumer={'eta':str(eta2),'zeta':str(zeta2),'completion_floor':str(p2),'m':m2,'rho_max':str(rho_max),'alpha':str(alpha2),'K_B':str(KB),'D':str(D),'Nuse':uses,'cost_feasibility':'not supplied; K and p must belong to the same capped attempt'}
deps=['lab/process/k2471-sharp-stopping-coefficient.json','lab/process/k2472-outcome-dependent-cost.json','lab/process/k2463-local-verifier-calibration.json']
for pth in deps:ck('authenticated_'+Path(pth).stem,authenticate(pth))
finish('k2475-retry-risk-cost',{'universal':'conditional expectation, local error/output domination, Bellman induction, shared calibration event mixture','finite':'rational adaptive trees, exact Bellman endpoints/grid, attaining IID laws and latent-selection counterexamples','ceiling':'sharp abstract interface; no claim arbitrary quantum effects realize it'},deps,{'composed_consumer':consumer,'design_example':{'alpha':str(alpha),'uncapped_completion':str(s),'cap_loss':str(delta),'p':str(p),'conditional_error_target':str(eta),'attempt_cap':m,'total_charge_cap':S+m*K}})
