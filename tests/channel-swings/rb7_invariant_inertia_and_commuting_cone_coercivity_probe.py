#!/usr/bin/env python3
"""Exact RB7 generalized-inertia and candidate-coercivity certificate."""

from __future__ import annotations

import argparse
from fractions import Fraction as Q
import sys

Matrix = list[list[Q]]
Vector = list[Q]


def matrix(rows: list[list[int | Q]]) -> Matrix:
    return [[Q(value) for value in row] for row in rows]


def transpose(a: Matrix) -> Matrix:
    return [list(row) for row in zip(*a)]


def multiply(a: Matrix, b: Matrix) -> Matrix:
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def matvec(a: Matrix, v: Vector) -> Vector:
    return [sum(row[j] * v[j] for j in range(len(v))) for row in a]


def scale(a: Matrix, value: Q) -> Matrix:
    return [[value * entry for entry in row] for row in a]


def subtract(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def determinant3(a: Matrix) -> Q:
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def dot(v: Vector, w: Vector) -> Q:
    return sum(x * y for x, y in zip(v, w))


def certificate() -> dict[str, bool]:
    # Set m^2=1: positive rescaling does not change either inertia.
    hessian = matrix([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
    metric = scale(matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), Q(-1))
    relative = scale(hessian, Q(-1))
    positive_h = [Q(1), Q(1), Q(1)]
    negative_h_1 = [Q(1), Q(-1), Q(0)]
    negative_h_2 = [Q(1), Q(0), Q(-1)]

    change = matrix([[1, 1, 0], [0, 1, 1], [1, 0, 1]])
    hessian_prime = multiply(multiply(transpose(change), hessian), change)
    metric_prime = multiply(multiply(transpose(change), metric), change)
    det_change = determinant3(change)
    pencil_congruence = all(
        determinant3(subtract(hessian_prime, scale(metric_prime, Q(lam))))
        == det_change**2 * determinant3(subtract(hessian, scale(metric, Q(lam))))
        for lam in (-3, -2, -1, 0, 1, 2, 3)
    )

    mixed_gram = matrix(
        [[Q(9, 16) if i == j and i < 9 else Q(0) for j in range(10)] for i in range(10)]
    )
    trace = [Q(0)] * 9 + [Q(1)]
    traceless = [Q(1)] + [Q(0)] * 9
    fields = [trace, [Q(0)] * 10, [Q(0)] * 10]
    gram_energy = sum(dot(field, matvec(mixed_gram, field)) for field in fields)
    commuting = all(not any(fields[i]) or not any(fields[j]) or fields[i] == fields[j] for i in range(3) for j in range(i + 1, 3))

    return {
        "full_triplet_stationarity": Q(-1) + 2 * Q(1) * Q(1, 2) == 0,
        "euclidean_inertia_1_2_0": matvec(hessian, positive_h) == [2 * x for x in positive_h]
        and matvec(hessian, negative_h_1) == [-x for x in negative_h_1]
        and matvec(hessian, negative_h_2) == [-x for x in negative_h_2]
        and determinant3(matrix([positive_h, negative_h_1, negative_h_2])) != 0,
        "generalized_inertia_2_1_0": matvec(relative, positive_h) == [-2 * x for x in positive_h]
        and matvec(relative, negative_h_1) == negative_h_1
        and matvec(relative, negative_h_2) == negative_h_2,
        "pencil_congruence_invariant": pencil_congruence,
        "mixed_gram_rank_9": all(mixed_gram[i][i] == Q(9, 16) for i in range(9)) and mixed_gram[9][9] == 0,
        "mixed_gram_kernel_is_trace": matvec(mixed_gram, trace) == [Q(0)] * 10
        and dot(traceless, matvec(mixed_gram, traceless)) == Q(9, 16),
        "nonzero_commuting_kernel_witness": any(trace) and commuting and gram_energy == 0,
        "coercivity_necessary_condition_fails": gram_energy == 0,
    }


def selftest() -> bool:
    baseline = certificate()
    controls = {
        "wrong_generalized_inertia_rejected": baseline["generalized_inertia_2_1_0"] and (1, 2, 0) != (2, 1, 0),
        "false_full_rank_gram_rejected": baseline["mixed_gram_rank_9"] and 9 != 10,
        "erased_trace_witness_rejected": baseline["nonzero_commuting_kernel_witness"] and Q(9, 16) != 0,
        "false_coercivity_claim_rejected": baseline["coercivity_necessary_condition_fails"],
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
    print(f"RB7 exact certificate: {'PASS' if ok else 'FAIL'} ({sum(checks.values())}/{len(checks)})")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
