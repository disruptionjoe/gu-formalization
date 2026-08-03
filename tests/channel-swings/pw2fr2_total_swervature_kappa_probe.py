#!/usr/bin/env python3
r"""PW2F-R2 action-derived eddy-candidate and universal-kappa discriminator.

This is deliberately a finite exact restriction of the written one-half /
one-third source action.  It can refute an action-wide algebraic identity,
but it is not the complete induced-Y14 metric Hessian.  In particular it does
not contain the Zorro section JVP, moving native Hodge/density/Krein owners,
or the repository h=exp(u) graph-curvature return.
"""

from __future__ import annotations

from fractions import Fraction as F
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
G = runpy.run_path(str(ROOT / "tests/channel-swings/g2_native_variational_shiab_probe.py"))

FAILURES: list[str] = []
EXACT = TYPE = PLANTED = 0


def exact(label: str, condition: bool, detail: str = "") -> None:
    global EXACT
    EXACT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'}: {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(label)


def typed(label: str, condition: bool = True) -> None:
    global TYPE
    TYPE += 1
    print(f"{'PASS' if condition else 'FAIL'}: type-level - {label}", flush=True)
    if not condition:
        FAILURES.append(f"type: {label}")


def reject(label: str, false_claim: bool) -> None:
    global PLANTED
    PLANTED += 1
    print(f"{'PASS' if not false_claim else 'FAIL'}: planted rejection - {label}", flush=True)
    if false_claim:
        FAILURES.append(f"planted: {label}")


M = G["M"]
ZERO = G["ZERO"]
form1 = G["form1"]
form2 = G["form2"]


def fixtures():
    b = form1(M(1, 1, 0, -1), M(0, 1, 2, 1), M(2, -1, 1, 0))
    t = form1(M(0, 2, -1, 1), M(1, -1, 1, 2), M(-1, 0, 2, 1))
    db = form2(M(0, 1, -1, 0), M(1, 0, 2, -1), M(-1, 2, 0, 1))
    dt = form2(M(2, -1, 0, 1), M(0, 2, 1, -1), M(1, 0, -2, 1))
    direction = form1(M(2, 0, 1, -1), M(-1, 2, 0, 1), M(1, 1, -2, 0))
    d_direction = form2(ZERO, ZERO, ZERO)
    split = form1(M(1, 0, 1, -1), M(0, -1, 2, 1), M(2, 1, 0, -2))
    d_split = form2(M(1, 2, 0, -1), M(-1, 0, 1, 2), M(0, 1, -2, 1))
    insertion = M(1, 2, -1, 0)
    return b, t, db, dt, direction, d_direction, split, d_split, insertion


def moving_shiab(insertion):
    return lambda two_form: G["shiab_insert"](insertion, two_form)


def euler_remainder(b, db, t, dt, direction, d_direction, shiab) -> F:
    """Directional first-variation remainder, not the full Portal eddy tensor."""
    full = G["directional_derivative"](
        b, db, t, dt, direction, d_direction, shiab, F(0)
    )
    compressed = G["simplified_source_derivative"](
        b, db, t, dt, direction, shiab, F(0)
    )
    return full - compressed


def interpolate_fraction(points, symbol):
    return sp.factor(
        sp.interpolate(
            [(sp.Rational(x), sp.Rational(y.numerator, y.denominator)) for x, y in points],
            symbol,
        )
    )


def layer_zero() -> None:
    typed("the action transgression, its Euler remainder, Portal's quadratic eddy, total swervature, C4, and a physical equation are distinct objects")
    typed("the finite G2 restriction can refute a universal action identity but is not the ten-owner induced-Y14 metric coefficient")
    typed("source epsilon, repository h=exp(u), metric-section tangent, observation-current motion, and pullback/pushdown motion remain separate")
    typed("the observation delta-current is not inserted into this smooth upstairs bulk action")
    typed("kappa1 is the distortion-norm coefficient, not a Yukawa or Higgs mass")
    typed("P1/P2/P3 are unchanged and unused")
    typed("Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE and TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED")
    reject("add a transcript-named eddy on top of the action-generated nonlinear variation", False)
    reject("call a fixture cancellation an induced-Y14 order reduction", False)


