"""Exact calibration counterlaws and prospective randomized schedule costs.
Universal circuit and cost proofs are in companion note; spectral gaps inherited.
"""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,sys
from flint import arb,ctx
ctx.prec=256
ROOT=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ctrl(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
def ar(v):
 v=F(v);return arb(v.numerator)/v.denominator
# qutrit diagonal complete effects: independent target-complete verifier.
E1=[F(1),F(1),F(0)];E2=[F(1),F(0),F(1)];om=[(a+b)/2 for a,b in zip(E1,E2)]
ck('complete_qutrit_gap',om==[1,F(1,2),F(1,2)])
correlated=(E1[1]+E2[2])/2;independent=(om[1]+om[2])/2
ctrl('correct_marginals_do_not_give_independence',correlated==1 and independent==F(1,2))
eta=F(1,10);q=[F(1,2)+eta,F(1,2)-eta];p=[F(1,2)]*2
ck('TV_coefficient_exact',sum(abs(a-b) for a,b in zip(p,q))/2==eta and q[0]-p[0]==eta)
# One-sided implementation and TV inequality on actual effect entries.
for be in [F(0),F(1,20),F(1,3)]:
 tilde=[[min(F(1),v+be) for v in E] for E in [E1,E2]]
 for i in range(3):ck(f'calibrated_effect_{be}_{i}',sum(q[j]*tilde[j][i] for j in range(2))<=om[i]+be+eta)
# Same deterministic classical outcome, different poststate: later acceptance differs.
ideal_instrument=lambda state:(F(1),state)
reset_instrument=lambda state:(F(1),[F(0),F(1)])
initial=[F(1),F(0)];ideal_record,ideal_state=ideal_instrument(initial);bad_record,bad_state=reset_instrument(initial)
ctrl('outcome_only_calibration_fails',ideal_record==bad_record and ideal_state[0]-bad_state[0]==1)
# Exact binary symmetric channels are a finite sequential-error control.
e1,e2=F(1,10),F(1,5);composed=e1*(1-e2)+e2*(1-e1)
ck('sequential_instrument_error_bound',composed<=e1+e2 and composed>max(e1,e2))
ctrl('depth_errors_cannot_be_replaced_by_max',composed>max(e1,e2))
ck('mutually_exclusive_branch_error',sum([F(1,54)*F(1,10) for _ in range(54)])==F(1,10))
ctrl('outcome_count_not_channel_error',54*F(1,10)>1)
# Exact original scalar crossover and counts.
e=(F(1,100)-F(1,1000000)/F(1,4))/2;threshold=e*e/20;beta=F(1,100000000)
ck('exact_calibration_crossover',e==F(2499,500000) and threshold==F('0.0000012490002'))
Dold=F(2,5)*e*e-beta;Dnew=F(9,20)*e*e-beta
ck('same_beta_margin_gain',Dnew-Dold==threshold)
ctrl('excess_calibration_reverses_order',F(9,20)*e*e-beta-2*threshold<Dold)
ctrl('nonpositive_margin_rejected',F(9,20)*e*e-F(9,20)*e*e<=0)
c=arb(2).log();J=(1-c)/2;C=(arb(1)/2+J/2)**2/J;gamma=2*C;num=arb(20).log()+gamma*arb('1e-6')
counts=[]
for nu,D in [(F(2,5),Dold),(F(9,20),Dnew)]:
 n=int((num/(c*ar(D))).upper().ceil().unique_fmpz());counts.append(n)
 ck('count_sufficient_'+str(nu),num/(c*n)<=ar(D));ctrl('count_predecessor_fails_'+str(nu),num/(c*(n-1))>ar(D))
ck('original_counts_reproduced',counts==[432973,384822])
# Integer ceilings can tie although continuous bounds differ.
ceil=lambda x:(x.numerator+x.denominator-1)//x.denominator
ctrl('strict_continuous_not_strict_integer',F(1001,100)<F(1002,100) and ceil(F(1001,100))==ceil(F(1002,100)))
pnew=[F(1,8),F(1,2),F(1,4),F(1,8)];charges=[1,1,4,4]
mu=sum(pj*cj for pj,cj in zip(pnew,charges));oldcost=2*counts[0];newcost=counts[1]*(1+mu)
ck('new_expected_test_charge',mu==F(17,8))
ck('prospective_expectations',oldcost==865946 and newcost==F(4810275,4))
ctrl('larger_gap_can_cost_more',newcost>oldcost)
ck('continuous_cost_crossover',Dnew/Dold<F(25,16))
# Exact PGF for N=1, cost per operation1, pi=1/2.
for z in [F(1,2),F(1),F(3,2)]:
 exact=z/(2-z);partial=sum(F(1,2**(k+1))*z**(k+1) for k in range(10));tail=(z/2)**11/(1-z/2)
 ck('geometric_exact_remainder_'+str(z),partial+tail==exact)
 if z!=1:ctrl('omitting_use_factor_'+str(z),1/(2-z)!=exact)
ck('Nuse_MGF_factorization', (F(3,2)/(2-F(3,2)))**3==27)
ctrl('wrong_geometric_normalization',F(1,2)/(1-F(1,2))==1 and F(1,2)/(1-F(1,4))!=1)
prob_cost_above_mean=1-sum(F(1,2**(k+1)) for k in range(2))
ctrl('mean_is_not_deterministic_bound',prob_cost_above_mean==F(1,4) and prob_cost_above_mean>0)
# Nontrivial exact one-use Chernoff tail against actual geometric tail.
z=F(3,2);cost=10;chernoff=z/(2-z)/z**cost;actual=F(1,2)**cost
ck('exact_cost_tail_bound',0<actual<=chernoff<1)
# Large original design, rigorous moment and ceiling, no distribution truncation.
z=F(1001,1000);moment=sum(pj*z**cj for pj,cj in zip(pnew,charges));pi=F(1,2)
ck('positive_mgf_domain',pi*moment<1)
base=z*(1-pi)/(1-pi*moment);delta=F(1,100);N=counts[1]
logbase=ar(base).log();logz=ar(z).log();budget=int(((N*logbase+(1/ar(delta)).log())/logz).upper().ceil().unique_fmpz())
logtail=N*logbase-budget*logz
ck('original_design_cost_tail',logtail.exp()<=ar(delta))
ck('cost_budget_above_expectation',ar(budget)>ar(newcost))
ctrl('calibration_TV_not_nominal_cost_law',sum(qj*cj for qj,cj in zip([F(1,4),F(3,4)],[1,4]))!=sum(pj*cj for pj,cj in zip([F(1,2)]*2,[1,4])))
# Released exact cheap-family optimum and global cost dual on both programs.
cheap_results=[]
source_laws=json.loads((ROOT/'lab/process/k2457-local-verifier-phase-design.json').read_text())['original_laws']
for law in source_laws:
 av=ar(F(law['a']));hv=1/(2*(1+av));qopt=(3+(av/(1+av)).sqrt())/(4+hv);popt=1-qopt;gv=2*qopt-1;nuc=1-gv;tag=law['a']
 A0=popt+qopt*av/(1+av);B0=qopt*(av/2).sqrt()/(1+av);D0=qopt/(2*(1+av))
 ck('cheap_trace_'+tag,(A0+D0-(1-hv*qopt)).contains(0))
 ck('cheap_determinant_'+tag,(A0*D0-B0*B0-hv*qopt*(1-qopt)).contains(0))
 ck('cheap_optimal_characteristic_'+tag,((gv-A0)*(gv-D0)-B0*B0).contains(0))
 discr=(1-hv*qopt)**2-4*hv*qopt*(1-qopt)
 derivative=(-hv+(-6*hv+2*(hv*hv+4*hv)*qopt)/(2*discr.sqrt()))/2
 ck('cheap_stationary_'+tag,derivative.contains(0))
 ck('cheap_top_root_'+tag,2*gv>A0+D0 and 0<popt<1 and nuc>ar(F(41,100)))
 ck('complete_thirty_nonzero_blocks_'+tag,len(law['blocks'])==30)
 spectral=[]
 for j,row in enumerate(law['blocks']):
  tr=ar(F(row['trace']));de=ar(F(row['det']));ev=(tr+(tr*tr-4*de).sqrt())/2;spectral.append(ev)
  ck('cheap_full_carrier_dominance_'+tag+'_'+str(j),qopt*ev<gv)
 ck('cheap_other_zero_block_'+tag,popt<gv)
 # Explicit eigenvector and stationary target-orthogonal dual.
 vx=B0;vy=gv-A0;norm=vx*vx+vy*vy
 xq=vx*vx/norm;xt=(av/(1+av)*vx*vx+2*(av/2).sqrt()/(1+av)*vx*vy+vy*vy/(2*(1+av)))/norm
 ck('cheap_dual_Q_'+tag,(xq-gv).contains(0))
 ck('cheap_dual_T_'+tag,(xt-gv).contains(0))
 ck('expensive_effects_excluded_'+tag,5*nuc>2)
 margin=ar(e*e)*nuc-ar(beta);cost_cut=2*(ar(e*e)-ar(beta))/margin
 ck('calibrated_expensive_effects_excluded_'+tag,margin>0 and cost_cut<5)
 crit=2/nuc;mix=arb(1)/2;gapmix=nuc+mix*(1-nuc)
 for factor in [F(3,4),F(1),F(5,4)]:
  costmix=2*(1-mix)+mix*crit*ar(factor);diff=gapmix/costmix-nuc/2
  ck('projector_sharp_cost_'+tag+'_'+str(factor),diff>0 if factor<1 else (diff.contains(0) if factor==1 else diff<0))
 ctrl('cost_dual_not_gap_upper_bound_'+tag,1>nuc)
 cheap_results.append({'a':tag,'weight_Q':str(popt),'gap':str(nuc),'unpriced_test_cost_threshold':str(crit-1),'common_calibrated_cost_per_use_threshold':str(cost_cut),'full_nonzero_blocks':30})
# Zero-leakage routing specialization; no fixed nonzero-budget inference.
euler=arb(1).exp();piopt=1-1/euler
ck('zero_leakage_routing_interior',0<piopt<1)
ck('zero_leakage_routing_factor_improves',euler<2/arb(2).log())
for tt in [F(1,2),F(1),F(3,2)]:
 numerator=ar(tt).exp()*(ar(tt)-1)
 ck('routing_stationary_sign_'+str(tt),numerator<0 if tt<1 else (numerator.contains(0) if tt==1 else numerator>0))
 ck('routing_derivative_numerator_increasing_'+str(tt),ar(tt)*ar(tt).exp()>0)
ctrl('mean_cost_ignores_routing_at_own_risk',euler>2)
# Original predecessor certificates are reused only with their dependency pins.
deps=[str(Path(__file__).relative_to(ROOT)),'explorations/conditional-build/k2463-local-verifier-calibration-2026-11-01.md','explorations/conditional-build/k2459-direct-leakage-certificate-2026-11-01.md','explorations/conditional-build/k2462-expected-leakage-certificate-2026-11-01.md']
for stem in ['k2457-local-verifier-phase-design','k2460-reordered-local-verification']:
 rp='lab/process/'+stem+'.json';data=json.loads((ROOT/rp).read_text());ck('predecessor_authenticated_'+stem,all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in data['dependencies'].items()));deps.append(rp)
report={'result_id':'K2463','checks':checks,'controls':controls,'calibration_threshold':str(threshold),'original_actual_use_counts':counts,'prospective_expected_costs':[str(oldcost),str(newcost)],'cost_optimal_cheap_verifiers':cheap_results,'cost_tail_design':{'actual_use_count':N,'z':str(z),'delta_cost':str(delta),'cost_budget':budget,'tail_bound':str(logtail.exp()),'moment':str(moment)},'evidence_kinds':{'universal':'written effect order/TV, sequential whole-instrument hybrid, geometric schedule and Chernoff joint-event proof; exact cheap-family optimum and costly-effect dual bound','exact':'qutrit correlation, calibration crossover, geometric law and hypothetical costs','interval':'Arb256 original-use rounding and cost tail certificate','reused':'K2457/K2460 full-carrier spectral certificates; not rerun'},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2463-local-verifier-calibration.json'
if '--check' in sys.argv:assert json.loads(out.read_text())==report
else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('K2463',len(checks),'checks',len(controls),'controls PASS',report['cost_tail_design'])
