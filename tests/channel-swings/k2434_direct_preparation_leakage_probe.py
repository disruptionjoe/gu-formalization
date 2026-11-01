"""Exact operational leakage controls and rigorous adaptive preparation budgets."""
from pathlib import Path
import json,hashlib,sys
import sympy as s
from flint import arb,ctx
ctx.prec=256
ROOT=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ctrl(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
c=s.Rational(4,5);z=s.Rational(3,5);q=z*z;I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Z=s.diag(1,-1)
U=(c*I).row_join(-z*X).col_join((z*Z).row_join(c*Z*X));D=U.T
ck('encoding_and_decoder_unitary',U.T*U==s.eye(4) and D*U==s.eye(4))
# Tensor order memory, signal, reference. Lift each 2x2 signal block.
Uf=s.BlockMatrix([[s.kronecker_product(U[2*i:2*i+2,2*j:2*j+2],I) for j in range(2)] for i in range(2)]).as_explicit();Df=Uf.T
phi=s.Matrix([1,0,0,1])/s.sqrt(2);P=phi*phi.T;e0=s.Matrix([1,0]);v0=s.kronecker_product(e0,phi);psi=Uf*v0;rho=psi*psi.T
mem=s.Matrix(2,2,lambda i,j:s.trace(rho[4*i:4*i+4,4*j:4*j+4]));ar=rho[:4,:4]+rho[4:,4:]
ck('joint_infidelity_original_state',s.simplify(1-s.trace(P*ar))==q)
ck('actual_memory_marginal',mem==s.diag(1-q,q))
ck('actual_decoder_returns_exact_Bell',Df*psi==v0)
Fail=s.kronecker_product(I,s.eye(4)-P)
p=s.simplify(s.trace(Fail*Df*rho*Df.T));p0=s.simplify(s.trace(Fail*Df*s.kronecker_product(mem,P)*Df.T))
ck('true_zero_failure',p==0)
ck('sharp_actual_memory_failure',p0==2*q-q*q)
ks=[c*c*I,-c*z*X,z*z*Z,c*z*X*Z]
ck('counterfactual_Kraus_TP',sum((k.T*k for k in ks),s.zeros(2))==I)
ck('counterfactual_Kraus_Bell_leakage',s.simplify(1-sum(s.trace(k)**2/4 for k in ks))==p0)
ctrl('one_q_allowance_false',p0>q)
post=s.simplify(s.trace(Fail*Df*s.kronecker_product(e0*e0.T,P)*Df.T))
ctrl('postselected_memory_changes_channel',post==q and post!=p0)
R=s.Matrix([[s.Rational(12,13),s.Rational(5,13)],[-s.Rational(5,13),s.Rational(12,13)]]);prep=s.kronecker_product(R.T,I)*phi;out=s.kronecker_product(R*R,I)*prep
qr=s.simplify(1-(phi.T*prep)[0]**2);pr=s.simplify(1-(phi.T*out)[0]**2);p0r=s.simplify(1-s.trace(R*R)**2/4)
ck('rotation_fixture_exact',qr==pr==s.Rational(25,169) and p0r==s.Rational(14400,28561))
ctrl('cross_term_is_required',p0r>pr+2*qr)
ck('direct_bound_holds_rotation',p0r<pr+2*s.sqrt(pr*qr)+2*qr)
ck('inverse_rotation_zero_output',s.kronecker_product(R,I)*prep==phi)
ck('entanglement_infidelity_rotation_identity',1-(s.trace(R)/2)**2==qr)
# Full sharp interior realization: c_g=33/65, s_g=56/65.
cg=s.Rational(33,65);sg=s.Rational(56,65)
DG=(cg*I).row_join(sg*Z).col_join((-sg*X).row_join(cg*X*Z))
DGf=s.BlockMatrix([[s.kronecker_product(DG[2*i:2*i+2,2*j:2*j+2],I) for j in range(2)] for i in range(2)]).as_explicit()
ck('interior_decoder_unitary',DG.T*DG==s.eye(4))
pint=s.simplify(s.trace(Fail*DGf*rho*DGf.T));p0int=s.simplify(s.trace(Fail*DGf*s.kronecker_product(mem,P)*DGf.T))
ck('interior_observed_failure',pint==s.Rational(25,169))
ck('interior_sharp_saturation',p0int==s.Rational(88201,105625) and p0int==q+(1-q)*(s.sqrt((1-q)*pint)+s.sqrt(q*(1-pint)))**2)
# Plateau realization: memoryless X, Bell mixture, p=3/4 q=1/2.
phiX=s.kronecker_product(X,I)*phi;phiZ=s.kronecker_product(Z,I)*phi
mix=P/2+phiX*phiX.T/4+phiZ*phiZ.T/4;XI=s.kronecker_product(X,I)
ck('plateau_state_positive_trace1',s.trace(mix)==1 and sorted(mix.eigenvals().keys())==[0,s.Rational(1,4),s.Rational(1,2)])
ck('plateau_original_probabilities',1-s.trace(P*mix)==s.Rational(1,2) and 1-s.trace(P*XI*mix*XI.T)==s.Rational(3,4) and 1-s.trace(P*XI*P*XI.T)==1)
# Concavity proof uses actual flagged physical mixtures; this exact pair exercises it.
def sharp(p,q):
 return s.Integer(1) if p+q>=1 else q+(1-q)*(s.sqrt((1-q)*p)+s.sqrt(q*(1-p)))**2
avgp=(pint+s.Rational(3,4))/2;avgq=(q+s.Rational(1,2))/2
ck('flag_mixture_Jensen_control',sharp(avgp,avgq)>=(p0int+1)/2)
# Direct probability gap is strictly improved beyond the loose amplitude bound.
ck('sharp_stronger_than_loose_interior',p0int<pint+2*s.sqrt(pint*q)+2*q)
# Sharp inverse follows h*x²+sqrt(a)*x+h-sqrt(1-a)=0.
AA,hh,kk=s.symbols('AA hh kk',positive=True)
xx=2*kk/(AA+s.sqrt(AA*AA+4*hh*kk))
ck('sharp_inverse_positive_root_substitution',s.simplify(hh*xx*xx+AA*xx-kk)==0)
# Algebraic budget inversion: x=sqrt(e), a=A^2, v=A^2+2Ax+2x^2.
A,x=s.symbols('A x',positive=True);vv=A*A+2*A*x+2*x*x
ck('budget_inversion_identity',s.expand(2*vv-A*A-(A+2*x)**2)==0)
ck('infinite_sample_scaling',s.simplify(vv.subs(A,0)/2-x*x)==0)
# Cauchy-Schwarz is the universal proof, rational arrays exercise nonuniform trials.
ps=[s.Rational(1,100),s.Rational(1,25),0];qs=[s.Rational(1,400),s.Rational(1,100),s.Rational(1,25)]
mean=lambda arr:sum(arr)/len(arr);am=mean(ps);em=mean(qs)
ck('nonuniform_adaptive_averaging',mean([p+2*s.sqrt(p*q)+2*q for p,q in zip(ps,qs)])<=am+2*s.sqrt(am*em)+2*em)
# Current tests only: same marginals do not establish repeated-process independence.
shared=s.diag(s.Rational(1,2),0,0,s.Rational(1,2));independent=s.eye(4)/4
ctrl('tested_one_use_average_not_process',sum(abs(z)*n for z,n in (shared-independent).eigenvals().items())/2==s.Rational(1,2))
Cb=2*(1+arb(2).sqrt()/arb('0.0522306').sqrt());lg=arb(60).log();budgets=[]
for name,C,n,trial in [('bad_previous',Cb,9000000,'1e-10'),('good_previous',arb(2),170000,'1e-9'),('bad_expanded',Cb,20000000,'1e-8')]:
 a=lg/n;v=(arb('0.01')/C)**2;gap=v-a
 ck(name+'_positive_margin',gap>0)
 e=gap**2/((2*v-a).sqrt()+a.sqrt())**2
 h=(1-v).sqrt();kk=gap/((1-a).sqrt()+h);xx=2*kk/(a.sqrt()+(a+4*h*kk).sqrt());esharp=xx**2/(1+xx**2)
 ck(name+'_sharp_budget_improves_simple',esharp>e)
 old=2*gap**2/(1+gap+(1+2*gap-3*gap**2).sqrt())
 ck(name+'_new_budget_larger',e>old)
 tr=arb(trial);ck(name+'_selected_epsilon',tr<e)
 b=a+2*(a*tr).sqrt()+2*tr
 ck(name+'_distance_target',C*b.sqrt()<arb('0.01'))
 ctrl(name+'_zero_counts_not_zero_probability',a>0)
 budgets.append({'branch':name,'n':n,'confidence_alpha':'1/60','distance_target':'0.01','C_upper':str(C),'a':str(a),'v':str(v),'simple_joint_infidelity_threshold':str(e),'sharp_joint_infidelity_threshold':str(esharp),'old_threshold':str(old),'improvement_factor':str(esharp/old),'sufficient_epsilon':trial,'distance_bound':str(C*b.sqrt())})
# Exact zero-p threshold is 1-sqrt(1-v), but cannot substitute for finite counts.
xx=s.symbols('xx',positive=True);qq=1-s.sqrt(1-xx)
ck('sharp_zero_inverse_identity',s.simplify(2*qq-qq*qq-xx)==0)
deps=['lab/process/k2432-bell-preparation-memory-decoupling.json','lab/process/k2430-adaptive-decoder-certification.json','lab/process/k2428-exact-recovery-uniqueness.json']
for dep in deps:
 prior=json.loads((ROOT/dep).read_text());ck('dependency_'+Path(dep).stem,all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in prior['dependencies'].items()))