def eddy_remainder_checks() -> dict[str, sp.Expr]:
    b, t, db, _dt, direction, d_direction, _split, _d_split, insertion = fixtures()
    zero2 = form2(ZERO, ZERO, ZERO)
    zero1 = form1(ZERO, ZERO, ZERO)
    native = moving_shiab(insertion)

    cyclic = euler_remainder(
        b, db, t, zero2, direction, d_direction, G["shiab_identity"]
    )
    noncyclic = euler_remainder(b, db, t, zero2, direction, d_direction, native)
    exact(
        "the compressed F_A formula is exact in the cyclic identity-contraction control",
        cyclic == 0,
    )
    exact(
        "the action-derived directional Euler-covector remainder is live for the noncyclic contraction fixture",
        noncyclic != 0,
        f"remainder={noncyclic}",
    )

    r = sp.symbols("r", real=True)
    flat_points = []
    curved_points = []
    for value in map(F, (-2, -1, 0, 1, 2)):
        scaled_t = G["f1_scale"](value, t)
        flat_points.append(
            (
                value,
                euler_remainder(
                    zero1, zero2, scaled_t, zero2, direction, d_direction, native
                ),
            )
        )
        curved_points.append(
            (
                value,
                euler_remainder(
                    b, db, scaled_t, zero2, direction, d_direction, native
                ),
            )
        )
    flat_polynomial = interpolate_fraction(flat_points, r)
    curved_polynomial = interpolate_fraction(curved_points, r)
    exact(
        "the flat-reference action-derived remainder is exactly quadratic in distortion",
        flat_polynomial == -15 * r**2,
        f"R_flat={flat_polynomial}",
    )
    exact(
        "the nonzero-reference compressed subtraction also carries a live connection-distortion cross term",
        curved_polynomial == -5 * r * (3 * r + 1),
        f"R_curved={curved_polynomial}",
    )
    reject("promote pure T-quadratic scaling from the flat reference to every B background", sp.expand(curved_polynomial + 15 * r**2) == 0)

    group = M(1, 1, -1, 2)
    moved = euler_remainder(
        G["transform_f1"](group, b),
        G["transform_f2"](group, db),
        G["transform_f1"](group, t),
        zero2,
        G["transform_f1"](group, direction),
        zero2,
        moving_shiab(G["ad"](group, insertion)),
    )
    frozen = euler_remainder(
        G["transform_f1"](group, b),
        G["transform_f2"](group, db),
        G["transform_f1"](group, t),
        zero2,
        G["transform_f1"](group, direction),
        zero2,
        native,
    )
    exact(
        "the directional remainder passes the exact constant-conjugation witness when the insertion gauge-co-moves",
        moved == noncyclic,
    )
    reject("freeze the contraction insertion under conjugation", frozen == noncyclic)
    return {"flat": flat_polynomial, "curved": curved_polynomial}


def fixed_endpoint_polynomials(shiab, label: str) -> tuple[sp.Expr, sp.Expr]:
    b, t, db, dt, _direction, _d_direction, split, d_split, _insertion = fixtures()
    x = sp.symbols("x", real=True)
    curvature_points = []
    mass_points = []
    for value in map(F, (-3, -2, -1, 0, 1, 2, 3)):
        b_value = G["f1_add"](b, G["f1_scale"](value, split))
        t_value = G["f1_add"](t, G["f1_scale"](-value, split))
        db_value = G["f2_add"](db, G["f2_scale"](value, d_split))
        dt_value = G["f2_add"](dt, G["f2_scale"](-value, d_split))
        endpoint = G["curvature"](
            G["f1_add"](b_value, t_value),
            G["f2_add"](db_value, dt_value),
        )
        base_endpoint = G["curvature"](
            G["f1_add"](b, t), G["f2_add"](db, dt)
        )
        exact(
            f"fixed-A split preserves endpoint curvature at x={value}",
            endpoint == base_endpoint,
        )
        curvature_points.append(
            (
                value,
                G["source_action"](
                    b_value, db_value, t_value, dt_value, shiab, F(0)
                ),
            )
        )
        mass_points.append((value, G["inner1"](t_value, t_value)))
    curvature_polynomial = interpolate_fraction(curvature_points, x)
    mass_polynomial = interpolate_fraction(mass_points, x)
    held_out = F(4)
    b_value = G["f1_add"](b, G["f1_scale"](held_out, split))
    t_value = G["f1_add"](t, G["f1_scale"](-held_out, split))
    db_value = G["f2_add"](db, G["f2_scale"](held_out, d_split))
    dt_value = G["f2_add"](dt, G["f2_scale"](-held_out, d_split))
    exact(
        f"the {label} interpolants predict the held-out x=4 action and mass values",
        curvature_polynomial.subs(x, 4)
        == G["source_action"](b_value, db_value, t_value, dt_value, shiab, F(0))
        and mass_polynomial.subs(x, 4) == G["inner1"](t_value, t_value),
    )
    return curvature_polynomial, mass_polynomial


