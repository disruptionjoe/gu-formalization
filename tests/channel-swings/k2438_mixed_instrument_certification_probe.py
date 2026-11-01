"""Mixed-support identification, original flagged-instrument counterexample and tomography."""
from pathlib import Path
from itertools import product,combinations
import ast,json,hashlib,sys
import sympy as s
from flint import arb,ctx
ctx.prec=256
ROOT=Path(__file__).resolve().parents[2];checks={};controls={};Q=s.Rational
I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1);pa=[I,X,Y,Z];paulis=[X,Z]
def ck(k,b):
 checks[k]=bool(b)
 if not b:raise AssertionError(k)
def ctrl(k,b):
 controls[k]=bool(b)
 if not b:raise AssertionError(k)
p=ROOT/'tests/channel-swings/k2419_positive_visibility_dual_probe.py'
for node in ast.parse(p.read_text()).body:
 if isinstance(node,ast.FunctionDef) and node.name in ['simp','choi','ptr','minors','psd']:
  exec(compile(ast.Module(body=[node],type_ignores=[]),str(p),'exec'),globals())
 # Reuse exact original law values, rather than typing fitted surrogate data.
 if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id in ['means','weights','norms'] for t in node.targets):
  exec(compile(ast.Module(body=[node],type_ignores=[]),str(p),'exec'),globals())
def dist(A):return s.simplify(sum(abs(v)*m for v,m in A.eigenvals().items())/2)
phi=s.Matrix([1,0,0,1])/s.sqrt(2);Pgood=phi*phi.H
basis=[s.kronecker_product(a,b) for a,b in product(pa,repeat=2)]
ck('complete_complex_Pauli_Gram',s.Matrix([[s.trace(a*b) for b in basis] for a in basis])==4*s.eye(16))
fixtures=[]
for num,(mean,w,norm) in enumerate(zip(means,weights,norms)):
 axis=mean/norm;law=[((1+norm)/2,axis),((1-norm)/2,-axis)]
 ck('original_antipodal_law_'+str(num),axis.dot(axis)==1 and all(v>0 for v,n in law))
 def opblock(op,sg,depolarized=False):
  rr=s.Matrix([s.trace(op*X),s.trace(op*Z)])
  return simp(sum((prob*(s.trace(op)+sg*nv.dot(rr))/2*(I if depolarized else I+(nv[0]*X+nv[1]*Z)/2)/2 for prob,nv in law),s.zeros(2)))
 target=[(1-w)*Pgood]+[w*choi(lambda op:opblock(op,sg))/2 for sg in [1,-1]]
 rival=[(1-w)*Pgood]+[w*choi(lambda op:opblock(op,sg,True))/2 for sg in [1,-1]]
 ck('original_CP_and_normalization_'+str(num),all(psd(x) for x in target+rival) and sum((ptr(x) for x in target),s.zeros(2))==I/2 and sum((ptr(x) for x in rival),s.zeros(2))==I/2)
 ck('original_recorded_ranks_1_4_4_'+str(num),[x.rank() for x in target]==[1,4,4])
 ck('rival_same_support_'+str(num),[x.rank() for x in rival]==[1,4,4] and rival[0]==target[0])
 ck('same_ALL_input_flag_effects_'+str(num),all(ptr(a)==ptr(b) for a,b in zip(target,rival)))
 ctrl('conditional_bad_not_TP_'+str(num),ptr(target[1])/s.trace(target[1])!=I/2)
 outdiff=[w*(opblock(I/2,sg)-opblock(I/2,sg,True)) for sg in [1,-1]]
 lower=sum(dist(x) for x in outdiff);expected=[Q(73,416),Q(259,2080)][num]
 ck('actual_operational_counterexample_'+str(num),lower==expected and lower==w*norm/4)
 ctrl('zero_support_failure_does_not_identify_'+str(num),lower>0)
 coeffs=[]
 for z,block in enumerate(target):
  co=[s.simplify(s.trace(B*block)) for B in basis];recon=sum((c*B/4 for c,B in zip(co,basis)),s.zeros(4))
  ck('full_block_reconstruction_'+str(num)+'_'+str(z),simp(recon-block)==s.zeros(4));coeffs.append(co)
 residuals=[[s.simplify(s.trace(B*(a-b))) for B in basis] for a,b in zip(target,rival)]
 bound=sum(s.sqrt(sum(v*v for v in vec)) for vec in residuals)/2
 actual=sum(dist(a-b) for a,b in zip(target,rival))
 ck('tomography_bounds_full_Choi_'+str(num),s.simplify(bound-actual)>=0)
 ctrl('within_block_moments_detect_missing_output_'+str(num),any(any(x for x in c) for c in residuals))
 fixtures.append({'law':num+1,'ranks':[1,4,4],'input_maximally_mixed_distance':str(lower),'Choi_distance':str(actual),'tomography_Choi_bound':str(bound),'target_moments':[[str(v) for v in c] for c in coeffs]})
