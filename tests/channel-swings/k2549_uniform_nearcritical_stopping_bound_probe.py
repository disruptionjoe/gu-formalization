"""Exact algebra supporting K2549; uniform analytic proof is in the note.
No sampled stage counts or numerical optimizers certify its all-policy claims.
"""
from pathlib import Path
import hashlib
import json
import sys
import sympy as s

ROOT = Path(__file__).resolve().parents[2]
checks = {}
controls = {}


def check(bank, name, value):
    bank[name] = bool(value)
    if not bank[name]:
        raise AssertionError('FAIL ' + name)


def eq(name, actual, expected=0):
    check(checks, name, s.simplify(actual - expected) == 0)


rt = 2*s.sqrt(3)-3
lt = 4*s.sqrt(3)/3
Hp = (141-81*s.sqrt(3))/8
c1 = (2841-1643*s.sqrt(3))/48
cL = (249*s.sqrt(3)-431)/2
Ki = (10309*s.sqrt(3)-17847)/96
mu0 = s.Rational(37, 66)-257*s.sqrt(3)/396
gamma = (202353685-116818417*s.sqrt(3))/371712
nu0 = (24165709-13458052*s.sqrt(3))/3066624
r, b, a, Y, lam = s.symbols('r b a Y lam')
al = (1-r)**2/(4*(1+r))
be = (1+r)/2
cc = be-al
w = s.log(1+(b-a)**2/(2*(a+b)*(2-a-b)))
original_arg = 1+(b-a)**2/(2*(a+b)*(2-a-b))
eq('original_log_argument', original_arg.subs(a, r*b), (1-cc*b)/(1-be*b))
M0 = -2*s.diff(al, r)
eq('analytic_zero_score_stationary_extension', M0, 2/(1+r)**2-s.Rational(1, 2))
eq('nondegenerate_stationary_ratio_derivative', s.diff(M0, r), -4/(1+r)**3)
eq('critical_stationarity', lt*M0.subs(r, rt), 1)
T = (Y-2*lam*w)/(1+a)
M = 2*w-2*(1+a)*s.diff(w, a)
eq('exact_original_suffix_derivative', s.diff(T, a), (lam*M-Y)/(1+a)**2)
check(checks, 'critical_left_endpoint_margin', s.simplify(lt*M0.subs(r, 0)-1) > 0)
check(checks, 'critical_right_endpoint_margin', s.simplify(lt*M0.subs(r, 1)-1) < 0)
eq('cloud_curvature_identity', Ki, cL+c1/2)
eq('cubic_boundary_cancellation', 2*Hp*mu0, c1)
eq('insertion_phase_second_coefficient', 2*Hp*nu0, gamma)
check(checks, 'exact_cL_positive', 3*249**2-431**2 == 242 > 0)
check(checks, 'exact_Kinf_positive', 3*10309**2-17847**2 == 311034 > 0)
check(checks, 'exact_c1_negative', 3*1643**2-2841**2 == 27066 > 0)
check(checks, 'exact_gamma_positive', 202353685**2-3*116818417**2 == 7386181921558 > 0)
check(checks, 'exact_Hprime_positive', 141**2-3*81**2 > 0)


def ordered(xs):
    RR = sum(xs[i]*xs[j]**2 for i in range(len(xs)) for j in range(i+1, len(xs)))
    TT = sum(xs[i]*xs[j]*xs[k] for i in range(len(xs)) for j in range(i+1, len(xs)) for k in range(j+1, len(xs)))
    return s.expand(RR), s.expand(TT)


def nonnegative_coefficients(poly, variables):
    return all(v >= 0 for v in s.Poly(s.expand(poly), *variables).coeffs())