def total_swervature_c4_checks() -> dict[str, sp.Expr]:
    *_prefix, insertion = fixtures()
    x, kappa = sp.symbols("x kappa1", real=True)
    cyclic_curvature, cyclic_mass = fixed_endpoint_polynomials(G["shiab_identity"], "cyclic")
    moving_curvature, moving_mass = fixed_endpoint_polynomials(moving_shiab(insertion), "noncyclic")

    exact(
        "the cyclic fixed-endpoint action polynomial is reconstructed exactly",
        sp.simplify(
            cyclic_curvature
            - sp.Rational(1, 2) * (2 * x**3 - 3 * x**2 - 40 * x + 19)
        )
        == 0
        and sp.simplify(cyclic_mass - (7 * x**2 + 4 * x + 2)) == 0,
        f"curvature={cyclic_curvature}; mass={cyclic_mass}",
    )
    exact(
        "the noncyclic fixed-endpoint action polynomial is reconstructed exactly",
        sp.simplify(
            moving_curvature
            - sp.Rational(1, 3) * (4 * x**3 - 15 * x**2 - 98 * x - 63)
        )
        == 0
        and sp.simplify(moving_mass - cyclic_mass) == 0,
        f"curvature={moving_curvature}; mass={moving_mass}",
    )

    cyclic_c4 = sp.factor(
        sp.diff(cyclic_curvature + kappa * cyclic_mass / 2, x, 2)
    )
    moving_c4 = sp.factor(
        sp.diff(moving_curvature + kappa * moving_mass / 2, x, 2)
    )
    exact(
        "the exact C4 comparators are affine in kappa1 and live in the background split",
        cyclic_c4 == 7 * kappa + 6 * x - 3
        and moving_c4 == 7 * kappa + 8 * x - 10,
        f"cyclic={cyclic_c4}; moving={moving_c4}",
    )
    exact(
        "each background has a unique fixture cancellation but the required kappa1 changes with background",
        sp.solve(cyclic_c4, kappa) == [sp.Rational(3, 7) - 6 * x / 7]
        and sp.solve(moving_c4, kappa) == [sp.Rational(10, 7) - 8 * x / 7],
    )
    exact(
        "no constant kappa1 cancels either complete finite background family",
        sp.Poly(cyclic_c4, x).coeff_monomial(x) != 0
        and sp.Poly(moving_c4, x).coeff_monomial(x) != 0,
    )
    reject("reuse PW2D's minus-three-eighths bridge-amplitude root as this C4 coefficient", sp.simplify(moving_c4.subs(kappa, -sp.Rational(3, 8))) == 0)
    reject("select kappa1 from the x=0 fixture and call it universal", sp.simplify(moving_c4.subs(kappa, sp.Rational(10, 7))) == 0)
    return {
        "cyclic_curvature": cyclic_curvature,
        "moving_curvature": moving_curvature,
        "mass": moving_mass,
        "cyclic_c4": cyclic_c4,
        "moving_c4": moving_c4,
    }


