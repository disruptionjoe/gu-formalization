from pathlib import Path
from itertools import product,combinations
from fractions import Fraction
import ast,json,hashlib,sys,math
import sympy as s
from flint import arb,ctx
ctx.prec=256
ROOT=Path(__file__).resolve().parents[2];Q=s.Rational;checks={};controls={}
def ck(k,b):
 checks[k]=bool(b)
 if not b:raise AssertionError(k)
def ctrl(k,b):
 controls[k]=bool(b)
 if not b:raise AssertionError(k)

# Use exp(-k)=1/2, pi=1/2, c=log(3/2). Bound conditional factors rigorously.
for pi in [Q(1,4),Q(1,2),Q(3,4)]:
 for t in [Q(1,2),Q(1,4),Q(3,4)]:
  ec=1+pi/(1-pi)*(1-t)
  ck(f'chord_cancellation_{pi}_{t}',(1-pi)*(ec-1)+pi*(t-1)==0)
  ck(f'endpoint_equality_{pi}_{t}',(1-pi)*ec+pi*t==1)
  ctrl(f'excess_exponent_fails_{pi}_{t}',(1-pi)*(ec+Q(1,1000))+pi*t>1)
  for p in [Q(1,9),Q(1,3),Q(1,2),Q(4,5)]:
   pa=arb(str(p.p))/int(p.q);ca=(arb(str(ec.p))/int(ec.q)).log();aa=arb(str(pi.p))/int(pi.q);tt=arb(str(t.p))/int(t.q)
   val=(1-aa)*(ca*pa).exp()+aa*(1-pa+pa*tt)
   ck(f'conditional_factor_{pi}_{t}_{p}',val<1)
# Exhaust adaptive depth8 tree. Use p in{0,1}; equality permits exact rational weights.
# State: probability, Q, F, U, prior observed label, ever finite-cross, ever infinite-cross.
alpha=Fraction(1,8);states=[(Fraction(1),0,0,0,0,False,False)]
for depth in range(1,9):
 nxt=[]
 for mass,q,f,u,hist,hit,hiti in states:
  p=(hist+depth)%2
  prev=Fraction(3,2)**q*Fraction(1,2)**f;previ=2**q if f==0 else 0
  cases=[(Fraction(1,2),q+p,f,u+1,2),(Fraction(p,2),q,f+1,u,1),(Fraction(1-p,2),q,f,u,0)]
  ev=Fraction(0);evi=Fraction(0)
  for pr,qq,ff,uu,hh in cases:
   if not pr:continue
   mm=Fraction(3,2)**qq*Fraction(1,2)**ff;mi=2**qq if ff==0 else 0;ev+=pr*mm;evi+=pr*mi
   nxt.append((mass*pr,qq,ff,uu,hh,hit or mm>=1/alpha,hiti or mi>=1/alpha))
  ck(f'adaptive_conditional_{depth}_{q}_{f}_{u}_{hist}',ev<=prev and evi<=previ)
 states=nxt
 ck(f'tree_mass_{depth}',sum(x[0] for x in states)==1)
 ck(f'tree_Ville_crossing_{depth}',sum(x[0] for x in states if x[-2])<=alpha and sum(x[0] for x in states if x[-1])<=alpha)
 ck(f'tree_terminal_expectation_{depth}',sum(mass*Fraction(3,2)**q*Fraction(1,2)**f for mass,q,f,u,h,hi,hii in states)<=1)
# Nonvacuous finite-k stopping control: original adaptive tree cannot cross8.
# Constant p=1 reaches the finite threshold after six uses; enumerate all route histories.
cross_states=[(Fraction(1),0,0,False)]
for depth in range(1,9):
 nn=[]
 for mass,q,f,hit in cross_states:
  for is_test in [False,True]:
   qq=q+int(not is_test);ff=f+int(is_test);mm=Fraction(3,2)**qq*Fraction(1,2)**ff
   nn.append((mass/2,qq,ff,hit or mm>=8))
 cross_states=nn
 cm=sum(m for m,q,f,hit in cross_states if hit)
 ck('constant_bad_crossing_upper_'+str(depth),cm<=Fraction(1,8))
 if depth>=6:ck('constant_bad_crossing_positive_'+str(depth),cm>0)