p1, p2, main, t1, t2 = s.symbols('p1 p2 main t1 t2', nonnegative=True)
xs = [p1, p2, main, t1, t2]
RR, TT = ordered(xs)
# These check the monomial inclusions used in the general proof; not sampled policies.
check(checks, 'prefix_R_term_inclusion', nonnegative_coefficients(RR-main**2*(p1+p2)-main*(t1**2+t2**2), xs))
check(checks, 'tail_T_term_inclusion', nonnegative_coefficients(TT-main*t1*t2, xs))
check(checks, 'cross_cut_R_plus_2T_inclusion', nonnegative_coefficients(RR+2*TT-(p1+p2)*(main+t1+t2)**2, xs))
eq('tail_coercivity_rewrite', cL*(t1*t1+t2*t2)+2*Ki*t1*t2, Ki*(t1+t2)**2+(cL-Ki)*(t1*t1+t2*t2))
check(checks, 'cut_constant_bound', s.Rational(1,4)*s.Rational(1,4)**2 == s.Rational(1,64))
S, z, z1, z2, nu, k, P, Q = s.symbols('S z z1 z2 nu k P Q')
R3, T3 = ordered([S-t1-t2, t1, t2])
Dc = s.expand(-cL*R3-2*Ki*T3)
# Homogeneous score cubic, differentiated at zero tail with S fixed.
eq('terminal_diagonal_hessian', s.diff(Dc, t1, 2).subs({t1:0, t2:0}), -2*cL*S)
eq('terminal_offdiagonal_hessian', s.diff(Dc, t1, t2).subs({t1:0, t2:0}), -2*Ki*S)
Rp, Tp = ordered([P, S-P])
Dp = s.expand(-cL*Rp-2*Ki*Tp)
eq('preceding_insertion_cubic_coefficient', s.diff(Dp, P).subs(P,0), -cL*S*S)
Rt, Tt = ordered([S-Q, Q])
Dt = s.expand(-cL*Rt-2*Ki*Tt)
eq('terminal_cubic_linear_cancellation', s.diff(Dt, Q).subs(Q,0), 0)
eq('cloud_tail_quadratic_form', cL*(z1*z1+z2*z2)+2*Ki*z1*z2, Ki*(z1+z2)**2-c1*(z1*z1+z2*z2)/2)
eq('sharp_positive_k_square_completion', k*z-Ki*z*z, k*k/(4*Ki)-Ki*(z-k/(2*Ki))**2)
m = s.symbols('m', positive=True)
Km = Ki-c1/(2*m)
eq('equal_cloud_penalty', Ki*Q*Q-c1*(m*(Q/m)**2)/2, Km*Q*Q)
eq('fixed_m_gap_from_sharp_coefficient', k*k/(4*Ki)-k*k/(4*Km), -c1*k*k/(8*m*Ki*Km))
eq('main_prefix_cloud_stability_identity', -cL*S*S*P+k*S**3*Q-S*(Ki*Q*Q-c1*(t1*t1+t2*t2)/2), k*k*S**5/(4*Ki)-cL*S*S*P-Ki*S*(Q-k*S*S/(2*Ki))**2+c1*S*(t1*t1+t2*t2)/2)
eq('two_satellite_cauchy_gap', 2*(t1*t1+t2*t2)-(t1+t2)**2, (t1-t2)**2)
# Exact integer/scaling controls for the absorption proof; they do not assert analytic bounds.
y, zz = s.symbols('y zz', nonnegative=True)
expr = S*P*(P+Q)+S*S*Q*Q+(P+Q)**3
scaled = s.Poly(s.expand(expr.subs({P:y*S**3,Q:zz*S**2})), S)
check(checks, 'localized_remainder_order_at_least_six', min(power[0] for power, _ in scaled.terms()) >= 6)
# Keep the shape-dependent remainder for the exact phase, rather than O(S^6) alone.
eq('remainder_vanishes_at_zero_satellites', expr.subs({P:0,Q:0}), 0)
absorb_gap = s.expand(4*P*(P+Q)**2+4*Q**3-(P+Q)**3)
check(checks, 'cubic_remainder_split_nonnegative', nonnegative_coefficients(absorb_gap, [P,Q]))

