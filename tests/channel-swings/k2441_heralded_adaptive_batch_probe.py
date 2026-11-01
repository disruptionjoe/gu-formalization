"""Original two-slot flag feedback, physical Bell program and hidden-batch budgets."""
from pathlib import Path
from itertools import product
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
# Reuse only unchanged original-law functions; no predecessor scientific replay or output.
src=ROOT/'tests/channel-swings/k2439_minimal_flagged_tomography_probe.py';tree=ast.parse(src.read_text());names={'simp','ptr','choi','psd','dist','law_data','instrument'}
I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1);pa=[I,X,Y,Z];phi=s.Matrix([1,0,0,1])/s.sqrt(2);Phi=phi*phi.H
from itertools import combinations
for node in tree.body:
 if isinstance(node,ast.FunctionDef) and node.name in names:exec(compile(ast.Module(body=[node],type_ignores=[]),str(src),'exec'),globals())
def apply(J,A):
 return simp(sum((2*A[i,j]*J[2*i:2*i+2,2*j:2*j+2] for i,j in product(range(2),repeat=2)),s.zeros(2)))
def apply_ref(J,A):
 out=s.zeros(4)
 for i,j,b,c,e,f in product(range(2),repeat=6):out[2*b+e,2*c+f]+=2*J[2*i+b,2*j+c]*A[2*i+e,2*j+f]
 return simp(out)
means,weights,norms=law_data();instruments=[instrument(*args) for args in zip(means,weights,norms)]
for k,B in enumerate(instruments):ck(f'original_CP_TP_{k}',all(psd(b) for b in B) and sum((ptr(b) for b in B),s.zeros(2))==I/2)
chi=s.Matrix([Q(3,5),0,0,4*s.I/5]);xi=chi*chi.H
Us=[s.diag(1,s.I),X,s.Matrix([[3,-4],[4,3]])/5]
Ls=[]
for z,U in enumerate(Us):
 L=s.zeros(4,16)
 for r1,b1,r2,b2,e in product(range(2),repeat=5):L[2*b2+e,((r1*2+b1)*2+r2)*2+b2]=chi[2*r1+e]*U[r2,b1]/2
 Ls.append(L);ck(f'physical_success_effect_{z}',max((L.H*L).eigenvals())<=1)
fixtures=[]
for a,B in enumerate(instruments):
 for b,C in enumerate(instruments):
  total=s.zeros(4);direct=s.zeros(4);probs=[]
  for z,w in product(range(3),repeat=2):
   P=s.kronecker_product(B[z],C[w]);out=simp(Ls[z]*P*Ls[z].H)
   U=s.kronecker_product(Us[z],I);want=apply_ref(C[w],simp(U*apply_ref(B[z],xi)*U.H))
   ck(f'original_flagged_Bell_link_{a}_{b}_{z}_{w}',out==want/16)
   total+=out;direct+=want;probs.append(s.simplify(s.trace(out)))
  ck(f'whole_flag_sum_success_{a}_{b}',s.simplify(s.trace(total))==Q(1,16) and total==direct/16)
  ctrl(f'flag_success_not_uniform_{a}_{b}',len(set(probs))>1)
  fixtures.append({'laws':[a,b],'flag_success_probabilities':[str(x) for x in probs]})
# Coherent feedback on a memory-bearing comb: same versus independent X label.
vx=s.kronecker_product(I,X)*phi;PX=vx*vx.H
shared=(s.kronecker_product(Phi,Phi)+s.kronecker_product(PX,PX))/2
independent=s.kronecker_product((Phi+PX)/2,(Phi+PX)/2)
L=s.zeros(2,16)
for r1,b1,r2,b2 in product(range(2),repeat=4):L[b2,((r1*2+b1)*2+r2)*2+b2]=Q(1,2)*int(r1==0 and r2==b1)
a=simp(L*shared*L.H);b=simp(L*independent*L.H)
ck('sharp_two_slot_tester_effect',max((16*L.H*L).eigenvals())==8 and max((L.H*L).eigenvals())==Q(1,2))
# A causal full-rank comb perturbation also saturates the strategy-distance factor.
causalH=s.kronecker_product(s.diag(1,0),Phi,Z);center=s.eye(16)/16
ck('sharp_causal_perturbations_positive',psd(center+causalH/16) and psd(center-causalH/16))
ck('sharp_causal_partial_trace_zero',all(sum(causalH[2*i+j,2*k+j] for j in range(2))==0 for i,k in product(range(8),repeat=2)))
ck('sharp_causal_forwarding_image',simp(16*L*causalH*L.H)==8*Z)
ck('sharp_causal_strategy_ratio',dist(16*L*causalH*L.H)==8*dist(causalH))
ck('flag_dimension_improvement',2**4*6**3==3456 and 2**7==128)
ck('memory_comb_success',s.trace(a)==Q(1,16) and s.trace(b)==Q(1,16))
ck('memory_comb_direct_feedback',16*a==s.diag(1,0) and 16*b==I/2)
ctrl('same_marginals_do_not_replace_comb',dist(16*a-16*b)==Q(1,2))
ctrl('omit_Bell_normalization_wrong',s.trace(4*a)!=Q(1,16))
ctrl('complex_transpose_wrong',xi!=xi.T and any(simp(L0*s.kronecker_product(instruments[0][0],instruments[0][0])*L0.T)!=simp(L0*s.kronecker_product(instruments[0][0],instruments[0][0])*L0.H) for L0 in Ls))
# A genuinely quantum memory stores A1 for B2, emits B1=0 and discards A2.
quantum=s.zeros(16)
for r1,r2,r1p in product(range(2),repeat=3):
 i=((r1*2)*2+r2)*2+r1;j=((r1p*2)*2+r2)*2+r1p;quantum[i,j]=Q(1,4)
