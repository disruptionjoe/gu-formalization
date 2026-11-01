from pathlib import Path
from itertools import product,combinations
import ast,json,hashlib,sys
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
src=ROOT/'tests/channel-swings/k2439_minimal_flagged_tomography_probe.py'
I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1);phi=s.Matrix([1,0,0,1])/s.sqrt(2);Phi=phi*phi.H
for node in ast.parse(src.read_text()).body:
 if isinstance(node,ast.FunctionDef) and node.name in {'simp','ptr','choi','psd','dist','law_data','instrument'}:exec(compile(ast.Module(body=[node],type_ignores=[]),str(src),'exec'),globals())

# Direct full matrices for three temporal depths, plus qutrit control.
fixtures=[]
for d,r in [(2,1),(2,2),(2,3),(3,2)]:
 size=d**(2*r);prev=size//d;v=s.zeros(prev,1)
 for ix in product(range(d),repeat=2*r-1):
  if ix[0]==0 and all(ix[2*j-1]==ix[2*j] for j in range(1,r)):
   idx=0
   for z in ix:idx=idx*d+z
   v[idx]=d**(-s.Rational(r-1,2))
 V=v*v.H;L=s.kronecker_product(v.H,s.eye(d))/s.sqrt(d);z=s.diag(-1,1,*([0]*(d-2)))
 H=s.kronecker_product(V,z);q=Q(1,d**(2*r));lam=Q(1,d);C=d**(2*r-1);alpha=Q(1,C)
 ck(f'v_normalized_{d}_{r}',(v.H*v)[0]==1)
 ck(f'scaled_success_effect_{d}_{r}',simp(L*L.H)==lam*s.eye(d))
 ck(f'zero_final_partial_trace_{d}_{r}',all(sum(H[d*i+b,d*j+b] for b in range(d))==0 for i,j in product(range(prev),repeat=2)))
 ck(f'sharp_forward_image_{d}_{r}',simp(L*H*L.H)==lam*z)
 sig=s.kronecker_product(s.eye(prev)/prev,s.diag(1,*([0]*(d-1))))
 for u in [alpha/5,alpha/2,alpha]:
  rho=sig+u*H;out=simp(L*rho*L.H)
  # Positivity is exact decomposition on V and its orthogonal complement.
  eigsmall=s.diag(alpha-u,u,*([0]*(d-2)))
  ck(f'positive_decomposition_{d}_{r}_{u}',all(x>=0 for x in eigsmall.diagonal()) and simp(rho-s.kronecker_product(s.eye(prev)-V,s.diag(alpha,*([0]*(d-1))))-s.kronecker_product(V,eigsmall))==s.zeros(size))
  ck(f'success_q_{d}_{r}_{u}',s.trace(out)==q)
  ck(f'normalized_sharp_error_{d}_{r}_{u}',dist(out/q-s.diag(1,*([0]*(d-1))))==C*u)
 fixtures.append({'d':d,'slots':r,'q':str(q),'lambda':str(lam),'C':C,'global_saturation_distance':str(alpha)})
# Positive classical mass controls in both trace orders, plus coherent output.
for p,t,s0,q0 in product([Q(1,5),Q(4,5)],[Q(1,7),Q(6,7)],[Q(1,8),Q(1,3)],[Q(1,7),Q(1,2)]):
 A=s0*s.diag(p,1-p);B=q0*s.diag(t,1-t)
 ck(f'mass_inequality_{p}_{t}_{s0}_{q0}',2*max(s0,q0)*dist(A/s0-B/q0)<=sum(abs(x) for x in (A-B).diagonal())+abs(s0-q0))
A=Q(1,8)*s.Matrix([[Q(1,2),s.I/4],[-s.I/4,Q(1,2)]]);B=Q(1,6)*s.diag(1,0)
ck('coherent_mass_inequality',2*Q(1,6)*dist(A/s.trace(A)-B/s.trace(B))<=2*dist(A-B)+abs(s.trace(A)-s.trace(B)))
e=Q(1,100);q=Q(1,4);ctrl('q_plus_error_denominator_rejected',e/q>e/(q+e))
ctrl('operation_error_cannot_scale',Q(1,100)/q>Q(1,2)*Q(1,100)/q)
means,weights,norms=law_data();orig=[]
for k,args in enumerate(zip(means,weights,norms)):
 B=instrument(*args);mu=min(B[1].eigenvals());v=s.kronecker_product(s.Matrix([1,0]),phi);H=s.kronecker_product(v*v.H,Z);L=s.kronecker_product(v.H,I)/s.sqrt(2);t=mu**2/2
 ck(f'original_CP_TP_{k}',all(psd(b) for b in B) and sum((ptr(b) for b in B),s.zeros(2))==I/2)
 ck(f'original_fullrank_plus_window_{k}',mu>0 and t<mu**2)
 ck(f'original_two_slot_sharp_slope_{k}',dist(16*L*(t*H)*L.H)==8*dist(t*H))
 orig.append({'law':k,'plus_minimum':str(mu),'positive_perturbation':str(t)})
tau=Q(1,100);kap=Q(1,10**6);q=Q(1,16);lam=Q(1,2);new=(tau*q-kap)/lam;old=tau*q/(1+tau)-kap
ck('prospective_error_allowance',new==Q(156,125000) and new>2*old)
ck('tomography_leading_cost_ratio',4<(new/old)**2<5)
evidence={'finite_exact':fixtures,'original_mixed_local':orig,'allowance':{'new':str(new),'old':str(old),'leading_tomography_ratio':str((new/old)**2)},'universal':'written scaled CP completion, two-mass normalization, all-r causal saturation; no novelty claim','ceilings':'predictable normalized mean only; operation error unscaled; global saturation not every fixed target'}

deps=['tests/channel-swings/k2444_sharp_heralded_transfer_probe.py', 'explorations/conditional-build/k2444-sharp-heralded-transfer-2026-11-01.md', 'tests/channel-swings/k2439_minimal_flagged_tomography_probe.py', 'lab/process/k2441-heralded-adaptive-batch.json', 'lab/process/k2442-replicated-process-distance.json']
report={'result_id':'K2444','checks':checks,'controls':controls,'evidence':evidence,'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2444-sharp-heralded-transfer.json'
if '--check' in sys.argv:assert json.loads(out.read_text())==report
else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('k2444-sharp-heralded-transfer',len(checks),'checks',len(controls),'controls PASS')