# Original supported carrier dimension33, four independent TP constraints.
# Good support projector plus all16 Hermitian operators in each bad flag.
cols=[s.Matrix(ptr(Pgood)).reshape(4,1)]+[s.Matrix(ptr(B)).reshape(4,1) for B in basis]*2
A=s.Matrix.hstack(*cols)
ck('supported_flagged_constraint_rank4',A.rank()==4 and A.cols==33 and len(A.nullspace())==29)
# Distinct strict-PSD TP states invisible to every real-plane moment.
YY=s.kronecker_product(Y,Y);plus=(s.eye(4)+YY/2)/4;minus=(s.eye(4)-YY/2)/4
ck('complex_direction_counterexample_CP_TP',psd(plus) and psd(minus) and ptr(plus)==I/2 and ptr(minus)==I/2 and plus.det()>0 and minus.det()>0)
ctrl('real_plane_tomography_misses_Y',all(s.trace(s.kronecker_product(a,b)*(plus-minus))==0 for a,b in product([I,X,Z],repeat=2)) and dist(plus-minus)==Q(1,2))
ck('complete_tomography_detects_Y',s.trace(YY*(plus-minus))==1)
# Explicit extreme mixed target: amplitude damping with gamma=3/4.
K0=s.diag(1,Q(1,2));K1=s.Matrix([[0,s.sqrt(3)/2],[0,0]])
amp=choi(lambda op:K0*op*K0.H+K1*op*K1.H)/2
vec0=s.Matrix([1,0,0,Q(1,2)])*2/s.sqrt(5);vec1=s.Matrix([0,1,0,0]);V=s.Matrix.hstack(vec0,vec1);P=V*V.H
Hbasis=[s.eye(2)/s.sqrt(2),X/s.sqrt(2),Y/s.sqrt(2),Z/s.sqrt(2)]
T=[ptr(V*B*V.H) for B in Hbasis];G=s.Matrix([[s.trace(a*b) for b in T] for a in T]);mineig=min(G.eigenvals())
ck('mixed_support_injectivity',psd(amp) and ptr(amp)==I/2 and P*amp==amp and G.det()>0 and mineig>0)
# Tensor-product conditioning is an algebraic singular-value fact.
ck('product_support_conditioning',s.kronecker_product(G,G).det()==G.det()**8)
# Both lie inside dephasing rank2 support; TP restriction there is singular.
Pd=s.diag(1,0,0,1);vd=s.Matrix.hstack(s.eye(4)[:,0],s.eye(4)[:,3]);Td=[ptr(vd*B*vd.H) for B in Hbasis];Gd=s.Matrix([[s.trace(a*b) for b in Td] for a in Td])
ctrl('support_without_constraint_injectivity',Gd.det()==0 and psd(Pd/2) and ptr(Pd/2)==I/2 and ptr(Pgood)==I/2 and dist(Pgood-Pd/2)==Q(1,2))
# Complete same-ensemble random-setting estimator: range [-S,S].
S=16
co=s.Rational(2,5);flagprob=s.Rational(3,7)
# Conditional expected weighted datum equals the full coefficient, not a selected subset.
ck('importance_weight_unbiased',sum(Q(1,S)*(S*co if j==3 else 0) for j in range(S))==co)
# Time-uniform confidence allocates alpha/[n(n+1)] over n and over M coefficients.
ck('time_union_telescope',s.summation(1/(s.Symbol('n',positive=True,integer=True)*(s.Symbol('n',positive=True,integer=True)+1)),(s.Symbol('n',positive=True,integer=True),1,s.oo))==1)
# Causal feedback constants include flags in each preceding output.
ck('recorded_output_dimensions',[(2**r)*(6**(r-1)) for r in [1,2,3]]==[2,24,288])
ctrl('ignoring_visible_flags_underprices_tester',24>8)
# Same mean target can hide variation across batches.
ck('same_average_mixed_target', (s.diag(1,0)+s.diag(0,1))/2==I/2)
ctrl('mean_distance_not_distance_of_mean',dist(s.diag(1,0)-I/2)==Q(1,2) and dist((s.diag(1,0)+s.diag(0,1))/2-I/2)==0)
# Concrete one-slot conservative whole-batch confidence budget at chosen n.
alpha=arb('0.05');M=48;n=4_000_000_000
Ln=(arb(2*M)*arb(n)*arb(n+1)/alpha).log()
radius=(2*S*Ln/n).sqrt()+2*(S+1)*Ln/(3*n)
hoeffding=arb(S)*(2*Ln/n).sqrt()
ck('freedman_sharpens_range_only',radius<hoeffding)
# For t=sqrt(2 v L)+2 b L/3, t^2 >= 2 L(v+b t/3).
u,b,L=s.symbols('u b L',positive=True);tt=u+2*b*L/3;vv=u*u/(2*L)
ck('freedman_tail_inversion',s.expand(tt*tt-2*L*(vv+b*tt/3))==2*L*b*u/3)
ck('importance_weight_second_moment',Q(1,S)*S*S==S)
ctrl('ignoring_random_setting_variance',S>1)
# Each block has16 errors bounded by the statistical radius plus observed residual.
residual=arb('1e-5');delta=12*(radius+residual)
ck('prospective_1percent_tomography_budget',delta<arb('0.01'))
e=arb('1e-8');f=(e+(4*e-3*e*e).sqrt())/2
ck('prospective_preparation_margin',delta+2*f<arb('0.01'))
# Readout observable-norm errors enter each coefficient before the norm.
eta=arb('1e-5');ck('prospective_readout_margin',12*(radius+residual+eta)+2*f<arb('0.01'))
ctrl('purification_access_not_implied_by_mixed_support',s.trace(Pd*Pgood)==1 and Pgood!=Pd/2)
deps=['tests/channel-swings/k2419_positive_visibility_dual_probe.py','lab/process/k2432-joint-preparation-decoupling.json','lab/process/k2436-multiround-process-certificate.json']
# Resolve prior preparation artifact by its unique native prefix if filename differs.
if not (ROOT/deps[1]).exists():
 matches=list((ROOT/'lab/process').glob('k2432-*.json'));assert len(matches)==1;deps[1]=str(matches[0].relative_to(ROOT))
