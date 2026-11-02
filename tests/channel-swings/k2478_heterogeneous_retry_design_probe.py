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


from itertools import product,permutations
from flint import arb,ctx
ctx.prec=256
def ar(x):
 x=F(x);return arb(x.numerator)/x.denominator
def vertices(a,p):
 qs={p,F(1)}
 if a>=p:qs.add(a)
 return sorted({(q,f) for q in qs for f in [F(0),min(a,q)]})
def masses(law):
 r=F(1);W=F(0)
 for q,f in law:W+=r*f;r*=1-q
 return W,1-r
def sharp(schedule,z=F(0)):
 W,C=masses([(max(a,p),a) for a,p in schedule]);return(z+(1-z)*W)/(z+(1-z)*C)
schedules=[[(F(1,10),F(1,2)),(F(1,5),F(2,3))],[(F(3,4),F(1,2)),(F(1,20),F(1,4))],[(F(0),F(1)),(F(1),F(1,3))],[(F(1,20),F(1,4)),(F(1,3),F(2,3)),(F(2,5),F(1,3))]]
for ix,sched in enumerate(schedules):
 for z in [F(0),F(1,100),F(1,3)]:
  vals=[]
  for law in product(*[vertices(a,p) for a,p in sched]):
   W,C=masses(law);v=(z+(1-z)*W)/(z+(1-z)*C);vals.append(v)
   ck('vertex_upper_'+str((ix,z,law)),v<=sharp(sched,z))
  ck('attains_'+str((ix,z)),max(vals)==sharp(sched,z))
 # independent backwards support oracle, including extreme eta values
 for eta in [F(0),F(1,5),F(1,2),F(1)]:
  v=F(0)
  for a,p in reversed(sched):v=max(f-eta*q+(1-q)*v for q,f in vertices(a,p))
  W,C=masses([(max(a,p),a) for a,p in sched]);ck('support_'+str((ix,eta)),v==W-eta*C)
items=[(F(1,100),F(1,2),F(10)),(F(1,10),F(1,2),F(1)),(F(1,5),F(2,3),F(3))]
def cost(seq,z=F(0)):
 r=F(1);val=F(0)
 for a,p,K in seq:val+=((1-z)*r+z)*K;r*=1-p
 return val
for z in [F(0),F(1,10)]:
 sr=sorted(items,key=lambda x:x[0]/max(x[0],x[1]));sc=sorted(items,key=lambda x:x[2]/x[1]);bestR=sharp([(a,p) for a,p,k in sr],z);bestC=cost(sc,z)
 for seq in permutations(items):
  ck('risk_order_'+str((z,seq)),sharp([(a,p) for a,p,k in seq],z)>=bestR)
  ck('cost_order_'+str((z,seq)),cost(seq,z)>=bestC)
A,B=items[:2]
ctrl('orders_conflict',sharp([(a,p) for a,p,k in [A,B]])<sharp([(a,p) for a,p,k in [B,A]]) and cost([A,B])>cost([B,A]))
ctrl('omitted_shared_bad_cost',cost([A,B],F(1,10))>cost([A,B]))
ck('example_exact_cost',cost([A,B])==F(21,2) and cost([B,A])==6)
# KKT exact two-attempt allocation, independent scalar grid budget optimum.
a1,a2=F(3,80),F(3,40);budget=F(3,40)
ck('allocation_risk',a1+a2/2==budget and sharp([(a1,F(1,2)),(a2,F(1,2))])==F(1,10))
ck('stationarity',1/a1==2/a2)
for n in range(1,120):
 x=F(n,1600);y=2*(budget-x)
 if 0<y<=F(1,2):ck('allocation_product_'+str(n),x*y<=a1*a2)
ctrl('common_allocation_suboptimal',a1*a2>F(1,20)**2)
ck('log_saving',(ar(a1*a2)/ar(F(1,20)**2)).log().overlaps(ar(F(9,8)).log()))
# Complete scalar KKT quadratic: exact selected lambda and reciprocal cost.
import sympy as sp
lam,r,w,aa,bb=sp.symbols('lambda r w a b',positive=True)
x=(w*aa+sp.sqrt((w*aa)**2+4*lam*r*w*bb))/(2*lam*r)
ck('quadratic_stationarity',sp.simplify(lam*r*x*x-w*aa*x-w*bb)==0)
# Certified ceiling counts, charging each rounded count.
c=arb(2).log();Cs=(1+c)**2/(4*(1-c));continuous=[];rounded=[]
for a in [a1,a2]:
 value=((1/ar(a)).log()+Cs*ar(F(1,1000000))/ar(a))/(c*ar(F(1,100)))
 nn=int(value.ceil().unique_fmpz());continuous.append(value);rounded.append(nn)
 ck('count_round_'+str(a),value<=nn and nn-1<value)
