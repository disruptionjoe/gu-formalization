"""Exact Markov-word versus instrument checks; universal proofs are in K2488."""
from pathlib import Path
import json,hashlib,sys,itertools
import sympy as S
R=Path(__file__).resolve().parents[2];Q=S.Rational
checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ctrl(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError('contrary '+k)
def simp(M):return M.applyfunc(S.simplify)
def co(r,u,v,n):
 if n==0:return [S.Integer(1)]*6
 p=v/(u+v);e=u/(u+v);a=1-u;b=1-v;K=S.Matrix([[a*r,u*(1-r)],[v*(1-r),b*r]])
 z=K**(n-1)*S.ones(2,1)
 return [p*a**(n-1),p*z[0],e*z[1],p*u**(n//2)*v**((n-1)//2),e*v**(n//2)*u**((n-1)//2),e*b**(n-1)]
def eps(c,F=Q(9,10)):return (1-F)*max(c[1:])/(F*c[0]+(1-F)*max(c[1:]))
prior=json.loads((R/'lab/process/k2486-noisy-flag-alternating-verifier.json').read_text());ck('original_dimension',prior['checks']['full_carrier_dimensions']);rs=[Q(f['r']) for f in prior['fixtures']];ck('original_angles',rs==[Q(27,127),Q(15,67)])
u,v,r,z=S.symbols('u v r z');a=1-u;b=1-v;K=S.Matrix([[a*r,u*(1-r)],[v*(1-r),b*r]])
ck('spectral_discriminator',S.factor((a*S.eye(2)-K).det()-(1-r)*((1-r)*(a*a-u*v)+r*a*(v-u)))==0)
ck('null_theta_crossover',S.factor((b*S.eye(2)-K).det()-(1-r)*(b*b-u*v-r*(1-u-v)))==0)
x=S.symbols('x',positive=True)
f=(x*S.eye(2)-K).det()
ck('alternating_rate_polynomial_identity',S.factor((f/r-((1-r)*x*(2*x-a-b)+r*(x-a)*(x-b))).subs(v,x*x/u))==0)
k,z=S.symbols('k z',positive=True)
ck('marginal_ratio_derivative',S.factor(S.diff(k*z*z/(1-k*z)**2,z)-2*k*z/(1-k*z)**3)==0)
ck('safe_quarter_marginal',Q(1,3)/(1-Q(1,3))**2<1)
ctrl('three_tenths_marginal_can_fail',Q(21,50)*Q(49,50)>(1-Q(21,50))**2)
fixtures=[]
for law,r in enumerate(rs):
 Qm=S.diag(1,1,0,1,0,0);Tm=S.zeros(6);Tm[0,0]=1;Tm[1,1]=r;Tm[2,2]=1-r;Tm[1,2]=Tm[2,1]=S.sqrt(r*(1-r));Tm[4,4]=1;I=S.eye(6)
 for ix,(u,v) in enumerate([(Q(1,100),Q(99,100)),(Q(1,10),Q(1,5)),(Q(2,5),Q(9,10)),(Q(1,2),Q(3,4)),(Q(1,5),Q(9,10))]):
  H=S.Matrix([[1-u,u],[v,1-v]]);pi=[v/(u+v),u/(u+v)]
  # Independent memory-conditioned selective instrument, no use of K in this recursion.
  states=[]
  for initial in range(6):
   rho=S.zeros(6);rho[initial,initial]=1;states.append([pi[e]*(Qm if e==0 else I-Qm)*rho*(Qm if e==0 else I-Qm) for e in range(2)])
  hist=[co(r,u,v,0)]
  for n in range(1,7):
   if n>1:
    B=Qm if n%2 else Tm
    for i in range(6):states[i]=[simp((B if e==0 else I-B)*sum((H[f,e]*states[i][f] for f in range(2)),S.zeros(6))*(B if e==0 else I-B)) for e in range(2)]
   actual=[S.simplify(sum(S.trace(t) for t in st)) for st in states];c=co(r,u,v,n);tag=f'{law}_{ix}_{n}'
   ck('instrument_'+tag,actual==c);ck('nested_'+tag,all(c[k]<=hist[-1][k] for k in range(6)))
   if u+v<=1:ck('normalized_order_'+tag,n==1 or all(c[k]<= (1-u)*hist[-1][k] for k in range(6)))
   hist.append(c)
  if u+v>1:ctrl(f'nonmonotone_A_{law}_{ix}',co(r,u,v,3)[3]/co(r,u,v,3)[0]>co(r,u,v,2)[3]/co(r,u,v,2)[0])
  if u*v==(1-u)**2:
   for n in [3,4,7,8]:
    c=co(r,u,v,n);ck(f'critical_scalar_{law}_{n}',c[3]/c[0]==(1 if n%2 else u/(1-u)) and c[4]/c[0]==(u/v if n%2 else u/(1-u)))
  if u*v>(1-u)**2:ctrl(f'supercritical_{law}',co(r,u,v,21)[3]/co(r,u,v,21)[0]>10)
  # Exact two-step chain and sharp cap calculation; bounded fixture only.
  eta=u/(u+v);t=1-u-v;um=eta*(1-t*t);vm=(1-eta)*(1-t*t)
  ck(f'spacing_matrix_{law}_{ix}',H**2==S.Matrix([[1-um,um],[vm,1-vm]]));ck(f'spacing_criterion_{law}_{ix}',um+vm<=1 and um*vm<(1-um)**2)
  if ix in [2,3]:
   n=1;tol=Q(1,1000)
   while eps(co(r,um,vm,n))>tol:
    n+=1
    if n>200:raise AssertionError('fixture cap unexpectedly large')
   c=co(r,um,vm,n);F=Q(9,10)
   # Fixed-F vertex cost including prep1, test2, skipped-transition price1/10 and m2.
   hs=[co(r,um,vm,j) for j in range(n+1)];costs=[1+2*sum(h[k] for h in hs[:-1])+Q(1,5)*sum(h[k] for h in hs[1:-1]) for k in range(6)]
   ratios=[costs[0]/c[0]]+[(F*costs[0]+(1-F)*costs[k])/(F*c[0]+(1-F)*c[k]) for k in range(1,6)]
   ck(f'first_feasible_{law}_{ix}',eps(co(r,um,vm,n-1))>tol and eps(c)<=tol)
   ctrl(f'omitted_transition_cost_{law}_{ix}',costs[0]>1+2*sum(h[0] for h in hs[:-1]))
   weights=[Q(1,5)]*5;num=sum(weights[k-1]*(F*costs[0]+(1-F)*costs[k]) for k in range(1,6));den=sum(weights[k-1]*(F*c[0]+(1-F)*c[k]) for k in range(1,6));ck(f'renewal_vertex_bound_{law}_{ix}',num/den<=max(ratios))
   fixtures.append({'r':str(r),'u':str(u),'v':str(v),'eta':str(eta),'spacing':2,'sampled_u':str(um),'sampled_v':str(vm),'fidelity_min':'9/10','tolerance':'1/1000','first_feasible_cap':n,'sharp_error':str(eps(c)),'target_yield_lower':str(F*c[0]),'worst_renewal_cost':str(max(ratios))})
  if ix==3:
   c=co(r,u,v,5);iid=co(r,eta,1-eta,5);ctrl(f'same_marginal_wrong_joint_{law}',c!=iid and eps(c)>eps(iid))
 # pure-target unit-price cost identity
 u=Q(1,10);v=Q(1,5);p=v/(u+v);n=9
 ck(f'pure_target_cost_{law}',sum(co(r,u,v,j)[0] for j in range(n))==1+p*(1-(1-u)**(n-1))/u)
# A direct nonrenewal counterexample: frozen chain bit, target input. First attempt
# succeeds with p, but failure reveals bad bit forever, so infinite retries have
# positive probability of never succeeding. Geometric C/p formula would be finite.
frozen= S.Matrix([[1,0],[0,1]]); reject=S.diag(0,1); initial=S.Matrix([[Q(2,3),Q(1,3)]])
tails=[(initial*(frozen*reject)**n*S.ones(2,1))[0] for n in range(1,5)]
ctrl('stationary_marginals_not_renewal',tails==[Q(1,3)]*4 and 1+sum(tails[:3])>Q(3,2))

deps=['lab/process/k2486-noisy-flag-alternating-verifier.json','tests/channel-swings/k2486_noisy_flag_alternating_verifier_probe.py','lab/process/k2484-coherent-verifier-instruments.json']
report={'result':'K2488','scope':'stationary classical Markov flag errors independent of input; ideal coherent Q/T control and storage','checks':checks,'contrary_controls':controls,'fixtures':fixtures,'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps},'evidence_kinds':{'universal':'written word-effect, phase, spacing, monotonicity and ratio proof','finite':'exact symbolic and rational selective-instrument controls','inherited':'original 108 carrier ranks authenticated, not reconstructed'}}
p=R/'lab/process/k2488-markov-flag-filtering.json'
if '--write' in sys.argv:p.write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
else:ck('saved_reproduction',json.loads(p.read_text())==report)
print(json.dumps({'result':'PASS','checks':len(checks),'controls':len(controls),'fixtures':[{k:v for k,v in f.items() if k not in ['sharp_error','worst_renewal_cost','target_yield_lower']} for f in fixtures]}))