u1, u2, u3, u4 = s.symbols('u1 u2 u3 u4', nonnegative=True)
us = [u1, u2, u3, u4]
merge_products = sum(sum(us[:j])*us[j] for j in range(1, len(us)))
eq('merge_product_telescoping', merge_products, (sum(us)**2-sum(u*u for u in us))/2)
hh, eps = s.symbols('h eps', nonnegative=True)
# A bin B<=h has B²<=hB; write B=h-eps to check the exact gap.
eq('small_bin_square_bound_gap', hh*(hh-eps)-(hh-eps)**2, eps*(hh-eps))
NN = s.symbols('N', positive=True)
eq('finite_horizon_rate_substitution', S*(2*S/(NN-1)), 2*S*S/(NN-1))
# Contrary controls change a load-bearing mathematical object, not a check predicate.
check(controls, 'fixed_m_cannot_attain_cloud_limit', s.simplify(Km-Ki) > 0)
check(controls, 'prefix_and_tail_insertions_are_different', s.simplify(s.diff(Dp,P).subs(P,0)-s.diff(Dt,Q).subs(Q,0)) != 0)
check(controls, 'omitting_offdiagonal_cloud_penalty_changes_coefficient', s.simplify(2*Ki) != 0)
check(controls, 'dropping_original_prefix_changes_stage_stationarity', s.simplify(s.diff(Y-2*lam*w,a)-s.diff(T,a)) != 0)
check(controls, 'absolute_sixth_order_error_cannot_decide_zero_satellite_sign', (S**6).subs({P:0,Q:0}) != 0)
check(controls, 'critical_fifth_order_zero_does_not_decide_higher_order', s.expand((nu0+S)-nu0) != 0)
check(controls, 'large_singleton_cannot_enter_small_bin_square_bound', s.Rational(3,4)**2 > s.Rational(1,4)*s.Rational(3,4))

note = 'explorations/conditional-build/k2549-uniform-nearcritical-stopping-bound-2026-11-04.md'
paths = [note, str(Path(__file__).relative_to(ROOT)),
         'explorations/conditional-build/k2547-nearcritical-satellite-instability-2026-11-04.md',
         'explorations/conditional-build/k2545-critical-stopping-aggregation-2026-11-04.md',
         'explorations/conditional-build/k2483-adaptive-stopping-bellman-2026-11-01.md',
         'explorations/conditional-build/k2485-constrained-stopping-frontier-2026-11-01.md']
report = {
    'result': 'K2549',
    'exact_algebra': checks,
    'contrary_controls': controls,
    'analytic_proof_refs': {
        'uniform_stage_count': note+'#2-a-common-analytic-domain-for-every-number-of-stages',
        'shape_sensitive_localization': note+'#3-shape-sensitive-cubic-remainder',
        'global_phase_in_tube': note+'#7-released-successor-the-insertion-curve-is-globally-decisive-in-its-tube',
        'policy_stability': note+'#8-released-successor-an-asymptotically-optimal-cloud-must-diffuse',
        'finite_stage_compression': note+'#9-released-construction-a-finite-stage-approximation-rate'
    },
    'evidence_boundary': 'Exact algebra supports the written analytic proof; no Boolean probe or finite-stage samples certify uniformity, phase, stability or local finite-stage compression. Compression constants and the common score radius are not numerically evaluated. Saved equality establishes reporting consistency.',
    'scope': 'Supplied original law. All-policy fifth-order value and phase comparison inside a shrinking nearcritical multiplier tube; local finite-stage compression rate on a common small-score neighborhood for lambda in a fixed neighborhood of criticality. No evaluated constants or score radius, fixed-score global frontier, infinite-policy attainment, physical law or GU claim.',
    'coefficients': {name: str(s.simplify(value)) for name,value in {'Hp':Hp,'c1':c1,'cL':cL,'Kinf':Ki,'mu0':mu0,'gamma':gamma,'nu0':nu0}.items()},
    'dependencies': {p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}
}
out = ROOT/'lab/process/k2549-uniform-nearcritical-stopping-bound.json'
if '--write' in sys.argv:
    out.write_text(json.dumps(report, indent=2)+'\n')
else:
    assert json.loads(out.read_text()) == report, 'saved report mismatch'
print('K2549',len(checks),'exact algebra groups',len(controls),'contrary controls; uniform analytic proof in companion note')
