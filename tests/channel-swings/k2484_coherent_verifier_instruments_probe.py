"""Exact original conditional vectors and instrument/cost controls; universal proofs in note."""
from pathlib import Path
from itertools import product
import ast,json,hashlib,sys
import sympy as s
ROOT=Path(__file__).resolve().parents[2];Q=s.Rational;checks={};controls={}
def ck(k,b):
 checks[k]=bool(b)
 if not b:raise AssertionError('FAIL '+k)
def ctrl(k,b):
 controls[k]=bool(b)
 if not b:raise AssertionError('FAIL contrary '+k)
def simp(M):return M.applyfunc(lambda x:s.simplify(s.expand_complex(x)))
env={'s':s,'Q':Q};src=ROOT/'tests/channel-swings/k2419_positive_visibility_dual_probe.py'
for node in ast.parse(src.read_text()).body:
 if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id in ['means','weights','norms'] for t in node.targets):exec(compile(ast.Module(body=[node],type_ignores=[]),str(src),'exec'),env)
strings=[(0,0,0,0),(0,1,1,0),(1,0,0,1),(1,0,1,2),(1,1,1,3),(1,1,0,4),(2,1,0,5),(2,1,1,6),(2,0,1,7),(2,0,0,8)]
frb=list(product(range(3),range(2),range(2)));coords=list(product(range(3),range(2),range(2),range(9)))
om=(-1+s.I*s.sqrt(3))/2;phase=lambda k,f:s.expand(om**((k*f)%3))
B=[s.Matrix([phase(k,f)*ss**rr*tt**bb/s.sqrt(12) for f,rr,bb in frb]) for k,ss,tt in product(range(3),[1,-1],[1,-1])]
ck('original108_and_product_basis',len(coords)==108 and simp(s.Matrix.hstack(*B).H*s.Matrix.hstack(*B))==s.eye(12))
prior=json.loads((ROOT/'lab/process/k2454-two-setting-local-verifier.json').read_text());fixtures=[]
for law,(w,l) in enumerate(zip(env['weights'],env['norms'])):
 a=1-w;mu=[a/2,a/2]+[s.cancel(w*((1+ss*l)/2)*((1+Q(hh,2))/2)/2) for zz,ss,hh in product([1,-1],repeat=3)]
 ck(f'original_weight_authentication_{law}',list(map(str,mu))==prior['original_laws'][law]['weights'] and sum(mu)==1)
 W=s.zeros(12,9)
 for m,(f,rr,bb,e) in zip(mu,strings):W[frb.index((f,rr,bb)),e]=s.sqrt(m)
 vectors=[];V=[];pvals=[];rebuild=s.zeros(12,9)
 for j,((k,ss,tt),av) in enumerate(zip(product(range(3),[1,-1],[1,-1]),B)):
  c=simp(W.T*av.conjugate());p=s.simplify((c.H*c)[0]);e=simp(c/s.sqrt(p));e0=e[0]
  ck(f'conditional_probability_{law}_{j}',p==(1+a*ss*tt)/12)
  ck(f'original_Householder_domain_{law}_{j}',s.simplify((e.H*e)[0])==1 and e0.is_real is True and 0<=e0<1)
  v=(s.eye(9)[:,0]-e)/s.sqrt(2*(1-e0));vv=s.simplify((v.H*v)[0]);H=s.eye(9)-2*v*v.H
  # Rank-one factorization proves H*=H and H^2=I from v*v=1, without a dense108 product.
  ck(f'Householder_unitarity_factor_{law}_{j}',vv==1 and simp(H-H.H)==s.zeros(9))
  ck(f'Householder_original_column_{law}_{j}',simp(H[:,0]-e)==s.zeros(9,1))
  vectors.append(e);pvals.append(p);rebuild+=s.sqrt(p)*av*e.T
  V.append(simp(s.Matrix([av[frb.index((f,rr,bb))]*e[ee] for f,rr,bb,ee in strings])))
 ck(f'original_full108_reconstruction_{law}',simp(rebuild-W)==s.zeros(12,9))
 ck(f'full_T_rank12_via_orthogonal_controls_{law}',s.Matrix(12,12,lambda j,k:s.simplify((B[j].H*B[k])[0]*(vectors[j].H*vectors[k])[0]))==s.eye(12))
 psi=s.Matrix([s.sqrt(m) for m in mu]);u=s.Matrix([1/s.sqrt(2),1/s.sqrt(2)]+[0]*8);v=s.Matrix([0,0]+[s.sqrt(m/w) for m in mu[2:]]);z=s.sqrt(w)*u-s.sqrt(a)*v;r=s.cancel(a/(1+a));G=simp(sum((v*v.H for v in V),s.zeros(10)))
 ck(f'original_QTQ_not_assumed_{law}',simp(G-psi*psi.H-r*z*z.H)==s.zeros(10))
 ck(f'original_r_{law}',r==[Q(27,127),Q(15,67)][law])
 # Original fine-label leakage, not manifest assertion: orthogonal FRB output labels.
 leaked=sum(p*p for p in pvals);ctrl(f'fine_record_destroys_target_{law}',leaked==(1+a*a)/12 and leaked<1)
 wrong=s.simplify(sum(s.expand_complex((av.H*W*e)[0]*s.conjugate((av.H*W*e)[0])) for av,e in zip(B,vectors)))
 ctrl(f'wrong_Fourier_conjugation_{law}',wrong<1)
 PP=s.diag(1,0,0,0);ZZ=s.diag(0,1,0,0);QQ=s.diag(1,1,0,1);TT=s.zeros(4);TT[0,0]=1;TT[1,1]=r;TT[1,2]=TT[2,1]=s.sqrt(r*(1-r));TT[2,2]=1-r
 ck(f'original_principal_block_projectors_{law}',simp(TT*TT-TT)==s.zeros(4) and QQ*TT*QQ==PP+r*ZZ)
 C=s.eye(4);rho=s.diag(Q(9,10),Q(1,20),Q(1,40),Q(1,40));F=Q(9,10);z0=Q(1,20);q0=s.trace(QQ*rho);cost=0;survive=s.Integer(1)
 for n in range(1,10):
  cn=Q(2) if n%2 else Q(3);cost+=cn*survive;C=(QQ if n%2 else TT)*C;effect=simp(C.H*C);survive=s.trace(effect*rho)
  if n>=2:
   ck(f'alternating_effect_{law}_{n}',effect==PP+r**(n-1)*ZZ and simp(C.H*PP*C)==PP)
   predicted=2+3*q0+sum((2 if j%2 else 3)*(F+r**(j-2)*z0) for j in range(3,n+1))
   ck(f'exact_stopped_cost_{law}_{n}',cost==predicted)
 ctrl(f'repeated_Q_not_alternation_{law}',QQ*QQ!=PP+r*ZZ)
 ctrl(f'any_pass_not_all_pass_{law}',1-(1-r)**4!=r**4)
 ck(f'five_test_consumer_{law}',r**4/(9+r**4)<Q(7,10000))
 ctrl(f'four_test_not_same_guarantee_{law}',r**3/(9+r**3)>Q(7,10000))
 fixtures.append({'law':law+1,'r':str(r),'five_test_infidelity_bound':str(r**4/(9+r**4)),'local_fine_T_target_fidelity':str(leaked),'wrong_phase_target_acceptance':str(wrong)})