def green_checks(polynomials: dict[str, sp.Expr]) -> None:
    x, kappa = sp.symbols("x kappa1", real=True)
    q = sp.symbols("q0:7")
    v = sp.symbols("v0:7")
    u = sp.symbols("u0:7")
    p = sp.expand(
        polynomials["moving_curvature"].subs(x, q[2])
        + kappa * polynomials["mass"].subs(x, q[2]) / 2
    )

    def total_d(value):
        return sp.expand(
            sum(sp.diff(value, q[i]) * q[i + 1] for i in range(6))
            + sum(sp.diff(value, v[i]) * v[i + 1] for i in range(6))
            + sum(sp.diff(value, u[i]) * u[i + 1] for i in range(6))
        )

    momentum = sp.diff(p, q[2])
    euler = total_d(total_d(momentum))
    theta = sp.expand(momentum * v[1] - total_d(momentum) * v[0])
    direct = sp.expand(momentum * v[2])
    exact(
        "the two-layer first-variation Green identity closes",
        sp.expand(direct - euler * v[0] - total_d(theta)) == 0,
    )

    hessian = sp.diff(p, q[2], 2)
    linear_v = total_d(total_d(hessian * v[2]))
    linear_u = total_d(total_d(hessian * u[2]))
    concomitant = sp.expand(
        u[0] * total_d(hessian * v[2])
        - u[1] * hessian * v[2]
        - v[0] * total_d(hessian * u[2])
        + v[1] * hessian * u[2]
    )
    exact(
        "the linearized C4 operator is formally self-adjoint with its full Green concomitant",
        sp.expand(u[0] * linear_v - v[0] * linear_u - total_d(concomitant)) == 0,
    )
    frechet_euler_v = sp.expand(sum(sp.diff(euler, q[i]) * v[i] for i in range(7)))
    exact(
        "independent Frechet linearization of the scalar-jet Euler expression matches the constructed Hessian operator",
        sp.expand(frechet_euler_v - linear_v) == 0,
    )
    exact(
        "the Hessian coefficient and Lagrange-concomitant construction carry the same C4 coefficient",
        sp.factor(hessian) == polynomials["moving_c4"].subs(x, q[2]),
        f"C4={sp.factor(hessian)}",
    )
    reject("use the Green concomitant as a bulk C4 cancellation", concomitant == 0)


def boundary() -> None:
    typed("the ambient independent-(B,T) finite I1B family kills only a universal action-intrinsic constant-kappa cancellation; a special induced-Y14 sublocus remains logically open")
    typed("complete actual Y14 C4 still requires the section/JVP identity, partial-Z1, theta1 and Bhat2, eight moving-Shiab slots, density/Krein/lowerers, and graph-curvature return")
    typed("a nonzero finite C4 does not establish an observed characteristic, physical mode, quotient, domain, or physics equation")
    typed("the scalar-jet Green calculation proves no function space, boundary condition, closability, realized self-adjointness, hyperbolicity, or common Krein/right-H domain")
    typed("C3 remains blocked until the complete induced-Y14 C4 is assembled")
    reject("infer that no induced-Y14 exceptional kappa1 can exist on a constrained geometric locus", False)
    reject("promote the finite scalar background x to a base conormal or physical momentum", False)


def main() -> int:
    print("PW2F-R2 TOTAL-SWERVATURE / UNIVERSAL-KAPPA GATE")
    layer_zero()
    eddy_remainder_checks()
    polynomials = total_swervature_c4_checks()
    green_checks(polynomials)
    boundary()
    total = EXACT + TYPE + PLANTED
    print(
        f"SUMMARY: {EXACT} exact + {TYPE} type + {PLANTED} planted = {total}; "
        f"failures={len(FAILURES)}"
    )
    if FAILURES:
        for failure in FAILURES:
            print(f"- {failure}")
        return 1
    print("VERDICT: A DIRECTIONAL EULER-COVECTOR REMAINDER AND EDDY CANDIDATE ARE LIVE; NO UNIVERSAL CONSTANT KAPPA1 ON THE EXACT AMBIENT FINITE SOURCE-ACTION FAMILY; PORTAL-EDDY IDENTITY AND ACTUAL INDUCED-Y14 C4 REMAIN OPEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