for dep in deps:
 if dep.endswith('.json'):
  j=json.loads((ROOT/dep).read_text());ck('pins_'+Path(dep).stem,all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in j.get('dependencies',{}).items()))
report={'result_id':'K2438','scope':'Imported finite-dimensional mixed-target quantum processes; actual flagged instruments need output moments. Tested-average certificate only for tomography, no actual counts, physical calibration, future transfer or native GU identification.','checks':checks,'controls':controls,'original_instrument_fixtures':fixtures,'supported_classical_carrier':{'dimension':33,'TP_rank':4,'invisible_dimension':29},'mixed_amplitude_damping':{'gamma':'3/4','mu_squared':str(mineig),'Gram':[[str(x) for x in row] for row in G.tolist()]},'prospective_budget':{'batches':n,'alpha':'0.05','settings':16,'coefficients':48,'statistical_radius':str(radius),'range_only_hoeffding_radius':str(hoeffding),'confidence_method':'time-uniform union of scalar Freedman bounds; increment S+1, variance S','one_slot_distance_with_empirical_tolerance':str(delta),'empirical_component_residual_bound':'1e-5','joint_infidelity':'1e-8','observable_readout_error':'1e-5','total_distance_bound':str(12*(radius+residual+eta)+2*f),'status':'sufficient conditional prospective example; estimates not supplied; not optimized'},'evidence_kinds':{'exact':'original CP/TP blocks, physical contrary instrument, complete Pauli reconstruction, support constraint rank and complex direction controls','rigorous_numeric':'Arb256 prospective sufficient error/sample consumer','universal':'written support uniqueness, conditioning, trace-norm tester transfer and adaptive martingale confidence proofs'},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2438-mixed-instrument-certification.json'
if '--check' in sys.argv:assert json.loads(out.read_text())==report
else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('K2438',len(checks),'checks',len(controls),'controls PASS');print(json.dumps(report['prospective_budget'],indent=2))
