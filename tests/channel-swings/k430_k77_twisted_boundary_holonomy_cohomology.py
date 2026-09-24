#!/usr/bin/env python3
"""K430 exact twisted-boundary cohomology for the K429 covariant derivative."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction as F

from k429_k77_covariant_incoming_domain_green import I2, U_at, matmul, matvec, transpose, vector_add, zero_vector


J = [[F(0), F(-1)], [F(1), F(0)]]
U0 = U_at(F(0))
U1 = U_at(F(1))


def det2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def sub2(left, right):
    return [[left[i][j] - right[i][j] for j in range(2)] for i in range(2)]


def inverse2(matrix):
    determinant = det2(matrix)
    assert determinant != 0
    return [[matrix[1][1] / determinant, -matrix[0][1] / determinant], [-matrix[1][0] / determinant, matrix[0][0] / determinant]]


def rank2(matrix):
    if det2(matrix) != 0:
        return 2
    if any(entry != 0 for row in matrix for entry in row):
        return 1
    return 0


def matrix_strings(matrix):
    return [[str(entry) for entry in row] for row in matrix]


def boundary_case(name: str, twist):
    relative_twist = matmul(matmul(transpose(U1), twist), U0)
    boundary_matrix = sub2(relative_twist, I2)
    nullity = 2 - rank2(boundary_matrix)
    return {
        "name": name,
        "twist": matrix_strings(twist),
        "relative_twist": matrix_strings(relative_twist),
        "boundary_matrix_determinant": str(det2(boundary_matrix)),
        "kernel_dimension": nullity,
        "cokernel_dimension": nullity,
        "fredholm_index": 0,
        "bounded_green_exists": nullity == 0,
    }


def primitive_g_at(x: F):
    return [x + x * x / 2, 2 * x - x * x / 2]


def verify_invertible_green() -> bool:
    relative_twist = matmul(transpose(U1), I2)
    boundary_matrix = sub2(relative_twist, I2)
    total = primitive_g_at(F(1))
    c = matvec(inverse2(boundary_matrix), total)
    u0 = matvec(U0, c)
    u1 = matvec(U1, vector_add(c, total))
    return zero_vector([u1[i] - u0[i] for i in range(2)])


def demo() -> dict:
    identity_twist = boundary_case("identity_boundary_twist", I2)
    transported_twist = boundary_case("connection_monodromy_twist", J)
    assert U0 == I2 and U1 == J and verify_invertible_green()
    assert identity_twist["kernel_dimension"] == 0
    assert transported_twist["kernel_dimension"] == 2
    return {
        "schema_version": "1.0",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "native_to_native",
        "operator": "K429 D_A on H1([0,1],R2)",
        "boundary_family": {
            "condition": "u(1)=R u(0), R orthogonal",
            "gauge_reduced_condition": "v(1)=S v(0), S=U(1)^T R U(0)",
            "kernel": "Fix(S)",
            "cokernel": "Fix(S^T), hence the same dimension",
            "fredholm_index": 0,
            "range_condition": "integral_0^1 U(s)^T f(s) ds lies in range(S-I)",
            "green_when_invertible": "v(t)=(S-I)^-1 integral_0^1 g + integral_0^t g",
        },
        "exact_cases": {
            "identity_twist": identity_twist,
            "transported_twist": transported_twist,
            "invertible_green_boundary_replayed": verify_invertible_green(),
        },
        "decision": {
            "same_variable_differential_has_boundary_dependent_cohomology": True,
            "identity_twist_is_invertible_for_quarter_turn_monodromy": True,
            "monodromy_matched_twist_has_kernel_and_cokernel_dimension": 2,
            "boundary_condition_is_source_selected": False,
            "physical_bfv_cohomology_constructed": False,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    if not args.demo:
        parser.error("use --demo")
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
