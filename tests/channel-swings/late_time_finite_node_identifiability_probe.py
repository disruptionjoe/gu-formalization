#!/usr/bin/env python3
"""Exact finite controls for the written FLRW interpolation/variation result.

No data fit, native GU cosmology, survey-window test, or continuum certification.
Default execution checks a clean baseline and actual altered-equation faults.
The script writes no files and uses only small symbolic expressions.
"""
import json

import sympy as s


FAULTS = (
    "curvature_sign",
    "bump_normalization",
    "upper_exponent",
    "lower_area_sign",
    "tent_switch",
    "endpoint_limit",
    "trace_coefficient",
    "redshift_sign",
    "action_quadratic_sign",
    "friedmann_vacuum_factor",
    "constraint_transport",
)


def controls(fault=None):
    out = {}

    def check(name, condition):
        out[name] = bool(s.simplify(condition))

    def equal(name, actual, expected):
        check(name, s.simplify(actual - expected) == 0)

    # Equation (1): actual independent flat/open/closed functions.
    z = s.symbols("z", real=True)
    curvature_sign = -1 if fault == "curvature_sign" else 1
    for name, m, kap in (
        ("flat", z, s.S.Zero),
        ("open", s.sinh(z), s.S.One),
        ("closed", s.sin(z), -s.S.One),
    ):
        equal("curvature_identity_" + name,
              s.diff(m, z) ** 2, 1 + curvature_sign * kap * m ** 2)
    check("closed_before_turnover", s.cos(s.pi / 3) > 0)
    check("closed_after_turnover_requires_other_branch", s.cos(2 * s.pi / 3) < 0)
    equal("closed_inverse_branch_area", s.asin(s.sqrt(3) / 2), s.pi / 3)
    equal("open_inverse_branch_area", s.asinh(s.sqrt(3)).rewrite(s.log), s.log(2 + s.sqrt(3)))

    # Exact C2 illustration of the smooth-bump proof, deliberately very narrow.
    # The written proof, not this polynomial, establishes arbitrary C-infinity data.
    t = s.symbols("t", nonnegative=True)
    cutoff = (1 - t) ** 3 * (1 + 3 * t + 6 * t ** 2)
    equal("cutoff_integral", s.integrate(cutoff, (t, 0, 1)), s.Rational(1, 2))
    equal("cutoff_derivative_sign_factor", s.diff(cutoff, t), -30 * t ** 2 * (1 - t) ** 2)
    check("cutoff_endpoint_values", cutoff.subs(t, 0) == 1 and cutoff.subs(t, 1) == 0)
    check("cutoff_two_flat_jets", all(s.diff(cutoff, t, j).subs(t, u) == 0
                                    for j in (1, 2) for u in (0, 1)))
    a, b, eps, width = s.Integer(100), s.S.One, s.Rational(1, 1000), s.Rational(1, 10000)
    target = s.Rational(1, 10)
    base_area = eps + (a + b - 2 * eps) * width / 2
    bump = (70 if fault == "bump_normalization" else 140) * t ** 3 * (1 - t) ** 3
    coeff = target - base_area
    check("positive_interpolation_coefficients", a > eps and b > eps and eps > 0
          and 0 < width < s.Rational(1, 2) and coeff > 0)
    equal("interpolation_total_area", base_area + coeff * s.integrate(bump, (t, 0, 1)), target)
    check("bump_preserves_two_endpoint_jets", all(s.diff(bump, t, j).subs(t, u) == 0
                                                for j in (0, 1, 2) for u in (0, 1)))
    equal("left_interpolation_endpoint", eps + (a - eps) * cutoff.subs(t, 0), a)
    equal("right_interpolation_endpoint", eps + (b - eps) * cutoff.subs(t, 0), b)
    # Positivity on each piece follows from the displayed factorizations and coefficients.

    # General area formulas independently checked against exponential integration.
    # Choose endpoint ratio exp(2q), interval 2d, and 0<q<d so switches are interior.
    # L=1 is sufficient to verify the algebra; scaling tests below cover general L.
    q, d, A = s.symbols("q d A", positive=True)
    B = A * s.exp(2 * q)
    switch_minus = d - q
    switch_plus = d - q if fault == "tent_switch" else d + q
    direct_minus = s.integrate(A * s.exp(-t), (t, 0, switch_minus)) + s.integrate(
        B * s.exp(-(2 * d - t)), (t, switch_minus, 2 * d))
    direct_plus = s.integrate(A * s.exp(t), (t, 0, switch_plus)) + s.integrate(
        B * s.exp(2 * d - t), (t, switch_plus, 2 * d))
    lower_sign = 1 if fault == "lower_area_sign" else -1
    formula_minus = A + B + lower_sign * 2 * A * s.exp(q - d)
    exponent = -d if fault == "upper_exponent" else d
    formula_plus = 2 * A * s.exp(q + exponent) - A - B
    equal("lower_area_independent_integral", direct_minus, formula_minus)
    equal("upper_area_independent_integral", direct_plus, formula_plus)
    equal("lower_envelope_switch_continuity", A * s.exp(-switch_minus), B * s.exp(-(2*d-switch_minus)))
    equal("upper_envelope_switch_continuity", A * s.exp(switch_plus), B * s.exp(2*d-switch_plus))

    # Synthetic exact cases: L=2log2, Delta=1, endpoints 1 and 1.
    ell = 2 * s.log(2)
    lo = (2 - 2 * s.exp(-ell / 2)) / ell
    hi = (2 * s.exp(ell / 2) - 2) / ell
    equal("symmetric_lower_area", lo, 1 / (2 * s.log(2)))
    equal("symmetric_upper_area", hi, 1 / s.log(2))
    check("synthetic_interior_pass", lo < 3 / (4 * s.log(2)) < hi)
    check("synthetic_low_area_rejected", 1 / (4 * s.log(2)) < lo)
    check("synthetic_high_area_rejected", 2 / s.log(2) > hi)
    theta = s.Rational(1, 2)
    equal("convex_mixture_exact_area", (1 - theta) * lo + theta * hi, 3 / (4 * s.log(2)))

    # Saturated endpoint compatibility is an exact exponential bridge.
    def envelope_areas(x, y, L, delta):
        return ((x+y-2*s.sqrt(x*y)*s.exp(-L*delta/2))/L,
                (2*s.sqrt(x*y)*s.exp(L*delta/2)-x-y)/L)

    sat_lo, sat_hi = envelope_areas(s.S.One, s.Integer(4), ell, s.S.One)
    equal("saturated_endpoint_lower", sat_lo, 3 / ell)
    equal("saturated_endpoint_upper", sat_hi, 3 / ell)
    endpoint_ratio = s.Integer(4) if fault == "endpoint_limit" else s.Integer(8)
    check("incompatible_endpoint_rejected", s.log(endpoint_ratio) > ell)
    L = s.symbols("L", positive=True)
    lim_lo, lim_hi = envelope_areas(A, A, L, d)
    equal("zero_L_lower_limit", s.limit(lim_lo, L, 0, dir="+"), A*d)
    equal("zero_L_upper_limit", s.limit(lim_hi, L, 0, dir="+"), A*d)
    check("unbounded_L_lower_to_zero", s.limit(lim_lo, L, s.oo) == 0)
    check("unbounded_L_upper_diverges", s.limit(lim_hi, L, s.oo) == s.oo)

    # Global unit dilation: H->H/scale, distances and ruler->scale, K->K/scale^2.
    scale, H, rd, c, DM = s.symbols("scale H rd c DM", positive=True)
    K = s.symbols("K", real=True)
    equal("ruler_dilation_radial_invariant", c / ((H/scale)*(rd*scale)), c/(H*rd))
    equal("ruler_dilation_transverse_invariant", (DM*scale)/(rd*scale), DM/rd)
    equal("ruler_dilation_curvature_invariant", -(K/scale**2)*(rd*scale)**2, -K*rd**2)
    equal("AP_ruler_cancellation", (DM/rd)/(c/(H*rd)), DM*H/c)

    # Initial derivative algebra, followed by the complete conditional local
    # homogeneous vacuum f(R) constraint. Neither identifies the ambient GU action.
    H0 = s.symbols("H0", positive=True)
    speed, P, alpha, lam, rho = s.symbols("speed P alpha lam rho", real=True, nonzero=True)
    R0 = (3 if fault == "trace_coefficient" else 6) * (2 + speed) * H0**2
    Hdot = R0/6 - 2*H0**2
    zdot = H0 if fault == "redshift_sign" else -H0
    equal("arbitrary_initial_log_H_derivative", Hdot/(H0*zdot), -speed)
    Pdot = (alpha*R0-2*rho)/lam - 3*H0*P
    equal("trace_equation_algebra", alpha*R0-lam*(Pdot+3*H0*P), 2*rho)

    R, u, beta, gain, bcoef = s.symbols("R u beta gain bcoef", real=True, nonzero=True)
    original = (alpha + beta*u)*R + gain*u**2/2 - rho
    eliminated = s.expand(original.subs(u, -beta*R/gain))
    quad_sign = 1 if fault == "action_quadratic_sign" else -1
    f = alpha*R + quad_sign*bcoef*R**2/2 - rho
    equal("algebraic_action_elimination", eliminated, f.subs(bcoef, beta**2/gain))
    F = s.diff(f, R)
    equal("metric_action_derivative", F, alpha-bcoef*R)
    Hdot_full = R/6 - 2*H**2
    Pdot_full = (alpha*R-2*rho)/(3*bcoef) - 3*H*P
    vacuum_factor = s.S.One if fault == "friedmann_vacuum_factor" else s.Rational(1, 2)
    C = 3*(alpha-bcoef*R)*H**2 + bcoef*R**2/4 - vacuum_factor*rho - 3*bcoef*H*P
    standard_00 = 3*F*H**2 - (F*R-f)/2 + 3*H*s.diff(F, R)*P
    equal("00_equation_from_metric_action", C, standard_00)
    Cdot = s.diff(C, H)*Hdot_full + s.diff(C, R)*P + s.diff(C, P)*Pdot_full
    transport = -3 if fault == "constraint_transport" else -4
    equal("full_constraint_propagation", Cdot, transport*H*C)
    P_constraint = (3*(alpha-bcoef*R)*H**2+bcoef*R**2/4-rho/2)/(3*bcoef*H)
    equal("initial_P_solves_vacuum_constraint", C.subs(P, P_constraint), 0)
    # -2 F Hdot = Fddot-H Fdot, with Fdot=-bP and Fddot=-bPdot.
    spatial_residual = -2*(alpha-bcoef*R)*Hdot_full + bcoef*Pdot_full - bcoef*H*P
    equal("independent_spatial_equation", spatial_residual.subs(P, P_constraint), 0)
    # Exact positive-F unbounded directions, with n>0 and fixed H,alpha,b.
    n, bpositive = s.symbols("n bpositive", positive=True)
    equal("positive_b_unbounded_R_branch", (alpha-bpositive*R).subs(R, alpha/bpositive-n), bpositive*n)
    equal("negative_b_unbounded_R_branch", (alpha+bpositive*R).subs(R, -alpha/bpositive+n), bpositive*n)
    return out


def main():
    baseline = controls()
    failures = [name for name, passed in baseline.items() if not passed]
    if failures:
        print(json.dumps({"status": "FAIL", "baseline_failures": failures}, indent=2))
        raise SystemExit(1)
    catches = {}
    for fault in FAULTS:
        altered = controls(fault)
        failures = [name for name, passed in altered.items() if not passed]
        if not failures:
            print(json.dumps({"status": "FAIL", "undetected_fault": fault}, indent=2))
            raise SystemExit(1)
        catches[fault] = failures
    print(json.dumps({
        "status": "PASS",
        "exact_checks": len(baseline),
        "faults_rejected": len(catches),
        "checks": list(baseline),
        "fault_failures": catches,
        "evidence": "Finite exact controls; universal interpolation, Lipschitz feasibility and ODE existence are written proofs requiring separate review.",
        "scope": "Synthetic geometric interface, no observed-data likelihood or native GU cosmological forecast.",
    }, indent=2))


if __name__ == "__main__":
    main()