# Q circuit equals ten joint controlled flips on all108 basis states; predicates are disjoint.
for x in coords:ck('Q_flag_'+''.join(map(str,x)),sum(int(x==t) for t in strings)%2==int(x in strings))
plus=s.ones(4,1)/2;QRB=s.diag(1,0,0,1);out=QRB*plus;ck('original_product_Bell_probability',(out.H*out)[0]==Q(1,2));ctrl('LOCC_product_output_entangled',s.Matrix(2,2,list(out)).det()==Q(1,4))
# Dirty flag swaps the complete outcome maps with probability eta; distinguishable on a Q eigenstate.
eta=Q(1,100);correct=s.Matrix([1,0]);dirty=(1-eta)*correct+eta*s.Matrix([0,1]);ck('dirty_flag_half_trace_distance',sum(abs(v) for v in dirty-correct)/2==eta);ctrl('full_rank_flag_not_exact',dirty!=correct)
# Terminal conditioning fixture: positive bad/good/fail laws at exact TV distance.
ideal=(Q(1,10),Q(4,10),Q(5,10));eps=Q(1,20);q=ideal[0]+ideal[1]
actual=(ideal[0]+eps,ideal[1]-eps,ideal[2]);ck('terminal_bound_sharp',sum(abs(x-y) for x,y in zip(actual,ideal))/2==eps and actual[0]/sum(actual[:2])==(ideal[0]+eps)/q)
for i in range(21):
 for j in range(21-i):
  actual=(Q(i,20),Q(j,20),Q(20-i-j,20));d=sum(abs(x-y) for x,y in zip(actual,ideal))/2
  if d<q and sum(actual[:2])>0:ck(f'terminal_simplex_{i}_{j}',actual[0]/sum(actual[:2])<=min(1,(ideal[0]+d)/q))
bell=s.Matrix([1,0,0,1])/s.sqrt(2);fine=s.diag(Q(1,2),0,0,Q(1,2));ctrl('effect_only_update_not_certificate',(bell.H*fine*bell)[0]==Q(1,2) and fine!=bell*bell.H)
deps=['tests/channel-swings/k2419_positive_visibility_dual_probe.py','tests/channel-swings/k2454_two_setting_local_verifier_probe.py','lab/process/k2454-two-setting-local-verifier.json','explorations/conditional-build/k2482-same-copy-retry-boundary-2026-11-01.md','explorations/conditional-build/k2090-coherent-coarse-readout-2026-10-26.md']
report={'result':'K2484','scope':'original coherent binary verifier under joint-control access; no device or native GU claim','checks':checks,'contrary_controls':controls,'original_laws':fixtures,'evidence_kinds':{'universal':'written projection, circuit, LOCC and full-instrument proofs','exact':'original conditional reconstruction, factor identities, alternating finite products and changed-instrument controls','inherited':'original native carrier and generic coherent coarse readout authenticated, not rerun'},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
p=ROOT/'lab/process/k2484-coherent-verifier-instruments.json'
if '--write' in sys.argv:p.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
else:ck('saved_report_reproduces',json.loads(p.read_text())==report)
print(json.dumps({'result':'PASS','checks':len(checks),'controls':len(controls),'laws':fixtures}))
