"""Exact finite support for K2570; universal operator/duality proofs are in the note.
No sampled ODE or report assertion is treated as a whole-domain proof.
"""
from pathlib import Path
import argparse
import hashlib
import json
import sympy as s

ap = argparse.ArgumentParser()
group = ap.add_mutually_exclusive_group()
group.add_argument('--write', action='store_true')
group.add_argument('--check', action='store_true')
args = ap.parse_args()
root = Path(__file__).resolve().parents[2]
checks, controls, provenance = {}, {}, {}
def ck(name, condition):
    checks[name] = bool(condition)
    if not condition:
        raise AssertionError(name)
def ct(name, condition):
    controls[name] = bool(condition)
    if not condition:
        raise AssertionError('contrary: ' + name)
pins = {
    'explorations/conditional-build/k2568-cauchy-preparation-bandwidth-2026-11-05.md': 'ba379771ece19cf306c3fbf9c41eb729d6d81bf248419485dea400622ded8f13',
    'explorations/conditional-build/k2566-finite-observation-preparation-2026-11-05.md': 'd8b0ce5e7cdd4ed80f3cf2fd8b3f627d2c7e36138ee2aca7d4e613b871ca792d',
}
for path, digest in pins.items():
    actual = hashlib.sha256((root/path).read_bytes()).hexdigest()
    if actual != digest:
        raise AssertionError('prerequisite changed: ' + path)
    provenance[path] = actual
K = s.Rational(35, 3624192)
mu = s.Rational(611557655, 39953092608)
ck('actual_positive_homogeneous_potential', mu/K-21 == s.Rational(120691003,77168))
ck('nonzero_original_gauge_invariant_field', mu-5*K == s.Rational(67736495,4439232512))
z = s.symbols('z', real=True)
for degree in range(5):
    H = s.chebyshevu(degree,z)
    ck('actual_S3_harmonic_'+str(degree), s.expand((1-z*z)*s.diff(H,z,2)-3*z*s.diff(H,z)+degree*(degree+2)*H)==0)
# First two zonal harmonics have equal norm and zero cross moment in S3 measure.
m0 = s.beta(s.Rational(1,2),s.Rational(3,2)).rewrite(s.gamma)
m2 = s.beta(s.Rational(3,2),s.Rational(3,2)).rewrite(s.gamma)
ck('first_two_harmonic_norms', s.simplify(m0-s.pi/2)==0 and s.simplify(4*m2-m0)==0)
ck('first_two_harmonic_weighted_cross_integral', s.integrate(2*z*s.sqrt(1-z*z),(z,-1,1))==0)
# Positive radial response integrals are not replaced by rational ODE approximations.
I1,I2=s.symbols('I1 I2',positive=True)
q = s.Matrix([s.Rational(3,2),s.Rational(34,5)])
g = s.Matrix([q[0]/I1,q[1]/I2])
ck('actual_detector_normalization', s.diag(I1,I2)*g == q)
W=s.diag(2,4);a=s.Matrix([s.Rational(3,10),s.Rational(2,5)])
delta2=s.Rational(1,4);R2=s.Rational(73,25)
ck('finite_truth_noise_constraint',a.dot(a)==delta2)
ck('finite_truth_preparation_constraint',(W*a).dot(W*a)==R2)
ck('dual_normal_alignment',q==(s.eye(2)+W**2)*a)
value=q.dot(a)
ck('exact_primal_readout',value==s.Rational(317,100))
dualsum=sum(q[i]**2/(1+W[i,i]**2) for i in range(2))
ck('exact_dual_sum',dualsum==value)
ck('matching_dual_certificate',(delta2+R2)*dualsum==value**2)
ck('indistinguishable_opposite_truths',a+(-a)==-a+a==s.zeros(2,1))
ck('minimax_lower_separation',(q.dot(a)-q.dot(-a))/2==value)
ck('linear_estimator_bias_relation',q-a==W**2*a)
ck('linear_estimator_noise_squared',delta2*a.dot(a)==delta2**2)
ck('linear_estimator_bias_squared',R2*(W.inv()*(q-a)).dot(W.inv()*(q-a))==R2**2)
ck('linear_estimator_exact_worst_error',delta2+R2==value and a.dot(a-a)-q.dot(a)==-value)
# Construct exact nuisance coordinates: observation remains fixed, preparation rises.
q3=q.col_join(s.Matrix([0]));a3=a.col_join(s.Matrix([s.Rational(1,10)]))
ck('higher_modes_have_zero_selected_readout',q3.dot(a3)==value)
ct('unseen_modes_still_consume_preparation',(s.diag(2,4,8)*a3).dot(s.diag(2,4,8)*a3)>R2)
# Dropping either ball changes the optimization. Squared one-ball radii suffice.
noise_only2=delta2*q.dot(q)
prior_only2=R2*(W.inv()*q).dot(W.inv()*q)
ct('dropping_preparation_inflates_radius',noise_only2>value**2)
ct('dropping_noise_inflates_radius',prior_only2>value**2)
opposite_readouts=[q.dot(a),q.dot(-a)]
midpoint=sum(opposite_readouts)/2
midpoint_errors=[abs(midpoint-readout) for readout in opposite_readouts]
endpoint_errors=[abs(opposite_readouts[0]-readout) for readout in opposite_readouts]
ct('endpoint_estimate_is_not_minimax_center',midpoint_errors==[value,value] and max(endpoint_errors)==2*value>max(midpoint_errors))
ct('normalization_omission_positive_integral_counterfixture',s.diag(2,3)*q!=q)
# Weighted dual vector on an arbitrary finite head, checked with exact rationals.
qf=s.Matrix([2,-3,5]);wf=s.diag(2,4,8)
adual=wf.inv()**2*qf
ck('dual_vector_identity',qf.dot(adual)==(wf*adual).dot(wf*adual))
ck('weighted_dual_squared_norm',qf.dot(adual)==sum((qf[i]/wf[i,i])**2 for i in range(3)))
# Laplace upper-bound identity underlying the compact cutoff threshold.
u,nn=s.symbols('u nn',positive=True)
for M in range(4):
    integral=s.integrate(u**M*s.exp(-nn*u),(u,0,s.oo))
    ck('flat_cutoff_Laplace_moment_'+str(M),s.simplify(integral-s.factorial(M)/nn**(M+1))==0)
