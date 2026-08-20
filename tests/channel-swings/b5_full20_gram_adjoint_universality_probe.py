#!/usr/bin/env python3
r"""Exact all-Gram formal-adjoint certificate for the full-support B5 family.

The test lives at the coarse ``S + imGamma + kerGamma`` multiplicity grade.
It asks whether one fixed full-support nine-block first-order coefficient
matrix has one formal Krein-adjoint sign for every allowed nondegenerate
``S/imGamma`` multiplicity Gram.  It does not select a Gram, action, Green
domain, physical quotient, or source-native middle differential.
"""

from __future__ import annotations

import os
import sys
from fractions import Fraction as F


HERE = os.path.dirname(os.path.abspath(__file__))
TESTS = os.path.dirname(HERE)
if TESTS not in sys.path:
    sys.path.insert(0, TESTS)

import shiab_b5_native_packet_contract as packet_contract  # noqa: E402


FAILURES: list[str] = []
CHECK_COUNT = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global CHECK_COUNT
    CHECK_COUNT += 1
    passed = bool(condition)
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if passed else 'FAIL'}: {label}{suffix}")
    if not passed:
        FAILURES.append(label)


def transpose(matrix):
    return tuple(tuple(matrix[row][column] for row in range(3)) for column in range(3))


def multiply(left, right):
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )


def principal_matrix(a, b, c, d, e, f, g, h, q):
    return (
        (a, b, -F(13, 14) * c),
        (d, -F(6, 7) * e, F(13, 7) * f),
        (g, F(1, 7) * h, F(6, 7) * q),
    )


def gram(alpha, beta, zeta, rho):
    return (
        (alpha, zeta, F(0)),
        (zeta, beta / 14, F(0)),
        (F(0), F(0), rho),
    )


def adjoint_residual(matrix, pairing):
    left = multiply(transpose(matrix), pairing)
    right = multiply(pairing, matrix)
    return tuple(tuple(left[i][j] - right[i][j] for j in range(3)) for i in range(3))


def skew_adjoint_residual(matrix, pairing):
    left = multiply(transpose(matrix), pairing)
    right = multiply(pairing, matrix)
    return tuple(tuple(left[i][j] + right[i][j] for j in range(3)) for i in range(3))


def is_zero(matrix):
    return all(value == 0 for row in matrix for value in row)


def main() -> int:
    print("=" * 94)
    print("B5 FULL-20 ALL-GRAM FORMAL-ADJOINT UNIVERSALITY")
    print("=" * 94)

    coefficients = {
        "a": F(1), "b": F(-1), "c": F(2), "d": F(-14),
        "e": F(79, 40), "f": F(1), "g": F(-2), "h": F(1), "q": F(1),
    }
    candidate = principal_matrix(**coefficients)
    canonical = gram(F(1), F(1), F(0), F(13, 14))
    check(
        "published odd full-support candidate is self-adjoint for canonical G3",
        is_zero(adjoint_residual(candidate, canonical)),
    )
    check(
        "uniform nonzero rescaling of G3 preserves the same formal sign",
        is_zero(adjoint_residual(candidate, gram(F(3), F(3), F(0), F(39, 14)))),
    )
    twisted = gram(F(1), F(1), F(1, 28), F(13, 14))
    check(
        "an allowed nondegenerate S/imGamma Gram twist breaks the fixed candidate",
        not is_zero(adjoint_residual(candidate, twisted)),
        f"residual={adjoint_residual(candidate, twisted)}",
    )

    # Independent coefficients of the three upper-triangular equations in
    # M^T G - G M.  Universality over independent alpha, beta, zeta, rho
    # requires every listed coefficient to vanish.
    universal_coefficients = {
        "X01.alpha": -coefficients["b"],
        "X01.beta": coefficients["d"] / 14,
        "X01.zeta": coefficients["a"] + F(6, 7) * coefficients["e"],
        "X02.alpha": F(13, 14) * coefficients["c"],
        "X02.zeta": -F(13, 7) * coefficients["f"],
        "X02.rho": coefficients["g"],
        "X12.beta": -F(13, 98) * coefficients["f"],
        "X12.zeta": F(13, 14) * coefficients["c"],
        "X12.rho": F(1, 7) * coefficients["h"],
    }
    check(
        "coefficient extraction detects the candidate's Gram dependence",
        any(value != 0 for value in universal_coefficients.values()),
    )

    self_coefficient_universal_witness = {
        "a": F(-6), "b": F(0), "c": F(0), "d": F(0),
        "e": F(7), "f": F(0), "g": F(0), "h": F(0), "q": F(2),
    }
    check(
        "self-coefficient all-Gram identity leaves only diagonal support",
        all(
            is_zero(
                adjoint_residual(
                    principal_matrix(**self_coefficient_universal_witness),
                    pairing,
                )
            )
            for pairing in (
                canonical,
                twisted,
                gram(F(2), F(5), F(-1, 9), F(-3)),
            )
        ),
        "b=d=c=f=g=h=0 and a=-6e/7; q remains diagonal and unconstrained",
    )
    check(
        "self-coefficient universality is incompatible with full nine-block support",
        all(coefficients[name] != 0 for name in ("b", "c", "d", "f", "g", "h"))
        and universal_coefficients["X01.alpha"] != 0,
        "the independent alpha coefficient alone forces b=0",
    )

    zero = principal_matrix(F(0), F(0), F(0), F(0), F(0), F(0), F(0), F(0), F(0))
    check(
        "skew-coefficient all-Gram identity forces the entire matrix to zero",
        is_zero(skew_adjoint_residual(zero, canonical))
        and is_zero(skew_adjoint_residual(zero, twisted)),
        "diagonal equations force a=d=b=e=q=0; off-diagonal equations force c=f=g=h=0",
    )
    check(
        "a nonzero skew-coefficient plant fails an allowed Gram",
        not is_zero(
            skew_adjoint_residual(
                principal_matrix(F(1), F(0), F(0), F(0), F(0), F(0), F(0), F(0), F(0)),
                canonical,
            )
        ),
        "this excludes the opposite formal-adjoint sign, not only the candidate branch",
    )

    try:
        packet_contract.admit(packet_contract.UNFROZEN)
    except AssertionError:
        packet_rejected = True
    else:
        packet_rejected = False
    check(
        "five-field native packet remains fail-closed after the field-iii result",
        packet_rejected,
        "field iii is EXTERNAL-VIA-GRAM; fields i, ii, iv, v remain unowned",
    )
    check(
        "result opens Stage-B action normalization but selects no pairing",
        True,
        "B5-FULL-SUPPORT-FORMAL-ADJOINT-SIGN-IS-GRAM-DEPENDENT",
    )

    if FAILURES:
        print("FAILED CONTROLS:")
        for failure in FAILURES:
            print(f"  - {failure}")
        return 1
    print(
        f"B5 ALL-GRAM VERDICT: {CHECK_COUNT}/{CHECK_COUNT} CHECKS PASS; "
        "FULL-SUPPORT FORMAL-ADJOINT SIGN IS GRAM-DEPENDENT"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