report={'result_id':'K2434','scope':'Conditional direct support-leakage transfer with actual memory; adaptive tested channels only; no measured calibration or native GU result.','checks':checks,'controls':controls,'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},'bound':'min(1,p+2sqrt(pq)+2q)','adaptive_bound':'min(1,a+2sqrt(ae)+2e)','sharp_bound':'q+(1-q)*(sqrt((1-q)*p)+sqrt(q*(1-p)))^2 for p+q<=1; 1 otherwise','sharp_true_zero_bound':'2q-q^2','sharp_interior_fixture':{'p':str(pint),'q':str(q),'p0':str(p0int)},'true_zero_fixture':{'q':str(q),'p':str(p),'p0':str(p0),'postselected_memory_p0':str(post)},'cross_term_fixture':{'p':str(pr),'q':str(qr),'p0':str(p0r)},'budgets':budgets,'evidence_kinds':{'exact':'unitaries, joint states, Kraus channels, contrary cases and inversion identities','rigorous_numerics':'Arb256 sufficient consumer budgets','universal':'purification amplitude, binary measurement fidelity, physical saturation, flagged-mixture concavity and conditional averaging in note'}}
path=ROOT/'lab/process/k2434-direct-preparation-leakage.json'
if '--check' in sys.argv:assert json.loads(path.read_text())==report
else:path.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('K2434',len(checks),len(controls),'PASS');print(json.dumps(budgets,indent=2))