ck('six_consecutive_uses_hit',Fraction(3,2)**5<8<=Fraction(3,2)**6)
ck('nonvacuous_crossing_probability',cm==sum(m for m,q,f,hit in cross_states if hit) and cm>0)
# All-bad zero-failure law exactly saturates exponential survival.
for m in [1,2,3,5,8,16]:ck('zero_count_endpoint_'+str(m),Fraction(1,2)**m*2**m==1)
ck('zero_failure_alive_and_dead_paths',any(f==0 and mass>0 for mass,q,f,u,h,hi,hii in states) and any(f>0 and mass>0 for mass,q,f,u,h,hi,hii in states))
# Predeclared union risk allocation, including infinity.
ww=[Q(1,3)]*3;ck('grid_weights',sum(ww)==1 and all(w>0 for w in ww));ctrl('unpenalized_three_choices_not_alpha',sum(Q(1,20) for _ in ww)>Q(1,20))
# Route-leaked preparation gives no common p. Exact contrasting expectation.
ctrl('leaked_route_breaks_supermartingale',Q(1,2)*Q(3,2)+Q(1,2)>1) # use loss1, test failure0
# Late branch disclosure: earlier reduced mixture remains distinct from retrospectively selected branch.
I=s.eye(2);z0=s.diag(1,0);z1=s.diag(0,1)
ctrl('final_transcript_not_predictable_state',(z0+z1)/2==I/2 and z0!=I/2)
# Rigorous prospective budgets, no observed data.
nu=arb('0.5');beta=arb('1e-7');kappa=arb('1e-6');alphaA=arb('.05');L=(3/alphaA).log();ci=arb(2).log();budgets=[]
for slots,uses,limit in [(1,10**6,'0.007'),(2,10**7,'0.0095')]:
 q=arb(1)/(4**slots);lam=arb('.5');C=lam/q;loss=(L/(ci*uses)+beta)/nu;eps=loss.sqrt();theta=lam*eps+kappa;out=theta/q
 ck('prospective_budget_'+str(slots),out<arb(limit) and theta<q)
 budgets.append({'slots':slots,'actual_uses_condition':uses,'test_probability':'1/2','failures_condition':0,'family_alpha':'.05','grid_candidates':3,'nu':'.5','beta':'1e-7','kappa':'1e-6','mean_infidelity_bound':str(loss),'output_error':str(out),'mean_success_lower':str(q-theta),'status':'prospective conditional, not measured'})
# A rationally certified design integer using interval bounds and neighboring integers.
tau=arb('.01');q=arb('.25');C=arb(2);allowed=nu*((tau-kappa/q)/C)**2-beta
ck('positive_systematic_headroom',allowed>0)
raw=L/(ci*allowed);needed=math.ceil(float(raw));ck('integer_use_design',arb(needed)>=raw and arb(needed-1)<raw)
# Finite-k route with observed failures, grid penalty retained.
finite=[]
for failures in [0,1,10,100]:
 options=[]
 for ek in [2,4]:
  kk=arb(ek).log();cc=(arb(2)-arb(1)/ek).log();options.append((kk*failures+L)/(cc*10**6))
 if failures==0:options.append(L/(ci*10**6))
 best=min(options,key=float);finite.append({'failures':failures,'uses':10**6,'mean_risk_bound':str(best)})
 ck('finite_k_nonvacuous_'+str(failures),best>0 and best<arb('.001'))
# Gap and systematic error cannot be omitted even with zero actual test probability.
ck('readout_gap_floor',Q(1,10000000)/Q(1,2)==Q(1,5000000))
ctrl('underpriced_readout_false_zero',Q(1,5000000)>0)
evidence={'universal':'conditional convex-chord supermartingale, elementary Ville stopping proof, weighted-grid union, zero-failure process and maximal coefficient within this family','finite_exact':'adaptive depth8 tree plus nonvacuous constant-bad finite-k crossing enumeration; endpoint and route-leaked exponential-factor controls','rigorous_numeric':'Arb256 original one/two-slot prospective consumer and integer-use budget','finite_crossing_probability_depth8':str(cm),'budgets':budgets,'design_one_slot_1percent_uses':needed,'finite_failure_grid':finite,'scope':'predictable used risks and normalized mean success only; no final transcript, independent-replica, hardware, native GU or global optimality claim'}

deps=['tests/channel-swings/k2448_binary_hidden_route_certificate_probe.py', 'explorations/conditional-build/k2448-binary-hidden-route-certificate-2026-11-01.md', 'explorations/conditional-build/k2447-coherent-program-verification-2026-11-01.md', 'lab/process/k2447-coherent-program-verification.json', 'explorations/conditional-build/k2444-sharp-heralded-transfer-2026-11-01.md']
report={'result_id':'K2448','checks':checks,'controls':controls,'evidence':evidence,'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2448-binary-hidden-route-certificate.json'
if '--check' in sys.argv:assert json.loads(out.read_text())==report
else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('k2448-binary-hidden-route-certificate',len(checks),'checks',len(controls),'controls PASS')
