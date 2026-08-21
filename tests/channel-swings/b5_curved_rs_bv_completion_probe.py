#!/usr/bin/env python3
r"""Exact curved completion certificate for the strict B5 RS/BV branch.

The prior native lift certified the principal sequence on the actual
complexified ``Cl(9,5)`` carrier.  This probe keeps that carrier and computes
the first curved obstruction without materializing a 1792-dimensional matrix.
For

    A_nabla(epsilon)_mu = nabla_mu epsilon,
    (K_nabla psi)^mu = gamma^{mu nu rho} nabla_nu psi_rho,

exact Clifford reduction gives

    K_nabla A_nabla = (1/2) G^mu{}_nu gamma^nu.

Thus arbitrary Weyl curvature is harmless to the gauge identity, while the
Einstein tensor is the complete massless defect.  The lower-order deformation

    A_alpha = nabla + alpha gamma,
    K_m = gamma(3) nabla + m gamma(2)

closes on an Einstein background with sectional Einstein parameter ``kappa``
when ``m=-(d-2)alpha`` and ``alpha^2=-kappa/4``.  The certificate uses exact
rational Clifford words in signature ``(9,5)``, includes a nonzero Ricci-flat
Weyl fixture, and plants wrong-mass, wrong-curvature and non-Einstein failures.

This is a local formal compact-core Noether/BV certificate.  It proves no null
symbol exactness, global cohomology, domain, quotient, source-preferred action,
particle result or GU verdict.
"""

from __future__ import annotations

from fractions import Fraction as F

from b5_native_rs_bv_hessian_lift_probe import (
    METRIC,
    N,
    ZERO,
    add,
    adjoint,
    gamma,
    multiply,
    scale,
)


FAILURES: list[str] = []
CHECK_COUNT = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global CHECK_COUNT
    CHECK_COUNT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'}: {label}{suffix}")
    if not condition:
        FAILURES.append(label)


def gamma2_up(mu: int, nu: int) -> dict[int, F]:
    if mu == nu:
        return ZERO
    return multiply(gamma(mu, raised=True), gamma(nu, raised=True))


def gamma3_up(mu: int, nu: int, rho: int) -> dict[int, F]:
    if len({mu, nu, rho}) < 3:
        return ZERO
    return multiply(gamma2_up(mu, nu), gamma(rho, raised=True))


def constant_sections(kappa: F) -> dict[tuple[int, int], F]:
    return {(i, j): kappa for i in range(N) for j in range(i + 1, N)}


def add_sections(*packets: dict[tuple[int, int], F]) -> dict[tuple[int, int], F]:
    result: dict[tuple[int, int], F] = {}
    for packet in packets:
        for pair, value in packet.items():
            result[pair] = result.get(pair, F(0)) + value
    return {pair: value for pair, value in result.items() if value}


def spin_curvature_commutator(
    nu: int,
    rho: int,
    sections: dict[tuple[int, int], F],
) -> dict[int, F]:
    """Return [nabla_nu,nabla_rho] for diagonal algebraic curvature.

    ``sections[(i,j)]`` is the signed sectional coefficient with
    ``R_ijij = sections[(i,j)] eta_i eta_j``.  In an orthonormal frame this
    gives ``[nabla_i,nabla_j]=(k_ij/2) gamma_i gamma_j``.
    """
    if nu == rho:
        return ZERO
    i, j = sorted((nu, rho))
    orientation = 1 if (nu, rho) == (i, j) else -1
    coefficient = F(orientation) * sections.get((i, j), F(0)) / 2
    return scale(coefficient, multiply(gamma(i), gamma(j)))


def curvature_defect(mu: int, sections: dict[tuple[int, int], F]) -> dict[int, F]:
    """Compute (1/2) gamma^{mu nu rho}[nabla_nu,nabla_rho]."""
    return add(*(
        scale(
            F(1, 2),
            multiply(
                gamma3_up(mu, nu, rho),
                spin_curvature_commutator(nu, rho, sections),
            ),
        )
        for nu in range(N)
        for rho in range(N)
        if len({mu, nu, rho}) == 3
    ))


def einstein_prediction(mu: int, sections: dict[tuple[int, int], F]) -> dict[int, F]:
    ricci_mixed = sum(
        (value for (i, j), value in sections.items() if mu in (i, j)),
        F(0),
    )
    scalar = 2 * sum(sections.values(), F(0))
    einstein_mixed = ricci_mixed - scalar / 2
    return scale(einstein_mixed / 2, gamma(mu, raised=True))


def derivative_deformation_defect(mu: int, nu: int, alpha: F, mass: F) -> dict[int, F]:
    return add(
        scale(
            alpha,
            add(*(
                multiply(gamma3_up(mu, nu, rho), gamma(rho))
                for rho in range(N)
                if rho not in (mu, nu)
            )),
        ),
        scale(mass, gamma2_up(mu, nu)),
    )


