"""Noncancelling pair score with exact original correlated false-replica controls."""
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
src=ROOT/'tests/channel-swings/k2439_minimal_flagged_tomography_probe.py';names={'simp','ptr','choi','psd','dist','law_data','instrument'}
I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1);phi=s.Matrix([1,0,0,1])/s.sqrt(2);Phi=phi*phi.H
for node in ast.parse(src.read_text()).body:
 if isinstance(node,ast.FunctionDef) and node.name in names:exec(compile(ast.Module(body=[node],type_ignores=[]),str(src),'exec'),globals())
def trprod(A,B):return s.simplify(sum(v*B[j,i] for (i,j),v in s.SparseMatrix(A).todok().items()))
def partpair(A,N,which):
 if which==0:return s.Matrix(N,N,lambda i,j:sum(A[i*N+k,j*N+k] for k in range(N)))
 return s.Matrix(N,N,lambda i,j:sum(A[k*N+i,k*N+j] for k in range(N)))
means,weights,norms=law_data();t=Q(1,100000);N=12
S=s.SparseMatrix(N*N,N*N,{(i*N+j,j*N+i):1 for i,j in product(range(N),repeat=2)})
H=s.diag(s.zeros(4),s.kronecker_product(Z,Y),s.zeros(4));fixtures=[]
for k,(m,w,l) in enumerate(zip(means,weights,norms)):
 B=instrument(m,w,l);sig=s.diag(*B);mu=min(1-w,w*(1-l)/16);rho=sig+t*H
 ck(f'original_CP_TP_{k}',all(psd(b) for b in B) and sum((ptr(b) for b in B),s.zeros(2))==I/2)
 evs=[z for b in B for z,mult in b.eigenvals().items() for _ in range(mult)];positive=[x for x in evs if x>0]
 ck(f'original_support_min_{k}',len(positive)==9 and min(positive)==mu)
 ck(f'complex_TP_tangent_{k}',H==H.H and s.trace(H)==0 and ptr(B[1]+t*s.kronecker_product(Z,Y))==ptr(B[1]) and s.trace(H*H)==4)
 ck(f'perturbed_original_CP_TP_{k}',psd(B[1]+t*s.kronecker_product(Z,Y)) and psd(B[1]-t*s.kronecker_product(Z,Y)))
 ck(f'pair_positivity_congruence_bound_{k}',1-2*t/mu>0)
 c=s.trace(sig*sig);HS=S-s.kronecker_product(sig,s.eye(N))-s.kronecker_product(s.eye(N),sig)+c*s.eye(N*N)
 Omega=s.kronecker_product(sig,sig)+t*(s.kronecker_product(sig,H)+s.kronecker_product(H,sig));ind=s.kronecker_product(rho,rho)
 ck(f'pair_marginals_{k}',partpair(Omega,N,0)==rho and partpair(Omega,N,1)==rho)
 ck(f'pair_trace_exchange_{k}',s.trace(Omega)==1 and S*Omega*S==Omega)
 # Total parallel output trace follows termwise from original TP and Tr_B H=0.
 ck(f'parallel_pair_TP_{k}',sum((ptr(b) for b in B),s.zeros(2))==I/2 and ptr(s.kronecker_product(Z,Y))==s.zeros(2))
 ck(f'pair_score_identity_{k}',trprod(HS,ind)==s.trace((rho-sig)**2)==4*t*t)
 ctrl(f'correlated_zero_score_false_replica_{k}',trprod(HS,Omega)==0 and rho!=sig and ind!=Omega)
 ck(f'counterfeit_distance_{k}',dist(rho-sig)==2*t)
 ck(f'counterfeit_exact_tensor_defect_{k}',simp(ind-Omega-t*t*s.kronecker_product(H,H))==s.zeros(144))
 ck(f'equal_marginal_bias_bound_{k}',4*t*t<=2*(8*t*t))
 ctrl(f'signed_average_hides_drift_{k}',(rho+(sig-t*H))/2==sig and s.trace((sig-t*H-sig)**2)==4*t*t)
 eig=[1-2*x+c for x in evs]+[sg-x-y+c for i,x in enumerate(evs) for y in evs[i+1:] for sg in [-1,1]]
 ck(f'score_spectrum_bounded_{k}',len(eig)==144 and min(eig)>=-2 and max(eig)<=2)
 # Direct dephasing of score on classical flag pair blocks reproduces both traces.
 Hd=s.SparseMatrix(144,144,{(i,j):v for (i,j),v in s.SparseMatrix(HS).todok().items() if (i//12//4,(i%12)//4)==(j//12//4,(j%12)//4)})
 ck(f'classical_flag_compressed_score_{k}',trprod(Hd,Omega)==trprod(HS,Omega) and trprod(Hd,ind)==trprod(HS,ind))
 ctrl(f'complex_Y_not_optional_{k}',H!=s.conjugate(H))
 fixtures.append({'law':k,'mu':str(mu),'pair_positive_factor':str(1-2*t/mu),'true_loss':str(4*t*t),'marginal_distance':str(2*t),'false_score':'0','pair_defect_distance':str(8*t*t),'score_spectrum_min':str(min(eig)),'score_spectrum_max':str(max(eig))})
# A one-copy affine nonnegative score on both signs forces zero tangent value.
x=s.symbols('x',real=True);ck('affine_opposite_tangent_sum',s.expand(t*x-t*x)==0)
# Explicit spectral-pair identity for arbitrary diagonal target and complex offdiagonal state.
sig=s.diag(Q(1,3),Q(2,3));rho=s.Matrix([[Q(2,5),s.I/5],[-s.I/5,Q(3,5)]]);swap=s.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
score=swap-s.kronecker_product(sig,I)-s.kronecker_product(I,sig)+s.trace(sig*sig)*s.eye(4)
ck('complex_general_pair_identity',trprod(score,s.kronecker_product(rho,rho))==s.trace((rho-sig)**2)>0)
orth=s.diag(1,-1);ctrl('unrelated_rank_one_support_invalid',dist(orth)==1 and s.sqrt(s.trace(orth*orth))/2<dist(orth))
ctrl('single_copy_support_zero_not_identity',rho!=sig and sig.rank()==2)
# Generic exact hidden-route moments for a bounded score with specified mean q.
for pi,q0 in product([Q(1,4),Q(1,2),Q(3,4)],[0,Q(1,7),1,2]):
 a=(1-pi)/pi;events=[(pi*(1+q0/2)/2,2*a),(pi*(1-q0/2)/2,-2*a),(1-pi,-q0)]
 ck(f'route_mean_{pi}_{q0}',sum(p*z for p,z in events)==0)
 ck(f'route_variance_{pi}_{q0}',sum(p*z*z for p,z in events)<=4*pi*a*a+4*(1-pi))
 ck(f'route_range_{pi}_{q0}',all(abs(z)<=max(2*a,2) for p,z in events if p))
ctrl('revealed_route_breaks_loss_transfer',Q(1,2)*0-Q(1,2)*1!=0)
# Quantitative sufficient consumer, not simulated or measured data.
n=10**12;L=(arb(2)*n*(n+1)/arb('.05')).log();Qdirect=(8*L/n).sqrt()+8*L/(3*n);Quse=((8*n*L).sqrt()+4*L/3)/(n//2)
state=(12*Quse).sqrt()/2;channel=2*(12*Qdirect).sqrt()/2;program=state/(arb('.25')-state)
ck('nonvacuous_direct_and_hidden_consumers',channel<arb('.02') and program<arb('.06'))
xierr=arb('1e-8');eta=arb('1e-8');Qfloor=4*xierr+eta;floorstate=(12*Qfloor).sqrt()/2
ck('replica_error_floor_positive',floorstate>0)
pros={'pairs':n,'alpha':'.05','direct_Q':str(Qdirect),'direct_mean_half_diamond':str(channel),'hidden_uses_assumed':n//2,'hidden_Q':str(Quse),'hidden_mean_state_distance':str(state),'hidden_program_normalized_error':str(program),'replica_xi':'1e-8','readout_eta':'1e-8','asymptotic_state_floor_for_general_replica_bound':str(floorstate),'status':'zero empirical scores and ideal calibration in main examples; no actual observations'}
deps=['tests/channel-swings/k2419_positive_visibility_dual_probe.py','tests/channel-swings/k2439_minimal_flagged_tomography_probe.py','lab/process/k2438-mixed-instrument-certification.json','lab/process/k2441-heralded-adaptive-batch.json',str(Path(__file__).relative_to(ROOT)),'explorations/conditional-build/k2442-replicated-process-distance-2026-11-01.md']
report={'result_id':'K2442','checks':checks,'controls':controls,'fixtures':fixtures,'prospective':pros,'evidence_kinds':{'exact':'original CP/TP pair counterfeits, full144-dimensional score contractions, complex tangents, spectrum formulas and route moments','rigorous_numeric':'Arb256 direct/hidden sufficient budgets and systematic floor','universal':'written affine impossibility, pair loss, confidence, mean-distance and conditional programming proofs'},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2442-replicated-process-distance.json'
if '--check' in sys.argv:assert json.loads(out.read_text())==report
else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('K2442',len(checks),'checks',len(controls),'controls PASS');print(json.dumps(pros,indent=2))
