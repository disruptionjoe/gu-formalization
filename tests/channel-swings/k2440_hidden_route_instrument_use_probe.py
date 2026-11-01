"""Hidden routing, actual Choi-program contraction, and conditional-average controls."""
from pathlib import Path
from itertools import product,combinations
import ast,json,hashlib,sys
import sympy as s
from flint import arb,ctx
ctx.prec=256
ROOT=Path(__file__).resolve().parents[2];Q=s.Rational;checks={};controls={}
I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1);pa=[I,X,Y,Z];phi=s.Matrix([1,0,0,1])/s.sqrt(2);Phi=phi*phi.H;basis=[s.kronecker_product(a,b) for a,b in product(pa,repeat=2)]
def ck(k,b):
 checks[k]=bool(b)
 if not b:raise AssertionError(k)
def ctrl(k,b):
 controls[k]=bool(b)
 if not b:raise AssertionError(k)
p=ROOT/'tests/channel-swings/k2439_minimal_flagged_tomography_probe.py'
for node in ast.parse(p.read_text()).body:
 if isinstance(node,ast.FunctionDef) and node.name in ['simp','ptr','choi','psd','dist','coeff','law_data','instrument']:exec(compile(ast.Module(body=[node],type_ignores=[]),str(p),'exec'),globals())
def teleport(J,xi):return simp(s.Matrix(2,2,lambda b,bp:sum(xi[i,j]*J[2*i+b,2*j+bp] for i,j in product(range(2),repeat=2))/2))
means,weights,norms=law_data();matrix_units=[s.eye(2)[:,i]*s.eye(2)[j,:] for i,j in product(range(2),repeat=2)];fixtures=[]
for k,(mean,w,n) in enumerate(zip(means,weights,norms)):
 B=instrument(mean,w,n);axis=mean/n
 def native(op,z):
  rr=s.Matrix([s.trace(op*X),s.trace(op*Z)]);return simp(w*sum((prob*(s.trace(op)+z*nv.dot(rr))/2*(I+(nv[0]*X+nv[1]*Z)/2)/2 for prob,nv in [((1+n)/2,axis),((1-n)/2,-axis)]),s.zeros(2)))
 for j,op in enumerate(matrix_units):
  expected=[(1-w)*op,native(op,1),native(op,-1)];ck(f'original_Bell_contraction_{k}_{j}',all(teleport(J,op)==out/4 for J,out in zip(B,expected)))
 xi=(I+Y/2+Z/3)/2;out=[teleport(J,xi) for J in B];ck(f'original_herald_success_{k}',sum(s.trace(o) for o in out)==Q(1,4) and all(psd(o) for o in out))
 ctrl(f'wrong_input_transpose_detected_{k}',teleport(B[0],xi.T)!=teleport(B[0],xi))
 fixtures.append({'law':k+1,'success':'1/4','complex_input':[[str(v) for v in row] for row in xi.tolist()]})
# An arbitrary channel cannot correct every Bell outcome with the bare Pauli.
K0=s.diag(1,Q(1,2));K1=s.Matrix([[0,s.sqrt(3)/2],[0,0]]);amp=lambda op:simp(K0*op*K0.H+K1*op*K1.H);Ja=choi(amp);xi=s.diag(1,0)
ck('noncovariant_channel_CP_TP',psd(Ja) and ptr(Ja)==I/2)
ctrl('all_Bell_outcome_Pauli_correction_false',X*amp(X*xi*X)*X!=amp(xi))
ck('chosen_Bell_outcome_still_exact',teleport(Ja,xi)==amp(xi)/4)
# Non-Choi actual program: success depends on input, normalization cannot be assumed1/4.
bad=s.kronecker_product(s.diag(1,0),I/2);ck('arbitrary_program_is_state',psd(bad) and s.trace(bad)==1)
ctrl('input_dependent_actual_success',s.trace(teleport(bad,s.diag(1,0)))==Q(1,2) and s.trace(teleport(bad,s.diag(0,1)))==0)
# Exact estimator enumeration for several pi,c,w. No simulated samples or iid premise.
for pi,c,w in product([Q(1,2),Q(1,3),Q(4,5)],[-Q(2,5),Q(0),Q(2,5)],[1,3,9]):
 wd=[(-w,(1-c)/(2*w)),(w,(1+c)/(2*w)),(0,1-Q(1,w))];distZ=[((1-pi)/pi*val,pi*pr) for val,pr in wd]+[(-c,1-pi)]
 b=max((1-pi)*w/pi,1);v=(1-pi)**2*w/pi+(1-pi)
 ck(f'route_moments_{pi}_{c}_{w}',sum(pr for z,pr in distZ)==1 and sum(z*pr for z,pr in distZ)==0 and sum(z*z*pr for z,pr in distZ)<=v and all(abs(z)<=b for z,pr in distZ))