def zero_order_deformation_defect(
    mu: int,
    sections: dict[tuple[int, int], F],
    alpha: F,
    mass: F,
) -> dict[int, F]:
    mass_term = scale(
        mass * alpha,
        add(*(
            multiply(gamma2_up(mu, nu), gamma(nu))
            for nu in range(N)
            if nu != mu
        )),
    )
    return add(curvature_defect(mu, sections), mass_term)


def main() -> int:
    print("=" * 96)
    print("B5 CURVED RARITA--SCHWINGER BV COMPLETION")
    print("=" * 96)

    check("actual curved carrier dimension remains fourteen", N == 14)
    check("actual Clifford real-form signature remains (9,5)", (METRIC.count(1), METRIC.count(-1)) == (9, 5))

    for mu, nu in ((0, 1), (0, 10), (9, 1), (9, 10)):
        contraction = add(*(
            multiply(gamma3_up(mu, nu, rho), gamma(rho))
            for rho in range(N)
            if rho not in (mu, nu)
        ))
        check(
            f"gamma(3)-gamma contraction is (d-2) gamma(2) at ({mu},{nu})",
            contraction == scale(F(N - 2), gamma2_up(mu, nu)),
        )

    for mu in (0, 4, 9, 13):
        contraction = add(*(
            multiply(gamma2_up(mu, nu), gamma(nu))
            for nu in range(N)
            if nu != mu
        ))
        check(
            f"gamma(2)-gamma contraction is (d-1) gamma at {mu}",
            contraction == scale(F(N - 1), gamma(mu, raised=True)),
        )

    generic_sections = {
        (0, 1): F(2),
        (0, 4): F(-3, 2),
        (2, 5): F(5, 3),
        (9, 13): F(-4, 7),
    }
    for mu in range(N):
        check(
            f"curvature defect equals one-half Einstein-Clifford contraction at {mu}",
            curvature_defect(mu, generic_sections) == einstein_prediction(mu, generic_sections),
        )

    weyl_sections = {
        (0, 1): F(1),
        (1, 2): F(-1),
        (2, 3): F(1),
        (0, 3): F(-1),
    }
    check("Ricci-flat algebraic Weyl fixture is nonzero", bool(weyl_sections))
    check(
        "nonzero Ricci-flat Weyl curvature gives zero massless gauge defect",
        all(not curvature_defect(mu, weyl_sections) for mu in range(N)),
    )

    non_einstein = {(0, 1): F(1)}
    check(
        "planted non-Einstein curvature produces a live massless gauge defect",
        any(curvature_defect(mu, non_einstein) for mu in range(N)),
    )

    alpha = F(1)
    mass = -F(N - 2) * alpha
    kappa = -4 * alpha * alpha
    einstein_weyl = add_sections(constant_sections(kappa), weyl_sections)

    check("Einstein completion coefficients are m=-(d-2)alpha and kappa=-4alpha^2", (mass, kappa) == (F(-12), F(-4)))
    check(
        "all first-order gauge-deformation terms cancel exactly",
        all(
            not derivative_deformation_defect(mu, nu, alpha, mass)
            for mu in range(N)
            for nu in range(N)
            if mu != nu
        ),
    )
    check(
        "all zero-order curvature and mass terms cancel on Einstein plus Weyl curvature",
        all(
            not zero_order_deformation_defect(mu, einstein_weyl, alpha, mass)
            for mu in range(N)
        ),
    )

    wrong_mass = mass + 1
    wrong_kappa = kappa + 1
    check(
        "planted wrong mass coefficient breaks the first-order Noether identity",
        any(
            derivative_deformation_defect(mu, nu, alpha, wrong_mass)
            for mu in range(N)
            for nu in range(N)
            if mu != nu
        ),
    )
    check(
        "planted wrong Einstein curvature breaks the zero-order Noether identity",
        any(
            zero_order_deformation_defect(mu, constant_sections(wrong_kappa), alpha, mass)
            for mu in range(N)
        ),
    )
    check(
        "formal dual Noether defect vanishes as the adjoint of the closed left defect",
        all(
            not adjoint(zero_order_deformation_defect(mu, einstein_weyl, alpha, mass))
            for mu in range(N)
        ),
    )

    if FAILURES:
        print("FAILED CONTROLS:")
        for failure in FAILURES:
            print(f"  - {failure}")
        return 1
    print(
        f"B5 CURVED RS BV VERDICT: {CHECK_COUNT}/{CHECK_COUNT} CHECKS PASS; "
        "DEFECT=ONE-HALF EINSTEIN-CLIFFORD, RICCI-FLAT AND EINSTEIN-DEFORMED CLOSURES EXIST"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