ck('sum_round_bound',sum(rounded)-sum(continuous,arb(0))<2)
ctrl('round_down_not_safe',sum(rounded)-2<sum(continuous,arb(0)))
# Marginal-only calibration counterexample from actual latent outcomes.
latent=list(range(20))
first=['wrong' if u<2 else ('correct' if u<18 else 'none') for u in latent]
second=['wrong' if u>=18 else 'correct' for u in latent]
terminal=[b if a=='none' else a for a,b in zip(first,second)]
ck('latent_marginals',F(first.count('wrong'),20)==F(1,10) and F(second.count('wrong'),20)==F(1,10) and F(first.count('none'),20)==F(1,10))
ctrl('marginal_calibration_not_conditional',F(terminal.count('wrong'),20)==F(1,5) and F(terminal.count('wrong'),20)>F(1,9))
# A genuine branching no-output history, independent of deterministic schedule products.
root=(F(1,10),F(1,3));left=(F(1,20),F(1,2));right=(F(2,5),F(1,4));beta=F(1,3)
branches=[]
for (q0,f0),(qL,fL),(qR,fR) in product(vertices(*root),vertices(*left),vertices(*right)):
 W=f0+(1-q0)*(beta*fL+(1-beta)*fR)
 C=q0+(1-q0)*(beta*qL+(1-beta)*qR)
 branches.append((W,C))
for eta in [F(0),F(1,10),F(2,3),F(1)]:
 VL=max(f-eta*q for q,f in vertices(*left));VR=max(f-eta*q for q,f in vertices(*right))
 value=max(f-eta*q+(1-q)*(beta*VL+(1-beta)*VR) for q,f in vertices(*root))
 ck('branched_support_'+str(eta),value==max(W-eta*C for W,C in branches))
optimal=max(W/C for W,C in branches)
ck('branch_ratio_zero',max(W-optimal*C for W,C in branches)==0)

# Exact integer count optimum in the supplied two-attempt sufficient-design class.
beta=Cs/1000000;rootbrackets={};delta=arb(2)**(-200)
for n in range(101,747):
 value=beta/(beta*(n*c/100).exp()).lambertw()
 lo=ar(F(str(value.lower().fmpq())))-delta
 hi=ar(F(str(value.upper().fmpq())))+delta
 ck('root_bracket_'+str(n),lo>0 and (1/lo).log()+beta/lo>n*c/100 and (1/hi).log()+beta/hi<n*c/100)
 rootbrackets[n]=(lo,hi)
ck('minimum_count_101',(arb(2).log()+2*beta)>100*c/100 and (arb(2).log()+2*beta)<101*c/100)
for n in range(101,747):
 ck('excludes_total847_'+str(n),rootbrackets[n][0]+rootbrackets[847-n][0]/2>ar(F(3,40)))
ck('attains_total848',rootbrackets[474][1]+rootbrackets[374][1]/2<ar(F(3,40)))
ck('equal_counts_min433',rootbrackets[432][0]>ar(F(1,20)) and rootbrackets[433][1]<ar(F(1,20)))
ctrl('one_fewer_use_fails',rootbrackets[474][0]+rootbrackets[373][0]/2>ar(F(3,40)))
integer_result={'total':848,'witness':[474,374],'excluded_predecessor_total':847,'equal_count_total':866,'claim_scope':'minimum integer uses for the supplied sufficient two-attempt certificate only'}
deps=['lab/process/k2475-retry-risk-cost.json']
for p in deps:ck('authenticate_'+p,authenticate(p))
finish('k2478-heterogeneous-retry-design',{'universal':'signed-payoff Bellman, calibration mixture, exchange argument and convex KKT proofs','finite':'exact rational vertices, ordered designs and allocation; symbolic quadratic identity and Arb256 rounded consumer','reused':'K2475 interfaces authenticated','ceiling':'sharp abstract classical risk/cost, continuous optimizer and feasible rounding, not original quantum attainability'},deps,{'unequal_allocation':[str(a1),str(a2)],'rounded_use_counts':rounded,'integer_optimum':integer_result})