pi=Q(1,2);ctest=1;cuse=-1;drift=(1-pi)*(ctest-cuse);ctrl('disclosed_route_breaks_martingale',drift==1)
# Analytic fixed-allocation variance/throughput tradeoff; not a random-count replacement.
rho,pi0=s.symbols('rho pi',positive=True)
ck('allocation_exact_square',s.factor(rho*rho/pi0+1/(1-pi0)-(rho+1)**2-(rho*(1-pi0)-pi0)**2/(pi0*(1-pi0)))==0)
ck('allocation_worst_weight9',9/Q(3,4)+1/Q(1,4)==16 and 9/Q(1,2)+1/Q(1,2)==20 and Q(1,4)*Q(1,4)==Q(1,16))
# Readout bias is over all rounds in predictable drift.
eta=Q(1,100);N=100;NU=10;ck('bias_normalization',Q(N)*(1-pi)*eta/NU==Q(1,20));ctrl('adding_eta_once_underprices_bias',Q(1,20)>eta)
u,b,L=s.symbols('u b L',positive=True);tt=u+2*b*L/3;vv=u*u/(2*L);ck('Freedman_inversion',s.expand(tt*tt-2*L*(vv+b*tt/3))==2*L*b*u/3)
zz=s.symbols('n',integer=True,positive=True);ck('all_time_union',s.summation(1/(zz*(zz+1)),(zz,1,s.oo))==1)
# Adaptive inputs reveal cancellation of two channels with exact target average.
P0=s.diag(1,0);P1=s.diag(0,1);Jx=choi(lambda op:X*op*X);Javg=(Phi+Jx)/2
ck('same_program_average_target',ptr(Javg)==I/2 and psd(Javg))
actual=(P0+X*P1*X)/2;nominal=((P0+X*P0*X)/2+(P1+X*P1*X)/2)/2
ctrl('adaptive_inputs_defeat_average_channel',dist(actual-nominal)==Q(1,2))
# Same cancellation failure at the ACTUAL original mixed targets, retaining every flag effect.
for k,(mean,w,norm0) in enumerate(zip(means,weights,norms)):
 original=instrument(mean,w,norm0);hh=Q(1,100000)*s.kronecker_product(Z,Y)
 plus=[original[0],original[1]+hh,original[2]];minus=[original[0],original[1]-hh,original[2]]
 ck(f'original_opposite_tangents_CP_TP_{k}',all(psd(B) for B in plus+minus) and all(ptr(a)==ptr(b) for a,b in zip(plus,original)) and all(ptr(a)==ptr(b) for a,b in zip(minus,original)))
 ck(f'original_mean_exact_{k}',all((a+b)/2==c for a,b,c in zip(plus,minus,original)))
 err=(teleport(plus[1]-original[1],P0)+teleport(minus[1]-original[1],P1))*2
 ctrl(f'original_adaptive_input_error_{k}',dist(err)==Q(1,50000))
# External side information can distinguish despite an exact marginal program.
correlated=s.diag(Q(1,2),0,0,Q(1,2));ctrl('unseen_external_memory',dist(correlated-s.eye(4)/4)==Q(1,2))
ck('correlated_marginals_target',ptr(correlated)==I/2)
ctrl('future_transcript_can_steer_past_description',dist(P0-I/2)==Q(1,2) and (P0+P1)/2==I/2)
# Normalize subchannels after averaging: unequal success weights matter.
A1=Q(1,2)*P0;A2=Q(1,10)*P1;weighted=(A1+A2)/s.trace(A1+A2);unweighted=(P0+P1)/2
ctrl('normalizing_each_branch_changes_target',dist(weighted-unweighted)==Q(1,3))
# Explicit normalized-output transfer control on actual physical resource states.
for delta in [Q(1,100),Q(1,10)]:
 rho=(1-delta)*Phi+delta*bad;eps=dist(rho-Phi);out=teleport(rho,(I+Y/2)/2);su=s.trace(out);target=(I+Y/2)/2
 ck(f'postselection_transfer_{delta}',psd(rho) and abs(su-Q(1,4))<=eps and dist(out/su-target)<=eps/su and eps<Q(1,4))
# Prospective used-subset tomography; not observed counts or success fractions.
n=4_000_000_000;NU=2_000_000_000;aa=arb('.05');L=(arb(96)*n*(n+1)/aa).log();eta=arb('.000001');width={}
for w in [1,3,9]:
 v=arb(w+1)/2;bc=arb(w)+eta/2;width[w]=((2*n*v*L).sqrt()+2*bc*L/3)/NU+arb(n)*eta/(2*NU)
es=[width[3**int(a!=0)*3**int(b!=0)]+arb('.000001') for a,b in product(range(4),repeat=2)];epsilon=3*sum((x*x for x in es),arb(0)).sqrt()/2;kappa=arb('.00001');total=epsilon+kappa;q=arb(1)/4;bound=total/(q-total)
ck('prospective_nonvacuous',total<q and bound<arb('.1'));ck('heralded_rate',Q(1,2)*Q(1,4)==Q(1,8))
deps=['tests/channel-swings/k2439_minimal_flagged_tomography_probe.py','lab/process/k2439-minimal-flagged-tomography.json','tests/channel-swings/k2419_positive_visibility_dual_probe.py',str(Path(__file__).relative_to(ROOT)),'explorations/conditional-build/k2440-hidden-route-instrument-use-2026-11-01.md']
report={'result_id':'K2440','checks':checks,'controls':controls,'original_contractions':fixtures,'prospective':{'total_emissions':n,'used_indices':NU,'test_probability':'1/2','alpha':'.05','empirical_residual_bound':'1e-6','readout_bias_bound':'1e-6','completed_program_operation_error':'1e-5','widths':{str(k):str(v) for k,v in width.items()},'program_state_distance':str(epsilon),'success_probability_lower':str(q-total),'normalized_average_success_output_bound':str(bound),'ideal_successes_per_emission':'1/8','status':'hypothetical data and trusted error premises; no realized success-count or future-device guarantee'},'evidence_kinds':{'exact':'original complete matrix-unit Bell contractions, complex input, route first/second moments, contrary noncovariance/conditioning/normalization controls','rigorous_numeric':'Arb256 conditional prospective allowance','universal':'written hidden-routing martingale, fixed-input linear contraction and completed-instrument postselection proof'},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2440-hidden-route-instrument-use.json'
if '--check' in sys.argv:assert json.loads(out.read_text())==report
else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('K2440',len(checks),'checks',len(controls),'controls PASS');print(json.dumps(report['prospective'],indent=2))