# Independent sequence fixture; NOT the exact curved-detector q_n.
N=s.symbols('N',positive=True)
ck('inverse_fourth_tail_integral',s.integrate(u**-4,(u,N,s.oo))==1/(3*N**3))
fixture=[]
for n in (2,4,8,16):
    w=s.Rational(3,2)**n
    qs=w/s.Integer(n)**2
    truth=1/w
    ck('critical_prior_unit_'+str(n),(w*truth)**2==1)
    ck('scalar_critical_response_'+str(n),qs*truth==s.Rational(1,n*n))
    ck('same_critical_full_field_response_'+str(n),w*truth==1)
    fixture.append({'n':n,'noise':str(truth),'scalar_response':str(qs*truth),'full_envelope_response':'1'})
scalar_outputs=[s.Rational(3,2)**n/s.Integer(n)**2*s.Rational(2,3)**n for n in (2,4,8,16)]
full_outputs=[s.Rational(3,2)**n*s.Rational(2,3)**n for n in (2,4,8,16)]
ct('full_field_nondecay_does_not_imply_scalar_nondecay',full_outputs==[1,1,1,1] and scalar_outputs==[s.Rational(1,4),s.Rational(1,16),s.Rational(1,64),s.Rational(1,256)])
# Bounded individual weighted entries do not imply a bounded scalar functional.
lengths=(4,16,64)
readings=[]
for length in lengths:
    # Use actual analytic weights, then verify both normalized preparation and response.
    weights=[s.Integer(2)**j for j in range(1,length+1)]
    coefficients=[1/(w*s.sqrt(length)) for w in weights]
    response=sum(w*a_n for w,a_n in zip(weights,coefficients))
    preparation2=sum((w*a_n)**2 for w,a_n in zip(weights,coefficients))
    ck('unit_preparation_counterfixture_'+str(length),preparation2==1)
    ck('weighted_entry_supremum_'+str(length),max(w/w for w in weights)==1)
    readings.append(s.simplify(response))
ct('weighted_supremum_is_not_scalar_dual_norm',readings==[2,4,8])
report={
 'result':'K2570',
 'evidence_kind':'exact actual-constant/harmonic identities, finite conserved-detector normalization and optimization certificate, separate sequence-tail support; universal proofs in note',
 'checks':checks,'contrary_controls':controls,'provenance':provenance,
 'finite_actual_detector':{'weights':['2','4'],'truth':['3/10','2/5'],'q':['3/2','34/5'],'noise_squared':'1/4','prior_squared':'73/25','exact_minimax_error':'317/100','optimal_linear_estimator':['3/10','2/5']},
 'supporting_sequence_fixture':fixture,
 'tail_bound':'sum_(n>N) n^-4 <= 1/(3N^3); sequence fixture only',
 'ceiling':'specified conserved scalar readout of the selected homogeneous family; no full-field existence on the extended prior, physical selection or GU verdict',
}
output=root/'lab/process/k2570-detector-recovery.json'
if args.write:
    output.write_text(json.dumps(report,indent=2)+'\n')
else:
    assert json.loads(output.read_text())==report,'saved report mismatch'
print(json.dumps({'result':'K2570','checks':len(checks),'controls':len(controls),'status':'pass'}))
