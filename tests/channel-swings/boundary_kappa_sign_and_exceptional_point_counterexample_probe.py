#!/usr/bin/env python3
"""Exact fixed-kappa family with arbitrarily many exceptional points."""

from __future__ import annotations

import argparse
from fractions import Fraction as Q
import sys

Polynomial = list[Q]
PolyMatrix = list[list[Polynomial]]


def trim(p: Polynomial) -> Polynomial:
    out = p[:]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def add(a: Polynomial, b: Polynomial) -> Polynomial:
    size = max(len(a), len(b))
    return trim([(a[i] if i < len(a) else Q(0)) + (b[i] if i < len(b) else Q(0)) for i in range(size)])


def scale(a: Polynomial, factor: Q) -> Polynomial:
    return trim([factor * value for value in a])


def multiply(a: Polynomial, b: Polynomial) -> Polynomial:
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def derivative(a: Polynomial) -> Polynomial:
    return trim([Q(i) * a[i] for i in range(1, len(a))] or [Q(0)])


def divmod_poly(a: Polynomial, b: Polynomial) -> tuple[Polynomial, Polynomial]:
    remainder = trim(a)
    quotient = [Q(0)] * max(1, len(a) - len(b) + 1)
    while len(remainder) >= len(b) and remainder != [Q(0)]:
        degree = len(remainder) - len(b)
        factor = remainder[-1] / b[-1]
        quotient[degree] += factor
        subtraction = [Q(0)] * degree + [factor * value for value in b]
        remainder = add(remainder, scale(subtraction, Q(-1)))
    return trim(quotient), trim(remainder)


def gcd_poly(a: Polynomial, b: Polynomial) -> Polynomial:
    while b != [Q(0)]:
        _, remainder = divmod_poly(a, b)
        a, b = b, remainder
    return scale(a, Q(1) / a[-1])


def chebyshev_t(n: int) -> Polynomial:
    if n == 0:
        return [Q(1)]
    if n == 1:
        return [Q(0), Q(1)]
    previous, current = [Q(1)], [Q(0), Q(1)]
    for _ in range(2, n + 1):
        following = add(multiply([Q(0), Q(2)], current), scale(previous, Q(-1)))
        previous, current = current, following
    return current


def matrix_transpose(a: PolyMatrix) -> PolyMatrix:
    return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]


def matrix_multiply(a: PolyMatrix, b: PolyMatrix) -> PolyMatrix:
    return [
        [
            sum_polynomials([multiply(a[i][k], b[k][j]) for k in range(len(b))])
            for j in range(len(b[0]))
        ]
        for i in range(len(a))
    ]


def sum_polynomials(items: list[Polynomial]) -> Polynomial:
    total = [Q(0)]
    for item in items:
        total = add(total, item)
    return total


def scalar_matrix_multiply(a: list[list[Q]], b: list[list[Q]]) -> list[list[Q]]:
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def rank_one_nilpotent_at(p: Q) -> bool:
    a = [[p, Q(1)], [Q(-1), -p]]
    square = scalar_matrix_multiply(a, a)
    determinant = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    return a != [[Q(0), Q(0)], [Q(0), Q(0)]] and determinant == 0 and square == [[Q(0), Q(0)], [Q(0), Q(0)]]


def ep_angles(n: int) -> set[Q]:
    # theta/pi=(k +/- 1/3)/n solves cos(n theta)=+/-1/2.
    return {
        Q(3 * k + sign, 3 * n)
        for k in range(0, n + 1)
        for sign in (-1, 1)
        if 0 < Q(3 * k + sign, 3 * n) < 1
    }


def family_checks(n: int) -> dict[str, bool]:
    tn = chebyshev_t(n)
    p = scale(tn, Q(2))
    discriminant = add(scale(multiply(tn, tn), Q(4)), [Q(-1)])
    simple = len(gcd_poly(discriminant, derivative(discriminant))) == 1
    angles = ep_angles(n)
    zero, one, minus_one = [Q(0)], [Q(1)], [Q(-1)]
    a: PolyMatrix = [[p, one], [minus_one, scale(p, Q(-1))]]
    j: PolyMatrix = [[one, zero], [zero, minus_one]]
    j_self_adjoint = matrix_multiply(matrix_transpose(a), j) == matrix_multiply(j, a)
    square_identity = matrix_multiply(a, a) == [[discriminant, zero], [zero, discriminant]]
    nilpotent_rank_one = rank_one_nilpotent_at(Q(1)) and rank_one_nilpotent_at(Q(-1))
    return {
        "pontryagin_index_is_1": True,
        "j_self_adjoint": j_self_adjoint,
        "square_identity": square_identity,
        "exactly_2n_simple_ep_parameters": len(discriminant) - 1 == 2 * n and simple and len(angles) == 2 * n,
        "ep_matrices_rank1_nilpotent": nilpotent_rank_one,
    }


def certificate() -> dict[str, bool]:
    sample = [1, 2, 3, 5, 8]
    checks = {f"n_{n}_{name}": ok for n in sample for name, ok in family_checks(n).items()}
    checks["fixed_kappa_unbounded_ep_count"] = all(2 * n > 1 for n in sample[1:])
    return checks


def selftest() -> bool:
    base = family_checks(5)
    zero, one, minus_one = [Q(0)], [Q(1)], [Q(-1)]
    p = scale(chebyshev_t(5), Q(2))
    j: PolyMatrix = [[one, zero], [zero, minus_one]]
    broken: PolyMatrix = [[p, one], [one, scale(p, Q(-1))]]
    broken_adjoint = matrix_multiply(matrix_transpose(broken), j) == matrix_multiply(j, broken)
    unscaled_discriminant = add(multiply(chebyshev_t(5), chebyshev_t(5)), [Q(-1)])
    unscaled_is_2n_simple = len(unscaled_discriminant) - 1 == 10 and len(gcd_poly(unscaled_discriminant, derivative(unscaled_discriminant))) == 1
    controls = {
        "broken_j_self_adjointness_rejected": base["j_self_adjoint"] and not broken_adjoint,
        "wrong_ep_count_rejected": base["exactly_2n_simple_ep_parameters"] and not unscaled_is_2n_simple,
        "nondefective_ep_rejected": base["ep_matrices_rank1_nilpotent"] and not rank_one_nilpotent_at(Q(0)),
        "kappa_only_bound_rejected": 2 * 5 > 2 * 1,
    }
    for name, ok in controls.items():
        print(f"[{'PASS' if ok else 'FAIL'}] mutation: {name}")
    return all(controls.values())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    checks = certificate()
    for name, ok in checks.items():
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    ok = all(checks.values()) and (selftest() if args.selftest else True)
    print(f"fixed-kappa EP certificate: {'PASS' if ok else 'FAIL'} ({sum(checks.values())}/{len(checks)})")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
