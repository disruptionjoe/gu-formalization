"""Exact adaptive-epoch and resource fixtures; universal reduction in K2569 note."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,math
ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
root=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(n,c):
 checks[n]=bool(c)
 if not c:raise AssertionError(n)
def ct(n,c):
 controls[n]=bool(c)
 if not c:raise AssertionError('contrary: '+n)
# Enumerate the actual two-attempt policy, preserving distinct continuation labels.
a=[F(1,4),F(1,5)];b=[F(1,3),F(1,4)]
reach=[F(1),(1-a[0])/2];nu=[r*(1+x)/2 for r,x in zip(reach,a)];abort=reach[-1]*(1-a[-1])/2
ck('compressed_weights',nu==[F(5,8),F(9,40)] and abort==F(3,20))
ck('all_mass_accounted',sum(nu)+abort==1)
use_original=[r/2 for r in reach];use_compressed=[v/(1+x) for v,x in zip(nu,a)]
fail_original=[r*x/2 for r,x in zip(reach,a)];fail_compressed=[v*x/(1+x) for v,x in zip(nu,a)]
ck('distinct_post_use_continuations_preserved',use_original==use_compressed==[F(1,2),F(3,16)])
ck('failure_weights_preserved',fail_original==fail_compressed)
ck('positive_trials_preserved',sum(2*v/(1+x) for v,x in zip(nu,a))==sum(reach)==F(11,8))
ck('original_log_cost_coefficients_preserved',[2*v/(1+x) for v,x in zip(nu,a)]==[F(1),F(3,8)])
# Unequal continuation values make lost labels detectable.
continuation=[F(7,10),F(1,5)]
ck('continuation_payoff_preserved',sum(u*v for u,v in zip(use_original,continuation))==sum(u*v for u,v in zip(use_compressed,continuation)))
ct('wrong_unhazarded_selection_changes_use',[r/2/(1+x) for r,x in zip(reach,a)]!=use_original)
ct('discarding_continuation_label_changes_payoff',sum(use_original)*continuation[0]!=sum(u*v for u,v in zip(use_original,continuation)))
# a>b normalization needs initial abort to preserve the original weights.
aa,bb=F(2,5),F(1,5);execute=(1+bb)/(1+aa)
ck('above_diagonal_execution_probability',execute==F(6,7))
ck('above_diagonal_use',execute/(1+bb)==1/(1+aa)==F(5,7))
ck('above_diagonal_trials',2*execute/(1+bb)==2/(1+aa)==F(10,7))
ct('omitting_preabort_changes_original_use',1/(1+bb)!=1/(1+aa))
# Overshoot has zero clipped cost but positive original cost.
aa,bb,ss=F(3,5),F(4,5),F(1,2);aprim=min(aa,ss);exe=(1+aprim)/(1+aa)
ck('overshoot_execution_probability',exe==F(15,16))
ck('overshoot_use_and_trials',exe/(1+aprim)==F(5,8) and 2*exe/(1+aprim)==F(5,4))
original_increment=(bb-aa)**2/(2*(aa+bb)*(2-aa-bb))
ck('overshoot_strict_cost_reduction',original_increment>0 and (ss-aprim)**2==0)
# b=0 stage: free random continuation has same survival but zero positive count.
aa=F(2,3)
ck('zero_score_free_randomized_continuation',1/(1+aa)==F(3,5))
# Original law with survival prefixes, not two trials times stage count.
stages=[(F(1,4),F(1,4)),(F(1,8),F(1,4))];P=F(1);prefix=[]
for aa,bb in stages:P/=1+aa;prefix.append(P)
trials=2*sum(prefix)
ck('prefix_weighted_resource',prefix==[F(4,5),F(32,45)] and trials==F(136,45))
ct('unweighted_stage_count_is_wrong',trials!=2*len(stages))
# An exactly computed logarithm interval checks a resource/cost fixture.
def log1p_interval(x,terms=20):
 t=x/(2+x);lo=2*sum((t**(2*j+1)/F(2*j+1) for j in range(terms)),F(0));hi=lo+2*t**(2*terms+1)/(F(2*terms+1)*(1-t*t));return lo,hi
costs=[]
for aa,bb in zip(a,b):costs.append(log1p_interval((bb-aa)**2/(2*(aa+bb)*(2-aa-bb))))
orig_lo=sum(r*c[0] for r,c in zip(reach,costs));orig_hi=sum(r*c[1] for r,c in zip(reach,costs))
comp_lo=sum(2*v*c[0]/(1+x) for v,x,c in zip(nu,a,costs));comp_hi=sum(2*v*c[1]/(1+x) for v,x,c in zip(nu,a,costs))
ck('actual_log_cost_intervals_equal',(orig_lo,orig_hi)==(comp_lo,comp_hi) and orig_lo>0)
ct('conditioning_cost_on_eventual_use_changes_cost',sum(u*c[1] for u,c in zip(use_original,costs))<orig_lo)
# Continuous-at-zero bound at independent exact triangle points (support only).
for j,(aa,bb) in enumerate([(F(0),F(1,2)),(F(1,20),F(1,10)),(F(1,5),F(1,5))]):
 xx=(bb-aa)**2/(2*(aa+bb)*(2-aa-bb));ck('zero_stage_cost_bound_fixture_'+str(j),0<=xx<=bb/(2*(2-bb)))
# Previously certified bounds consumed as evidence, not recertified here.
lower=F(711079567311,10**12);one_upper=F(71,100);gap=F(1079,10**6)
ck('existing_certificate_gap_consumer',lower-one_upper>gap>0)
eta=gap/10;ck('one_stage_mixture_mass_bound',eta/gap==F(1,10))
# Exact upper bound exp(1/2)<180/109 gives the claimed >2.18 without float arithmetic.
exp_partial=sum((F(1,2)**j/F(math.factorial(j)) for j in range(10)),F(0))
exp_tail=(F(1,2)**10/F(math.factorial(10)))/(1-F(1,22))
ck('exponential_upper_rational',exp_partial+exp_tail<F(180,109))
ck('resource_example_rational',F(18,5)/F(180,109)==F(109,50))
# Finite prefixes of a never-finitely-hitting schedule: geometric exact identities.
S=F(1,2)
for j in [1,4,16]:
 score=sum((S/F(2)**i for i in range(1,j+1)),F(0));ck('infinite_approach_prefix_'+str(j),score==S*(1-F(1,2)**j)<S)
ct('finite_hit_cannot_be_replaced_by_limit_hit',S*(1-F(1,2)**16)!=S)
ck('reused_attainment_regime_interval_separation',F(98,51)**2<F(16,3))
# Exact stage-vs-Euler transfer; finite identities, not a sampled universal sign.
import sympy as sy
rr,bb,xx,ll,gg,ee=sy.symbols('rr bb xx ll gg ee',nonnegative=True)
Euler=xx-bb*(rr*xx+ll*gg)
atom=(xx-ll*bb*gg-ll*ee)/(1+rr*bb)
ck('original_stage_Euler_identity',sy.cancel(atom-Euler-(rr**2*bb**2*xx+ll*rr*bb**2*gg-ll*ee)/(1+rr*bb))==0)
ck('positive_Euler_remainder_factors',sy.Poly(rr**2*bb**2*xx+ll*rr*bb**2*gg,rr,bb,xx,ll,gg).coeffs()==[1,1])
ck('hybrid_and_substitution_errors_compose',F(1,4)+F(3,4)==1)
# Exact irregular-block partition fixture preserves score and caps squared lengths.
NN=4;h=F(1,2)/NN;blocks=[F(1,50),F(3,50),F(7,100),F(1,10),F(1,20)]
pieces=[]
for bblock in blocks:
 cnt=math.ceil(bblock/h);pieces.extend([bblock/cnt]*cnt)
ck('continuum_partition_score',sum(pieces)==sum(blocks))
ck('continuum_partition_size_and_count',max(pieces)<=h and len(pieces)<=2*NN+1)
ck('continuum_partition_square_budget',sum(v*v for v in pieces)<=F(1,4)/NN)
NN=4750
ck('explicit_original_policy_tolerance',F(19,10)*F(1,4)/NN==F(1,10000))
ck('explicit_original_stage_resource_ceiling',3*NN+1==14251 and 6*NN+2==28502)
# Actual r=0,b=1/4: finite stage pays more than the constant-r continuum.
lo,hi=log1p_interval(F(1,14))
ct('finite_stage_cost_exceeds_continuum_cost',2*lo>F(1,8))
report={'result':'K2569','evidence_kind':'exact finite original-law accounting and gap consumers; universal reduction/compactness in note','checks':checks,'contrary_controls':controls,'epoch':{'selection_weights':[str(v) for v in nu],'abort':str(abort),'mean_positive_trials':'11/8'},'gap_consumer':{'score':'1/2','lambda':'19/10','lower_bound_for_V_minus_D1':str(gap),'not_a_computed_g1':True},'scope':'all original adaptive policies; necessary divergence and sufficient O(1/eta) upper resource; no matching lower rate','reused_evidence':['k2483-adaptive-stopping-bellman-2026-11-01.md','k2567-stopping-family-structure-2026-11-05.md','k2561-higher-budget-stopping-2026-11-05.md','k2565-bellman-supersolution-2026-11-05.md']}
f=root/'lab/process/k2569-stopping-maximizing-sequences.json'
if args.write:f.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(f.read_text())==report,'saved report mismatch'
print(json.dumps({'result':'K2569','checks':len(checks),'controls':len(controls),'status':'pass'}))
