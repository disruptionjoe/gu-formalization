#!/usr/bin/env python3
"""W191: exact projected I1B + native-current quadratic-block audit.

This is a lightweight symbolic audit of the one-mode block pre-registered in
W190.  It does not implement the full GU representation, the full shiab, or a
QFT C-operator.  It tests what follows exactly once the typed projected block
is fixed.
"""

from __future__ import annotations

import sys

import sympy as sp


checks = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global checks
    if not bool(condition):
        print(f"[FAIL] {label}" + (f" -- {detail}" if detail else ""))
        raise AssertionError(label)
    checks += 1
    print(f"[PASS] {label}" + (f" -- {detail}" if detail else ""))


def section(name: str) -> None:
    print("\n" + "=" * 88)
    print(name)
    print("=" * 88)


def main() -> int:
    h, tau, j = sp.symbols("h tau j", real=True)
    q, kappa, c, eps = sp.symbols("q kappa c eps", nonzero=True, real=True)

    section("A -- exact same-carrier I1B/current block")

    # The projected quadratic block at B0 flat, T0=0:
    #   eps [ tau q h + 1/2 tau c tau - kappa tau j ].
    # q is the projected shiab-curvature form factor; c is the projected
    # symmetric torsion kernel; eps is the declared Krein type.
    action = eps * (tau * q * h + sp.Rational(1, 2) * c * tau**2 - kappa * tau * j)
    eom_tau = sp.diff(action, tau)
    tau_star = sp.solve(sp.Eq(eom_tau, 0), tau)[0]
    expected_tau = (kappa * j - q * h) / c
    check("A1 projected torsion stationary point", sp.simplify(tau_star - expected_tau) == 0,
          f"tau*={tau_star}")

    effective = sp.factor(action.subs(tau, tau_star))
    expected_effective = -eps * (q * h - kappa * j) ** 2 / (2 * c)
    check("A2 exact Schur/Legendre effective action",
          sp.simplify(effective - expected_effective) == 0,
          f"S_eff={effective}")

    x = sp.Matrix([h, j])
    delta_kernel = sp.hessian(effective, x)
    expected_kernel = -(eps / c) * sp.Matrix(
        [[q**2, -q * kappa], [-q * kappa, kappa**2]]
    )
    check("A3 induced two-sector kernel is the expected outer product",
          sp.simplify(delta_kernel - expected_kernel) == sp.zeros(2),
          f"DeltaK={delta_kernel}")
    check("A4 same-carrier correction has determinant zero",
          sp.simplify(delta_kernel.det()) == 0)
    check("A5 same-carrier correction has generic rank one",
          delta_kernel.subs({q: 2, kappa: 3, c: 5, eps: 1}).rank() == 1)
    check("A6 cross-sector relation Delta_hj^2 = Delta_hh Delta_jj",
          sp.simplify(delta_kernel[0, 1] ** 2 - delta_kernel[0, 0] * delta_kernel[1, 1]) == 0)

    full_hessian = sp.hessian(action, sp.Matrix([h, j, tau]))
    schur_from_full = sp.simplify(
        full_hessian[:2, :2]
        - full_hessian[:2, 2:] * full_hessian[2:, 2:].inv() * full_hessian[2:, :2]
    )
    check("A7 full block Schur complement reproduces DeltaK",
          sp.simplify(schur_from_full - delta_kernel) == sp.zeros(2))

    section("B -- law-shadow coefficient and physical-pole gates")

    trace_t = sp.symbols("trace_t", real=True)
    c_r_base = -2 * trace_t**2 + trace_t - sp.Rational(1, 6)
    check("B1 shiab-family discriminant is negative",
          sp.discriminant(c_r_base, trace_t) == -sp.Rational(1, 3))
    check("B2 Einstein shiab point has Ricci-class c_R=-1/6",
          c_r_base.subs(trace_t, sp.Rational(1, 2)) == -sp.Rational(1, 6))

    c0 = sp.symbols("c0", positive=True, real=True)
    c_r_eff = sp.factor(eps * c_r_base / c0)
    check("B3 operative Krein type flips the local induced scalar sign",
          c_r_eff.subs({trace_t: sp.Rational(1, 2), eps: 1}) < 0
          and c_r_eff.subs({trace_t: sp.Rational(1, 2), eps: -1}) > 0,
          f"c_R_eff={c_r_eff}")

    s, gamma, b = sp.symbols("s gamma b", positive=True, real=True)
    k_eff_algebraic = sp.factor(gamma * s - eps * b**2 * s**2 / c0)
    nonzero_root = sp.solve(sp.Eq(k_eff_algebraic / s, 0), s)[0]
    check("B4 derivative mixing can create an additional full-block zero",
          sp.simplify(nonzero_root - gamma * c0 / (eps * b**2)) == 0,
          f"s_extra={nonzero_root}")

    c1 = sp.symbols("c1", nonzero=True, real=True)
    c_dynamic = c0 + c1 * s
    c_zero = sp.solve(sp.Eq(c_dynamic, 0), s)[0]
    check("B5 projected d_B T kernel creates an auxiliary-invertibility gate",
          sp.simplify(c_zero + c0 / c1) == 0,
          f"C_T=0 at s={c_zero}")

    section("C -- reservoir spectral sign")

    a, rho = sp.symbols("a rho", real=True)
    complex_c = a + sp.I * rho
    retarded_factor = sp.simplify(-eps / complex_c)
    imag_factor = sp.simplify(sp.im(sp.expand_complex(retarded_factor)))
    expected_imag = sp.simplify(eps * rho / (a**2 + rho**2))
    check("C1 imaginary self-energy sign is the relative Krein/spectral sign",
          sp.simplify(imag_factor - expected_imag) == 0,
          f"Im(-eps/C_R)={imag_factor}")
    check("C2 ultralocal real W180 kernel has no damping width",
          imag_factor.subs(rho, 0) == 0)
    check("C3 changing magnitude cannot rescue the wrong spectral sign",
          sp.sign(imag_factor.subs({eps: 1, a: 2, rho: 3}))
          == -sp.sign(imag_factor.subs({eps: -1, a: 2, rho: 3})))

    section("D -- selector rank and predictive relation")

    outputs = sp.Matrix([q**2 / c, q * kappa / c, kappa**2 / c])
    jac_q_kappa = outputs.jacobian(sp.Matrix([q, kappa]))
    check("D1 unbuilt reduction amplitude plus source magnitude have generic rank two",
          jac_q_kappa.subs({q: 2, kappa: 3, c: 5}).rank() == 2)
    check("D2 three induced coefficients obey one target-free relation",
          sp.simplify(outputs[1] ** 2 - outputs[0] * outputs[2]) == 0)

    boundary_outputs_q_fixed = sp.Matrix([q * kappa / c, kappa**2 / c])
    jac_kappa = boundary_outputs_q_fixed.jacobian(sp.Matrix([kappa]))
    check("D3 after q is derived, the remaining magnitude response is rank one",
          jac_kappa.subs({q: 2, kappa: 3, c: 5}).rank() == 1)

    c_source, c_shadow = sp.symbols("c_source c_shadow", positive=True, real=True)
    separate_carrier = sp.diag(-eps * q**2 / c_shadow, -eps * kappa**2 / c_source)
    check("D4 separate source and shadow carriers generically destroy the rank-one relation",
          sp.simplify(separate_carrier.det()) != 0,
          f"det={sp.factor(separate_carrier.det())}")

    section("E -- everpresent-fade scope control")

    n_records, kappa0, g_kin, r_star = sp.symbols(
        "N kappa0 g_kin r_star", positive=True, real=True
    )
    ratio_n = kappa0 * sp.sqrt(n_records) / g_kin
    n_star = sp.solve(sp.Eq(ratio_n, r_star), n_records)[0]
    check("E1 positive growing source eventually crosses a fixed threshold",
          sp.simplify(n_star - (r_star * g_kin / kappa0) ** 2) == 0,
          f"N*={n_star}")
    check("E2 crossing epoch still depends on the unbuilt source magnitude",
          sp.simplify(sp.diff(n_star, kappa0)) != 0,
          f"dN*/dkappa0={sp.diff(n_star, kappa0)}")
    check("E3 the fade removes magnitude from the eventual-basin bit, not from predictions",
          sp.limit(ratio_n, n_records, sp.oo) == sp.oo)

    section("F -- verdict")
    print(
        "The actual displayed I1B + W180 same-carrier block forces a rank-one induced\n"
        "shadow/source kernel and one target-free cross-sector relation.  It fixes the\n"
        "Gaussian shadow to the shiab/Ricci class, not geometric |II|^2.  It does not\n"
        "fix the physical pole, the nonlocal spectral sign, or the source magnitude:\n"
        "those require the full projected shiab/torsion kernel and reservoir two-point\n"
        "function.  The everpresent growth can guarantee eventual threshold crossing\n"
        "for the favorable sign, while the crossing epoch still carries kappa0."
    )
    print(f"\nW191: {checks}/{checks} checks passed")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # pragma: no cover - explicit nonzero audit failure
        print(f"W191 FAILED: {exc}")
        sys.exit(1)