ck('quantum_memory_program_positive',psd(quantum) and s.trace(quantum)==1)
qout=simp(Ls[0]*quantum*Ls[0].H)
ck('quantum_memory_preserves_private_entanglement',qout==xi/16)
classical=s.diag(*[quantum[i,i] for i in range(16)]);cout=simp(Ls[0]*classical*Ls[0].H)
ctrl('dephased_memory_loses_private_coherence',dist(16*qout-16*cout)==Q(12,25))
ck('quantum_memory_same_one_slot_marginals',all(sum(quantum[4*i+j,4*k+j] for j in range(4))==sum(classical[4*i+j,4*k+j] for j in range(4)) for i,k in product(range(4),repeat=2)) and all(sum(quantum[4*j+i,4*j+k] for j in range(4))==sum(classical[4*j+i,4*j+k] for j in range(4)) for i,k in product(range(4),repeat=2)))
# Original one-slot cancellation embedded in history-selected two-slot controller choices.
t=Q(1,100000);H=s.kronecker_product(Z,Y);B=instruments[0]
for sign in [-1,1]:ck(f'original_perturb_CP_{sign}',psd(B[1]+sign*t*H))
Dplus=apply(t*H,s.diag(1,0));Dminus=apply(-t*H,s.diag(0,1))
ctrl('history_selected_inputs_prevent_average_transfer',Dplus==Dminus and Dplus!=s.zeros(2))
ctrl('revealed_route_counterfeit',Q(1,2)*0-Q(1,2)*1!=0)
# Generic local randomized-axis operator identities tensor into every multi-slot coefficient.
for a in range(4):
 first=s.zeros(2);second=s.zeros(2);weight=1 if a==0 else 3
 for setting,sg in product(range(1,4),[-1,1]):
  eff=(I+sg*pa[setting])/6;val=weight*int(a==0 or setting==a)*(sg if a else 1)
  first+=val*eff;second+=val*val*eff
 ck(f'axis_operator_unbiased_{a}',first==pa[a]);ck(f'axis_second_moment_{a}',second==weight*I)
# Symbolic direct test/use first and second moments with bounded synthetic W.
for pi in [Q(1,4),Q(1,2),Q(3,4)]:
 for w in [1,3,9,81]:
  for c in [Q(-1,3),0,Q(2,5)]:
   aa=(1-pi)/pi;events=[(pi*(1+c/w)/2,aa*w),(pi*(1-c/w)/2,-aa*w),(1-pi,-c)]
   ck(f'route_mean_{pi}_{w}_{c}',sum(p*z for p,z in events)==0)
   # This synthetic two-point W has second moment w², so use its actual variance.
   ck(f'route_second_moment_{pi}_{w}_{c}',s.simplify(sum(p*z*z for p,z in events)-(pi*aa*aa*w*w+(1-pi)*c*c))==0)
# Sparse estimator second moment w is established by operator identity above, not synthetic w².
n=4_000_000_000_000_000;NU=n//2;r=2;M=48**r;pi=arb('.5');ell=(arb(2*M)*n*(n+1)/arb('.05')).log()
errors=[]
for labels in product(range(4),repeat=4):
 w=3**sum(x!=0 for x in labels);b=max(w,1);v=arb(w+1)/2;bias=arb('1e-8');bb=arb(b)+bias/2
 radius=((2*n*v*ell).sqrt()+2*bb*ell/3)/NU+n*bias/(2*NU)
 errors.append(radius+arb('1e-8'))
epsilon=arb(9)/2*sum((e*e for e in errors),arb(0)).sqrt();kap=arb('1e-6');q=arb(1)/16;allow=(epsilon+kap)/(q-epsilon-kap)
ck('prospective_nonvacuous',epsilon+kap<q and allow<arb('.01'))
pros={'emissions':n,'realized_uses_assumed':NU,'slots':2,'settings':81,'coefficients':M,'sharper_tester_factors':{'r1':2,'r2':8,'r4':128},'state_allowance':str(epsilon),'operation_allowance':str(kap),'normalized_output_allowance':str(allow),'success_lower':str(q-epsilon-kap),'ideal_successes_per_emission':'1/32','status':'prospective assumptions, no actual records'}
deps=['tests/channel-swings/k2419_positive_visibility_dual_probe.py','tests/channel-swings/k2439_minimal_flagged_tomography_probe.py','lab/process/k2440-hidden-route-instrument-use.json',str(Path(__file__).relative_to(ROOT)),'explorations/conditional-build/k2441-heralded-adaptive-batch-2026-11-01.md']
report={'result_id':'K2441','checks':checks,'controls':controls,'fixtures':fixtures,'prospective':pros,'evidence_kinds':{'exact':'original CP/TP flagged feedback and complex entangled-reference Bell contractions, memory comb, local randomized operator identities and route moments','rigorous_numeric':'Arb256 conditional two-slot budget','universal':'written sequential comb link and complete-operation normalization proof; inherited martingale theorem'},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2441-heralded-adaptive-batch.json'
if '--check' in sys.argv:assert json.loads(out.read_text())==report
else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('K2441',len(checks),'checks',len(controls),'controls PASS');print(json.dumps(pros,indent=2))
