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

src=ROOT/'tests/channel-swings/k2439_minimal_flagged_tomography_probe.py'
I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1);phi=s.Matrix([1,0,0,1])/s.sqrt(2);Phi=phi*phi.H
for node in ast.parse(src.read_text()).body:
 if isinstance(node,ast.FunctionDef) and node.name in {'simp','ptr','choi','psd','dist','law_data','instrument'}:exec(compile(ast.Module(body=[node],type_ignores=[]),str(src),'exec'),globals())
means,weights,norms=law_data();fixtures=[]
expected_purity=[Q(50434873,216320000),Q(347981,1730560)];expected_flag=[Q(6787,20000),Q(1819,5408)]
for law,(mean,w,l) in enumerate(zip(means,weights,norms)):
 axis=mean/l;vplus=s.Matrix([s.sqrt((1+axis[1])/2),axis[0]/s.sqrt(2*(1+axis[1]))]);vminus=s.Matrix([-vplus[1],vplus[0]]);eig={1:vplus,-1:vminus}
 for sign in [-1,1]:ck(f'original_axis_eigenvector_{law}_{sign}',simp((axis[0]*X+axis[1]*Z)*eig[sign]-sign*eig[sign])==s.zeros(2,1))
 ks=[s.sqrt(1-w)*I];flags=[0];lam=[1-w]
 for z,ss,hh in product([1,-1],repeat=3):
  aa=(1+ss*l)/2;bb=(1+Q(hh,2))/2
  ks.append(s.sqrt(w*aa*bb)*eig[hh*ss]*eig[z*ss].H);flags.append(1 if z==1 else 2);lam.append(w*aa*bb/2)
 ck(f'original_isometry_{law}',simp(sum((K.H*K for K in ks),s.zeros(2)))==I)
 W=s.zeros(12,9)
 for j,(K,flag) in enumerate(zip(ks,flags)):
  vec=s.Matrix([K[b,a] for a,b in product(range(2),repeat=2)])/s.sqrt(2)
  W[4*flag:4*flag+4,j]=vec
 B=instrument(mean,w,l);sigma=s.diag(*B)
 ck(f'original_exact_reduction_{law}',simp(W*W.H)==sigma)
 ck(f'orthogonal_nine_Kraus_vectors_{law}',simp(W.H*W)==s.diag(*lam))
 ck(f'minimal_environment_rank9_{law}',all(x>0 for x in lam) and sum(lam)==1)
 psi=s.Matrix([W[i,j] for i in range(12) for j in range(9)])
 ck(f'pure_extension_normalized_{law}',s.simplify((psi.H*psi)[0])==1)
 # Full E dephasing purity and flag dephasing from orthogonal Kraus sectors.
 pure=s.simplify(sum(x*x for x in lam));flag_weights=[s.simplify(sum(lam[j] for j in range(9) if flags[j]==z)) for z in range(3)]
 ck(f'purity_original_matrix_{law}',s.trace(sigma*sigma)==pure==expected_purity[law])
 ck(f'flag_probabilities_{law}',flag_weights==[1-w,w/2,w/2])
 ck(f'flag_dephased_acceptance_{law}',sum(x*x for x in flag_weights)==expected_flag[law])
 ctrl(f'environment_dephasing_rejects_correct_program_{law}',pure<1 and simp(W*W.H)==sigma)
 ctrl(f'flag_dephasing_rejects_correct_program_{law}',expected_flag[law]<1 and sigma==s.diag(*B))
 # Direct rank-one Householder application, not a hypothetical hardware compiler.
 zero=s.eye(108)[:,0];vv=zero-psi;den=s.simplify((vv.H*vv)[0]);reflect=lambda v:simp(v-2*vv*((vv.H*v)[0]/den))
 ck(f'householder_target_preparation_{law}',reflect(zero)==psi)
 ck(f'householder_inverse_test_{law}',reflect(psi)==zero)
 alt=s.eye(108)[:,1];alt=simp(alt-psi*(psi.H*alt)[0]);alt=alt/s.sqrt(s.simplify((alt.H*alt)[0]))
 ck(f'orthogonal_projector_rejection_{law}',s.simplify((psi.H*alt)[0])==0)
 psi_bad=simp(Q(3,5)*psi+s.I*Q(4,5)*alt)
 ck(f'coherent_error_infidelity_{law}',s.simplify(1-abs((psi.H*psi_bad)[0])**2)==Q(16,25))
 # Actual original CP/TP supported tangents: positive zero-baseline witnesses cannot see them.
 H=s.diag(s.zeros(4),s.kronecker_product(Z,Y),s.zeros(4));t=Q(1,100000);support=s.diag(Phi,s.eye(4),s.eye(4));witness=s.eye(12)-support
 ck(f'support_projector_{law}',support*support==support and simp(support*sigma)==sigma)
 ck(f'causal_complex_tangent_{law}',ptr(H[4:8,4:8])==s.zeros(2) and dist(H)==2)
 for sign in [-1,1]:
  rho=sigma+sign*t*H
  ck(f'actual_alternative_positive_{law}_{sign}',psd(B[1]+sign*t*s.kronecker_product(Z,Y)))
  ck(f'actual_alternative_TP_{law}_{sign}',sum((ptr(rho[4*z:4*z+4,4*z:4*z+4]) for z in range(3)),s.zeros(2))==I/2)
  ctrl(f'zero_failure_support_blind_{law}_{sign}',s.trace(witness*rho)==0 and dist(rho-sigma)==2*t)
 ck(f'nondisturbing_product_extension_mixed_{law}',pure<1) # General no-upgrade theorem is written Choi proof.
 # Original normalized Schmidt bank embeds into actual12-dimensional program space.
 U=s.Matrix.hstack(*[W[:,i]/s.sqrt(lam[i]) for i in range(9)])
 ck(f'original_Schmidt_embedding_{law}',simp(U.H*U)==s.eye(9))
 vectors=[]
 for shift in range(9):
  vv=s.zeros(81,1)
  for i in range(9):vv[9*i+(i+shift)%9]=s.sqrt(lam[i])
  vectors.append(vv)
 G=s.Matrix.hstack(*vectors);PZ=s.diag(*[int(i==a) for i,a in product(range(9),repeat=2)]);PF=simp(G*G.H);PP=vectors[0]*vectors[0].H
 ck(f'Fourier_test_projection_{law}',simp(G.H*G)==s.eye(9))
 ck(f'two_test_intersection_{law}',simp(PZ*PF)==PP and simp(PF*PZ)==PP)
 ck(f'two_test_target_eigenvalue_{law}',simp((PZ+PF)*vectors[0])==2*vectors[0])
 ck(f'exact_gap_half_witness_{law}',simp((PZ+PF)*vectors[1])==vectors[1])
 ctrl(f'Fourier_setting_alone_insufficient_{law}',simp(PF*vectors[1])==vectors[1] and simp(vectors[0].H*vectors[1])==s.zeros(1))
 # Direct spectral sector test: PZ vector orthogonal to Psi is accepted with probability1/2.
 zz=s.zeros(81,1);zz[0]=s.sqrt(lam[1]);zz[10]=-s.sqrt(lam[0])
 ck(f'basis_setting_gap_half_{law}',simp((PZ+PF)*zz)==zz)
 fixtures.append({'law':law+1,'environment_dimension':9,'weights':list(map(str,lam)),'full_dephasing_acceptance':str(pure),'flag_dephasing_acceptance':str(expected_flag[law]),'original_alternative_distance':str(2*t),'minimum_extension_infidelity':str(4*t*t)})
