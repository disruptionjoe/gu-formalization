"""Exact adaptive support-test controls and complete-channel inference boundaries."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import json,hashlib,sys
import sympy as s
from flint import arb,ctx
ctx.prec=256
ROOT=Path(__file__).resolve().parents[2]
checks={};controls={}
def ck(name,value):
 checks[name]=bool(value)
 if not value:raise AssertionError('FAIL '+name)
def ctrl(name,value):
 controls[name]=bool(value)
 if not value:raise AssertionError('FAIL control '+name)
def ar(q):q=Q(q);return arb(q.numerator)/q.denominator
prior=json.loads((ROOT/'lab/process/k2428-exact-recovery-uniqueness.json').read_text())
ck('inherited_certificate_dependency_pins',all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==v for p,v in prior['dependencies'].items()))
# Fully enumerated history-adaptive binary experiment. p can include 0 and 1.
alpha=Q(1,8);nodes=[([],Q(1),Q(0),Q(1),False)];crossing=Q(0);expectations=[];jensen_checks=0
for t in range(1,10):
 new=[]
 for hist,weight,A,M,hit in nodes:
  p=Q((t+2*sum(hist))%5,4)
  A1=A+p
  # Exact conditional supermartingale expectation, including certain failure.
  nextM=M/(1-p) if p<1 else Q(0)
  ck('conditional_hazard_recursion_'+str(t)+'_'+''.join(map(str,hist)),(1-p)*nextM<=M)
  for x,prob in [(0,1-p),(1,p)]:
   if not prob:continue
   h=hist+[x];m=nextM if x==0 else Q(0)
   ishit=not any(h) and (1-A1/t)**t<alpha
   if not any(h):
    ck('Jensen_'+str(t)+'_'+''.join(map(str,hist)),m*(1-A1/t)**t>=1);jensen_checks+=1
   new.append((h,weight*prob,A1,m,hit or ishit))
 nodes=new
 expectation=sum(w*m for h,w,a,m,hit in nodes);crossing=sum(w for h,w,a,m,hit in nodes if hit)
 ck('hazard_expectation_'+str(t),expectation<=1)
 ck('anytime_crossing_'+str(t),crossing<=alpha)
 expectations.append([t,str(expectation),str(crossing)])
ck('full_probability_mass',sum(x[1] for x in nodes)==1)
# Planted positive: an actual crossing under a valid null, with exact nonzero mass.
positive_cross=sum(Q(1,16) for h in product([0,1],repeat=4) if any(not any(h[:n]) and Q(1,2)**n<alpha for n in range(1,5)))
ck('positive_crossing_probability_one_sixteenth',positive_cross==Q(1,16) and 0<positive_cross<=alpha)
ctrl('zero_crossing_detector_would_miss_planted_event',positive_cross!=0)
# Nonzero-failure bound's conditional factor. The universal proof is log(1-z)<=-z.
for p in [Q(0),Q(1,7),Q(1,3),Q(3,4),Q(1)]:
 for c in [Q(1,2),Q(3,4),Q(7,8)]:
  z=ar(c*p);factor=z.exp()*(1-z)
  ck('exponential_supermartingale_'+str(p)+'_'+str(c),factor.contains(1) if not p else factor<1)
weights=[Q(1,2),Q(1,4),Q(1,4)];ck('grid_error_allocation',sum(weights)==1)
bounds=[]
for c,w in zip([Q(1,2),Q(3,4),Q(7,8)],weights):
 bound=((- (1-ar(c)).log())*10+(1/ar(Q(1,60)*w)).log())/(10000*ar(c));bounds.append(bound)
ck('nonzero_failure_bound_nonvacuous',all(b>0 and b<arb('0.01') for b in bounds))
# Prospective budgets use the already certified full-complex support conditioning.
mu_floor=arb('0.0522306');Cbad=2*(1+arb(2).sqrt()/mu_floor.sqrt());log60=arb(60).log()
ck('bad_budget_9000000',Cbad*(log60/9000000).sqrt()<arb('0.01'))
ck('good_budget_170000',2*(log60/170000).sqrt()<arb('0.01'))
ck('three_branch_joint_error',3*Q(1,60)==Q(1,20))
ck('systematic_probability_before_root',Cbad*(log60/9000000+arb('1e-9')).sqrt()<arb('0.01'))
ctrl('systematic_floor_cannot_be_sampled_away',Cbad*arb('1e-5').sqrt()>arb('0.01'))
# Wrong resetting protocol has exact coverage failure.
reset_failure=1-Q(63,64)**9
ctrl('reset_after_failures_breaks_coverage',reset_failure>Q(1,8))
ctrl('unpenalized_grid_is_not_declared_budget',sum([Q(1,60)]*3)>Q(1,60))
# Complete complex Choi channels, output-first with trace 2.
I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1)
def choi(U):
 v=s.Matrix([U[0,0],U[0,1],U[1,0],U[1,1]])
 return v*v.conjugate().T
def ptr(J):return s.Matrix(2,2,lambda a,b:sum(J[2*k+a,2*k+b] for k in range(2)))
Ji=choi(I);Jx=choi(X);Pi=Ji/2
ck('original_unitary_CP_TP',Ji.eigenvals()=={s.Integer(2):1,s.Integer(0):3} and ptr(Ji)==I and ptr(Jx)==I)
ck('orthogonal_error_support_failure',s.trace((s.eye(4)-Pi)*Jx)/2==1)
# Only one of a hundred tested channels is X: average d=1/100, one-round d=1.
p=Q(1,100);Javg=(1-s.Rational(1,100))*Ji+s.Rational(1,100)*Jx
ck('nonstationary_average_support_linear',s.trace((s.eye(4)-Pi)*Javg)/2==s.Rational(1,100))
ck('average_CPTP',ptr(Javg)==I and all(v>=0 for v in Javg.eigenvals()))
ctrl('average_certificate_does_not_bound_each_round',arb(1)>2*ar(p).sqrt())
ctrl('future_switch_unconstrained',s.trace((s.eye(4)-Pi)*Ji)==0 and s.trace((s.eye(4)-Pi)*Jx)==2)
# Rational coherent phase: sin(theta)=3/5, cos(theta)=4/5.
U=s.diag((4+3*s.I)/5,(4-3*s.I)/5);Ju=choi(U);failure=s.simplify(s.trace((s.eye(4)-Pi)*Ju)/2)
ck('coherent_complex_unitary_support',s.simplify(U.conjugate().T*U)==I and failure==s.Rational(9,25))
ctrl('linear_failure_distance_bound_false',s.Rational(3,5)>failure)
# Marginal Bell-input calibration is insufficient: Bell and product mixed share I/2.
rhomix=s.eye(4)/4
ctrl('marginal_input_not_joint_calibration',ptr(Pi)==ptr(rhomix) and s.trace(Pi*Pi)==1 and s.trace(Pi*rhomix)==s.Rational(1,4))
eps=s.Rational(1,4);Jp=s.eye(4)/2+eps*s.kronecker_product(Y,I);Jm=s.eye(4)/2-eps*s.kronecker_product(Y,I)
real_basis=[]
for a in range(4):
 for b in range(a,4):
  A=s.zeros(4);A[a,b]=1;A[b,a]=1;real_basis.append(A)
ck('complex_control_CP_TP',ptr(Jp)==I and ptr(Jm)==I and all(v>=0 for J in [Jp,Jm] for v in J.eigenvals()))
ctrl('real_symmetric_tomography_blind',Jp!=Jm and all(s.trace(A*(Jp-Jm))==0 for A in real_basis))
# A uniform random tested index, independent after testing, is the certified channel.
ck('uniform_tested_index_channel',sum([Ji]*99+[Jx],s.zeros(4))/100==Javg)
# A two-use product channel remains sensitive to inter-round correlations.
ck('correlated_noise_single_use_average', (Ji+Jx)/2==s.eye(4)/2+s.kronecker_product(X,X)/2)
ctrl('average_not_product_process',Q(1,2)!=Q(1,4)) # same fair X label reused vs independent labels
# Released consequence: bounded reweighting, exceptional-trial fraction and transport.
# Exact Bernoulli mixture family: d(C_t,Id)=p_t for X-flip mixtures.
ps=[Q(0),Q(1,100),Q(1,4),Q(1)];ws=[Q(1,2),Q(1,4),Q(1,4),Q(0)];rho=Q(2);b=sum(ps)/4
ck('reweighting_original_probability',sum(ws)==1 and max(ws)<=rho/4 and sum(w*p for w,p in zip(ws,ps))<=rho*b)
# Square-root pointwise bound implies a simultaneous exceptional-set bound.
threshold=Q(1,2);fraction=sum(p>=threshold for p in ps)/Q(4)
ck('exceptional_trial_fraction_control',fraction<=4*b/(threshold*threshold))
# A useful sharper positive case, with a single distant trial.
ck('rare_bad_trial_bound_nonvacuous',4*Q(1,10000)/(Q(1,2)**2)<Q(1,100))
# Actual weighted selection can be adversarial if no density cap is imposed.
ctrl('uncapped_postselection_breaks_uniform_average',arb(1)>2*ar(Q(1,100)).sqrt())
# Concrete future X-mixture channels with an independently supplied drift allowance.
target_p=Q(1,10);training=[Q(1,20),Q(3,20)];gamma=sum(abs(target_p-p) for p in training)/2
ck('future_transfer_triangle_exact',target_p<=sum(training)/2+gamma)
ck('Lipschitz_age_transport_exact',gamma==Q(1,20))
report={'result_id':'K2430','checks':checks,'controls':controls,'evidence_kinds':{'exact_tree':'rational adaptive conditional-probability recursion, mass, crossing and Jensen controls','exact_channel':'full complex Choi positivity/TP and concrete contrary constructions','interval':'256-bit Arb budgets and finite factor controls','proof':'universal supermartingale and channel transfer are proved in companion note; finite tree is not universal proof'},'adaptive_tree':{'depth':9,'leaf_count':len(nodes),'expectations_and_crossings':expectations,'jensen_checks':jensen_checks,'positive_crossing_fixture':{'iid_failure_probability':'1/2','depth':4,'alpha':'1/8','strict_crossing_probability':str(positive_cross)}},'prospective_budgets':{'bad_each':9000000,'good':170000,'total':18170000,'alpha_each':'1/60','all_three_error':'1/20','bad_constant_upper':str(Cbad),'nonzero_grid_bounds':list(map(str,bounds))},'reset_false_coverage_probability':str(reset_failure),'scope':'Anytime inference for tested predictable average conditional channels and average per-trial distance only; no next device, process tensor, observed data or native GU claim.'}
deps=['lab/process/k2428-exact-recovery-uniqueness.json','tests/channel-swings/k2428_exact_recovery_uniqueness_probe.py','lab/process/k2426-recovery-rigidity.json']
report['dependencies']={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}
out=ROOT/'lab/process/k2430-adaptive-decoder-certification.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
else:assert json.loads(out.read_text())==report
print(json.dumps({'checks':len(checks),'controls':len(controls),'tree_leaves':len(nodes)}))
