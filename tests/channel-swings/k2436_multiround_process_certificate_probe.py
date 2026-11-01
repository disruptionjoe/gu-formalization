"""Exact causal testers, process memory controls and rigorous batch budgets."""
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
def psd(A):return all(v>=0 for v in A.eigenvals())
def halftrace(A):return s.simplify(sum(abs(v)*m for v,m in A.eigenvals().items())/2)
def ptr(A,dims,keep):
 import itertools
 outdims=[dims[i] for i in keep];tr=[i for i in range(len(dims)) if i not in keep]
 def idx(t):
  ans=0
  for x,d in zip(t,dims):ans=ans*d+x
  return ans
 labels=list(itertools.product(*[range(d) for d in outdims]));out=s.zeros(len(labels))
 for a,u in enumerate(labels):
  for b,v in enumerate(labels):
   for w in itertools.product(*[range(dims[i]) for i in tr]):
    aa=[0]*len(dims);bb=[0]*len(dims)
    for i,x,y in zip(keep,u,v):aa[i]=x;bb[i]=y
    for i,x in zip(tr,w):aa[i]=bb[i]=x
    out[a,b]+=A[idx(aa),idx(bb)]
 return out
I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);phi=s.Matrix([1,0,0,1])/s.sqrt(2);P1=phi*phi.T
vI=phi;vX=s.kronecker_product(X,I)*phi;PX=vX*vX.T
# Ordering B2,A2,B1,A1, each slot's normalized Choi state is generated chronologically.
P=s.kronecker_product(P1,P1);v=s.kronecker_product(phi,phi)
shared=(s.kronecker_product(P1,P1)+s.kronecker_product(PX,PX))/2
independent=s.kronecker_product((P1+PX)/2,(P1+PX)/2)
for label,rho in [('target',P),('shared',shared),('independent',independent)]:
 ck(label+'_positive_normalized',psd(rho) and s.trace(rho)==1)
 rho1=ptr(rho,[2]*4,[2,3])
 ck(label+'_causal_last_trace',ptr(rho,[2]*4,[1,2,3])==s.kronecker_product(I/2,rho1))
 ck(label+'_causal_first_trace',ptr(rho1,[2,2],[1])==I/2)
ck('same_complete_one_slot_channels',ptr(shared,[2]*4,[0,1])==ptr(independent,[2]*4,[0,1]) and ptr(shared,[2]*4,[2,3])==ptr(independent,[2]*4,[2,3]))
ctrl('different_full_temporal_processes',halftrace(shared-independent)==s.Rational(1,2))
# Feeding |00> and reading both Z outputs distinguishes correlation (nonunitary marginals).
sharedout=s.diag(s.Rational(1,2),0,0,s.Rational(1,2));indout=s.eye(4)/4
ck('physical_same_input_memory_discriminator',halftrace(sharedout-indout)==s.Rational(1,2))
ctrl('marginal_control_not_exact_unitary_target',s.trace(P1*(P1+PX)/2)==s.Rational(1,2))
# Causal feedback: prepare |0>, feed first output directly to second input.
L=s.zeros(2,16)
for b2 in range(2):
 for a2 in range(2):
  for b1 in range(2):
   for a1 in range(2):
    col=((b2*2+a2)*2+b1)*2+a1
    L[b2,col]=2*int(a2==b1 and a1==0)
e0=s.Matrix([1,0]);omega=s.sqrt(2)*phi
T=s.kronecker_product(I,omega*omega.T,e0*e0.T)
ck('normalized_Choi_tester_operator',L.T*L==4*T)
ck('tester_trace_and_norm',s.trace(T)==4 and max(T.eigenvals())==2 and max((L.T*L).eigenvals())==8)
ctrl('generic_tester_norm_one_is_false',max(T.eigenvals())>1)
ck('pure_target_link',L*v==e0)
F=L.T*(I-e0*e0.T)*L
ck('failure_effect_positive_annihilates_target',psd(F) and F*P==s.zeros(16))
ck('pure_target_operator_bound',psd(8*(s.eye(16)-P)-F))
for label,rho in [('shared',shared),('independent',independent)]:
 out=L*rho*L.T;p0=s.simplify(1-s.trace(P*rho));failure=s.trace((I-e0*e0.T)*out)
 ck(label+'_feedback_normalization',psd(out) and s.trace(out)==1)
 ck(label+'_feedback_effect_probability',failure==s.trace(F*rho) and failure<=8*p0)
# Coherent rotation controls square-root scaling and reference-sensitive testing.
R=s.Matrix([[s.Rational(4,5),s.Rational(-3,5)],[s.Rational(3,5),s.Rational(4,5)]]);vr=s.kronecker_product(R,I)*phi
rhoR=s.kronecker_product(vr*vr.T,P1);out=L*rhoR*L.T;pr=1-s.trace(P*rhoR)
ck('coherent_process_exact_failure',pr==s.Rational(9,25) and halftrace(out-e0*e0.T)==s.Rational(3,5))
ctrl('linear_failure_distance_bound_false',halftrace(out-e0*e0.T)>pr)
# A genuinely complex unitary target checks conjugation and coherent feedback.
Uc=s.diag(1,s.I);vc=s.kronecker_product(Uc,I)*phi;vfull=s.kronecker_product(vc,phi);Pc=vfull*vfull.H
Lc=s.zeros(2,16)
for b2 in range(2):
 for a2 in range(2):
  for b1 in range(2):
   for a1 in range(2):
    Lc[b2,((b2*2+a2)*2+b1)*2+a1]=s.sqrt(2)*int(a2==b1)
