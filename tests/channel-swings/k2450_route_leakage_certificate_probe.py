"""Sharp conditional route-leakage algebra and stopped adaptive trees."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,hashlib,sys
from flint import arb,ctx
ctx.prec=256
ROOT=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,b):
 checks[k]=bool(b)
 if not b:raise AssertionError(k)
def ctrl(k,b):
 controls[k]=bool(b)
 if not b:raise AssertionError(k)
def A(q):return arb(q.numerator)/q.denominator
for pi,delta,e in product([F(1,4),F(1,2),F(3,4)],[F(0),F(1,4),F(3,4)],[F(0),F(1,2),F(3,4)]):
 a=1-pi;L=1-delta;r=1-e;ec=1+pi*r*L/a
 key=str((pi,delta,e))
 ck('shifted_endpoint_'+key,a*ec+pi*(1-r*L)==1)
 ck('compensated_endpoint_'+key,a*(1+pi*r/a)+pi*(1-r*L)==1+pi*r*delta)
 for j in range(1,8):
  h=L*F(j,8);c=A(ec).log()/A(L);fac=A(a)*(c*A(h)).exp()+A(pi)*(1-A(r*h))
  ck('chord_'+key+'_'+str(j),fac<=1)
 ck('zero_survival_'+key,(a/(a+pi*L))**3==(1+pi*L/a)**(-3))
pi=F(1,2);delta=F(1,4);L=1-delta;r=F(1,2)
ctrl('unpriced_leakage_supermartingale_fails',(1-pi)*(1+pi*r/(1-pi))+pi*(1-r*L)==F(17,16)>1)
ctrl('larger_coefficient_fails',(1-pi)*(F(11,8)+F(1,100))+pi*(1-r*L)>1)
# Exact quantum diagonal witnesses: TV equals half trace norm.
for delta in [F(0),F(1,4),F(3,4),F(1)]:
 use=[F(0),F(1)];test=[delta,1-delta]
 ck('state_distance_'+str(delta),sum(abs(a-b) for a,b in zip(use,test))/2==delta)
 ck('risk_difference_'+str(delta),use[1]-test[1]==delta)
 # Same test law pT=0; arbitrary allowed pU=delta, record law independent of delta.
 good={'pT':F(0),'pU':F(0)};leaky={'pT':F(0),'pU':delta};pi=F(2,3)
 observable=lambda model:(1-pi,pi*(1-model['pT']),pi*model['pT'])
 ck('floor_indistinguishability_'+str(delta),observable(good)==observable(leaky) and leaky['pU']-good['pU']==delta)
 ck('leakage_premise_'+str(delta),leaky['pU']<=leaky['pT']+delta)
ctrl('no_leakage_bound_no_information',observable(good)==observable(leaky) and leaky['pU']==1 and good['pU']==0)
# Fully enumerated adaptive exact tree, tracking any crossing.
# h is selected from{0,L}; all exponential factors are rational despite adaptive pi,delta.
alpha=F(1,4);cross=F(0);mass=F(0);nodes=0
stack=[(0,F(1),F(1),0,0,False)]
while stack:
 depth,prob,M,uses,fails,hit=stack.pop();nodes+=1
 if depth==9:
  mass+=prob
  if hit:cross+=prob
  continue
 pi=F(1,2) if depth%2==0 else F(2,3);delta=F(1,4) if uses%2==0 else F(1,3);L=1-delta;e=F(1,2);r=1-e
 h=L if fails%2==0 else F(0);pT=h;factorU=1+pi*r*L/(1-pi) if h else F(1)
 branches=[(1-pi,factorU,1,0),(pi*(1-pT),F(1),0,0),(pi*pT,e,0,1)]
 assert sum(p*factor for p,factor,_,_ in branches)==1
 for p,factor,u,x in branches:
  if not p:continue
  MM=M*factor;stack.append((depth+1,prob*p,MM,uses+u,fails+x,hit or MM>=1/alpha))
ck('adaptive_tree_probability',mass==1);ck('adaptive_crossing_bound',cross<=alpha);ctrl('adaptive_crossing_nonvacuous',cross>0)
# Exact survival recursion sums arbitrary passing tests before each use.
for pi,delta,m in product([F(1,3),F(1,2),F(3,4)],[F(0),F(1,4),F(1,2)],[1,2,5]):
 a=1-pi;L=1-delta;one=a/(1-pi*delta)
 ck('absorbing_survival_'+str((pi,delta,m)),one**m==(a/(a+pi*L))**m)
# Strict positive denominators and integer ceiling consumers, interval arithmetic.
budgets=[]
for slots in [1,2]:
 pi=arb(1)/2;delta=arb('0.0000001');beta=arb('0.0000001');kappa=arb('0.000001');nu=arb(1)/2;q=arb(4)**(-slots);C=arb(2)**(2*slots-1);tau=arb('0.01');L=1-delta;c=(1+pi*L/(1-pi)).log()/L
 D=nu*((tau-kappa/q)/C)**2-delta-beta;need=arb(20).log()/(c*D);N=int(need.upper().ceil().unique_fmpz())
 ck('positive_budget_'+str(slots),D>0)
 allowance=lambda n:C*((arb(20).log()/(c*n)+delta+beta)/nu).sqrt()+kappa/q
 ck('count_suffices_'+str(slots),allowance(N)<=tau);ctrl('predecessor_count_fails_'+str(slots),allowance(N-1)>tau)
 ck('success_margin_'+str(slots),allowance(N)/C/2<q) # stronger direct check below
 Q=(arb(20).log()/(c*N)+delta+beta)/nu
 ck('direct_success_margin_'+str(slots),Q.sqrt()/2+kappa<q)
 budgets.append({'slots':slots,'required_actual_uses':N,'output_allowance':str(allowance(N)),'risk_denominator':str(D)})
deps=[str(Path(__file__).relative_to(ROOT)),'explorations/conditional-build/k2450-route-leakage-certificate-2026-11-01.md','lab/process/k2448-binary-hidden-route-certificate.json','explorations/conditional-build/k2444-sharp-heralded-transfer-2026-11-01.md']
report={'result_id':'K2450','checks':checks,'controls':controls,'adaptive_tree':{'nodes':nodes,'crossing_probability':str(cross),'alpha':str(alpha)},'prospective_not_data':budgets,'evidence_kinds':{'universal':'written chord, exact maximal coefficient, Ville and quantum effect argument','finite':'endpoint algebra, full adaptive tree, interval consumers','ceiling':'per-history leakage premise not established by test observations'},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2450-route-leakage-certificate.json'
if '--check' in sys.argv:assert json.loads(out.read_text())==report
else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('K2450',len(checks),'checks',len(controls),'controls PASS')