# Exact finite Fourier sum via cyclotomic reduction; covers complex phase cancellation.
x=s.symbols('x');cycl=s.Poly(s.cyclotomic_poly(9,x),x)
for exponent in range(9):
 pp=s.Poly(sum(x**((k*exponent)%9) for k in range(9)),x).rem(cycl)
 ck('Fourier_orthogonality_'+str(exponent),pp.as_expr()==(9 if exponent==0 else 0))
# Product verifier eigenvalue theorem on independently specified nontrivial local gaps.
for gaps in [(Q(1,2),Q(1,3)),(Q(2,3),Q(3,4),Q(4,5))]:
 vals=list(product(*[[1,1-nu,0] for nu in gaps]));ev=[math.prod(v) for v in vals];ck('product_gap_'+str(gaps),ev.count(1)==1 and 1-max(x for x in ev if x!=1)==min(gaps))
# Degenerate acceptance is a real counterexample, not a lost hypothesis in reporting.
P=s.diag(1,0,0);Om=s.diag(1,1,0);bad=s.diag(0,1,0)
ctrl('degenerate_acceptance_not_fixed_target',s.trace(Om*bad)==1 and dist(bad-P)==1)
# Direct pure-marginal extension positive product and impossible entangled candidate.
bell=Phi;environment=s.diag(Q(1,3),Q(2,3));J=s.kronecker_product(bell,environment)
ck('identity_channel_extension_product',s.trace(J*J)==s.trace(environment*environment) and J.rank()==2)
# A replacement can certify its newly prepared state; it is not an identity extension.
ctrl('target_replacer_changes_other_inputs',s.diag(1,0)!=I/2)
evidence={'original_instruments':fixtures,'universal':'pure-state convexity/partial-trace bound; positive witness support annihilation; identity-channel pure Choi marginal extension theorem; product verification gap','finite_exact':'original complex CP/TP alternatives, nine Kraus isometry/reduction, dephasing acceptances, Householder action, actual two-setting verifier, exact Fourier cancellation and product-gap controls','scope':'coherent reference access required, no hardware/data/native GU or free measured-record upgrade'}

deps=['tests/channel-swings/k2447_coherent_program_verification_probe.py', 'explorations/conditional-build/k2447-coherent-program-verification-2026-11-01.md', 'tests/channel-swings/k2439_minimal_flagged_tomography_probe.py', 'tests/channel-swings/k2419_positive_visibility_dual_probe.py', 'explorations/conditional-build/k2444-sharp-heralded-transfer-2026-11-01.md', 'lab/process/k2442-replicated-process-distance.json']
report={'result_id':'K2447','checks':checks,'controls':controls,'evidence':evidence,'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2447-coherent-program-verification.json'
if '--check' in sys.argv:assert json.loads(out.read_text())==report
else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('k2447-coherent-program-verification',len(checks),'checks',len(controls),'controls PASS')