psic=s.Matrix([1,s.I])/s.sqrt(2);Fc=Lc.H*(I-psic*psic.H)*Lc
ck('complex_unitary_target_positive_and_causal',psd(Pc) and s.trace(Pc)==1 and ptr(Pc,[2]*4,[1,2,3])==s.kronecker_product(I/2,P1))
ck('complex_target_coherent_feedback',Lc*vfull==psic and max((Lc.H*Lc).eigenvals())==8)
ck('complex_target_pure_effect_bound',Fc*Pc==s.zeros(16) and psd(Fc) and psd(8*(s.eye(16)-Pc)-Fc))
ctrl('complex_transpose_without_conjugation_rejected',vfull*vfull.T != Pc and vfull*vfull.T != (vfull*vfull.T).H)
# Outcome-released marginal protocol: joint product fidelity is union-bounded.
Pfirst=s.kronecker_product(s.eye(4),P1);Psecond=s.kronecker_product(P1,s.eye(4))
U=(s.eye(16)-Pfirst)+(s.eye(16)-Psecond)-(s.eye(16)-P)
ck('same_batch_projector_union_operator',psd(U) and Pfirst*Psecond==P)
for label,rho in [('shared',shared),('independent',independent),('coherent',rhoR)]:
 ck(label+'_marginal_union_bound',1-s.trace(P*rho)<=2-s.trace(Pfirst*rho)-s.trace(Psecond*rho))
# Exact marginals pure force full product; no hidden-memory counterexample under these premises.
ck('zero_marginal_union_kernel_is_target',U.shape==(16,16) and ((s.eye(16)-Pfirst)+(s.eye(16)-Psecond)).nullspace()==[s.Matrix([1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1])])
# Conditional batch budget: alpha=.05, tau=.01, ideal prep/readout, zero retained failures.
budgets=[]
for r in [1,2,4,8]:
 K2=2**(2*r-1);tau=arb('0.01');alpha=arb('0.05');logalpha=-(alpha.log())
 raw=K2*logalpha/(tau*tau);n=int(raw.upper().ceil().unique_fmpz())+1
 a=logalpha/n;ck('r'+str(r)+'_ideal_budget',K2*a<tau*tau)
 # Give preparation an actual positive margin with four times as many whole batches.
 nn=4*n;aa=logalpha/nn;vv=tau*tau/K2;gap=vv-aa
 hh=(1-vv).sqrt();kk=gap/((1-aa).sqrt()+hh);xx=2*kk/(aa.sqrt()+(aa+4*hh*kk).sqrt());e=xx*xx/(1+xx*xx)
 trial=vv/100
 B=trial+(1-trial)*(((1-trial)*aa).sqrt()+(trial*(1-aa)).sqrt())**2
 ck('r'+str(r)+'_nonzero_preparation_budget',trial<e and K2*B<tau*tau)
 budgets.append({'qubit_slots':r,'K_squared':K2,'alpha':'0.05','distance_target':'0.01','ideal_zero_failure_batches':n,'batches_with_margin':nn,'sharp_joint_preparation_threshold':str(e),'conservative_joint_infidelity':str(trial),'distance_bound_with_margin':str((K2*B).sqrt()),'slot_uses_ideal':r*n})
# Conditional average/fraction/capped-weight statements consume p0, not future trials.
pvals=[s.Rational(0),s.Rational(1,100),s.Rational(1,25)];mean=sum(pvals)/3
ck('mean_square_root_consumer',sum(s.sqrt(8*p) for p in pvals)/3<=s.sqrt(8*mean))
ck('exceptional_fraction_consumer',s.Rational(sum(bool(8*p>=s.Rational(1,4)) for p in pvals),3)<=8*mean/s.Rational(1,4))
# New campaigns and future devices remain uncontrolled even after true zero past leakage.
ctrl('future_switch_not_constrained',s.trace(P1*PX)==0 and s.trace(P1*P1)==1)
deps=['lab/process/k2434-direct-preparation-leakage.json','lab/process/k2430-adaptive-decoder-certification.json']
for dep in deps:
 j=json.loads((ROOT/dep).read_text());ck('pins_'+Path(dep).stem,all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in j['dependencies'].items()))
report={'result_id':'K2436','scope':'Conditional tested fixed-slot combs against a memoryless unitary target; no measured calibration, future process transfer, optimal dimension constant or GU identification.','checks':checks,'controls':controls,'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},'strategy_bound':'min(1,sqrt(D*product_{i<r}d_Bi*p))','batch_bound':'min(1,sqrt(D*product_{i<r}d_Bi*B(a,e)))','tester_fixture':{'D':4,'tester_norm':2,'normalized_contraction_squared_norm':8},'budgets':budgets,'evidence_kinds':{'exact':'causal Choi traces, actual feedback map, operator inequality, complete marginal/memory controls and union projector','rigorous_numerics':'Arb256 prospective sample and preparation budgets','universal':'written pure-target effect, batch conditional martingale transfer and same-batch union argument'}}
p=ROOT/'lab/process/k2436-multiround-process-certificate.json'
if '--check' in sys.argv:assert json.loads(p.read_text())==report
else:p.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('K2436',len(checks),'checks',len(controls),'controls PASS');print(json.dumps(budgets,indent=2))
